# Council Memo — 2026-10-05

*This memo is a structured synthesis of your own agents' analysis of data fetched this
session. It is not licensed investment advice. Every number in it comes from a file
written today, or is labelled as carried forward, user-relayed, or this memo's own
arithmetic.*

---

## What leads this memo

**1. The BTC0E.AS trim most likely never happened.** Three files say it did. They are
wrong. Treat the position as 150 units until you say otherwise.

- `OPEN_ITEMS.md`'s emphasis paragraph says "a ~2,500 SEK crypto trim executed
  mechanically". S26's 2026-09-28 review says the same. This sweep's launch note
  repeated it.
- The source of that claim, the 2026-09-28 memo, wrote "**Applied:** Option 1 — trim
  ~2,500 SEK". That memo also listed the trim as headline call #3, a call that "needs a
  decision this session". The Council *applied its own default as a recommendation*.
  This system never executes a trade (CLAUDE.md).
- The 2026-09-28 SESSION_LOG entry says "User decisions: none — automated/scheduled
  sweep".
- `portfolio.json` was last updated 2026-09-02 and holds 150 units, 61.37 SEK cost and
  11,031 SEK value.
- So the file of record is consistent with every other piece of evidence. The
  "executed" wording is the error. Somewhere between memo and backlog, "the Council
  decided" became "it happened". This is an S27-type drift (stored text claiming a fact
  that live files contradict), and this time it is *inside* the repository.

Consequences:

- **D-c is still open.** It was never resolved.
- S26's "precedent of a capital action executing on a default" did not occur. No capital
  moved.
- This sweep's crypto weight (10.95% of total capital, 11.53% of the investable base) is
  computed on the right quantity. It is still a stale *mark*: BTC is carried at the
  2026-08-21 broker price.

**What I need from you (one line):** "trim not done", or "trimmed N units at X SEK" so
`portfolio.json` can be corrected. §6 sets out the D-c decision.

**2. This is ABB.ST's deadline sweep.** Last sweep committed to re-test the SELL from
scratch rather than carry it a seventh time. That re-test is in #1 below. **Result: SELL
survives, conviction falls 7 → 6.** Two of last sweep's three load-bearing facts turned
out weaker than stated. The thesis-review's new PEG signal does not survive contact with
the data.

**3. A unit error was quietly shaping two holdings' cases.**
- `fcf_yield_pct` for **ABB.ST and AZN.ST** divides USD free cash flow by a SEK market
  cap. Both companies report in USD and are priced in SEK.
- AZN.ST's real free-cash-flow yield is **~2.0%, not 0.20%**: 4.905B USD × 9.9047 =
  48.6B SEK, divided by 2,441B SEK.
- ABB.ST's is **~0.87%, not 0.09%**: 1.5705B × 9.9047 = 15.6B SEK, divided by 1,792B SEK.
- Last sweep's "strongest case against" AZN was the 0.19% figure. It was an artifact.
- The same mismatch plausibly explains TSM's never-flagged 29.8% FCF yield (TWD cash
  flow over a USD market cap). That is a hypothesis for `meta` (§9), not verified here.

**4. Two days from now (2026-10-07):** Investor AB *and* Industrivärden both report Q3.
That report is D-b's single re-entry trigger (S6). Recording one NAV figure per company
closes a gap that has cost a voice its call for eight sweeps.

**Settled facts in this sweep's launch premises, not re-litigated:**
- The Handelsbanken wrapper was closed 2026-07-07/08-03.
- `reference_targets` is not null; 80/10/5/0/5 is in `portfolio.json`.

This sweep's launch note named both stale premises itself and asked that they not shape
the opening, and they don't. The occurrence count is in §9.

---

## 1. Position report

`scripts/position_report.py` output was not supplied to the `council` subagent (it has no
shell), so it reconstructed the table by hand from the snapshot and `portfolio.json`,
flagged for `meta` as a process gap (§9: pass the script's file path to `council`, same
fix S27 already recommends for lens outputs). The orchestrating session ran the script
directly afterward — this is the actual mechanical output, not a reconstruction, and it
matches the hand-rebuilt figures exactly:

```
Position report — 2026-10-05
Snapshot: 20261005T061958.json · previous: 20260928T062025.json

Position                                                    Price      Δ vs prev   Δ vs cost   52w range   Value (SEK)   Source
Handelsbanken A (stock)                                     152.00     -1.6%       +17.6%      86%         152.00        fetched
Investor A (stock)                                          393.40     -2.1%       +35.6%      79%         1,967.00      fetched
Volvo B                                                      318.40     -0.9%       -13.4%      57%         4,139.20      fetched
Atlas Copco B                                                177.50     +0.7%       -2.1%       85%         4,792.50      fetched
AstraZeneca                                                  1,599.00   -1.9%       +4.0%       29%         12,792.00     fetched
Xetra-Gold (physically-backed gold ETC, ISIN DE000A0S9GB0)   no data    no data     no data     -           5,689.22      FETCH FAILED
Alfa Laval                                                   550.40     -1.6%       -4.2%       75%         4,953.60      fetched
ABB                                                           961.40     -0.5%       +1.5%       77%         3,845.60      fetched
Avanza Auto 3 (fund)                                         no data    no data     +65.2%      -           16,191.00     book value
Avanza Global (fund)                                         no data    no data     +0.0%       -           119,999.00    book value
Valour Bitcoin Zero SEK (certificate, ISIN CH0585378661)     no data    no data     no data     -           11,031.00     FETCH FAILED
ETH (self-custody wallet)                                    27,385.60  +4.0%       no data     -           13,743.46     fetched (CoinGecko, converted via sek_per_eur)

Crypto context (spot, from CoinGecko):
ethereum: 2,425.35 EUR, Δ vs prev +4.1%, 7d +1.8%, 30d +10.5%, vs ATH -42.7%.
Bitcoin is the agreed directional proxy for the XBT certificate, which has no working
ticker. It indicates direction, not the certificate's actual price — that comes from the
user.
```

**What moved.** Little.
- **Every Swedish holding except Atlas Copco drifted down 0.5–2.1%.** No fetched
  fundamental moved with them, so this is not a thesis event for any of them.
- **AZN.ST −1.9%** is now 29% of its range, cheaper still. The thesis is INTACT
  (thesis-review).
- **ETH +4.0%** is the only material move. It pushes the crypto sleeve further above
  target; see D-c.
- **Volvo** is −13.4% vs cost. This is still TOO_EARLY, not broken. The 10-23 print is
  the test.
- **Not priced:** 16,720 SEK has no live price (gold, BTC). The index funds are at book
  value, so there is nothing to read.

---

## 2. Scout health

```
Universe    624
Fetched     621  (cache 0, new 625, failed 4)
Ranked      613
Candidates  74   (holdings 9, watchlist 30, new 35)
Focus       23
Screened    74
Passed      38
Missing     17
Failed      19
Status      VALID
```

**Reading:** VALID, so nothing upstream needs distrusting before §3. Two corrections to
how this run was described.

**"New" is not "first seen".** `source=new` means "not held, not watchlisted". 35 rows
carry it, but only **5 names are in the candidate set for the first time this run**:
CTVA, GPN, PLTR, EOG and TEL2-B.ST. Five left: VRTX, SMCI, SYF, BURE.ST and FIX. VRTX
was last sweep's top Defensive pick and can no longer be picked or tracked here.
Discovery is producing at the margin, not at the head.

**The head of the funnel is frozen.** Checked against `candidate_history.csv`:
- APP, SNDK, NVDA, MA, V, TSM, INDU-C.ST and **VICI** have been top-10 in **all 7 runs**
  (2026-08-25 to today).
- **MU** has been top-10 in every run since it was first seen (08-31), which is **6, not
  7**.
- The launch note's list swapped VICI for MU and over-counted MU.

**Suspect values withheld from lens scoring** (the CSV `suspect` column):
- ABB.ST `price_to_book` 113.06
- INDU-C.ST `revenue_growth` 1,197.9% (holding-company investment gains counted as
  revenue)
- SNDK `revenue_growth` 371.6%
- MU `revenue_growth` 379.3%
- CMCSA `peg` 142.98
- ASML `price_to_book` 1,621.97 and `roic` 4.05
- KINV-B.ST `price_to_sales` −2.17
- FANG `peg` 20.47

**Still unflagged:**
- TSM `roic_pct` 183.7% and `fcf_yield_pct` 29.8%, a **5th sweep** (S24).
- ALL `fcf_yield_pct` 26.79%, a 2nd sweep.
- ABB.ST and AZN.ST `fcf_yield_pct`, which are unit-mismatched (see the opening). These
  are a new member of the same family, never flagged.

