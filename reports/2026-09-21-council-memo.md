# Council Memo — 2026-09-21

*This is structured synthesis of your own agents' analysis over data fetched this
session. It is not licensed investment advice. Every number below traces to a file
written today, or is labelled user-relayed.*

---

## Blocking item first: S26, not the Handelsbanken wrapper

Per CLAUDE.md's blocking-question rule, this memo opens with the one open item that
genuinely makes a conclusion here untrustworthy. It is **S26 — the drawdown backtest
window contains no real shock**.

This sweep's `portfolio` lens (§8) is explicit: the adopted 80/10/5/0/5 target
*"holds in principle; the drawdown-tolerance claim underneath it does not."* Two
carried-forward reads disagree — a real backtest at −20.62% over 2019–2026 whose own
worst equity shock was only −19.14% (so it never tested a −30%-scale event), versus a
prior sweep's stress *arithmetic* (explicitly not a backtest) at roughly −36%. Neither
was refreshed today.

What that actually blocks tonight: **any claim that adding high-beta names respects the
stated −30% tolerance.** The three top-ranked names in this sweep's funnel carry betas
of 2.488 (APP), 2.217 (NVDA) and 2.222 (MU), and SNDK has no beta field at all. I am
not recommending any of them, and S26 is part of why. It also keeps open decision D-c
(crypto sizing) genuinely undecidable with numbers, three sweeps running.

Two corrections to the stored prompt that launched this sweep, so they do not distort
the record (this is the **fourth** confirmed occurrence of the same drift, tracked as
S27 — `meta` handles it, not this memo):

1. The Handelsbanken wrapper question is **not** open. It was resolved 2026-07-07 /
   2026-08-03; all capital is in the ISK; `portfolio.json.open_structural_questions`
   has been a pointer to `OPEN_ITEMS.md`, not a live list, since 2026-08-03. This memo
   does not open with it.
2. `investor_profile.json.reference_targets` are **not** null. They were adopted
   2026-07-27 and written 2026-08-03; `portfolio.json.targets` carries the current
   80/10/5/0/5 after the 2026-09-02 gold carve. The standing task was done correctly
   by the `portfolio` lens as a *review* of the adopted target (its §8), used below —
   no target is proposed from scratch.

P1 (ETH cost basis) is open but not blocking tonight: no ETH sale is proposed, so no
tax math depends on it.

---

## 1. Position report

Snapshot: `20260921T060913.json` · previous: `20260914T060927.json`

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 155.05 | +3.5% | +20.0% | 99% | 155.05 | fetched |
| Investor A (stock) | 401.00 | +0.4% | +38.2% | 87% | 2,005.00 | fetched |
| Volvo B | 337.80 | -0.4% | -8.1% | 72% | 4,391.40 | fetched |
| Atlas Copco B | 172.45 | -1.2% | -4.9% | 75% | 4,656.15 | fetched |
| AstraZeneca | 1,626.50 | +5.5% | +5.8% | 47% | 13,012.00 | fetched |
| Xetra-Gold (physically-backed gold ETC, ISIN DE000A0S9GB0) | no data | no data | -0.0% | - | 5,689.22 | user-relayed |
| Alfa Laval | 556.00 | +1.9% | -3.2% | 79% | 5,004.00 | fetched |
| ABB | 948.40 | +2.4% | +0.2% | 74% | 3,793.60 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| Valour Bitcoin Zero SEK (certificate, ISIN CH0585378661) | 47.29 | +0.0% | -22.9% | - | 7,093.80 | fetched |
| ETH (self-custody wallet) | 26,147.81 | +7.8% | no data | - | 13,122.28 | fetched (CoinGecko, via sek_per_eur) |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high.*

**Data-quality note carried from the position-report lens:** the BTC0E.AS row
(7,093.80 SEK) uses Yahoo's known-bad `BTC0E.AS` feed (47.29 EUR, ~7x off,
52w-high = 52w-low). Use the broker-confirmed **11,031 SEK** for any total or drift
math, as the `portfolio` lens does. The apparent ~37% weekly drop in that row is a
feed artifact, not a move.

**What moved, and whether it mattered.** AZN.ST +5.5% was the week's real move and it
cuts both ways: it is the largest individual holding (5.77% of total capital) and the
move is thesis-consistent, but it also erodes the entry discount the thesis rests on —
AZN's `valuation_reason` cites being "~20% off its 52-week high" and it now sits 47% into
its range, ~15.5% below the high. That is the observable that will eventually retire the
BUY. SHB-A.ST +3.5% puts it at 99% of its 52-week range on revenue of −3.8% YoY — the
"good upside" the user originally cited is fully captured, exactly as the WEAKENING status
says; the position is one share (155 SEK), so this remains a finding without a trade.
ABB.ST +2.4% does not contradict the SELL — the call is valuation-based, and a higher
price raises the proceeds. ETH +7.8% takes crypto to 11.24% of the investable base,
above its 10% target, against a Fear & Greed reading of 70 ("Greed"). Index funds:
Avanza Global and Auto 3 carry no fresh NAV this sweep; nothing to read.

---

## 2. Scout health

```
Universe    624
Fetched     622  (cache 0, new 625, failed 3)
Ranked      613
Candidates  74   (holdings 9, watchlist 30, new 35)
Focus       23
Screened    74
Passed      39
Missing     17
Failed      18
Status      VALID
```

**Reading:** the funnel ran and is VALID, and **35 of 74 candidate rows are `new`** —
discovery is genuinely producing, which answers the standing worry directly. But the
production is all in the tail: ranks 1–11 this sweep (APP, SNDK, NVDA, MU, MA, V, TSM,
INDU-C.ST, VICI, INVE-A.ST, TPL) are the same eleven names as 2026-08-31, and APP/SNDK/
NVDA have held ranks 1/2/3 for five consecutive runs (`data/candidate_history.csv`).
Discovery works at the margin, not at the head of the funnel. Separately, 35 of 74 rows
screen MISSING or FAILED (47%) and the MISSING block is again dominated by Swedish
names lacking `forward_pe` or `debt_to_equity` — INVE-A.ST, INDU-C.ST, SHB-A.ST,
SWED-A.ST, SEB-A.ST, LUND-B.ST, ERIC-B.ST, ASSA-B.ST, LATO-B.ST, BURE.ST — i.e. S21's
measured coverage asymmetry, fifth sweep running, still shaping which names can clear a
screen at all.

---

## 3a. The seven voices — independent passes

Each voice triaged its own columns across all 74 rows before writing, and drafted
without seeing the others. Where a voice pulled in a name outside `focus=Y`, or argued
against its own screen flag, it says so.

### Voice 1 — Fundamental / Quality

*Triage (`z_quality`):* APP 2.571, SNDK 2.544, MU 2.332, MA 2.231, V 1.939, TSM 1.919,
INDU-C.ST 1.906, INVE-A.ST 1.826, TPL 1.823, MO 1.794.

**BUY — V (Visa), conviction 8.** ROIC 41.5%, ROE 61.2%, net margin 50.8%, operating
margin 66.1%, net debt/EBITDA 0.32, revenue +14.4% on a 10.9% three-year CAGR. It is the
only name in the set combining >40% ROIC with double-digit growth and no balance-sheet
strain. Moat and capital-allocation quality are in no fetched field — reasoning
qualitatively: a two-sided network with rising nominal-spend leverage.
*Key risk:* regulatory intervention in interchange compressing the take rate — a
political event, invisible in any metric until after it lands.
*Invalidated by:* ROIC below ~30%, or revenue growth at mid-single digits for two prints.
*Missing:* no EV/EBITDA; no US insider data this sweep; institutional ownership not fetched.

**BUY — TSM, conviction 8.** ROE 40.0%, net margin 49.9%, operating margin 60.3%, net
debt/EBITDA −0.77 (net cash), revenue +36.0% on an 18.9% three-year CAGR. Stated plainly:
I **discard** this row's `roic_pct` 183.7% and `fcf_yield_pct` 32.42% as implausible for a
capital-intensive foundry. They are *not* in the suspect column (S24, third consecutive
sweep on this exact name) and they are feeding its z_quality of 1.919 and its rank-7 slot.
My case rests on ROE and net debt/EBITDA only.
*Key risk:* single-island manufacturing base plus customer concentration among a handful
of fabless designers — neither quantifiable here.
*Invalidated by:* operating margin below ~45% while capex intensity rises.
*Missing:* two of four headline quality inputs unreliable; no insider data.

**BUY — MA (Mastercard), conviction 7 — pulled back in against its screen FAIL.** The FAIL
is `debt_to_equity` 439.583% > 250%, which for Mastercard is a buyback-driven negative-equity
artifact, not distress: net debt/EBITDA is 0.59. Underneath it sit ROIC 56.1%, ROE 241.2%,
margins 46.3/61.1, revenue +14.1% on a 13.8% three-year CAGR.
*Key risk:* the same take-rate regulation as V, plus negative book equity leaving no
cushion if a large litigation settlement lands.
*Invalidated by:* net debt/EBITDA above ~2.0, or revenue growth below 8%.
*Missing:* as V.

**BUY — ATCO-B.ST (holding), conviction 6.** ROIC 39.7%, ROE 25.7%, operating margin 20.6%,
net debt/EBITDA 0.50 — the best business among current holdings on every capital-return
field, and ttm revenue +9.1% confirms FY2025's −4.8% was a dip. This is a business-quality
verdict only; the price objection belongs to Valuation and I expect it to disagree with me.
*Key risk:* short-cycle industrial orders turning — compressor and vacuum demand is
capex-linked, and the 2026-10-22 print is the test.
*Invalidated by:* ttm revenue growth turning negative again.
*Missing:* `forward_pe` MISSING (S21) — no forward view on the highest-quality holding.

**BUY — APP (AppLovin), conviction 6.** ROIC 65.5%, operating margin 77.7%, net margin
64.6%, revenue +52.8% on a 24.8% three-year CAGR, net debt/EBITDA 0.09 — the strongest
pure quality profile among 613 ranked names, and the funnel's #1 for five consecutive runs.
Held at 6 rather than 9 because ROE 203.7% is leverage-inflated (D/E 111.13) and because
the price sits at 5% of its 52-week range, which no quality field explains.
*Key risk:* a single advertising platform's algorithm or an ad-market slowdown;
advertiser concentration in mobile gaming is not measurable here.
*Invalidated by:* operating margin below 60%, or net debt/EBITDA above 1.5.
*Missing:* S29 — no 52-week endpoints, so the drawdown behind "5% of range" is invisible.

