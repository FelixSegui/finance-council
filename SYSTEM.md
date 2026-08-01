# Finance Council — System Architecture

Personal investment advisory system. Runs locally via Claude Code. No brokerage
integration — you are the human-in-the-loop for every action. This system
produces analysis and flags; it never executes trades.

This file replaces `CLAUDE.md` as of the 2026-08-01 migration to a local,
Excel-backed project. The investment logic below is unchanged from before the
migration — what changed is *where things live* and *how state flows*.

## Design philosophy — read before extending anything

**One canonical owner for every piece of information.** If the same fact
exists in two places, the architecture is wrong. Concretely:

| Kind of information | Owner | Format |
|---|---|---|
| Holdings, transactions, watchlist, thesis notes, pending orders, settings, open questions | **Human** | `master.xlsx` |
| Market data, cached API responses, rankings, factor calculations, controller metrics | **Machine** | `data/cache/*.json`, `data/sync/*.json` |
| Sweep reports, investment memos, candidate research | **AI** | `reports/*.md` |

Reports never become the source of truth. A number in a report traces back to
`data/cache/` or `master.xlsx` — it is never itself where a number lives.

**Only `data/sync/sync.py` understands Excel.** No script, agent, or report
opens `master.xlsx` directly except through `sync.py`'s `read` / `write-cache`
/ `append` commands. This is what makes "master.xlsx is the source of truth"
an enforced property, not a convention people forget.

**The smallest system that works.** Prefer simple modules with clear
responsibilities over complex autonomous systems. Every module should be
understandable in isolation. `run.py` handles the deterministic (machine)
steps only — sync, fetch, coverage, controller metrics. It never calls an LLM.
Reasoning (valuation calls, thesis judgment, council synthesis) happens in a
live Claude Code session reading the `.claude/agents/lens-*.md` /
`core-*.md` files — exactly as before the migration, just from a
better-organized project.

**AI supports decisions, it does not replace process.** Its job is reasoning,
summarizing, finding opportunities, challenging assumptions, and highlighting
missing information. It never invents data — every numerical statement must
be traceable to fetched or locally stored data. This is the single biggest
risk in an LLM-based investment system: **confident structure built on stale
or hallucinated numbers.** If data wasn't fetched, the correct output is "no
data," never an estimate from training knowledge.

## Data sources (all free, no keys)

yfinance / Yahoo chart endpoint, CoinGecko, FRED, Riksbank SWEA, SCB PxWeb, ECB
Data Portal, alternative.me Fear & Greed, SEC EDGAR (Form 4 insider counts, US
tickers, `--insiders` flag), Finansinspektionen's Insynsregistret (Swedish
insider register — explored, not yet wired in, see the Notes sheet).

## Scope (Phase 1 — locked 2026-07-03)

Covered: **equities, ETFs/index funds, crypto**, with **macro (rates, yield
curve, inflation, dollar)** as regime context, not a tradeable asset class.

Explicitly out of scope until a paid data feed is added: individual bonds,
options, alternatives. Free data for these is either non-existent (bonds,
alts) or too thin to trust (options IV/skew). Do not let any agent generate
options or alts recommendations from scraped/free data — that is false
confidence, not analysis. If asked, agents should say so and stop.

## Priority order (Swedish retail context, ~200-250k SEK)

At this portfolio size, the return hierarchy is:
1. **Account wrapper efficiency** (ISK tax-free allowance vs taxed AF) —
   structural, certain, largest.
2. **Fee drag** (bank funds at 1%+ vs index at ~0.2%) — structural,
   certain, second largest.
3. **Allocation / drift** — controllable, probabilistic.
4. **Selection** (which stock/fund/coin) — smallest edge, most effort.

`lens-portfolio.md` owns 1-3. `lens-valuation.md`/`lens-thesis-review.md` own
4. Never let a sweep report lead with a stock pick while a wrapper
inefficiency or 1.5% fee sits unaddressed — that's optimizing the smallest
lever first.

Currencies: base currency is SEK. Equity data may arrive in USD/EUR; convert
using the `sek_per_usd` rate in the macro snapshot before computing weights.
Crypto certificates trade on Nasdaq Stockholm in SEK — fetch them as `.ST`
tickers, not via CoinGecko.

## Blocking questions rule

