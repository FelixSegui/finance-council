# Council Memo — 2026-09-14

*This is structured synthesis of your own agents' analysis, run over data fetched
this session. It is not licensed investment advice.*

Every number below traces to `data/cache/snapshots/20260914T060927.json`,
`data/screens/20260914T061009-candidates.csv`, `data/candidate_history.csv`,
`data/portfolio.json`, `data/investor_profile.json`,
`data/cache/calendar/20260914-events.json`, `data/company_profiles/`, or this
sweep's four lens outputs — or is labelled user-relayed / background.

---

## 1. Position report

## Position report — 2026-09-14

Snapshot: `20260914T060927.json` · previous: `20260907T061430.json`

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 149.75 | +0.2% | +15.9% | 94% | 149.75 | fetched |
| Investor A (stock) | 399.50 | -1.6% | +37.7% | 86% | 1,997.50 | fetched |
| Volvo B | 339.20 | -2.6% | -7.7% | 73% | 4,409.60 | fetched |
| Atlas Copco B | 174.55 | -0.1% | -3.7% | 79% | 4,712.85 | fetched |
| AstraZeneca | 1,541.00 | -1.9% | +0.2% | 31% | 12,328.00 | fetched |
| Xetra-Gold (physically-backed gold ETC, ISIN DE000A0S9GB0) | no data | no data | no data | - | 5,689.22 | FETCH FAILED |
| Alfa Laval | 545.60 | -1.7% | -5.0% | 73% | 4,910.40 | fetched |
| ABB | 926.60 | +1.6% | -2.2% | 69% | 3,706.40 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| Valour Bitcoin Zero SEK (certificate, ISIN CH0585378661) | 47.29 | +0.0% | -22.9% | - | 7,093.80 | fetched |
| ETH (self-custody wallet) | 24,248.04 | +0.9% | no data | - | 12,168.88 | fetched (CoinGecko, converted via sek_per_eur) |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high.*

### Crypto context (spot, from CoinGecko)

| Coin | Price (EUR) | Δ vs prev snapshot | 7d | 30d | vs ATH |
|---|---|---|---|---|---|
| ethereum | 2,182.11 | +1.0% | +0.7% | +33.6% | -48.4% |

**Reading it.** A broadly soft week across the Swedish sleeve (Volvo -2.6%,
AstraZeneca -1.9%, Alfa Laval -1.7%, Investor -1.6%), with ABB the only
meaningful gainer at +1.6% — which is mildly awkward, since ABB is the one
holding carrying a live SELL call. Nothing here contradicts a thesis: Volvo's
drop leaves it at 73% of range with its thesis metrics improving (thesis-review:
revenue growth flipped to +2.7%, PEG 1.49→0.99), and AstraZeneca at 31% of range
is the cheapest holding on the valuation lens's read — that discount *is* its
thesis, not a break of it. Index funds: Avanza Global and Auto 3 both carried at
book, no live NAV, no action.

**Two rows in that table are not real, and the memo does not use them.**
(a) **Valour Bitcoin Zero's "47.29 / -22.9% / 7,093.80 SEK" comes from the known-bad
Yahoo `BTC0E.AS` feed** — the standing S1 gap, roughly 7x off, with an identical
52-week high and low (47.735/47.735 EUR), the signature of a stale listing. The
position is carried at its last broker-confirmed value: **150 units @ 73.54
SEK/unit = 11,031 SEK, +19.82% since purchase (Avanza screen, 2026-08-23)** —
which is what `portfolio.json` and this sweep's portfolio lens both use (crypto
23,199.88 = ETH 12,168.88 + BTC0E 11,031). This is not new; it is S1 working as
designed. (b) **Xetra-Gold returned HTTP 404 for a third consecutive week** (direct
and chart-fallback both). Carried at cost, 5,689.22 SEK. Do not read its "no
data" as "flat."

---

## 2. Scout health

```
Universe     624
Fetched      624 (1 failed)
Ranked       614
Candidates    73  (holdings 9, watchlist 30, new 34)
Focus         23
Screened      73
Passed        40
Missing       17
Failed        16
Status       VALID
```

**Reading it.** Status VALID, so section 3 can be trusted on its own terms. The
funnel did search and it did find non-held names — **34 `new` rows**, so this is
not a holdings-only sweep. But the discovery signal underneath is thin: the
top-15 is now frozen across four consecutive runs (APP/SNDK/NVDA at ranks 1/2/3
in all four), and comparing `candidate_history.csv` run-over-run, exactly **one
name is genuinely first-seen this sweep — LULU** (MEKO.ST is a returning name,
last present 2026-08-25). Three names dropped out: UHS, TEL2-B.ST and
**VOLCAR-B.ST**. That last one matters: VOLCAR-B.ST was last sweep's single
Swedish name with a genuine multi-insider buying signal and S21's live worked
example, and it has now left the candidate set without the question being
resolved either way. Flagged, not fixed.

---

## 3. Top opportunities — the Chairman's Top 5

Before the five: what the seven voices actually produced is summarised at the end
of this section, and every pick is recorded in
`data/picks/2026-09-14-picks.csv`.

---

### #1 OPPORTUNITY: ABB.ST — ABB Ltd

