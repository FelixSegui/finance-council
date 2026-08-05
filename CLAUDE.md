# Finance Council — Investment Analytics System

Personal investment advisory system. Runs locally via Claude Code. No brokerage
integration — you are the human-in-the-loop for every action. This system
produces analysis and flags; it never executes trades.

Data sources (all free, no keys): yfinance (price + full fundamentals as
of 2026-07-28 - see note below), CoinGecko, FRED, Riksbank SWEA, SCB
PxWeb, ECB Data Portal, alternative.me Fear & Greed, SEC EDGAR (Form 4
insider counts, US tickers, `--insiders` flag).

**yfinance data-availability note (RESOLVED 2026-07-28):** Yahoo's
fundamentals endpoint (P/E, dividend yield, sector, margins, growth,
debt/equity, 4-year revenue history) requires a "crumb" token from
fc.yahoo.com, which the user unblocked in this environment's network
policy. yfinance's own Python client still fails on this network (its
curl_cffi-based browser-TLS-fingerprint impersonation gets
connection-reset by Yahoo's anti-bot layer) - `scripts/fetch_market_data.py`
bypasses yfinance's client entirely and talks to Yahoo's quoteSummary API
directly via plain `urllib` + a cookie jar, which works reliably and is
NOT detected the way curl_cffi is. Full fundamentals now fetch cleanly for
both US and Nordic tickers. One real gap remains: Yahoo's legacy
multi-year cash-flow module only exposes `netIncome` per year, not
capex/FCF - free cash flow is trailing-only (a single current figure), not
a multi-year series. For a genuine FCF trend, use a company's own cash
flow statement (PDF via the `pdf` skill).

**Swedish-equity data sources (for the `swedish-equity-review` skill):**
Finansinspektionen's Insynsregister (insider transactions) does have real
public data (PDMR transaction register, free, attribution only), but the
actual search/data tool lives at `marknadssok.fi.se` - a DIFFERENT
subdomain from `www.fi.se` (which the user unblocked 2026-07-28).
`marknadssok.fi.se` is still blocked by this environment's egress policy,
confirmed via the proxy status log - would need that specific subdomain
added too. Until then, insider activity for Swedish names stays
user-relayed, not fetched. Börsdata requires registration/API key - NOT
free/no-key,
usable only if that tradeoff is deliberately accepted for one source.
Placera, Dagens Industri, Affärsvärlden, Börskollen are editorial content,
not structured APIs - treat as user-relayed information, not a fetch
target. Kvartalsrapporter/årsredovisningar are PDFs - use the `pdf` skill
to extract real figures from a user-provided report rather than asking
for manual transcription.

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
   structural, certain, largest. **STATUS 2026-08-03: DONE.** All capital
   sits in the ISK; the Handelsbanken and SEB taxable accounts are exited.
2. **Fee drag** (bank funds at 1%+ vs index at ~0.2%) — structural,
   certain, second largest. **STATUS 2026-08-03: SUBSTANTIALLY DONE.**
   Avanza Global (the largest holding) is 0.10%, Auto 3 is 0.39%, the 2.6%
   Tundra fund is sold. One item left: the 2.5% BTC certificate (P4).
3. **Allocation / drift** — controllable, probabilistic. **Live.**
4. **Selection** (which stock/fund/coin) — smallest edge, most effort.
   **Now the main active work**, because 1-2 are finished.

The portfolio agent owns 1-3. Valuation/thesis own 4.

**Phase shift, 2026-08-03.** Levers 1 and 2 were the reason this system
front-loaded structural work, and they are now closed. The rule "never
lead with a stock pick while a wrapper inefficiency sits unaddressed"
still holds — but it is no longer binding, because there is no such
inefficiency left. Sweeps should now lead with **how the positions are
behaving** and **what should change**, and mention structure only when
something actually breaks. Re-flagging settled structural facts every
week is noise, not diligence.

Currencies: base currency is SEK. Equity data may arrive in USD/EUR;
convert using the sek_per_usd rate in the macro snapshot before computing
weights. Crypto certificates trade on Nasdaq Stockholm in SEK — fetch them
as .ST tickers via yfinance, not via CoinGecko.

## Open items — one list, one place

**`/OPEN_ITEMS.md` is the single review surface** (consolidated 2026-08-03
at the user's request). It replaced two separate lists: the
`open_structural_questions` array that used to live in `portfolio.json`
(now **P-items**) and the `IMPROVEMENTS.md` backlog (now **S-items**).
`IMPROVEMENTS.md` is a stub pointing here.

Rules:
- Agents read `OPEN_ITEMS.md` for what's outstanding. Do not recreate a
  question list inside `portfolio.json` — that split is what was fixed.
- Every Council memo pulls its open actions from this file, and closed
  items move to the bottom log with a one-line resolution. Never delete
  an item silently.
- The `meta` agent proposes S-items; nothing self-applies; the user
  approves with "apply S3".

**Blocking-question rule (still live, now general):** if an open item makes
a conclusion untrustworthy, the memo leads with it rather than burying it.
The original instance — the Handelsbanken wrapper, which gated 70% of the
portfolio — was resolved 2026-07-07 and the account fully exited, so no
item currently holds that status. The rule stays because the situation
will recur; it is not a permanent instruction to open with any particular
question.

## Flow

0. **Every session starts with `journal`** — it reads the tail of
   `reports/SESSION_LOG.md` and reports where the last sweep left off,
   pending decisions, and open items, including OPEN_ITEMS.md's "This
   sweep's recommended emphasis" block (prospecting / portfolio-tending /
   balanced — `meta`'s call from last session, a recommendation to weigh
   when deciding whether to invoke `scout` this round, not a rule). No
   analysis before this runs.
