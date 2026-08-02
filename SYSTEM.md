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
tickers), Finansinspektionen's Insynsregistret (Swedish insider register, real
buy/sell direction — richer than Form 4's count-only feed).

Each data KIND is its own independently runnable module — not one monolith —
so a broken source is isolated and debuggable on its own:

All fetchers live in `scripts/fetchers/` — one folder, so a broken source is
easy to find and target ("if I see something not working properly").

| Module | Data |
|---|---|
| `scripts/fetchers/fetch_prices.py` | equity/ETF prices |
| `scripts/fetchers/fetch_fundamentals_us.py` | equity fundamentals (US-listed only — no free source exists for non-US) |
| `scripts/fetchers/fetch_crypto_prices.py` | crypto prices |
| `scripts/fetchers/fetch_macro.py` | FRED / Riksbank / SCB / ECB |
| `scripts/fetchers/fetch_sentiment.py` | crypto Fear & Greed |
| `scripts/fetchers/fetch_insiders_us.py` | SEC Form 4 filing counts |
| `scripts/fetchers/fetch_insiders_se.py` | Finansinspektionen Insynsregistret (issuer-name search, one call per `.ST` stock holding) |
| `scripts/fetchers/fetch_calendar.py` | earnings dates + macro event calendar (used by `util-calendar`, not part of the standard snapshot) |

`scripts/fetchers/fetch_market_data.py` is a thin orchestrator that calls the first
five and assembles one combined snapshot (what the lenses read).
`python run.py fetch --only <kind>` runs exactly one module standalone —
use this when a specific source breaks instead of re-running everything.

