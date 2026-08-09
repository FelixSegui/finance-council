# Investment Management System — V2 Upgrade Specification

**Status: user-authored roadmap, received 2026-08-09.** Saved here verbatim
so it's never lost or re-typed from memory. `OPEN_ITEMS.md`'s "V2 Roadmap"
section tracks phase-level progress against this document; this file is the
full source text, not maintained/edited as work completes — check
`OPEN_ITEMS.md` and `git log` for what's actually been built.

**Phase 1 (sections 4-5, 18-20, 24-25 in substance) was implemented
2026-08-09** — see that date's commits for what shipped: a structured
thesis schema, Council's structured Chairman action format, per-field
data-quality states + source-tier hierarchy in `data/company_profiles/`,
and new Layer A/B fetched+derived company metrics
(`scripts/derived_metrics.py`, extended `scripts/fetch_market_data.py`).
Phases 2-6 (the rest of this document) are not yet built.

---

You are working on an existing personal investment-management and financial-analysis system. Do not rebuild the system from scratch. First inspect the existing repository, scripts, JSON schemas, reports, OPEN_ITEMS.md, SESSION_LOG.md, and the current Excel import pipeline. Preserve working architecture and conventions unless there is a strong reason to change them.
The goal of this upgrade is to make the system materially better at:

1. finding high-quality companies at reasonable/attractive valuations;
2. distinguishing "quality" from "quality at a good price";
3. identifying portfolio concentration by actual risk factor, not merely by ticker or sector;
4. incorporating a standardized macro/regime layer;
5. preventing emotional attachment to existing holdings;
6. using deterministic quantitative data for what can be standardized and AI reasoning only where qualitative judgment genuinely adds value;
7. screening a large universe efficiently without sending hundreds of companies to an LLM;
8. preserving the existing weekly Sweep → Lenses → Council → Journal → Meta architecture

## 1. Current architecture — preserve this
The current weekly sweep is:

0. Journal/session start
1. Market data
1a. Excel import
1b. Position report
2. Four lenses:
   * valuation
   * macro-regime
   * portfolio
   * thesis-review
3. Six-voice Investment Council
4. Journal/session end
5. Meta/system review
6. Human decides
7. Unmerged-work guard + push

The current Excel architecture is also intentional:

* `Holdings` = canonical holdings ledger
* `Transactions` = append-only transaction history
* `Watchlist` = screening candidates
* `Analytics` = portfolio calculations
* `Summary` = high-level view
* `FX Rates` = FX data
* `Value history` = portfolio history

The Excel importer is strictly read-only and must remain read-only.
Never silently overwrite, repair, or mutate the workbook.
Any inconsistency should become an explicit data-quality flag.

## 2. Important portfolio update
The user purchased:

* AstraZeneca (`AZN.ST`)
* 1 share
* purchase date: 2026-08-06
* purchase price: 1,520.50 SEK

The system should treat this as a real transaction and ensure the portfolio/transaction state reflects it correctly.
Do not replace the user's actual purchase price with the later market snapshot price.

## 3. New architectural principle
The system should now explicitly separate:

**Layer A — Deterministic data.** Facts that can be fetched or calculated consistently. Examples: revenue, EBIT, EBITDA, operating cash flow, capex, cash, total debt, interest expense, equity, invested capital, shares outstanding, market capitalization, price, P/E, EV/EBIT, FCF yield, historical earnings, dividend, EPS, sector, country, FX, macroeconomic indicators.

**Layer B — Quantitative derived metrics.** Calculated locally from standardized data. Examples: ROIC, FCF margin, operating margin, net debt / EBITDA, interest coverage, EPS CAGR, FCF CAGR, earnings volatility, margin stability, valuation percentile, quality score, valuation score, balance-sheet score, stability score, macro sensitivity, portfolio concentration, risk-factor exposure.

**Layer C — AI qualitative analysis.** AI should only be used where interpretation is genuinely valuable. Examples: competitive advantage / moat, management quality, capital allocation quality, unusual company-specific risks, regulatory/geopolitical risks, interpretation of conflicting macro signals, interpretation of earnings/news, whether the current thesis remains valid, whether valuation appears justified by business quality, whether a company fits the current macro regime.

