# Council Memo — 2026-09-28

*This is a structured synthesis of your own agents' analysis over data fetched this
session. It is not licensed investment advice. Every number below comes from a file
written today, or is labelled as carried or user-relayed.*

---

## What leads this memo: the execution backlog, not a new finding

`OPEN_ITEMS.md`'s recommended emphasis (from the 2026-09-21 review) is
**portfolio-tending**, and today's data backs it. Nothing in this memo needs new
research. What it needs is for four calls that are already made to be carried out,
declined, or explicitly re-decided:

1. **ABB.ST SELL, now in its 6th consecutive sweep** (first made 2026-08-24). ABB
   reports on **2026-10-20**. If the sale waits past that date, a valuation decision
   becomes a bet on one earnings print.
2. **The VICI BUY that has depended on the ABB sale for 5 sweeps.** This memo
   **separates the timing of the two legs**. The ABB sale should happen before 10-20
   whether or not you buy VICI. But the concentration fix needs the second leg (see #1
   and #3 below).
3. **The AZN.ST share is still blocked on P3.** ISK cash is 845.43 SEK, which I
   re-checked against this sweep's `portfolio` output. One share costs 1,630.00 SEK.
   P3 has now gone unexecuted for 8+ sweeps.
4. **D-c's own stated default takes effect this sweep.** Last sweep's Chairman wrote: "if
   S26 is not run before the next sweep, Option 1 [trim the crypto leg] becomes the
   default." S26 has not run. The `portfolio` lens confirms the trigger fires: "YES,
   stated default should trigger this sweep". I carry that out below, with a correction
   to how the lens measured the overweight (§6, D-c).

Institution concentration (Avanza 82.65%, ACT) is still unresolved. It is structural,
and nothing in this memo moves it.

**Two false premises in this sweep's launch prompt, corrected (6th confirmed occurrence,
S27).** The scheduled task again claimed that (a) "open structural question #1
(Handelsbanken wrapper) is unresolved, the memo MUST open with it", and (b)
`investor_profile.json` `reference_targets` "are null", so a target must be proposed from
scratch. Both are false:
- (a) CLAUDE.md's priority order says wrapper efficiency is "DONE 2026-08-03. All capital
  is in the ISK", and `portfolio.json`'s `hb-af-exit` plan is fully executed.
- (b) `reference_targets` holds the target adopted 2026-07-27 (85/10/0/5).
  `portfolio.json.targets` holds the gold-adjusted 80/10/5/0/5 applied 2026-09-02.
  Drift below is measured against those real targets.

The same two lines have now come through unedited in six sweeps (2026-08-31, 09-07, 09-14,
09-21, 09-28, plus a different drift on 08-17). The fix still requires a five-minute edit
to the scheduler's stored prompt, which sits outside this repository. This is recorded
for `meta` against S27 and is not worked around silently.

---

## 1. Position report

## Position report — 2026-09-28
Snapshot: `20260928T062025.json` · previous: `20260921T060913.json`

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 154.50 | -0.4% | +19.5% | 94% | 154.50 | fetched |
| Investor A (stock) | 401.90 | +0.2% | +38.5% | 87% | 2,009.50 | fetched |
| Volvo B | 321.20 | -4.9% | -12.6% | 59% | 4,175.60 | fetched |
| Atlas Copco B | 176.20 | +2.2% | -2.8% | 82% | 4,757.40 | fetched |
| AstraZeneca | 1,630.00 | +0.2% | +6.0% | 45% | 13,040.00 | fetched |
| Xetra-Gold (physically-backed gold ETC, ISIN DE000A0S9GB0) | no data | no data | no data | - | 5,689.22 | FETCH FAILED |
| Alfa Laval | 559.60 | +0.6% | -2.6% | 81% | 5,036.40 | fetched |
| ABB | 966.20 | +1.9% | +2.0% | 78% | 3,864.80 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| Valour Bitcoin Zero SEK (certificate, ISIN CH0585378661) | no data | no data | no data | - | 11,031.00 | FETCH FAILED |
| ETH (self-custody wallet) | 26,341.67 | +0.7% | no data | - | 13,219.57 | fetched (CoinGecko, converted via sek_per_eur) |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high.*

### Crypto context (spot, from CoinGecko)
| Coin | Price (EUR) | Δ vs prev snapshot | 7d | 30d | vs ATH |
|---|---|---|---|---|---|
| ethereum | 2,329.74 | +0.2% | -0.4% | +8.7% | -44.9% |

**What moved, and whether it matters.**
- **Volvo B −4.9%** (now −12.6% vs cost, 59% of range) was the only real move. It does
  **not** contradict the TOO_EARLY recovery thesis, because no fetched fundamental moved
  against it. ttm revenue is still +2.7%, and the forward P/E fell to 13.06 while
  trailing is 18.47 (PEG 0.95). The price fell, the business numbers did not. No fetched
  field explains the drop, and I will not invent a reason. The test is still the
  2026-10-23 print.
- **ABB +1.9%** is not vindication. This is a valuation and cash-conversion SELL, and a
  higher price only raises the proceeds.
- **Two feeds failed:** Xetra-Gold and the BTC certificate both returned 404. They are
  carried at cost (5,689.22) and at the 2026-08-21 broker mark (11,031.00), so ~16,720
  SEK of the portfolio has no live price.
- **Index funds:** book value only, nothing to read.

---

## 2. Scout health

```
Universe    624
Fetched     621  (cache 579, new 46, failed 4)
Ranked      613
Candidates  75   (holdings 9, watchlist 30, new 36)
Focus       23
Screened    75
Passed      39
Missing     18
Failed      18
Status      VALID
```

**Reading:** the funnel is VALID and **36 of 75 candidate rows are `new`**, so discovery
is producing. The first scout run this sweep returned DEGRADED only because
`data/universe.json` was 35 days old against a 30-day refresh interval. After
`build_universe.py` rebuilt it (624 tickers, +3/−3), scout re-ran VALID. No filter was
broken and no fetch was bad, so nothing needs distrusting.

The head of the funnel is still frozen:

- **Correction to the launch note.** The launch note said APP/SNDK/NVDA/MA/V/TSM/
  INDU-C.ST/VICI had been top-10 "for 7 consecutive runs". `data/candidate_history.csv`
  holds only **6 runs** (08-25 to 09-28), and those eight names were top-10 in **all 6**.
- **MU:** top-10 in 5 (first seen 08-31).
- **INVE-A.ST:** 2 of 6 (09-14, 09-21), back to rank 12 today.
- **TPL:** 3 of 6, none since 09-07.
- **CHTR** is the only genuinely new entry into the top-10 (rank 9, from 14). It got there
  by **falling 11.9% in one week**. That tells you the value lens rewards falling prices,
  not that CHTR has been discovered as a good company. See #5.

The same Nordic coverage gap as last sweep (S21) drives the 18 MISSING rows. INVE-A.ST,
INDU-C.ST, SHB-A.ST, SWED-A.ST, SEB-A.ST, LUND-B.ST, ERIC-B.ST, ASSA-B.ST, LATO-B.ST,
BURE.ST and AZN.ST all lack `forward_pe` or `debt_to_equity`.

Suspect values withheld from lens scores this sweep:
- ABB.ST `price_to_book`=109.57
- INDU-C.ST `revenue_growth`=1197.9%
- SNDK `revenue_growth`=371.6%
- MU `revenue_growth`=345.7%
- CMCSA `peg`=142.98
- ASML `price_to_book`=1496.99 and `roic`=4.04
- KINV-B.ST `price_to_sales`=−2.14
- FANG `peg`=20.69

**Still not flagged, a 4th sweep running:** TSM `roic_pct` 183.7% and `fcf_yield_pct`
31.27% (S24).

---

## 3. Top opportunities

### 3a. The seven voices (independent passes)

Each voice first ran a quick numeric sort over its own columns across all 75 rows, then
drafted without seeing the other voices. Where a voice pulls in a name outside `focus=Y`,
or argues against a name's own screen flag, it says so.

#### Voice 1 — Fundamental / Quality

