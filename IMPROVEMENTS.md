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
