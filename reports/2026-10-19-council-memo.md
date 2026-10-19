# Council Memo — 2026-10-19

*This memo is a structured synthesis of your own agents' analysis of data fetched this
session. It is not licensed investment advice. Every number in it comes from a file
written for this sweep, or is labelled as carried forward, user-relayed, or this memo's
own arithmetic.*

---

## What leads this memo

**1. ABB.ST reports tomorrow (2026-10-20). This memo does not renew last week's SELL.**
The 2026-10-12 Chairman made that call non-renewable. Its words: "If nothing has executed
by the 10-20 print, it is recorded as lapsed. The 10-19 memo, if one runs, does not
restate it." This is the 10-19 memo, so I am honouring that.
- **Last week's SELL (conviction 5) can still be executed today, exactly as written.** If
  you do, you are acting on the 10-12 decision. This memo adds no conviction to it.
- **If it has not executed by the print, it lapses.** The 10-26 memo then decides ABB from
  the reported Q3 numbers, with no streak count. #1 below names the Q3 numbers that
  decide it.
- **The VICI BUY no longer depends on the ABB sale.** It stands on its own merits and
  has a second funding route (P3). See #3.

**2. D-c's band was computed on the wrong denominator. Corrected here.**
- The 2026-10-12 memo sized the BTC0E.AS band against the *investable base* (excluding
  the tax reserve). It said the denominator was "unpinned".
- It is pinned. `data/definitions.json` → `investable_capital_convention`: you decided on
  2026-08-17 that crypto trip-wires use the **full portfolio**. You explicitly rejected
  the investable-only reading.
- **On your convention the trim fires only above ~14,080 SEK** for the 150 units (≈93.9
  SEK/unit), not ~11,730 SEK. That is a real change to the decision, not a rounding
  difference (§6, D-c).

**3. Settled facts the launch premises asserted otherwise (S27). Not re-litigated.**
- The orchestrator reports that the scheduled prompt again called the Handelsbanken
  wrapper "unresolved". It is resolved: `portfolio.json.resolved_structural_questions`,
  2026-07-07, with the HB exit executed 2026-07-12/20.
- It also called `reference_targets` "null". They are not null. They hold a stale
  85/10/0/5 against `portfolio.json.targets`' 80/10/5/0/5.
- **More serious this week: the scheduled prompt left out `scout.py` entirely.** The
  orchestrator ran it anyway. A prompt that skips a mandatory pipeline stage is a worse
  failure than a stale fact (§9).
- I can verify the premises against the files. I cannot read the prompt itself, so the
  recurrence claim rests on the orchestrator's relay. By the count chain (7 through
  10-05 in OPEN_ITEMS.md, 8th on 10-12), this is the **9th occurrence**.

---

## 1. Position report

`scripts/position_report.py` output, handed over as a file path (unchanged):

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 151.35 | +0.8% | +17.1% | 84% | 151.35 | fetched |
| Investor A (stock) | 405.60 | +1.9% | +39.8% | 89% | 2,028.00 | fetched |
| Volvo B | 319.70 | +3.3% | -13.0% | 56% | 4,156.10 | fetched |
| Atlas Copco B | 175.40 | -2.4% | -3.2% | 79% | 4,735.80 | fetched |
| AstraZeneca | 1,675.50 | +6.4% | +9.0% | 45% | 13,404.00 | fetched |
| Xetra-Gold (physically-backed gold ETC, ISIN DE000A0S9GB0) | no data | no data | no data | - | 5,689.22 | FETCH FAILED |
| Alfa Laval | 571.40 | +2.0% | -0.5% | 86% | 5,142.60 | fetched |
| ABB | 915.40 | -3.1% | -3.3% | 66% | 3,661.60 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| Valour Bitcoin Zero SEK (certificate, ISIN CH0585378661) | no data | no data | no data | - | 11,031.00 | FETCH FAILED |
| ETH (self-custody wallet) | 24,281.56 | -6.0% | no data | - | 12,185.70 | fetched (CoinGecko, converted via sek_per_eur) |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high.* Crypto context
(CoinGecko): ETH 2,168.50 EUR, −4.9% vs the previous snapshot, −5.3% over 7 days, −7.3%
over 30 days, −48.7% vs its all-time high.

**What moved, and whether it matters:**
- **AZN.ST +6.4%**, the largest move, from 23% to 45% of its range. The thesis is INTACT,
  and the move is in its favour. It does make last week's unfunded 1-share BUY ~101 SEK
  dearer (1,574.50 → 1,675.50), and the stock reports 10-30.
- **ABB −3.1% the day before its print.** This is not evidence for or against the lapsed
  SELL. It lowers the proceeds by ~118 SEK.
- **Volvo B +3.3%**, still −13.0% vs cost. The thesis is TOO_EARLY and the 10-23 print is
  the test. Nothing contradicts it.
- **ETH −6.0%** shrinks the crypto sleeve on its own (§6, D-c).
- The index funds are at book value, and gold and BTC are at stale marks, as every week.
  That is 152,910 SEK, or 67.9% of capital, unrepriced (this memo's arithmetic: 119,999 +
  16,191 + 5,689.22 + 11,031).

---

## 2. Scout health

```
Universe    624
Fetched     621  (cache 0, new 625, failed 4)
Ranked      613
Candidates  74   (holdings 9, watchlist 30, new 35)
Focus       24
Screened    74
Passed      39
Missing     17
Failed      18
Status      VALID
```
(`scout.json` also reports `share_class_collapsed` 6 and `suspect_values` 8.)

**Reading.** The status is VALID: the funnel ran and nothing upstream needs distrusting
before §3. Scout ran only because the orchestrator overrode a launch prompt that omitted
it (lead item 3).

**"New" is not "first seen".** 35 rows carry `source=new`. I checked them against all 9
runs in `candidate_history.csv`:
- **Two are genuinely first-seen in the history file: AZA.ST (rank 14) and FSLR (rank
  43).** OPEN_ITEMS.md S21 records AZA.ST in a 2026-08-24 run, which predates this file's
  first row (08-25).
- **Three are returnees:** BURE.ST (last seen 09-28), FIX (09-28) and PLTR (10-05).
- **Three left:** FANG, GPN and SMCI.
- This is the third explicit catch of the miscount (§9).

**The frozen head, measured rather than asserted:**
- **APP has been rank 1 in 9 of 9 runs.**
- **NVDA, SNDK, MA, V and VICI have been top-10 in 9 of 9.** MU has been top-10 in 8 of 8
  since first seen (08-31).
- **TSM fell 7 → 29, its first exit from the top 10.** Its `roic_pct` (257.3%) is now
  suspect-flagged and withheld, so `z_quality` fell from 1.930 to 1.520. Its
  `fcf_yield_pct` rose from 31.08% to **56.22% and is still unflagged** (§9).
- **INVE-A.ST fell 12 → 38.** Yahoo's holding-company fields moved: operating margin
  88.7% → 48.5%, and revenue growth is now −60.8% against a ttm "revenue" of 282B SEK
  (FY2025: 64.8B). Last sweep suspected its rank rested on an artifact. The artifact
  changed, and the rank changed with it. The business did not.

**Suspect values withheld from lens scoring (8):**
- ABB.ST `price_to_book` 103.88
- SNDK and MU `revenue_growth` 371.6% / 379.3%
- CMCSA `peg` 142.98
- TSM `roic` (new this sweep)
- INDU-C.ST `operating_margin` 102.5%
- ASML `price_to_book` 1,409 and `roic`
- KINV-B.ST `price_to_sales`

**Not flagged, and wrong or suspected wrong:**
- **AZN.ST `price_to_sales` 41.54 / `price_to_book` 50.68.** Same USD/SEK mismatch as
  ABB (S32). The `valuation` lens caught it; FX-corrected ~4.2x / ~5.1x.
- **TSM `fcf_yield_pct` 56.22%.**

---

## 3. Top opportunities

### 3a. The seven voices (independent passes)

Each voice triaged all 74 rows on its own columns before drafting. A name pulled in from
outside `focus=Y`, or argued for against its screen flag, is labelled as such.

#### Voice 1 — Fundamental / Quality