*Triage (`z_quality`):* APP 2.570, SNDK 2.546, NVDA 2.503, MU 2.333, MA 2.231, V 1.938,
TSM 1.919, INDU-C.ST 1.904, INVE-A.ST 1.823, TPL 1.820, MO 1.794, LLY 1.727.

- **BUY V (Visa), 8.**
  - Why: ROIC 41.5%, ROE 61.2%, net margin 50.8%, operating margin 66.1%, net
    debt/EBITDA 0.32, FCF yield 2.96%, revenue +14.4% on a 10.9% 3-year CAGR. That is
    >40% ROIC, double-digit growth and no balance-sheet strain at once. Moat reasoning
    (two-sided network) is qualitative; no field measures it.
  - Risk: regulation of interchange fees cutting Visa's take rate. It is political and
    shows in no metric until it lands.
  - Invalidated by: ROIC below ~30%, or revenue growth at mid-single digits for two prints.
- **BUY NVDA, 7.**
  - Why: ROIC 59.2%, ROE 117.2%, net margin 63.7%, operating margin 66.2%, net
    debt/EBITDA −0.12 (net cash), D/E 16.97.
  - Held at 7 on one specific number. The FCF yield is **0.77%** against an earnings
    yield of ~3.5% (1/28.49). So under a quarter of reported earnings is showing up as
    free cash this period, and trailing-only FCF cannot tell working-capital build from
    anything worse.
  - Invalidated by: FCF yield staying below 1% for another two sweeps while earnings grow.
- **BUY MA (Mastercard), 7 (pulled back in against its screen FAIL).**
  - Why the FAIL is not the story: D/E 439.58 is a buyback-driven negative-equity
    artifact. Net debt/EBITDA is 0.59.
  - Underneath: ROIC 56.1%, margins 46.3/61.1, revenue +14.1% on a 13.8% CAGR.
  - Risk: the same take-rate regulation as V, with no book-equity cushion against a
    large legal settlement.
  - Invalidated by: net debt/EBITDA above 2.0.
- **BUY TSM, 6.**
  - I **discard** `roic_pct` 183.7% and `fcf_yield_pct` 31.27% as implausible for a
    capital-intensive foundry. This is the 4th sweep they have gone unflagged, and they
    still feed z_quality 1.919 (S24).
  - The case rests on ROE 40.0%, net margin 49.9%, operating margin 60.3% and net
    debt/EBITDA −0.77 alone.
  - Invalidated by: operating margin below ~45%.
- **BUY ATCO-B.ST (holding), 6.**
  - Why: ROIC 39.7%, ROE 25.7%, operating margin 20.6%, net debt/EBITDA 0.50, ttm revenue
    +9.1%. It is the best business among the holdings. This is a verdict on the business
    only; price is Valuation's job.
  - Risk: short-cycle orders turning before the 10-22 print.
  - Invalidated by: ttm revenue growth turning negative.
  - Missing: `forward_pe` (S21).
- **SELL ABB.ST, 7.**
  - Why: FCF yield 0.09%; FCF/revenue ~4.4% (thesis-review: FCF 1.57B on revenue
    35.75B). ROIC 20.6% is not a quality franchise when owners receive this little cash.
  - Risk of being wrong: FCF is trailing-only, so capex timing cannot be ruled out.
  - Invalidated by: FCF/revenue above ~8% in the next annual report.
- **Declined:**
  - **APP.** ROE 203.7% is inflated by leverage (D/E 111.13), and the price sits at 3% of
    its range, which no quality field explains (S29).
  - **MU/SNDK.** Operating margins of 80.4/78.5% look like peak memory-cycle margins, and
    both carry suspect revenue growth.
  - **INVE-A.ST/INDU-C.ST.** Holding-company fields cannot be graded as operating quality
    (S6).

#### Voice 2 — Valuation

*Triage (`z_value`):* CHTR 1.836, CMCSA 1.829, ALL 1.794, FIS 1.765, EG 1.696, FISV 1.635,
CORE-B.ST 1.507, BURE.ST 1.491, DOM.ST 1.490, MEKO.ST 1.413, SYF 1.391, AFRY.ST 1.350,
INDU-C.ST 1.283, DIOS.ST 1.248, INVE-A.ST 1.165, EXE 1.126, EIX 1.113, VICI 0.766.

- **BUY VICI, 8.**
  - Why: 9.11x trailing / 7.86x forward, 7.83% dividend, 67.5% net margin, revenue +5.7%
    on a 15.5% CAGR, **1% of its 52-week range**, screen PASS. It is cheaper than last
    sweep and no fetched field got worse.
  - Approximation, flagged: this system has no EV/EBITDA, so I am approximating from net
    debt/EBITDA 4.82, which is high. I quote no enterprise multiple.
  - Risk: the discount rate and the refinancing cost rise together. The 10-year moved
    from 4.94% to 5.18% between sweeps.
  - Invalidated by: a dividend cut, or net debt/EBITDA above ~6.
  - Missing: FFO, AFFO and lease coverage, the metrics REITs are actually valued on.
- **BUY NVDA, 7.**
  - Why: PEG 0.47, forward 14.35x against trailing 28.49x, on 105.9% revenue growth. The
    forward multiple is below the multiple on most defensive names in this set (KO
    24.90, PG 19.76, JNJ 22.34).
  - Risk: the forward figure assumes consensus AI capex continues; this system fetches no
    revisions.
  - Invalidated by: forward P/E rising above trailing.
- **BUY AZN.ST (holding), 6.**
  - Why: PEG 1.16, improved from 1.33 at the 2026-08 review, price at 45% of range.
    Background, labelled: large-cap pharma typically trades 15–20x trailing, so the raw
    24.95x is a premium and the growth-adjusted figure is not.
  - Risk: FCF yield 0.19%, meaning the earnings are not currently cash.
  - Invalidated by: PEG above 1.6.
  - Missing: `forward_pe`, absent in all 6 runs on record.
- **BUY TSM, 6.**
  - Why: PEG 0.86, forward 20.55x against trailing 33.55x on 36% growth, net cash.
  - Lower than last sweep because the price rose 430.26 → 451.15 (+4.9%) to 87% of range,
    so some of the discount is gone.
  - Invalidated by: forward P/E rising above trailing.
- **BUY ALL (Allstate), 5 (focus name).**
  - Why: trailing 4.56x, forward 8.20x, PEG 1.67, 1.9% dividend, beta 0.15.
  - Stated plainly: the price fell **9.9% this week** (252.21 → 227.17) and forward P/E is
    **above** trailing, which means the market expects earnings to fall by roughly
    40–45%. I am buying 8.2x *forward*, not 4.6x trailing.
  - FCF yield 26.34% is unflagged but implausible for an insurer, because float passes
    through cash flow. I do not reason from it.
  - Invalidated by: forward P/E rising further above 10.
- **SELL ABB.ST, 7.**
  - Why: forward 36.43x is **above** trailing 35.59x despite 14.2% revenue growth, screen
    FAIL. P/B 109.57 is suspect; use the FX-corrected ~11.7x. No margin of safety.
- **SELL ATCO-B.ST, 5.**
  - Why: trailing 32.58x, PEG 2.18, 82% of range. Background, labelled: the industrials
    norm is mid-teens to low-20s.
  - Invalidated by: PEG below 1.5.
- **Cheap for a reason, not picks:**
  - **CHTR:** 2.94x, but D/E 441.58, revenue −1.7%, and −11.9% this week.
  - **CMCSA:** revenue −1.2%; PEG artifact.
  - **FIS:** revenue +29.1% against a −9.8% CAGR, net debt/EBITDA 5.82, and still falling
    (36.43 → 34.99). Dropped from last sweep's BUY because nothing resolved the
    divestiture-pattern question.
  - **EIX, AFRY.ST, EG, DOM.ST, MEKO.ST:** cheap, with nothing in the data saying why
    the discount is wrong.
- **No verdict possible:** INVE-A.ST, INDU-C.ST, BURE.ST, LUND-B.ST (NAV artifacts, S6).