**SELL — ABB.ST, conviction 7.** ROIC 20.6% looks acceptable until you reach the cash: FCF
yield 0.09%, FCF/revenue ~4.4%. A business converting 4% of revenue into owner cash while
its forward multiple sits *above* trailing is failing on earnings quality.
*Key risk of being wrong:* FCF here is trailing-only (Yahoo's legacy module exposes only
`netIncome` per year), so a capex-timing effect cannot be excluded.
*Invalidated by:* FCF/revenue above ~8% in the next annual report.

**Considered and declined:** MU and SNDK — operating margins of 80.4% and 78.5% are
peak-memory-cycle margins, not evidence of a durable franchise, and both carry
suspect-flagged revenue growth (345.7%, 371.6%) withheld from scoring. INVE-A.ST and
INDU-C.ST — a holding company's operating quality cannot be graded from these fields at
all (S6); INDU-C's 99.3% "margin" and 1198% "revenue growth" are the same artifact, the
latter suspect-flagged.

### Voice 2 — Valuation

*Triage (`z_value`):* CMCSA 1.799, CHTR 1.791, FIS 1.771, ALL 1.724, EG 1.709, FISV 1.643,
BURE.ST / DOM.ST 1.490, CORE-B.ST 1.482, MEKO.ST 1.408, AFRY.ST 1.374, INDU-C.ST 1.297,
INVE-A.ST 1.173, EXE 1.152, EIX 1.081, BALD-B.ST 0.846, MKC 0.816, VICI 0.760.

**BUY — VICI, conviction 8.** 9.19x trailing / 7.93x forward, 7.76% dividend yield, 67.5%
net margin, revenue +5.7% on a 15.5% three-year CAGR, priced at 4% of its 52-week range,
screen PASS. What separates it from CMCSA and CHTR is that the cheapness is not
accompanied by deterioration in any fetched field. **Approximation flagged:** this system
computes no EV/EBITDA, so I am approximating enterprise value from net debt/EBITDA 4.82 —
which is high, and I am not quoting a multiple the system did not compute.
*Key risk:* a rising 10-year raises the discount rate and the refinancing cost together;
REIT equity has no protection from that.
*Invalidated by:* a dividend cut, or net debt/EBITDA above ~6.
*Missing:* no FFO, no AFFO, no EV/EBITDA, no lease-coverage data — the two metrics REITs
are actually valued on do not exist here.

**BUY — TSM, conviction 7.** PEG 0.83, forward 19.8x against trailing 32.5x on 36% growth,
with net cash. Background knowledge, labelled as such: leading-edge foundry peers have
typically traded 25–35x trailing, so 19.8x forward on this growth is a discount to the
sector's own norm rather than to the market's.
*Key risk:* the forward multiple embeds consensus AI capex continuing; a flat 2027 order
book reprices "cheap" instantly.
*Invalidated by:* forward P/E rising above trailing.
*Missing:* no analyst-revision data of any kind.

**BUY — CMCSA (Comcast), conviction 6.** Trailing 7.29x, forward 6.35x, FCF yield 15.74%
(the largest in the focus set), dividend 5.80%, 14% of range. At 6.4x forward, even zero
growth clears a reasonable hurdle. Against: revenue is −1.2% and the PEG of 142.98 is
suspect-flagged — a near-zero-growth denominator artifact, not a real PEG, and I am not
reasoning from it. I am buying a declining business at a price that may already assume
worse decline.
*Key risk:* broadband subscriber losses accelerating; no subscriber data is fetched.
*Invalidated by:* FCF yield below ~10%, or revenue decline steepening past −3%.

**BUY — AZN.ST (holding), conviction 6.** PEG 1.20, improved from 1.33, at 47% of range.
Background knowledge, labelled: large-cap pharma typically trades 15–20x trailing, so the
raw 24.9x is a premium while the growth-adjusted figure is not.
*Key risk:* the 0.19% FCF yield means the earnings are not currently cash.
*Invalidated by:* PEG above 1.6, or the price returning within 5% of its 52-week high
without an earnings step-up.
*Missing:* `forward_pe` MISSING in all five runs on record (S21).

**BUY — FIS, conviction 5.** PEG 0.19, forward 5.32x, FCF yield 14.44%, 3% of range,
screen PASS. Held deliberately low: revenue is +29.1% ttm against a −9.8% three-year CAGR,
which is a divestiture pattern rather than growth, and I cannot separate
cheap-despite-quality from cheap-for-a-reason. Net debt/EBITDA 5.82 is high.
*Key risk:* the leverage on a shrinking three-year revenue base.
*Invalidated by:* net debt/EBITDA above 7, or ttm growth reverting to the three-year trend.
*Missing:* margins and D/E both absent from this fetch for this name.

**SELL — ABB.ST, conviction 7.** Forward 36.53x *above* trailing 35.97x on 14.2% revenue
growth, screen FAIL, and its `price_to_book` of 109.9 is suspect-flagged and unusable
(use the FX-corrected ~11.7x in `data/company_profiles/ABB.ST.json`). There is no margin
of safety on any read available to me.
*Invalidated by:* forward falling decisively below trailing.

**SELL — ATCO-B.ST, conviction 5.** Trailing 31.33x, PEG 2.09, 75% of range. Background
knowledge, labelled: the industrials norm is mid-teens to low-20s. Quality is not in
dispute; price is.
*Invalidated by:* PEG below 1.5.

**Cheap for a reason, explicitly not picks:** CHTR (3.34x but D/E 441.6% on −1.7% revenue),
EXE (−10.6% revenue, forward above trailing), EIX, AFRY.ST, HM-B.ST, ERIC-B.ST, EG,
BETS-B.ST (forward 62.6x against trailing 9.0x — the steepest deceleration in the set).
**No verdict possible:** INVE-A.ST, INDU-C.ST, BURE.ST, LUND-B.ST — holding-company
accounting artifacts, S6.

### Voice 3 — Growth / Opportunity

*Triage (`z_growth`):* NVDA 1.887, AVGO 1.762, SMCI 1.742, APO 1.729, AXON 1.500,
DASH / FIX 1.496, GPN 1.474, FANG 1.472, LLY 1.461, APP 1.425. *Forward P/E below
trailing (the market pricing earnings growth):* MU 6.49 vs 22.94, SNDK 6.77 vs 24.27,
TPL 4.82 vs 45.04, NVDA 14.17 vs 28.10, APP 14.69 vs 23.70, VOLV-B.ST 13.37 vs 18.90.

**BUY — NVDA, conviction 8.** Revenue +105.9% on a 100.0% three-year CAGR, net margin
63.7%, PEG 0.47, forward 14.17x against trailing 28.10x, net cash (−0.12). A
forward/trailing gap that wide on a 106%-growth name is the exact signal this lens is
for, and the forward multiple is below the broad market's.
*Key risk:* hyperscaler capex digestion — a handful of customers deferring two quarters
breaks the forward number, and this system fetches no order-book, backlog or
earnings-revision data.
*Invalidated by:* forward P/E rising above trailing, or growth decelerating below ~40%.
*Missing:* no TAM, no revisions, no market-share data — growth here means *measured*
growth; the catalyst commentary above is qualitative and labelled.

**BUY — TSM, conviction 7.** +36.0% on an 18.9% three-year CAGR — a lower rate than NVDA
from a far larger base, with the leading-edge monopoly position and a 19.8x forward.
*Key risk:* the same AI-capex dependency, one step down the supply chain.
*Invalidated by:* revenue growth below 15% for two consecutive prints.

**BUY — APP, conviction 6.** +52.8% revenue on a 24.8% three-year CAGR *with* a 77.7%
operating margin — growth and operating leverage together, PEG 0.67. Held at 6: at 5% of
its 52-week range the market is discounting this growth hard, and with no revision or TAM
data I cannot adjudicate who is right.
*Key risk:* advertising demand is the single input and it is cyclical.
*Invalidated by:* revenue growth below 25%, or operating margin below 65%.

**BUY — VOLV-B.ST (holding), conviction 5 — pulled in.** Forward 13.37x below trailing
18.90x, PEG 0.97, and ttm revenue growth has turned positive (+2.7%) after FY23–25 ran
552.8B → 526.8B → 479.2B. That is an inflection, which is what this lens exists to catch.
Held at 5 because the three-year CAGR is +0.4% — one positive ttm reading is thin.
*Key risk:* the truck cycle rolling over before the recovery is confirmed; D/E 147.35.
*Invalidated by:* the 2026-10-23 print showing revenue back in decline.

**SELL — ABB.ST, conviction 5.** 14.2% revenue growth that is not reaching earnings. The
forward/trailing inversion says the growth is being handed back in margin, which makes
this a growth story only in the revenue line.
*Invalidated by:* operating margin expanding at the 2026-10-20 print.

**SELL — SHB-A.ST, conviction 4.** Revenue −3.8%, `z_growth` −1.278 — the worst growth
profile of any holding — with forward above trailing. Noted as immaterial at one share.
*Invalidated by:* two consecutive quarters of positive revenue growth.

**Explicitly declined, with reasons:** MU and SNDK, despite ranks 4 and 2 — their revenue
growth figures (345.7%, 371.6%) are suspect-flagged and withheld, SNDK's growth lens has
only 1 of 4 fields, and a forward P/E collapsing to 6.5x/6.8x is a memory-cycle earnings
spike, not growth. SMCI — z_growth 1.742 but FCF yield −32.12%, i.e. growth funded by cash
burn. AXON, DASH, FIX — the growth is real; trailing multiples of 185x, 101x and 40.7x are
the problem.

### Voice 4 — Defensive / Risk

