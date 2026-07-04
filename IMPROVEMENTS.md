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
