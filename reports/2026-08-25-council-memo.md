# Council memo — 2026-08-25

*Structured synthesis of this system's own agents, not licensed investment
advice. Every figure traces to `data/cache/snapshots/20260825T090036.json`,
`data/screens/20260825T090427-candidates.csv`, or is labelled user-relayed.*

**Two data defects were found and fixed mid-sweep. Both changed conclusions.
Read section 2 before section 3.**

---

## 1. Position report

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A | 144.55 | -1.0% | +11.8% | 84% | 144.55 | fetched |
| Investor A | 407.90 | +0.6% | +40.5% | 92% | 2,039.50 | fetched |
| Volvo B | 347.00 | +2.1% | -5.6% | 79% | 4,511.00 | fetched |
| Atlas Copco B | 176.95 | +0.8% | -2.4% | 84% | 4,777.65 | fetched |
| AstraZeneca | 1,568.00 | +0.5% | +3.9% | 36% | 7,840.00 | fetched |
| Alfa Laval | 566.00 | +3.2% | -1.5% | 85% | 5,094.00 | fetched |
| ABB | 924.60 | -2.0% | -2.4% | 69% | 3,698.40 | fetched |
| Avanza Auto 3 | no data | no data | +65.2% | – | 16,191.00 | book value |
| Avanza Global | no data | no data | +0.0% | – | 119,999.00 | book value |
| Valour Bitcoin Zero | 47.29 | +0.0% | -22.9% | – | 7,093.80 | **user-relayed (S1)** |
| ETH (self-custody) | 23,533.40 | +2.0% | no data | – | 11,810.24 | fetched |

Nothing moved enough to change a thesis. Alfa Laval (+3.2%) and Volvo (+2.1%)
led; ABB fell 2.0% into its own SELL call. **The one structurally interesting
line is AstraZeneca at 36% of its 52-week range** — every other equity holding
sits at 69–92%. That gap is the single most decision-relevant fact in the
table and it is what two voices below build on.

The Valour certificate's fetched price (47.29 EUR ≈ 523 SEK/unit) still does
not reconcile with the broker figure (~73.54 SEK/unit). **S1 remains open and
this position is still priced from a user-relayed number, not a live feed.**
All allocation math below uses the broker figure, not Yahoo's.

---

## 2. Scout health, and two defects found mid-sweep

```
SCOUT HEALTH

  Universe:   624
  Fetched:    624   (cache 0, new 624, failed 0)
  Ranked:     614    (names that earned >=1 lens score)
  Candidates: 71  (holdings 8, watchlist 30, new 33)
  Focus:      22   (full Council analysis; the rest stay available as context)
  Screened:   71
  Passed:     36
  Missing:    17
  Failed:     18

  Status: VALID
```

The funnel itself ran clean: 624 names, zero fetch failures, 33 candidates
that are neither held nor previously watchlisted. But two defects surfaced
while reading the output, and **both had been silently corrupting earlier
sweeps.**

**Defect 1 — cross-currency ratios (found via TSM, fixed).** Yahoo reports
financial statements in a company's *reporting* currency and market cap in its
*listing* currency. For a cross-listed name these differ, and this pipeline
treated them as the same unit. TSM screened at a **34% free-cash-flow yield**
(TWD cash flow ÷ USD market cap — wrong by ~32×) and a 184% ROIC. Eight names
in the universe are affected, including **two holdings: AZN.ST and ABB.ST**
(both report in USD, priced in SEK), plus EVO.ST, HEXA-B.ST, BETS-B.ST, ASML
and TSM.

These metrics are now withheld rather than computed wrong, which lowers those
names' lens coverage and shrinks their scores toward neutral. **The practical
consequence: TSM dropped out of the quality shortlist entirely, and part of
the quality case made for AZN.ST in the last three sweeps rested on a ROIC
figure that was never computable.** That is stated again in AZN's entry below.

**Defect 2 — macro rates were strings, not numbers.** Every FRED-derived value
(`sek_per_usd`, the yields, VIX, the dollar index) came back as text. Any
downstream SEK conversion would have raised an error at best and silently
concatenated at worst. Found when this memo's own allocation math failed on
`'9.4632' × 1177.49`. Fixed; both defects now have regression tests.

**Flagged but not corrected** (9 values): Industrivärden's 1198% "revenue
growth" and SanDisk's 371.6% are real numbers with the wrong meaning — the
first is Yahoo counting investment gains as revenue for a holding company, the
second a spin-off comparability artefact. These are withheld from lens scoring
and shown with a `suspect` flag; the root fix is an `entity_type` column
(Excel request A1, S24).