**CATEGORY:** holding
**RANK HISTORY:** current 65, previous 66, 0/4 times in top 10 (ranks 64/64/66/65
across the four runs — it has never been a candidate on merit, only as a holding)
**VOICES IN FAVOR (of selling):** Copycat: 7, ~51,255 shares disposed by two named
insiders in three weeks against 7,777 shares of same-date, same-price board
allotment · Valuation: 7, forward P/E 35.44x is flat against trailing 35.47x
despite 14.2% ttm revenue growth · Macro: 6, the most expensive name in a Nordic
industrial sleeve facing a +1.45% Swedish real policy rate · Fundamental/Quality:
6, `fcf_yield_pct` 0.09% and ~4.4% FCF margin is the thinnest cash conversion of
any holding
**VOICES AGAINST / CAUTIOUS:** Defensive: ABB's balance sheet is the *best* of the
three P6 industrials — net debt/EBITDA 0.46, D/E 55.8 — so this is not a risk
sell, and calling it one would be wrong
**STRONGEST CASE FOR:** Valuation's. A forward multiple that does not fall below
the trailing multiple while revenue grows 14.2% is the market saying it expects
margin compression. You are paying 35x for earnings the market does not expect to
grow. Independently, thesis-review reached BROKEN from the same numbers this
sweep without being shown the Council's prior calls.
**STRONGEST CASE AGAINST:** Defensive's. Every metric the SELL rests on is a
valuation or governance metric; none is a solvency or downside metric. ABB is not
a risky holding, it is an expensive one — and expensive holdings can stay
expensive for years.
**KEY DISAGREEMENT:** Whether the insider evidence still counts. Copycat weights
it at 7; the disposal cluster is real (Terwiesch 18,799 @ 76.76 CHF on 07/29,
10,000 @ 77.30 on 07/30, 20,000 @ 83.46 on 08/13; Meline 2,456 @ 82.12 on 08/05).
But this is the **third consecutive FI pull returning the identical set** — the
cluster has not grown since 2026-08-13. It is a real signal that has gone static.
Copycat says static-and-unreversed still counts; Defensive says an eight-week-old
frozen signal is not fresh evidence. Both are right about different things. The
SELL does not depend on resolving this, because Valuation's case stands alone.
**DATA GAPS:** `price_to_book=106.60` is scout-flagged suspect (currency/scale
artifact; FX-corrected ~11.8x sits in `company_profiles/ABB.ST.json`) and is not
used. No EV/EBITDA is computed anywhere in this system, so the leverage-adjusted
multiple is approximated from `net_debt_to_ebitda` 0.46 only. `interest_expense`
and `interest_coverage` are MISSING for this name. None of this discounts the
call materially — the case rests on P/E, forward P/E, revenue growth and FCF
conversion, all of which are clean.
**CHAIRMAN CONVICTION:** 7
**WHAT WOULD CHANGE THIS:** A forward P/E that falls meaningfully below the
trailing multiple at the 2026-10-20 print — i.e. the market starting to price
earnings growth rather than margin compression. That is the observable, and it is
five weeks away.
**PORTFOLIO FIT:** Portfolio's read, cited not re-derived: the position is
3,706.40 SEK (1.66% of the 223,730.67 SEK book) — this is a quality/rotation call,
not a sizing one. Industrials are **55.1% of the identifiable single-stock sleeve
(ACT)** and Sweden **50.2% (ACT)**; ABB is in both buckets. Portfolio's own
rebalancing item (e) says it directly: if ABB is exited, redirecting the proceeds
to gold (undershooting at 2.54% vs a 5% target) or to a genuinely diversifying
sector "would improve portfolio shape more than redeploying into another Nordic
industrial." ISK-wrapped, so the sale is not a taxable event.
**FINAL CALL:** SELL
**HORIZON:** Medium (6mo–3y)

> **This is the fourth consecutive sweep this call has been made and not
> executed** (2026-08-24, 2026-08-31, 2026-09-07, today). For the record, the cost
> of the delay so far is approximately nothing: ABB was 924.60 on 2026-08-25 and
> is 926.60 today, +0.2%. The argument for executing is not that you are losing
> money by waiting — it is that a decision reaching its fourth sweep unactioned
> stops being a decision. An explicit "no, I am keeping ABB" closes this item just
> as validly and frees the attention.

---

### #2 OPPORTUNITY: VICI — Vici Properties

**CATEGORY:** new candidate (discovered by the funnel; never promoted to the
watchlist, still arriving as `source=new` on its fourth run)
**RANK HISTORY:** current 9, previous 9, 4/4 times in top 10 (8 → 8 → 9 → 9)
**VOICES IN FAVOR:** Valuation: 8, P/E 9.62 / forward 8.30 / 7.41% dividend yield
at 1% of its 52-week range · Contrarian: 7, revenue still +5.7% with a 15.5%
three-year CAGR and 70.2% operating margin while the price sits at the 52-week
low — the de-rating is about the discount rate, not the cash flows
**VOICES AGAINST / CAUTIOUS:** Macro: 4, this is the single most 10-year-sensitive
name in the focus set and the US 10y is 4.95% with real fed funds at -0.08% —
downgraded explicitly on regime grounds, not buried in a score · Defensive: net
debt/EBITDA 4.82 and D/E 60.3, and **this system fetches no credit-spread data at
all**, so the refinancing risk cannot be measured
**STRONGEST CASE FOR:** Contrarian's, and it is a specific claim rather than "it's
cheap and unpopular": VICI's rents are contracted and the contracted base is still
compounding (+5.7% ttm, +15.5% 3y CAGR, 67.5% net margin), while the equity trades
at the bottom of its 52-week range. Those two facts are in tension, and the
tension resolves through the discount rate, which is a market variable, not a
business one.
**STRONGEST CASE AGAINST:** Macro's, and it is the same fact seen from the other
side: the discount rate is precisely the problem. US CPI is 3.71% against a 3.63%
fed funds rate — the Fed has essentially no real-rate cushion to cut from without
re-accelerating inflation. A 7.41% yield on 4.82x levered real estate in that
setting is a price, not a bargain.
**KEY DISAGREEMENT:** Not paraphrased away — Valuation and Contrarian are buying a
cash-flow stream at a discount; Macro is saying the discount is the correct price
of the rate risk and will not close until the 10y does. Neither can be settled
from fetched data. **What tilts it:** the price fell from 26.51 to 24.73 USD
(-6.7%) across the four sweeps this call has been open, while every business
metric held or improved. The entry got better and the thesis did not get worse.
That is not the same as the thesis being validated — but it does mean the
opportunity has not decayed.
**DATA GAPS:** No EV/EBITDA (the right multiple for a REIT), no FFO or AFFO
anywhere in this system, no credit-spread data, and no insider data of any kind —
`insider_activity` returned `CIK mapping fetch failed: 403 Forbidden` and VICI was
never submitted to the fetch regardless. `peg` is null. Discount confidence by
roughly one point for the missing FFO alone; a REIT valued on P/E is being valued
on the wrong denominator.
**CHAIRMAN CONVICTION:** 6
**WHAT WOULD CHANGE THIS:** The FOMC decision on 2026-09-15/16 — tomorrow. A
signal that the policy path is turning down resolves Macro's objection directly;
a hawkish hold hardens it. Nothing else on the calendar moves this call as much.
**PORTFOLIO FIT:** Portfolio's read, cited: VICI "diversifies sector (Real Estate,
0%) + country" and sits at "the smaller end of large-cap." It is the only Top-5
name that answers two ACT-rated concentrations at once (Industrials 55.1%, Sweden
50.2%). Capital: **verified against this sweep's portfolio output — ISK cash is
845.43 SEK.** There is no idle capital. The funding source is the ABB sale:
3,706.40 SEK ÷ (24.73 USD × 9.5646 SEK/USD = 236.53 SEK) ≈ 15 shares. Note this
also increases Avanza institution concentration, already **83.12% — ACT, over the
80% cap** — though the ABB sale offsets it exactly, since both sit in the same ISK.
**FINAL CALL:** BUY
**HORIZON:** Medium (6mo–3y)
**Execution note:** structurally linked — no ABB sale, no VICI buy. No idle capital
confirmed. If you decline the ABB sale, this reverts to a watch item funded by the
next contribution.

