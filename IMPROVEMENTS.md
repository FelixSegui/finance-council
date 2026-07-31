# Improvement Backlog

Maintained by the meta agent. Each entry is a concrete, actionable change
to THIS SYSTEM (not to the portfolio). The meta agent proposes; the user
approves; nothing here self-applies. To apply one, tell Claude:
"apply improvement #N".

Status: `open` | `approved` | `done` | `rejected (reason)`

---

## #1 — Fill Riksbank 2026 meeting dates into macro_calendar.json
- **Status:** done (2026-07-04 — user provided H2 2026 dates: Aug 20, Sep 24, Nov 4, Dec 16)

## #2 — Verify FOMC 2026 dates in macro_calendar.json
- **Status:** open
- **Why:** Dates were written from model knowledge, which violates the no-unverified-numbers ethos. One-time check against federalreserve.gov, then set `last_verified`.

## #3 — Itemize Avanza ISK holdings in portfolio.json
- **Status:** open
- **Why:** "Avanza ISK holdings" as one TBD line makes thesis-review and valuation blind to 36k SEK. One entry per holding, one thesis per holding.

## #4 — Add verified SEK crypto certificate tickers to universe.json
- **Status:** open
- **Why:** The ISK-wrapped route to crypto exposure can't be screened until the actual .ST tickers are confirmed on Avanza.

## #5 — Extract Form 4 buy/sell direction, not just counts
- **Status:** open
- **Why:** Filing counts alone are weak signal — a CFO selling for taxes and a cluster buy look identical. Requires parsing the Form 4 XML from EDGAR; doable, ~1 more fetch per filing.

## #7 — SCB Swedish CPI returns a lagged period
- **Status:** open
- **Why:** Live test on 2026-07-04 returned `se_cpi_yoy` for period 2025M12 — ~7 months stale. Either the KPItotM table lags on the English endpoint or the query needs a different table (KPIF). Stale inflation silently mislabels the Swedish rate regime.
- **How:** Check the SCB PxWeb table's latest period manually; switch table or endpoint in `fetch_se_cpi_yoy()` if a fresher one exists. Until fixed, macro-regime should treat `se_cpi_yoy` as dated by its `period` field (it already carries the period, so the data is honest — just old).

## #6 — Optional Alpha Vantage / FMP key support for earnings calendar
- **Status:** open
- **Why:** yfinance earnings dates are spotty for non-US tickers. A free-tier key would firm up the calendar agent. Blocked on: user creating a key.

## #8 — Discovery funnel: index-sourced universe + coarse factor ranker
- **Status:** done (2026-07-22 — user-requested and applied same session)
- **What:** Replaced the ~30-name hand-typed universe with a two-stage
  selection funnel. `scripts/build_universe.py` fetches the S&P 500 (~503
  names, with GICS sector + SEC CIK) from a public constituents CSV and merges
  it with the preserved user-maintained categories. `scripts/rank_candidates.py`
  (stage 1) computes cross-sectional factor z-scores — value (earnings yield),
  quality (margin/ROE/low debt), growth (revenue growth), momentum — over the
  universe and writes a ranked shortlist to `data/rankings/`. `scout.md` now
  drives rank -> hard screen -> valuation. Factor data is cached in
  `data/universe_cache/factors.json` (7-day TTL).
- **Why it mattered:** the old screener could only filter names already
  hand-typed into the universe — a filter over a wishlist, not a discovery
  engine. This was the user's self-identified biggest bottleneck.
- **Follow-ups (open):** (a) add a reachable Nordic universe source — Wikipedia
  and Nasdaq Nordic are proxy-blocked, so Nordic large caps remain a manual
  seed; SEC fundamentals also don't cover them, so Nordic names rank on momentum
  only. (b) The full 503-name fundamentals fetch takes several minutes on a cold
  cache; consider a scheduled weekly refresh so sessions always read a warm cache.

## #15 — Wire nordic_large_cap into --stack; valuation/thesis-review read the funnel
- **Status:** done (2026-07-30 — caught while re-running the finalist analysis)
- **What:** `rank_candidates.py`'s `STACK_CATEGORIES` was
  `sp500,europe_large_cap,thesis_candidates` — it silently EXCLUDED
  `nordic_large_cap` (the Swedish seed), so every `--stack` run to date ranked
  Swedish names not at all. Fixed: now
  `sp500,europe_large_cap,nordic_large_cap,thesis_candidates`. Also:
  `valuation.md` and `thesis-review.md` only listed `data/snapshots/` and
  `portfolio.json` as inputs, not `data/rankings/*.json` or
  `data/thesis_candidates.json` — so those agents couldn't actually see scout's
  funnel output for candidate tickers despite valuation's own job description
  saying it covers "candidates," not just holdings. Both agent specs now list
  the funnel outputs as inputs.
- **Consequence of the bug:** every "candidate" answer prior to this fix that
  claimed to cover Swedish names was working from ad-hoc individual fetches,
  not the stacked ranking - now closed.