The **Notes sheet** in `master.xlsx` (synced to `data/sync/notes.json`) holds
open and resolved structural questions. While a `status: open` question is
flagged as blocking (a note whose text says so explicitly — e.g. a wrapper
question touching most of the portfolio), every sweep report must open with
it. Agents may still analyze the other accounts fully. Move a question's
status to `resolved` (don't delete the row) as it gets answered — the
resolution history is itself useful.

## The project structure

```
finance-council/
  README.md              # quick start — how to run a sweep
  SYSTEM.md               # this file
  master.xlsx              # the human-owned source of truth
  run.py                  # deterministic steps: sync, fetch, coverage, controller
  config/settings.py       # tunable constants (AI Council threshold, risk bands, etc.)
  .claude/agents/
    core-*.md               # orchestrating agents (journal, market-data, scout, council, controller)
    lens-*.md                # read-only analytical lenses (valuation, macro-regime, portfolio, thesis-review)
    util-*.md                 # optional/supplementary (calendar, backtest)
  scripts/                 # the fetch/compute logic — unchanged in spirit from before the migration
  data/
    cache/                   # machine-owned, reproducible, disposable (snapshots, rankings, screens, ...)
    sync/                     # data/sync/sync.py + the JSON files it produces from master.xlsx
  reports/                 # ONE reports/YYYY-MM-DD-sweep.md per sweep — nothing else
  archive/                 # everything superseded by the 2026-08-01 migration, kept for history
```

## Flow

The pipeline is unchanged from before the migration:

```
journal → market-data → scout (optional) → valuation → macro-regime
        → portfolio → thesis-review → council → sweep report
```

0. **Every session starts with `journal`** — it reads the most recent
   `reports/*-sweep.md` and reports where the last sweep left off, pending
   decisions, and open Notes-sheet items. No analysis before this runs.
1. Run `python run.py prep` (or let the `market-data` agent do it) — this
   chains `sync` (master.xlsx → `data/sync/*.json`), `fetch`
   (`scripts/fetch_market_data.py` → a timestamped snapshot in
   `data/cache/snapshots/`, plus `_MarketCache` in the workbook), and
   `coverage` (`scripts/generate_coverage_report.py` → a machine-readable
   coverage summary — the standing answer to "what data did this sweep
   actually get, and what's still missing").
2. Invoke `lens-valuation`, `lens-macro-regime`, `lens-portfolio`,
   `lens-thesis-review` — they read the synced data, never fetch themselves
   redundantly. Optional, when relevant: `core-scout` (new candidates),
   `util-calendar` (event collisions), `util-backtest` (risk profile of a
   proposed allocation).
3. Invoke `core-council` last. It reads all outputs plus the coverage summary
   and controller metrics, forces disagreements into the open, and writes
   ONE file: `reports/YYYY-MM-DD-sweep.md`.
4. **Every sweep ends with `journal`** — it reconciles last sweep's calls
   against today's data (recorded as a Notes-sheet row) and hands the lines
   to `council` for that sweep's report. An unlogged sweep is invisible to
   the next session.
5. Optionally invoke `core-controller` — it reviews how the system itself
   performed and maintains `data/cache/controller_state.json`'s
   recommendations.
6. You read the report. You decide. Nothing here executes anything.

## Time horizons

Every Council call carries a horizon tag. The system's edge shrinks as the
horizon shortens — weight effort accordingly:

- **Long (3y+)** — wrapper efficiency, fee drag, allocation. Owned by
  `lens-portfolio`. Highest edge, structural, this is where the money is.
- **Medium (6mo–3y)** — valuation entry/exit, thesis health, regime
  positioning. Owned by `lens-valuation` + `lens-thesis-review` +
  `lens-macro-regime`.
- **Short (<6mo)** — tactical overlay ONLY: capped at 10% of portfolio,
  never High confidence, always flagged as tactical in the report. LLMs on
  free data have no demonstrated short-term edge; the system says so rather
  than pretending otherwise.

## Session continuity

The most recent `reports/*-sweep.md` plus the Notes sheet ARE the system's
memory across sessions — `journal` reconciles previous calls against current
data (the only calibration mechanism this system has) and records the
reconciliation as a Notes row. `data/valuations.csv` accumulates portfolio
value observations for `scripts/performance.py` (are we beating "just buy the
index"?). If a session did meaningful work without a sweep report, that's a
process failure — fix it before ending the session.

Pre-migration history (the old `SESSION_LOG.md`, dated council memos,
`IMPROVEMENTS.md`) lives in `archive/reports-pre-migration/` — read once for
continuity on the first post-migration sweep, then treat `reports/*-sweep.md`
as the live record.

## Self-improvement

`core-controller` owns `data/cache/controller_state.json`'s `recommendations`
— evidence-backed proposals for changes to the system itself. It proposes,
never applies — the user applies by saying "apply recommendation #N".
Recurring bad calls (visible in reconciliation Notes rows) are a system
defect to be traced, not bad luck. This replaces the old standalone
`IMPROVEMENTS.md` file — see `archive/` for its history.

## Your portfolio state

`master.xlsx` is the source of truth — you maintain it manually (no brokerage
API), editing the Portfolio, Transactions, Pending Orders, Watchlist,
Investment Thesis, Settings, and Notes sheets directly, or via
`python data/sync/sync.py append` during a session. Run `python run.py sync`
whenever the workbook changes so `data/sync/*.json` (what every script and
agent actually reads) reflects it. Every agent treats the synced JSON, not
memory, as ground truth for what you hold.

The **Settings sheet** is the client profile — risk tolerance, the 60/30/10
tier split, horizon, buffer, constraints. It is what a human advisor would
establish first, and it is what turns `lens-portfolio`'s balance scorecard
from generic rules of thumb into advice measured against your situation.
Every sweep report carries the scorecard; missing Settings keys are named in
the report until filled.

## Council rule

`core-council`'s only job is adversarial synthesis. If two agents agree,
that's not interesting — the report should foreground *where they disagree*
and force an explicit confidence call. A report with no tension in it means
the Council didn't do its job; re-run it.