---

### #3 OPPORTUNITY: SHB-A.ST — Handelsbanken A

**CATEGORY:** holding (carries an open Chairman SELL from 2026-08-31)
**RANK HISTORY:** current 42, previous 40, 0/4 times in top 10 (37 → 37 → 40 → 42
— steadily drifting down)
**VOICES IN FAVOR (of selling):** Valuation: 6, PEG 18.85 with revenue -3.8% YoY at
94% of its 52-week range — priced like a grower it is not · Growth: 6,
`z_growth` -1.268, the worst growth score of any holding in the set
**VOICES AGAINST:** Copycat: 5, the largest insider transaction anywhere in this
sweep's data points the other way
**STRONGEST CASE FOR:** Valuation's, seconded by thesis-review's independent
"captured upside" read — 149.75 against a 52-week high of 151.75 is 98.7% of the
way there, and the stated reason for owning it ("good upside") has been collected.
**STRONGEST CASE AGAINST:** Copycat's, and it is genuinely large. On 2026-08-26,
Chairman Pär Boman filed **ten separate acquisitions totalling 1,850,000 A-shares
at 145.55–146.24 SEK** — roughly 270M SEK — every one marked "Closely associated:
Yes." Today's 149.75 is 2.4–2.9% above where that buyer bought.
**KEY DISAGREEMENT:** Whether that purchase is a signal at all, and this is where
the voice's own interpretation rule bites. "Closely associated: Yes" means the
shares were bought by a related party, not personally out of salary, and Boman
chairs both Handelsbanken and Industrivärden. Ten fills on one day totalling 1.85M
shares has the shape of an **entity-level reallocation inside the sphere**, not a
conviction bet by a person. Copycat's own standard — interpret by quality and
context, never by direction alone — says this is a different and weaker signal
than the Investor A pattern (see below), even though it is ten times the size.
Valuation and Copycat therefore do not actually meet: one is arguing about the
price of the earnings, the other about who owns the shares.
**DATA GAPS:** `debt_to_equity` MISSING, and `roic_pct` reads 1.2% — both are
meaningless for a bank, which is exactly the `entity_type` gap S24 names. The
funnel is ranking this name on fields that do not describe it.
**CHAIRMAN CONVICTION:** 6 — on the NO ACTION, not on either side of the argument
**WHAT WOULD CHANGE THIS:** Nothing, at this position size. That is the point.
**PORTFOLIO FIT:** The decisive fact, and it is arithmetic: **the position is one
share, 149.75 SEK, 0.07% of a 223,730.67 SEK portfolio.** Whether it doubles or
goes to zero cannot change the portfolio's risk or return by any measurable amount.
**FINAL CALL:** NO ACTION — **and the open SELL from 2026-08-31 is formally
retired.** This is not a reversal of the valuation read, which I think is correct:
if this were a 5% position the answer would be sell today. It is a judgement that
a decision incapable of moving the portfolio should not consume a Council slot,
a conviction score and a line in the open-calls ledger every week. The valuation
finding is recorded in the picks file; the trade instruction is withdrawn.
**HORIZON:** n/a

---

### #4 OPPORTUNITY: APP — AppLovin

**CATEGORY:** new candidate (discovered by this sweep's funnel; `source=new` on all
four runs, never promoted to the watchlist)
**RANK HISTORY:** current 1, previous 1, 4/4 times in top 10 — rank 1 in every run
since the funnel began recording
**VOICES IN FAVOR:** Fundamental/Quality: 8, the best quality profile in the entire
candidate set — ROE 203.7%, ROIC 65.5%, 64.6% net margin, 77.7% operating margin,
net debt/EBITDA 0.09 · Growth: 7, 52.8% revenue growth on a 24.8% three-year CAGR
with PEG 0.70 and forward P/E 15.44 against trailing 24.88 · Valuation lens:
"cheap" — PEG 0.70 with the price at 4% of its 52-week range
**VOICES AGAINST / CAUTIOUS:** Defensive: **beta 2.488, the highest in the focus
set**, plus D/E 111.13, against a -30% drawdown tolerance the system has never
stress-tested (S26 open) · Macro: this regime rewards cyclicals and value over
long-duration growth; a 2.5-beta growth name is the profile that de-rates first ·
Copycat: no data — zero insider coverage, see below
**STRONGEST CASE FOR:** Quality's. A business earning 65.5% ROIC on 77.7% operating
margins with essentially no net debt, growing 52.8%, at a forward multiple of 15.4x
is not a normal combination, and four consecutive mechanical runs have put it
first out of 614 ranked names on that basis.
**STRONGEST CASE AGAINST:** The one nobody can answer. **The price is at 4% of its
52-week range while having gone essentially nowhere across four sweeps (305.77 →
314.49, +2.9%).** Those two facts together mean the 52-week high is far above the
current price and the drawdown happened before this system started watching — and
`pct_52w_range` is the *only* range field in the candidates CSV. The 52-week high
and low are not there. So the system can see that something large happened to this
stock and cannot see what, when, or from what level. That is not a reason to
disbelieve the quality metrics; it is a reason not to commit capital on them.
**KEY DISAGREEMENT:** Quality and Growth are reading the fundamentals; Defensive
and Macro are reading the volatility and the regime. Neither side is engaging the
actual blocker, which is that the price history is invisible to this system.
**DATA GAPS, and they should discount this hard:** (a) no 52-week high/low in the
candidates CSV, so the headline "near the lows" signal cannot be interpreted;
(b) `div_yield_pct` is null and `beta` 2.488 is the only volatility measure;
(c) **zero insider data** — `insider_activity` returned `CIK mapping fetch failed:
403 Forbidden` and, separately, APP was never submitted to the insider fetch at
all, which only received the eight portfolio tickers; (d) no earnings-revision or
TAM data anywhere, so Growth's case is measured growth only.
**CHAIRMAN CONVICTION:** 5
**WHAT WOULD CHANGE THIS:** Add `week52_high` / `week52_low` to the candidates CSV
(a scout change, not a data-source change — the snapshot already carries both
fields per ticker). That single column turns "4% of range" from an uninterpretable
number into a thesis or a disqualification. It is the cheapest high-value fix on
this memo's list.
**PORTFOLIO FIT:** Portfolio's read, cited: APP "diversifies sector (Communication
Services, 0%) + country; concentrates market-cap tier (large)." Capital: ISK cash
845.43 SEK against a 314.49 USD × 9.5646 = 3,008 SEK share price — not fundable
from idle capital in any case.
**FINAL CALL:** HOLD-WATCH — **and promote APP to `data/watchlist.json`.** A name
that has ranked #1 out of 614 for four consecutive runs and is still arriving as
an unpromoted `new` row is a gap in the funnel's own bookkeeping, independent of
whether it is ever bought.
**HORIZON:** Medium (6mo–3y)