*Triage (`z_quality`):* APP 2.549, NVDA 2.540, SNDK 2.509, MU 2.501, MA 2.256, V 1.975,
TPL 1.807, AZA.ST 1.771, MO 1.763, LLY 1.762, TSM 1.520, EVO.ST 1.384, GOOGL 1.384.
*Moat, management and capital allocation are qualitative here; no fetched field measures
them.*

- **BUY V, 8.**
  - Why: ROIC 41.5%, ROE 61.2%, margins 50.8/66.1, net debt/EBITDA 0.32, revenue +14.4% on
    a 10.9% CAGR. Every quality field is unchanged.
  - The price rose 6.6% in a week (375.10 → 399.75, now 95% of range). That is a valuation
    question, not a quality one.
  - Risk: regulation of interchange fees (qualitative).
  - Invalidated by: ROIC below 30%, or two prints of mid-single-digit growth.
- **BUY MA, 7 (pulled in against its FAIL).**
  - Why the FAIL misleads: D/E 439.58 comes from buyback-driven negative equity. Net
    debt/EBITDA is 0.59.
  - Underneath: ROIC 56.1%, margins 46.3/61.1, revenue +14.1% on a 13.8% CAGR.
  - Invalidated by: net debt/EBITDA above 2.0.
- **BUY NVDA, 7.**
  - Why: ROIC 59.2%, ROE 117.2%, margins 63.7/66.2, net cash (−0.12).
  - Held at 7: FCF yield 0.81% against an earnings yield of ~3.69% (1/27.07). Only about
    22% of reported earnings reach free cash.
  - Invalidated by: FCF yield still below 1% after the 11-17 print (date carried from the
    2026-10-05 calendar file).
- **BUY ATCO-B.ST (holding), 6.**
  - Why: still the best business held. ROIC 39.7%, ROE 25.7%, operating margin 20.6%, net
    debt/EBITDA 0.50, FCF yield 3.01% (SEK over SEK, clean).
  - Invalidated by: ttm revenue growth turning negative at the **10-22** print, which is
    also its own break condition.
- **BUY AZA.ST, 5 (first-seen).**
  - Why: ROE 36.9%, ROIC 36.9%, margins 53.6/65.4, revenue +12.1% on a 14.8% CAGR, beta
    0.631, D/E 3.89.
  - Qualitative: Avanza's position as a large Swedish retail platform is a moat argument.
    No fetched field measures it.
  - Risk: forward P/E 28.09 sits *above* trailing 19.84, which implies roughly a 29% EPS
    decline. Net debt/EBITDA is null and would mean little for a broker anyway.
  - Invalidated by: the next print confirming the decline.
- **SELL ABB.ST, 4 (down from 5).**
  - Why: FCF/revenue is still 4.4% (1.5705B / 35.752B, both USD), the thinnest
    conversion held.
  - Lower because ROE 32.6% and net debt/EBITDA 0.46 describe a sound business, and my own
    invalidation test (FCF/revenue above ~8%) gets its data point in 24 hours.
- **Declined:**
  - **APP.** ROE 203.7% on D/E 111.13 overstates quality. The ROIC of 65.5% is real, but I
    will not rank a company on leverage-inflated ROE.
  - **MU/SNDK.** Suspect growth fields and operating margins of 80.7/78.5% read as peak
    cycle. The prices fell **−10.1% / −13.3%** this week (1,035.84 → 931.24; 1,609.46 →
    1,394.83). The market is reading the same thing.
  - **EVO.ST.** Quality is real (ROIC 23.1%, net cash) but revenue is −1.2%.
  - **TPL.** FAIL on a 46.6x trailing multiple, and a forward figure nobody trusts.

#### Voice 2 — Valuation

*Triage (`z_value`):* CHTR 1.882, CMCSA 1.871, FIS 1.786, ALL 1.747, CORE-B.ST 1.669, EG
1.633, FISV 1.618, BURE.ST 1.504, DOM.ST 1.487, MEKO.ST 1.422, GM 1.358, DIOS.ST 1.306,
INDU-C.ST 1.232, EIX 1.079, INVE-A.ST 1.064, EXE 1.064, FSLR 1.044.
*Named gap: no EV/EBITDA or EV/EBIT. Where I lean on net debt/EBITDA, I say so.*

- **BUY VICI, 7 (down from 8).**
  - Why: 9.18x trailing, 7.89x forward, 7.8% dividend, 67.5% net margin, revenue +5.7% on
    a 15.5% CAGR, PASS. No fetched field has deteriorated in 9 runs.
  - Lower only because the price rose 2.9% (22.79 → 23.46) and the range position went
    from 4% to 11%. The margin of safety narrowed; nothing broke.
  - Approximation: net debt/EBITDA 4.82 is heavy. I quote no enterprise multiple.
  - Invalidated by: a dividend cut, or net debt/EBITDA above 6.
  - Missing: FFO, AFFO and lease coverage, the metrics REITs are actually priced on.
- **BUY NVDA, 7.**
  - Why: forward 13.45x against trailing 27.07x on +105.9% revenue. The forward multiple
    fell again (14.41 → 13.45) as the price dropped 5.7% (230.48 → 217.23).
  - I do not lean on PEG 0.26.
  - Invalidated by: forward P/E rising above trailing.
- **BUY AZN.ST (holding), 6 (down from 7).**
  - Why: PEG 1.16. The `valuation` lens's FX-corrected P/S ~4.2x and P/B ~5.1x are not
    stretched for large-cap pharma. FX-corrected FCF yield ~2.0% (0.20% × 10.0039, S32).
  - Lower: the price rose 6.4% to 45% of range, so last week's entry argument is half
    used.
  - Missing: `forward_pe` in **9 of 9** runs (S21).
  - Invalidated by: PEG above 1.6.
- **BUY FSLR, 4 (pulled in, rank 43, first-seen).**
  - Why: the cleanest set of cheap fields in the value list. 10.64x trailing, 7.33x
    forward, FCF yield 8.62% (USD over USD), net cash (net debt/EBITDA −0.64), D/E 1.88,
    7% of range.
  - FCF is ~92% of earnings (8.62% FCF yield vs 9.40% earnings yield). Few cheap names in
    this file convert like that.
  - Held at 4: revenue −3.7% ttm; one run of history.
- **SELL ABB.ST, 4 (down from 5).**
  - Why: 35.34x trailing; forward 34.54x sits only 2.3% below it, implying flat EPS on
    14.2% revenue growth.
  - Against my own case, and stronger than last week: PEG 1.25 is now the *lowest* of the
    three industrials held (ALFA 1.76, ATCO 2.15).
- **SELL ATCO-B.ST, 4 (down from 5).**
  - Why: 32.38x trailing, PEG 2.15, still the richest growth-adjusted multiple held.
  - Lower because the range position eased from 88% to 79%.
  - Invalidated by: PEG below 1.5.
- **Testing the `valuation` lens's "Cheap" verdicts:**
  - **DIOS.ST / BALD-B.ST: disagree.** A 7–9x P/E on a property company carrying net
    debt/EBITDA of 10.07 / 16.13 is the leverage, priced. The lens's "Riksbank easing"
    argument has also weakened. Swedish CPI rose 0.3% → 1.1%, cutting the real policy
    rate from +1.45pp to +0.65pp, which leaves less room to cut.
  - **FIS: disagree, as last week.** 29.1% one-year growth on a −9.8% three-year CAGR is
    a base effect, and the PEG of 0.19 inherits it. Net debt/EBITDA 5.82.
  - **APP: no view from me.** The file holds nothing that tells mispricing from
    deterioration.
- **Cheap for a reason, not picks:**
  - **CHTR, CMCSA.** Revenue −1.7% / −1.2%.
  - **ALL.** Forward 8.82 vs trailing 4.96 implies an earnings halving.
  - **EG.** Revenue −11.3%.
  - **TPL.** Forward 4.80 is not credible.
- **Flag, not a pick: EVO.ST's FCF yield of 0.63% looks like the S32 currency bug.**
  Evolution reports in EUR and lists in SEK. ×11.1974 gives ~7.0%. If verified, that
  would make it the cheapest quality name in the set. Unverified hypothesis; §9.

#### Voice 3 — Growth / Opportunity