The 17 MISSING rows are again mostly Nordic names lacking `forward_pe` or
`debt_to_equity` (S21). AZN.ST has had no forward multiple in any of the 7 runs.

---

## 3. Top opportunities

### 3a. The seven voices (independent passes)

Each voice ran its own numeric triage over all 74 rows, then drafted without reading the
others. Where a voice pulls in a name outside `focus=Y`, or argues against a name's
screen flag, it says so.

#### Voice 1 — Fundamental / Quality

*Triage (`z_quality`):* APP 2.570, SNDK 2.532, MU 2.524, NVDA 2.503, MA 2.223, V 1.924,
TSM 1.908, INDU-C.ST 1.900, INVE-A.ST 1.820, TPL 1.818, MO 1.787, LLY 1.719.

- **BUY V, 8.**
  - Why: ROIC 41.5%, ROE 61.2%, net margin 50.8%, operating margin 66.1%, net
    debt/EBITDA 0.32, FCF yield 3.01%, revenue +14.4% on a 10.9% 3-year CAGR. The
    numbers are identical to last sweep and the price is 2.2% lower (367.98 → 359.85).
    Same business, cheaper. Moat reasoning (the two-sided network) is qualitative.
  - Risk: interchange-fee regulation.
  - Invalidated by: ROIC below 30%, or growth in mid-single digits for two prints. First
    test is the 10-27 print.
- **BUY NVDA, 7.**
  - Why: ROIC 59.2%, ROE 117.2%, margins 63.7/66.2, net debt/EBITDA −0.12 (net cash).
  - Held at 7 for the same reason as last sweep. FCF yield is 0.74% (USD over USD, so
    genuine) against an earnings yield of ~3.4% (1/29.58). About a fifth of reported
    earnings reached free cash.
  - Invalidated by: FCF yield still below 1% after the 11-17 print.
- **BUY MA, 7 (pulled back in against its FAIL).**
  - Why the FAIL misleads: D/E 439.58 is negative equity created by buybacks. Net
    debt/EBITDA is 0.59.
  - Underneath: ROIC 56.1%, margins 46.3/61.1, revenue +14.1% on a 13.8% CAGR.
  - Risk: the same as V, with no book-equity cushion.
  - Invalidated by: net debt/EBITDA above 2.0.
- **BUY ATCO-B.ST (holding), 6.**
  - Why: the best business held. ROIC 39.7%, ROE 25.7%, operating margin 20.6%, net
    debt/EBITDA 0.50, and FCF/revenue **15.3%** (25.97B / 169.92B, both SEK, so clean).
    This is a business verdict; the price is Valuation's objection.
  - Invalidated by: ttm revenue growth turning negative at the 10-22 print.
- **BUY TSM, 5 (down from 6).**
  - I discard `roic_pct` 183.7% and `fcf_yield_pct` 29.8%. My new suspicion is that both
    are currency-unit errors (TWD figures over a USD market cap), the same shape as
    ABB/AZN.
  - The case rests on ROE 40.0%, net margin 49.9%, operating margin 60.3% and net
    debt/EBITDA −0.77.
  - Lower because five sweeps of the headline quality fields being unusable is itself a
    data-confidence cost.
  - Invalidated by: operating margin below 45% at the 10-15 print.
- **BUY AZN.ST (holding), 5 (new from this voice).**
  - Why: corrected for the unit error, FCF/revenue is **8.0%** (4.905B / 61.37B, both
    USD) and FCF yield ~2.0%. Gross margin 81.7%, operating 23.5%, revenue up every
    fiscal year 2022–2025 (44.4 → 45.8 → 54.1 → 58.7B) with ttm at 61.4B.
  - Only 5: ROIC 13.1% (estimated) is good, not excellent.
  - Invalidated by: operating margin below 20% at the 10-30 print.
- **SELL ABB.ST, 6 (down from 7).**
  - Why: FCF/revenue is **4.4%** (1.5705B / 35.752B, both USD, valid). That is the
    thinnest cash conversion held, against Atlas Copco's 15.3%.
  - Last sweep I quoted an FCF yield of 0.09%. That was the unit artifact. The real
    figure is ~0.87%. Still the lowest held, but I overstated it by about ten times, and
    conviction comes down for that.
  - Invalidated by: FCF/revenue above ~8% in the next annual report.
- **Declined:**
  - **APP.** ROE 203.7% sits on D/E 111.13, and the price is making new lows (−10.0% this
    week, still 3% of range). I cannot grade quality the market is visibly re-pricing
    without knowing why.
  - **MU/SNDK.** Operating margins of 80.7/78.5% look like a peak memory-cycle reading.
    Both revenue-growth figures are suspect-flagged.
  - **INVE-A.ST/INDU-C.ST.** Holding-company fields (S6).

#### Voice 2 — Valuation

*Triage (`z_value`):* CHTR 1.842, CMCSA 1.814, FIS 1.803, ALL 1.784, CTVA 1.707,
FISV 1.668, EG 1.656, CORE-B.ST 1.571, DOM.ST 1.494, MEKO.ST 1.419, INDU-C.ST 1.308,
GPN 1.287, DIOS.ST 1.271, INVE-A.ST 1.169, EXE 1.116, EIX 1.069, VICI 0.793.

*Named gap: no EV/EBITDA or EV/EBIT. Where I approximate from net debt/EBITDA, I say so.*

- **BUY VICI, 8.**
  - Why: 8.81x trailing, 7.58x forward, 8.12% dividend, 67.5% net margin, revenue +5.7%
    on a 15.5% CAGR, 2% of range, PASS. It is cheaper again (23.27 → 22.73) and no
    fetched field got worse.
  - Approximation: net debt/EBITDA 4.82 is heavy leverage. I quote no enterprise
    multiple.
  - Risk: the discount rate (the 10-year at 5.24%) and refinancing cost.
  - Invalidated by: a dividend cut, or net debt/EBITDA above 6.
  - Missing: FFO, AFFO and lease coverage, the metrics REITs are actually priced on.
- **BUY AZN.ST (holding), 7 (up from 6).**
  - Why: PEG 1.1 (from 1.16), 29% of range (from 45%), price −1.9%.
  - FX-corrected price/sales is ~4.0x (39.78 / 9.9047) and FCF yield ~2.0%. The raw
    39.8x and 0.20% are the unit error. Background, labelled: large-cap pharma typically
    trades 15–20x trailing, so 25.1x is a premium only before adjusting for growth.
  - Invalidated by: PEG above 1.6.
  - Missing: `forward_pe` (all 7 runs).
- **BUY NVDA, 7.**
  - Why: forward 14.91x against trailing 29.58x on 105.9% growth.
  - The PEG went from 0.47 to 0.29 with no earnings event (NVDA reports 11-17). I do not
    lean on that move; see Growth's caveat below. The forward/trailing gap alone carries
    the case.
  - Invalidated by: forward P/E rising above trailing.
- **BUY TSM, 5.**
  - Why: PEG 0.90, forward 21.56x against trailing 34.36x, net cash.
  - Down from 6: the price rose again (451.15 → 459.20) to 91% of its range.
- **SELL ABB.ST, 6 (down from 7).**
  - What changed against my own case: last sweep's **load-bearing fact has flipped**.
    Forward P/E 37.59 is now *below* trailing 38.46. Last sweep it was above (36.43 vs
    35.59). The gap is only 2.3%, which means the market expects next-year EPS
    essentially flat on 14.2% revenue growth. The "inversion" I sold on is gone, so I
    lower conviction.
  - What did not change: ABB is still the richest multiple held, with no margin of safety
    on any read. P/B 113 is suspect; the FX-corrected figure is ~11.7x.
- **SELL ATCO-B.ST, 5.**
  - Why: 33.1x trailing, PEG 2.21, 85% of range.
  - Invalidated by: PEG below 1.5.
- **Cheap for a reason, not picks:**
  - **CHTR.** −5.3% this week, roughly −26% since 08-25. D/E 441.58, revenue −1.7%.
  - **CMCSA.** Revenue −1.2%; the PEG is an artifact.
  - **FIS.** −5.4% this week. Revenue +29.1% against a −9.8% CAGR, net debt/EBITDA 5.82.
  - **CTVA.** New this run. Margins read 0.0/0.0, so the data is broken.
  - **GPN.** New. Negative margin.
  - **CORE-B.ST, DOM.ST, MEKO.ST.** No data says the discount is wrong.
  - **MKC.** A trailing 7.4x looks like an anomaly.
  - **ALL.** Dropped from last sweep's 5. Forward 8.05 vs trailing 4.48 still implies an
    earnings drop, and nothing new resolves it.
  - **APP.** PEG 0.58 and forward 12.8x look cheap. A −10% week with no fetched cause
    says the price is pricing something the file doesn't contain. Not until the 11-04
    print.