**Standardized per-ticker records.** Every stock's data — price,
fundamentals, and now insider activity — lands in the SAME snapshot record
(`equities[ticker]`), regardless of which module fetched which field, so
every lens reads one place instead of knowing which side-file to check.
`run.py fetch`'s default sweep runs `fetch_insiders_us.py` (US holdings) and
`fetch_insiders_se.py` (`.ST` holdings, issuer name guessed from the
Portfolio sheet's `name` column) automatically and merges the result into
`equities[ticker]["insider_activity_us"/"_se"]` — it is standard sweep data,
not an opt-in extra. `lens-thesis-review.md` is the lens that reads and
reasons on it (insider buying/selling is thesis-support evidence, not a
valuation input).

**Currency conversion is now enforced in code, not just convention.** Every
`_MarketCache` record's `market_value_sek` is computed from this sweep's
fetched `sek_per_usd`/`sek_per_eur` macro rate — previously it silently
copied the raw price with no conversion, understating the Dashboard's
"Total value (SEK)" for every non-SEK holding (and showing `None`, i.e.
zero, for ethereum and any foreign-currency cash balance). If a rate is
missing this sweep, the record is tagged `(FX MISSING)` rather than
guessed as 1:1 — treat that as a real gap in the same sweep report, not a
silent omission.

## Manual data — filling what the automated fetch can't find

Some fields have no free source at all (non-US equity fundamentals — SEC
EDGAR is US-filer-only). The **Manual Data sheet** in `master.xlsx` is where
you supply them: `ticker, field, value, currency, as_of, source, notes`.

`python run.py fetch` applies these as a fallback — filling a field ONLY if
the automated fetch genuinely couldn't get it, NEVER overwriting a real
fetched value — and tags every filled field in the snapshot's
`_manual_overrides`, so a hand-entered number is never silently presented as
if it were live-fetched. `generate_coverage_report.py` lists the exact
missing field names per holding (not just a status word) specifically so you
know what to go find and enter.

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
    core-*.md               # orchestrating agents (journal, market-data, scout, council)
                              # council absorbed controller 2026-08-02 — see archive/
    lens-*.md                # read-only analytical lenses (valuation, macro-regime, portfolio, thesis-review)
    util-*.md                 # optional/supplementary (calendar, backtest)
  scripts/                 # the fetch/compute logic, grouped by role (2026-08-02 reorg)
    fetchers/                # one file per data KIND — price, fundamentals, crypto, macro,
                              # sentiment, US/SE insiders, calendar. Target one directly when
                              # a specific source breaks (`run.py fetch --only <kind>`).
    funnel/                  # the stock-discovery funnel: build_universe, rank_candidates,
                              # rank_crypto, screen_candidates (used by core-scout)
    generate_coverage_report.py, migrate_from_json.py, performance.py,
    backtest.py, add_manual_tickers.py   # standalone utilities, not part of either group above
  data/
    cache/                   # machine-owned, reproducible, disposable (snapshots, rankings, screens, ...)
    sync/                     # data/sync/sync.py + the JSON files it produces from master.xlsx
  reports/                 # ONE reports/YYYY-MM-DD-sweep.md per sweep — nothing else
  archive/                 # everything superseded by the 2026-08-01 migration, kept for history
```

## Flow

As of 2026-08-02, `core-controller` is merged into `core-council` (see
"Self-improvement" below) — one final "overall control" step instead of two
separately-invoked agents. This also fixes a real ordering bug from this
system's first live sweep (2026-08-02): journal's reconciliation needs to
exist BEFORE Council writes the report (Council's own report format folds
reconciliation into "Council conclusions"), but the old Flow ran journal's
reconciliation AFTER council — so the very first sweep's report had nothing
to fold in even though the format expected it. Journal now runs twice, both
before Council: once for session-start context, once for reconciliation.

```
journal (context) → market-data → scout (optional) → valuation → macro-regime
        → portfolio → thesis-review → journal (reconcile) → council → sweep report
```

0. **Every session starts with `journal`** — it reads the most recent
   `reports/*-sweep.md` and reports where the last sweep left off, pending
   decisions, and open Notes-sheet items. No analysis before this runs.
1. Run `python run.py prep` (or let the `market-data` agent do it) — this
   chains `sync` (master.xlsx → `data/sync/*.json`), `fetch`
   (`scripts/fetchers/fetch_market_data.py` → a timestamped snapshot in
   `data/cache/snapshots/`, plus `_MarketCache` in the workbook), and
   `coverage` (`scripts/generate_coverage_report.py` → a machine-readable
   coverage summary — the standing answer to "what data did this sweep
   actually get, and what's still missing").
2. Invoke `lens-valuation`, `lens-macro-regime`, `lens-portfolio`,
   `lens-thesis-review` — they read the synced data, never fetch themselves
   redundantly. Optional, when relevant: `core-scout` (new candidates),
   `util-calendar` (event collisions), `util-backtest` (risk profile of a
   proposed allocation).
3. **Invoke `journal` again, to reconcile** — it checks last sweep's calls
   against today's data and records a Notes-sheet row (`id` starting
   `reconciliation-`). This must happen BEFORE step 4; an unlogged sweep is
   invisible to the next session either way.
4. Invoke `core-council` last. It reads all lens outputs, the coverage
   summary, and the reconciliation row from step 3; gathers its own
   system-health evidence and runs the standing system-persona debate
   (module runs, coverage trends, `controller_state.json` recommendations —
   this is the former `core-controller`'s job, now performed directly by
   Council in the same invocation); forces disagreements into the open; and
   writes ONE file: `reports/YYYY-MM-DD-sweep.md`, opening with a 3-line
   Executive briefing (top investment action, top portfolio-construction
   gap, top system finding).
5. You read the report. You decide. Nothing here executes anything.

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

**As of 2026-08-02, `core-council` owns this** — the standalone `controller`
agent is merged in (archived at
`archive/agents-pre-merge-2026-08-02/core-controller.md`), so there is one
final "overall control" step per sweep instead of two agents run in an
ambiguous order. Council maintains `data/cache/controller_state.json`'s
`recommendations` — evidence-backed proposals for changes to the system
itself — via a standing 5-persona debate every sweep (not a rare gate
before big proposals): **Analyst** (facts only — what broke, what's stale,
sourced from `module_runs`/coverage/reconciliation), **Strategist** (is
effort landing on what SYSTEM.md's priority order says actually moves the
needle, across sweeps not just this one), **Maverick** (the deliberately
unconventional, out-of-the-box proposal — new data source, new capability,
a rethink nobody asked for), **Minimalist** (the counterweight — argues
removal/simplification over addition, names the maintenance cost of
anything proposed), **User Advocate** (checks every idea against actual
lived friction, not architectural taste), closed out by a **Chairman**
verdict per item: promote to a recommendation (tagged with which persona
raised it), fold into an existing one, reject with a reason, or defer.

It proposes, never applies — the user applies by saying "apply recommendation
#N". Recurring bad calls (visible in reconciliation Notes rows) are a system
defect to be traced, not bad luck. This replaces the old standalone
`IMPROVEMENTS.md` file, the earlier gated 6-voice pre-check, and (as of
today) the standalone `controller` agent itself — see `archive/` for history.

**Portfolio construction gaps** (a missing sector/asset-class, not a system
defect) are a separate concern owned by `lens-portfolio`'s coverage-gap
check and surfaced in the sweep report's Executive briefing — see "Flow"
above. Don't confuse the two: a missing healthcare position is a portfolio-
construction question for the Council's investment half; a broken fetcher
is a system-health question for its self-improvement half. Both now surface
in the same report, which is the point of the merge, but they're answered
by different evidence and different rigor.

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