**Layer D — Council.** The Council integrates A+B+C and makes the final recommendation.

This separation is critical. Do not ask an LLM to calculate ratios that Python can calculate deterministically. Do not ask Python to determine whether management has a durable competitive moat.

## 4. Build a standardized company-data layer
Create or extend a standardized company data schema. The objective is that the system can represent hundreds of companies in a compact machine-readable format without sending annual reports or huge datasets to the LLM. A company record should contain approximately:

```json
{
  "ticker": "ATCO-B.ST",
  "company": "Atlas Copco",
  "country": "Sweden",
  "sector": "Industrials",

  "quality": {
    "roic_current": null,
    "roic_5y_avg": null,
    "operating_margin": null,
    "operating_margin_5y_avg": null,
    "fcf_margin": null,
    "fcf_margin_5y_avg": null,
    "margin_stability": null
  },

  "growth": {
    "revenue_cagr_5y": null,
    "eps_cagr_5y": null,
    "fcf_cagr_5y": null,
    "eps_volatility": null
  },

  "balance_sheet": {
    "net_debt_ebitda": null,
    "interest_coverage": null
  },

  "valuation": {
    "pe": null,
    "ev_ebit": null,
    "fcf_yield": null,
    "peg": null,
    "historical_pe_percentile": null,
    "historical_ev_ebit_percentile": null
  },

  "market": {
    "price": null,
    "52w_position": null,
    "beta": null
  },

  "data_quality": {
    "as_of": null,
    "age_days": null,
    "missing_fields": [],
    "suspect_fields": []
  }
}
```

The exact schema may differ if the repository already has a better convention. Do not duplicate schemas unnecessarily.

## 5. Do NOT fetch every ratio independently
Prefer fetching standardized financial statement inputs and calculating derived metrics locally. For example:

```
FCF = Operating Cash Flow - Capex
FCF Margin = FCF / Revenue
Operating Margin = EBIT / Revenue
Net Debt = Total Debt - Cash
Net Debt / EBITDA = Net Debt / EBITDA
Interest Coverage = EBIT / Interest Expense
```

The system should clearly distinguish: source data, calculated data, estimated data, AI-derived judgments. Never mix them.

## 6. Minimum quantitative screening set
Do not over-engineer the first version. Prioritize these metrics because they provide high decision value relative to data complexity:

**Quality:** ROIC, operating margin, FCF margin, 5-year average ROIC, margin stability.
**Growth:** 5-year revenue CAGR, 5-year EPS CAGR, 5-year FCF CAGR, EPS volatility.
**Balance sheet:** net debt / EBITDA, interest coverage.
**Valuation:** P/E, EV/EBIT, FCF yield, PEG, historical valuation percentile where available.

These are the initial quantitative core. Do NOT add dozens of ratios merely because they are available.

## 7. Quality must be separated from valuation
This is a major conceptual upgrade. The system must explicitly distinguish GOOD COMPANY from GOOD INVESTMENT AT CURRENT PRICE. For example, "Quality Score: 92/100, Valuation Score: 41/100" is a valid outcome — excellent company, unattractive current price. Likewise "Quality Score: 82/100, Valuation Score: 87/100" could identify a potentially interesting "cheap quality" candidate. The system must not allow a high Quality Score to automatically produce a BUY.

## 8. PEG is a screening metric, not a decision rule
Do not introduce a hard rule such as "PEG < 2 = BUY". PEG should be treated as one valuation input, interpreted alongside P/E, EV/EBIT, FCF yield, historical valuation, expected growth, quality, balance sheet. The system should explicitly recognize that PEG depends on estimated future growth and therefore contains forecast uncertainty.

## 9. Introduce "Fair Value Gap"
Where sufficient data exists, introduce a standardized valuation comparison: current valuation vs. historical/estimated reasonable valuation. For example: "Current P/E: 33.7x, Historical reasonable P/E: 27x, Valuation gap: -20%". Do not pretend this is precise intrinsic value. Call it something such as `valuation_gap_estimate` and attach: methodology, confidence, data source, date. If fair-value estimation is unreliable, return `UNKNOWN` rather than inventing precision. The system should prefer "unknown" over "false precision."