---

## 3. Top 5 opportunities

Seven voices ran over the 22 focus names. **Architectural caveat, stated
plainly: the voices were run sequentially in one context, not in isolation**
(V2 Phase 7a is roadmapped, not built), so independence here is enforced by
discipline, not by architecture.

### #1 SHB-A.ST — Handelsbanken A

```
CATEGORY: existing holding (0.5% of the individual-stock sleeve — a token position)
RANK HISTORY: mechanical rank 37 of 71; first sweep with rank history recorded
VOICES IN FAVOR: copycat (8, chairman bought ~1.1m shares on the open market),
                 defensive (7, lowest-risk profile in the set), valuation (5, 12.1x with a 5.44% yield)
VOICES AGAINST / CAUTIOUS: growth (z -0.62, no growth case exists),
                 quality (unimpressed on its metrics — see below), macro (a Riksbank cut compresses NIM)
STRONGEST CASE FOR: Copycat. Pär Boman, Chairman of the Board, acquired roughly
        1.1 million shares across eight filings on 2026-07-21 at 139.15–140.87 SEK,
        with Fredrik Lundberg buying alongside him. Price today is 144.55. This is
        open-market buying, by the most informed insider, in size, recently, with a
        second insider in the same direction — it clears every quality test the
        Copycat lens applies, and it is the only signal in this sweep that does.
STRONGEST CASE AGAINST: Macro. Swedish CPI is 0.2% and the Riksbank is at 1.75%;
        the room to cut that makes CATE.ST attractive is the same room that
        compresses a bank's net interest margin.
KEY DISAGREEMENT: Quality scores this 0.473 and reports ROIC of 1.2% — but ROIC is
        not a meaningful metric for a bank, and the screen does not know that. This
        is the entity_type gap (S24) distorting a lens, not a finding about
        Handelsbanken. Named rather than averaged in.
DATA GAPS: no forward P/E issue here (12.76x available), but PEG of 20.24 is flagged
        implausible and was withheld from scoring.
CHAIRMAN CONVICTION: 7
WHAT WOULD CHANGE THIS: insider direction reversing, or a Riksbank cut arriving
        faster and deeper than the 2026-09-24 decision implies.
PORTFOLIO FIT: The position is 1 share, 144.55 SEK — 0.5% of the individual-stock
        sleeve and 0.07% of the portfolio. It is a placeholder, not a position.
        Adding here also improves the sleeve's 64.3% industrials concentration by
        diluting it, which no other candidate does as directly.
FINAL CALL: BUY — 20 shares, ~2,891 SEK, from ISK cash
HORIZON: Long (3y+)
```

### #2 AZN.ST — AstraZeneca

```
CATEGORY: existing holding (27.9% of the individual-stock sleeve, the largest)
RANK HISTORY: mechanical rank 59 of 71 — the screen does not like this name
VOICES IN FAVOR: contrarian (7), defensive (6)
VOICES AGAINST / CAUTIOUS: valuation (z -1.604, the WORST value score in the focus
                 set), copycat (explicitly neutral — see below), quality (0.109, and
                 now un-assessable on ROIC)
STRONGEST CASE FOR: Contrarian. At 36% of its 52-week range while every other equity
        holding sits at 69–92%, with margin 17.0%, revenue +6.4% and PEG 1.44. The
        de-rating is sector-wide, not a broken business.
STRONGEST CASE AGAINST: Valuation. 24.9x trailing with no forward multiple available,
        and the lowest value z-score of all 22 focus names. Cheap relative to its own
        past is not the same as cheap.
KEY DISAGREEMENT: Contrarian reads the 52-week position as opportunity; Valuation
        reads the same price as still expensive on earnings. Both are looking at the
        same number and drawing opposite conclusions, and the disagreement is real.
DATA GAPS: **This is the fourth consecutive sweep recommending AZN.ST, and this is
        the sweep where part of the earlier case turned out to be unfounded.** The
        ROIC that supported the quality argument was computed from a USD balance
        sheet against a SEK market cap and is now correctly withheld. No forward P/E
        (Nordic coverage gap). Copycat's apparent "insider buying" is CEO/CFO share
        awards at 0.00 GBP and plan allotments — compensation, not conviction, and
        must not be read as a signal.
CHAIRMAN CONVICTION: 6 — **down from High in the prior three sweeps, and the reason
        is the corrected data, not a change in the business.**
WHAT WOULD CHANGE THIS: a forward earnings figure becoming available, or the
        healthcare de-rating extending past the 2026-10 reporting round.
PORTFOLIO FIT: Already the largest single stock at 27.9% of the sleeve. Adding
        concentrates further into one name. Beta 0.211 argues it is the right kind of
        concentration, but concentration nonetheless.
FINAL CALL: BUY — 2 shares only, ~3,136 SEK, from ISK cash. **Deliberately smaller
        than the 3 shares recommended in each of the last three sweeps**, because the
        evidence base is now demonstrably thinner than those memos believed.
HORIZON: Long (3y+)
```