---

### #5 OPPORTUNITY: AZN.ST — AstraZeneca

**CATEGORY:** holding (carries an open Chairman BUY from 2026-09-07)
**RANK HISTORY:** current 60, previous 61, 0/4 times in top 10 (59 → 60 → 61 → 60)
**VOICES IN FAVOR:** Valuation: 7, the only holding this lens calls **cheap** — PEG
1.14 at 31% of its 52-week range with 17.0% net margin and 6.4% revenue growth ·
Macro: 6, the only holding whose macro driver is genuinely different from the
Nordic industrial/financial sleeve the regime data argues against
**VOICES AGAINST / CAUTIOUS:** Fundamental/Quality: ROIC 13.1% and `fcf_yield_pct`
0.21% are the weakest cash-return figures of any holding outside ABB, and D/E
64.2 with net debt/EBITDA 1.38 is real leverage · Copycat: no usable data — the FI
register returns only two "Gift given" rows (Philip Broadley, 5,735 shares at 0.00
GBP, 2025-12-17), which is a transfer, not a signal in either direction
**STRONGEST CASE FOR:** Valuation's, reinforced by thesis-review being the only
holding it answers **YES** on for "would I buy this today." PEG improved from 1.33
at purchase to 1.14, four consecutive years of revenue growth, margins stable,
dividend intact at a 47.4% payout, and none of the three recorded key_risks has
occurred.
**STRONGEST CASE AGAINST:** Quality's. A 0.21% FCF yield means the trailing cash
generation is negligible relative to the price, and this system cannot see a
multi-year FCF series for any name (Yahoo's legacy cash-flow module exposes only
`netIncome` per year). The valuation case rests on earnings and PEG, neither of
which is cash.
**KEY DISAGREEMENT:** Real but narrow — Valuation and Quality agree on the business
and disagree on whether trailing FCF at 0.21% is a red flag or a fetch artifact
for a pharma with heavy in-period R&D and capex. Neither can settle it without the
company's own cash-flow statement (the `pdf` skill could; it has not been run).
**DATA GAPS:** No `forward_pe` (screen status MISSING for exactly this reason —
the S21 Nordic-coverage asymmetry, now measured at a 33pp forward-P/E coverage gap
Sweden vs US across three consecutive scorecards). No multi-year FCF. Copycat
blind.
**CHAIRMAN CONVICTION:** 6
**WHAT WOULD CHANGE THIS:** The 2026-10-30 earnings print, specifically whether the
17.0% net margin and 6.4% revenue growth hold. That is the recorded break
condition, and it is testable in six weeks.
**PORTFOLIO FIT:** Already the second-largest single position at 12,328 SEK (5.5%
of the book) and 38.3% of the identifiable single-stock sleeve by sector. Adding
concentrates Healthcare further — but Healthcare is not one of the two ACT-rated
buckets; Industrials (55.1%) and Sweden (50.2%) are, and AZN is in neither.
Capital: **verified against this sweep's portfolio output — ISK cash 845.43 SEK,
not enough for one share at 1,541 SEK.** The 14,227.88 SEK sitting in PayPal is
the only source, and it is blocked on P3.
**FINAL CALL:** BUY
**HORIZON:** Long (3y+)
**Execution note:** no idle capital confirmed — blocked on the P3 PayPal conversion
(sixth-plus consecutive sweep unexecuted). Flag for the next contribution if P3
does not clear. Merit and timing are separate; the merit stands.

---

### Other SELL recommendations on current holdings that did not place

**VOLV-B.ST — Defensive voice, SELL, conviction 6. Chairman overrules to HOLD.**
Defensive's evidence is correct and specific: D/E 147.3 and net debt/EBITDA 3.8
are the highest leverage of any holding, the 7.6% net margin is the thinnest, and
the buyer is a cyclical truck manufacturer facing a +1.45% Swedish real policy
rate. I am overruling it for three reasons, each from this sweep's data: (1)
thesis-review reports every metric moved in the thesis's favour — revenue growth
flipped to **+2.7%** from a two-year -13% decline at purchase, PEG 1.49→0.99,
forward P/E 14.6→13.67, consensus now "buy"; (2) the position is six weeks old
against a recorded three-month test window, with the proper re-test due early
November; (3) Copycat's read is that board member Helena Stjernholm's 1,300,000-share
acquisition on 2026-07-27 at ~359–361 SEK is currently 5.7% underwater at today's
339.20 — which at a six-week horizon is not evidence against anything.
**Defensive's leverage point is the reason not to add to Volvo, not the reason to
sell it.** That distinction is the whole call.

**No other voice issued a SELL on a current holding this sweep.** Specifically:

- **INVE-A.ST — the Contrarian voice stood down after four consecutive sweeps of
  wanting to sell.** Its objection was never confidence, it was measurability: a
  holding company at 86% of its 52-week range whose only real valuation metric
  (NAV discount/premium) this system has never obtained (S6). What changed is
  primary evidence, not another voice's opinion — **Jacob Lund bought 1,000
  A-shares at 399.13 SEK on 2026-09-09, five days ago, within 0.1% of today's
  399.50.** That is the first datapoint the Contrarian has ever had suggesting
  somebody who can see the NAV thinks this price is acceptable. It is not proof of
  value and the voice says so. The call moves to HOLD and the pressure moves to
  S6 / decision D-b instead.