*Triage (`z_growth`):* NVDA 1.922, BE 1.797, AVGO 1.760, PLTR 1.751, APO 1.731, AXON
1.600, DASH 1.540, FIX 1.524, MU 1.488, LLY 1.467, APP 1.444, AMD 1.419.
*Forward below trailing:* MU 4.25/11.82, SNDK 4.88/17.62, TPL 4.80/46.60, MEKO.ST
4.80/30.04, DOM.ST 5.17/23.21, GM 5.56/37.65, APO 10.38/39.71, FSLR 7.33/10.64, APP
12.97/20.46, NVDA 13.45/27.07, VOLV-B.ST 13.07/18.50, AVGO 16.95/41.99, TSM 17.64/26.74,
META 20.48/26.73, FIX 23.90/35.41, LLY 26.63/42.20.
*Named gaps: no TAM, earnings-revision or market-share data.*

- **BUY NVDA, 8.**
  - Why: revenue +105.9% on a 100.0% CAGR, forward at half of trailing, no suspect flag.
  - Risk: a pause in hyperscaler capex (qualitative; no backlog data).
  - Invalidated by: growth below 40%, or forward above trailing.
- **BUY FIX, 6 (pulled in, rank 28, returnee; now PASS).**
  - Why: revenue +50.3% on a 30.0% CAGR, forward 23.90x vs 35.41x, PEG 0.48, ROIC 42.1%,
    net cash (−0.77). FCF yield 3.64% *exceeds* its earnings yield (2.82%).
  - This is measured growth with clean fields, and the price is −9.9% since 09-28
    (1,643.39 → 1,481.27).
  - Risk: margin 12.8% is thin for the multiple; beta 1.659.
  - Invalidated by: growth below 25%.
- **BUY APP, 5.**
  - Why: +52.8% revenue at a 77.7% operating margin, forward 12.97x vs 20.46x. The price
    has been flat for three weeks (281.31 → 280.12 → 279.29).
  - Decided by: the **11-04** print (carried from the 10-05 calendar).
- **BUY LLY, 5 (down from 6; pulled in, rank 17).**
  - Why: revenue +47.7% on a 31.7% CAGR, operating margin 54.2%, forward 26.63x vs
    42.20x.
  - Lower because the price rose 7.0% (1,169.60 → 1,251.61), tipping it into FAIL on
    trailing P/E (42.2 > 40). D/E 162.07.
- **BUY VOLV-B.ST (holding), 5.**
  - Why: forward 13.07 vs trailing 18.50, ttm revenue +2.7% after a two-year decline.
  - The **10-23** print is the test.
- **SELL SHB-A.ST, 4.** Revenue −3.8%, z_growth −1.274 (the worst held), forward 13.48
  above trailing 12.90. Immaterial at one share.
- **ABB.ST: SELL flag withdrawn.** I cannot defend selling 14.2% measured revenue growth
  at a PEG of 1.25 on the strength of one estimate field (forward P/E) that I trust no
  more than the PEG. Tomorrow's print settles which estimate was right.
- **Declined:**
  - **MU/SNDK.** Suspect growth; −10.1% / −13.3% this week.
  - **BE.** −13.4% this week (272.82 → 236.30), 291x trailing.
  - **APO.** Forward 10.38 vs 39.71 implies a ~3.8x EPS jump the data cannot reconcile.
  - **AVGO.** 85.5% vs a 24.4% CAGR, likely an acquisition base effect.
  - **PLTR, AXON, DASH.** 99–162x trailing.
  - **META.** Unchanged growth-only case; FIX is the better version of it this week.

#### Voice 4 — Defensive / Risk

*Triage (lowest `beta`):* SAAB-B.ST 0.03, ALL 0.138, BETS-B.ST 0.17, JNJ 0.206, AZN.ST
0.212, ABBV 0.228, EG 0.259, CME 0.27, KO 0.318, TEL2-B.ST 0.34, PEP 0.364, PG 0.377,
NOVO-B.CO 0.384. *Lowest leverage (D/E):* TPL 1.077, SNDK 1.277, FSLR 1.88, EVO.ST 2.13,
INDU-C.ST 2.821.

**The scenario I position for:** a hawkish re-pricing at the **10-27/28 FOMC**.
- US CPI re-accelerated from 3.71% (the 08-01 print) to **4.02%** (09-01). Fed funds at
  3.75% is now a **negative** real rate (−0.27pp).
- The curve flattened from +0.47 to +0.33 (10y 5.10, 2y 4.77).
- VIX at 16.46 is still pricing calm.
- That shock would land on a portfolio whose −30% tolerance no traceable file has tested
  (S26).

- **BUY AZN.ST (holding), 7.**
  - Why: beta 0.212, net debt/EBITDA 1.35, operating margin 23.5%, revenue up four fiscal
    years running.
  - Invalidated by: a dividend cut, or operating margin below 20% at 10-30.
- **BUY CME, 5 (down from 6).**
  - Why: beta 0.27, net debt/EBITDA 0.33, net margin 63.4%. Rate re-pricing is
    rate-futures volume (qualitative; no volume data).
  - Lower because the price rose 4.7% (276.44 → 289.46). PEG 4.97 on 0.8% growth.
- **BUY JNJ, 5 (pulled in, rank 55).**
  - Why: beta 0.206, net debt/EBITDA 0.83, forward 21.83x vs 38.78x, revenue +5.9%.
  - Risk: 3-year CAGR −0.3%, so this is stability, not growth. Litigation is
    qualitative and unmeasured.
- **BUY ERIC-B.ST, 4 (pulled in, rank 57).**
  - Why: net cash (−0.36), FCF yield 8.39% (SEK over SEK, clean), ROIC 20.6%, beta 0.511,
    44% of range.
  - Risk: 3-year CAGR −4.5%, and `forward_pe` is MISSING (S21).
- **SELL VOLV-B.ST, 4.** D/E 147.35 and net debt/EBITDA 3.8 make it the most leveraged
  holding, at beta 1.0. A risk view only; the 10-23 print may make it moot.
- **MO dropped from my list.** It is at 86% of range after another +3.4%, and the yield
  argument has thinned two weeks running.
- **Attacking this sweep's BUY cases:**
  - **NVDA / APP / FIX.** Betas 2.216 / 2.557 / 1.659.
  - **VICI.** Net debt/EBITDA 4.82 into an FOMC with CPI rising.
  - **FIS.** Net debt/EBITDA 5.82.
  - **DIOS.ST / BALD-B.ST.** 10.07 / 16.13; not investable on leverage.
  - **CHTR.** D/E 441.58.
  - **AZA.ST.** A forward P/E implying −29% EPS is an earnings-risk flag, not a
    defensive one.
- **Not flagging ABB.ST.** Net debt/EBITDA 0.46, beta 0.982. There is no risk case.

#### Voice 5 — Contrarian / Risk Taker

*Triage (`pct_52w_range`):* CORE-B.ST 3, APP 4, FISV 4, CHTR 5, BALD-B.ST 7, DOM.ST 7,
FSLR 7, CMCSA 10, PEP 10, DIOS.ST 11, VICI 11, FIS 11, EIX 15, BETS-B.ST 16, EXE 17.

- **BUY VICI, 6.**
  - Why: the discount-rate story got its first confirming observation. Last week I said
    the price was tracking the 10-year, not the asset. This week the 10-year eased (5.22
    → 5.10) and the price rose 2.9%. The fundamentals are unchanged across 9 runs.
  - One week is one observation, so conviction holds.
  - Invalidated by: a dividend cut or tenant default at the 10-28 print (date carried from
    the 10-05 calendar).
- **BUY FSLR, 5 (first-seen).**
  - Why the pessimism looks wrong: at 7% of range, the market is pricing a business in
    decline (revenue −3.7%). But the forward multiple (7.33 vs 10.64) says earnings are
    expected to rise ~45%. FCF is ~92% of earnings, and the balance sheet is net cash.
  - The pessimism is plausibly US solar-policy risk (qualitative; no policy data
    fetched). A net-cash balance sheet is what lets a company wait out a policy cycle.
  - Risk: beta 1.794; a policy shock that turns the forward estimate into fiction.
  - Invalidated by: forward P/E rising above trailing, or FCF yield turning negative.
  - Missing: insider data (EDGAR 403), earnings date (holdings-only calendar).
- **BUY APP, 4.** A 77.7%-margin, +52.8% grower held at 4% of range. Flat for three weeks;
  S29 still hides the 52-week endpoints.