## #14 — Add pending_executions tracker (committed-but-unsettled trades)
- **Status:** done (2026-07-29 — user flagged the gap directly)
- **What:** The user bought Avanza Global (119,999 SEK) and sold Tundra, but
  portfolio.json still showed the OLD 144,864 SEK undeployed cash and Tundra as
  "awaiting execution" days later - both had been mentioned in conversation but
  never confirmed executed, so they stayed invisible in the source-of-truth file.
  Root cause: the file only records SETTLED holdings on explicit confirmation
  (correct - it must never guess a trade happened), but there was no visible
  place to track "committed, not yet confirmed" trades in between, so they
  silently fell through the cracks until the user noticed and asked.
- **Fix:** added `portfolio.json.pending_executions` - a array for
  committed-but-unsettled trades (ticker, amount, date committed, status,
  rationale), separate from `holdings` and excluded from tier/exposure totals.
  An entry moves into `holdings` only on explicit user confirmation of actual
  execution. Seeded with Visa (7,500 SEK) and Schneider (5,000 SEK), both
  committed 2026-07-29, execution not yet confirmed.
- **Process note:** this is a recurring pattern worth watching - the user
  committing to a trade in conversation should immediately prompt logging it as
  PENDING (not skipping it entirely), so "did I log that?" doesn't have to be
  asked. `journal` should check `pending_executions` each sweep and ask the user
  whether any have settled.

## #13 — Fix multi-class share-count staleness (false-cheap valuations)
- **Status:** done (2026-07-29 — caught reviewing the user's Visa buy before
  confirming it as a reasonable purchase)