## 10. Create a Quant Screen pipeline for the 500+ company universe
The system currently has approximately 540 companies/candidates available through the broader universe/watchlist architecture. Do NOT send all 540 companies to an LLM. Build a funnel:

```
~540 companies
       ↓
Data validation
       ↓
Hard quality/balance-sheet filters
       ↓
~150–250
       ↓
Quant quality ranking
       ↓
~50–75
       ↓
Valuation ranking
       ↓
~20–30
       ↓
Portfolio-fit / diversification filter
       ↓
~10–15
       ↓
AI qualitative analysis
       ↓
~5–10
       ↓
Investment Council
```

The exact thresholds must be configurable rather than hardcoded. The Scout Agent should therefore output a compact candidate dataset, not a huge textual report.

## 11. Introduce portfolio-fit scoring
A company should not receive a high final score merely because it is individually attractive. The system must ask "Does owning this improve the portfolio?" Include: sector concentration, geography, revenue geography, currency exposure, factor exposure, cyclicality, beta, correlation where feasible, existing position size, existing holdings with similar economic drivers.

This is especially important because the current portfolio has high industrial exposure. Do not treat Volvo + Atlas Copco + Alfa Laval + ABB as four completely independent risks — they share economic exposures: global industrial activity, capital expenditure, manufacturing, business investment, global trade, interest rates, cyclical demand. The system should therefore introduce a concept of `risk_factor_exposure` in addition to ordinary sector classification.

## 12. Sector concentration is not enough
Build toward factor/risk-bucket classification. Initial buckets could include: Global industrial cycle, Defensive healthcare, Financials, Consumer staples, Technology/growth, Energy/commodities, Real estate/rates, Broad market, Crypto, Cash. Do not require perfect classification initially. Use deterministic classifications where possible and AI classification only when necessary. The goal is to answer "What economic scenario hurts my portfolio?" rather than merely "How many industrial stocks do I own?"

## 13. Build a Macro Regime Engine
Do NOT attempt to build an AI crystal ball that predicts "the market will crash next month." Instead, create a standardized `market_regime` layer classifying the current environment across several dimensions:

**Liquidity:** central-bank policy, policy-rate direction, balance-sheet/liquidity conditions where available, financial conditions.
**Inflation:** CPI/inflation trend, inflation surprises, real yields.
**Growth:** PMI, unemployment, GDP/growth trend, earnings revisions where available.
**Credit:** credit spreads, financial stress indicators, funding conditions.
**Market risk:** VIX, equity breadth where available, volatility, valuation extremes.
**Currency / global funding** (particularly important for the current portfolio): DXY, USD/JPY, JPY direction, BOJ policy, US Treasury yields. The Japan/yen carry-trade channel should be explicitly represented because changes in Japanese rates can affect global liquidity and risk assets.

## 14. Macro output should be a regime, not a prediction
Example:

```
REGIME: Tightening / elevated liquidity risk
CONFIDENCE: Medium
KEY DRIVERS:
- rising real yields
- tighter central-bank policy
- stronger USD
- widening credit stress
- BOJ tightening / JPY appreciation
PORTFOLIO IMPLICATION:
- reduce enthusiasm for highly leveraged growth assets
- prefer strong balance sheets
- require greater valuation margin of safety
- avoid increasing already concentrated cyclical exposure
- crypto additions require stronger confirmation
```

The Macro Agent should NOT say "Sell everything." Instead it should modify the required investment threshold.

## 15. Introduce Macro → Asset Fit
Every candidate should eventually receive `macro_fit: positive / neutral / negative / unknown` and ideally `macro_sensitivity: rates / inflation / growth / liquidity / USD / credit / commodity`. Example:

```
AstraZeneca: growth sensitivity low/medium, rates sensitivity low, credit sensitivity low, macro fit positive
Atlas Copco: growth sensitivity high, rates sensitivity medium, macro fit neutral
High-growth tech: growth sensitivity medium, real-rate sensitivity high, valuation sensitivity very high, macro fit negative
```

These do not have to be perfectly precise. The point is to expose portfolio-level risk.

## 16. Macro must NOT override valuation automatically
A strong macro regime should never automatically make a cheap stock a buy. Likewise, a bad macro regime should not automatically make a great company a sell. Instead: Company quality + Valuation + Balance sheet + Portfolio fit + Macro regime = Decision context. The Council makes the final judgment.