*Triage (`beta`, `de_ratio`, `net_debt_to_ebitda`, `z_defensive`):* lowest betas — SAAB-B.ST
0.033, ALL 0.150, AZN.ST 0.205, BETS-B.ST 0.216, JNJ 0.235, CME 0.275, EG 0.277, ABBV 0.281,
VRTX 0.320, KO 0.342. Lowest leverage — BURE.ST 0.008 D/E, TPL 1.077, SNDK 1.277, ASML 9.092,
VRTX 9.767.

**BUY — VRTX (Vertex), conviction 7 — pulled in from outside `focus=Y`.** Beta 0.320, net
debt/EBITDA −1.15 (net cash), D/E 9.77, net margin 35.0%, revenue +12.5% on a 10.4%
three-year CAGR, screen PASS. The scenario I am pricing is a growth de-rating with rates
staying high; the names that survive it hold net cash and sell something non-discretionary.
This is the only candidate combining net cash, sub-10 D/E, sub-0.4 beta and double-digit
growth.
*Key risk:* single-franchise concentration in cystic-fibrosis therapies — a pipeline or
competitive event is binary and no pipeline data is fetched.
*Invalidated by:* net debt turning positive, or revenue growth below 5%.

**BUY — MO (Altria), conviction 6.** Beta 0.494, net margin 39.0%, operating margin 76.1%,
6.39% dividend, 7.77% FCF yield, net debt/EBITDA 1.41. Tobacco cash flow is the canonical
recession-insensitive earnings stream: inelastic demand and annual price increases.
*Key risk:* the volume decline is structural (three-year revenue CAGR −0.9%) — this is a
melting ice cube you are paid to hold, and a regulatory shock to nicotine is unhedgeable.
*Invalidated by:* the dividend not covered by FCF, or net debt/EBITDA above 2.5.
*Missing:* `roe_pct` and `de_ratio` are both MISSING (negative book equity from decades of
buybacks), so I cannot assess balance-sheet resilience the usual way and rest on net
debt/EBITDA alone. No ESG data anywhere, and tobacco is commonly screened elsewhere —
`investor_profile.json.constraints.exclusions` is empty, so nothing is enforced here.

**BUY — CME Group, conviction 6.** Beta 0.275, net debt/EBITDA 0.33, D/E 14.59, net margin
63.4%, screen PASS. The distinguishing property: exchange volumes *rise* in a volatility
shock, so this is one of very few equities with positive downside convexity rather than
merely low beta.
*Key risk:* the flip side — 0.8% revenue growth and PEG 4.80 mean you pay a great deal for
that convexity, and in a calm tape it does nothing.
*Invalidated by:* PEG above 6, or volumes falling in a quarter when VIX rose.
*Missing:* no volume or open-interest data; institutional ownership not fetched.

**BUY — AZN.ST (holding), conviction 6.** Beta 0.205 is the lowest of any holding, and its
function here is explicitly ballast against a 54.05% industrials sleeve.
*Key risk:* a 0.19% FCF yield and net debt/EBITDA 1.38 put the defensiveness in the
revenue line, not the cash line.
*Invalidated by:* beta rising above ~0.5, or a dividend cut.

**Attacking this sweep's BUY cases — the other half of this job:**
- **VICI:** net debt/EBITDA 4.82, D/E 60.28. In the downside I am pricing, a leveraged REIT
  meets a higher discount rate and tenant-coverage stress simultaneously, and casino
  operators are not defensive tenants. A 7.76% yield at 4% of the range is the market
  pricing that, not missing it.
- **APP, NVDA, MU:** betas 2.488, 2.217, 2.222 — the three highest in the focus set, and APP
  additionally carries D/E 111.13. **SNDK has no beta field at all**, which is worse than a
  high one. Adding any of these against an *unverified* −30% drawdown tolerance (S26) is
  the specific thing I object to this sweep.
- **CHTR:** D/E 441.58, net debt/EBITDA 4.41, revenue declining. The screen FAIL is deserved.
- **Swedish real-estate contrarian block:** BALD-B.ST net debt/EBITDA 16.13, CORE-B.ST 15.52,
  CATE.ST 10.85. Not investable at this portfolio's size however cheap the multiples look.

**SELL — VOLV-B.ST, conviction 4.** D/E 147.35 and net debt/EBITDA 3.8 make it the most
leveraged holding into the most cyclical end-market. This is the risk view, not the thesis
view; Growth's inflection case may well win.
*Invalidated by:* net debt/EBITDA below 2.5.

**Explicitly declining to flag ABB.ST:** D/E 55.75, net debt/EBITDA 0.46, beta 1.008. There
is no balance-sheet or cyclicality case against it, and I will not lend this lens's name
to a sale argued on other grounds.

### Voice 5 — Contrarian / Risk Taker

*Triage (`pct_52w_range`, low = near the low):* FIS 3, CATE.ST 3, DOM.ST 3, FISV 3, VICI 4,
APP 5, BALD-B.ST 6, EXE 8, PEP 10, HD 11, AFRY.ST 12, EIX 12, CORE-B.ST 12, CHTR 13,
CMCSA 14, MKC 18, BETS-B.ST 21.

**BUY — VICI, conviction 7.** The specific reason the pessimism looks wrong: it is *sector*
pessimism applied to a company whose own numbers did not change. Across five consecutive
runs at rank 8–9 the fetched fields have read revenue growth 5.7%, net margin 67.5%, screen
PASS — while the price went 26.51 → 25.77 → 25.65 → 24.73 → 24.11. The market is repricing
a rate environment, not an asset. Qualitative and labelled: triple-net master leases with
contractual escalators are the structure being discounted, and no lease-level data exists
here to confirm it.
*Key risk:* Macro's counter is the real one — if the 10-year is right, this sits at 4% of
range indefinitely and the 7.76% yield is the entire return.
*Invalidated by:* a dividend cut, or a tenant default.

**BUY — PEP (PepsiCo), conviction 6 — pulled in from outside `focus=Y`.** 10% of its 52-week
range, PEG 1.33, 4.56% dividend, 4.42% FCF yield, beta 0.361, screen PASS. Why the
pessimism looks wrong specifically: the de-rating is narrative-driven (GLP-1 and snacking),
while the fetched numbers show revenue still +6.4% ttm on a 2.8% three-year CAGR with a
10.8% net margin. A global staple at a below-market multiple with the highest dividend of
any consumer name in the set.
*Key risk:* D/E 238.95 and net debt/EBITDA 2.25 — this is a *leveraged* staple, so a real
volume decline hits the equity harder than the brand suggests.
*Invalidated by:* revenue growth turning negative, or net debt/EBITDA above 3.
*Missing:* no price/volume split, so I cannot tell price-led from volume-led growth.

**BUY — MKC (McCormick), conviction 5 — pulled in.** 18% of range, revenue +16.7%, 3.94%
dividend, 5.45% FCF yield, screen PASS. The trailing 8.11x is almost certainly distorted
(background knowledge, labelled: MKC has historically traded 20–25x), so I use forward
14.78x / PEG 1.89 — still a discount to what a branded-condiment franchise normally
commands.
*Key risk:* net debt/EBITDA 3.17 on a 2.5% three-year CAGR.
*Invalidated by:* the forward multiple rising above ~18x with no earnings step-up, or the
trailing figure resolving upward (meaning the distortion was real earnings weakness).

**BUY — FIS, conviction 5.** 3% of range, PEG 0.19, forward 5.32x, FCF yield 14.44%, and it
screens PASS despite the pessimism. I am naming the limit of my own case: revenue +29.1%
ttm against a −9.8% three-year CAGR, margins and D/E partly absent from this fetch, so I
cannot say specifically *why* the pessimism is wrong — only that the price implies terminal
decline and the cash flow does not.
*Key risk:* it may be cheap because payment processors are losing share to newer rails,
which no fetched field measures.
*Invalidated by:* FCF yield below 8%.

**Declined — the machine's penalty is deserved:** CHTR (D/E 441.6% on declining revenue),
CORE-B.ST (profit margin −85.6%), CATE.ST and BALD-B.ST (net debt/EBITDA 10.85 and 16.13),
EXE (−10.6% revenue with forward above trailing — no asymmetry), DOM.ST (1.5% net margin),
GPN (−9.2% margin). "Cheap and unpopular" is not a thesis, and none of these gives me a
reason the pessimism is wrong.

**SELL flags: none this sweep.** For the sixth sweep running my natural target is
INVE-A.ST — 87% of its 52-week range with no measurable valuation is the opposite of a
contrarian holding, it is a crowded one I cannot measure. I stand down again, and on
*evidence* rather than on the missing number: three different insiders bought in the last
three weeks, two at or above today's 401.00 (Lund 1,000 shares at 399.13 on 09/09, Elfving
850 at 411.55 on 01/09). People who can see the NAV are buying here. That does not make it
a contrarian BUY either.

### Voice 6 — Macro / Regime

*Regime, from this sweep's `macro-regime` output:* risk-on, US-anchored — 10y−2y spread
+0.27 (uninverted), real fed funds ≈ **−0.08%** (3.63% against US CPI 3.71%, both dated
2026-08-01), VIX 15.44, crypto Fear & Greed 70 ("Greed"). Running against a dollar index of
**118.21**, and against Sweden's own **+1.45% real policy rate** (Riksbank 1.75% vs Swedish
CPI 0.3%) — which is the regime this SEK-based, Sweden-heavy portfolio actually lives in.

**BUY — V (Visa), conviction 7.** The macro-specific argument: US CPI is still 3.71% and
Visa's revenue is a percentage of *nominal* transaction value, so inflation is revenue for
this model rather than a cost. USD-denominated earnings also sit on the right side of a
118.21 dollar instead of against it.
*Key risk:* a consumer-spending slowdown is the one state where nominal and real volume
fall together. The uninverted curve says that is not currently signalled — a signal, not a
forecast.
*Invalidated by:* the curve re-inverting, or US CPI below ~2% alongside decelerating volume.

**BUY — MO (Altria), conviction 6.** US-domestic, USD-earning, demand inelastic to both the
cycle and the rate path. With the real US policy rate at roughly zero, a 6.39% dividend on
a 7.77% FCF yield is a genuinely positive real return from an asset with almost no macro
beta.
*Key risk:* regime-neutral cuts both ways — it underperforms badly if this risk-on tape
continues. Stated plainly rather than hidden.
*Invalidated by:* real US policy rates moving decisively positive (above ~1.5%), which
would make the yield unremarkable.