- **BUY PEP, 4 (down from 5).** 10% of range, 4.5% dividend, 5.05% FCF yield, beta 0.364.
  Revenue +5.6% has not turned. D/E 230.72.
- **SELL flags: none.** INVE-A.ST is a durable hold (D-b); I do not reopen it.
- **Declined (penalty deserved):**
  - **CHTR/CMCSA.** The fundamentals agree with the price.
  - **CORE-B.ST, DOM.ST, BALD-B.ST, DIOS.ST.** The leverage explains the range position.
  - **FISV.** Too many MISSING fields to judge.
  - **NOVO-B.CO.** Forward 11.83 above trailing 9.91; consensus sees a real slowdown.

#### Voice 6 — Macro / Regime

*Regime (from `macro-regime`): TRANSITIONAL, tilted risk-on for now, not for the
quarter.* Changes vs last sweep:
- **US:** 10y 5.22 → 5.10, 2y 4.75 → 4.77, spread +0.47 → +0.33. CPI 3.71 → **4.02**, so
  the real fed funds rate is now **−0.27pp**.
- **Dollar and FX:** DXY 121.38 → 121.60. SEK/USD 10.0688 → 10.0039 (the krona firmed
  ~0.6%; dated 10-09).
- **Sweden:** Riksbank 1.75% against CPI 1.1%, a real rate of +0.65pp (from +1.45pp).
- **Sentiment:** VIX 16.46; crypto Fear & Greed 69 → 59.

*Named gap: no commodity-price and no credit-spread data.*

- **BUY AZN.ST (holding), 6.** SEK-listed, low-beta, USD-reporting. The right side of a
  rising-inflation, strong-dollar regime. Revenue-currency mix is unmeasured.
- **BUY V, 5.** Revenue is a share of nominal spending, so 4.02% CPI is revenue. The
  stronger krona cut the SEK entry price ~0.6%; the stock's +6.6% more than undid that.
- **BUY CME, 5.** An FOMC re-pricing is rate-futures volume (qualitative).
- **Explicit regime calls, stated rather than buried:**
  - **VICI: last week's regime-only downgrade is relaxed, not removed.** The 10-year
    moved away from the 5.5% retirement trigger. But a negative real rate with CPI rising
    is exactly the setup for a hawkish 10-28 surprise, on VICI's own print date.
  - **Swedish property (DIOS.ST, BALD-B.ST).** The rising Swedish CPI weakens the
    rate-cut argument the `valuation` lens made for them.
  - **AZA.ST.** A Riksbank cutting path compresses a broker's interest income. That is
    consistent with its forward P/E sitting above trailing (qualitative).
  - **Crypto.** DXY rose again and Fear & Greed cooled 69 → 59. Sentiment and dollar no
    longer point opposite ways; both are now less supportive. This argues against adding.
    It does not size a trim (D-c).
  - **NVDA, APP, FIX, LLY.** Long duration at a 5.10% 10-year. The businesses are fine.
  - **Swedish industrials (ABB 35.3x, ATCO 32.4x, ALFA 29.1x).** Wrong side of the
    10-year; their exporter SEK-translation tailwind is a currency mechanic, not demand.
- **SELL flags on macro grounds alone: none.**

#### Voice 7 — Copycat / Smart Money

**Coverage first.**
- **US:** SEC EDGAR CIK mapping returned 403 again, so there is **zero US insider data**.
  Nothing on any US candidate, including VICI, NVDA and FSLR.
- **Sweden:** Finansinspektionen covered 7 issuers (Handelsbanken, Investor, Volvo, Atlas
  Copco, AstraZeneca, Alfa Laval, ABB). **No publication is dated after 17/09/2026 for
  any of them, now five weeks.**
- No candidate issuer was pulled. AZA.ST, the one Swedish first-seen name, has no read.
- **Institutions:** `MISSING: institutional ownership not fetched`.

This voice reviews holdings only and contributes nothing to discovery, a second week
running.

- **BUY AZN.ST, 5 (down from 6).**
  - Why: CEO Soriot bought 60,000 at 121.02 GBP and Chairman Demare 2,500 at 121.21 GBP,
    both on 14/09, at real prices. The CFO's 0.00-price lines are vestings and carry no
    signal.
  - Lower: five weeks old and not extended. GBP/SEK is not fetched, so I cannot place
    today's 1,675.50 SEK against their entry.
- **BUY ALFA.ST (holding), 4 (down from 5).**
  - Why: CFO Ekström bought 1,000 at 547.49 on 11/09; today's 571.40 is 4.4% above. The
    10 rows shown are all acquisitions (2023-12 to 2026-09).
  - Lower: nothing new.
- **BUY INVE-A.ST (holding), 4 (down from 5).**
  - Why: Cederholm 1,500 at 395.90 (14/09), Lund 1,000 at 399.13 (09/09), Elfving 850 at
    411.55 (01/09). Today's 405.60 sits inside that range, with zero disposals.
  - Lower: five weeks with nothing new.
- **Reads that are not calls:**
  - **ABB.ST.** Disposals only: Terwiesch 18,799 / 10,000 / 20,000 (29/07–13/08) and
    Meline 2,456. **Nothing since 13/08, now negative on a fourth pull.** The May
    "acquisitions" are fee allotments at an identical 78.42 CHF.
  - **VOLV-B.ST.** Stjernholm's 27/07 cluster sits at ~359–361. Today's 319.70 is ~11%
    below it. Volvo Car AB rows (Nota, Severinson) are discarded.
  - **SHB-A.ST.** Boman's 26/08 cluster sits at 145.55–146.24; today's 151.35 is above.
  - **ATCO-B.ST.** Option exercises with same-day disposals: compensation, not a signal.
- **SELL flags: none.**

---

### 3b. Chairman's Top 5

Mechanical rank is not used as evidence below. Scorecard pillar 3 measures the rank as
non-predictive (S33). Rank history is reported for persistence only.

#### #1 OPPORTUNITY: ABB.ST — ABB (the D-a window closes at tomorrow's print)

**CATEGORY:** holding

**RANK HISTORY:** 65 now; 64 (10-12). **0 of 9 runs in the top 10.**

**VOICES IN FAVOR (of selling):**
- Fundamental, 4: FCF/revenue 4.4%.
- Valuation, 4: 35.3x trailing with flat forward EPS.

**VOICES AGAINST / CAUTIOUS:**
- Growth: *withdrew* its SELL; it cannot sell 14.2% revenue growth at PEG 1.25.
- Defensive: no risk case.
- Copycat: insider clause negative on a fourth pull.
- Macro: multiple on the wrong side of the 10-year, but no SELL on macro alone.

**STRONGEST CASE FOR (selling):** `thesis-review`'s "would I buy it today?" returns NO for
a third independent re-test, on realized figures that have not moved to the decimal.
FCF/revenue is 4.4%, the same as in August. The forward P/E is still flat against
trailing despite 14.2% revenue growth. No voice argues BUY.

**STRONGEST CASE AGAINST:** Growth's withdrawal plus Valuation's own concession.
- PEG has gone 2.11 (09-07) → 1.31 (10-12) → **1.25**, and is now the lowest of the three
  industrials held.
- `thesis-review` is right that a consensus revision should not overturn realized facts.
  But the SELL is now a *relative-valuation* call resting on two estimate fields that
  contradict each other.
- One of them gets marked to reality tomorrow.

**KEY DISAGREEMENT:** whether to act on a valuation SELL 24 hours before the one event
that tests it.
- Fundamental and Valuation say the realized cash conversion has not changed, so the SELL
  stands.
- Growth says the estimates disagree, and selling the day before they are resolved turns
  a valuation call into an earnings bet.
- I do not resolve this by picking a side. I resolve it by the rule this system wrote for
  exactly this case: the 10-12 call is not renewed.

**DATA GAPS:**
- No EV/EBITDA. FCF is trailing-only.
- P/B 103.9 is a unit mismatch (S32).
- No revisions feed to say whether PEG or forward P/E is current.

Moderate discount.

**CHAIRMAN CONVICTION:** 6, that *not renewing* is correct. This is not a view on ABB's
direction.