## 17. Introduce dynamic investment thresholds
This is important for avoiding sentimental investing. In a favorable market regime, BUY threshold = normal. In an elevated-risk regime, BUY threshold = higher. For example: Normal: Quality > 75, Valuation > 60. Elevated risk: Quality > 80, Valuation > 70, Balance sheet > 70. The exact numbers should be configurable and backtestable. The system should not simply sell existing holdings because the regime worsened.

## 18. Fix the emotional attachment problem with thesis states
Every active position should have a formal thesis. Required fields: `why_owned`, `expected_driver`, `valuation_reason`, `key_risks`, `break_conditions`, `thesis_status`, `last_reviewed`. Possible thesis states: `INTACT`, `WEAKENING`, `BROKEN`, `UNTESTED`, `TOO_EARLY`. Crucially: `UNTESTED` is NOT the same as `OK`. A stock without a testable thesis is not automatically healthy.

## 19. Force every purchase to create a testable hypothesis
Before or at the time of purchase, the system should require: "Why do I own this? What do I expect? What would prove me wrong?" A good hypothesis should resemble: "I own X because Y. I expect Z over the next 3–5 years. I will reconsider/exit if A, B or C occurs." Do not allow generic statements such as "Good company." "Strong stock." "Has potential." "I like the sector." The user's actual AZN reasoning is a useful model: historically resilient quality company; healthcare is more defensive than high-beta tech; reasonable dividend history; diversification away from industrials/technology; expectation of greater resilience if high-valuation growth assets correct. The system should preserve this reasoning but turn it into falsifiable conditions.

## 20. Improve the Council's role
The Council should not simply write a sophisticated paragraph. Its job is to decide. For every headline call, force the Chairman to answer:

```
ACTION: BUY / ADD / HOLD / REDUCE / SELL / WATCH / NO ACTION
POSITION: Current weight
TARGET: Target weight or range
REASON: 1–3 strongest reasons
THESIS STATUS: INTACT / WEAKENING / BROKEN / UNTESTED / TOO_EARLY
WHAT CHANGED: Specific new evidence
BREAK CONDITION: What would force a different decision?
CONFIDENCE: Low / Medium / High
HORIZON: Short / Medium / Long
```

The six voices remain: Contrarian, First Principles, Expansionist, Outsider, Executor, Chairman. But the Chairman must produce an actual action.

## 21. Add a "Sell discipline"
The system must treat selling as a legitimate outcome, not as a failure. A position can be sold/reduced when: 1) thesis is broken; 2) valuation becomes extreme relative to quality; 3) portfolio concentration becomes excessive; 4) a materially better opportunity exists; 5) macro/risk regime changes and the position has unusually high sensitivity; 6) balance sheet deteriorates; 7) expected risk-adjusted return falls materially below alternatives. Do NOT require the system to wait until a loss occurs. Likewise, do not sell merely because a position has risen. The question is: "Would I buy this position today at today's price given today's information?" This should become a standard thesis-review question.

## 22. Add "Would I buy it today?"
For every holding: "If I had zero shares today, would I initiate this position at today's price?" Possible answers: YES / YES, BUT SMALLER / HOLD ONLY / NO — VALUATION / NO — THESIS / NO — PORTFOLIO FIT / UNKNOWN. This is specifically designed to combat anchoring and sentimental attachment.

## 23. Improve the Watchlist
The current Watchlist should remain the human-editable candidate universe. However, it should be expanded to include diversification candidates currently missing from the narrower universe. The system should explicitly look for: financials, consumer defensives, healthcare, non-Swedish European companies, quality ETFs available to the user, quality technology at reasonable valuations, other sectors that reduce current industrial concentration. Do not assume the solution to industrial concentration is simply "buy more healthcare." Let the quantitative Scout identify candidates.