**BUY — TSM, conviction 6.** On the right side of the dominant capital-spending cycle *and*
structurally long the strong dollar (USD revenue, TWD cost base) — a rare combination here,
since a 118.21 dollar is a headwind for most non-US assets.
*Key risk:* Taiwan. No field in this system prices geopolitical risk and I will not invent
one — this is the largest unmeasured macro exposure in any recommendation in this memo.
*Invalidated by:* a dollar index below ~105, which removes the FX leg entirely.

**Explicit regime downgrades, stated rather than buried in a score:**
- **VICI — downgraded on regime grounds alone.** The US 10-year at 4.94% (2026-09-17) sets
  both the discount rate and the refinancing cost for a triple-net REIT. I am not disputing
  Valuation's multiple; I am saying this is the asset class this regime punishes most
  directly, and five sweeps of the price not recovering is consistent with that.
- **Crypto sleeve (BTC0E.AS + ethereum) — not the add window.** Fear & Greed at 70
  ("Greed", up from 29 three weeks ago) against a 118.21 dollar is the worst configuration
  for adding: elevated sentiment plus a structural FX headwind. No flag against the 3y+
  thesis; a flag against sizing up now.
- **Swedish industrials (VOLV-B, ATCO-B, ALFA, ABB)** — betas 0.78–1.07 put them on the
  right side of the *US* risk-on read, but they are priced into Sweden's tighter +1.45%
  real backdrop, with a Riksbank decision three days out. US risk-on is not cover for
  holding expensive names; it is a different economy's tailwind.
- **Xetra-Gold** — expected to lag in a low-VIX risk-on tape. That is the crash hedge doing
  its job, not a thesis break.

**SELL flags: none on macro grounds.** Macro influences conviction; it does not dictate the
portfolio. This is not a market-timing system.
*Missing:* **no commodity-price series**, which disqualifies me from a real view on TPL
(rank 11), FANG (33) and EXE (36) — the three energy candidates whose driving variable is
unfetched. **No credit-spread data**, so the "VIX 15.44 = calm" read has no cross-check;
given the internally inconsistent strong-dollar / low-VIX / Greed combination, a credit
spread is the single series I would most want this sweep. Staleness named:
`fed_funds_rate` and `us_cpi_yoy` both 2026-08-01 (seven weeks, internally consistent with
each other), dollar index 2026-09-11, yields 2026-09-17.

### Voice 7 — Copycat / Smart Money

**Coverage first, because it determines what this voice can legitimately say.**
`insider_activity` (SEC Form 4) returned `skipped: non-US ticker, not covered by SEC EDGAR`
for all nine submitted tickers, and **no US candidate was ever submitted** — so there is
**zero US insider data this sweep**, covering none of APP, NVDA, TSM, MU, SNDK, MA, V, VICI,
MO, CMCSA, CHTR, FIS or any other `new` name. `MISSING: institutional ownership not
fetched` — no 13F, no activist positions, no accumulation/distribution data exists
anywhere in this system, and I will not fill that from training knowledge. This voice can
therefore review holdings but cannot contribute to discovery at all. Everything below comes
from Finansinspektionen's Insynsregister via this session's fetch (FI does not review
notifications before publication; completeness is not guaranteed).

**BUY — AZN.ST, conviction 8.** CEO **Pascal Soriot, 60,000 shares at 121.02 GBP**,
transaction date 14/09/2026 (published 17/09) — roughly £7.3m of open-market buying seven
days ago — with Chairman **Michel Demare, 2,500 at 121.213296 GBP** on the same date. Two
distinct people, both at real market prices. Interpreted by quality, not direction: the
same pull shows CFO Aradhana Sarin "acquiring" 11,133 shares (17/08) and 73 shares (14/09)
at a **price of 0.00**, and Soriot himself 18,359 at 0.00 (14/05) — those are award
vestings and carry no information whatsoever. The 14/09 purchases at 121.02/121.21 do.
*Key risk:* a single well-timed CEO purchase is still one data point, and insiders buy into
declines that keep going.
*Invalidated by:* a Soriot or Demare disposal in the next FI pull.

**BUY — INVE-A.ST, conviction 7.** **Three separate insiders in three weeks** — CEO
Christian Cederholm 1,500 A-shares at 395.90 (14/09), Jacob Lund 1,000 A at 399.13 (09/09),
Ulrika Elfving 850 B at 411.55 (01/09) — on top of Cederholm again at 387.30 (17/07) and
Jessica Häggström 270 at 377.50 (05/06). Five distinct individuals buying through 2026 at
*rising* prices, with zero disposals in the record. Several insiders moving the same way
independently is a materially different signal from one insider repeating, and this is the
former.
*Key risk:* holding-company insiders buying their own NAV-discounted vehicle is partly
structural behaviour, and none of it substitutes for the NAV figure itself (S6).
*Invalidated by:* any Cederholm disposal, or two consecutive pulls with no buying.

**BUY — SHB-A.ST, conviction 6.** Chairman **Pär Boman**, 26/08/2026, a very large
single-day multi-tranche cluster at 145.55–146.24 SEK — tranches of 750,000, 411,472,
387,039, 282,391, 8,136, 7,113, 1,715, 1,403, 559 and 172 A-shares, over 1.8m shares in
one day. Today's 155.05 is ~6.5% above his average. Quality caveat stated: every tranche
is marked **"Closely associated: Yes"**, i.e. executed through a related entity rather
than a personal account, which lowers the signal relative to a personal purchase — and it
is one person on one day, not a pattern.
*Key risk:* this directly contradicts Valuation and Growth on the same name (revenue −3.8%,
99% of 52-week range, forward above trailing). I am not resolving that; I am reporting that
the best-informed person in the company bought heavily 6.5% below today's price.
*Invalidated by:* a Boman disposal, or a second consecutive pull with no further buying.

**Reads that are not calls:**
- **ABB.ST — no new transactions since 13/08.** The record still ends on disposals:
  Terwiesch 20,000 at 83.46 CHF (13/08), 10,000 at 77.30 (30/07), 18,799 at 76.76 (29/07)
  = 48,799 shares, plus board member Meline 2,456 at 82.12 (05/08). The six board-member
  "acquisitions" of 917–1,948 shares each at an *identical* 78.42 CHF on 04/05/2026 read as
  a routine annual board-fee share allotment, not conviction buying — six people, one day,
  one price. Net: the insider clause has tested negative for a **third consecutive pull**
  (08-23, 09-07, 09-21). **No SELL from this voice** — the ABB sale must stand on valuation.
- **ALFA.ST** — CFO Carl Fredrik Ekström, 1,000 shares at 547.49 (11/09), extending a streak
  with zero disposals on record. The break condition explicitly named a disposal as the
  thesis-killer, and it has not happened. Positive; not a BUY, and valuation is not my lens.
- **ATCO-B.ST** — nothing usable. Henrik Elmin exercised 79,442 options at 138.80 and
  disposed of the identical 79,442 shares at 199.50 the same day (23/07); Sara Hägg Liljedal
  did the same with 18,850 at 143.94→197.50 and 42,762 at 138.21→197.50 (21/07). That is
  compensation monetisation, not a view. The one genuine open-market buy is Kenneth
  Lagerborg, 7,000 B shares at 161.5681 (09/06) — below today's 172.45, but three months old
  and a single insider.
- **VOLV-B.ST** — the Helena Stjernholm cluster is unchanged and dated 27/07: ~1.25m B-shares
  across five tranches at 359.20–360.93, all marked "Closely associated: Yes" (qualitative
  and labelled: Stjernholm is Industrivärden's CEO, so this reads as an
  Industrivärden-related purchase rather than a personal one). Today's 337.80 is *below* her
  entry. Note also that the FI issuer search for "Volvo" returns **Volvo Car AB** rows in the
  same block (Nota 63,000 at 19.60; Samuelsson 50,000 at 19.295; Severinson 15,306 at 19.00)
  — a different company, and conflating the two would be a real error.

**SELL flags: none.** Stated explicitly: the only disposals in the entire dataset are ABB's
(three pulls stale) and Atlas Copco's option-exercise mechanics, neither of which is a sell
signal on its own.

---

## 3b. Chairman's Top 5