- **ATCO-B.ST** — Valuation flagged it expensive (PEG 2.15, trailing P/E 32.08, no
  forward estimate) but issued no SELL, and thesis-review's "would I buy today"
  answer is NO on valuation. This is a no-add, not a sell.
- **ALFA.ST** — one genuinely new Copycat finding worth recording without a call:
  the "10/10 insider buys, zero disposals" signal from the 2026-08-17 review is
  still true but **going stale**. The most recent FI transaction is 2026-04-24
  (Annica Bresky, 553 shares @ 542.00, an acquisition); the bulk of the cluster is
  2023–2024. ALFA's recorded break condition fires on "the pattern breaks with a
  disposal" — no disposal has occurred, so it has not fired. But "still buying"
  and "has not sold in five months" are different statements, and the thesis
  currently leans on the first while the data supports only the second.

---

### What the seven voices produced

| Voice | BUY | SELL |
|---|---|---|
| Fundamental / Quality | NVDA 8, APP 8, V 8, TSM 7 | ABB.ST 6 |
| Valuation | VICI 8, AZN.ST 7, MU 6, FIS 6 | ABB.ST 7, SHB-A.ST 6 |
| Growth / Opportunity | AVGO 7, NVDA 7, APP 7, TSM 7 | SHB-A.ST 6 |
| Defensive / Risk | VRTX 7, CME 7, EG 6, MO 5 | VOLV-B.ST 6 |
| Contrarian / Risk Taker | VICI 7, FIS 6, LULU 5 | none |
| Macro / Regime | AZN.ST 6, EG 6, CME 6 | ABB.ST 6 |
| Copycat / Smart Money | INVE-A.ST 6, SHB-A.ST 5 | ABB.ST 7 |

**Three voice-level notes the Chairman is carrying forward rather than burying:**

1. **Copycat produced only two BUYs, and that is the correct output, not a failure
   to try.** `insider_activity` (SEC) returned `CIK mapping fetch failed: Tunnel
   connection failed: 403 Forbidden` and every ticker marked `skipped: non-US
   ticker`. `insider_activity_fi` covered seven issuers — Handelsbanken, Investor,
   Volvo, Atlas Copco, AstraZeneca, Alfa Laval, ABB — **all of which are
   holdings.** Not one of the 34 `new` candidates has insider data of any kind.
   This voice is currently structurally incapable of contributing to stock
   *selection*; it can only comment on stock *retention*.
2. **Two voices independently declined to use a metric the detector passed.**
   Quality refused TSM's `roic_pct` 183.7% and `fcf_yield_pct` 32.52% as
   implausible for a capital-intensive foundry and rested its TSM case on ROE
   40.0% and net debt/EBITDA -0.77 instead. **Neither figure is in this run's
   suspect list, and both still feed `z_quality` 1.916 and TSM's rank-7 position.**
   This is the second consecutive sweep with the identical finding (see S24's
   2026-09-07 review). A voice compensating for a detector gap is not the detector
   working.
3. **Growth explicitly declined to buy the name its own triage ranked third.**
   SMCI scores `z_growth` 1.743 on 93.2% revenue growth and a 76.3% three-year
   CAGR, with forward P/E 7.53 against trailing 12.30 — and `fcf_yield_pct`
   **-31.31%**, a 5.7% net margin and a 13.4% operating margin. Growth that
   consumes cash at that rate is working capital, not operating leverage. Named
   here because triage narrowing and triage deciding are different things.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens. **Total portfolio
(exposure-class basis): 223,730.67 SEK.**

| Dimension | Rating | Detail |
|---|---|---|
| Asset allocation vs adopted target (80/10/5/0/5) | **WATCH** | Equity 72.37% vs 80% (-7.63pp); cash 11.82% vs 5% (+6.82pp); gold 2.54% vs 5% (-2.46pp); crypto 10.37% vs 10% (on target). Drift is mostly idle cash, not a directional bet. |
| Asset allocation vs `investor_profile.json` reference_targets (85/10/0/5) | **ACT (stale reference)** | The two target sets disagree; reference_targets was never updated for the 2026-09-02 gold carve. Bookkeeping gap, not a portfolio-shape problem. |
| Equity sector concentration | **ACT** | Industrials 55.1% of the identifiable single-stock sleeve; Healthcare 38.3%; Financial Services 6.7%. 80% of the total equity sleeve (Avanza Global + Auto 3) has no sector look-through — confirmed data gap. |
| Geography | **ACT** | Sweden 50.2% of identifiable sleeve, UK 38.3%, Switzerland 11.5%. Same look-through gap. |
| Currency exposure | **UNKNOWN** | No per-holding revenue-currency breakdown fetched. Directionally heavy underlying USD/EUR. |
| Single-position concentration | **WATCH/ACT contextual** | Avanza Global 53.6% of total — technically breaches the >15% rule but is a diversified index fund, not single-company risk. Next largest AZN.ST at 5.5%. |
| Institution concentration | **ACT** | Avanza (ISK) 83.12% (185,970.15/223,730.67), over the 80% cap. Custodial risk on a regulated Swedish broker — lower severity than single-issuer risk, but it crosses. |
| Fee drag | **OK** | ≈187.13 SEK/yr ≈0.084%, well under the 0.4% cap. No fund above 0.5%. |
| Wrapper efficiency | **OK** | All active capital in ISK, under the ~300k allowance (verify with Skatteverket). Only AF residue is the frozen SEB Osteuropafond, 0.25 SEK basis, immaterial. |
| Drawdown-tolerance fit | **WATCH** | S26: -20.62% max drawdown (2019–2026) is inside the -30% tolerance, but that window's worst equity shock was only -19.14% and does not price crypto's own tail (BTC/ETH routinely draw down 50–80%). The 10% crypto sleeve is the specific untested risk driver. |

