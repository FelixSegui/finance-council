# Council Memo — 2026-10-12

*This memo is a structured synthesis of your own agents' analysis of data fetched this
session. It is not licensed investment advice. Every number in it comes from a file
written for this sweep, or is labelled as carried forward, user-relayed, or this memo's
own arithmetic.*

---

## What leads this memo

**1. ABB.ST: eight days left in the window, and this is a fresh decision, not an eighth
sweep.** On 2026-10-05 the Chairman set a lapse condition: if the SELL is not executed
before ABB's **2026-10-20** print, the call lapses. The print has not happened yet, so the
call has not lapsed. I still did not carry it forward. I re-decided it from today's data
alone (#1 below).
- **Result: SELL, conviction 5 (down from 6).**
- The insider-selling clause has now tested negative on three pulls in a row (08-23,
  09-07, 10-12; no ABB disposal since 13/08). That leaves the case on four legs:
  valuation, cash conversion, a false ownership premise, and concentration.
- **This call cannot be renewed.** If nothing has executed by the 10-20 print, it is
  recorded as lapsed. The 10-19 memo, if one runs, does not restate it. The 10-26 memo
  decides ABB from the reported Q3 numbers with no streak count.

**2. S6 / D-b: the 2026-10-07 NAV window passed with nothing recorded, so the named
consequence now applies.** `data/company_profiles/INVE-A.ST.json`'s `review_history`
still ends at 2026-07-28 and holds no NAV discount or premium figure. On 2026-10-05,
OPEN_ITEMS.md said that if this window passed again with nothing recorded, the Option-3
fallback "should be treated as this system's durable position on the holding, not a
temporary stand-down."
- That is now the position. **INVE-A.ST is a durable HOLD.** This memo does not re-flag
  S6 as a pending trigger, and no future memo should either.
- S6 stays open as a system item (no free NAV source exists). It is no longer a
  decision fork.
- This is a default the system pre-committed to, not an action anyone took. You can
  override it in one line (§6, D-b).

**3. D-c (BTC0E.AS trim): the position's price is staler than the trim is large.**
`portfolio.json` still shows 150 units, valued at the **2026-08-21** broker mark (11,031
SEK). This sweep fetched no Bitcoin price at all: the snapshot's `crypto` block holds
only `ethereum`.
- The trim proposed last sweep was ~2,500 SEK. Seven weeks of BTC movement on an
  11,031 SEK position could plausibly be larger than that, in either direction. So the
  sleeve's real weight is not known to within the size of the proposed trade.
- §6 replaces "trim now" with a band rule keyed to the one number this system lacks:
  the live Avanza value of the 150 units.

**4. A correction to this sweep's launch note: ALFA.ST's insider data is not fresh.**
- The launch note calls CFO Ekström's 2026-09-11 purchase (1,000 shares at 547.49) "a
  genuine fresh positive data point this sweep". The 2026-10-05 memo's Copycat voice
  already cited that exact transaction.
- It is new relative to the 2026-08-17 review's 10/10 count. It is not new this week.
- This sweep's FI pull shows **10 acquisitions and 0 disposals** for Alfa Laval
  (2023-12-12 to 2026-09-11). I cannot reproduce "11/11" from this file.
- More important: **across all seven issuers pulled, Finansinspektionen has published
  nothing dated after 17/09/2026.** The Copycat voice's evidence is four weeks old
  everywhere, not just on ALFA.

**5. Settled facts asserted otherwise in the launch premises (S27), not re-litigated.**
- The Handelsbanken wrapper is resolved. `portfolio.json.resolved_structural_questions`
  records it as confirmed 2026-07-07 and the HB exit executed 2026-07-12/20.
- `investor_profile.json.reference_targets` is not null: 85/10/0/5 was adopted
  2026-07-27 and written 2026-08-03. `portfolio.json.targets` carries the gold-carved
  80/10/5/0/5 (carve applied 2026-09-02).

The orchestrator reports that the scheduled launch prompt asserted both stale premises
again. I can verify the premises are false against the files. I cannot read the
scheduled prompt text itself, so "verbatim recurrence" rests on the orchestrator's
relay. By OPEN_ITEMS.md's own count (7 confirmed through 2026-10-05), **this is the 8th
occurrence.** Item 4 above is a second, in-session instance of the same family.

---

## 1. Position report

`scripts/position_report.py` output, run this session and handed to `council` as a file
path (the S27 fix recommended last sweep, now applied):

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 150.20 | -1.2% | +16.2% | 81% | 150.20 | fetched |
| Investor A (stock) | 398.20 | +1.2% | +37.2% | 83% | 1,991.00 | fetched |
| Volvo B | 309.50 | -2.8% | -15.8% | 50% | 4,023.50 | fetched |
| Atlas Copco B | 179.70 | +1.2% | -0.9% | 88% | 4,851.90 | fetched |
| AstraZeneca | 1,574.50 | -1.5% | +2.4% | 23% | 12,596.00 | fetched |
| Xetra-Gold (physically-backed gold ETC, ISIN DE000A0S9GB0) | no data | no data | no data | - | 5,689.22 | FETCH FAILED |
| Alfa Laval | 560.40 | +1.8% | -2.4% | 81% | 5,043.60 | fetched |
| ABB | 945.00 | -1.7% | -0.2% | 73% | 3,780.00 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| Valour Bitcoin Zero SEK (certificate, ISIN CH0585378661) | no data | no data | no data | - | 11,031.00 | FETCH FAILED |
| ETH (self-custody wallet) | 25,839.96 | -5.6% | no data | - | 12,967.79 | fetched (CoinGecko, converted via sek_per_eur) |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high.* Crypto context
(CoinGecko): ETH 2,279.36 EUR, −6.0% vs the previous snapshot, −5.2% over 7 days, +2.0%
over 30 days, −46.1% vs its all-time high.

**What moved, and whether it matters:**
- **Volvo B −2.8%** (now −15.8% vs cost, 50% of range) is the largest equity move.
  - No fetched fundamental moved with it: ttm revenue is still +2.7%, forward P/E 12.67
    against trailing 17.89.
  - The thesis is TOO_EARLY, not contradicted. Its two tests arrive together: the
    **10-23 print**, and the 3-month checkpoint in its own break condition (~11-03).
- **AZN.ST −1.5%**, to 23% of its range, a cheaper entry on an INTACT thesis.
- **ETH −5.6%** shrinks the crypto overweight on its own.
- **Not priced.** 67.8% of total capital has no live mark this sweep (152,910 SEK of
  225,411 SEK: the two Avanza funds at book value, gold and BTC at stale marks). That
  is noted for `meta` (§9).

---

## 2. Scout health

```
Universe    624
Fetched     621  (cache 0, new 625, failed 4)
Ranked      613
Candidates  72   (holdings 9, watchlist 30, new 33)
Focus       23
Screened    72
Passed      38
Missing     16
Failed      18
Status      VALID
```

**Reading.** The status is VALID, so nothing upstream needs distrusting before §3. Three
facts should still shape how you read the run.

**"New" is not "first seen".** 33 rows carry `source=new`, which means "not held, not
watchlisted". Checked against all eight runs in `candidate_history.csv`:
- **Only GM is in the candidate set for the first time.**
- Two are returnees: BALD-B.ST (last seen 09-21) and SMCI (last seen 09-28).
- Five names left this run: CATE.ST, CTVA, EOG, MKC and PLTR. EOG was last sweep's
  Defensive pick.
- **The one genuinely new name is a data artifact rather than an opportunity.** GM ranks
  37 on the value lens, built on forward P/E 5.47 against trailing 37.10 (a ~6.8x
  implied EPS jump) and an unflagged FCF yield of 30.22%. Net margin is 1.1% and net
  debt/EBITDA 6.32.
- Discovery produced one name this week, and the voices cannot use it.

**The frozen head thawed slightly, for a data reason, not a market one.**
- APP, SNDK, NVDA, MA, V, TSM and VICI have been top-10 in **all 8 runs**. MU has been
  top-10 in 7 of 7 runs since first seen (08-31).
- **INDU-C.ST fell 8 → 28.** Its operating margin (102.5%) is now suspect-flagged and
  withheld, so `z_quality` dropped from 1.904 to 1.320. The business did not change; the
  withholding did what it is meant to do.
- **CMCSA entered the top 10 for the first time (rank 8)** by falling −2.3%. That is the
  value-lens-rewards-falling-prices pattern S33 already names.

**Suspect values withheld from lens scoring (8 names):**
- ABB.ST `price_to_book` 109.41
- SNDK `revenue_growth` 371.6%; MU `revenue_growth` 379.3%
- CMCSA `peg` 142.98
- INDU-C.ST `operating_margin` 102.5%
- ASML `price_to_book` 1,546.43 and `roic` 4.05
- KINV-B.ST `price_to_sales` −2.35
- FANG `peg` 21.29

**Still unflagged, and feeding the value lens:**
- TSM `roic_pct` 183.7% and `fcf_yield_pct` 31.08%, a 6th sweep.
- ABB.ST `fcf_yield_pct` 0.09 and AZN.ST 0.21, the S32 unit mismatch, still unfixed.
- A cluster of implausible FCF yields on value-ranked names: GM 30.22%, MEKO.ST 36.43%,
  GPN 36.17%, DOM.ST 27.07%, ALL 26.13%, CORE-B.ST 24.15%.

None is verified as wrong. Each sits in the lens that S33 measures as anti-correlated
with outcomes.

---

## 3. Top opportunities

### 3a. The seven voices (independent passes)

Each voice triaged all 72 rows on its own columns, then drafted without reading the
others. A voice that pulls in a name outside `focus=Y`, or argues against a screen flag,
says so.

#### Voice 1 — Fundamental / Quality

*Triage (`z_quality`):* APP 2.560, NVDA 2.527, SNDK 2.523, MU 2.514, MA 2.245, V 1.951,
TSM 1.930, INVE-A.ST 1.813, TPL 1.810, MO 1.776, LLY 1.740. *Moat, management and capital
allocation are qualitative here; no fetched field measures them.*

- **BUY V, 8.**
  - Why: ROIC 41.5%, ROE 61.2%, net margin 50.8%, operating margin 66.1%, net
    debt/EBITDA 0.32, revenue +14.4% on a 10.9% 3-year CAGR. Every field is unchanged
    from last sweep.
  - The price rose 4.2% (359.85 → 375.10, 87% of range). That is Valuation's problem,
    not mine.
  - Risk: regulation of interchange fees (qualitative).
  - Invalidated by: ROIC below 30%, or growth in mid-single digits for two prints.
- **BUY NVDA, 7.**
  - Why: ROIC 59.2%, ROE 117.2%, margins 63.7/66.2, net cash (−0.12).
  - Held at 7 for one reason: FCF yield 0.76% (USD over USD) against an earnings yield
    of ~3.45% (1/28.99). About 22% of reported earnings reach free cash.
  - Invalidated by: FCF yield still below 1% after the 11-17 print.
- **BUY MA, 7 (pulled in against its FAIL).**
  - Why the FAIL misleads: D/E 439.58 is buyback-created negative equity. Net
    debt/EBITDA is 0.59.
  - Underneath: ROIC 56.1%, margins 46.3/61.1, revenue +14.1% on a 13.8% CAGR.
  - Invalidated by: net debt/EBITDA above 2.0.
- **BUY ATCO-B.ST (holding), 6.**
  - Why: the best business held. ROIC 39.7%, ROE 25.7%, operating margin 20.6%, net
    debt/EBITDA 0.50, FCF yield 2.91% (SEK over SEK, clean).
  - Invalidated by: ttm revenue growth turning negative at the **10-22** print. That is
    also its own break condition.
- **BUY AZN.ST (holding), 5.**
  - Why: operating margin 23.5%, net debt/EBITDA 1.35, revenue up every fiscal year
    2022–2025. FX-corrected FCF yield is ~2.1% (0.21% × 10.07).
  - Only 5: ROIC 13.1% is good, not excellent.
  - Invalidated by: operating margin below 20% at the **10-30** print.
- **BUY TSM, 5.**
  - I discard `roic_pct` 183.7% and `fcf_yield_pct` 31.08% (suspected TWD/USD unit
    error, S32, unverified).
  - The case rests on ROE 40.0%, margins 49.9/60.3 and net cash (−0.77).
  - Six sweeps of unusable headline fields is a confidence cost in itself.
- **SELL ABB.ST, 5 (down from 6).**
  - Why: FCF/revenue 4.4% (1.5705B / 35.75B, both USD; capex derived as OCF − FCF in the
    snapshot) is the thinnest cash conversion held. Atlas Copco's is 15.3%, carried from
    2026-10-05.
  - Lower because ROE 32.6% and net debt/EBITDA 0.46 describe a sound business. I am
    selling a conversion profile, not a broken company.
  - Invalidated by: FCF/revenue above ~8% in the next annual report.
- **Declined:**
  - **APP.** ROE 203.7% on D/E 111.13, still at 3% of range.
  - **MU/SNDK.** Suspect growth flags; operating margins of 80.7/78.5% read as peak
    cycle. SNDK fell 10.0% this week.
  - **EVO.ST** (pulled in and rejected). ROIC 23.1%, net margin 51.8%, net cash, but
    revenue is −1.2%. A quality business that has stopped growing.
  - **INVE-A.ST/TPL.** Holding-company or implausible fields.

#### Voice 2 — Valuation

*Triage (`z_value`):* CMCSA 1.885, CHTR 1.872, FIS 1.783, ALL 1.782, EG 1.670, CORE-B.ST
1.657, FISV 1.633, DOM.ST 1.518, MEKO.ST 1.410, GM 1.349, DIOS.ST 1.306, GPN 1.280,
INDU-C.ST 1.232, INVE-A.ST 1.165, EXE 1.170. *Named gap: no EV/EBITDA or EV/EBIT. Where I
lean on net debt/EBITDA, I say so.*

- **BUY VICI, 8.**
  - Why: 8.90x trailing, 7.65x forward, 8.04% dividend, 67.5% net margin, revenue +5.7%
    on a 15.5% CAGR, 4% of range, PASS.
  - This is the first week in four the price did not fall (22.73 → 22.79). No fetched
    field deteriorated in 8 runs.
  - Approximation: net debt/EBITDA 4.82 is heavy. I quote no enterprise multiple.
  - Invalidated by: a dividend cut, or net debt/EBITDA above 6.
  - Missing: FFO, AFFO and lease coverage, the metrics REITs are actually priced on.
- **BUY AZN.ST (holding), 7.**
  - Why: PEG 1.12, 23% of range, price −1.5%. FX-corrected FCF yield ~2.1%.
  - Background, labelled: large-cap pharma typically trades 15–20x trailing, so 25.4x is
    a premium only before adjusting for growth.
  - Invalidated by: PEG above 1.6.
  - Missing: `forward_pe`, absent in **8 of 8** runs (S21).
- **BUY NVDA, 7.**
  - Why: forward 14.41x against trailing 28.99x on +105.9% revenue. The forward/trailing
    gap carries the case. I do not lean on PEG 0.28, which moves between prints with no
    event.
  - Invalidated by: forward P/E rising above trailing.
- **SELL ABB.ST, 5 (down from 6).**
  - Why: still the richest trailing multiple held (37.22x vs ATCO 33.51x, ALFA 29.14x).
    Forward 36.37x sits only 2.3% below trailing, implying roughly flat next-year EPS on
    14.2% revenue growth. P/B 109.4 is suspect; FX-corrected ~11.7x is carried from the
    company profile.
  - Against my own case: ABB's PEG (1.31) is now the *lowest* of the three industrials
    held (ALFA 1.82, ATCO 2.24). I trust the forward/trailing pair over PEG, but this
    leg is weaker than a week ago.
- **SELL ATCO-B.ST, 5.**
  - Why: 33.51x trailing, PEG 2.24, 88% of range.
  - Invalidated by: PEG below 1.5.
- **Testing the `valuation` lens's own "Cheap" verdicts against the data:**
  - **FIS: declined.** The lens calls it "mispricing, not deterioration" on PEG 0.18 and
    29.1% revenue growth. But the 3-year CAGR is **−9.8%**, so 29.1% looks like a base
    effect, not organic growth, and the PEG inherits that. Net debt/EBITDA is 5.82.
    "Cheap" is asserted, not shown.
  - **APP: declined.** The lens calls it "mispricing, not deterioration". The file has no
    data that distinguishes the two; the price has sat at 3% of range for many sweeps.
- **Cheap for a reason, not picks:**
  - **CMCSA, CHTR.** Revenue −1.2% / −1.7%; CHTR D/E 441.58.
  - **GM.** See §2.
  - **ALL.** Forward 8.18 vs trailing 4.59 implies an earnings halving.
  - **EG.** Revenue −11.3%.
  - **DIOS.ST, BALD-B.ST, CORE-B.ST.** Net debt/EBITDA 10.07 / 16.13 / 15.52.
  - **TPL.** Forward 4.94 vs trailing 46.04 is not credible.
- **ALFA.ST: expensive, not a SELL.** Its forward 26.33x is the lowest forward multiple of
  the three industrials.

#### Voice 3 — Growth / Opportunity

*Triage (`z_growth`):* NVDA 1.925, BE 1.785, AVGO 1.761, SMCI 1.746, APO 1.734, AXON
1.546, DASH 1.504, MU 1.492, GPN 1.475, FANG 1.441, LLY 1.435, APP 1.400. *Forward below
trailing:* MU 4.99/13.84, SNDK 5.94/21.45, TPL 4.94/46.04, GPN 5.13/38.59, GM 5.47/37.10,
NVDA 14.41/28.99, APP 13.33/21.29, AVGO 18.64/46.17, APO 11.09/42.53, LLY 24.76/39.59,
META 20.80/27.08, VOLV-B.ST 12.67/17.89. *Named gaps: no TAM, revisions or market-share
data.*

- **BUY NVDA, 8.**
  - Why: revenue +105.9% on a 100.0% CAGR, forward at half of trailing, clean data.
  - Risk: a pause in hyperscaler capex (qualitative; no backlog data).
  - Invalidated by: growth below 40%, or forward above trailing.
- **BUY LLY, 6 (pulled in, rank 21).**
  - Why: revenue +47.7% on a 31.7% CAGR, operating margin 54.2%, ROIC 38.4%, forward
    24.76x vs 39.59x.
  - Risk: D/E 162.07, and dependence on one drug class (qualitative).
  - Invalidated by: ttm growth below 25%.
- **BUY META, 5 (pulled in, rank 50, watchlist).**
  - Why: revenue +28.0% on a 19.9% CAGR, forward 20.80x vs 27.08x, PEG 0.95, operating
    margin 34.8%. This is measured growth at a forward multiple below the S&P-type names
    around it (NVDA excepted).
  - Risk: the funnel ranks it 50. Its quality z (0.639) is mid-pack, so this is a
    growth-only case.
  - Invalidated by: forward P/E rising above trailing.
- **BUY AVGO, 5 (pulled in against its FAIL on trailing 46.17).**
  - Why: forward 18.64x on +85.5% revenue, 34% of range.
  - Held: 85.5% against a 24.4% CAGR is likely an acquisition base effect.
- **BUY APP, 5.**
  - Why: +52.8% revenue at a 77.7% operating margin, forward 13.33x vs 21.29x. The price
    is flat this week (−0.4%), still at 3% of range.
  - Decided by: the **11-04** print.
- **BUY VOLV-B.ST (holding), 5.**
  - Why: forward 12.67 vs trailing 17.89, ttm revenue +2.7% after a two-year decline. The
    3-year CAGR is only +0.4%.
  - The **10-23** print is the test.
- **SELL SHB-A.ST, 4.** Revenue −3.8%, z_growth −1.274 (the worst held), forward 13.25
  above trailing 12.67. Immaterial at one share.
- **SELL ABB.ST, 4.** 14.2% revenue growth that the forward multiple says will not reach
  EPS. PEG 1.31 contradicts that; I trust neither strongly.
- **Declined:**
  - **MU/SNDK.** Suspect growth fields; SNDK −10.0% this week.
  - **GM, GPN, TPL, APO.** Forward/trailing gaps the data cannot reconcile.
  - **SMCI** (returned). FCF yield −30.0%.
  - **BE, AXON, DASH.** The growth is real; the multiples are 57–103x trailing or worse.

#### Voice 4 — Defensive / Risk

*Triage (lowest `beta`):* SAAB-B.ST 0.03, ALL 0.138, BETS-B.ST 0.17, JNJ 0.206, AZN.ST
0.212, ABBV 0.228, EG 0.259, CME 0.27, KO 0.318, TEL2-B.ST 0.34, PEP 0.364, PG 0.377,
NOVO-B.CO 0.384. *Lowest leverage:* TPL D/E 1.077, SNDK 1.277, EVO.ST 2.13, INDU-C.ST
2.821.

**The scenario I position for:** the regime lens calls this TRANSITIONAL.
- The 10-year is at 5.22%, the 2-year at 4.75%, and DXY at 121.38, up from 120.33.
- Sweden's real policy rate is +1.45pp (Riksbank 1.75% against CPI 0.3%).
- VIX at 15.41 is pricing calm.

My worry is a de-rating of long-duration and leveraged names if 5%+ yields persist,
landing on a portfolio whose −30% tolerance no traceable file has tested (S26).

- **BUY AZN.ST (holding), 7.**
  - Why: beta 0.212, net debt/EBITDA 1.35, operating margin 23.5%, revenue up four fiscal
    years running.
  - Invalidated by: a dividend cut.
- **BUY CME, 6.**
  - Why: beta 0.27, net debt/EBITDA 0.33, net margin 63.4%. Exchange volumes typically
    rise in shocks; that is qualitative, since no volume data is fetched.
  - Cost: PEG 4.88 on 0.8% growth.
  - Invalidated by: a quarter where VIX rose and revenue didn't.
- **BUY JNJ, 5 (pulled in, rank 51; replaces EOG, which left the set).**
  - Why: beta 0.206, net debt/EBITDA 0.81, net margin 21.5%, forward 21.12x vs 30.29x,
    revenue +6.6%.
  - Risk: the 3-year CAGR is −0.3%, so this is stability, not growth. Litigation exposure
    is qualitative and unmeasured.
  - Invalidated by: revenue growth turning negative.
- **BUY MO, 4.**
  - Why: beta 0.461, 6.19% dividend, 7.55% FCF yield, net debt/EBITDA 1.41.
  - A shrinking business (+1.2% on a −0.9% CAGR). `de_ratio` is MISSING.
    `constraints.exclusions` is empty, so tobacco is not excluded. The price rose 6.7%
    this week, which thins the yield argument.
- **SELL VOLV-B.ST, 4.**
  - Why: D/E 147.35 and net debt/EBITDA 3.8 make it the most leveraged holding, beta 1.0,
    in a +1.45pp Swedish real-rate regime.
  - Invalidated by: net debt/EBITDA below 2.5.
- **Attacking this sweep's BUY cases:**
  - **NVDA / APP / MU.** Betas 2.216 / 2.557 / 2.226 against an untested −30% tolerance.
  - **VICI.** Net debt/EBITDA 4.82 with the 10-year above 5%.
  - **DIOS.ST / BALD-B.ST.** Net debt/EBITDA 10.07 / 16.13; not investable on leverage.
  - **CHTR.** D/E 441.58; the FAIL is deserved.
  - **EIX.** Net debt/EBITDA 4.85, D/E 228.04, forward 8.50 above trailing 5.70.
- **Not flagging ABB.ST.** D/E 55.75, net debt/EBITDA 0.46. No risk case.

#### Voice 5 — Contrarian / Risk Taker

*Triage (`pct_52w_range`):* DIOS.ST 0, DOM.ST 0, BALD-B.ST 1, CORE-B.ST 1, FISV 2, APP
3, VICI 4, CHTR 4, CMCSA 6, FIS 6, PEP 10, EIX 10, EXE 13, NOVO-B.CO 14, HD 15.

- **BUY VICI, 6.**
  - Why the pessimism looks wrong: in 8 runs the fetched fundamentals have not moved
    (revenue +5.7%, margin 67.5%, PASS). The price fell 26.51 → 22.79 (−14.0%) as the
    10-year rose. This week the 10-year eased 5.24 → 5.22 and the price stopped falling.
    That is consistent with a discount-rate story, not an asset story.
  - I am not predicting a re-rating; the 8.04% yield pays for waiting.
  - Invalidated by: a dividend cut or a tenant default. The 10-28 print, per the
    2026-10-05 calendar file (not in this sweep's holdings-only calendar), is the first
    test.
- **BUY PEP, 5 (down from 6).**
  - Why: 10% of range after bouncing off 1%. PEG 1.29, 4.7% dividend, 5.27% FCF yield,
    beta 0.364.
  - Lower because revenue growth slipped from +6.4% (last sweep's file) to +5.6%. The
    "revenue hasn't turned" leg is weaker.
  - Risk: D/E 230.72, net debt/EBITDA 2.12.
  - Invalidated by: revenue growth turning negative.
- **BUY APP, 4.**
  - A 77.7%-margin, +52.8% grower at 13.33x forward that the market keeps pricing at
    3% of range.
  - Held low: S29 still hides the 52-week endpoints, so the size and start of the
    drawdown are invisible.
  - Invalidated by: growth below 25% at 11-04.
- **SELL flags: none.** INVE-A.ST is now a durable hold (D-b); I do not reopen it.
- **Declined (penalty deserved):**
  - **DIOS.ST, BALD-B.ST, CORE-B.ST, DOM.ST.** At 0–1% of range, the leverage explains
    the price.
  - **NOVO-B.CO.** Growth fell from a 20.4% CAGR to 2.1%, and forward 11.63 sits above
    trailing 9.74. Consensus is reading a real slowdown.
  - **EIX.** Forward above trailing; no file explains why.

#### Voice 6 — Macro / Regime

*Regime (from `macro-regime`): TRANSITIONAL.*
- **US:** real fed funds ≈ +0.04pp (3.75% vs CPI 3.71%, the CPI print dated 2026-08-01).
  10y−2y +0.47 (5.22/4.75). VIX 15.41.
- **Dollar:** DXY 121.38, up from 120.33.
- **Sweden:** Riksbank 1.75% against CPI 0.3%, a +1.45pp real rate.
- **FX and sentiment:** SEK/USD 10.0688 (dated 10-02), up from 9.9047, so the krona
  weakened ~1.7% against the dollar. Crypto Fear & Greed 69 ("Greed").

*Named gap: no commodity-price and no credit-spread data.*

- **BUY AZN.ST (holding), 6.** SEK-listed and low-beta, with a USD-reporting business.
  The strong dollar is a mild translation tailwind for SEK holders (per the regime lens).
  Revenue-currency mix is unmeasured.
- **BUY V, 5 (down from 6).** Revenue is a share of nominal spending, so 3.71% CPI is
  revenue. Lower because the SEK entry price for any USD asset rose ~1.7% this week, at
  DXY 121. A SEK investor buying here carries the mean-reversion risk.
- **BUY CME, 5.** Rate volatility drives rate-futures activity (qualitative). A low-beta
  earner.
- **Explicit regime downgrades, stated rather than buried:**
  - **VICI, downgraded on regime grounds alone.** The 10-year is at 5.22%, below the
    5.5% retirement trigger. The added cost this week is FX: 16 shares now cost ~229.47
    SEK each, against 225.13 last week.
  - **NVDA, APP, LLY, META.** Long duration at a 5.22% 10-year. The businesses are fine.
  - **Crypto.** DXY rose again while F&G stays at "Greed": macro and sentiment point
    opposite ways. That supports *not adding*. It does not by itself size a trim; see
    D-c.
  - **Swedish industrials** (ABB 37.2x, ATCO 33.5x, ALFA 29.1x). Expensive in a
    restrictive local regime.
  - **Energy (EXE, FANG, TPL).** Not assessable; no commodity series.
- **SELL flags on macro grounds alone: none.**

#### Voice 7 — Copycat / Smart Money

**Coverage first.**
- **US:** SEC EDGAR CIK mapping returned 403 again, so there is **zero US insider data**.
  Nothing on any US candidate.
- **Sweden:** Finansinspektionen covered 7 issuers. **No publication is dated after
  17/09/2026 for any of them.** Everything below is ≥4 weeks old.
- **Discards:**
  - The "Volvo" pull again mixes in Volvo Car AB (Nota, Severinson, Samuelsson). Those
    rows are discarded.
  - Industrivärden was not pulled.
- **Institutions:** `MISSING: institutional ownership not fetched`.

This voice reviews holdings and contributes nothing to discovery this sweep.

- **BUY AZN.ST, 6 (down from 7).**
  - Why: CEO Soriot bought 60,000 at 121.02 GBP and Chairman Demare 2,500 at 121.21 GBP,
    both on 14/09, at real prices. The CFO's 0.00-price lines are vestings and say
    nothing.
  - Lower: the signal is four weeks old and has not extended. GBP/SEK is not fetched, so
    I cannot place today's 1,574.50 SEK against their entry.
  - Invalidated by: a Soriot or Demare disposal.
- **BUY ALFA.ST (holding), 5.**
  - Why: CFO Ekström bought 1,000 at 547.49 on 11/09; today's 560.40 is +2.4% above.
    This pull shows 10 acquisitions by 9 named individuals, 2023-12 to 2026-09, and
    zero disposals.
  - Not new this sweep (see the opening, item 4).
  - Invalidated by: any insider disposal.
- **BUY INVE-A.ST (holding), 5 (down from 6).**
  - Why: the three most recent buys are Cederholm 1,500 at 395.90 (14/09), Lund 1,000 at
    399.13 (09/09) and Elfving 850 at 411.55 (01/09). Today's 398.20 sits between them.
    Zero disposals in the pull.
  - Lower: nothing new in four weeks.
  - Invalidated by: a Cederholm disposal.
- **Reads that are not calls:**
  - **ABB.ST.** Disposals only: Terwiesch 18,799 / 10,000 / 20,000 between 29/07 and
    13/08, and Meline 2,456. **Nothing since 13/08 on a third pull.** The May
    "acquisitions" are six board members at an identical 78.42 CHF, i.e. fee allotments.
    No SELL from this voice.
  - **VOLV-B.ST.** Stjernholm's 27/07 cluster sums to exactly 1,300,000 shares at
    ~359–361 (closely associated). Today's 309.50 is ~14% below it, and the insider has
    not sold.
  - **SHB-A.ST.** Boman's 26/08 cluster sums to exactly 1,850,000 shares at
    145.55–146.24. One person, one day.
  - **ATCO-B.ST.** Option exercises paired with same-day disposals: compensation, not a
    signal.
- **SELL flags: none.**

---

### 3b. Chairman's Top 5

#### #1 OPPORTUNITY: ABB.ST — ABB (fresh re-decision, final window)

**CATEGORY:** holding

**RANK HISTORY:** 64 now; 66 (10-05). **0 of 8 runs in the top 10.**

**VOICES IN FAVOR (of selling):**
- Fundamental, 5: FCF/revenue 4.4%, the thinnest held.
- Valuation, 5: the richest trailing multiple held; forward implies flat EPS.
- Growth, 4: revenue growth not reaching earnings.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: net debt/EBITDA 0.46, no risk case.
- Copycat: no disposal since 13/08, so the insider clause is negative a third time.
- Valuation's own concession: ABB's PEG (1.31) is now the lowest of the three
  industrials held.

**STRONGEST CASE FOR (selling):** thesis-review's "would I buy it today?" test, which
returns **NO** for the third straight independent re-test, and no voice argues BUY.
- The stated reason for owning it ("Swedish industrial champion") is false: the snapshot
  lists ABB's country as Switzerland.
- It is the richest trailing multiple held (37.22x) with the thinnest cash conversion
  (4.4%).
- The user's own tier rule says medium-tier names move "if it is detected it can be
  better off elsewhere without increasing the risk".

**STRONGEST CASE AGAINST:** the case keeps shrinking as it is tested.
- In five weeks three legs have gone: insider selling (negative on three pulls), the
  "inversion" (flipped 10-05), and the 0.09% FCF yield (a unit artifact; ~0.9% real).
- What remains is a *relative* valuation argument. On PEG, ABB is now the cheapest of
  the three industrials held.
- Defensive is right that nothing about ABB is dangerous. It is 1.7% of capital, at
  −0.2% vs cost.

**KEY DISAGREEMENT:** whether a SELL that has lost three of its legs should survive at
all, or lapse now.
- I keep it, at 5, for one reason no earnings print changes: no lens would buy ABB
  today. Holding a position nobody would initiate is inertia, not a decision.
- But I will not let the 10-20 print become a coin-flip this system pretends to have an
  edge in. Before the print it is a valuation SELL. After the print it is a new
  question.

**DATA GAPS:**
- No EV/EBITDA. FCF is trailing-only.
- P/B (109.4) and FCF yield (0.09%) are unit-mismatched (S32).
- PEG and the forward multiple contradict each other, and no revisions feed exists to
  say which is current.

Moderate discount.

**CHAIRMAN CONVICTION:** 5 (down from 6)

**WHAT WOULD CHANGE THIS:** before the print, nothing in the fetched data. At the print,
operating margin clearly above 16.9% *and* FCF/revenue above ~8% would retire the SELL on
merit.

**PORTFOLIO FIT** (from `portfolio`):
- Industrials are **54.6%** of the 32,436 SEK visible stock sleeve, rated ACT.
- Rotating ABB into VICI takes that to **42.9%** (WATCH). Selling to cash leaves it
  ~48.6% (ACT, this memo's arithmetic).
- Sweden's 49.5% is unaffected either way, because ABB is Swiss-domiciled.
- The trade is tax-free inside the ISK.

**FINAL CALL: SELL** — all 4 shares (~3,780 SEK at 945.00), **before 2026-10-20.**
**Non-renewable.** If not executed by the print it is recorded as lapsed, and the 10-26
memo decides ABB on reported Q3 numbers with no streak. Holding through the print by
choice is legitimate; say so and it is recorded as your decision.

**HORIZON:** Medium

#### #2 OPPORTUNITY: AZN.ST — AstraZeneca

**CATEGORY:** holding

**RANK HISTORY:** 57 now; 59 (10-05). **0 of 8 in the top 10.** The rank is depressed by
two data defects, not the business:
- `forward_pe` is missing in 8 of 8 runs (S21).
- The unit-mismatched FCF yield (0.21%) feeds z_value −1.531 (S32).

**VOICES IN FAVOR:**
- Valuation, 7: PEG 1.12, 23% of range.
- Defensive, 7: beta 0.212, four years of rising revenue.
- Copycat, 6: CEO plus Chairman open-market buys, 14/09.
- Macro, 6: the right side of the regime.
- Fundamental, 5: corrected cash conversion, but ROIC 13.1%.

**VOICES AGAINST / CAUTIOUS:** none at SELL. Fundamental's ROIC caveat is the ceiling.

**STRONGEST CASE FOR:** five lenses citing five different fields, none dependent on
another. Thesis-review independently grades the thesis INTACT and says the buy case is
"stronger now than at the original purchase" (1,574.50 vs a blended cost of 1,537.73,
at 23% of range).

**STRONGEST CASE AGAINST:** Copycat's evidence is aging and nothing new has replaced it.
And `portfolio`'s concentration read: Healthcare is 38.8% of the visible sleeve, all of
it this one name.

**KEY DISAGREEMENT:** merit against fit, kept separate.
- One more share takes Healthcare to ~41.7% (still under 45%) and lowers Sweden from
  49.5% to ~47.2% (this memo's arithmetic). It trades a sliver of an ACT row for a
  deeper WATCH.

**DATA GAPS:**
- No forward multiple in 8 runs.
- GBP/SEK is not fetched.
- Revenue-currency mix is unknown.

Moderate discount.

**CHAIRMAN CONVICTION:** 7

**WHAT WOULD CHANGE THIS:** operating margin below 20% at the **10-30** print, or a
Soriot/Demare disposal.

**PORTFOLIO FIT:**
- **Capital check against this sweep's `portfolio`:** ISK dry powder is **845 SEK**; one
  share is 1,574.50 SEK. Not fundable today.
- Deployable cash outside the tax reserve is almost entirely the unconverted PayPal
  balance (14,887 SEK, P3).

**FINAL CALL: BUY** — 1 share. **Execution note: no idle capital confirmed (845 SEK ISK
cash). Funded by P3 or the next contribution.**

**HORIZON:** Medium

#### #3 OPPORTUNITY: VICI — Vici Properties

**CATEGORY:** new candidate (first surfaced by this funnel 2026-08-25; not held, not
watchlisted)

**RANK HISTORY:** 10 now; 10 (10-05). **8 of 8 runs in the top 10.**

**VOICES IN FAVOR:**
- Valuation, 8: 7.65x forward, 8.04% yield, no deterioration in 8 runs.
- Contrarian, 6: the discount rate repriced, not the asset.

**VOICES AGAINST / CAUTIOUS:**
- Macro: a regime-only downgrade, plus a worse FX entry at DXY 121.
- Defensive: net debt/EBITDA 4.82.

**STRONGEST CASE FOR:** Valuation's. A 67.5%-margin, still-growing landlord at 7.65x
forward and an 8.04% yield, with a PASS screen, unchanged on every fetched field for 8
weeks.

**STRONGEST CASE AGAINST:** Macro's. The price tracked the 10-year down for seven weeks,
and the SEK cost of entry rose ~1.7% this week on FX alone.

**KEY DISAGREEMENT:** Valuation says the multiple is wrong; Macro says it is pricing a 5%+
10-year correctly. The pre-committed observable (10-year ≥5.5% with the price still
falling) has **not** fired (5.22%). Conviction holds at 5; a threshold moved every week is
not a threshold.

**DATA GAPS:**
- No FFO, AFFO, EV/EBITDA or lease coverage.
- Zero US insider data. Institutional ownership not fetched.
- No candidate earnings dates in this sweep's calendar.

Heavy discount.

**CHAIRMAN CONVICTION:** 5

**WHAT WOULD CHANGE THIS:** the 10-year at ≥5.5% with the price still falling retires it.
A dividend cut at the print kills it.

**PORTFOLIO FIT:**
- `portfolio`: Real Estate is at 0%, so it "diversifies industry", and it is the first
  direct US listing, so it "diversifies country". It "concentrates cap-tier" like
  everything else.
- Price in SEK: 22.79 × 10.0688 = **229.47 SEK**. ABB's ~3,780 SEK buys **16 shares
  (~3,672 SEK)**, not last sweep's 17, because of the FX move.
- Confirm it is tradeable in the Avanza ISK and how US dividend withholding treats it.

**FINAL CALL: BUY** — 16 shares from the ABB proceeds. If ABB does not sell, this call
has no funding and stands as merit-only.

**HORIZON:** Medium

#### #4 OPPORTUNITY: NVDA — Nvidia

**CATEGORY:** watchlist

**RANK HISTORY:** 2 now; 4 (10-05). **8 of 8 in the top 10.**

**VOICES IN FAVOR:**
- Growth, 8: +105.9% on a 100% CAGR, forward at half of trailing.
- Valuation, 7: forward 14.41x vs 28.99x.
- Fundamental, 7: ROIC 59.2%, net cash.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: beta 2.216 against an untested tolerance.
- Macro: duration at a 5.22% 10-year, plus a worse FX entry.
- Fundamental's caveat: FCF is ~22% of earnings.

**STRONGEST CASE FOR:** Growth's. The cleanest forward/trailing signal in the set, with no
suspect flag and no screen penalty.

**STRONGEST CASE AGAINST:** Fundamental's. FCF yield 0.76% against a ~3.45% earnings
yield, USD over USD, so it is real.

**KEY DISAGREEMENT:** three voices see the cheapest measured growth in the set; two say
the earnings are neither stable nor yet cash. Not reconciled.

**DATA GAPS:** no revisions or backlog; the PEG moves between prints (not relied on); no
US insider data.

**CHAIRMAN CONVICTION:** 6

**WHAT WOULD CHANGE THIS:** FCF yield moving toward the earnings yield after the **11-17**
print raises it. Forward P/E above trailing kills it.

**PORTFOLIO FIT:**
- `portfolio`: it would add the first Technology line to the visible sleeve and
  "concentrates cap-tier".
- One share is ~2,320.70 SEK (230.48 × 10.0688) against 845 SEK of ISK cash.
- P3's proceeds are already spoken for (AZN, gold tranche 2, the equity underweight).

**FINAL CALL: HOLD-WATCH.** Strong on merit; held for capital and the untested drawdown
tolerance, not for doubt about the business.

**HORIZON:** Medium

#### #5 OPPORTUNITY: INVE-A.ST — Investor A (the S6 window that passed)

**CATEGORY:** holding

**RANK HISTORY:** 12 now; 11 (10-05). **2 of 8 runs in the top 10** (09-14 and 09-21).

**VOICES IN FAVOR:** Copycat, 5: insiders bought at 395.90–411.55 in September; today's
398.20 sits inside that range.

**VOICES AGAINST / CAUTIOUS:**
- Fundamental and Valuation: no usable metric. P/E 4.72 and PEG 4.91 are holding-company
  artifacts.
- Thesis-review: WEAKENING, with the price at 95.1% of its 52-week high.

**STRONGEST CASE FOR (holding):** Copycat's. Five-plus distinct insiders bought through
2026 at rising prices, with zero disposals in the pull.

**STRONGEST CASE AGAINST:** there is still no valuation evidence of any kind, and the
cheapest chance to get it (the 2026-10-07 Q3 report) has passed.

**KEY DISAGREEMENT:** none left to adjudicate. That is the point of the pre-committed
fallback: a question this system cannot answer stops consuming a slot every sweep.

**DATA GAPS:** NAV discount/premium (S6); this sweep had no web or PDF access to the Q3
report. No earnings date returned by the calendar.

**CHAIRMAN CONVICTION:** 6 (that no action is correct; not a valuation view)

**WHAT WOULD CHANGE THIS:** you recording a NAV figure (from the Q3 report or Investor's
IR page) into `data/company_profiles/INVE-A.ST.json`, or a Cederholm disposal.

**PORTFOLIO FIT:** 1,991 SEK, 0.9% of capital; Financial Services is 6.6% of the visible
sleeve. No fit pressure either way.

**FINAL CALL: NO ACTION — durable hold.** The 2026-10-05 pre-commitment, applied as
written: not re-flagged again unless the NAV arrives.

**HORIZON:** Long

### 3c. Other SELL recommendations on current holdings

You get a direct answer to "should I sell anything" every sweep. Beyond ABB.ST:

- **ATCO-B.ST.** Valuation SELL at 5, **declined.**
  - It is the best business held, and its break condition (ttm revenue negative) has
    not fired (+9.1%).
  - The **10-22** print is the test. **NO ACTION.**
- **VOLV-B.ST.** Defensive SELL at 4, **declined.**
  - TOO_EARLY; the 10-23 print and the ~11-03 3-month checkpoint come together.
    **NO ACTION.**
- **SHB-A.ST.** Growth SELL at 4, **declined.** One share, 150.20 SEK. **NO ACTION.**
- **BTC0E.AS.** A sizing question, not a thesis sell. See D-c in §6.
- **ALFA.ST, INVE-A.ST, ETH, Xetra-Gold, Avanza Global, Avanza Auto 3:** no sell flag.
  ETH cannot be sold cleanly while P1 is open.

**Considered for the Top 5, not placed:**
- **APP** (HOLD-WATCH in substance, conviction 4). No new information this week (−0.4%);
  the 11-04 print decides it.
- **GM.** The only first-seen name; see §2.
- **LLY / META.** Growth-only cases, no second lens in support.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens:

| Dimension | Grade | Number behind it |
|---|---|---|
| Asset allocation vs targets | WATCH | Equity 71.9% vs 80% target (-8.1pp); cash 12.0% vs 5% (+7.0pp). Driven mostly by idle PayPal cash (14,887 SEK, outside any wrapper) and the HB tax reserve (11,364 SEK, not deployable) — not a market-driven drift. |
| Equity sector concentration | ACT (visible sleeve) / UNKNOWN (fund-wrapped 80%) | Industrials = 54.6% of the 32,436 SEK identifiable individual-stock sleeve (VOLV-B, ATCO-B, ALFA, ABB) — well over the 45% ACT line. But 80% of the true equity sleeve sits in Avanza Global + Auto 3, which carry no look-through sector data (standing gap, named below) — the sleeve-wide figure cannot be computed, only the visible slice. |
| Geography (home bias) | ACT (visible sleeve) / UNKNOWN (fund-wrapped 80%) | Sweden = 49.5% of the same 32,436 SEK identifiable sleeve — over the 45% ACT line. Same fund-wrapped caveat as above. |
| Currency exposure | UNKNOWN | No revenue-by-currency breakdown was fetched this sweep. Qualitatively diversified (crypto USD, gold EUR, Avanza Global broadly multi-currency, PayPal USD+EUR) but not quantifiable from today's data — not graded on a guess. |
| Single-position concentration | ACT (mechanical) | Avanza Global = 53.2% of total portfolio (119,999 / 225,411 SEK) vs the 15% cap. Flagged because the rule is mechanical ("any single holding"), but this is a globally diversified index fund, not single-company risk — context, not an argument to trim a core holding. |
| Institution concentration | ACT | Avanza ISK = 82.6% of total (186,192 / 225,411 SEK) vs the 80% cap — standing issue, essentially unchanged for many sweeps. |
| Fee drag | OK | 187.12 SEK/yr total (0.083% of portfolio) vs the 0.4% cap. No fund over 0.5%. |
| Wrapper efficiency | OK (core) / minor note | ISK vs AF axis is clean (lever #1 closed). Secondary: ~14,887 SEK sits idle in PayPal outside any wrapper with ISK headroom of ~113,800 SEK before the 300k allowance (verify current threshold) — a convenience/FX-friction issue, not a tax-wrapper one, since it's uninvested cash, not an appreciated asset. |
| Drawdown-tolerance fit | UNKNOWN | S26's only quoted figure (-20.62% max DD) has no backing file. data/backtests/ does not exist. Cannot be graded OK on an unverifiable number. |

**Provisional, per `investor_profile.json`:**
- `horizon.primary_goal` is "nature UNCERTAIN", with a soft 3–7y horizon.
- `constraints.exclusions` is empty ("None stated yet"). That matters because MO is a
  live Defensive pick.
- The profile was last updated 2026-07-20. Its `reference_targets` still reads 85/10/0/5
  with no gold line, while `portfolio.json.targets` holds 80/10/5/0/5. Two files
  disagree on one concept (see the target proposal in the structural section).

**Denominator, unpinned.** The crypto row reads 10.65% of total capital, but **11.21%** of
the investable base (23,999.65 / 214,047.29, excluding the 11,363.76 SEK tax reserve).
Last sweep used the investable base. This memo uses it for D-c.

---

## 5. Headline calls

Each needs a decision this session.

1. **SELL ABB.ST (all 4 shares) before 2026-10-20 and BUY 16 VICI with the proceeds.**
   ABB conviction is 5 and the window is non-renewable. VICI conviction is 5. If you are
   holding ABB through the print deliberately, say so.
2. **Read one number off Avanza: the current value of your 150 BTC0E.AS units.** If it is
   above **~11,730 SEK**, trim back to 10% of the investable base. If not, no trade
   (D-c, §6).
3. **Execute P3 (PayPal → SEK → ISK), now a 10th-plus sweep.** About 14,290 SEK net at the
   accepted 4% spread. It funds the AZN.ST share (1,574.50 SEK) and gold tranche 2
   (~5,590 SEK), with the rest to Avanza Global.
4. **Accept or override the durable INVE-A.ST hold (D-b).** Silence means accept.
5. **Keep 80/10/5/0/5 as the provisional target and make S26 the next build** (structural
   section). This is a reaffirmation, not a change.

---

## 6. Open actions vs open decisions

### Open actions (things to go do), by ID

| ID | Status | Action |
|---|---|---|
| **P3** | decided — pending execution (10th-plus sweep) | Convert 1,177.49 USD + 266.88 EUR in PayPal (14,887 SEK per `portfolio`, ~595 SEK spread at 4%) and transfer ~14,290 SEK net to the ISK. Zero the paypal holdings in `portfolio.json`. |
| **S26** | open, top build | Run the shock-window backtest and **write its output to `data/backtests/`** (the directory still does not exist, per `portfolio`). |
| **P1** | blocked (on you) | ETH cost basis. Blocks any ETH sale. |
| **P9** | open | Delete the phantom AZN OPENING row in the Excel Transactions tab. |
| **P10** | open | Confirm one 5,000 SEK deposit or two (2026-08-17 vs 2026-08-22). |
| **S6** | open, no longer a decision trigger | No free NAV source exists. Kept as a system item only. |

The D-series still has no standalone register (S30 closed under cap pressure). It is
reconstructed again below.

### Open decisions (forks), by ID

**D-a — ABB.ST and where its proceeds go.** Final window: 8 days.
- *Option 1 — sell before 10-20, buy 16 VICI.* Industrials ACT → WATCH (42.9%). Trade-off:
  rate and FX risk on a USD REIT, bought at DXY 121.
- *Option 2 — sell before 10-20, hold the cash.* No rate or FX risk. Trade-off:
  Industrials stays ACT (~48.6%), and cash is already 7pp over target.
- *Option 3 — hold through the print.* The call lapses at 10-20 and the 10-26 memo
  re-decides on Q3 numbers. Trade-off: you turn a valuation decision into a single-event
  bet.
- **Pick: Option 1.** Option 2 is the honest fallback if you do not want USD REIT
  exposure.

**D-b — Investor A's unmeasurable valuation.** The trigger passed with nothing recorded.
- *Option 1 — durable hold, stop re-flagging* (selected as default per the 2026-10-05
  pre-commitment). Trade-off: a 1,991 SEK position held without valuation evidence,
  indefinitely.
- *Option 2 — you record the NAV yourself* from Investor's Q3 report or IR page (~10
  minutes). This re-opens a real call. Trade-off: your time, for a 0.9% position.
- *Option 3 — sell all 5 shares on absence of evidence.* Trade-off: you exit against
  four weeks of insider buying, on missing data rather than bad data.
- **Pick: Option 1.**

**D-c — crypto sleeve sizing.** Re-framed this sweep.
- *Option 1 — trim ~2,500 SEK of BTC0E.AS now* (last sweep's pick). Trade-off: the trim
  is about the same size as the plausible error in a 7-week-old mark, so you may be
  trading against noise.
- *Option 2 — band rule (new).* Read the live Avanza value of the 150 units, V.
  - Crypto = 12,967.79 (ETH) + V. Investable base = 203,016.29 + V.
  - Trim back to 10% only if crypto exceeds **11.5%** of that base, i.e. if V is above
    ~**11,730 SEK** (~78.2 SEK/unit, against the 08-21 mark of 73.54).
  - Trade-off: a mechanical tolerance band substitutes for the S26 analysis it cannot
    replace.
- *Option 3 — no action until S26 runs.* Trade-off: an untested tolerance with F&G at
  "Greed" and DXY rising.
- **Pick: Option 2.** What changed is the evidence, not the risk view:
  - ETH's −5.6% pulled the sleeve from 11.53% to 11.21% investable (at the stale BTC
    mark).
  - This sweep fetched no BTC price at all, so the trade size cannot be set without your
    number.
  - Macro's dissent (strong dollar plus Greed) argues against *adding* and stays on
    record. It does not set the size of a trim.

---

## 7. Cost of being wrong

| Headline call | If wrong | Realistic SEK downside | Recoverable? |
|---|---|---|---|
| SELL ABB.ST before 10-20 | Q3 beats and the stock re-rates 25% | ~945 SEK foregone (25% of 3,780) | Yes. It stays in the universe and can be rebought tax-free in the ISK. |
| BUY 16 VICI | The 10-year hits 5.5%+, the REIT de-rates 30%, SEK strengthens 10% | ~1,100 SEK + ~370 SEK FX, offset by ~295 SEK/yr dividend (8.04%) | Yes. Income-producing, ~1.6% of capital. |
| D-c band rule (no trim at the stale mark) | Crypto halves from a "Greed" reading | ~12,000 SEK on the 24,000 SEK sleeve; ~1,300 SEK of it on the overweight | The overweight part, yes. Whether the whole loss fits −30% is what S26 hasn't tested. |
| Execute P3 / BUY 1 AZN.ST | You pay the spread; AZN falls 30% | ~595 SEK spread (certain) + ~470 SEK on the share | Spread, no, and it recurs every ~2 months while P3 waits. AZN, yes. |
| Accept the durable INVE-A.ST hold | The NAV premium is stretched and the stock de-rates 30% | ~600 SEK on 1,991 SEK | Yes. Small, ISK, tax-free exit at any time. |
| Keep 80/10/5/0/5 provisional | A ≥−30% shock arrives before S26 runs | −30% on 225,411 SEK ≈ 67,620 SEK, at the edge of tolerance or beyond | Only with time. The soft 3–7y horizon is what makes it recoverable. |

---

## 8. Timing collisions

From `data/cache/calendar/20261012-events.json`. Caveats:
- `calendar_last_verified` is 2026-08-03.
- US/SE CPI dates are missing.
- **This calendar covers holdings only.** No candidate dates exist; VICI's and APP's are
  carried from the 2026-10-05 calendar file.
- INVE-A.ST returned no date (a data gap, not confirmed quiet).

- **10-20: ABB.ST reports.** D-a's hard edge: sell before, or the call lapses.
- **10-21 SHB-A.ST, 10-22 ATCO-B.ST, 10-23 VOLV-B.ST.** ATCO's print tests its break
  condition; VOLV's tests its TOO_EARLY thesis.
- **10-27: ALFA.ST reports on FOMC day 1.** The price reaction will mix company news with
  the rate decision. No ALFA trade is proposed; read the results, not the day-one move.
- **10-28: FOMC statement.** VICI's print falls the same day (per the 10-05 calendar).
  Buying VICI alongside the ABB sale *before 10-20* avoids a rate-decision-plus-earnings
  entry day.
- **10-30: AZN.ST reports.** This is the test for the share add. If P3 executes before
  then, the share is bought ahead of the print; that is acceptable on a Medium-horizon
  call, and flagged here so it is a conscious choice.
- **11-04: Riksbank decision** (and APP's print, per the 10-05 calendar). **11-10:**
  Riksbank minutes.

---

## 9. Data gaps for `meta`

Ordered by what each cost this sweep. Surfaced, not fixed.

1. **No BTC price fetched, and BTC0E.AS carried at a 2026-08-21 mark.** The snapshot's
   crypto block holds only `ethereum`. D-c could not be sized and had to be converted
   into a band rule keyed to a number you supply.
2. **67.8% of capital has no live mark** (152,910 / 225,411 SEK: Avanza Global and Auto 3
   at book value, gold and BTC at stale marks). The OUTCOME pillar's "actual vs
   benchmark" rests mostly on unrepriced values.
3. **FI insider data: no publication after 17/09 for any of the 7 issuers.** Separately:
   - The first fetch this sweep failed on a missing `bs4` dependency, so all four lenses
     ran without FI data.
   - The "Volvo" search still returns Volvo Car AB rows.
   - Industrivärden is not pulled.
   - US insider data is zero (EDGAR 403).
4. **S27, 8th occurrence (by OPEN_ITEMS.md's count), plus an in-session instance.** This
   sweep's launch note presented ALFA's 2026-09-11 insider buy as "fresh this sweep" and
   asserted "11/11". The buy was already in the 2026-10-05 memo, and this pull shows
   10/10. On the positive side, `position_report.py` output was handed over as a file
   path this sweep, as recommended last sweep.
5. **The `source=new` miscount: a second explicit catch.** 33 rows carry `new`; 1 is
   first-seen (GM) and 2 are returnees. The 2026-10-05 "considered, not opened" entry
   said a second catch "would meet the pattern-recognition bar". It has.
6. **S32 unfixed, and a wider cluster of implausible FCF yields on value-ranked names**:
   GM 30.22%, MEKO.ST 36.43%, GPN 36.17%, DOM.ST 27.07%, ALL 26.13%, CORE-B.ST 24.15%,
   and TSM 31.08% for a 6th sweep. These feed the value lens, which S33 measures as
   anti-correlated. GM, the only first-seen name, ranks almost entirely on two such
   fields.
7. **The suspect flag moved a rank materially, and correctly.** INDU-C.ST fell 8 → 28 once
   its 102.5% operating margin was withheld. Worth checking that INVE-A.ST (88.7%
   operating margin, the same holding-company artifact, unflagged) is not being ranked
   12 on the same distortion.
8. **S29, 8th sweep:** APP still at 3% of range with no endpoints. **S21:** AZN.ST has no
   `forward_pe` in 8 of 8 runs.
9. **Calendar: holdings only, no candidate dates** (the regression flagged 09-28 is
   unchanged).
10. **No EV/EBITDA, FFO or AFFO** (VICI). No commodity or credit-spread series (EXE,
    FANG, TPL unassessable). `us_cpi_yoy` is dated 2026-08-01.
11. **The allocation denominator is still unpinned** in `data/definitions.json` (total vs
    investable). Crypto reads 10.65% or 11.21% depending on the base.
12. **CLAUDE.md priority line 2 is stale** (per `portfolio`): "the 2.5% BTC certificate
    (P4)" was closed 2026-08-17.

---

## Structural decisions (non-stock)

Levers 1–2 (wrapper, fees) are structurally closed and not re-flagged.

**ACTION:** Execute P3. Convert the PayPal balance and transfer it to the Avanza ISK.
- **POSITION:** ~14,887 SEK (1,177.49 USD + 266.88 EUR at this sweep's FX, per
  `portfolio`), outside any wrapper.
- **TARGET:** ISK. ~5,590 SEK to gold tranche 2 (closes the −2.48pp gap), 1,574.50 SEK to
  the AZN share, the remainder (~7,130 SEK) to Avanza Global.
- **REASON:** a recurring ~4% spread on every ~2-month inflow, and the binding constraint
  on three other calls.
- **THESIS STATUS:** decided by you 2026-08-17 (Option A).
- **WHAT CHANGED:** only the count (10th-plus sweep).
- **BREAK CONDITION:** a fee-free route appears, or the realised spread is materially
  above 4%.
- **CONFIDENCE:** High (arithmetic, not a forecast).
- **HORIZON:** Long

**ACTION:** D-c band rule. Recommended, not executed; nothing in this system trades.
- **POSITION:** BTC0E.AS, 150 units, carried at 11,031 SEK (2026-08-21 mark; the feed
  404s). Crypto is 11.21% of the investable base at that mark.
- **TARGET:** trim to 10% of the investable base only if the live value exceeds ~11,730
  SEK. Proceeds go to Avanza Global (`profit_recycling_rule`). ETH stays untouched (P1).
- **REASON:** the proposed trade is smaller than the uncertainty in the mark.
- **THESIS STATUS:** INTACT (thesis-review). This is a sizing action.
- **WHAT CHANGED:** ETH −5.6% shrank the overweight, and no BTC price was fetched.
- **BREAK CONDITION:** S26's shock-window result, which supersedes the band either way.
- **CONFIDENCE:** Medium
- **HORIZON:** Medium
- *Not in the picks ledger:* BTC0E.AS has no fetched price to join.

### Target allocation — proposal only (nothing written to any file)

**What is currently written.**
- `portfolio.json.targets`: equity 80 / crypto 10 / cash 5 / FI 0 / gold 5. The base was
  adopted 2026-08-03 and the gold carve applied 2026-09-02.
- `investor_profile.json.reference_targets`: 85/10/0/5 with no gold line. This is stale
  against the carve.
- `glidepath_table.now_T5plus` (50/40/5/5) is superseded by your 2026-07-22 direction
  (fixed income near zero, equity above 70% accepted). It re-engages only if the
  property goal firms up.

**Tested against the profile.**
1. **−30% max drawdown: no traceable test exists.**
   - The only "pass" (−20.62%) has no file (`data/backtests/` absent) and came from a
     window whose worst equity shock was −19.14% (S26).
   - **Break-even arithmetic, using assumed shocks rather than data:** with gold flat and
     crypto down 70%, the 80/10/5/0/5 target breaches −30% once equity falls more than
     **~28.75%** (0.80E + 0.10 × −70 = −30).
   - At last sweep's alternative, 80/7/5/0/8, the break-even moves only to ~31.4%.
   - Cutting crypto by 3pp buys about 2.6pp of equity-shock headroom. That is real, but
     it does not change whether a 2008-scale equity shock breaches the tolerance. Only
     the equity weight does.
2. **Horizon, 3–7y SOFT.** 80% equity is defensible only because the goal has no date.
   The glidepath's `T3y` row (40/45/10/5) would mean selling about half the equity,
   possibly into a drawdown, if the goal firmed.
3. **Today's actual exposure is lower than the target.** Equity is 71.9% and cash 12.0%
   (`portfolio`). The live drawdown risk is below what the target implies until P3 and
   new contributions deploy.

**Proposal.**
- **Reaffirm 80/10/5/0/5, labelled PROVISIONAL.** Do not cut crypto pre-emptively; the
  arithmetic above shows it is the wrong lever for the risk that matters.
- Add D-c's ±1.5pp crypto band (on the investable base) as the operating rebalance rule
  until S26 reports.
- Give the glidepath re-anchor trigger an owner: ask once a quarter at `journal`'s
  session start whether the property goal now has a date inside 3 years.
- Separately, when you next edit the profile, replace its duplicated 85/10/0/5 with a
  pointer to `portfolio.json.targets`, the owner under CLAUDE.md's data-ownership table.

**What would change this proposal:** S26's shock-window result. If it is worse than −30%
at 80% equity, the next proposal cuts *equity* toward 70% with cash or gold ballast, not
crypto alone.

---

## 10. Learning notes

- **A deadline you set yourself only means something if you honour it when it arrives.**
  On 2026-10-05 this system said that if the Investor AB NAV window passed with nothing
  recorded, the "hold and stop asking" fallback becomes permanent. The window passed, so
  it is permanent. Re-flagging it again "just in case" would make every pre-commitment
  this system writes worthless.
- **When the price you are using is older than the trade you are planning is large,
  fetch the price first.** A ~2,500 SEK trim on a position whose last real price is seven
  weeks old could be the wrong size or the wrong direction. That is why D-c now asks for
  one number before any trade.
- **A case that keeps losing legs under testing should lose conviction too, even if the
  verdict survives.** ABB's SELL rested on five arguments five weeks ago and rests on two
  today. It is still a SELL, because no lens would buy it today. But conviction 5 is the
  honest number, and the print is the last chance to act on it at all.
- **"New" in a data file is a label someone chose, not a fact about the world.** 33 rows
  said "new", and one name actually was. Any count you read in a report is worth checking
  against what the word in the file actually means.

---

`journal` **must run next.** An unlogged memo is invisible to the next session and can
never be reconciled. Then run `python scripts/decisions.py record --picks
data/picks/2026-10-12-picks.csv`, followed by `python scripts/decisions.py basis --write`.