### #3 ABB.ST — ABB Ltd

```
CATEGORY: existing holding (13.2% of the individual-stock sleeve)
RANK HISTORY: mechanical rank 64 of 71, screen status FAIL
VOICES IN FAVOR (of selling): valuation (7), quality (6), copycat (6)
VOICES AGAINST: none this sweep
STRONGEST CASE FOR SELLING: Three independent sources agree. Valuation: 36.6x
        trailing and 35.7x forward, the most expensive holding on both measures,
        z -1.235. Quality: 14.1% margin and 14.2% revenue growth do not support that
        multiple, and ROIC is no longer computable for it. Copycat: recent insider
        direction is net selling — Peter Terwiesch disposed of 48,799 shares across
        2026-07-29, 07-30 and 08-13, and David Meline 2,456 on 08-05, while every
        acquisition on file predates May 2026.
STRONGEST CASE AGAINST: ABB is not a broken business, and selling a quality
        industrial at 69% of its range on relative-merit grounds is a rotation, not a
        rescue. If the alternative use of the capital disappoints, this was churn.
KEY DISAGREEMENT: none — the only sweep item where all voices that considered it
        point the same way. Reported as such rather than manufacturing tension.
DATA GAPS: ROIC and FCF yield withheld (cross-currency); price/book of 107.4 flagged
        implausible and withheld from scoring.
CHAIRMAN CONVICTION: 7
WHAT WOULD CHANGE THIS: insider buying resuming, or a multiple re-rating below ~30x.
PORTFOLIO FIT: Selling reduces the industrials block from 64.3% to 56.9% of the
        individual-stock sleeve — still ACT-rated, but the first real movement on a
        concentration this system has flagged for months. Frees ~3,698 SEK.
FINAL CALL: SELL — all 4 shares, ~3,698 SEK
HORIZON: Medium (6mo–3y)
```

### #4 VICI — VICI Properties

```
CATEGORY: NEW CANDIDATE — discovered by this sweep's funnel, not held, not previously watchlisted
RANK HISTORY: mechanical rank 8 of 71; top of the contrarian lens (z 1.857)
VOICES IN FAVOR: valuation (7), defensive (6), contrarian (top pick)
VOICES AGAINST / CAUTIOUS: macro (US 10y at 4.74% caps the re-rating; USD at 9.46 SEK
                 makes the entry expensive), growth (z 0.061, none)
STRONGEST CASE FOR: Valuation. 8.96x forward earnings and a 6.79% dividend yield at
        9% of its 52-week range, with beta 0.687. A triple-net casino REIT with
        contractual rent escalators priced as though the tenants were at risk.
STRONGEST CASE AGAINST: Macro. Net debt/EBITDA of 4.82 is normal for the structure
        but real, and REIT valuations are a rates story — with the US 10y at 4.74%
        and CPI still 3.54%, the thing that would re-rate this is not in view.
KEY DISAGREEMENT: Valuation treats the 52-week low as mispricing; Macro treats it as
        correctly priced for the rate environment. Unresolved, and it is the reason
        this is not a BUY today.
DATA GAPS: no PEG. No US insider data at all this sweep (SEC EDGAR returned 403
        through the proxy), so Copycat has nothing on this name — that silence is a
        fetch failure, not an absence of insider activity.
CHAIRMAN CONVICTION: 6
WHAT WOULD CHANGE THIS: US 10y falling toward 4%, or capital freeing up beyond the
        two calls above.
PORTFOLIO FIT: Would be the first US-listed individual stock and the first real
        estate exposure — genuinely diversifying against a 64% industrials sleeve.
        But after #1 and #2 the ISK holds ~5,261 SEK, and the dollar at 9.46 SEK/USD
        with the index at 118 is a poor moment to add USD exposure.
FINAL CALL: HOLD-WATCH — promote to the watchlist, revisit when capital frees up
HORIZON: Medium (6mo–3y)
```

### #5 NVDA — NVIDIA