#### Voice 3 — Growth / Opportunity

*Triage (`z_growth`):* NVDA 1.885, BE 1.773, AVGO 1.762, SMCI 1.741, APO 1.725, AXON 1.490,
DASH 1.474, FIX 1.468, FANG 1.437, LLY 1.430, APP 1.394.

*Forward P/E below trailing (the market pricing earnings growth):* SNDK 6.75 vs 24.10,
MU 6.79 vs 24.45, TPL 4.66 vs 43.50, NVDA 14.35 vs 28.49, APP 14.81 vs 23.87, AVGO 18.20
vs 45.58, APO 11.34 vs 43.31, LLY 25.00 vs 39.69, VOLV-B.ST 13.06 vs 18.47.

- **BUY NVDA, 8.**
  - Why: revenue +105.9% on a 100.0% 3-year CAGR, PEG 0.47, and the widest
    forward/trailing gap among names whose data is clean.
  - Risk: hyperscalers deferring capex spending for two quarters. No backlog or revision
    data exists here.
  - Invalidated by: revenue growth below ~40%, or forward P/E above trailing.
  - Missing: TAM, revisions, market share. Growth here means measured growth.
- **BUY LLY (Eli Lilly), 6 (pulled in from outside `focus=Y`, rank 21).**
  - Why: revenue +47.7% on a 31.7% CAGR with a 54.2% operating margin, ROIC 38.4%, PEG
    1.17, and forward 25.0x well below trailing 39.7x. It is the only healthcare name
    with measured hypergrowth.
  - Risk: D/E 162.07 and a growth rate that depends on one drug class, which is
    qualitative and labelled. NOVO-B.CO's growth falling from a 20.4% CAGR to 2.1% is
    the visible example of that franchise risk in this same file.
  - Invalidated by: ttm growth falling below 25%.
- **BUY AVGO (Broadcom), 5 (pulled in, rank 18, against its FAIL).**
  - Why the FAIL misleads: it is trailing P/E 45.58 > 40. Forward 18.20x on revenue
    +85.5% (24.4% CAGR) and PEG 0.35 say the trailing figure is backward-looking.
  - Held at 5 because 29% of range with no explanation, and 85.5% growth on a 24.4% CAGR
    suggests an acquisition base effect I cannot separate out.
  - Invalidated by: forward P/E rising toward trailing.
- **BUY VOLV-B.ST (holding), 5 (pulled in).**
  - Why: forward 13.06 < trailing 18.47, PEG 0.95, ttm revenue turned positive (+2.7%)
    after a two-year decline. That is an inflection. Thin, because the 3-year CAGR is
    +0.4%.
  - Invalidated by: the 10-23 print showing revenue back in decline.
- **BUY APP, 5.**
  - Why: +52.8% revenue at a 77.7% operating margin, PEG 0.67.
  - Held at 5: the price is at 3% of range for the 6th run and I cannot tell who is right.
  - Invalidated by: growth below 25%.
- **SELL ABB.ST, 5.** Revenue growth of 14.2% is being handed back in margin: the forward
  multiple is above trailing.
- **SELL SHB-A.ST, 4.** Revenue −3.8%, z_growth −1.275 (worst of any holding), forward
  13.67 above trailing 13.03. Immaterial at one share.
- **Declined:**
  - **MU/SNDK.** Suspect growth figures, and forward P/Es around 6.8x look like a cyclical
    earnings spike.
  - **SMCI.** FCF yield −29.02%: growth paid for by burning cash.
  - **BE, AXON, DASH, FIX.** The growth is real; trailing multiples of 370x, 178x, 101x
    and 40.8x are the problem.

#### Voice 4 — Defensive / Risk

*Triage (lowest `beta`):* SAAB-B.ST 0.033, ALL 0.150, AZN.ST 0.205, BETS-B.ST 0.216,
JNJ 0.235, CME 0.275, EG 0.277, ABBV 0.281, VRTX 0.320, KO 0.342, NOVO-B.CO 0.344.
*Lowest leverage:* BURE.ST D/E 0.008, TPL 1.077, SNDK 1.277, EVO.ST 2.13.

The scenario I am positioning for: the regime lens calls this **Transitional**, with a
5.18% US 10-year, a 119.51 dollar index and a +1.45% Swedish real policy rate. The risk
is multiple compression, with rates staying high while VIX 14.21 prices no shock.

- **BUY VRTX (Vertex), 7 (pulled in, rank 48).**
  - Why: beta 0.320, net debt/EBITDA −1.15 (net cash), D/E 9.77, net margin 35.0%,
    revenue +12.5% on a 10.4% CAGR, PASS. It is still the only candidate combining net
    cash, D/E under 10, beta under 0.4 and double-digit growth.
  - Risk: concentration in one franchise (cystic fibrosis). No pipeline data exists here.
  - Invalidated by: net debt turning positive.
- **BUY CME, 6.**
  - Why: beta 0.275, net debt/EBITDA 0.33, net margin 63.4%. Exchange volumes rise in a
    shock, so it gains in a crash rather than merely falling less. With VIX at 14.21 that
    protection is cheap to hold.
  - Risk: PEG 4.60 on 0.8% growth. You pay heavily for that protection and it does
    nothing in a calm market.
  - Invalidated by: volumes falling in a quarter when VIX rose. No volume data is fetched.
- **BUY AZN.ST (holding), 6.**
  - Why: beta 0.205 is the lowest of any holding, and it is ballast against a
    53.98%-industrials sleeve.
  - Risk: FCF yield 0.19%, so the defensiveness sits in the revenue line.
  - Invalidated by: a dividend cut (payout 47.4% per thesis-review).
- **BUY MO (Altria), 5.**
  - Why: beta 0.494, 6.45% dividend, 7.86% FCF yield, net debt/EBITDA 1.41.
  - Lower than last sweep's 6: revenue +1.2% on a −0.9% CAGR is a shrinking business you
    are paid to hold.
  - Missing: `roe_pct` and `de_ratio`. `investor_profile.json.constraints.exclusions` is
    empty, so tobacco is not excluded. No ESG data exists.
- **SELL VOLV-B.ST, 4.**
  - Why: D/E 147.35 and net debt/EBITDA 3.8 make it the most leveraged holding in the most
    cyclical end-market, and it was the only holding to fall materially this week (−4.9%).
    This is the risk view; Growth's inflection case may win.
  - Invalidated by: net debt/EBITDA below 2.5.
- **Attacking this sweep's BUY cases:**
  - **VICI.** Net debt/EBITDA 4.82 into a 10-year that moved 4.94 → 5.18%. In my
    scenario, rates and tenant stress hit a leveraged REIT at the same time.
  - **ALL.** It is the second-lowest beta in the set (0.150) and fell 9.9% in a week.
    Beta is a backward-looking statistic, and it did not protect against whatever hit
    underwriting. Low beta is not the same as low risk.
  - **NVDA / APP / MU.** Betas of 2.217 / 2.488 / 2.222; SNDK has no beta at all. Adding
    any of them while the −30% drawdown tolerance is unverified (S26) is the specific
    thing I object to.
  - **CHTR.** D/E 441.58, net debt/EBITDA 4.41, declining revenue. The FAIL is deserved.
  - **Swedish real estate** (CATE.ST 10.85x, DIOS.ST 10.07x, CORE-B.ST 15.52x net
    debt/EBITDA). Not investable on leverage.
- **Explicitly not flagging ABB.ST.** D/E 55.75, net debt/EBITDA 0.46. There is no risk
  case against it, and I will not lend this lens to a sale argued on other grounds.

#### Voice 5 — Contrarian / Risk Taker

*Triage (`pct_52w_range`, low = near the low):* DOM.ST 0, VICI 1, FISV 1, FIS 2, CATE.ST 2,
EIX 2, APP 3, CHTR 3, PEP 3, HD 3, CORE-B.ST 6, CMCSA 7, DIOS.ST 7, AFRY.ST 8, EXE 9,
MKC 11, NOVO-B.CO 15.