## 24. Data quality must be a first-class system component
The current system already does this well. Strengthen it. Every quantitative field should have: value, source, as_of, age_days, confidence, and potentially calculation_method. Data-quality states: `OK`, `STALE`, `MISSING`, `SUSPECT`, `CONFLICTING`, `ESTIMATED`. Never silently replace missing values. Never allow a suspicious value to drive a major investment decision without an explicit warning. The current Atlas Copco P/E discrepancy is exactly the kind of issue this should prevent: Excel contained an implausible 2.05x P/E while the live snapshot showed approximately 33.7x. The system correctly treated the Excel figure as suspect. Preserve and strengthen this behavior.

## 25. Add source hierarchy
Where multiple sources exist, define a hierarchy. For example: Tier 1: Company filings / official investor relations. Tier 2: Reliable structured market-data provider. Tier 3: Excel Stocks data type. Tier 4: Secondary financial websites. Tier 5: User-provided data. This does not mean lower-tier data is unusable — it means the system knows how much confidence to assign to it. User-provided data should be accepted for portfolio reconciliation but clearly marked as user-relayed.

## 26. Avoid token waste
The AI should NOT receive: all 540 company records in full; entire annual reports; entire Excel workbooks; repetitive financial history; every raw market-data point. Instead: the quant engine processes the entire universe locally; the AI receives only top-ranked candidates, compact quantitative summaries, relevant company-specific news, relevant macro context, portfolio context, existing thesis if the company is already held. The AI should usually analyze 5–15 companies, not 540.

## 27. Recommended data flow
```
DATA SOURCES → STANDARDIZED RAW DATA → DATA VALIDATION → DERIVED METRICS →
QUALITY/VALUE/BALANCE/STABILITY SCORES → UNIVERSE SCREEN → PORTFOLIO-FIT FILTER →
MACRO REGIME → TOP 10–15 → AI QUALITATIVE ANALYSIS → INVESTMENT COUNCIL → MEMO
```
This should integrate with the existing weekly Sweep rather than create an entirely separate system.

## 28. Suggested new weekly Sweep structure
Preserve the existing flow but update step 2:
```
0. Journal
1. Market data
1a. Excel import
1b. Position report
2. Quant / screening layer
    2a. Data validation
    2b. Recalculate derived metrics
    2c. Update quality/value/balance/stability scores
    2d. Run universe screen
    2e. Run portfolio-fit screen
3. Four lenses (valuation, macro-regime, portfolio, thesis-review)
4. AI qualitative analysis — only on selected candidates/relevant holdings
5. Investment Council — six voices + Chairman
6. Journal
7. Meta
```
Do not make the Scout run a full AI analysis of every company every week.

## 29. Backtesting and calibration
Before treating the scoring system as predictive, create a framework for evaluating it. Track: quality score vs future return; valuation score vs future return; combined score vs future return; macro regime vs future drawdown; portfolio-fit decisions; Council recommendations vs outcomes. Initially this is an experiment. Do not assume "ROIC > 15% works." Test it. Do not assume "PEG < 2 works." Test it. The Meta agent should eventually ask "Which rules are actually adding predictive or risk-management value?" and recommend removing rules that do not.

## 30. Drawdown test
The portfolio currently has an 85/10/5/0 target framework and an approximately -30% portfolio drawdown tolerance. Before declaring the target allocation valid, implement a historical/hypothetical stress-testing framework. At minimum test: 2008-style crisis; 2020 crash; 2022 rate/inflation shock; 2024/2025/2026-style concentrated tech correction; crypto-specific crash; strong USD/weak SEK scenario; BOJ tightening/yen carry unwind scenario. The purpose is NOT to predict these events — it's "would this portfolio violate the user's stated risk tolerance under plausible shocks?" This should become part of Portfolio Health.

## 31. Macro should affect allocation gradually, not emotionally
Do not implement "macro bad → sell everything." Instead: macro risk rising → raise quality requirement → raise valuation margin-of-safety requirement → reduce additions to highly sensitive sectors → slow new risk-taking → review overweight positions. Only exceptionally strong evidence should trigger actual reductions. This creates a disciplined risk-management system rather than a market-timing system.

## 32. Add a portfolio-level "risk narrative"
Every weekly memo should eventually contain something like:
```
PORTFOLIO RISK MAP
Largest economic exposures: 1. Global industrial cycle 2. Swedish/European equity 3. Global equity 4. Crypto/liquidity 5. SEK/USD exposure
Current macro regime: Tightening / Neutral / Risk-on / Risk-off / etc.
Most vulnerable holdings: ...
Most resilient holdings: ...
Main concentration: ...
Most important diversification opportunity: ...
What would hurt this portfolio most: ...
```
This is more useful than simply listing sector weights.