```
CATEGORY: watchlist name
RANK HISTORY: mechanical rank 3 of 71; quality z 2.521, growth z 1.906
VOICES IN FAVOR: quality (8, best measured business economics in the set),
                 growth (7, PEG 0.59)
VOICES AGAINST / CAUTIOUS: defensive (beta 2.215 and an earnings print tomorrow),
                 valuation (z -1.260), macro (long-duration, most exposed to a higher 10y)
STRONGEST CASE FOR: Quality. ROIC 63.1%, net margin 63.0%, net cash (-0.24×
        EBITDA), revenue +85.2%, and a forward multiple of 16.0 against 32.9
        trailing. On measured economics nothing else in the set is close.
STRONGEST CASE AGAINST: Defensive, on timing rather than merit. **NVDA reports
        earnings tomorrow, 2026-08-26.** Beta 2.215 on a 5.05T market cap means a
        single print can move this double digits in either direction.
KEY DISAGREEMENT: Quality and Growth both rank it top; Valuation ranks it near the
        bottom. Both are correct — it is an outstanding business at a demanding
        price, and which matters more depends on a horizon the data cannot settle.
DATA GAPS: no US insider data this sweep. No analyst revision data anywhere.
CHAIRMAN CONVICTION: 7 on merit, but the action is governed by timing.
WHAT WOULD CHANGE THIS: tomorrow's print.
PORTFOLIO FIT: not reached — the timing call settles it before portfolio fit matters.
FINAL CALL: NO ACTION — **do not transact before the 2026-08-26 print.** Buying a
        2.2-beta name the day before earnings is a coin flip, and this system has no
        edge on one print.
HORIZON: Medium (6mo–3y)
```

**Other SELL recommendations on current holdings:** none. Volvo B, Atlas Copco
B, Alfa Laval and Investor A were all reviewed; none drew a sell flag from any
voice. Investor A carries the strongest insider support of the four (CEO plus
four other insiders, all acquisitions across 2026) and remains un-valuable on
P/E — the NAV discount that would settle it is still unavailable (S6, and
Excel request A2).

---

## 4. Portfolio health scorecard

| Dimension | Status | Reading |
|---|---|---|
| Wrapper efficiency | OK | All capital in the ISK; closed since 2026-08-03 |
| Fee drag | WATCH | One item left: the 2.5%/yr BTC certificate (P4) |
| Industrials concentration | **ACT** | 64.3% of the individual-stock sleeve; the ABB sale takes it to 56.9% |
| Single-name concentration | WATCH | AZN.ST 27.9% of the sleeve, rising to ~31% if #2 executes |
| Crypto vs target | OK | 8.59% vs a 10% target — below, no action |
| Cash | OK | 11,288 SEK ISK + 14,094 SEK in PayPal (P3 unexecuted) |
| Geographic mix | WATCH | The sleeve is 100% Nordic/European; VICI would be the first US name |
| ESG / exclusions | UNKNOWN | No stated exclusions exist — open since 2026-08-24 |

Allocation: individual stocks 12.8%, index funds 61.9%, crypto 8.6%, cash
10.3%, PayPal 6.4%. Total 219,939 SEK.

---

## 5. Headline calls

1. **BUY 20 SHB-A.ST (~2,891 SEK) from ISK cash** — confidence **Medium**, horizon **Long**. New top call, on the strongest insider evidence in the sweep.
2. **SELL 4 ABB.ST (~3,698 SEK)** — confidence **Medium**, horizon **Medium**. Second consecutive sweep; now corroborated by insider selling as well as valuation.
3. **BUY 2 AZN.ST (~3,136 SEK) from ISK cash** — confidence **Medium**, horizon **Long**. Fourth sweep, but **downgraded from High and reduced from 3 shares to 2** because a supporting metric turned out to be wrong.
4. **NO ACTION on NVDA until after the 2026-08-26 print** — confidence **High**, horizon **Medium**.
5. **Execute or explicitly decline P3 (PayPal conversion, ~564 SEK cost)** — confidence **High**, horizon **Long**. Fourth consecutive sweep of identical unexecuted advice. An explicit "no" closes this as well as a "yes" does.

Capital check: ISK cash 11,288 SEK. Calls 1 and 3 consume ~6,027 SEK, leaving
~5,261 SEK. Call 2 adds ~3,698 SEK on settlement. No call depends on PayPal.

---

## 6. Open actions vs open decisions