**WHAT WOULD CHANGE THIS (the 10-26 test, fixed now so it cannot drift):**
- **Retires the SELL case on merit:** Q3 operating margin clearly above 16.9% **and** a
  forward P/E falling meaningfully below trailing (EPS growth finally priced).
- **Revives it fresh:** FCF/revenue still ~4–5% **and** forward/trailing still flat.

**PORTFOLIO FIT** (from `portfolio`; my arithmetic labelled):
- Industrials are **53.15%** of the 33,278.45 SEK visible stock sleeve, rated ACT.
- Selling to cash takes them to ~47.4% (still ACT). Selling plus 15 VICI takes them to
  ~42.4% (WATCH). Both figures are mine, using the position report's Volvo value of
  4,156.10.
- **Correction to the `portfolio` lens:** the ABB → VICI swap is *not* a two-dimensional
  improvement.
  - It swaps a Swiss line for a US one. Sweden's share of the sleeve moves 48.72% →
    ~48.9%, still ACT (my arithmetic).
  - Selling ABB to cash pushes Sweden to ~54.7%.
  - The swap fixes sector, not geography.
- The trade is tax-free inside the ISK.

**FINAL CALL: NO ACTION from this memo. The 2026-10-12 SELL is not renewed.**
- It stays executable today as last week's decision (all 4 shares, ~3,661.60 SEK at
  915.40).
- If you act, you act on that decision. If you hold through the print, that is recorded as
  your choice.
- Either way, 10-26 decides fresh.

**HORIZON:** Medium

#### #2 OPPORTUNITY: AZN.ST — AstraZeneca

**CATEGORY:** holding

**RANK HISTORY:** 58 now; 57 (10-12). **0 of 9 in the top 10.** The rank is depressed by
`forward_pe` missing in 9 of 9 runs (S21) and the unit-mismatched FCF yield feeding
`z_value` −1.528 (S32).

**VOICES IN FAVOR:**
- Defensive, 7: beta 0.212, four years of rising revenue.
- Valuation, 6: PEG 1.16, FX-corrected P/S/P/B not stretched.
- Macro, 6: right side of the regime.
- Copycat, 5: CEO and Chairman open-market buys, 14/09.

**VOICES AGAINST / CAUTIOUS:**
- No SELL from any voice.
- Fundamental did not pick it this week: ROIC 13.1% is good, not excellent.
- Valuation and Copycat both lowered on the +6.4% move and aging evidence.

**STRONGEST CASE FOR:** Defensive's. In the scenario this memo is worried about (a hawkish
FOMC with CPI rising), a 0.212-beta, 1.35x-levered, still-growing pharma is what you
want more of. Four voices cite four independent fields.

**STRONGEST CASE AGAINST:** Valuation's own downgrade. Last week's argument was "23% of
range, cheaper entry". That is now 45% of range, with the stock up 6.4% in a week and a
print on 10-30. The entry has been half spent while P3 sat unexecuted.

**KEY DISAGREEMENT:** none on direction; the disagreement is on price.
- Defensive holds at 7 because the reason to own it is its behaviour in a shock.
- Valuation drops to 6 because the reason to *add* was partly the price.
- I side with the lower number for sizing, and keep it a 1-share add.

**DATA GAPS:**
- No forward multiple in 9 runs.
- GBP/SEK is not fetched.
- Revenue-currency mix is unknown.

Moderate discount.

**CHAIRMAN CONVICTION:** 6 (down from 7)

**WHAT WOULD CHANGE THIS:** operating margin below 20% at the **10-30** print, or a
Soriot/Demare disposal.

**PORTFOLIO FIT** (from `portfolio`):
- Healthcare is **40.28%** of the visible sleeve (WATCH, >30%), all of it this one name.
- One more share takes it to ~43.1% (my arithmetic), still under 45%.
- AZN is 5.95% of total capital, well inside the 15% cap.
- **Capital check against this sweep's `portfolio`:** ISK cash is **845.43 SEK** (last
  confirmed 2026-08-25, stale). One share costs 1,675.50 SEK. Not fundable today.

**FINAL CALL: BUY** — 1 share. **Execution note: no idle capital confirmed (845.43 SEK ISK
cash). Funded by P3 or the next contribution.** If P3 lands before 10-30, you are buying
ahead of the print. That is acceptable on a Medium horizon; make it a conscious choice.

**HORIZON:** Medium

#### #3 OPPORTUNITY: VICI — Vici Properties

**CATEGORY:** new candidate (`source=new`: not held, not watchlisted; in the funnel since
2026-08-25)

**RANK HISTORY:** 9 now; 10 (10-12). **9 of 9 runs in the top 10.**

**VOICES IN FAVOR:**
- Valuation, 7: 7.89x forward, 7.8% yield, no deterioration in 9 runs.
- Contrarian, 6: the discount-rate story got its first confirming week.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: net debt/EBITDA 4.82 into an FOMC with CPI rising.
- Macro: regime downgrade relaxed, not removed; the FOMC statement lands on VICI's print
  date.
- Copycat: no data.

**STRONGEST CASE FOR:** Valuation's. A 67.5%-margin landlord still growing revenue (+5.7%
on a 15.5% CAGR) at 7.89x forward and a 7.8% yield, with a PASS screen, unchanged on
every fetched field for 9 weeks.

**STRONGEST CASE AGAINST:** Defensive's. US CPI just rose to 4.02% with the Fed's real
rate negative. If the FOMC re-tightens on 10-28, a 4.82x-levered REIT re-prices on the
same day as its own print. The rate move that helped this week can reverse in one
statement.

**KEY DISAGREEMENT:** whether this week's +2.9% on a −12bp 10-year confirms the
mispricing or just confirms the rate sensitivity.
- Both readings are true at once.
- The pre-committed retirement observable (10-year ≥5.5% with the price still falling)
  moved *away* from firing. That holds conviction; it does not raise it.

**DATA GAPS:**
- No FFO, AFFO, EV/EBITDA or lease coverage.
- Zero US insider data. Institutional ownership not fetched.
- The 10-28 print date is carried from the 10-05 calendar file.

Heavy discount.

**CHAIRMAN CONVICTION:** 5

**WHAT WOULD CHANGE THIS:** the 10-year at ≥5.5% with the price still falling retires it.
A dividend cut at the 10-28 print kills it.

**PORTFOLIO FIT** (from `portfolio`):
- Real Estate is at 0% and the US is at 0% of the visible sleeve, so it diversifies both
  sector and country. It "concentrates cap-tier" like everything else.
- **Price in SEK:** 23.46 × 10.0039 = **234.69 SEK**. 15 shares cost 3,520.35 SEK, one
  fewer than last week's 16 because the price rose.
- **Two funding routes, now decoupled:**
  - (a) the ABB proceeds, if you execute last week's SELL today: 3,661.60 SEK covers 15
    shares.
  - (b) P3's remainder. `portfolio` leaves ~10,035 SEK of the P3 proceeds for an equity
    pick the Council names.
- Without the ABB sale, adding VICI does not lift Industrials out of ACT (~48.1%, my
  arithmetic). It does help Sweden's share.
- Confirm it is orderable in the Avanza ISK, and check how US dividend withholding is
  treated there.

**FINAL CALL: BUY** — 15 shares, from either route. **Execution note: no idle capital is
confirmed today. Route (a) exists only if ABB sells before the print; otherwise this
waits on P3.**

**HORIZON:** Medium

#### #4 OPPORTUNITY: NVDA — Nvidia

**CATEGORY:** watchlist

**RANK HISTORY:** 2 now; 2 (10-12). **9 of 9 in the top 10.**

**VOICES IN FAVOR:**
- Growth, 8: +105.9% on a 100% CAGR, forward at half of trailing.
- Valuation, 7: forward 13.45x, down again on a −5.7% price.
- Fundamental, 7: ROIC 59.2%, net cash.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: beta 2.216.
- Macro: duration at a 5.10% 10-year.
- Fundamental's own caveat: FCF is ~22% of earnings.

**STRONGEST CASE FOR:** Growth's. The cleanest forward/trailing signal in the set, no
suspect flag and no screen penalty. This week the price fell while the forward multiple
compressed (14.41 → 13.45). The market paid less for the same measured growth.

**STRONGEST CASE AGAINST:** Fundamental's. FCF yield 0.81% against a 3.69% earnings
yield, USD over USD, so the gap is real. Reported earnings are not yet cash. Until they
are, part of the "cheap forward multiple" is cheap on accruals.