- **What:** Visa's ranker PE showed 8.7 (implying deeply cheap) when its real
  PE is ~30-35 (premium). Root cause in `fetch_fundamentals.py:_shares()`: SEC's
  `EntityCommonStockSharesOutstanding` DEI tag for Visa has no rows after
  2010-01-27 (Visa later moved to per-class share reporting that the free,
  non-dimensional companyfacts API can't cleanly aggregate) - the function had
  NO staleness check, so `sorted(rows)[-1]` silently returned a 16-year-stale
  share count as if it were current, understating shares ~4x and inflating the
  computed EPS/deflating the computed PE by the same factor. Same bug also hit
  BRK.B (the earlier outlier that had already required winsorizing the value
  factor, IMPROVEMENTS #12's sibling issue - never root-caused until now).
- **Fix:** `_shares()` now rejects any share-count row older than
  `_SHARES_MAX_AGE_DAYS` (400 days) and returns None (checked at both the DEI
  and us-gaap fallback stage) instead of returning it as current. Per this
  system's own rule, "no data" beats "wrong data" - Visa and BRK.B now correctly
  show null EPS/PE (insufficient data) instead of a false number. Verified:
  Visa shares None (was 469M vs real ~2.0B), BRK.B shares None, GOOGL unaffected
  (24,088,000,000... reports a clean current count), LLY/NVDA/EIX unaffected.
- **Consequence:** any multi-class US filer with this reporting pattern will now
  correctly rank on value/quality-minus-margin only, flagged as insufficient
  rather than confidently wrong. Re-run `rank_candidates.py --stack --refresh`
  for the corrected rankings to take effect (cached pre-fix records are stale).

## #12 — Fix contaminated quality factor (revenue-concept mismatch)
- **Status:** done (2026-07-29 — caught during the first stacked decision run)
- **What:** The margin/quality factor and P/E were garbage for a subset of names:
  NVDA showed a 446% net margin (revenue 26.9B vs net income 120B — impossible),
  banks/REITs showed 400-2000% margins. Two root causes, both fixed in
  `fetch_fundamentals.py`: (a) `_annual_flow` returned the first XBRL concept that
  had ANY data, so when a filer switched revenue tags it returned a STALE year's
  revenue against the current year's net income — now it MERGES across all
  revenue concepts by period-end and takes the latest. (b) Banks/REITs have no
  representative "Revenues" tag at all — added a plausibility guard that nulls any
  net margin outside [-100%, +100%], so a meaningless margin is set aside by the
  ranker rather than poisoning the cross-sectional quality z-score. Verified:
  NVDA 446%→55.6%, RF 2073%→null, LLY unchanged 31.7%.
- **Consequence:** the factor cache built before this fix carries the bad margins;
  a `--refresh` re-fetch is needed for the corrected values to flow into rankings.
- **Follow-up (open):** financials/REITs still can't be margin-ranked on free data
  (no clean revenue tag) — they'll rank on value/momentum only, quality null.
  A bank-specific revenue proxy (net interest income + noninterest income) would
  restore them but needs more XBRL concept handling.

## #11 — Stack thesis-driven judgment onto the data-driven funnel (quantamental)
- **Status:** done (2026-07-29 — user-requested, planned, and applied)
- **What:** A thesis layer on top of the data funnel, governed by "thesis
  NOMINATES, data VETS, risk score ROUTES." (a) `data/thesis_candidates.json`
  — nomination store (ticker, thesis, policy_tailwind, source, date, subjective
  risk_tag); seeded with 6 Claude picks. (b) `rank_candidates.py --stack` ranks
  universe + European seed + thesis names together, and emits a HYBRID risk read
  per name: objective `data_risk_score` (0-100 from volatility 40% / max_drawdown
  35% / leverage 15% / size 10%) shown SEPARATELY from the subjective `risk_tag`.
  (c) `fetch_fundamentals.py` now returns volatility + max_drawdown (same formulas
  as backtest.py). (d) `thesis-review.md` extended to nominate candidates + assign
  risk_tag. (e) `council.md` gains the candidate DECISION MEMO: candidates grouped
  by tier + score, a data-rank-vs-thesis reconciliation, and a forced verdict
  (BUY / re-sweep / adjust-portfolio-instead / other) with an anti-action-bias
  rule. (f) `investor_profile.json` records risk_score -> tier routing + the
  medium-tier "hold risk constant" rule.
- **Guardrails:** a thesis name never silently overrides a hard-screen failure —
  it's flagged with its reason and buyable only as a logged override; every
  number still traces to fetched data; objective and subjective risk stay
  decomposed; theses are dated and flagged when they lean on training knowledge.
- **Bug fixed in build:** the factor cache didn't invalidate when the record
  schema changed (added volatility/max_drawdown), so risk scores were silently
  computed on partial inputs for pre-existing cached names. gather() now treats a
  record missing `volatility` as stale and refetches.
- **Known limit:** thesis picks that are non-US (most of the seed) have no free
  fundamentals, so they rank momentum-only — the data can partially, not fully,
  vet them. That is itself signal: those names carry more thesis-reliance and the
  memo should say so.

## #10 — Extend the funnel: crypto context, European seed, sustainability screen
- **Status:** done (2026-07-22 — user-requested and applied same session)
- **What:** (a) `scripts/rank_crypto.py` — high-risk-tier CONTEXT (CoinGecko
  momentum/ATH-distance + Fear & Greed), explicitly not a buy-ranker, since
  crypto has no fundamentals to standardise. (b) `scripts/add_manual_tickers.py`
  — validated ticker adder for non-US categories (verifies each against Yahoo
  price data, drops anything that doesn't resolve); seeded `europe_large_cap`
  with 27 validated European large-caps tilted to growth/quality + renewables.
  (c) `rank_candidates.py` gains `--exclude-sectors` (sustainability negative
  screen on GICS sector) and a `momentum_only_ranking` for names without
  fundamentals (non-US), kept separate from the full-factor composite.
- **Known limits / follow-ups:** European names rank on momentum ONLY — no free
  European fundamentals source exists (SEC is US-only; Yahoo fundamentals
  blocked). Sector exclusion can't touch non-US names (no GICS metadata). The
  clean growth-preserving way to get Europe + sustainability remains a
  FUND-level choice in the secure tier (European index fund / ESG fund), not
  individual-stock ranking — real ESG scoring needs paid data (MSCI/
  Sustainalytics) and must not be faked from free sources.
- **Bug fixed in build:** `_yahoo_symbol()` was rewriting every dotted ticker's
  dot to a dash (for US class shares like BRK.B->BRK-B), which mangled European
  exchange suffixes (SAP.DE->SAP-DE, a 404). Now only US class-share dots are
  rewritten; real exchange suffixes (.DE/.AS/.PA/.CO/.MI/.SW/.MC/.L...) are kept.

## #9 — Correct the "equities data blackout" diagnosis (Yahoo crumb, not egress)
- **Status:** done (2026-07-22 — diagnosis corrected; workaround shipped with #8)
- **What:** The session log (2026-07-20/22) attributed the equities fetch
  failures to an "org egress policy block on Yahoo Finance." Direct probing on
  2026-07-22 showed that is imprecise: Yahoo's price/chart endpoint
  (`query1.../v8/finance/chart`) returns 200 and is fully reachable; only the
  crumb-gated fundamentals endpoint (`quoteSummary`) fails — the cookie host
  `fc.yahoo.com` is proxy-blocked, so the crumb auth 401s. i.e. PRICES work,
  FUNDAMENTALS via Yahoo don't.
- **Consequence:** `fetch_market_data.py:fetch_equities()` relies on `yf.info`
  (quoteSummary) and so still returns nulls for SHB-A.ST/INVE-A.ST/COIN-XBT.ST.
  The ranker sidesteps this by taking fundamentals from SEC EDGAR and prices
  from the working chart endpoint. Follow-up: rework `fetch_equities()` to pull
  price/52w/momentum from the chart endpoint (so per-ticker holding prices
  refresh again) and source US fundamentals from SEC EDGAR, mirroring
  `fetch_fundamentals.py`. Non-US fundamentals remain unavailable for free.