**Provisional because of `investor_profile.json`:** no TBDs — all fields are
populated. But one genuinely new inconsistency was found this sweep and it makes
the first two rows read against each other: **`investor_profile.json.reference_targets`
(85/10/0/5, adopted 2026-07-27) and `portfolio.json.targets` (80/10/5/0/5,
gold-carved 2026-09-02) now disagree**, because the profile file was never updated
after the gold carve. Per CLAUDE.md's ownership table `portfolio.json` owns
targets, so every live figure in this memo is correct — but the profile file is a
stale copy of a superseded number and should be corrected to 80/10/5/0/5.

**PROPOSED target allocation — proposal only, not written to any file, and not
mine to write.** Portfolio's proposal, carried here for your decision:

| | Current adopted | Proposed |
|---|---|---|
| Equity | 80% | 80% (unchanged) |
| Crypto | 10% | **7%** |
| Cash | 5% | 5% (unchanged) |
| Fixed income | 0% | 0% (unchanged) |
| Gold | 5% | **8%** |

Rationale (portfolio's, quoted in substance): a minimal-touch adjustment
responding to the one specific unvalidated assumption — S26's backtest window
contains no shock large enough to test the -30% tolerance, and crypto is the 10%
of the book most capable of blowing through it on its own (a 60–70% BTC/ETH
drawdown contributes roughly -6 to -7pp to total portfolio drawdown before
equities move at all). It leaves your explicit 2026-07-22 directions (equity >70%
acceptable, fixed income near zero) untouched, and routes the trim into the
crash-hedge instrument already structurally cleared (Xetra-Gold, 0.07%/yr,
physically backed) rather than into bonds. It does **not** invoke the profile's
tighter T3y glidepath bands, because the re-anchor trigger (goal firming up inside
~3 years) has not fired. Contingent on (a) a real stress-tested backtest including
crypto's realistic drawdown distribution, and (b) your direct confirmation, since
it touches standing risk directions you set yourself.

**A correction to the premise this proposal was requested under:** the scheduled
prompt asserted `investor_profile.json.reference_targets` "are null." They are
not, and have not been since 2026-08-03. This proposal is therefore a
reassessment of an existing adopted 80/10/5/0/5 against horizon, drawdown and
glidepath — not a first target derived from nothing.

---

## 5. Headline calls

1. **SELL ABB.ST, 4 shares, ~3,706 SEK — fourth consecutive sweep.** Valuation
   (forward P/E flat vs trailing despite 14.2% growth) and Copycat (~51,255 shares
   disposed by two insiders in three weeks) both hold; thesis-review independently
   confirms BROKEN from current data. Or decline it explicitly and close D-a.
2. **BUY VICI with the ABB proceeds, ~15 shares.** Structurally linked — no ABB
   sale, no VICI buy. It is the only Top-5 name that answers both ACT-rated
   concentrations (Industrials 55.1%, Sweden 50.2%). **Macro dissents at
   conviction 4 and the FOMC decision lands tomorrow** — see timing collisions.
3. **The open SHB-A.ST SELL is retired, not executed.** One share, 149.75 SEK,
   0.07% of the book. Valuation's bearish read is recorded and I believe it; the
   position cannot move anything either way, and Copycat's 1.85M-share
   counter-evidence cannot be resolved at this size either. Decide nothing here.
4. **Get Investor A's NAV discount/premium (decision D-b, ~10 minutes).** Fifth
   consecutive sweep this single missing number has blocked a real call. This
   sweep it stopped being one silenced voice and became a genuine two-sided
   disagreement — and then the Contrarian stood down on new insider evidence
   (Jacob Lund, 1,000 shares @ 399.13, 2026-09-09), which resolves nothing, it
   just moves the deadlock.
5. **Decide the crypto sleeve (decision D-c).** Crypto is at 10.37% against a 10%
   target — on target, so no trim is indicated under the *current* target. The
   question is only whether you adopt the proposed 7%. Macro's input is pointed:
   crypto Fear & Greed moved from 29 ("Fear") to **57 ("Greed")** in three weeks
   while ETH ran +33.6% over 30 days with the dollar index at 118.07. That
   combination is where momentum should not be read as confirmation.

---

## 6. Open actions vs open decisions

### Actions — things to go do

| ID | Action | Status |
|---|---|---|
| **P3** | Convert the full PayPal balance (14,227.88 SEK at this sweep's FX) inside PayPal at the accepted 4% worst-case spread, then route the SEK into the ISK. | decided — pending execution, **sixth-plus consecutive sweep.** This is now the binding constraint on the AZN.ST BUY (ISK cash 845.43 SEK vs a 1,541 SEK share price) as well as the original fee-drag rationale. |
| **P9** | Delete the phantom AZN OPENING row in the Excel Transactions tab (the workbook's own README names this bug). | open — blocks nothing, re-flags every sweep until fixed at source. |
| **P10** | Confirm: was there one 5,000 SEK deposit or two? (`transactions.csv` carries both 2026-08-17 and 2026-08-22; the real Avanza export shows only 2026-08-22.) | open — real money, not merged without your confirmation. |
| **S6** | Get Investor A's NAV discount/premium from IR or the quarterly PDF and record it in `data/company_profiles/INVE-A.ST.json`. ~10 minutes. | open — blocked a real call on five consecutive sweeps. |
| **S27** | Fix the scheduled task's stored prompt: drop the Handelsbanken-wrapper framing (closed 2026-07-07/2026-08-03) and rewrite the reference_targets line. Outside any agent's write access. | open — **fourth confirmed occurrence today.** See section 9. |
| *(new, small)* | Correct `investor_profile.json.reference_targets` from 85/10/0/5 to match `portfolio.json.targets` at 80/10/5/0/5. One line. | new this sweep — portfolio lens found it; see section 4. |
| *(new, small)* | Promote APP to `data/watchlist.json`. Rank 1 of 614 for four consecutive runs and still arriving as an unpromoted `new` row. | new this sweep. |

### Decisions — forks that need you to pick

**D-a — where the ABB proceeds go (~3,706 SEK), if the sale happens.**
- *Option 1 — VICI (this memo's call).* Answers both ACT concentrations at once
  (Real Estate 0%, US 0% direct); 7.41% yield; against it, the most rate-sensitive
  name in the set with an FOMC decision tomorrow.
- *Option 2 — gold tranche 2.* Gold is undershooting at 2.54% vs a 5% target;
  portfolio computes 5,497 SEK needed to reach 5%, so 3,706 SEK covers two-thirds
  of the gap. Lowest-friction, zero analysis risk, no return thesis.
- *Option 3 — do not sell ABB.* Closes D-a and the SELL together. Costs nothing
  measurable so far (+0.2% since the first call), and stops four sweeps of
  re-litigation.

**D-b — Investor A's unmeasurable valuation (S6).**
- *Option 1 — get the NAV number (~10 min).* Makes the holding testable for the
  first time and settles a disagreement that has now run five sweeps.
- *Option 2 — sell on absence of evidence.* Defensible in principle; harder this
  sweep, because an insider bought 1,000 shares five days ago within 0.1% of
  today's price.
- *Option 3 — keep holding and stop re-flagging it.* Legitimate, and cheaper than
  either of the above — but it means accepting a position you have explicitly
  recorded as not properly testable.

**D-c — the crypto sleeve.**
- *Option 1 — adopt the proposed 7% target and trim ~7,539 SEK, entirely from
  BTC0E.AS.* ISK-wrapped so the sale is tax-free; must not come from the ETH
  wallet, where P1 (no cost basis) makes any disposal unreportable. Costs upside if
  crypto keeps running.
- *Option 2 — wait for S26's real shock-window backtest before deciding.* Honest,
  but the sleeve keeps running at 10.37% in the meantime and this is the third
  sweep the question has been deferred.
- *Option 3 — keep 10% and change nothing.* Crypto is on target; this is only a
  live question because the drawdown tolerance backing that target was never
  tested against a real shock.

---

## 7. Cost of being wrong

| Headline call | If it's wrong | Realistic SEK downside | Recoverable? |
|---|---|---|---|
| SELL ABB.ST (~3,706 SEK) | ABB re-rates on the 2026-10-20 print and you forgo the move | ~741 SEK on a 20% upward re-rating | Yes — the position can be re-established; ISK, so no tax friction either way |
| BUY VICI (~3,706 SEK, 15 sh) | Macro is right; the 10y stays at 4.95%+ and the REIT de-rates further | ~1,112 SEK on a further 30% drawdown | Yes — and the 7.41% yield offsets roughly 274 SEK/yr while you wait. Not permanent capital loss unless a tenant fails, which is a different risk than the rate risk |
| NO ACTION on SHB-A.ST | Valuation is right and the share halves | **~75 SEK** | Trivially. This number is the entire argument for retiring the call |
| HOLD-WATCH APP | The quality case is right and it re-rates while you watch | 0 SEK of capital at risk; the cost is foregone upside, which this system will not quantify because it does not produce price targets | n/a — no capital committed |
| BUY AZN.ST (1 sh, 1,541 SEK, if P3 clears) | Margins or revenue growth break at the 2026-10-30 print | ~308 SEK on a 20% pharma drawdown | Yes |
| D-c: trim crypto 10%→7% | Crypto rallies after the trim | ~3,770 SEK foregone on a 50% subsequent move in the trimmed 7,539 SEK | Yes |
| D-c: **don't** trim | A 60–70% BTC/ETH drawdown lands | ~13,400–15,600 SEK (portfolio's -6 to -7pp on 223,730.67 SEK) | Yes in time, but this is the larger and less-tested side, and it is the asymmetry that makes D-c a real decision rather than a preference |

Every call in this memo has a stated downside. Nothing was included whose downside
could not be stated.

---

## 8. Timing collisions

`calendar` ran (`data/cache/calendar/20260914-events.json`, 45-day window) and two
flags land on this memo's calls.

- **FOMC 2026-09-15/16 — tomorrow and the day after.** This collides directly with
  the **VICI BUY**. VICI is the most rate-sensitive name in the focus set (net
  debt/EBITDA 4.82, 7.41% yield, priced off the 10y at 4.95%), and Macro's
  dissent is entirely about the policy path. A BUY sized today executes into the
  decision. This does not change the call; it means the entry price is a coin flip
  over 48 hours, and if you would rather not take that, waiting two days costs
  nothing — the thesis is Medium-horizon.
- **Riksbank rate decision + Monetary Policy Report 2026-09-24 (10 days).** Sweden
  runs a +1.45% real policy rate (1.75% nominal vs SE CPI 0.3%), genuinely
  restrictive and tighter than the US read. That is the specific mechanism behind
  Macro's caution on the Nordic industrial/financial sleeve — Volvo, Atlas Copco,
  Alfa Laval, ABB, Handelsbanken, Investor, i.e. 55.1% of the identifiable
  single-stock sleeve. A cut on 2026-09-24 loosens that constraint directly and is
  the single observable most likely to change Macro's read inside two weeks. The
  **ABB SELL** sits inside this window; a dovish surprise would lift the whole
  sleeve including the name being sold. It does not change the call (the case is
  valuation, not cycle), but it is the honest counter-timing.
- **No imminent earnings collision.** All six SEK-listed holdings report 2026-10-20
  to 2026-10-30 — ABB.ST 10-20, SHB-A.ST 10-21, ATCO-B.ST 10-22, VOLV-B.ST 10-23,
  ALFA.ST 10-27, AZN.ST 10-30. Five to six weeks out, none inside seven days. Any
  trade sized this sweep on these names should be sized knowing the print is
  coming.
- **Data gap, not an absence:** the fetch returned **no earnings date for INVE-A.ST
  or BTC0E.AS**. That is a missing field, not a confirmed quiet period.

---

## 9. Data gaps for `meta` — surfaced, not fixed

1. **No 52-week high/low in the candidates CSV.** `pct_52w_range` is present; its
   endpoints are not. This directly capped a Top-5 conviction this sweep — APP at
   "4% of range" with a flat four-sweep price is uninterpretable without the high.
   The snapshot already carries `52w_high` and `52w_low` per ticker, so this is a
   scout output change, not a new data source. Highest value-per-effort item on
   this list.
2. **Two different "% of 52-week" conventions in circulation, again.** The
   candidates CSV gives INVE-A.ST `pct_52w_range` = 86.0 ((price-low)/(high-low));
   thesis-review gives 95.5% (price/high). Both are correct and they are different
   metrics, but they appear in the same memo reading like a contradiction. S11
   closed a genuine version of this on 2026-08-11. This is not that bug — it wants
   a `data/definitions.json` entry naming both, not a code fix.
3. **No EV/EBITDA or EV/EBIT anywhere in the system.** Named as a standing gap in
   the Council definition; it bit twice this sweep, on VICI (a REIT valued on P/E
   is valued on the wrong denominator — no FFO/AFFO either) and on FIS
   (net debt/EBITDA 5.82 makes the 5.86x P/E much less cheap than it looks).
4. **Copycat coverage is structurally broken for stock selection, from two causes
   at once.** `insider_activity` returned `CIK mapping fetch failed: 403
   Forbidden` (S20, closed 2026-09-07 as confirmed-unreachable — this is the
   fourth confirmation, no action needed). Separately, **only the eight portfolio
   tickers were submitted to the fetch at all**, so not one of the 34 `new`
   candidates would have been covered even with a working gateway. That is S25's
   scope gap, which was closed as "superseded by S20." The closure reasoning was
   right for that sweep, but the scope half is still unfixed and will bite the
   moment a gateway opens. Worth a note against S25's closed entry rather than a
   reopening.
5. **S24's plausibility detector has the same coverage hole as last sweep.** TSM's
   `roic_pct` 183.7% and `fcf_yield_pct` 32.52% are not in this run's suspect list,
   and both still feed `z_quality` 1.916 and rank 7. Identical finding to
   2026-09-07 — two consecutive sweeps, same metric family, same name. The
   detector catches `price_to_book` tails (ABB 106.60, ASML 1431.30) and
   `revenue_growth` tails (INDU-C 11.98x, SNDK 3.72x, MU 3.46x) but not
   `roic_pct`/`fcf_yield_pct` tails. Asymmetric calibration, now twice evidenced.
6. **Zero mid-cap or small-cap exposure anywhere — and the funnel mirrors it.**
   Portfolio's finding: all 7 individual holdings are large-cap, and **none of the
   14 focus=Y candidates fall in the $2–10B mid-cap or <$2B small-cap bands
   either.** The closest are EG ($14.25B) and FIS ($19.67B). This is a screening-criteria
   question for scout, not a legacy portfolio problem.
7. **Discovery: the top-15 is frozen across four consecutive runs.** APP/SNDK/NVDA
   at 1/2/3 in all four. Exactly one first-seen name this sweep (LULU), and three
   dropped out — including VOLCAR-B.ST, last sweep's only genuine multi-insider
   Swedish buy signal and S21's worked example, which left the set without
   resolution. Status is VALID so this is a watch item, not a failure, but it is
   now four runs old.
8. **New, small S-item candidate:** `investor_profile.json.reference_targets`
   (85/10/0/5) vs `portfolio.json.targets` (80/10/5/0/5). The 2026-09-07 session
   logged this as "considered, not opened" and recommended a direct one-line fix;
   that fix was not applied, and this sweep's portfolio lens found it
   independently and rated the row **ACT**. Second occurrence of the same
   uncorrected inconsistency — that is different evidence from the first.
9. **S27 — fourth confirmed occurrence, and `meta` should update S27's evidence
   rather than open a new item.** The scheduled prompt that launched this sweep
   again asserted (a) that the Handelsbanken wrapper question is unresolved and
   that this memo "MUST open with it," and (b) that `reference_targets` are null.
   Both are false, both were false on 2026-08-31 and 2026-09-07, and both are the
   *identical two lines* S27 already documents. The wrapper question closed
   2026-07-07/2026-08-03 (CLAUDE.md: "1. Account wrapper efficiency — DONE
   2026-08-03") and this memo therefore does **not** open with it. The
   reference_targets are non-null and have been since 2026-08-03. Corrected here,
   as in the previous two sweeps. The pattern is now self-mitigating four times
   running, which is the good news; the bad news is that three consecutive memos
   have spent a section correcting a stored text file nobody has edited.

---

## 10. Learning notes

- **"An insider bought" is four different sentences.** This sweep's FI data
  contains all four shapes under one word. *Investor A:* seven different people
  buying across seven months — 338.38, 340.50, 344.90, 361.30, 377.50, 387.30,
  399.13, 411.55 SEK — at varied sizes on varied dates, monotonically rising, zero
  disposals. That is many independent people deciding separately, which is the
  strongest shape. *Handelsbanken:* one person, one day, ten fills, 1.85M shares,
  all marked "closely associated" — enormous, but it is an entity moving, not a
  person betting, and the size makes it look stronger than it is. *ABB, May 2026:*
  six board members buying 917–1,948 shares each **on the same date at the
  identical price of 78.42 CHF** — that is a fee allotment wearing an acquisition
  label, and it should be read as zero signal. *Atlas Copco:* an option exercise at
  138.80 and a same-day disposal of the identical 79,442 shares at 199.50 — also
  zero signal, in both directions. Sorting by "Nature of transaction" would have
  got three of these four wrong.
- **A BUY call that gets cheaper while unexecuted is not automatically a better
  BUY.** VICI fell 6.7% (26.51 → 24.73 USD) over the four sweeps this call has
  been open, and every business metric held. It is tempting to read that as a free
  improvement in the entry. But the *reason* it fell — the US 10y at 4.95% — is
  exactly the reason Macro argues against it. A falling price is evidence about
  what the market believes, and here the market and this memo's own Macro voice
  believe the same thing. The entry improved; the disagreement did not.
- **A forward P/E below a trailing P/E is a fact about expectations, not about
  value.** MU reads 6.25x forward against 22.02x trailing, SNDK 6.17x against
  22.12x — the market expects earnings to multiply. LULU reads the other way,
  10.92x forward against 8.15x trailing — the market expects earnings to fall, and
  has said so in the number. Neither tells you whether the expectation is right,
  and for the memory names both PEGs rest on `revenue_growth` figures scout has
  flagged as suspect (3.46x for MU, 3.72x for SNDK — Yahoo reporting multiples as
  percentages). The forward/trailing *gap* is real and usable; the PEG built on
  top of it is not.
- **Deciding well about something that cannot matter is a cost.** The
  Handelsbanken SELL was analytically sound and has been carried for two sweeps.
  The position is 0.07% of the portfolio. Retiring the call is not a concession
  that the analysis was wrong — it is recognising that a system with finite
  attention spent two Council slots, two conviction scores and a ledger row on
  150 SEK, while a 3,706 SEK SELL and a 14,228 SEK funding decision sat unactioned
  beside it.

---

*Decisions recorded in `data/picks/2026-09-14-picks.csv`.*