1. Run `python scripts/fetch_market_data.py` (or let the `market-data`
   subagent do it) → writes timestamped JSON to `/data/snapshots/`.
   Include `--crypto ethereum,bitcoin`: BTC is the agreed directional
   proxy for the XBT certificate, which has no working ticker.
1b. Run `python scripts/position_report.py` → the per-position movement
   table (price, move since last sweep, move vs cost, 52-week range).
   This is the user's primary weekly output and leads the memo.
2. Invoke `valuation`, `macro-regime`, `portfolio`, `thesis-review` — they
   read the latest snapshot, never fetch data themselves redundantly.
   Optional, when relevant: `scout` (new candidates), `calendar` (event
   collisions), `backtest` (risk profile of a proposed allocation).
3. Invoke `council` last. It reads all outputs, forces disagreements
   into the open, and writes one memo to `/reports/`.
4. **Every sweep ends with `journal`** — it reconciles last sweep's calls
   against today's data and appends the session entry. An unlogged sweep
   is invisible to the next session.
5. Invoke `meta` — it reviews how the system itself performed and
   maintains the S-items in `/OPEN_ITEMS.md`, plus two structural jobs
   (added 2026-08-04): a prospecting-capability check specifically for
   `scout`/`data/universe.json`, and the next-sweep emphasis
   recommendation (step 0 above). No longer purely optional — run it most
   sessions so the emphasis recommendation stays current, not stale.
6. You read the memo. You decide. Nothing here executes anything.
   Separately, roughly monthly (not every sweep), the `monthly-contribution`
   skill helps decide how much new money to move from available to
   invested that month — see its own file for why that's a different
   cadence from this flow.
7. **Every sweep ends with `python scripts/check_unmerged_work.py`** and a
   push. This is not optional bookkeeping. On 2026-08-03 we found the repo
   had been forked in two since 07-22, with ~25 commits on each side
   invisible to the other, duplicating fixes and each missing the other's
   work — undetected for 12 days. The user does not write the code and
   cannot be the one to catch this. If the check exits non-zero, resolve it
   before ending the session.

## Branching rule

Branches for testing before "prod" are fine and encouraged. What is not
fine is leaving one unmerged and unannounced. Any branch that still holds
commits `main` doesn't have at the end of a session must be either merged
or explicitly reported to the user as pending, by name, with what's on it.
Never let work go quiet on a branch.

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

**Token/cost hygiene (added 2026-07-28):** `data/portfolio.json` keeps
short current-state summaries only — resolved questions and superseded
account/holding narratives live in `data/portfolio_history_archive.md`
instead, read only during `journal` reconciliation or deep audits, not
every sweep. Per-company research that doesn't change monthly (business
description, quarterly-report figures) lives in
`data/company_profiles/<TICKER>.json` (schema:
`data/company_profiles/_SCHEMA.md`), checked before re-asking the user or
re-parsing a report. When editing `portfolio.json`, keep this shape: trim
to current state, archive the history, don't let notes/thesis fields
regrow into essays.

`data/learning_log.md` (added 2026-08-04) accumulates the "Learning notes"
section from every council memo — plain-English explanations of the
reasoning behind that sweep's concepts/decisions, at the user's request to
learn from the process, not just receive its output. Append-only, never a
source of truth for a decision.

## Self-improvement

The `meta` agent owns the **S-items** section of `/OPEN_ITEMS.md`, a
numbered backlog of changes to the system itself, each with evidence and a
concrete how. It proposes, never applies — the user applies by saying
"apply S3". It must not edit P-items (the user's portfolio questions).
Recurring bad calls in the session log are a system defect to be traced,
not bad luck.

**Structural-level jobs (added 2026-08-04):** `meta` also runs a
prospecting-capability check every session (is `scout`'s discovery
capability structurally limited — universe too narrow, screen miscalibrated,
a missing data source — tagged `[prospecting]` in the S-item title) and
sets the "This sweep's recommended emphasis" block at the top of
`OPEN_ITEMS.md` (prospecting / portfolio-tending / balanced, with a
one-line reason from real signal — idle cash, unreviewed recent
purchases, stale theses). `journal` surfaces it at the next session's
start; it's advisory, never binding.

**Model tiering (added 2026-08-04):** subagent frontmatter now sets
`model:` where the task's stakes/mechanical-ness clearly argue for
something other than the default. `council` runs on `opus` — it's the
single highest-stakes synthesis point, the only output the user acts on
directly. `market-data`, `scout`, and `calendar` run on `haiku` — pure
script execution, hard numeric filtering, and event-fetching respectively,
none requiring strong judgment. Everything else (`valuation`,
`macro-regime`, `portfolio`, `thesis-review`, `journal`, `meta`,
`backtest`) is left on the default (`inherit`) — real judgment involved,
but not the one point where a stronger model buys the most. Revisit if a
tier turns out wrong in practice; this was a reasoned first pass, not
tested against outcomes yet.

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