#### Voice 3 — Growth / Opportunity

*Triage (`z_growth`):* NVDA 1.909, BE 1.774, AVGO 1.754, PLTR 1.740, APO 1.727,
AXON 1.545, MU 1.484, DASH 1.475, GPN 1.468, FANG 1.436, LLY 1.430, APP 1.400.

*Forward P/E below trailing:* SNDK 6.53/23.32, MU 5.22/14.46, TPL 4.65/43.39, GPN
4.90/36.80, NVDA 14.91/29.58, APP 12.78/20.62, AVGO 18.31/45.36, APO 10.66/40.87,
LLY 24.01/38.36, VOLV-B.ST 12.64/17.86.

*Named gaps: no TAM, revisions or market-share data.* One caveat on the PEG field
specifically: it moved sharply this week on names with no report. NVDA went 0.47 → 0.29
and ABB 2.11 → 1.33. PEG embeds an analyst long-term growth estimate this system cannot
see or verify, so I rank on measured growth and the forward/trailing gap, not on PEG
moves.

- **BUY NVDA, 8.**
  - Why: revenue +105.9% on a 100.0% CAGR, forward at half of trailing, clean data.
  - Risk: a two-quarter pause in hyperscaler capex (qualitative; no backlog data).
  - Invalidated by: growth below 40%, or forward P/E above trailing.
- **BUY LLY, 6 (pulled in, rank 22).**
  - Why: revenue +47.7% on a 31.7% CAGR, operating margin 54.2%, ROIC 38.4%, forward
    24.0x vs 38.4x. The price is −2.7% this week.
  - Risk: D/E 162.07, and dependence on one drug class (qualitative).
  - Invalidated by: ttm growth below 25%.
- **BUY APP, 5.**
  - Why: +52.8% revenue at a 77.7% operating margin, forward 12.8x vs 20.6x.
  - Held at 5: the price fell 10.0% this week to fresh lows (still 3% of range). The
    market is betting growth breaks. The file shows no sign of it, but has no revisions
    data to say who is right.
  - Invalidated by: the 11-04 print showing growth below 25%.
- **BUY AVGO, 5 (pulled in against a FAIL on trailing 45.36).**
  - Why: forward 18.31x on +85.5% revenue (24.4% CAGR), 26% of range.
  - Held: 85.5% on a 24.4% CAGR is likely an acquisition base effect.
  - Invalidated by: forward P/E drifting toward trailing.
- **BUY VOLV-B.ST (holding), 5.**
  - Why: forward 12.64 < trailing 17.86, PEG 0.92 (from 1.49 at purchase), ttm revenue
    +2.7% after a two-year decline. Thin: the 3-year CAGR is +0.4%.
  - The test is the **10-23 print**.
- **SELL SHB-A.ST, 4.** Revenue −3.8%, z_growth −1.274 (worst held), forward 13.40 above
  trailing 12.81. Immaterial at one share.
- **SELL ABB.ST, 4 (down from 5).**
  - A 14.2% revenue grower whose forward multiple implies roughly flat next-year EPS is
    giving the growth back in margin.
  - The PEG 1.33 implies ~29% long-term EPS growth. The two analyst-derived fields
    contradict each other, so I trust neither strongly.
- **Declined:**
  - **MU/SNDK.** Suspect growth flags; single-digit forward P/Es look like cyclical-peak
    earnings.
  - **PLTR** (new, 162.7x), **BE**, **AXON**, **DASH.** The growth is real; the
    multiples are the problem.
  - **GPN** (new). 68.6% growth on a 4.8% CAGR with a negative margin looks like an
    acquisition.
  - **TPL.** Forward 4.65 vs trailing 43.39 is implausible.
  - **APO.** The forward/trailing gap cannot be reconciled from the data.

#### Voice 4 — Defensive / Risk

*Triage (lowest `beta`):* SAAB-B.ST 0.033, ALL 0.150, AZN.ST 0.205, BETS-B.ST 0.216,
JNJ 0.235, EOG 0.272, CME 0.275, EG 0.277, ABBV 0.281, EXE 0.323, TEL2-B.ST 0.324,
KO 0.342, NOVO-B.CO 0.344. *Lowest leverage:* TPL D/E 1.077, SNDK 1.277, EVO.ST 2.13,
PLTR 2.139.

**The scenario I position for:** the regime lens calls this TRANSITIONAL.
- The 10-year is at 5.24% (up from 5.18%), DXY at 120.33 and US CPI at 3.71%.
- Sweden's real policy rate is +1.45pp.
- VIX at 16.39 is not pricing a shock.

My worry is multiple compression in long-duration names, plus stress on leveraged Swedish
cyclicals. VRTX, last sweep's top pick here, has left the candidate set and cannot be
re-picked; I note the loss rather than substitute for it silently.

- **BUY AZN.ST (holding), 7 (up from 6).**
  - Why: beta 0.205, net debt/EBITDA 1.38, operating margin 23.5%, revenue up four fiscal
    years running. The unit correction removes last sweep's caveat that its
    defensiveness "sits in revenue, not cash": FCF/revenue is 8.0%.
  - Invalidated by: a dividend cut (payout 46.95%).
- **BUY CME, 6.**
  - Why: beta 0.275, net debt/EBITDA 0.33, net margin 63.4%. Exchange volumes typically
    rise in shocks; that is qualitative, since no volume data is fetched.
  - Cost: PEG 4.58 on 0.8% growth.
  - Invalidated by: a quarter where VIX rose and revenue didn't.
- **BUY EOG, 5 (new to the candidate set this run; pulled in, rank 51).**
  - Why: beta 0.272, net debt/EBITDA 0.23, D/E 25.9, net margin 25.7%, FCF yield 6.04%,
    forward 9.2x. If the downside is an inflation/rates shock (CPI 3.71%, 10-year 5.24%)
    rather than a demand collapse, a low-leverage producer's cash flow is what holds up.
  - Risk: **no commodity-price data is fetched**, so the main driver is invisible. The
    +58.7% ttm against a −4.2% CAGR shows how cyclical it is, and it sits at 76% of
    range.
  - Invalidated by: revenue growth turning negative while net debt rises.
- **BUY MO, 4 (down from 5).**
  - Why: beta 0.494, 6.59% dividend, 8.03% FCF yield, net debt/EBITDA 1.41.
  - A shrinking business (+1.2% on a −0.9% CAGR). `de_ratio` and `roe_pct` are MISSING.
    `constraints.exclusions` is empty, so tobacco is not excluded.
- **SELL VOLV-B.ST, 4.**
  - Why: D/E 147.35 and net debt/EBITDA 3.8 make it the most leveraged holding, in a
    market with a +1.45pp real policy rate.
  - Invalidated by: net debt/EBITDA below 2.5.
- **Attacking this sweep's BUY cases:**
  - **NVDA / APP / MU.** Betas 2.217 / 2.488 / 2.222 against a −30% tolerance no
    traceable file has tested (S26). APP fell 10.0% in one week. That is what beta 2.5
    looks like.
  - **VICI.** Net debt/EBITDA 4.82 while the 10-year rose again.
  - **CHTR.** D/E 441.58. The FAIL is deserved.
  - **Swedish real estate** (CATE.ST 10.85x, DIOS.ST 10.07x, CORE-B.ST 15.52x net
    debt/EBITDA). Not investable on leverage.
  - **TEL2-B.ST** (new). Beta 0.324, but forward P/E more than doubles from trailing
    (11.1 → 24.3) and net debt/EBITDA is 2.25.
- **Not flagging ABB.ST.** D/E 55.75 and net debt/EBITDA 0.46. There is no risk case,
  and I will not lend this lens to a sale argued on other grounds.

#### Voice 5 — Contrarian / Risk Taker

*Triage (`pct_52w_range`):* CORE-B.ST 0, DOM.ST 0, CTVA 1, PEP 1, VICI 2, DIOS.ST 2,
CHTR 2, FISV 2, APP 3, FIS 3, CATE.ST 3, MKC 3, CMCSA 4, HD 4, EXE 6, EIX 9, MEKO.ST 13,
NOVO-B.CO 14.

- **BUY VICI, 6.**
  - Why the pessimism looks wrong: over 7 runs the fetched fundamentals have not moved
    (revenue +5.7%, margin 67.5%, PASS). The price went 26.51 → 22.73 (−14.3%) as the
    10-year rose. The market is repricing the discount rate, not the asset.
  - Honest about the record: the call has been wrong on price for seven weeks. The 8.12%
    yield is what pays for being early. I am not predicting a re-rating.
  - Invalidated by: a dividend cut or a tenant default. The 10-28 print is the first
    test.