- **BUY VICI, 6.**
  - Why the pessimism looks wrong: across 6 runs the company's fetched fields have not
    moved (revenue +5.7%, margin 67.5%, PASS), while the price went 26.51 → 25.77 → 25.65
    → 24.73 → 24.11 → 23.27 (−12.2%). The market is repricing interest rates, not this
    asset.
  - Named honestly: this week's move (10-year +24bp, price −3.5%) is exactly what
    Macro's case predicts. My case is that the yield now pays for waiting, not that a
    re-rating is due.
  - Invalidated by: a dividend cut or a tenant default.
- **BUY PEP (PepsiCo), 6 (pulled in).**
  - Why: now 3% of range (was 10% last sweep; price 133.66 → 128.15), PEG 1.32, 4.6%
    dividend, 4.46% FCF yield, beta 0.361, revenue +6.4%. The de-rating is a narrative
    about snacking demand; the fetched revenue has not turned.
  - Risk: D/E 238.95, net debt/EBITDA 2.25, a leveraged staple.
  - Invalidated by: revenue growth turning negative.
- **BUY APP, 5.**
  - Why: 3% of range for the 6th consecutive run while revenue grows +52.8% at a 77.7%
    operating margin, and the price has barely moved (305.77 → 312.47 since 08-25). The
    drop to the low happened before this system started watching. The metrics since then
    have not deteriorated.
  - Held at 5 because S29 still hides from what level, and when, it fell.
  - Invalidated by: operating margin below 65%.
- **Declined, penalty deserved:**
  - **CHTR.** −11.9% this week, −21.7% since 08-25, P/E 2.94. With D/E 441.58 the equity
    is a thin slice of equity on top of a lot of debt, and revenue is falling. There is
    no specific reason the pessimism is wrong.
  - **ALL.** −9.9% this week, with forward P/E above trailing. The market expects an
    earnings drop and I have no evidence it is wrong.
  - **NOVO-B.CO.** 15% of range and 9.63x, but forward P/E is above trailing and growth
    fell from a 20.4% CAGR to 2.1%. The pessimism is consensus reading a real slowdown.
  - **CORE-B.ST, CATE.ST, DIOS.ST.** Leverage.
- **SELL flags: none.** INVE-A.ST is still the name I would naturally target. I stand down
  a 7th time on the insider record, and hand it to D-b's fallback rather than re-flag it.

#### Voice 6 — Macro / Regime

*Regime (from `macro-regime`):* **TRANSITIONAL**. Last sweep's regime lens was risk-on,
US-anchored; the call moved.
- Real US fed funds ≈ −0.08% (3.63% against CPI 3.71%, both dated **2026-08-01**, 8
  weeks stale).
- 10y−2y spread +0.31 (10y 5.18%, 2y 4.87%, 09-24).
- Dollar index 119.51 (09-18), up from 118.21.
- SEK/USD 9.8628.
- VIX 14.21.
- Riksbank 1.75% against Swedish CPI 0.3%: a +1.45% real rate.
- Crypto Fear & Greed 74.

- **BUY V, 6.** Revenue is a percentage of nominal spending, so 3.71% US CPI is revenue
  here. USD earnings sit on the right side of a strong dollar.
  - Risk: consumer volume falling alongside inflation.
  - Invalidated by: the curve re-inverting.
- **BUY AZN.ST (holding), 6.** The regime lens names quality defensives with real earnings
  as what Transitional rewards, and AZN is the only holding it marks "not wrong-side".
  AZN's USD/GBP revenue mix is **unmeasured** (currency exposure UNKNOWN in `portfolio`).
  - Invalidated by: the regime flipping to clean risk-on (curve steepening with VIX in
    single digits), which would make ballast the lagging asset.
- **BUY TSM, 5.** Long the dollar structurally (USD revenue). Down from 6 because the call
  moved to Transitional, and a 5.18% 10-year punishes long-duration growth multiples.
  - Largest unmeasured exposure: Taiwan. No field prices it.
- **Explicit regime downgrades, stated rather than buried:**
  - **VICI, downgraded on regime grounds alone.** The 10-year rose 4.94 → 5.18% between
    sweeps and the price fell 3.5%. Last sweep's Chairman set the 10-year as the thing
    that would change the call. It moved against the BUY. That is not a sell signal on
    the company. It is evidence that the rate argument is currently winning.
  - **Every new USD purchase carries FX risk.** Buying at 9.86 SEK/USD with a 119.5 dollar
    index means a strengthening SEK (which a +1.45% Swedish real rate should support)
    subtracts directly from any US pick's SEK return. This applies to VICI, NVDA, TSM and
    V equally. It is a sizing consideration, not a veto.
  - **Crypto sleeve.** F&G 74 "Greed" against a strong-dollar backdrop, historically a
    headwind. Sentiment and macro point opposite ways. That supports trimming (D-c), not
    adding.
  - **Swedish industrials** (ATCO 32.6x, ABB 35.6x, ALFA 28.4x). These are expensive
    names in a restrictive local real-rate regime, which reinforces the existing
    WEAKENING/BROKEN statuses.
- **SELL flags: none on macro grounds.**
- **Missing:** no commodity series, so no view on TPL, FANG or EXE. No credit spreads, so
  there is no cross-check on the low VIX.

#### Voice 7 — Copycat / Smart Money

**Coverage first.**
- **US:** SEC EDGAR returned **403** this sweep (thesis-review), so there is **zero US
  insider data**: nothing on APP, NVDA, TSM, MU, SNDK, MA, V, VICI, CHTR, ALL or any other
  US `new` name.
- **Sweden:** Finansinspektionen's register populated 7 issuers (10 transactions each),
  covering the Swedish-listed equity holdings. **Industrivärden (INDU-C.ST, rank 8) was
  not among the issuers reported**, so no read exists on it.
- **Institutions:** `MISSING: institutional ownership not fetched`. There is no 13F or
  activist data anywhere.

This voice can review holdings but contributes nothing to discovery.

- **BUY AZN.ST, 8.**
  - Why: CEO Pascal Soriot bought **60,000 shares at 121.02 GBP** and Chairman Michel
    Demare 2,500 at 121.21 GBP, both on 14/09. Two people, both at real market prices.
    CFO Sarin's lines at a price of 0.00 are award vestings and carry no information.
    No disposals by either buyer since.
  - Risk: it is one well-timed purchase, and insiders sometimes buy into declines that
    keep going.
  - Invalidated by: a Soriot or Demare disposal.
- **BUY INVE-A.ST, 6 (down from 7).**
  - Why: five distinct buyers through 2026, zero disposals. The three most recent are
    CEO Cederholm 1,500 at 395.90 (14/09), Lund 1,000 at 399.13 (09/09) and Elfving 850
    at 411.55 (01/09).
  - Lower because **no new purchase appeared this week**. The streak is intact but not
    extending.
  - Invalidated by: a Cederholm disposal, or two pulls with no buying.
- **BUY ALFA.ST (holding), 5.**
  - Why: CFO Ekström bought 1,000 at 547.49 on 11/09; today's 559.60 is only 2.2% above
    his price. The record over several years is buy-only with zero disposals (per
    thesis-review). The break condition named a disposal and none has occurred.
  - Invalidated by: any insider disposal.
- **Reads that are not calls:**
  - **ABB.ST.** The record since 13/08 is only disposals (Terwiesch 20,000 at 83.46 CHF;
    Meline 2,456 at 82.12; two earlier Terwiesch disposals). The only acquisition,
    04/05, was a routine board-fee allotment. There is nothing new, and the pattern did
    not continue for a 4th pull. **No SELL from this voice.**
  - **SHB-A.ST.** Chairman Boman's 26/08 cluster (>1.8m shares at 145.55–146.24) is now
    ~6% below the price and marked "closely associated", i.e. bought through a related
    entity. One person, one day, and not extending.
  - **VOLV-B.ST.** Thesis-review reported no new Volvo transaction. The last cluster on
    record, carried from the 2026-09-21 memo's FI read and not re-read here, was
    Stjernholm's ~1.25m shares at 359–361 (27/07). Today's 321.20 is ~11% below it.
  - **ATCO-B.ST.** Option-exercise monetisation only; not a signal.