**KEY DISAGREEMENT:** three voices see the cheapest measured growth in the set; one says
the earnings quality is unproven. Not reconciled. The 11-17 print is the test.

**Why this moves from HOLD-WATCH to BUY without NVDA changing much:** last week's WATCH
rested on capital and on the untested drawdown tolerance. `council.md` is explicit that
pending funding is never a reason to downgrade merit. And one share (~1% of capital) does
not move the portfolio's drawdown profile in a way S26's absence makes material. That was
my error last week, corrected here.

**DATA GAPS:** no revisions or backlog data; PEG is not relied on; no US insider data; the
11-17 date is carried.

**CHAIRMAN CONVICTION:** 6

**WHAT WOULD CHANGE THIS:** FCF yield moving toward the earnings yield after the 11-17
print raises it. Forward P/E rising above trailing kills it.

**PORTFOLIO FIT** (from `portfolio`): adds the first Technology line, and a new country,
to the visible sleeve; "concentrates cap-tier".
- One share costs 217.23 × 10.0039 = **2,173.15 SEK**.
- **Capital check:** ISK cash is 845.43 SEK. Not fundable today.
- After P3 (net ~14,177 SEK after the 4% spread, plus 845.43 ISK cash = ~15,023 SEK):
  - gold tranche 2: 5,578
  - AZN: 1,675.50
  - VICI via route (b): 3,520.35
  - NVDA: 2,173.15
  - Remainder: ~2,075 SEK to Avanza Global.
  - All of this is my arithmetic on `portfolio`'s figures.

**FINAL CALL: BUY** — 1 share. **Execution note: no idle capital confirmed — fund from
P3, last in the queue behind gold tranche 2, AZN and VICI.**

**HORIZON:** Medium

#### #5 OPPORTUNITY: FSLR — First Solar (discovered this sweep)

**CATEGORY:** new candidate (discovered this sweep, first appearance in 9 runs of
`candidate_history.csv`)

**RANK HISTORY:** 43, first seen.

**VOICES IN FAVOR:**
- Contrarian, 5: the market prices decline while the forward multiple prices a ~45% EPS
  rise, on net cash.
- Valuation, 4: the cleanest cheap fields in the value list; FCF ≈ 92% of earnings.

**VOICES AGAINST / CAUTIOUS:**
- Growth: did not pick it (revenue −3.7%).
- Defensive: beta 1.794.
- Macro: no policy or commodity data to assess the obvious risk.
- Copycat: no data.

**STRONGEST CASE FOR:** Valuation's. Net cash, a 7.33x forward multiple, and an 8.62% FCF
yield that matches its earnings. In a file full of cheap names that are cheap because of
leverage (DIOS, BALD, CHTR, FIS), this is the one cheap name with no balance-sheet
excuse.

**STRONGEST CASE AGAINST:** that the pessimism is not about the balance sheet at all.
Revenue is falling and the stock sits at 7% of range. The probable cause, US solar
policy, is in no file this system fetches. A forward estimate is only as good as the
policy it assumes, and nothing here tests that.

**KEY DISAGREEMENT:** is a forward/trailing gap on a falling-revenue business evidence of
mispricing, or the same stale-estimate pattern that made GM, TPL and APO untrustworthy?
- FSLR's gap is 1.45x, not 4–10x.
- It comes with real FCF.
- That makes it more credible than those names, but not proven.

**DATA GAPS:** one run of history, no earnings date, no insider data, no policy data.
Heavy discount.

**CHAIRMAN CONVICTION:** 4

**WHAT WOULD CHANGE THIS:** a second and third run holding the forward multiple below
trailing, with FCF yield still above ~7%, raises it to a BUY case. Forward rising above
trailing ends it.