- **BUY PEP, 6.**
  - Why: now 1% of range (128.15 → 125.60). Revenue +6.4%, PEG 1.29, 4.7% dividend,
    4.55% FCF yield, beta 0.361. The de-rating is a narrative about snacking demand; the
    revenue line hasn't turned.
  - Risk: D/E 238.95, net debt/EBITDA 2.25.
  - Invalidated by: revenue growth turning negative.
- **BUY APP, 4 (down from 5).**
  - The most interesting name here, not the most supportable. A 77.7%-operating-margin
    business growing 52.8% at 12.8x forward is priced for a collapse the reported
    numbers don't show.
  - But −10.0% this week to *fresh* lows means someone is selling on information this
    file lacks. S29 still hides the 52-week endpoints.
  - Invalidated by: growth below 25% at 11-04.
- **SELL flags: none.** INVE-A.ST stays parked under D-b until the 10-07 NAV.
- **Declined (penalty deserved):**
  - **CHTR** and **FIS.** Both still falling, with leverage and no specific error in the
    pessimism.
  - **CORE-B.ST, DOM.ST.** At 0% of range the fundamentals agree with the price.
  - **CTVA.** Broken data.
  - **NOVO-B.CO.** Growth fell from a 20.4% CAGR to 2.1%; consensus is reading a real
    slowdown.

#### Voice 6 — Macro / Regime

*Regime (from `macro-regime`): TRANSITIONAL, split by asset class.*
- **US:** real fed funds ≈ +0.04pp (3.75% vs CPI 3.71%; the CPI print is dated
  2026-08-01). 10y−2y +0.46 (5.24/4.78). VIX 16.39. That is calm.
- **Dollar:** DXY 120.33, very strong. A headwind for crypto and FX-sensitive assets.
- **Sweden:** Riksbank 1.75% against CPI 0.3%, a **+1.45pp real rate**, which is
  restrictive.
- **FX and sentiment:** SEK/USD 9.9047 (dated 09-25). Crypto Fear & Greed 70 ("Greed").

- **BUY AZN.ST (holding), 6.** The only holding the regime lens marks on the right side:
  low-duration, defensive, real earnings. Revenue-currency mix is unmeasured.
- **BUY V, 6.** Revenue is a share of nominal spending, so 3.71% CPI is revenue. USD
  earnings.
  - Invalidated by: the curve re-inverting.
- **BUY CME, 5.** Rate volatility drives rate-futures activity (qualitative). A low-beta
  US earner in a high-nominal-rate regime.
- **Explicit regime downgrades, stated rather than buried:**
  - **VICI, downgraded on regime grounds alone.** The 10-year rose again, 5.18 → 5.24%,
    and the price fell again (−2.3%). Last sweep's retirement trigger (10-year ≥ 5.5%
    with the price still falling) has **not** been hit, so this is pressure, not
    retirement.
  - **NVDA, APP, LLY.** Long-duration growth at a 5.24% 10-year. The business is fine;
    the discount rate is the headwind.
  - **Every USD purchase.** It is bought at 9.90 SEK/USD with DXY at 120. A strengthening
    SEK, which a +1.45pp real rate should support, subtracts directly.
  - **Crypto.** F&G 70 against DXY 120.33: sentiment and macro point opposite ways. That
    supports D-c's trim.
  - **Swedish industrials** (ABB 38.5x, ATCO 33.1x, ALFA 28.3x). Expensive in a
    restrictive local regime.
  - **EOG/FANG/EXE.** Not assessable: no commodity series.
- **SELL flags on macro grounds alone: none.**

#### Voice 7 — Copycat / Smart Money

**Coverage first.**
- **US:** SEC EDGAR returned 403 again (CIK mapping), so there is **zero US insider
  data**. Nothing on APP, NVDA, V, MA, VICI or any US `new` name.
- **Sweden:** Finansinspektionen covered 7 issuers.
  - **No transaction published after 17/09 anywhere.** Everything below is three or more
    weeks old.
  - Industrivärden was not pulled.
  - **The "Volvo" pull mixes in Volvo Car AB**, a different company: Nota 63,000 at
    19.60, Severinson, and Samuelsson at 19.295. Those rows are discarded. Only AB Volvo
    rows are read.
- **Institutions:** `MISSING: institutional ownership not fetched`. No 13F or activist
  data exists.

This voice reviews holdings and contributes nothing to discovery.

- **BUY AZN.ST, 7 (down from 8).**
  - Why: CEO Soriot bought 60,000 at 121.02 GBP and Chairman Demare 2,500 at 121.21 GBP,
    both on 14/09, at real prices. CFO Sarin's 0.00-price lines are vestings and say
    nothing. There have been no disposals since.
  - Lower because the signal is three weeks old and has not extended. GBP/SEK is not
    fetched, so I cannot say where today's 1,599 SEK sits against their price.
  - Invalidated by: a Soriot or Demare disposal.
- **BUY INVE-A.ST, 6.**
  - Why: the three most recent buys sit **above** today's 393.40: Cederholm 1,500 at
    395.90 (14/09), Lund 1,000 at 399.13 (09/09), Elfving 850 at 411.55 (01/09). Six
    distinct 2026 buyers, zero disposals in the pull. Insiders are underwater on recent
    buys and have not sold.
  - Invalidated by: a Cederholm disposal.
- **BUY ALFA.ST, 5.**
  - Why: CFO Ekström bought 1,000 at 547.49 (11/09); today's 550.40 is +0.5% above. Nine
    acquisitions, zero disposals back to 2023 in the pull.
  - Invalidated by: any insider disposal.
- **Reads that are not calls:**
  - **ABB.ST.** Disposals only (Terwiesch 18,799, 10,000 and 20,000 between 29/07 and
    13/08; Meline 2,456). Nothing since 13/08. The May "acquisitions" are six board
    members at an identical 78.42 CHF on one date, i.e. fee allotments, not conviction.
    **No SELL from this voice.**
  - **SHB-A.ST.** Chairman Boman's 26/08 cluster is ≥1.85m shares at 145.55–146.24
    through a closely associated entity. The price is now ~4% above it. One person, one
    day.
  - **VOLV-B.ST.** Stjernholm's 27/07 cluster totals exactly 1,300,000 shares at
    ~359–361 (closely associated). Today's 318.40 is ~11.7% below it. The insider is
    underwater and has not sold; that is consistent with the recovery thesis, not proof
    of it.
  - **ATCO-B.ST.** Option exercises paired with same-day internal disposals: compensation
    being cashed out, not a signal.
- **SELL flags: none.**

---

### 3b. Chairman's Top 5

#### #1 OPPORTUNITY: ABB.ST — ABB (the fresh re-test)

**CATEGORY:** holding

**RANK HISTORY:** 66 now; 67 (09-28). **0 of 7 runs in the top 10.**

**VOICES IN FAVOR (of selling):**
- Fundamental, 6: FCF/revenue 4.4%, the thinnest held.
- Valuation, 6: the richest multiple held, no margin of safety.
- Growth, 4: forward EPS implied roughly flat on 14.2% revenue growth.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: D/E 55.75, net debt/EBITDA 0.46, no risk case.
- Copycat: no insider selling since 13/08.
- Thesis-review's new data point: the PEG improved 2.11 → 1.33.

**STRONGEST CASE FOR (selling):** thesis-review's, and it is the one no earnings print
can change.
- The stated reason for owning ABB, "Swedish industrial champion", is factually false.
  The snapshot lists ABB's country as Switzerland.