- **SELL flags: none.**

---

### 3b. Chairman's Top 5

#### #1 OPPORTUNITY: ABB.ST — ABB
**CATEGORY:** holding

**RANK HISTORY:** 67 now; 66 (09-21). **0 of 6 runs in the top 10.** Bottom sixth of the
funnel every run.

**VOICES IN FAVOR (of selling):**
- Valuation, 7: forward 36.43 above trailing 35.59 on 14.2% growth.
- Fundamental, 7: FCF yield 0.09%, FCF/revenue ~4.4%.
- Growth, 5: revenue growth being handed back in margin.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: balance sheet sound (D/E 55.75, net debt/EBITDA 0.46), no risk case.
- Copycat: insider selling did not continue for a 4th pull, so nothing new either way.

**STRONGEST CASE FOR:** Valuation's inversion. A business growing revenue 14.2% whose
*forward* multiple sits above its trailing one is being priced for margin compression.
With ~4.4% cash conversion and an independently re-derived BROKEN thesis (thesis-review,
6th sweep of evidence), none of the purchase thesis shows in any number.

**STRONGEST CASE AGAINST:** Defensive's. Nothing here is dangerous. A 3,864.80 SEK
position at +2.0% with a clean balance sheet does not need rescuing.

**KEY DISAGREEMENT:** three voices want it sold on price and earnings quality; two refuse
to lend their evidence to the sale. It is **not** a consensus sell. It stands on valuation
and thesis alone, as it has for six sweeps.

**DATA GAPS:** no EV/EBITDA; trailing-only FCF; P/B suspect (use ~11.7x FX-corrected). A
modest discount only, because the two load-bearing facts (forward above trailing, FCF
conversion) are clean.

**CHAIRMAN CONVICTION:** 7

**WHAT WOULD CHANGE THIS:** operating margin expanding and forward P/E falling below
trailing at the **2026-10-20** print. The sale should come *before* that print, not be
bet on it.

**PORTFOLIO FIT:**
- `portfolio` rates Industrials at 53.98% of the stock sleeve, ACT.
- **Arithmetic this memo adds from portfolio's own figures:** selling ABB and **holding
  the cash** takes Industrials to ~13,969 / 29,173 = **~47.9%**, still ACT.
- Only redeploying into a non-industrial stock clears the line. `portfolio` gives
  **~42%** for ABB → VICI.
- There is no tax event either way; both legs sit inside the ISK.

**FINAL CALL: SELL** — all 4 shares (~3,864.80 SEK), **before 2026-10-20**, and **no
longer conditional on the destination.** The destination is decided in #3 and D-a.

**HORIZON:** Medium

**Sixth sweep.** ABB was 924.60 on 2026-08-25 and is 966.20 today (+4.5%). The delay has
not cost money, and that was never the argument. This is the last sweep this memo carries
the call as a live recommendation. If it has not executed by the 10-20 print, the
2026-10-05 memo re-tests it on the reported numbers from scratch.

#### #2 OPPORTUNITY: AZN.ST — AstraZeneca
**CATEGORY:** holding

**RANK HISTORY:** 62 now; 61 (09-21). **0 of 6 in the top 10.** The funnel under-ranks
it partly because `forward_pe` is MISSING in all 6 runs (S21) and z_value is −1.525.

**VOICES IN FAVOR:**
- Copycat, 8: CEO Soriot 60,000 shares at 121.02 GBP plus Chairman 2,500, both 14/09, at
  real prices.
- Valuation, 6: PEG 1.16, 45% of range.
- Defensive, 6: lowest beta held, 0.205.
- Macro, 6: the only holding the regime lens marks as on the right side of the regime.

**VOICES AGAINST / CAUTIOUS:**
- Fundamental (by silence, not a flag): ROIC 13.1% and FCF yield 0.19% make it a good
  business, not an excellent one.

**STRONGEST CASE FOR:** Copycat's. It is the highest-quality insider signal in the
dataset, and it separates real purchases (121.02/121.21 GBP) from the 0.00-price vestings
in the same pull.

**STRONGEST CASE AGAINST:** 0.19% FCF yield. Revenue +6.4% and a 23.5% operating margin
are not reaching free cash this period, and trailing-only FCF cannot say why.

**KEY DISAGREEMENT:** the insider signal speaks to *price*; the FCF figure speaks to
*business quality*. They answer different questions and I will not merge them. I weight
the insider signal because it is fresh and primary, and cap conviction on the FCF gap.

**DATA GAPS:** no forward multiple on the portfolio's largest individual stock; trailing
FCF only; revenue-currency mix unknown.

**CHAIRMAN CONVICTION:** 7

**WHAT WOULD CHANGE THIS:** a Soriot or Demare disposal, or margin compression at the
**2026-10-30** print.

**PORTFOLIO FIT:**
- **Capital check against this sweep's `portfolio`:** ISK cash is **845.43 SEK**; one
  share costs 1,630.00. Unfundable today.
- After P3, `portfolio` has ~14,046 SEK net arriving. It allocates ~5,611 to gold tranche
  2 and ~8,435 to Avanza Global; one AZN share fits inside the Avanza Global remainder.
- **Against:** AZN is already the largest individual company at 5.77% of total, and
  Healthcare is 39.47% of the stock sleeve (WATCH, >30%). One share breaches no cap, but
  it deepens a WATCH. This is the last AZN share I would add before the sleeve gets a
  different sector.

**FINAL CALL: BUY** — 1 share. **Execution note: no idle capital confirmed (845.43 SEK);
funded by P3 or the next contribution.** Not downgraded for pending funding.

**HORIZON:** Medium

#### #3 OPPORTUNITY: VICI — Vici Properties
**CATEGORY:** new candidate (first surfaced by this funnel 2026-08-25)

**RANK HISTORY:** 10 now; 9 (09-21). **6 of 6 runs in the top 10**, but today is its
lowest rank (8, 8, 9, 9, 9, 10).

**VOICES IN FAVOR:**
- Valuation, 8: 7.86x forward, 7.83% yield, 1% of range, no fetched deterioration.
- Contrarian, 6: 6 runs of unchanged fundamentals while the price fell 12.2%.

**VOICES AGAINST / CAUTIOUS:**
- Macro: an explicit **regime-only** downgrade. The 10-year rose 4.94 → 5.18%, and each
  new USD purchase at 9.86 SEK/USD carries FX risk.
- Defensive: net debt/EBITDA 4.82 into that rate move.

**STRONGEST CASE FOR:** Valuation's. A 7.83% yield at 7.9x forward, with a 67.5% margin
and positive revenue growth, is not a distressed profile.

**STRONGEST CASE AGAINST:** Macro's. It gets stronger this sweep because it is backed by
evidence, not just argued. Last sweep's Chairman named the 10-year as the thing that
would change this call. It moved the wrong way and the price followed. On the one
observable this system itself chose, **the rate argument is winning.**

**KEY DISAGREEMENT:** Valuation says the multiple is wrong; Macro says the multiple is
correctly pricing a 5%+ 10-year and will not fix itself until the rate path does. Not
averaged. It resolves as: own it for income and for the concentration fix, not for a
re-rating. At a lower conviction than last sweep, because the evidence moved.

