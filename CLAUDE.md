# Finance Council — Investment Analytics System

Personal investment advisory system. Runs locally via Claude Code. No brokerage
integration — you are the human-in-the-loop for every action. This system
produces analysis and flags; it never executes trades.

Data sources (all free, no keys): yfinance, CoinGecko, FRED, Riksbank
SWEA, SCB PxWeb, ECB Data Portal, alternative.me Fear & Greed, SEC EDGAR
(Form 4 insider counts, US tickers, `--insiders` flag).

## Scope (Phase 1 — locked 2026-07-03)

Covered: **equities, ETFs/index funds, crypto**, with **macro (rates, yield
curve, inflation, dollar)** as regime context, not a tradeable asset class.

Explicitly out of scope until a paid data feed is added: individual bonds,
options, alternatives. Free data for these is either non-existent (bonds,
alts) or too thin to trust (options IV/skew). Do not let any agent generate
options or alts recommendations from scraped/free data — that is false
confidence, not analysis. If asked, agents should say so and stop.

## Why this exists (read before extending)

The single biggest risk in an LLM-based investment system is **confident
structure built on stale or hallucinated numbers**. Every numerical claim in
every agent's output must trace to a file in `/data` written by
`scripts/fetch_market_data.py` in the same session. No agent invents a price,
ratio, or macro figure. If data wasn't fetched, the agent says "no data" —
it does not estimate from training knowledge, which is stale by definition.

## Priority order (Swedish retail context, ~200-250k SEK)

At this portfolio size, the return hierarchy is:
1. **Account wrapper efficiency** (ISK tax-free allowance vs taxed AF) —
   structural, certain, largest.
2. **Fee drag** (bank funds at 1%+ vs index at ~0.2%) — structural,
   certain, second largest.
3. **Allocation / drift** — controllable, probabilistic.
4. **Selection** (which stock/fund/coin) — smallest edge, most effort.

The portfolio agent owns 1-3. Valuation/thesis own 4. Never let a memo
lead with a stock pick while a wrapper inefficiency or 1.5% fee sits
unaddressed — that's optimizing the smallest lever first.

Currencies: base currency is SEK. Equity data may arrive in USD/EUR;
convert using the sek_per_usd rate in the macro snapshot before computing
weights. Crypto certificates trade on Nasdaq Stockholm in SEK — fetch them
as .ST tickers via yfinance, not via CoinGecko.

## Blocking questions rule

`portfolio.json` contains an `open_structural_questions` list. While
question 1 (Handelsbanken wrapper) is unresolved, every Council memo must
open with it — 70% of the portfolio sits in that account, and no
allocation, rebalancing, or tax conclusion touching it is trustworthy
until the wrapper is confirmed. Agents may still analyze the other
accounts fully. Remove questions from the list as they get answered.

## Flow

0. **Every session starts with `journal`** — it reads the tail of
   `reports/SESSION_LOG.md` and reports where the last sweep left off,
   pending decisions, and open items. No analysis before this runs.
1. Run `python scripts/fetch_market_data.py` (or let the `market-data`
   subagent do it) → writes timestamped JSON to `/data/snapshots/`.
2. Invoke `valuation`, `macro-regime`, `portfolio`, `thesis-review` — they
   read the latest snapshot, never fetch data themselves redundantly.
   Optional, when relevant: `scout` (new candidates), `calendar` (event
   collisions), `backtest` (risk profile of a proposed allocation).
3. Invoke `council` last. It reads all outputs, forces disagreements
   into the open, and writes one memo to `/reports/`.
4. **Every sweep ends with `journal`** — it reconciles last sweep's calls
   against today's data and appends the session entry. An unlogged sweep
   is invisible to the next session.
5. Optionally invoke `meta` — it reviews how the system itself performed
   and maintains `IMPROVEMENTS.md`.
6. You read the memo. You decide. Nothing here executes anything.

## Time horizons

Every Council call carries a horizon tag. The system's edge shrinks as
the horizon shortens — weight effort accordingly:

- **Long (3y+)** — wrapper efficiency, fee drag, allocation. Owned by
  `portfolio`. Highest edge, structural, this is where the money is.
- **Medium (6mo–3y)** — valuation entry/exit, thesis health, regime
  positioning. Owned by `valuation` + `thesis-review` + `macro-regime`.
- **Short (<6mo)** — tactical overlay ONLY: capped at 10% of portfolio,
  never High confidence, always flagged as tactical in the memo. LLMs on
  free data have no demonstrated short-term edge; the system says so
  rather than pretending otherwise.

## Session continuity

`reports/SESSION_LOG.md` is the system's memory across sessions —
append-only, one entry per sweep, written by `journal`, which also
reconciles previous calls against current data (the only calibration
mechanism this system has). `data/valuations.csv` accumulates portfolio
value observations for `scripts/performance.py` (are we beating "just
buy the index"?). If a session did meaningful work without a log entry,
that's a process failure — fix it before ending the session.

## Self-improvement

The `meta` agent owns `IMPROVEMENTS.md`, a numbered backlog of changes to
the system itself, each with evidence and a concrete how. It proposes,
never applies — the user applies by saying "apply improvement #N".
Recurring bad calls in the session log are a system defect to be traced,
not bad luck.

## Your portfolio state

`data/portfolio.json` is the source of truth — you maintain it manually
(no brokerage API). Update it whenever you actually place a trade. Every
agent treats this file, not memory, as ground truth for what you hold.

`data/investor_profile.json` is the client profile — risk tolerance,
horizon, buffer, constraints. It is what a human advisor would establish
first, and it is what turns the portfolio agent's balance scorecard from
generic rules of thumb into advice measured against your situation.
Every Council memo carries the scorecard; TBDs in the profile are named
in the memo until filled.

## Council rule

The Council subagent's only job is adversarial synthesis. If two agents
agree, that's not interesting — the memo should foreground *where they
disagree* and force an explicit confidence call. A memo with no tension in
it means the Council didn't do its job; re-run it.