**Open actions** (things to go do):
- Execute or decline P3 — PayPal conversion, 1,177.49 USD + 266.88 EUR, ~564 SEK cost at the confirmed 4% spread.
- P9 — reconcile AZN.ST share count: the Excel ledger says 6, Avanza says 5. **This memo assumes 5.** If it is 6, call 3's sizing is wrong.
- P10 — confirm whether the 5,000 SEK deposits on 2026-08-17 and 2026-08-22 are two deposits or one mis-dated.

**Open decisions** (forks the data does not settle):
- **What replaces ABB in the sleeve?** Options: (a) VICI, diversifying into US real estate but adding USD exposure at 9.46 SEK/USD; (b) add to SHB-A, deepening the strongest insider signal but concentrating in Swedish financials; (c) hold the proceeds as cash pending the NVDA print. My reading: (b) then reassess after 2026-08-26.
- **Investor A's NAV discount (S6/P5).** Two voices have now wanted it and been unable to act. Options: supply it once per quarter via Excel (request A2), or accept that INVE-A cannot be valued by this system and stop ranking it on P/E.
- **Do you have any portfolio exclusions at all?** Unanswered since 2026-08-24; it is why the ESG row reads UNKNOWN.

---

## 7. Cost of being wrong

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| BUY 20 SHB-A.ST (2,891 SEK) | A Riksbank cut compresses NIM; a 20% drawdown is ~578 SEK | Yes — 1.3% of the portfolio, dividend-supported |
| SELL 4 ABB.ST (3,698 SEK) | ABB re-rates upward after sale; opportunity cost on ~3,700 SEK | Yes — repurchasable, no tax event inside the ISK |
| BUY 2 AZN.ST (3,136 SEK) | Healthcare de-rating continues; 20% is ~627 SEK | Yes, but it deepens an already-27.9% position |
| NO ACTION on NVDA | The print is good and the entry is missed | Yes — the business does not change on one print |
| P3 execution | The 4% spread (~564 SEK) is a known, accepted cost | No — but it is already sunk by delay |

---

## 8. Timing collisions

- **NVDA reports 2026-08-26 (tomorrow)** — governs call 4 above.
- Riksbank rate decision 2026-09-24; FOMC 2026-09-15/16. Both matter for the
  SHB-A NIM question and the VICI rate question, neither is imminent.
- No holding reports before 2026-10-20 (ABB), so the SELL faces no earnings risk.

---

## 9. Data gaps for `meta`

1. **No US insider data this sweep** — SEC EDGAR's CIK mapping returned 403 through the proxy. Copycat covered 7 Swedish issuers and zero US names. That asymmetry must not be read as "no US insider activity" (S20).
2. **Cross-currency metrics** — now withheld for 8 universe names including 2 holdings. The fix is correct but the coverage loss is real: AZN.ST and ABB.ST can no longer be quality-ranked at all.
3. **`entity_type` is the highest-value missing field** — it would fix the bank-ROIC distortion (SHB-A scored 1.2%), the holding-company revenue artefact (INDU-C at 1198%), and the REIT leverage reading in one column (S24, Excel A1).
4. **No NAV for holding companies** (S6) — blocks INVE-A and INDU-C, the two cheapest-looking P/Es in the focus set, both uninterpretable.
5. **Forward P/E still missing for 5 of 22 focus names**, all Nordic.

---

## 10. Learning notes

- **A ratio is only meaningful when its numerator and denominator share a
  unit.** TSM's 34% "free-cash-flow yield" was TWD cash flow over a USD market
  cap. It looked like the most attractive number in the entire universe
  precisely because it was wrong by the exchange rate. When a figure is a
  clear outlier among peers, the first question is whether the units match —
  not whether you have found something.
- **ROIC is not a universal metric.** Handelsbanken screening at 1.2% ROIC is
  not a finding about Handelsbanken; banks fund themselves with deposits, so
  "invested capital" does not mean what it means for a manufacturer. A screen
  that applies one metric set to every business type will systematically
  mis-rank whole sectors.
- **Insider "buying" is not one thing.** AstraZeneca's CFO and CEO both show
  acquisitions this year — at 0.00 GBP, which means shares vesting under a
  compensation plan. Handelsbanken's chairman bought 1.1 million shares with
  his own money on the open market. Only the second tells you what someone
  who knows the business thinks it is worth.
- **A recommendation repeated four times is not four pieces of evidence.**
  AZN.ST has led three prior memos partly on a ROIC figure that was never
  computable. Repetition felt like conviction accumulating; it was the same
  unverified input being re-read. The call survives on other grounds, at lower
  size and lower confidence — which is what the correction should cost it.

---

*`journal` must run to log this sweep. An unlogged memo is invisible to the
next session and can never be reconciled.*