**DATA GAPS:** no FFO/AFFO/EV/EBITDA/lease coverage; zero US insider data (EDGAR 403);
institutional ownership not fetched; **no VICI earnings date this sweep** (the calendar
fetched holdings only, whereas last sweep's calendar had 10-29 next to the FOMC). Heavy
discount: a REIT underwritten without REIT metrics.

**CHAIRMAN CONVICTION:** 5 (down from 6)

**WHAT WOULD CHANGE THIS:** the 10-year at 5.5% or above with the price still falling
retires the BUY. A dividend cut kills it outright.

**PORTFOLIO FIT:**
- `portfolio` calls it "single highest-leverage diversification move available this
  sweep". Real Estate is 0%, direct US is 0% among individual stocks, and ABB → VICI takes
  Industrials from ACT 53.98% to ~42%, tax-free, with zero new capital.
- The caveat `portfolio` names: true US exposure via Avanza Global look-through is
  unverified and "likely already large".
- At 23.27 USD × 9.8628, ABB's ~3,864.80 SEK buys **~16 shares (~3,672 SEK)**.

**FINAL CALL: BUY** (~16 shares, funded by the ABB proceeds), conviction 5. If you decline
it, hold the ABB proceeds as ISK cash (D-a Option 2), knowing Industrials stays ACT at
~47.9%.

**HORIZON:** Medium

#### #4 OPPORTUNITY: NVDA — Nvidia
**CATEGORY:** watchlist

**RANK HISTORY:** 3 now; 3 (09-21). **6 of 6 in the top 10**, rank 3 every run.

**VOICES IN FAVOR:**
- Growth, 8: +105.9% on a 100% CAGR, forward 14.35 vs trailing 28.49.
- Valuation, 7: PEG 0.47, a forward multiple below the defensive staples'.
- Fundamental, 7: ROIC 59.2%, net cash.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: beta 2.217 against an unverified −30% tolerance (S26).
- Fundamental's own caveat: FCF yield 0.77% against a ~3.5% earnings yield.
- Macro: FX, since buying at 9.86 SEK/USD means SEK strength subtracts from the return.

**STRONGEST CASE FOR:** Growth's. A 106%-growth company at 14.35x forward is the exact
signal the forward-below-trailing test exists to catch, and it is the only top-5-ranked
name with **no suspect flag and no screen penalty.**

**STRONGEST CASE AGAINST:** Fundamental's cash-conversion point. It is sharper than the
beta objection because it is about *this* company's numbers, not portfolio risk. Under a
quarter of reported earnings reached free cash this period, and trailing-only FCF cannot
separate working-capital build from something worse.

**KEY DISAGREEMENT:** three voices see the cheapest growth in the set; Defensive and
Fundamental's caveat say the earnings are neither low-volatility nor yet cash. Not
reconciled. It is a real opportunity with a real unanswered question.

**DATA GAPS:** no revisions, backlog or TAM; no US insider data; institutional ownership
not fetched; FCF trailing-only.

**CHAIRMAN CONVICTION:** 6

**WHAT WOULD CHANGE THIS:** FCF yield moving toward the earnings yield (cash catching up
with earnings) raises it. Forward P/E rising above trailing kills it.

**PORTFOLIO FIT:**
- `portfolio`: Tech is 0% of the sleeve, so it diversifies by sector. The US diversification
  is "smaller benefit than raw delta suggests" because Avanza Global likely already holds
  it heavily (unverified look-through).
- **Capital:** ISK 845.43 SEK against a share at ~2,215 SEK (224.58 × 9.8628). P3's
  proceeds are already allocated to gold tranche 2, Avanza Global and the AZN share. No
  ISK sale is proposed beyond ABB, whose proceeds go to VICI.

**FINAL CALL: HOLD-WATCH** — strong on merit, WATCH on capital and on the unverified
drawdown tolerance. Not on doubt about the business.

**HORIZON:** Medium

*Why NVDA over TSM this sweep (TSM was #4 last sweep):* TSM rose 4.9% to 87% of its range,
and its two headline quality fields are unflagged-implausible for a 4th consecutive sweep
(S24). NVDA's data is clean.

#### #5 OPPORTUNITY: CHTR — Charter Communications
**CATEGORY:** new candidate (discovered by this sweep's funnel)

**RANK HISTORY:** 9 now; 14 (09-21). **1 of 6 in the top 10 (first time).** History 14,
18, 17, 17, 14, 9.

**VOICES IN FAVOR:** none at BUY. Valuation's triage ranks it #1 on z_value (1.836): P/E
2.94, forward 2.70, FCF yield 14.98%.

**VOICES AGAINST / CAUTIOUS:**
- Valuation: cheap for a reason.
- Defensive: D/E 441.58, net debt/EBITDA 4.41, revenue −1.7%.
- Contrarian: declined, no specific reason the pessimism is wrong.

**STRONGEST CASE FOR:** a 14.98% FCF yield means the business generates its market cap in
cash in under seven years, even while shrinking.

**STRONGEST CASE AGAINST:** Defensive's. With net debt at 4.41x EBITDA, the equity is a
thin slice at the bottom of the capital structure. A cash-generative, slowly shrinking
business can still wipe out that slice if refinancing at a 5.18% 10-year costs more than
the business grows.

**KEY DISAGREEMENT:** there is none on the call. The point of this entry is **why it
ranked**. It rose from 14 to 9 by falling 11.9% in one week (−21.7% since 08-25). The
value lens gets more excited as the price falls, and the screen FAIL (D/E) is the
mechanism working as designed. That is worth knowing whenever a `new` name climbs fast.

**DATA GAPS:** no subscriber data, no EV/EBITDA, no US insider data.

**CHAIRMAN CONVICTION:** 6 (in NO ACTION)

**WHAT WOULD CHANGE THIS:** revenue growth turning positive with net debt/EBITDA falling
below 3.5.

**PORTFOLIO FIT:** not reached. A merit-stage NO ACTION.

**FINAL CALL: NO ACTION**

**HORIZON:** Medium

### 3c. Other SELL recommendations on current holdings

You get a direct answer to "should I sell anything" every sweep. Beyond ABB.ST:

- **ATCO-B.ST.** Valuation SELL at 5, **declined.** Fundamental rates it the best business
  held (ROIC 39.7%), and its break condition (ttm revenue negative) has not fired (+9.1%).
  Selling the highest-quality industrial while the lowest-quality one is still unsold is
  the wrong order. **NO ACTION.** It is the next rotation candidate after ABB.
- **VOLV-B.ST.** Defensive SELL at 4, **declined.** The −4.9% week is not a thesis event;
  forward P/E and PEG both *improved*. TOO_EARLY is honest. **NO ACTION**, re-test after
  the 10-23 print.
- **SHB-A.ST.** Growth SELL at 4, **declined.** One share, 154.50 SEK. Retired on
  2026-09-14 as too small to matter; not re-raised.
- **INVE-A.ST.** No voice flags a SELL. **D-b's stated fallback takes effect:** stop
  re-flagging until the NAV figure exists (see §6).
- **ALFA.ST, ethereum, DE000A0S9GB0, Avanza Global, Avanza Auto 3.** No sell flag.
- **BTC0E.AS.** **Partial trim under D-c's default.** This is a sizing action, not a
  thesis sell; see the structural section.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens.

| Dimension | Rating | Detail (verbatim) |
|---|---|---|
| Asset allocation vs targets | **WATCH** | Equity 72.01% vs 80% (-7.99pp); Crypto 10.73% vs 10% (+0.73pp); Gold 2.52% vs 5% (-2.48pp); Cash 11.88% vs 5% (+6.88pp); FI/alt (Auto3 bond sleeve) 2.87% vs 0% (+2.87pp). Cash overweight = unexecuted PayPal conversion (P3) + gold tranche 2 sitting undeployed. |
| Equity sector concentration | **ACT** | Industrials 53.98% of stock sleeve (>45% line); Healthcare 39.47% single-name AZN.ST (WATCH >30% line). |
| Geography (home bias) | **ACT** | Sweden 48.83% (>45%); UK/AZN.ST 39.47% (WATCH). Caveat: only 20.3% of equity sleeve has known look-through. |
| Currency exposure (underlying revenue) | **UNKNOWN** | not computable this snapshot. |
| Single-position | (distinct flag) | Avanza Global 53.09% of total mechanically >15% cap but diversified index fund not single-company risk - flagged distinctly. Largest single company AZN.ST 5.77% - OK. |
| Institution concentration | **ACT** | Avanza 82.65% of total (down marginally from 82.77%, still over 80% cap). |
| Fee drag | **OK** | 187.12 SEK/yr = 0.083% of total, well under 0.4% cap. |
| Wrapper efficiency | **OK (ISK/AF) / WATCH (PayPal)** | No active AF balance (only frozen immaterial Osteuropafond). ISK 186,793.85 SEK comfortably under ~300k allowance. ~14,631 SEK idle in PayPal outside any wrapper, ~4% conversion spread exposure, P3 now 8th-plus consecutive sweep unexecuted. |
| Drawdown-tolerance fit | **WATCH-unverified-not-OK** | S26 still open... Existing backtest -20.62% never tested a -30%-scale shock (window's worst equity drawdown only -19.14%). Prior stress-arithmetic estimate (not a backtest) put 80/10/5/5 mix near -36%, over tolerance. |

**Two measurement inconsistencies inside this scorecard, flagged rather than silently
fixed** (arithmetic from `portfolio`'s own figures; for `meta`):

1. **The denominator changed between sweeps.**
   - Last sweep's allocation percentages were of the *investable base*, which excludes
     the 11,363.76 SEK Handelsbanken tax reserve: Avanza Global 55.84% of investable,
     crypto 11.24%, cash 7.39%.
   - This sweep's are of *total capital*, which includes it.
   - On last sweep's basis, today's figures would be: crypto 24,250.69 / 214,644 =
     **11.30%**, not 10.73%. Cash is ~7.2%, not 11.88%. Equity is ~75.8%, not 72.01%.
   - So `portfolio`'s line that crypto is "down from 11.24% last sweep... mostly
     denominator dilution" is a **change of convention, not a change in exposure.**
     Crypto actually edged up. This matters for D-c.
2. **The geography rating tightened without the number moving.** Sweden was WATCH at
   49.10% last sweep and is ACT at 48.83% today. The WATCH/ACT threshold used for
   geography changed between runs.

**Provisional because of `investor_profile.json` gaps, named:**
- `horizon.primary_goal` is still "nature UNCERTAIN", and `years_until_needed` is a soft
  3–7y.
- `constraints.exclusions` is empty (relevant because MO is a live Defensive pick).
- `risk_tier_framework_proposed.open_items` still leaves the SEK-level tier mapping and
  contribution routing undecided.
- `reference_targets` carries no gold line (85/10/0/5). `portfolio.json.targets`
  (80/10/5/0/5) is the authoritative one; the profile was last updated 2026-07-20.

---

## 5. Headline calls

Each needs a decision this session.

1. **SELL ABB.ST, all 4 shares (~3,864.80 SEK), before the 2026-10-20 print.** Sixth
   sweep, conviction 7. No longer tied to any destination.
2. **BUY ~16 VICI with the ABB proceeds (conviction 5, down from 6), or explicitly
   decline and hold the cash.** Buying clears the Industrials ACT line (53.98% → ~42%).
   Holding the cash does not (~47.9%). The rate evidence moved against VICI this week, so
   decide with that in view.
3. **D-c default: trim ~2,500 SEK of BTC0E.AS at the live broker price.** Proceeds go to
   Avanza Global by default, per your own `profit_recycling_rule`. Do not touch ETH (P1).
4. **Execute P3 (PayPal → SEK → ISK), 8th-plus sweep.** ~14,046 SEK net arrives. It funds
   the AZN share (1,630 SEK), gold tranche 2 (~5,611 SEK, closing the −2.48pp gap) and the
   rest into Avanza Global, and it removes ~14,631 SEK from outside any wrapper.

---

## 6. Open actions vs open decisions

### Open actions (things to go do), by ID

| ID | Status | Action |
|---|---|---|
| **P3** | decided — pending execution | Convert PayPal's 1,177.49 USD + 266.88 EUR at the accepted ~4% spread (~585 SEK), transfer ~14,046 SEK net to the ISK, zero the paypal holdings in `portfolio.json`. |
| **P1** | blocked (on user) | ETH cost basis. Blocks any ETH sale, and the reason ETH is excluded from the D-c trim. |
| **P9** | open | Delete the phantom AZN OPENING row in the Excel Transactions tab. |
| **P10** | open | Confirm one 5,000 SEK deposit or two (2026-08-17 vs 2026-08-22). |
| **S6** | open | Record Investor AB's NAV discount/premium from the Q3 report (**2026-10-07**) in `data/company_profiles/INVE-A.ST.json`. |
| **S26** | open | Run the fixed shock-window backtest (2007–09 or 2020-02/03) with crypto's real drawdown distribution. Its deadline passed this sweep, which is why D-c's default fired. |
| **P6** (residual) | open | ~1,744 SEK of original medium-tier cash still uninvested; carried flags stand. |

The D-series still has no standalone register in `OPEN_ITEMS.md` (S30, unapplied). It is
reconstructed below from P-item text and last sweep's memo.

### Open decisions (forks), by ID

**D-a — where ABB's proceeds go.** 5th sweep at the VICI destination.
- *Option 1 — ~16 VICI.* Clears Industrials ACT (~42%), adds Real Estate and direct US.
  Trade-off: the 10-year moved against it this week; FX risk at 9.86 SEK/USD.
- *Option 2 — hold as ISK cash.* No rate or FX risk. Trade-off: Industrials stays ACT at
  ~47.9%, and cash is already over target.
- *Option 3 — 2 AZN shares instead (~3,260 SEK).* Stays in SEK, and the insiders bought.
  Trade-off: Healthcare becomes ~50% of the sleeve in a single name, which swaps one
  concentration for another.
- **My pick: Option 1.** It is the only option that resolves an ACT rating with the capital
  available. Option 2 is the acceptable fallback if you do not want USD REIT exposure into
  this rate path.

**D-b — Investor A's unmeasurable valuation.** 7th sweep.
- Last sweep's Chairman set the fallback: "If it is not done before the next sweep,
  Option 3 is the honest fallback." It was not done.
- **Applied: Option 3 — hold the 5 shares (2,009.50 SEK), and stop re-flagging until the
  NAV exists.** Single re-entry trigger: a NAV figure recorded from the 2026-10-07 Q3
  report. Until then no voice renders a valuation verdict on INVE-A.ST.
- Trade-off accepted: 0.89% of capital stays unvalued, which frees one voice's attention
  every sweep.

**D-c — crypto sleeve sizing.** 4th sweep; the stated default fires.
- The condition was calendar-based ("if S26 is not run before the next sweep"). S26 has
  not run, and `portfolio` confirms the trigger fires.
- **The size of the overweight differs by convention:**
  - `portfolio`'s total-capital basis: +0.73pp (~1,650 SEK).
  - Last sweep's investable basis: 11.30%, **+1.30pp (~2,786 SEK)**.
  - The BTC0E.AS mark is also stale (2026-08-21) while F&G went from 29 to 74, so the
    true weight is more likely understated than overstated.
- **Applied: Option 1 — trim ~2,500 SEK of BTC0E.AS**, inside `portfolio`'s 1,650–2,500
  range and toward the investable-basis overweight.
- Proceeds go to Avanza Global per `investor_profile.json`'s `profit_recycling_rule`
  ("proceeds from trims or sales in medium/high-risk should default toward the secure
  tier unless the user says otherwise").
- Trade-off: selling part of a 3y+ INTACT holding into rising sentiment. That is why it is
  a trim, not an exit.
- S26 still needs to run. A mechanical trim does not replace testing the tolerance.

---

## 7. Cost of being wrong

| Headline call | If wrong | Realistic SEK downside | Recoverable? |
|---|---|---|---|
| SELL ABB.ST | ABB re-rates on a margin beat at 10-20 | ~970 SEK (25% of 3,864.80, foregone) | Yes. It stays in the universe and can be rebought |
| BUY ~16 VICI | 10-year to 5.5%+ and the REIT de-rates further; SEK strengthens | ~1,100 SEK (30% of ~3,672) plus ~370 SEK per 10% SEK appreciation; offset by ~290 SEK/yr dividend | Yes. Income-producing, no leverage at portfolio level |
| Trim ~2,500 SEK BTC0E.AS | BTC doubles from here | ~2,500 SEK of foregone upside | Yes. It can be rebought inside the ISK, 0% fee, no tax event |
| Not trimming (the alternative) | Crypto halves from a "Greed" reading | ~12,125 SEK on the 24,250 sleeve; ~1,390 SEK on the overweight alone | The overweight part, yes. Whether the sleeve loss fits the −30% budget is what S26 has not tested |
| Execute P3 / BUY 1 AZN.ST | Spread paid; AZN falls 30% | ~585 SEK spread (certain) + ~490 SEK on the AZN share | Spread: no, but it recurs every ~2 months if delayed. AZN: yes |

---

## 8. Timing collisions

From `data/cache/calendar/20260928-events.json`. **Caveats:** `calendar_last_verified`
is 2026-08-03 and US/SE CPI dates are still unverified. The calendar fetched earnings for
**holdings only** this sweep; there are no dates for VICI, NVDA or any other candidate.

- **ABB.ST reports 2026-10-20.** The standing SELL should execute **before** this date.
  If it slips past, it is a 7th sweep and the call becomes a bet on the print.
- **ALFA.ST reports 2026-10-27, the same day as FOMC day 1** (statement 10-28). No trade
  in ALFA is proposed, so this is a read-carefully flag: the print's price reaction will
  mix company news with the rate decision.
- **VICI:** no earnings date this sweep. Last sweep's calendar placed it at 10-29, right
  after the FOMC; unverified this session. If D-a Option 1 is chosen, executing in the
  next days avoids the FOMC window either way.
- **Riksbank minutes 09-30; rate decision 11-04; minutes 11-10.** None of this memo's
  actions depend on them. Sweden's +1.45% real rate is the backdrop for the SEK-FX point
  under Macro.
- **Other holding prints:** SHB-A 10-21, ATCO-B 10-22, VOLV-B **10-23 (the TOO_EARLY
  re-test)**, AZN 10-30. INVE-A.ST returned no date again; that is a data gap, not
  confirmed quiet. Its Q3 report is 10-07 per the prior memo and OPEN_ITEMS.

---

## 9. Data gaps for `meta`

Ordered by what each gap cost this sweep. Surfaced, not fixed.

1. **The scorecard's denominator changed between sweeps without saying so.** Crypto
   11.24% (investable) last sweep versus 10.73% (total) this sweep read as "crypto fell"
   when it rose to 11.30% on a like-for-like basis. This nearly set the size of D-c's
   trim. `data/definitions.json` should pin one allocation denominator. The geography
   threshold also moved (WATCH at 49.10% → ACT at 48.83%).
2. **US insider data: zero coverage (EDGAR 403).** Copycat contributes nothing to
   discovery. Institutional ownership is not fetched anywhere.
3. **S24, 4th sweep:** TSM `roic_pct` 183.7% / `fcf_yield_pct` 31.27% are still unflagged
   and still feed rank 7. New this sweep: ALL `fcf_yield_pct` 26.34% (insurer float) is
   the same class of error, also unflagged.
4. **S29, 6th sweep:** no 52-week endpoints in the candidates CSV. APP (rank 1, 3% of
   range, 6 runs) is again uninterpretable. So is ALL's and CHTR's one-week collapse.
5. **The calendar covered holdings only.** No earnings dates for any candidate, including
   the live VICI BUY. Last sweep's calendar had them.
6. **No EV/EBITDA, FFO or AFFO.** VICI is a Top-5 BUY underwritten without REIT metrics;
   the ABB SELL rests on P/E and FCF.
7. **S6, 7th sweep:** now parked under D-b Option 3 until the 10-07 Q3 report.
8. **S21:** Nordic `forward_pe`/`debt_to_equity` gaps still make up most of the 18
   MISSING rows. AZN.ST has had no forward multiple in any of 6 runs.
9. **No commodity or credit-spread series** (TPL, FANG, EXE unassessable; the low VIX has
   no cross-check). `fed_funds_rate`/`us_cpi_yoy` are 8 weeks stale (2026-08-01).
10. **Process: S27, 6th confirmed occurrence** (see the opening section). Two related
    orchestration defects this sweep:
    - The launch prompt's four lens sections arrived as literal unexpanded `$(cat ...)`
      strings. I read them from the scratchpad files directly; the orchestrator then
      confirmed that route.
    - The launch note said "7 consecutive runs" for the top-10 streaks;
      `candidate_history.csv` holds 6.
    Neither caused a wrong call. Both are the same stored-text-drifts-from-state pattern.

---

## Structural decisions (non-stock)

Levers 1–2 (wrapper, fees) are structurally closed and not re-flagged.

**ACTION:** Execute P3. Convert the PayPal balance (1,177.49 USD + 266.88 EUR) at the
accepted ~4% spread and transfer to the Avanza ISK.
- **POSITION:** 14,630.90 SEK in PayPal, outside any wrapper.
- **TARGET:** ISK. `portfolio` allocates ~5,611 SEK to gold tranche 2 and the remainder
  (~8,435 SEK) to Avanza Global, from which the 1 AZN.ST share (1,630 SEK) is taken.
- **REASON:** recurring fee drag, plus it is the binding constraint on the AZN BUY, the
  gold gap and the cash overweight.
- **THESIS STATUS:** decided by you 2026-08-17 (Option A). Unchanged.
- **WHAT CHANGED:** only the count, now the 8th-plus sweep.
- **BREAK CONDITION:** the disclosed rate turns out materially worse than 4%, or a
  fee-free route appears.
- **CONFIDENCE:** High (arithmetic, not a forecast).
- **HORIZON:** Long

**ACTION:** Trim BTC0E.AS by ~2,500 SEK at the live Avanza price (D-c default).
- **POSITION:** Valour Bitcoin Zero SEK. Carried at 11,031 SEK (stale mark from
  2026-08-21, feed 404).
- **TARGET:** crypto back toward 10% of the investable base. Proceeds go to Avanza Global
  (profit_recycling_rule default).
- **REASON:** S26 missed its own deadline, so the pre-committed default applies. On a
  like-for-like basis crypto is 11.30% against a 10% target, F&G is 74 ("Greed"), and
  Macro reads the strong dollar as a crypto headwind.
- **THESIS STATUS:** INTACT (thesis-review). This is sizing, not a thesis sell.
- **WHAT CHANGED:** the deadline passed.
- **BREAK CONDITION:** S26's shock-window backtest shows the 80/10/5/0/5 mix inside −30%.
  Then the sleeve may drift back to target without further trims.
- **CONFIDENCE:** Medium
- **HORIZON:** Medium
- *Not recorded in the picks ledger:* BTC0E.AS has no fetched price to join, and a partial
  trim scored as a full SELL would misstate performance.

---

## 10. Learning notes

- **A ranking can rise because a stock fell.** CHTR entered the top 10 for the first time
  this sweep, not because anything about the business improved, but because an 11.9% drop
  made every valuation ratio look better. A screen that sorts by cheapness will always
  push recent losers up the list. That is why a fast-climbing `new` name deserves more
  suspicion, not less, until something other than the price explains the move.
- **Pick the observable before the outcome arrives, then honour it.** Last sweep named the
  10-year yield as what would move the VICI call. It went the wrong way (4.94 → 5.18%)
  and the price followed, so conviction drops from 6 to 5. That is not a reaction to a
  bad week. It is the system doing what it said it would, which is the only way a
  "what would change this" line means anything.
- **The same number can mean opposite things depending on its denominator.** Crypto was
  "11.24%" last week and "10.73%" this week, which reads as a fall. On the same base it
  actually rose to 11.30%. Before acting on a drift figure, check it is measured against
  the same total as the one it is compared with.
- **Selling a position and fixing a concentration are not the same trade.** Selling ABB
  alone leaves Industrials at ~47.9%, still above the 45% line. Only putting the money
  into something non-industrial brings it below. That is why the sale's *timing* (before
  10-20) is now separate from its *destination*: the sale's case needs no destination,
  but the concentration fix needs both legs.

---

`journal` **must run next.** An unlogged memo is invisible to the next session and can
never be reconciled, and reconciliation is the only calibration mechanism this system has.
Then run `python scripts/decisions.py record --picks data/picks/2026-09-28-picks.csv`,
followed by `python scripts/decisions.py basis --write`.