**PORTFOLIO FIT** (from `portfolio`'s pattern for US Technology names): diversifies sector
and country; concentrates cap-tier. One share costs 178.81 × 10.0039 ≈ 1,788.81 SEK. No
capital is assigned to it.

**FINAL CALL: HOLD-WATCH.** This is discovery working, not a trade yet. Persistence is
the evidence still missing.

**HORIZON:** Medium

### 3c. Other SELL recommendations on current holdings

You get a direct answer to "should I sell anything" every sweep. Beyond ABB.ST (#1):

- **ATCO-B.ST.** Valuation SELL at 4, **declined.**
  - Its break condition (ttm revenue negative) has not been retested since August: the
    +9.1% is byte-identical.
  - The **10-22** print is the first real test, three days out. **NO ACTION.**
- **VOLV-B.ST.** Defensive SELL at 4, **declined.**
  - TOO_EARLY. The **10-23** print and the ~11-03 3-month checkpoint land together.
    **NO ACTION.**
- **SHB-A.ST.** Growth SELL at 4, **declined.**
  - One share, 151.35 SEK. Prints **10-21**. **NO ACTION.**
- **BTC0E.AS.** A sizing question, not a thesis sell. See D-c in §6.
- **ALFA.ST, INVE-A.ST, ETH, Xetra-Gold, Avanza Global, Avanza Auto 3:** no sell flag.
  - ETH cannot be sold cleanly while P1 is open.
  - INVE-A.ST's durable hold (D-b) is unchanged.

**Considered for the Top 5, not placed:**
- **V** (Fundamental 8, Macro 5). Valuation calls it expensive at 95% of range after +6.6%
  in a week. It has the highest single conviction of the sweep, and the price is
  Valuation's unanswered objection.
- **APP** (Growth 5, Contrarian 4). Rank 1 in 9 of 9 runs, flat for three weeks. The
  11-04 print decides it, and S29 still caps it.
- **FIX** (Growth 6). A clean-field returnee. It adds to the ACT-rated Industrials sector,
  which is a fit issue, not a merit one. Watch for persistence.
- **AZA.ST** (Fundamental 5). First-seen quality name, but its forward P/E implies −29%
  EPS.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens:

| Dimension | Grade | Number behind it |
|---|---|---|
| Asset allocation vs targets | WATCH | equity 72.32% vs 80% (-17,289 SEK), cash 11.97% vs 5% (+15,709 SEK), gold 2.52% vs 5% (-5,578 SEK), crypto 10.30% vs 10% (+682 SEK negligible). Driven mainly by the still-unexecuted P3 PayPal conversion sitting as unwrapped cash. Auto 3's equity/FI split is an ESTIMATE (60/40 from its 40-70% factsheet band, not a verified point figure). |
| Equity sector concentration | ACT (partial coverage) | within the 33,278.45 SEK individually-picked sleeve: Industrials 53.15% (ACT, >45%; VOLV-B+ATCO-B+ALFA+ABB=17,695.10 SEK), Healthcare 40.28% (WATCH, >30%; AZN.ST 13,404.00 SEK), Financial Services 6.55% (SHB+INVE-A). CAVEAT: this sleeve is only 20.4% of total equity exposure (33,278.45/162,992.05) — the other 79.6% (Avanza Global+Auto 3) has NO sector look-through data, confirmed gap. |
| Geography (home bias) | ACT (partial coverage) | same sleeve: Sweden 48.72% (ACT, >45%), UK 40.28% (AZN.ST), Switzerland 11.00% (ABB.ST). Same look-through caveat. |
| Currency exposure | UNKNOWN | no revenue-currency breakdown exists anywhere (listing currency ≠ revenue currency: AZN SEK-listed but GBP/USD-revenue, ABB SEK-listed but USD/EUR/CHF-revenue). Only directly observable: PayPal (USD+EUR), gold (EUR-priced), ETH (EUR-quoted). |
| Single-position concentration (max 15%) | ACT | Avanza Global = 53.24% of total (119,999/225,351.51), far above cap. Context: broadly diversified index fund, not idiosyncratic risk, but the rule as written has no fund exception. Next-largest: Auto 3 at 7.18%, AZN.ST at 5.95%. |
| Institution concentration (max 80%) | ACT | Avanza = 82.99% of total. Structural tension: largely a consequence of the system's own wrapper-efficiency priority (ISK consolidation); moving capital elsewhere would cost tax efficiency. |
| Fee drag (max 0.4%) | OK | ≈187.12 SEK/yr, 0.083% blended. No fund over 0.5%. |
| Wrapper efficiency | OK with a caveat | all securities in ISK except frozen immaterial Osteuropafond. 14,767.86 SEK (PayPal) + 12,185.79 SEK (ETH) sit outside any wrapper (already tracked as P3/P1). |
| Drawdown-tolerance fit | WATCH | unverified, no backing file. data/backtests/ confirmed absent this sweep by direct read attempt. S26 unchanged, open. |
| ISK allowance headroom | OK | 187,034.10 SEK vs reportedly 300,000 SEK threshold (verify with Skatteverket, not independently confirmed). |

Total portfolio (from `portfolio`): **≈225,351.51 SEK**. Deployable idle cash: **15,613.29
SEK** (ISK 845.43 + PayPal 14,767.86), before P3's 4% spread.

**Provisional, per `investor_profile.json`:**
- `horizon.primary_goal` is "nature UNCERTAIN", with a 3–7y SOFT horizon.
- `constraints.exclusions` is empty ("None stated yet").
- `reference_targets` still reads 85/10/0/5 with no gold line (last updated 2026-07-20).
  It disagrees with `portfolio.json.targets` (80/10/5/0/5), which `portfolio` correctly
  treats as operative.
- OPEN_ITEMS.md's own 2026-09-14 note said "a third unapplied occurrence should open an
  S-item without further deliberation." The fix has now gone unapplied for five-plus
  sweeps (§9).
- Arithmetic note: `portfolio` carries Volvo at 4,155.10 SEK. The position report gives
  4,156.10 (13 × 319.70). This is immaterial, but it is why my sleeve figures differ from
  `portfolio`'s at the second decimal.

---

## 5. Headline calls

Each needs a decision this session.

1. **ABB.ST: execute last week's SELL today, or let it lapse at tomorrow's print.** This
   memo does not renew it. Holding through is a legitimate choice and is recorded as
   yours. 10-26 decides fresh on Q3.
2. **Execute P3 (PayPal → SEK → ISK), now an 11th-plus sweep.** About 14,177 SEK net at
   the accepted 4% spread. It funds, in order:
   - gold tranche 2 (5,578 SEK)
   - 1 AZN.ST (1,675.50)
   - 15 VICI if ABB did not sell (3,520.35)
   - 1 NVDA (2,173.15)
   - the remainder (~2,075 SEK) to Avanza Global
3. **BUY 15 VICI**, from the ABB proceeds if you sold today, otherwise from P3.
4. **D-c: read one number off Avanza, the current value of your 150 BTC0E.AS units.** Trim
   back to 10% only if it is above **~14,080 SEK** (corrected to your own full-portfolio
   convention).

---

## 6. Open actions vs open decisions

### Open actions (things to go do), by ID

| ID | Status | Action |
|---|---|---|
| **P3** | decided — pending execution (11th-plus sweep) | Convert 1,177.49 USD + 266.88 EUR (14,767.86 SEK per `portfolio`; ~591 SEK spread at 4%) and move ~14,177 SEK to the ISK. Zero the paypal holdings in `portfolio.json`. |
| **S26** | open, top build | Run the shock-window backtest and write it to `data/backtests/` (still absent, per `portfolio`). |
| **P1** | blocked (on you) | ETH cost basis. Blocks any ETH sale or K4 figure. |
| **P9** | open | Delete the phantom AZN OPENING row in the Excel Transactions tab. |
| **P10** | open | Confirm one 5,000 SEK deposit or two (2026-08-17 vs 2026-08-22). |
| **S6** | open, no longer a decision trigger | `data/company_profiles/INVE-A.ST.json`'s `review_history` still ends 2026-07-28; no NAV recorded. |
| — | file hygiene, not an S-item | Replace `investor_profile.json.reference_targets`' 85/10/0/5 with 80/10/5/0/5, or with a pointer to `portfolio.json.targets`. One field, by hand. |

The D-series still has no standalone register (S30 was closed under cap pressure). It is
reconstructed below.

### Open decisions (forks), by ID

**D-a — ABB.ST and its proceeds.** The window closes at tomorrow's print.
- *Option 1 — sell today, buy 15 VICI with the proceeds.* Industrials ACT → ~42.4%
  (WATCH). Trade-off: you act a day before the print on a call this memo did not renew.
- *Option 2 — hold through the print; the call lapses.* Fund VICI from P3 instead.
  Trade-off: Industrials stays ACT (~48.1% with VICI added), and you carry a binary
  earnings outcome on 1.6% of capital.
- *Option 3 — sell today, hold the cash.* Trade-off: Industrials ~47.4% (still ACT),
  Sweden rises to ~54.7%, and cash is already 7pp over target. This option fixes nothing.
- **No pick from this memo.** The pre-commitment forbids restating the 10-12 call, and
  Options 1 and 2 are both defensible on today's data. Option 3 is the one to rule out.

**D-b — Investor A's unmeasurable valuation.** Durable hold since 2026-10-12 (the 10-05
pre-commitment, applied as written).
- Re-checked: `INVE-A.ST.json` holds no NAV figure, so nothing re-opens it.
- The rank fall (12 → 38) comes from Yahoo's holding-company fields changing, not from new
  evidence.
- *Option 1 — keep the durable hold* (selected as default). Trade-off: a 2,028 SEK
  position held without valuation evidence.
- *Option 2 — you record the NAV* from Investor's Q3 report or IR page (~10 minutes).
  Trade-off: your time, for a 0.9% position.
- **Pick: Option 1.** Not re-flagged further.

**D-c — crypto sleeve sizing.** Re-opened on the denominator, and escalated.
- **The correction:** the 10-12 band (trim above 11.5% of the *investable* base, ~11,730
  SEK) used the reading you rejected on 2026-08-17. On your pinned full-portfolio
  convention (`definitions.json`), crypto is **10.30%** at the stale BTC mark. The 11.5%
  band fires only if the 150 units are worth more than **~14,080 SEK** (≈93.9 SEK/unit,
  +27.6% on the 08-21 mark of 73.54).
  - Arithmetic: 12,185.79 + V > 0.115 × (214,320.51 + V).
  - The older 12% trip-wire would fire above ~15,378 SEK.
- **The escalation:** two sweeps running, no Bitcoin price has been fetched at all. The
  snapshot's `crypto` block holds only `ethereum`, although CLAUDE.md's canonical fetch
  command includes `--crypto ethereum,bitcoin`. Without a number the band cannot be
  evaluated.
- *Option 1 — you read the live Avanza value of the 150 units, and the next fetch adds
  `bitcoin`.* Trade-off: one minute of your time, plus a directional proxy every week
  after.
- *Option 2 — keep the band, wait for a number.* Trade-off: a third sweep with an
  unsizable sleeve.
- *Option 3 — drop the band; no action until S26 runs.* Trade-off: an untested tolerance
  with no interim rule.
- **Pick: Option 1.**

---

## 7. Cost of being wrong

| Headline call | If wrong | Realistic SEK downside | Recoverable? |
|---|---|---|---|
| ABB: sell today (Option 1) | Q3 beats and ABB re-rates +15% | ~550 SEK foregone (15% of 3,661.60) | Yes. It can be rebought tax-free in the ISK. |
| ABB: hold through (Option 2) | Q3 misses and ABB falls 15% | ~550 SEK loss | Yes. 10-26 can still sell it. |
| Execute P3 + queued buys | Spread is certain; AZN −30%, NVDA −40% (beta 2.2), gold −20% | ~591 SEK spread + ~503 + ~869 + ~1,116 | The spread, no, and it recurs every ~2 months while P3 waits. The positions, yes, with time. |
| BUY 15 VICI | Hawkish FOMC, REIT de-rates 30%, SEK firms 10% | ~1,056 + ~352 FX, offset by ~275 SEK/yr dividend (7.8%) | Yes. ~1.6% of capital, income-producing. |
| D-c: no trim at an unknown mark | BTC has run far above the mark, then crypto halves | ~11,600 SEK on the 23,217 SEK sleeve; the overweight slice is the avoidable part | The overweight part, yes. Whether the whole loss fits −30% is what S26 has not tested. |

---

## 8. Timing collisions

From `data/cache/calendar/20261019-events.json`. Caveats:
- `calendar_last_verified` is 2026-08-03, and US/SE CPI dates are missing.
- **Holdings only again.** VICI, APP and NVDA dates are carried from the 2026-10-05 file.
  FSLR has none.
- INVE-A.ST returned no date (a data gap, not confirmed quiet).

- **10-20 (tomorrow): ABB.ST reports.** D-a's hard edge.
- **10-21 SHB-A.ST, 10-22 ATCO-B.ST, 10-23 VOLV-B.ST.** ATCO's print is the first real
  test of its break condition since August. VOLV's tests TOO_EARLY.
- **10-27: ALFA.ST reports on FOMC day 1.** The reaction will mix company news and rates.
  Read the results, not the day-one move.
- **10-28: FOMC statement, and VICI's print (carried).** With CPI at 4.02% and a negative
  real rate, this is the date most likely to move VICI.
  - Buying VICI before 10-28 means owning it into both events.
  - Buying after means paying whatever the statement sets.
  - Neither is an edge this system has. Execute when funded, and do not time it.
- **10-30: AZN.ST reports.** If P3 lands first, the AZN share is bought ahead of the print.
  Conscious choice, acceptable at a Medium horizon.
- **11-04: Riksbank decision**, plus APP's print (carried). **11-10:** Riksbank minutes.
  **11-17:** NVDA (carried).

---

## 9. Data gaps for `meta`

Ordered by what each cost this sweep. Surfaced, not fixed.

1. **No Bitcoin price in the snapshot, a second sweep running.**
   - CLAUDE.md's fetch command includes `--crypto ethereum,bitcoin`; this sweep's crypto
     block has only `ethereum`.
   - BTC0E.AS is carried at a 2026-08-21 mark.
   - D-c could not be evaluated. The fix is one argument in the fetch.
2. **In-repository drift on a user decision (the S27 family).**
   - The 2026-10-12 memo sized D-c on the investable base, calling the denominator
     "unpinned". Its §9 item 11 said the same.
   - `definitions.json` has pinned full-portfolio since 2026-08-17, by your decision.
   - The error moved the trim trigger by ~2,350 SEK. It was caught here before any
     trade.
3. **S27, 9th occurrence, and a new, more severe form.** The scheduled prompt *omitted
   `scout.py`* as well as repeating the two stale premises. Skipping a mandatory stage is
   not a stale fact. Had the orchestrator followed it, this sweep would have been outcome
   2 ("we did not search").
4. **Last sweep's `journal` and `meta` did not run.** There is no SESSION_LOG entry for
   2026-10-12, and OPEN_ITEMS.md is unchanged since 10-05: its "emphasis" paragraph still
   describes D-a as "15 days" out. The orchestrator reports it will write the 10-12 entry
   retroactively.
5. **S32 is widening, with two new catches and two hypotheses.**
   - **New:** AZN.ST P/S and P/B (the `valuation` lens), and **TSM `fcf_yield_pct`
     56.22%** (up from 31.08%) still unflagged while its ROIC is now flagged.
   - **Hypotheses, unverified:** EVO.ST FCF 0.63% and HEXA-B.ST 0.24%, both EUR-reporting
     and SEK-listed. ×11.1974 gives ~7.0% / ~2.7%. If EVO's is real, the value lens is
     hiding its cheapest quality name.
6. **FI insider data: nothing published after 17/09 for any of 7 issuers (five weeks), and
   no candidate issuer is pulled.** AZA.ST, the one Swedish first-seen name, has no read.
   US data is zero (EDGAR 403). Copycat contributed nothing to discovery for a second
   week.
7. **`source=new` miscount, third explicit catch.** 35 rows say `new`. 2 are first-seen
   (AZA.ST, FSLR) and 3 are returnees. The 10-05 "considered" entry set the bar at a
   second catch, and the 10-12 memo met it. This is the third.
8. **The calendar is holdings-only, now a standing regression** (first noted 09-28). Four
   Top-5 or near-Top-5 names have no fresh earnings date.
9. **S29, 9th sweep** (APP's 52-week endpoints). **S21:** AZN.ST `forward_pe` missing 9 of
   9.
10. **Lens-level issues:**
    - `portfolio`'s "two-dimensional diversification" claim for ABB → VICI is overstated
      on geography (§3b #1).
    - Volvo is valued 1 SEK off (§4).
    - The `investor_profile.json.reference_targets` fix has passed its own pre-set
      "open an S-item" threshold.
11. **Still missing everywhere:** EV/EBITDA, FFO/AFFO (VICI), commodity and credit-spread
    series, and policy data (FSLR). `us_cpi_yoy` is dated 09-01; FX is dated 10-09.

---

## Structural decisions (non-stock)

Levers 1–2 (wrapper, fees) are structurally closed and not re-flagged.

**ACTION:** Execute P3. Convert the PayPal balance and transfer it to the Avanza ISK.
Recommended; nothing in this system trades.
- **POSITION:** 14,767.86 SEK (1,177.49 USD + 266.88 EUR at this sweep's FX, per
  `portfolio`), outside any wrapper.
- **TARGET:** ISK, in this order:
  - gold tranche 2: ~5,578 SEK (closes −2.48pp)
  - 1 AZN.ST
  - 15 VICI if ABB did not sell
  - 1 NVDA
  - remainder to Avanza Global
- **REASON:** a recurring ~4% spread on every ~2-month inflow, and the binding constraint
  on four other calls.
- **THESIS STATUS:** decided by you 2026-08-17 (Option A).
- **WHAT CHANGED:** only the count (11th-plus sweep), and the queue behind it is one name
  longer.
- **BREAK CONDITION:** a fee-free route appears, or the realised spread is materially above
  4%.
- **CONFIDENCE:** High (arithmetic, not a forecast).
- **HORIZON:** Long

**ACTION:** D-c band rule, corrected to the full-portfolio convention. Recommended, not
executed.
- **POSITION:** BTC0E.AS, 150 units, carried at 11,031 SEK (the 2026-08-21 mark; the feed
  404s). Crypto is 10.30% of the full portfolio at that mark.
- **TARGET:** trim to 10% of the full portfolio only if the live value exceeds ~14,080 SEK.
  Proceeds go to Avanza Global (`profit_recycling_rule`). ETH stays untouched (P1).
- **REASON:** the band's trigger was set on a denominator you had rejected. On yours, the
  stale-mark sleeve is 1.2pp inside the band.
- **THESIS STATUS:** INTACT (`thesis-review`). This is a sizing action.
- **WHAT CHANGED:** the denominator (corrected), and ETH −6.0%.
- **BREAK CONDITION:** S26's shock-window result, which supersedes the band either way.
- **CONFIDENCE:** Medium
- **HORIZON:** Medium
- *Not in the picks ledger:* BTC0E.AS has no fetched price to join.

**Target allocation:** no change proposed. 80/10/5/0/5 stays PROVISIONAL pending S26. The
10-12 memo's break-even arithmetic still stands: equity weight, not crypto, is the lever
for a 2008-scale shock.

---

## 10. Learning notes

- **A rule written for "the day before the deadline" is only worth something on the day
  before the deadline.** Last week this system said it would not restate the ABB SELL
  this week. Restating it now, the day the temptation is strongest, would teach every
  future memo that its pre-commitments are suggestions.
- **Whether money is available and whether an idea is good are separate questions.**
  NVDA moved from WATCH to BUY with almost nothing about NVDA changing. Last week's WATCH
  was partly "no cash today", which says when to buy, not whether. Mixing the two hides
  good ideas behind a funding queue.
- **The same holding can be 10.30% or 10.85% of "the portfolio"; that is why the
  definition is written down.** You chose the full-portfolio reading on 2026-08-17. A memo
  that forgot it moved the trim trigger by ~2,350 SEK. Pinned definitions exist so a
  decision does not depend on which sweep happens to remember them.
- **Concentration percentages move when you sell, not only when you buy.** Selling ABB, a
  Swiss company, *raises* Sweden's share of your stock sleeve, because the denominator
  shrinks. A trade that fixes one concentration can quietly worsen another.

---

`journal` **must run next**, and the 2026-10-12 entry it missed must be written first. An
unlogged memo is invisible to the next session and can never be reconciled. Then run
`python scripts/decisions.py record --picks data/picks/2026-10-19-picks.csv`, followed by
`python scripts/decisions.py basis --write`.