## 33. Specific current issue to preserve
The current system identified: approximately 69% industrial exposure in the stock-picking sleeve; crypto approximately 12.8% vs a 10% target; equity approximately 82.8% of investable capital vs 85%; high-quality industrial names purchased at relatively high valuation; several new positions without testable theses. Do not erase these findings. Use them as the first test case for the new architecture.

## 34. Current crypto rule
Keep the existing "let crypto dilute" principle but improve it. Current logic: target crypto = 10%; current crypto is above target; no additional crypto purchases; new contributions go to equity; if crypto remains above 12% at the specified review point, consider trimming. Preserve this basic rule unless new evidence clearly justifies changing it. However, integrate macro/funding-risk information into the Council. Particularly monitor: BTC valuation/cycle position, crypto Fear & Greed, DXY, real yields, global liquidity, BOJ policy, USD/JPY, funding/leverage conditions. Do not automatically sell BTC because macro is negative.

## 35. Important principle for the entire system
The system should optimize for risk-adjusted decision quality, not maximum number of signals. A small number of robust metrics is preferable to dozens of noisy indicators. Likewise, uncertainty is preferable to false precision. If data cannot reliably establish a metric, say `UNKNOWN`. If AI cannot establish a qualitative conclusion confidently, say `LOW CONFIDENCE`.

## 36. Implementation discipline
Before changing code: 1) Inspect the current repository. 2) Identify existing scripts and schemas. 3) Identify what already implements the requested functionality. 4) Avoid duplicate functionality. 5) Propose the minimum number of new files/components. 6) Implement incrementally. 7) Run existing tests. 8) Add tests for new calculations. 9) Run the weekly sweep on current data. 10) Compare the new memo against the previous memo. 11) Report what changed. Do not silently change portfolio data. Do not silently change allocation targets. Do not execute trades. Do not write into the Excel workbook. Do not delete old data unless explicitly instructed.

## 37. Meta-agent responsibilities
The Meta agent should now specifically monitor:
**Data quality:** missing fields, stale fields, source conflicts, suspicious values.
**Model quality:** whether scores actually discriminate, whether metrics are redundant, whether thresholds are too strict/loose.
**AI quality:** hallucinations, unsupported qualitative claims, false precision, repeated generic reasoning.
**Portfolio behavior:** concentration drift, thesis drift, anchoring, overtrading, failure to sell broken theses.
**System efficiency:** token consumption, API calls, runtime, duplicate fetches, unnecessary AI calls.
Meta should propose improvements, not automatically apply structural changes.

## 38. Definition of success
The upgraded system should be able to answer, for any candidate: "Is this a good company?" (standardized quantitative + qualitative evidence); "Is it attractively valued?" (multiple valuation measures + historical context); "Is the balance sheet strong?" (standardized metrics); "Does it improve my portfolio?" (sector, geography, risk-factor exposure); "Does the current macro regime favor or penalize it?" (Macro Regime Engine); "What would make us wrong?" (explicit thesis + break conditions); "Would we buy it today?" (independent of whether we already own it); "How confident are we?" (explicit confidence and data-quality states). That is the target architecture.

## 39. Final design philosophy
The system should behave like a disciplined investment team: Python/data layer — "What is true?"; Quant layer — "What is statistically interesting?"; Portfolio layer — "Does it improve what we already own?"; Macro layer — "What environment are we operating in?"; AI analyst — "What does the data not capture?"; Contrarian — "What could we be missing?"; First Principles — "What actually drives the return?"; Outsider — "Would an independent investor buy this today?"; Executor — "What should actually happen?"; Chairman — "BUY / ADD / HOLD / REDUCE / SELL / WATCH — and why?"; Meta — "Did the system make a better decision this week than it would have made previously?"

The system should never become a machine that rationalizes existing holdings. Its job is to continuously challenge them. The key mental model is: **Do not protect the portfolio. Protect the investment thesis.** And: **Do not search for good companies. Search for good companies at prices that compensate you for the risks you are taking.**