### #1 OPPORTUNITY: ABB.ST — ABB
**CATEGORY:** holding
**RANK HISTORY:** rank 66 now; 65 (09-14), 66 (09-07), 64 (08-31), 64 (08-25). Never in
the top 10; bottom third of the funnel every run it has appeared.
**VOICES IN FAVOR (of selling):** Valuation: 7, forward P/E 36.53 is *above* trailing
35.97 despite 14.2% revenue growth — no margin of safety; Fundamental: 7, FCF yield 0.09%
and FCF/revenue ~4.4% is the worst cash conversion of any holding; Growth: 5, double-digit
revenue growth that does not reach earnings is not growth.
**VOICES AGAINST / CAUTIOUS:** Defensive: the balance sheet is *fine* — D/E 55.75, net
debt/EBITDA 0.46, beta 1.008 — so this is not a risk-driven sell and it declines to flag it
as one; Copycat: the insider clause has tested negative a third consecutive pull, so there
is no fresh insider signal in either direction.
**STRONGEST CASE FOR:** Valuation's forward-versus-trailing inversion. A company growing
revenue 14.2% whose forward multiple sits *above* its trailing one is a market telling you
margins compress from here; combined with 4.4% FCF conversion and `thesis_status: BROKEN`,
there is no version of this where the stated thesis (electrification tailwinds →
re-rating) is visible in the numbers.
**STRONGEST CASE AGAINST:** Defensive's — nothing here is *dangerous*. A 3,793.60 SEK
position with a clean balance sheet and a 0.2% gain is not a problem that needs solving,
and forced selling to satisfy a screen is its own error.
**KEY DISAGREEMENT:** named, not averaged. Three voices want it gone on price and earnings
quality; two independently refuse to support the sale on their own evidence (balance sheet
sound; insiders quiet, not negative). The sale therefore stands on valuation and thesis
alone — it is *not* a consensus sell and I will not present it as one.
**DATA GAPS:** no EV/EBITDA or EV/EBIT anywhere in this system, so "expensive" rests on P/E
and FCF yield rather than an enterprise multiple — a real limitation on a name whose case
is entirely valuation. Raw `price_to_book` 109.9 is suspect-flagged and unusable; use the
FX-corrected ~11.7x in `data/company_profiles/ABB.ST.json`. No ESG data. Discount
confidence modestly, not heavily — the forward/trailing inversion and the FCF figure are
both clean.
**CHAIRMAN CONVICTION:** 7
**WHAT WOULD CHANGE THIS:** one reported quarter where operating margin expands and forward
P/E falls below trailing. ABB reports **2026-10-20**.
**PORTFOLIO FIT:** `portfolio` §1 rates equity sector concentration **ACT** — Industrials
54.05% of the 33,017.20 SEK individual-stock sleeve, against a 45% line. ABB is 3,793.60
SEK, i.e. 11.5% of that sleeve. Selling it and putting the proceeds into a non-industrial
name takes Industrials to 14,051.55 / 33,017.20 = **42.6%**, below the ACT threshold for the
first time. Both legs sit inside the same Avanza ISK, so institution concentration (82.77%,
also ACT) is unchanged either way, and there is no tax event.
**FINAL CALL: SELL** (all 4 shares, ~3,793.60 SEK at today's price)
**HORIZON:** Medium

**Fifth sweep.** First called 2026-08-24, reaffirmed 08-31, 09-07, 09-14. ABB was 924.60 on
2026-08-25 and 948.40 today, +2.6% — the delay has cost essentially nothing, and that is
not the argument. The argument is that a call reaching a fifth sweep unexecuted is no longer
a decision, it is a habit. Execute it, or decline it explicitly and let me retire it the way
the SHB-A.ST SELL was retired on 2026-09-14.

### #2 OPPORTUNITY: AZN.ST — AstraZeneca
**CATEGORY:** holding
**RANK HISTORY:** rank 61 now; 60 (09-14), 61 (09-07), 60 (08-31), 59 (08-25). Never in the
top 10 — the funnel consistently under-ranks it, because `forward_pe` is MISSING every run
(S21) and its z_value is the lowest in the focus set (−1.528).
**VOICES IN FAVOR:** Copycat: 8, CEO Soriot bought 60,000 shares at 121.02 GBP on 14/09 and
Chairman Demare 2,500 at 121.21 the same day; Valuation: 6, PEG 1.20 (improved from 1.33)
with the price 47% into its range; Defensive: 6, beta 0.205 is the lowest of any holding and
this is the portfolio's designed ballast against a 54% industrials sleeve.
**VOICES AGAINST / CAUTIOUS:** Fundamental: ROIC 13.1% and an FCF yield of 0.19% are
mediocre for a name bought on quality grounds — a good business, not an excellent one;
Macro: no flag but no tailwind — defensive pharma is on the wrong side of a risk-on tape by
construction.
**STRONGEST CASE FOR:** Copycat's, and the distinction it drew is what makes it strong:
Soriot's and Demare's purchases carry real prices (121.02 / 121.21 GBP) while the same FI
pull shows CFO Sarin's 11,133- and 73-share lines at a price of **0.00** — award vestings
with no signal. A CEO committing ~£7.3m of his own money at market with the Chairman
alongside him on the same date is the highest-quality insider signal in the entire
candidate set.
**STRONGEST CASE AGAINST:** Fundamental's 0.19% FCF yield. Four straight years of revenue
growth (44.4B → 45.8B → 54.1B → 58.7B) is real, but almost none of it is reaching free cash
flow this year, and this system cannot see a multi-year FCF series to tell whether that is
capex timing or deterioration.
**KEY DISAGREEMENT:** Copycat reads insider conviction; Fundamental reads a business earning
13% on capital and converting almost nothing to cash. Both look at the same company and
neither is wrong — the insider signal is about price, the FCF figure is about the business.
I weight the insider evidence because it is fresh, primary and unambiguous, and discount
overall conviction because the FCF question is unresolvable with this system's data.
**DATA GAPS:** `forward_pe` MISSING (no forward multiple on the portfolio's largest stock);
trailing-only FCF; no ESG data. Also a live definitional conflict inside this memo's own
inputs: the candidates CSV reads "47% of 52-week range" while thesis-review reads "84.5% of
the 52-week high" — both correct under different formulas, which is S29 and
`data/definitions.json` unresolved.
**CHAIRMAN CONVICTION:** 7
**WHAT WOULD CHANGE THIS:** the next FI pull showing Soriot or Demare disposing, or the
2026-10-30 print showing margin compression. Either retires the BUY.
**PORTFOLIO FIT:** `portfolio` §7a is the binding constraint. Deployable capital **today** is
ISK cash of **845.43 SEK** — re-verified against this sweep's `portfolio` output, not carried
from a prior memo — and one AZN share costs 1,626.50 SEK. The BUY is unfundable until P3
executes, which frees ~15,261.55 SEK, of which `portfolio` allocates ~9,207 SEK to equity
(closing a −4.28pp underweight) and ~5,057 SEK to gold tranche 2. One share fits inside that
equity bucket. Against: AZN is already the largest individual stock at 5.77% of total capital
and healthcare is 39.41% of the stock sleeve — one share breaches no cap, but this is the
last share I would add before the sleeve gets a different sector.
**FINAL CALL: BUY** — 1 share. **Execution note: no idle capital confirmed (845.43 SEK ISK
cash); flag for the P3 conversion or the next contribution.** Merit and timing are separate
decisions; this is not downgraded to WATCH because funding is pending.
**HORIZON:** Medium

### #3 OPPORTUNITY: VICI — Vici Properties
**CATEGORY:** new candidate (first surfaced by this funnel 2026-08-25, `source: new`)
**RANK HISTORY:** rank 9 now; 9 (09-14), 9 (09-07), 8 (08-31), 8 (08-25). **Five consecutive
runs in the top 10**, best_lens contrarian every time.
**VOICES IN FAVOR:** Valuation: 8, 9.19x trailing / 7.93x forward, 7.76% yield, 67.5% net
margin, revenue +5.7% on a 15.5% three-year CAGR, at 4% of its 52-week range; Contrarian: 7,
five runs of top-10 ranking with no deterioration in any fetched field while the price fell
from 26.51 to 24.11.
**VOICES AGAINST / CAUTIOUS:** Macro: explicit downgrade **on regime grounds, stated plainly
rather than buried** — the US 10-year at 4.94% sets both the cap rate and the refinancing
cost for a triple-net REIT, and this is the asset class this regime punishes most directly;
Defensive: net debt/EBITDA 4.82 and D/E 60.3 with casino tenants — the 7.76% yield at the
bottom of the range *is* the market pricing that.
**STRONGEST CASE FOR:** Valuation's. A 7.76% yield at 7.9x forward earnings with 67.5%
margins and positive revenue growth is not a distressed profile — the cheapness and the
price position both point at the sector, not the company.
**STRONGEST CASE AGAINST:** Macro's, and it is the better argument than Defensive's.
Defensive describes a risk; Macro describes *why the price is where it is* and why it may
stay there. Five sweeps at 4% of range with unchanged fundamentals is consistent with the
market repricing rates correctly — which means "it hasn't rallied yet" is not evidence that
it will.
**KEY DISAGREEMENT:** Valuation says the multiple is wrong; Macro says the multiple is
correct for this rate regime and will not fix itself until the rate path does. Not
reconcilable, and I am not averaging it. It resolves as: own it for the income and the
diversification, not for a re-rating, and do not size it as though the re-rating is coming.
**DATA GAPS:** no EV/EBITDA, no FFO, no AFFO, no lease-coverage or tenant data; no US insider
data at all this sweep (EDGAR returned `skipped` for all nine submitted tickers and no US
candidate was submitted — the scope gap noted against S25's closed entry, still real);
`MISSING: institutional ownership not fetched`. A meaningful discount: this is a REIT
underwritten without the two metrics REITs are actually valued on.
**CHAIRMAN CONVICTION:** 6
**WHAT WOULD CHANGE THIS:** the US 10-year moving decisively through 4.5% in either
direction. Down and the thesis works quickly; up and Macro was right and this sits at 4% of
range for another five sweeps.
**PORTFOLIO FIT:** the best-fitting candidate in the set on `portfolio` §6's own read — Real
Estate is **0%** of the portfolio and direct US exposure is **0%** among individual stocks,
so it diversifies on both dimensions at once. It does nothing for the zero small/mid-cap gap
(all 14 net-new focus names are large-cap). Critically, funding is **not new capital**: it is
ABB's ~3,793.60 SEK, which is exactly what takes Industrials from 54.05% (ACT) to 42.6%. At
24.11 USD and sek_per_usd 9.6936, that is roughly 16 shares.
**FINAL CALL: BUY — structurally conditional on the ABB.ST sale executing.** If ABB is not
sold this is NO ACTION, because there is no other capital: `portfolio` §7b confirms no ISK
sale is needed or proposed, and §7a's new money is already allocated to the equity
underweight and gold tranche 2.
**HORIZON:** Medium

**Fourth sweep at this destination.** The ABB → VICI pairing has been the recommendation on
08-31, 09-07, 09-14 and today, after two earlier destinations (GOOGL, then META) were
superseded. That churn is worth naming: three destinations in five sweeps says the *sale* is
the call with conviction behind it and the *redeployment* is the part the system keeps
re-litigating. VICI has now held its top-10 rank longer than either predecessor did, which
is the main reason it has stopped moving.

### #4 OPPORTUNITY: TSM — Taiwan Semiconductor Manufacturing
**CATEGORY:** watchlist
**RANK HISTORY:** rank 7 now; 7 (09-14), 7 (09-07), 7 (08-31), 6 (08-25). Five consecutive
runs in the top 10.
**VOICES IN FAVOR:** Fundamental: 8, ROE 40.0%, net margin 49.9%, operating margin 60.3%,
net debt/EBITDA −0.77 (net cash); Growth: 7, +36.0% revenue on an 18.9% three-year CAGR at
19.8x forward; Valuation: 7, PEG 0.83 with forward far below trailing 32.5x; Macro: 6, right
side of the AI-capex cycle and structurally long the strong dollar.
**VOICES AGAINST / CAUTIOUS:** Fundamental itself flags that TSM's `roic_pct` 183.7% and
`fcf_yield_pct` 32.42% are **implausible for a capital-intensive foundry and are not in the
suspect column** — third consecutive sweep the same two fields on the same name evade the
detector (S24), while feeding its z_quality of 1.919 and its rank-7 position. Macro: Taiwan
concentration risk is unpriceable from any field this system fetches.
**STRONGEST CASE FOR:** Fundamental's, once the bad fields are stripped out. ROE 40% plus a
net cash position at 19.8x forward on 36% growth is the best quality-and-price combination in
the entire 74-row set, and the only one where the growth rests on a structural monopoly at
the leading edge rather than on a cycle.
**STRONGEST CASE AGAINST:** that a voice had to delete by hand two of the four metrics its
own lens ranks on. When the detector built to catch exactly this error class misses the same
name three sweeps running, the honest response is lower conviction, not a workaround.
**KEY DISAGREEMENT:** there is no real one on merit — four voices converge. The disagreement
is between the *opportunity* (strong) and the *ability to act* (zero free capital), which is
a portfolio question, and it belongs below rather than in a voice's score.
**DATA GAPS:** `roic_pct` and `fcf_yield_pct` unreliable and unflagged (S24); no insider data
of any kind — EDGAR was never queried for any candidate; `MISSING: institutional ownership
not fetched`; no geopolitical-risk field anywhere.
**CHAIRMAN CONVICTION:** 6 — capped by the unflagged suspect metrics, not by the thesis.
**WHAT WOULD CHANGE THIS:** free capital. On merit this is the best unowned name in the set;
the only thing between it and a BUY is that every SEK is accounted for. Secondarily, S24's
bounds being fixed so the quality case rests on data rather than a manual correction.
**PORTFOLIO FIT:** `portfolio` §6 rates it a double diversifier — Technology is 0% of the
individual-stock sleeve and Taiwan is a wholly new country against Sweden 49.10% (WATCH),
UK 39.41%, Switzerland 11.49%. But: no capital. ISK cash is 845.43 SEK against a 430.26 USD
share (~4,171 SEK); P3's ~15,261 SEK is already committed to the equity underweight and gold
tranche 2; and §7b explicitly finds no ISK sale is needed. Buying this would mean displacing
the AZN share or the gold tranche, neither of which is a better use of the same money.
**FINAL CALL: HOLD-WATCH** — a high-merit opportunity that resolves to WATCH on capital, not
on doubt. That is a correct output, not a contradiction.
**HORIZON:** Medium

### #5 OPPORTUNITY: INVE-A.ST — Investor A
**CATEGORY:** holding
**RANK HISTORY:** rank 10 now; 10 (09-14), 11 (09-07), 11 (08-31), 11 (08-25). Five
consecutive runs in the top 10 — and the rank is close to meaningless, which is the whole
problem.
**VOICES IN FAVOR:** Copycat: 7 — three separate insiders bought in the last three weeks
(CEO Cederholm 1,500 A at 395.90 on 14/09; Jacob Lund 1,000 A at 399.13 on 09/09; Ulrika
Elfving 850 B at 411.55 on 01/09), plus Cederholm again at 387.30 (17/07) and Häggström at
377.50 (05/06) — five distinct individuals through 2026 at rising prices, zero disposals,
two of the three most recent at or above today's 401.00.
**VOICES AGAINST / CAUTIOUS:** Valuation: no verdict possible — trailing P/E 4.68 and PEG
4.91 are holding-company pass-through artifacts (the 117% "revenue growth" and 80.1%
"margin" confirm it) and there is no NAV discount/premium, so there is literally no
valuation read to give; Fundamental: ROIC 40.7% and ROE 27.3% are the same artifact and
cannot be graded as operating quality; Contrarian: stood down, but only on the insider
evidence, not because the missing number arrived.
**STRONGEST CASE FOR:** Copycat's, the only case with real evidence behind it. The people
buying are the people who can see the NAV. That is not the NAV number, but it is the closest
substitute this system has ever had.
**STRONGEST CASE AGAINST:** Valuation's — which is not an argument against the company at
all. It is the observation that after **six consecutive sweeps** this holding still cannot be
valued, and a position that cannot be valued cannot be sized, added to, or defended. The
insider buying says someone informed finds 401 acceptable; it does not say what you own.
**KEY DISAGREEMENT:** the sharpest in the memo and unmoved in six weeks. Copycat has primary
evidence and wants to add; Valuation and Fundamental have no usable metric and cannot
consent. Last sweep's memo called it "resolves nothing, it just moves the deadlock" and that
still holds — the insider evidence got *stronger* this sweep (three buyers in three weeks
rather than one), which makes the missing number more expensive, not less necessary.
**DATA GAPS:** the central one is S6 — no holding-company NAV source, which simultaneously
blinds the funnel's `value` lens on INVE-A.ST, INDU-C.ST, BURE.ST and LUND-B.ST. Also
`forward_pe` MISSING, and the same two-conventions problem as AZN (CSV "87% of range" vs
thesis-review "95.8% of the 52-week high"), S29.
**CHAIRMAN CONVICTION:** 5 — deliberately low. Not because the evidence is weak but because
the strongest evidence and the missing evidence answer different questions.
**WHAT WOULD CHANGE THIS:** the NAV discount/premium. One number, read off the quarterly
report or Investor's IR page (Q3 reports **2026-10-07**), recorded in
`data/company_profiles/INVE-A.ST.json`. Roughly ten minutes of human work that resolves a
deadlock which has consumed a voice's verdict in six consecutive sweeps.
**PORTFOLIO FIT:** `portfolio` §6 — adding concentrates on two flagged dimensions at once:
Sweden is 49.10% of the sleeve (WATCH) and Financial Services is already present via
SHB-A.ST and INVE-A.ST itself. It also structurally overlaps INDU-C.ST (rank 8, watchlist),
the other Swedish holding company in the top 10, with the identical unmeasured NAV gap. The
current position is 2,005 SEK (5 shares), 0.93% of total capital — no cap is near breaching,
so this is a knowledge problem, not a sizing one.
**FINAL CALL: HOLD-WATCH** — no add without the NAV figure, no sale against three insiders
buying at today's price. See open decision **D-b**.
**HORIZON:** Medium

### Other SELL recommendations on current holdings

You get a direct answer to "should I sell anything" every sweep. Beyond ABB.ST:

- **VOLV-B.ST — flagged by Defensive only, conviction 4, and I am declining it.** D/E 147.35
  and net debt/EBITDA 3.8 make it the most leveraged holding into the most cyclical
  end-market. But Growth's read is better: forward 13.37x below trailing 18.90x with PEG 0.97
  and revenue growth turned positive (+2.7%) off a real two-year decline is the earnings
  inflection the position was bought for, and `thesis_status: TOO_EARLY` is honest — bought
  2026-08-03/04, the break condition's own clock runs to ~early November. **NO ACTION**,
  re-test after the 2026-10-23 print.
- **SHB-A.ST — flagged by Growth, conviction 4, and I am declining it.** Revenue −3.8%,
  forward above trailing, 99% of its 52-week range, PEG 19.14. Every word is true and the
  position is **one share, 155.05 SEK**. The SELL was correctly retired on 2026-09-14 as too
  small to matter; re-raising it weekly is noise, not diligence. The genuinely interesting
  thing is Copycat's opposite read — Chairman Pär Boman's 1.8m-share single-day cluster at
  145.55–146.24 SEK, 6.5% below today's price, though "Closely associated: Yes" (a related
  entity, not a personal account, which lowers the signal). **NO ACTION.**
- **ATCO-B.ST — flagged by Valuation, conviction 5, and I am declining it.** Trailing 31.33x,
  PEG 2.09, 75% of range. Fundamental's counter is specific: ROIC 39.7%, ROE 25.7%, net
  debt/EBITDA 0.50 make this the best *business* among the holdings, and ttm revenue +9.1%
  means its break condition has not fired. Selling the highest-quality industrial to fix an
  industrials overweight, while the lowest-quality one is already queued for sale, is the
  wrong order of operations. **NO ACTION** — it stays the next rotation candidate after ABB.
- **ALFA.ST, BTC0E.AS, DE000A0S9GB0, ethereum — no sell flag from any voice.** ALFA is
  expensive (27.55x, PEG 1.72) with thesis WEAKENING, but the insider streak extended again
  (CFO Ekström, 1,000 shares at 547.49 on 11/09, still zero disposals on record). The crypto
  and gold positions are structural; see D-c and §10.
- **APP — the funnel's #1 name for five consecutive runs resolves to NO ACTION for a fifth
  sweep**, on the same unfixed gap: quality metrics are pristine (ROIC 65.5%, operating margin
  77.7%, revenue +52.8%) while the price sits at 5% of its 52-week range, and S29 means the
  system cannot see from what level or when that drawdown happened. That is not a reason to
  disbelieve the metrics; it is a reason not to commit capital on them. It is also the single
  clearest case for the one-column fix S29 asks for.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens §1.

| Dimension | Rating | Number | Reason |
|---|---|---|---|
| Asset allocation vs targets | **WATCH** | Equity 75.72% (target 80, −4.28pp); crypto 11.24% (target 10, +1.24pp); gold 2.65% (target 5, −2.35pp); FI 3.01% (target 0, +3.01pp); cash 7.39% (target 5, +2.39pp) | No single drift >5pp, but four of five buckets are off, and equity+gold underweight roughly nets against the cash+FI overweight — a deployment problem, not a market-move problem. |
| Equity sector concentration | **ACT** | Industrials 54.05% of the sector-tagged individual-stock sleeve (33,017 SEK); >45% ACT line | Same long-running finding (VOLV-B/ATCO-B/ALFA/ABB all Industrials). Diluted to ~11% if weighted against the full equity sleeve including Avanza Global — but that dilution is *unverified*. |
| Geography (home bias) | **WATCH** | Sweden 49.10% / UK 39.41% / Switzerland 11.49% of the same sleeve; >30% WATCH line | Sweden bias is a stated user preference, not an accident — flagged mechanically regardless. |
| Currency exposure | **UNKNOWN** | — | No per-holding revenue-currency split in the snapshot. All individual stocks quote in SEK, but AZN/ABB/Volvo/ATCO/Alfa Laval earn substantially in USD/EUR — genuinely unmeasured, not a guess. |
| Single-position concentration | **ACT (nominal)** | Avanza Global fund = 53.17% of total capital / 55.84% of investable portfolio; >15% cap | A diversified-index-fund artifact, not single-company risk. |
| Institution concentration | **ACT** | Avanza = 82.77% of total capital / 86.90% of investable portfolio; >80% cap | Consistent with last sweep's 83.12%. Structural and largely intentional (ISK consolidation) — flagged per rule regardless. |
| Fee drag | **OK** | ~187 SEK/year total (~0.083% of total capital); cap is 0.4% | No holding above 0.5%/yr. |
| Wrapper efficiency | **OK, with one open sub-item** | ISK 186,772.85 SEK vs ~300,000 SEK allowance (verify with Skatteverket) → ~113,227 SEK headroom | No capital sits in a taxed AF while ISK headroom exists. Sub-item: 14,416.12 SEK (PayPal) + 611 SEK (hb-checking) sit outside any wrapper. |
| Drawdown-tolerance fit | **WATCH — unverified, not resolved this sweep** | Backtest −20.62% (2019–2026) vs −30% tolerance = "inside," but that window's own worst equity shock was only −19.14%; a prior sweep's stress arithmetic (not a backtest) put the mix at roughly −36%, i.e. "outside." | Both carried forward from S26. A fresh shock-window backtest is warranted before this row can be called OK or ACT. |

**Provisional because of `investor_profile.json` gaps, named:**
`reference_targets` still carries the superseded **85/10/5/0** rather than
`portfolio.json`'s authoritative 80/10/5/0/5 — the **third** consecutive sweep this one-line
staleness has been flagged unapplied, and the closed log's own standing rule says a third
occurrence opens an S-item without further deliberation (`meta`'s call, not this memo's).
`horizon.primary_goal` remains "nature UNCERTAIN"; `years_until_needed` is a soft 3–7y;
`constraints.exclusions` is empty (so nothing is mechanically screened out — relevant because
MO, a tobacco name, ranks 13th and is a live Defensive pick); and
`risk_tier_framework_proposed.open_items` still leaves the tier-level SEK mapping and the
contribution-routing rule undecided. The scorecard is honest against the adopted target; it
is provisional against a goal that has no date.

---

## 5. Headline calls

Five, each needing a decision this session.

1. **SELL ABB.ST, all 4 shares (~3,793.60 SEK).** Fifth consecutive sweep, conviction 7.
   Execute it or decline it — a call at a fifth sweep should not reach a sixth.
2. **BUY ~16 VICI, funded by the ABB proceeds, not new money.** Conviction 6, and this is the
   leg that actually fixes something: Industrials 54.05% (ACT) → 42.6%, plus the portfolio's
   first Real Estate and first direct US exposure. Dead if #1 doesn't happen.
3. **BUY 1 AZN.ST share (1,626.50 SEK) — unfunded today.** ISK cash is 845.43 SEK
   (re-verified this sweep). The CEO bought 60,000 shares seven days ago. Flag for the P3
   conversion or the next contribution.
4. **Execute P3 (PayPal → SEK → ISK), seventh-plus sweep.** ~15,261.55 SEK becomes deployable,
   which is simultaneously the funding for #3, for gold tranche 2 (~5,057 SEK, closing the
   −2.35pp gold gap), and the fix for the cash overweight and the unwrapped 14,416.12 SEK.
   The 4% cost is already accepted; the recurring ~750–1,000 EUR every two months keeps
   paying it until this executes.
5. **Get the Investor AB NAV discount/premium (S6 / D-b), or decide to stop asking.** Six
   sweeps, one number, ten minutes. Q3 report lands 2026-10-07.

---

## 6. Open actions vs open decisions

### Open actions (things to go do), by ID

| ID | Status | Action |
|---|---|---|
| **P3** | decided — pending execution | Convert the full PayPal balance inside PayPal at the accepted 4% spread, route the SEK into the ISK, then zero the paypal holdings in `portfolio.json`. ~15,261.55 SEK deployable once done. |
| **P1** | blocked (on user) | Find the ETH cost basis. Blocks any sale, any tax math, any return figure — and per the 2026-08-17 ruling, blocks adding ETH units too. |
| **P9** | open | Delete the phantom AZN OPENING row in the Excel Transactions tab, per the workbook's own README. `portfolio.json` correctly holds 8 shares; this only stops the discrepancy re-flagging. |
| **P10** | open | Confirm: one 5,000 SEK deposit or two? (`data/transactions.csv` carries both 2026-08-17 and 2026-08-22; the real Avanza export shows only 08-22.) |
| **S6** | open | Record Investor AB's NAV discount/premium in `data/company_profiles/INVE-A.ST.json` with source and date. |
| **S26** | open | Run `backtest.py` over a fixed window containing a real ≥−30% equity shock (2007–2009 or 2020-02/03), with crypto's realistic drawdown distribution, reported as a clearly-labelled second "shock window" figure alongside the rolling one. |
| **P6** (residual) | open | ~1,744 SEK of the original medium-tier cash is still uninvested; the two carried flags stand (Spiltan Aktiefond Investmentbolag overlaps Investor A; Swedbank Robur Technology A is a concentrated, higher-fee single-sector fund). |

**Note on the D-series:** D-a, D-b and D-c are referenced by ID throughout `OPEN_ITEMS.md`'s
P-item text, but **no standalone "D — Open decisions" section exists in the file** — the
space between the P- and S-sections is empty. Their content is fully reconstructible from
the P-item notes, which is what I have done below, but the register itself is missing and
should be restored so these stop living only inside other items' histories.

### Open decisions (forks), by ID

**D-a — where ABB's proceeds go.** Third destination in five sweeps (GOOGL → META → VICI).
- *Option 1 — VICI, ~16 shares.* Fixes the ACT-rated industrials concentration (54.05% →
  42.6%), adds the portfolio's only Real Estate and only direct US exposure, 7.76% yield.
  Trade-off: Macro's explicit downgrade — a leveraged REIT into a 4.94% 10-year, with no
  FFO/AFFO or EV/EBITDA to underwrite it.
- *Option 2 — hold the proceeds as ISK cash.* Trade-off: cash is already +2.39pp overweight
  and the sector concentration stays ACT; you buy optionality with a flagged drift.
- *Option 3 — TSM instead (~4,171 SEK/share, so ~1 share).* Better business, better
  growth-adjusted price, diversifies sector *and* country. Trade-off: one share is a
  0.4%-of-capital position that moves nothing, and TSM's two headline quality metrics are
  unreliable (S24).
- **My pick: Option 1** — the only one that resolves a flagged ACT rating with the capital
  actually available.

**D-b — Investor A's unmeasurable valuation.** Sixth sweep.
- *Option 1 — get the NAV number* (Q3 report 2026-10-07, ~10 min). Trade-off: none, except
  that it needs a human.
- *Option 2 — sell the 5 shares (2,005 SEK) on absence of evidence.* Trade-off: selling into
  three insiders buying at today's price, with a +38.2% gain, on a knowledge gap rather than
  a finding.
- *Option 3 — keep holding and stop re-flagging it.* Trade-off: accepts permanently that
  0.93% of capital is unvaluable, but frees a voice's attention every sweep.
- **My pick: Option 1**, as on 2026-09-07 and 2026-09-14. If it is not done before the next
  sweep, Option 3 is the honest fallback — three unexecuted picks of Option 1 means Option 1
  is not actually available.

**D-c — crypto sleeve sizing.** Third sweep deferred, with the timing pressure sharpened
again: crypto is 11.24% of the investable base against a 10% target while Fear & Greed reads
**70 ("Greed")**, up from 57 last sweep and 29 three weeks before, with ETH +7.8% on the week.
- *Option 1 — trim the certificate leg (BTC0E.AS) back toward 10%.* Cleanest on tax (no
  per-trade tax inside the ISK, 0%/yr fee). Trade-off: selling a structural 3y+ conviction
  holding on a 1.24pp drift, into strength.
- *Option 2 — wait for S26's shock-window backtest, then decide with numbers.* Trade-off:
  three sweeps of waiting have coincided with crypto rising and sentiment turning greedy,
  which is exactly when the decision gets hardest to make calmly.
- *Option 3 — revise the −30% tolerance upward and stop treating 11.24% as a drift.*
  Trade-off: changing the yardstick because the position moved is the wrong direction of
  causation, and `portfolio` §8 says so.
- **My pick: Option 2, with a stated deadline.** The backtest is the named precondition on
  every version of this decision and it is a script run, not a research project. But if S26
  is not run before the next sweep, Option 1 becomes the default — deferring a sizing
  decision indefinitely while the position drifts further above target is itself a decision,
  just an unstated one. Selling ETH is not on this list: P1 makes the tax math uncomputable.

---

## 7. Cost of being wrong

| Headline call | If wrong | Realistic SEK downside | Recoverable? |
|---|---|---|---|
| SELL ABB.ST | ABB re-rates on a margin recovery you sold before | ~950 SEK (25% of the 3,793.60 SEK position, foregone) | Yes — a 1.8% position, and the name stays in the universe; you can buy it back |
| BUY ~16 VICI | REIT de-rating continues as Macro argues; 10y goes to 5.5% | ~1,140 SEK (30% drawdown on 3,793.60 SEK), partly offset by the 7.76% yield (~294 SEK/yr) | Yes — income-producing, no portfolio-level leverage |
| BUY 1 AZN.ST | Margin or pipeline deterioration; the insiders were early | ~490 SEK (30% on 1,626.50 SEK) | Yes — and it would also signal reviewing the existing 8 shares, a ~3,900 SEK second-order exposure |
| Execute P3 | The 4% spread (~610 SEK on 15,261 SEK) is paid and the SEK sits idle anyway | ~610 SEK, certain rather than contingent | Partly — the spread is unrecoverable, but it recurs every ~2 months if you don't, so delay costs more than execution |
| Defer D-c (crypto) | Crypto halves from a greedy-sentiment peak | ~12,077 SEK on the full 24,153 SEK sleeve; ~1,330 SEK attributable to the 1.24pp overweight specifically | The overweight portion, yes. Whether the sleeve-level loss sits inside the stated risk budget is precisely what S26 leaves unverified |
| HOLD-WATCH TSM | It compounds and you never own it | 0 SEK realised; pure opportunity cost | Yes — it has held rank 7 for five runs and will be there when capital is |

---

## 8. Timing collisions

From `data/cache/calendar/20260921-events.json`. **Caveat first: `macro_calendar.json` was
last verified 2026-08-03 and US/SE CPI release dates are still unverified** — the Riksbank
and FOMC dates below are as-stored; the earnings dates come from a live fetch this session.

- **Riksbank rate decision + Monetary Policy Report, 2026-09-24 — three days out.** The live
  flag for this memo. Every individual holding quotes in SEK, the sleeve is 49.10% Swedish,
  and `macro-regime` makes the specific point that Sweden's real policy rate is **+1.45%**
  (Riksbank 1.75% vs Swedish CPI 0.3%), materially tighter than the US backdrop the risk-on
  call rests on. Nothing in this memo needs to execute before Wednesday; the ABB sale and
  the P3 conversion are both insensitive to it.
- **ABB.ST reports 2026-10-20.** The SELL should execute *before* the print, not after —
  waiting converts a valuation decision into a binary event bet, which is neither the thesis
  nor a game this system claims an edge in.
- **FOMC 2026-10-27/28, immediately followed by VICI's earnings 2026-10-29.** A genuine
  double collision, landing on the one recommendation whose main risk is the rate path. If
  the ABB → VICI trade slips ~5 weeks it executes into exactly that window — an argument for
  doing it in the next few days rather than letting it drift.
- **Other prints inside 45 days:** MU 09-30, INDU-C.ST 10-07, TSM 10-15, SHB-A.ST 10-21,
  ATCO-B.ST 10-22, VOLV-B.ST 10-23 (the TOO_EARLY re-test), ALFA.ST 10-27, AZN.ST 10-30,
  APP 11-04, SNDK 11-06. INVE-A.ST returned no earnings date from the fetch.

---

## 9. Data gaps for `meta`

What the voices most often wanted and did not have, ordered by what it cost this sweep.
Surfacing, not fixing.

1. **US insider data: zero coverage, again.** `insider_activity` returns `skipped: non-US
   ticker, not covered by SEC EDGAR` for all nine submitted tickers, and **no US candidate
   was ever submitted** — so Copycat had nothing on APP, NVDA, TSM, MU, SNDK, MA, V, VICI,
   MO, CMCSA, CHTR, FIS or any other `new` name. That is the scope gap noted against S25's
   closed entry sitting on top of S20's confirmed gateway block. The consequence is
   structural: this voice can review holdings but can never contribute to *discovery*. Also
   standing: `MISSING: institutional ownership not fetched` — no 13F, no activist positions,
   anywhere.
2. **S24's detector hole — third consecutive sweep, same name, same two fields.** TSM's
   `roic_pct` 183.7% and `fcf_yield_pct` 32.42% are again absent from the suspect list and
   again feeding z_quality 1.919 and rank 7. A voice compensating by hand is not the detector
   working. The asymmetry hypothesis from 2026-09-07 — bounds tighter on `price_to_book` than
   on `roic_pct`/`fcf_yield_pct` — is now worth testing rather than restating a third time.
3. **No EV/EBITDA, EV/EBIT, FFO or AFFO.** Named generally in `council.md`, but it bit
   specifically here: VICI is a Top-5 BUY underwritten without either metric REITs are
   actually valued on, and the ABB SELL rests on P/E and FCF yield because no enterprise
   multiple exists anywhere in this system.
4. **S29, fifth sweep unfixed.** `week52_high` / `week52_low` are still absent from the
   candidates CSV though the snapshot carries both. Two live consequences today: the funnel's
   #1-ranked name for five straight runs (APP) again resolves to **NO ACTION** because "5% of
   52-week range" cannot be interpreted without knowing from what level and when; and this
   memo contains two different "% of 52-week range" conventions for AZN and INVE-A that read
   like a contradiction and are not one. One column, no new fetch.
5. **S6, sixth sweep.** No holding-company NAV source blinds the `value` lens on four
   candidates simultaneously (INVE-A.ST, INDU-C.ST, BURE.ST, LUND-B.ST) and produced the only
   Top-5 entry in this memo where no valuation verdict was possible at all.
6. **S21, fifth measurement.** Swedish `forward_pe` coverage still drives the MISSING block:
   10 of this sweep's 17 MISSING rows are Nordic names missing `forward_pe` or
   `debt_to_equity`. Note AZN.ST specifically — the portfolio's largest stock has had no
   forward multiple in any of the five runs on record, which is part of why the funnel ranks
   it 59–61 while three voices call it a BUY.
7. **No commodity-price and no credit-spread series.** The commodity gap disqualified a real
   macro view on three energy candidates this sweep (TPL rank 11, FANG 33, EXE 36 — the
   variable that drives all three is unfetched). The missing credit spread means the "VIX
   15.44 = calm" read has no cross-check, and given the internally inconsistent
   strong-dollar / low-VIX / Greed combination `macro-regime` flags, that is the single series
   I would most want.
8. **No ESG field for any holding or candidate.** Stated per name by the `portfolio` lens.
   Currently harmless — `investor_profile.json.constraints.exclusions` is empty — but MO
   (tobacco) ranks 13th and is a live Defensive BUY, so the absence now touches a real
   recommendation rather than a hypothetical one.
9. **The missing D-series register in `OPEN_ITEMS.md`** (see §6). Not a fetch gap, but three
   open decisions referenced by ID across the file have no section of their own.

---

## 10. Structural / non-stock decision

Only one is live. Levers 1–2 are structurally closed per CLAUDE.md and are not re-flagged.
(One housekeeping note from the `portfolio` lens: CLAUDE.md's priority-order text still names
the 2.5%/yr BTC certificate as the open fee item — it was closed 2026-08-17 when COIN-XBT.ST
was replaced by the 0%/yr Valour certificate. Stale text, not a portfolio finding.)

**ACTION:** Convert the full PayPal balance (1,177.49 USD + 266.88 EUR) inside PayPal at the
accepted 4% spread and transfer the SEK into the Avanza ISK.
**POSITION:** PayPal balance, 14,416.12 SEK at this sweep's FX (`portfolio` §2).
**TARGET:** Avanza ISK. Deployable total becomes ISK cash 845.43 + 14,416.12 ≈ **15,261.55
SEK**; `portfolio` §7a allocates ~9,207 SEK to the equity underweight, ~5,057 SEK to gold
tranche 2, ~998 SEK residual cash.
**REASON:** fee drag (lever 2) on a balance sitting outside any wrapper, paying the 4% spread
on a recurring ~750–1,000 EUR inflow every ~2 months, indefinitely. It is also the binding
constraint on two separate BUY calls in this memo and on the gold underweight.
**THESIS STATUS:** decided 2026-08-17 by the user (Option A, 4% accepted). Unchanged.
**WHAT CHANGED:** nothing about the decision. Only the count — seventh-plus sweep pending
execution, and the list of things waiting on it has grown from one (fee drag) to four (fee
drag, the AZN.ST share, gold tranche 2, the cash overweight).
**BREAK CONDITION:** if PayPal's disclosed conversion rate turns out materially worse than 4%,
or a fee-free route appears, reopen the routing question. Neither has happened.
**CONFIDENCE:** High — this is arithmetic, not a forecast.
**HORIZON:** Long (structural, recurring).

---

## 11. Learning notes

- **Five voices can converge and still not produce a buy.** TSM took four independent BUYs at
  conviction 6–8 and resolved to HOLD-WATCH — not because anyone doubted it, but because
  every SEK is committed. That separation is the whole point of running opportunity selection
  before portfolio fit: the merit verdict and the capital verdict answer different questions,
  and collapsing them would have hidden a genuinely good idea behind "no cash."
- **Direction is the least informative thing about an insider trade.** Four datasets this
  sweep look superficially alike and mean entirely different things. AstraZeneca's CEO buying
  60,000 shares at 121.02 GBP is conviction; the same company's CFO "acquiring" 11,133 shares
  at a price of **0.00** is an award vesting and means nothing. Atlas Copco's executives
  exercised options at 138–144 SEK and sold the identical shares at 197.50 the same day —
  compensation monetisation, not a view. Handelsbanken's Chairman bought 1.8m shares in one
  day, but flagged "Closely associated," i.e. through a related entity rather than personally.
  Reading the buy/sell column alone would have got all four wrong.
- **A metric can be real, correctly fetched, and still mean nothing.** Investor A's trailing
  P/E of 4.68 and 80.1% "margin" are not errors — they are what happens when a holding
  company's investment gains land in the revenue line. The same shape at a larger magnitude
  is why Industrivärden's 1198% "revenue growth" is suspect-flagged and withheld from its lens
  scores. The only difference between the two is that one tripped a plausibility bound and the
  other did not, which is exactly why S24 matters: the detector decides which unusable numbers
  get quarantined and which get quietly reasoned from.
- **An unexecuted decision has a cost that never shows up in the price.** ABB has moved +2.6%
  since the SELL was first made, so the delay has cost essentially nothing in SEK. But the ABB
  sale is the funding for the VICI buy, which is the only thing that moves Industrials below
  its ACT threshold, which is the oldest open flag on the list. Five sweeps of not executing
  one small trade has therefore held three findings open simultaneously — and none of that is
  visible in a P&L.

---

`journal` **must run next.** An unlogged memo is invisible to the next session and can never
be reconciled — which is the only calibration mechanism this system has. Then
`python scripts/decisions.py record --picks data/picks/2026-09-21-picks.csv`, followed by
`python scripts/decisions.py basis --write`.