- On top of that it is the richest multiple held (38.46x trailing, 37.59x forward) with
  the thinnest cash conversion (4.4% vs Atlas Copco's 15.3%).
- It is one of four industrials in a sleeve rated ACT at 54.32%.

**STRONGEST CASE AGAINST:** the PEG move, which the re-test was asked to weigh honestly.
I did, and **it does not survive contact with the data**:
- **It contradicts its sibling field.** PEG 1.33 on a 38.46x P/E implies ~29% annual EPS
  growth. A forward P/E of 37.59 against a trailing 38.46 implies **~2.3%** EPS growth
  over the next twelve months. Both come from the same analyst consensus, and they
  disagree by an order of magnitude.
- **Nothing happened to cause it.** ABB has not reported since July; its next print is
  10-20. Between 09-28 and today the trailing P/E rose 35.59 → 38.46 on a −0.5% price
  move. That means "trailing EPS" fell ~8% in a week with no report.
- Thesis-review read the P/E move as "margin compression continuing". That reading does
  not hold either, because there was no new margin data.
- **Both fields moved for reasons no file explains.** Neither is evidence of anything new
  about the business, in either direction.

The real strongest case against is Defensive's: nothing about ABB is dangerous. It is
1.7% of capital at +1.5% vs cost.

**KEY DISAGREEMENT:** whether the 10-20 print should decide this. Thesis-review says the
print is the test, and a beat would re-open the case to WEAKENING. The Chairman's
position is that the print can test the multiple, but not the premise or the
concentration:
- A beat that cut the forward P/E by 10% still leaves ~34x, the richest held.
- Holding *through* the print turns a valuation decision into a bet on a single earnings
  event. That is a short-horizon bet, the one this system says it has no edge in.

**DATA GAPS:**
- No EV/EBITDA. FCF is trailing-only.
- The P/B (113) and FCF-yield fields are unit-mismatched. Use FX-corrected ~11.7x and
  ~0.87%.
- The PEG and trailing EPS fields moved with no reported cause.

Moderate discount. Two of last sweep's three load-bearing facts weakened: the
forward-above-trailing inversion flipped (marginally), and the 0.09% FCF yield was a
unit error.

**CHAIRMAN CONVICTION:** 6 (down from 7)

**WHAT WOULD CHANGE THIS:** before the print, nothing in the data this system fetches.
After it: operating margin clearly above 16.9%, *and* FCF/revenue above ~8%, would retire
the SELL on merit. The wrong-premise problem would remain, but on its own that is a
reason to re-underwrite, not to sell.

**PORTFOLIO FIT** (from `portfolio`):
- Industrials are 54.32% of the stock sleeve, rated ACT.
- Selling and holding cash takes that to 48.22%, still ACT.
- ABB → VICI takes it to **~42.54%** (WATCH), which `portfolio` calls "the only
  combination in this candidate set that both resolves a Chairman-visible stock-selection
  call and closes a flagged diversification gap".
- The trade is tax-free inside the ISK, with a ~+57.76 SEK gain.

**FINAL CALL: SELL** — all 4 shares (~3,845.60 SEK), **before 2026-10-20**.

How this differs from carrying it a seventh time:
- This is a new call from a fresh test, at lower conviction.
- If it has not executed by the print, **it lapses**. The 2026-10-12 or 10-26 memo
  evaluates ABB only on the *reported* Q3 numbers, as a new decision with no streak
  count.
- If you are choosing to hold through the print, that is a legitimate decision. Say so,
  and it is recorded as yours.

**HORIZON:** Medium

#### #2 OPPORTUNITY: AZN.ST — AstraZeneca

**CATEGORY:** holding

**RANK HISTORY:** 59 now; 62 (09-28). **0 of 7 in the top 10.** The funnel's rank is
depressed by two data defects, not by the business:
- `forward_pe` is missing in all 7 runs (S21).
- The unit-mismatched FCF yield (0.20% instead of ~2.0%) feeds z_value −1.532.

**VOICES IN FAVOR:**
- Valuation, 7: PEG 1.1, 29% of range, price falling.
- Defensive, 7: beta 0.205, FCF/revenue 8.0%.
- Copycat, 7: CEO plus Chairman open-market buys on 14/09.
- Macro, 6: the only holding on the right side of the regime.
- Fundamental, 5: corrected cash conversion, but ROIC 13.1% is good, not excellent.

**VOICES AGAINST / CAUTIOUS:** none at SELL. Fundamental's 5 is the ceiling: a good
business, not a great one.

**STRONGEST CASE FOR:** the convergence, which survived a correction that cut the other
way.
- Last sweep's strongest case against was the 0.19% FCF yield. It was a unit error, and
  the real ~2.0% removes it.
- Four independent lenses (price, risk, regime, insiders) point the same way, and
  thesis-review independently grades the thesis INTACT and "arguably stronger".

I checked hard for a manufactured consensus. Each voice cites a different field, and
none depends on another's.

**STRONGEST CASE AGAINST:** `portfolio`'s concentration read. Healthcare is 39.18% of the
stock sleeve and the UK 39.18%, both WATCH and both entirely this one name. `portfolio`
says: "Do NOT add more AZN.ST shares right now on diversification grounds."

**KEY DISAGREEMENT:** merit against fit, kept separate.
- On fit, I partly disagree with `portfolio`, using its own figures. One more share takes
  Healthcare to ~42%, still under the 45% ACT line. It also *lowers* Sweden, the
  geography row rated **ACT**, from 49.03% toward ~46.8%. `portfolio` scored the
  sector cost and not the geography benefit.
- The add swaps some of an ACT problem for a deeper WATCH.

**DATA GAPS:**
- No forward multiple, 7 runs running.
- The GBP/SEK rate is not fetched, so the insider price cannot be compared with today's.
- Revenue-currency mix is unknown.

Moderate discount.

**CHAIRMAN CONVICTION:** 7

**WHAT WOULD CHANGE THIS:** operating margin below 20% at the **10-30** print, or a
Soriot/Demare disposal.

**PORTFOLIO FIT:**
- **Capital check against this sweep's `portfolio`:** ISK cash is **845.43 SEK**; one
  share costs 1,599.00 SEK. Not fundable today.
- Deployable cash outside the tax reserve is 16,132.57 SEK, almost all of it the
  unconverted PayPal balance (P3).
- Sequence it **after** the ABB → VICI leg, so a non-industrial, non-healthcare name
  enters the sleeve first.

**FINAL CALL: BUY** — 1 share. **Execution note: no idle capital confirmed (845.43 SEK).
Funded by P3 or the next contribution.** This is the last AZN add before the sleeve
gains another sector.

**HORIZON:** Medium

#### #3 OPPORTUNITY: VICI — Vici Properties

**CATEGORY:** new candidate (first surfaced by this funnel 2026-08-25, never watchlisted)

**RANK HISTORY:** 10 now; 10 (09-28). **7 of 7 runs in the top 10.**

**VOICES IN FAVOR:**
- Valuation, 8: 7.58x forward, 8.12% yield, 2% of range, no deterioration.
- Contrarian, 6: seven runs of unchanged fundamentals against a −14.3% price.

**VOICES AGAINST / CAUTIOUS:**
- Macro: a regime-only downgrade; the 10-year rose again to 5.24%.
- Defensive: net debt/EBITDA 4.82 into rising rates.

**STRONGEST CASE FOR:** Valuation's. A 67.5%-margin, still-growing landlord at 7.6x
forward and an 8.12% yield, with a PASS screen.

**STRONGEST CASE AGAINST:** Macro's, and it keeps being right on price. The 10-year went
4.94 → 5.18 → 5.24% over two sweeps, and the price followed each move.

**KEY DISAGREEMENT:** Valuation says the multiple is wrong. Macro says it is correctly
pricing a 5%+ 10-year. Not averaged. The pre-committed observable decides how much each
side gets:
- The retirement trigger was "10-year ≥ 5.5% with the price still falling". It sits at
  5.24%, not hit.
- So conviction holds at 5 rather than being nudged down on every tick. A threshold that
  is moved every week is not a threshold.

**DATA GAPS:**
- No FFO, AFFO, EV/EBITDA or lease coverage.
- Zero US insider data. Institutional ownership not fetched.

Heavy discount: a REIT underwritten without REIT metrics.

**CHAIRMAN CONVICTION:** 5

**WHAT WOULD CHANGE THIS:** the 10-year at ≥5.5% with the price still falling retires the
BUY. A dividend cut at the **10-28** print kills it.

**PORTFOLIO FIT:**
- `portfolio` on what it adds:
  - Real Estate is 0% of the sleeve, so it "DIVERSIFIES".
  - It is the first direct US listing, so it "DIVERSIFIES" by country and by currency.
  - It is the same large-cap tier as everything else.
- `portfolio` also asks you to confirm before ordering: that VICI is tradeable in the
  Avanza ISK, and how US dividend withholding treats it.
- Price in SEK: 22.73 × 9.9047 = 225.13 SEK per share (the FX rate is dated 09-25). The
  ABB proceeds buy **17 shares (~3,827 SEK)**.

**FINAL CALL: BUY** — 17 shares from the ABB proceeds, conviction 5.

If you decline it, keep the ABB proceeds as ISK cash and know that Industrials stays ACT
at ~48.2%. The cumulative drift since first surfaced is −14.3%: so far, not executing has
been the better *price* outcome. Seven weekly observations are noise, not evidence about
the 3-year call (n < 20).

**HORIZON:** Medium

#### #4 OPPORTUNITY: NVDA — Nvidia

**CATEGORY:** watchlist

**RANK HISTORY:** 4 now; 3 (09-28). **7 of 7 in the top 10.**

**VOICES IN FAVOR:**
- Growth, 8: +105.9% on a 100% CAGR, forward at half of trailing.
- Valuation, 7: forward 14.91x vs 29.58x.
- Fundamental, 7: ROIC 59.2%, net cash.

**VOICES AGAINST / CAUTIOUS:**
- Defensive: beta 2.217 against an untested −30% tolerance.
- Macro: duration at a 5.24% 10-year, plus FX.
- Fundamental's caveat: FCF is ~22% of earnings.

**STRONGEST CASE FOR:** Growth's. The cleanest forward/trailing signal in the set, on a
name with no suspect flag and no screen penalty.

**STRONGEST CASE AGAINST:** Fundamental's cash conversion. FCF yield is 0.74% against a
~3.4% earnings yield, and this one is USD over USD, so unlike AZN's it is real.

**KEY DISAGREEMENT:** three voices see the cheapest measured growth in the set; two say
the earnings are neither low-volatility nor yet cash. Not reconciled.

**DATA GAPS:**
- No revisions or backlog.
- The PEG moved 0.47 → 0.29 with no report (not relied on).
- No US insider data.

**CHAIRMAN CONVICTION:** 6

**WHAT WOULD CHANGE THIS:** FCF yield moving toward the earnings yield after the **11-17**
print raises it. Forward P/E rising above trailing kills it.

**PORTFOLIO FIT:**
- `portfolio`: it would add the first Technology weight to the stock sleeve, but
  "Avanza Global... is likely already heavy in by mandate, unverified".
- **Capital:** one share is ~2,287 SEK against 845.43 SEK of ISK cash. P3's proceeds are
  already allocated to gold tranche 2, AZN and the equity underweight.

**FINAL CALL: HOLD-WATCH.** Strong on merit; on hold for capital and for the untested
drawdown tolerance, not because of doubts about the business.

**HORIZON:** Medium

#### #5 OPPORTUNITY: APP — AppLovin

**CATEGORY:** new candidate (discovered by this funnel; not held, not watchlisted)

**RANK HISTORY:** 1 now; 1 (09-28). **7 of 7 in the top 10**, rank 1 in most runs. It is
the funnel's top name and has never been acted on.

**VOICES IN FAVOR:**
- Growth, 5: +52.8% revenue at a 77.7% operating margin, forward 12.8x vs 20.6x.
- Contrarian, 4: priced for a collapse the numbers don't show.

**VOICES AGAINST / CAUTIOUS:**
- Fundamental: ROE 203.7% sits on D/E 111.13, and the price is making new lows.
- Valuation: "cheap" on estimates the price is visibly rejecting.
- Defensive: beta 2.488, and this week shows it.
- Macro: long-duration growth at 5.24%.
- Copycat: no data (EDGAR 403).

**STRONGEST CASE FOR:** Growth's. No other name pairs this growth rate and this margin at
a 12.8x forward multiple.

**STRONGEST CASE AGAINST:** Fundamental's, in a sentence: the price fell 10.0% in a week
(312.47 → 281.31) and is still at 3% of its range. So it is setting **new** 52-week lows
while every fetched fundamental is unchanged. Either the market is wrong, or it knows
something the file does not contain. This system cannot tell which, and committing
capital before it can would be a guess.

**KEY DISAGREEMENT:** the funnel ranks it #1 on reported fundamentals; the market is
re-pricing it down on information that is not in the file. This is the purest case in
the set of "the mechanical rank and the price disagree", and it is why the rank alone is
not a BUY.

**DATA GAPS:**
- **S29**: no 52-week endpoints, so the size and start of the drawdown are invisible.
- No news or revisions. No US insider data. Institutional ownership not fetched.

These gaps are what cap the call.

**CHAIRMAN CONVICTION:** 4

**WHAT WOULD CHANGE THIS:** the **11-04** print. Growth ≥40% at an operating margin ≥70%
with the price still near its lows turns this into a real BUY case. A growth break
confirms the market.

**PORTFOLIO FIT:** not reached; this is a merit-stage watch.

**FINAL CALL: HOLD-WATCH**

**HORIZON:** Medium

### 3c. Other SELL recommendations on current holdings

You get a direct answer to "should I sell anything" every sweep. Beyond ABB.ST:

- **ATCO-B.ST.** Valuation SELL at 5, **declined.** It is the best business held
  (FCF/revenue 15.3%, ROIC 39.7%) and its break condition (ttm revenue negative) has not
  fired (+9.1%). Re-test after the **10-22** print. **NO ACTION.**
- **VOLV-B.ST.** Defensive SELL at 4, **declined.** PEG and forward P/E are still
  improving, and it is TOO_EARLY by its own 3-month window. The **10-23** print is the
  test. **NO ACTION.**
- **SHB-A.ST.** Growth SELL at 4, **declined.** One share, 152 SEK; retired 2026-09-14 as
  too small to matter. **NO ACTION.**
- **INVE-A.ST.** No SELL. D-b Option 3 stands, re-entry on the 10-07 NAV.
- **BTC0E.AS.** A partial **trim** (D-c), not a thesis sell. It depends on your
  confirmation that the 09-28 trim did not happen (see the opening and §6).
- **ALFA.ST, ETH, Xetra-Gold, Avanza Global, Avanza Auto 3:** no sell flag.
  - ETH cannot be sold cleanly while P1 is open.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens:

| Dimension | Grade | Number | One-line reason |
|---|---|---|---|
| Asset allocation vs targets | WATCH | Equity 71.79% vs 80% target (−8.21pp) | Largest single drift; driven by cash/gold underweight, not a sell signal on any specific holding |
| Equity sector concentration | ACT | Industrials 54.32% of the 7-name direct-stock sleeve (>45% line) | Unresolved since last sweep's ~53.98% — ABB.ST SELL call still not executed |
| Geography (home bias) | ACT | Sweden 49.03% of the direct-stock sleeve (>45% line) | Entirely from the 7 direct Swedish/UK names; Avanza Global's look-through country mix is unverified (data gap) |
| Currency exposure (revenue basis) | UNKNOWN | — | No fetched revenue-by-currency data exists for any holding this sweep — listing currency ≠ revenue currency; refusing to guess |
| Single-position concentration | ACT (with caveat) | Avanza Global = 53.06% of total (>15% cap) | Literal breach of max_single_position_pct, but it's a diversified global index fund, not single-company risk — flagged per the rule as written, not a sell signal. No individual stock exceeds 15% (largest: AZN.ST 5.65%) |
| Institution concentration | ACT | Avanza (ISK) = 82.41% of total (>80% cap) | Essentially unchanged from last sweep's 82.65% — structural side-effect of correctly consolidating into one ISK at this portfolio size, not a new problem |
| Fee drag | OK | 187.12 SEK/yr = 0.083% of total (cap 0.4%) | Clean; highest single fee is Auto 3 at 0.39%, under the 0.5% naming threshold |
| Wrapper efficiency | OK | ISK total 186,397.55 SEK vs ~300k allowance (headroom ~113,603 SEK); AF has zero deployable capital | Clean, consistent with CLAUDE.md's "DONE 2026-08-03" — verify the 300k figure with Skatteverket |
| Drawdown-tolerance fit | UNKNOWN | Tolerance −30%; portfolio.json cites a −20.62% backtest result | `data/backtests/` does not exist on disk — the cited figure has no backing file this session can verify. Treat the −20.62% claim as unverified, not confirmed. |

**What this memo adds, without overriding the table.**
- **Denominator.** The crypto row uses *total* capital (10.95%). On last sweep's
  investable basis, which excludes the 11,363.76 SEK tax reserve, crypto is
  24,774.46 / 214,817.15 = **11.53%**. That is the figure relevant to D-c. Last sweep
  flagged this convention change for `definitions.json` and it is still unpinned.
- **Provisional.** `portfolio` says the scorecard is not provisional. The allocation rows
  still inherit three `investor_profile.json` soft spots:
  - `horizon.primary_goal` is "nature UNCERTAIN", with a soft 3–7y horizon.
  - `constraints.exclusions` is empty, which matters because MO is a live pick.
  - `reference_targets` in the profile still reads 85/10/0/5 with no gold line, while
    `portfolio.json.targets` holds 80/10/5/0/5. That is two files disagreeing on one
    concept; see the target review in the structural section.

---

## 5. Headline calls

Each needs a decision this session.

1. **SELL ABB.ST, all 4 shares, before 2026-10-20.** The fresh re-test gives conviction 6.
   If it is not executed by the print, the call lapses; it is not carried again. Pair it
   with **BUY 17 VICI** (conviction 5) to clear Industrials ACT (54.32% → ~42.5%). If you
   are holding through the print deliberately, say so.
2. **Confirm the BTC0E.AS trim status in one line**, then decide D-c. My recommendation:
   trim ~2,500 SEK at the live Avanza price if it has not been done. Crypto is 11.53%
   of the investable base, F&G is 70, DXY is 120.33.
3. **Record Investor AB's and Industrivärden's NAV from the 2026-10-07 Q3 reports** in
   `data/company_profiles/`. This closes S6/D-b, eight sweeps old, for about ten minutes
   of work.
4. **Execute P3 (PayPal → SEK → ISK), 9th-plus sweep.** About 14,089 SEK net at the
   accepted 4% spread. It funds the AZN share (1,599 SEK) and gold tranche 2
   (~5,620 SEK), with the rest toward the 18,589 SEK equity underweight.
5. **Choose how to treat the 80/10/5/0/5 target until S26 runs** (structural section):
   keep it labelled provisional and build S26 first (my pick), or pre-emptively cut
   crypto to 7%.

---

## 6. Open actions vs open decisions

### Open actions (things to go do), by ID

| ID | Status | Action |
|---|---|---|
| **P3** | decided — pending execution (9th-plus sweep) | Convert 1,177.49 USD + 266.88 EUR in PayPal (14,676.14 SEK at today's FX, ~587 SEK spread at 4%) and transfer ~14,089 SEK net to the ISK. Zero the paypal holdings in `portfolio.json`. |
| **S6** | open, trigger in 2 days | Record the NAV discount/premium from Investor's **and** Industrivärden's 2026-10-07 Q3 reports. |
| **S26** | open, more urgent | Build the shock-window backtest **and write its output to a file** (`data/backtests/` does not exist; the −20.62% figure has no backing file). |
| **P1** | blocked (on you) | ETH cost basis. Blocks any ETH sale and keeps ETH out of D-c. |
| **P9** | open | Delete the phantom AZN OPENING row in the Excel Transactions tab. |
| **P10** | open | Confirm one 5,000 SEK deposit or two (2026-08-17 vs 2026-08-22). |
| **(new, record fix)** | for `journal`/`meta` | Correct OPEN_ITEMS.md's emphasis paragraph and S26's 2026-09-28 review: the BTC trim was *recommended*, not executed. Pending your confirmation. |

The D-series still has no standalone register (S30, unapplied). Reconstructed again:

### Open decisions (forks), by ID

**D-a — where ABB's proceeds go.** 6th sweep.
- *Option 1 — 17 VICI.* Clears Industrials ACT (~42.5%) and adds Real Estate and direct
  US. Trade-off: the rate path keeps moving against it, and there is FX risk at 9.90
  SEK/USD.
- *Option 2 — hold as ISK cash.* No rate or FX risk. Trade-off: Industrials stays ACT at
  ~48.2%, and cash is already over target.
- *Option 3 — 2 AZN shares (~3,198 SEK).* Stays in SEK and lowers Sweden's geography
  share. Trade-off: Healthcare goes to ~50% of the sleeve in one name (15,990 / 31,994
  SEK), swapping one ACT for another.
- **Pick: Option 1.** Option 2 is the honest fallback if you don't want USD REIT exposure
  into this rate path.

**D-b — Investor A's unmeasurable valuation.** Option 3 (hold, stop re-flagging) has been
in force since 09-28. The re-entry trigger fires **2026-10-07**. No other action.

**D-c — crypto sleeve sizing.** **Re-opened.** The 09-28 "applied" default was never
executed (see the opening).
- *Option 1 — trim ~2,500 SEK of BTC0E.AS at the live Avanza price.* Crypto goes from
  11.53% to ~10.4% of the investable base. The proceeds go to Avanza Global under your
  `profit_recycling_rule`. Trade-off: you sell part of an INTACT 3-year holding into
  rising sentiment.
- *Option 2 — no trim until S26 runs.* Trade-off: the overweight (~3,290 SEK on the
  investable base) stays inside an untested tolerance while F&G is 70.
- *Option 3 — raise the crypto target to 12%.* Trade-off: this ratifies drift with no
  analysis behind it, the opposite of what S26 exists to check.
- **Pick: Option 1**, once you confirm it has not already been done. Same reasoning as
  09-28; nothing about it has improved.

---

## 7. Cost of being wrong

| Headline call | If wrong | Realistic SEK downside | Recoverable? |
|---|---|---|---|
| SELL ABB.ST before 10-20 | Q3 beats, the stock re-rates 25% | ~960 SEK foregone (25% of 3,845.60) | Yes. It stays in the universe and can be rebought tax-free in the ISK. |
| BUY 17 VICI | The 10-year reaches 5.5%+ and the REIT de-rates 30%; SEK strengthens 10% | ~1,150 SEK + ~380 SEK FX, offset by ~310 SEK/yr dividend (8.12%) | Yes. Income-producing, and small (~1.7% of capital). |
| Trim ~2,500 SEK BTC0E.AS | BTC doubles | ~2,500 SEK upside foregone | Yes. It can be rebought in the ISK at 0% fee with no tax event. |
| *Not* trimming (the alternative) | Crypto halves from a "Greed" reading | ~12,390 SEK on the 24,774 SEK sleeve, ~1,650 SEK of it on the overweight alone | The overweight part, yes. Whether the sleeve loss fits −30% is what S26 hasn't tested. |
| Record the 10-07 NAVs | The number is mis-transcribed | ~0 SEK directly; a wrong NAV would mis-steer a 1,967 SEK holding | Yes. One number, re-checkable against the report. |
| Execute P3 / BUY 1 AZN.ST | You pay the spread; AZN falls 30% | ~587 SEK spread (certain) + ~480 SEK on the share | Spread, no, and it recurs every ~2 months while P3 waits. AZN, yes. |
| Keep 80/10/5/0/5 provisional (not cut crypto) | A ≥−30% shock arrives before S26 runs | At −30% on 226,181 SEK, ~67,850 SEK, beyond tolerance if the only on-record estimate (~−36%, see target review) is right | Only with time. The soft 3–7y horizon is what makes it recoverable, and that is exactly the thing nobody is checking. |

---

## 8. Timing collisions

From `data/cache/calendar/20261005-events.json`. Caveats: `calendar_last_verified` is
2026-08-03, US/SE CPI dates are still missing, and INVE-A.ST returned no date (a data
gap, not confirmed quiet).

- **2026-10-07 (2 days): Investor AB and Industrivärden Q3.** This is D-b's NAV trigger.
  Record the numbers; no trade is proposed.
- **TSM reports 10-15.** It is a Fundamental and Valuation pick, and its operating margin
  is the tested field.
- **ABB reports 10-20.** The SELL should execute **before** this date. After it, the call
  lapses and is re-decided on reported numbers.
- **SHB-A 10-21, ATCO-B 10-22, CMCSA 10-22, VOLV-B 10-23.** VOLV's is its TOO_EARLY
  re-test.
- **10-27: FOMC day 1, plus ALFA.ST and V both report.** Price reactions will mix company
  news with the rate decision. No ALFA or V trade is proposed. Read the results, don't
  act on day-one moves.
- **10-28: FOMC statement and VICI's print, on the same day.** If D-a Option 1 is chosen,
  buy alongside the ABB sale before 10-20. That avoids a rate-decision-plus-earnings
  double event on entry day.
- **10-29: SNDK, MA, MO. 10-30: AZN.ST and CHTR.** AZN's print is the share-add's test.
- **11-04: Riksbank decision, APP, TPL, FIS.** APP's print is #5's deciding event.
  **11-10:** Riksbank minutes. **11-17:** NVDA.

---

## 9. Data gaps for `meta`

Ordered by what each cost this sweep. Surfaced, not fixed.

1. **A recommendation was recorded as an execution (BTC0E.AS).** The "executed" wording
   in OPEN_ITEMS.md's emphasis paragraph and S26's 09-28 review contradicts both the
   09-28 SESSION_LOG ("User decisions: none") and `portfolio.json`. It propagated into
   this sweep's launch note and the portfolio lens's framing. Same family as S27, now
   inside the repository. A decision recorded as done needs a user-confirmation source
   cited next to it.
2. **Currency-unit mismatch in `fcf_yield_pct`** (and P/S and P/B) for issuers that
   report in a currency other than their listing. Verified by arithmetic: AZN.ST (0.20%
   → ~2.0%) and ABB.ST (0.09% → ~0.87%). **Hypothesis:** TSM's unflagged 29.8% FCF yield
   and 183.7% ROIC are the same error (TWD over USD). If so, S24's TSM hole is a unit
   bug, not a bounds-calibration problem.
   - This distorted the funnel's z_value for the portfolio's largest single stock.
   - It supplied last sweep's "strongest case against" AZN.
   - It inflated last sweep's ABB cash argument by about ten times.
3. **S24, 5th sweep:** TSM unflagged. ALL `fcf_yield_pct` 26.79% unflagged, 2nd sweep.
4. **S26 sharpened:** `data/backtests/` is absent per `portfolio`, so the only drawdown
   "pass" (−20.62%) has no traceable file. Not verified by this agent (no directory
   listing).
5. **Estimate fields move with no event.** Between prints, ABB's PEG went 2.11 → 1.33 and
   its trailing EPS fell ~8%; NVDA's PEG went 0.47 → 0.29. With no earnings-revision
   feed, the Council cannot tell a real revision from source noise. A thesis-review
   reading was built on one of these moves this sweep.
6. **US insider data: zero (EDGAR 403).** Separately, the FI search for "Volvo" returns
   Volvo Car AB rows mixed with AB Volvo. The issuer string should be the exact "AB
   Volvo". Institutional ownership is not fetched anywhere.
7. **S29, 7th sweep:** APP, the funnel's #1, made fresh lows (−10.0%) and the system
   cannot see from where. This capped #5 directly.
8. **S21:** AZN.ST has had no `forward_pe` in 7 of 7 runs. The Nordic MISSING rows
   persist.
9. **No EV/EBITDA, FFO or AFFO** (the VICI BUY). **No commodity or credit-spread series**
   (EOG/FANG/EXE unassessable; no cross-check on VIX 16.39). `us_cpi_yoy` is dated
   2026-08-01.
10. **`position_report.py` output not handed to `council`,** which has no shell. §1 was
    reconstructed from the same inputs. The orchestrator should run it and pass the file
    path, as S27 already recommends for lens outputs.
11. **The allocation denominator is still unpinned** (total vs investable). Crypto reads
    10.95% or 11.53% depending on the base, which sets D-c's size.
12. **Process: S27 scheduled-prompt drift, 7th occurrence by OPEN_ITEMS.md's own count.**
    S27's text counts six through 2026-09-28; this sweep's launch note says "8th", itself
    a hand-counted claim. Three in-session instances this sweep, none of which caused a
    wrong call:
    - the "trim executed" premise (#1);
    - MU counted as top-10 for 7 runs when it was first seen 08-31 (6);
    - "35 of 74 rows genuinely new" when only 5 names are first-time this run.
13. **CLAUDE.md priority line 2 is stale** (per `portfolio`): "the 2.5% BTC certificate
    (P4)" was closed 2026-08-17. Also, thesis-review recommends Xetra-Gold
    `thesis_status` TOO_EARLY → INTACT. The Chairman agrees, since the
    structure-not-price thesis was verifiable on day one. Not written by `council`.

---

## Structural decisions (non-stock)

Levers 1–2 (wrapper, fees) are structurally closed and not re-flagged.

**ACTION:** Execute P3. Convert the PayPal balance and transfer it to the Avanza ISK.
- **POSITION:** 14,676.14 SEK (1,177.49 USD + 266.88 EUR at today's FX), outside any
  wrapper.
- **TARGET:** ISK. ~5,620 SEK to gold tranche 2 (closes −2.48pp), 1,599 SEK to the AZN
  share, the remainder (~6,870 SEK) to Avanza Global against the 18,589 SEK equity
  underweight.
- **REASON:** a recurring ~4% spread on every ~2-month inflow. It is the binding
  constraint on the AZN BUY, the gold gap and the cash overweight.
- **THESIS STATUS:** decided by you 2026-08-17 (Option A).
- **WHAT CHANGED:** only the count (9th-plus sweep).
- **BREAK CONDITION:** a fee-free route appears, or the realised spread is materially
  worse than 4%.
- **CONFIDENCE:** High (arithmetic, not a forecast).
- **HORIZON:** Long

**ACTION:** Trim BTC0E.AS by ~2,500 SEK at the live Avanza price (D-c, Option 1).
**Conditional on your confirming the 09-28 trim did not happen.**
- **POSITION:** 150 units, 11,031 SEK at the stale 2026-08-21 mark (feed 404).
- **TARGET:** crypto from 11.53% to ~10.4% of the investable base. Proceeds to Avanza
  Global (`profit_recycling_rule`).
- **REASON:** S26 has still not run. F&G is 70 against DXY 120.33, and ETH's +4.0% this
  week widened the overweight. ETH stays untouched (P1).
- **THESIS STATUS:** INTACT (thesis-review). This is a sizing action.
- **WHAT CHANGED:** the record. Last week's "applied" turned out not to be executed.
- **BREAK CONDITION:** S26's shock-window backtest shows 80/10/5/0/5 inside −30%.
- **CONFIDENCE:** Medium
- **HORIZON:** Medium
- *Not in the picks ledger:* BTC0E.AS has no fetched price to join.

### Reference-target review (proposal only — nothing written to any file)

**What is adopted.**
- `portfolio.json.targets`: equity 80 / crypto 10 / cash 5 / FI 0 / gold 5. The 85/10/5/0
  split was adopted 2026-07-27 and written in 2026-08-03; the gold carve was applied
  2026-09-02.
- `investor_profile.json.reference_targets` still shows 85/10/0/5 with no gold line, last
  updated 2026-07-20.
- Under CLAUDE.md's ownership table, `portfolio.json` owns targets. The profile's copy is
  stale and should either note the carve or stop duplicating the numbers.

**Tested against the profile:**

1. **−30% max drawdown: unverified by any traceable file.**
   - The only "pass" is −20.62%. It has no backing file this session (`data/backtests/`
     absent), and per S26 it came from a window whose worst equity shock was only −19.14%.
   - The only other figure on record is the portfolio lens's 2026-09-07 stress arithmetic
     at **~−36%**, carried from the 09-28 scorecard, explicitly *not* a backtest, and not
     recomputed here. That one points outside tolerance.
   - So the one estimate that exists says "no", and the one "yes" cannot be traced.
2. **Horizon (house deposit, 3–7y SOFT).** 80% equity plus 10% crypto is acceptable only
   because the goal has no date.
   - The glidepath's `T3y` row is 40 equity / 45 FI / 10 cash / 5 crypto. If the goal
     firms inside three years, about half the equity has to be sold, possibly during a
     drawdown.
   - The profile names the re-anchor trigger as "the operative control". **Nothing in the
     system ever asks whether it has fired.**
3. **Currency.** If the Mediterranean option materialises, the liability is EUR
   (`horizon.currency_note`). The target is currency-neutral, which is correct while
   that is unknown.
4. **Crypto at 10%** is the sleeve the backtest tests least, because monthly
   rebalancing dilutes it (S26). It has drifted to 11.53% investable.

**Options:**
- **A.** Keep 80/10/5/0/5, labelled **PROVISIONAL**, and make S26 the first build. It must
  write its output to a file. *Trade-off:* you run an untested tolerance for however long
  the build takes.
- **B.** Pre-emptively move to 80/7/5/0/8 (`portfolio`'s 2026-09-14 proposal) until S26
  reports. *Trade-off:* this acts on an estimate as weak as the one it distrusts.
- **C.** Add one question to `journal`'s session-start, asked quarterly: "has the
  property goal acquired a date inside 3 years?". That gives the re-anchor trigger an
  owner. *Trade-off:* one question per quarter.

**Pick: A + C.** B only if S26's shock-window result is worse than −30%.

**This does not close S26. It makes S26 more urgent:** the "pass" it was opened to
qualify now has no traceable file behind it at all.

---

## 10. Learning notes

- **A recommendation is not an execution.** Last week the Council "applied" its own
  pre-committed default for the BTC trim. That meant the *advice* defaulted to "trim".
  It did not mean anything was sold, because this system cannot trade. Within a week the
  backlog described it as executed. Whenever a file says something happened to your
  money, check that it points to *you* confirming it.
- **A number can change when nothing has happened.** ABB's PEG and trailing EPS both
  moved sharply in a week when ABB reported nothing. Before treating a moved metric as
  news, ask what event could have moved it. If there was none, it is noise or a quiet
  data revision, not a signal in either direction.
- **Divide like by like.** AstraZeneca reports in dollars and is priced in kronor. Dividing
  dollar cash flow by a kronor market value made a ~2% free-cash-flow yield look like
  0.2%, and that error was last week's main argument against buying more. Ratios built
  from two currencies are wrong by the exchange rate (~9.9x here).
- **Not acting has been "right" on VICI so far, and that proves nothing yet.** The price
  is down 14% since the BUY was first made, so delay saved money. Seven weekly
  observations are noise for a 3-year call. This is why the scorecard withholds any
  verdict below 20 observations.

---

`journal` **must run next.** An unlogged memo is invisible to the next session and can
never be reconciled. Then run `python scripts/decisions.py record --picks
data/picks/2026-10-05-picks.csv`, followed by `python scripts/decisions.py basis --write`.
