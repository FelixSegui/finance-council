# Council memo — 2026-08-11

*Structured synthesis of this system's own agents (market-data, valuation,
macro-regime, portfolio, thesis-review). Not advice from a licensed advisor.
Every number traces to `data/cache/snapshots/20260811T170152.json`,
`data/portfolio.json`, `/OPEN_ITEMS.md`, or an agent output from this session.*

Snapshot: `20260811T170152.json` · previous: `20260810T061323.json` · no Excel
import this sweep · no calendar run this sweep (S3 unfixed — earnings dates
unavailable, stated rather than estimated).

---

## 1. Position report

| Position | Price | Δ vs prev | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A | 146.85 | -1.4% | +13.6% | 91% | 146.85 | fetched |
| Investor A | 414.30 | -0.4% | +42.8% | 97% | 2,071.50 | fetched |
| Volvo B | 354.60 | -2.0% | -3.5% | 85% | 4,609.80 | fetched |
| Atlas Copco B | 183.40 | -0.2% | +1.2% | 97% | 4,951.80 | fetched |
| AstraZeneca | 1,543.50 | +1.4% | +2.2% | 32% | 7,717.50 | fetched |
| Alfa Laval | 570.80 | -0.3% | -0.6% | 88% | 5,137.20 | fetched |
| ABB | 962.00 | -0.3% | +1.6% | 78% | 3,848.00 | fetched |
| Avanza Auto 3 | no data | no data | +65.2% | - | 16,191.00 | book value |
| COIN-XBT.ST | no data | no data | +26.0% | - | 15,240.00 | user-relayed (stale 8 days) |
| Avanza Global | no data | no data | +0.0% | - | 119,999.00 | book value |
| ETH (self-custody) | no data | no data | no data | - | 8,911.00 | user-relayed (S7 bug) |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high (true
percentile).*

**Crypto context (spot):** bitcoin 54,995 EUR (-2.5% vs prev, -48.9% vs ATH),
ethereum 1,614.85 EUR (-3.0% vs prev, +2.4% 30d, -61.8% vs ATH). Fear & Greed
29 (Fear), down from 30.

**Reading it.** One red day, everywhere except one name. Six of seven
individual stocks fell (Volvo B -2.0% the widest, now -3.5% vs cost and the
only position underwater), both crypto legs fell 2.5-3.0%, and **AstraZeneca
was the sole riser at +1.4%** — which is not a coincidence and is worth
pausing on: AZN's whole stated reason for being in this book is that it is
low-beta defensive ballast (beta 0.211, confirmed by thesis-review this
sweep), and a day where everything cyclical sold off and the defensive name
rose is that thesis behaving exactly as written. **No move this sweep
contradicts any holding's thesis.** Volvo at one week held is squarely in
TOO_EARLY territory, and a -2.0% day says nothing about a 3+ month recovery
claim. The industrial cluster (Atlas Copco 97th percentile, Alfa Laval 88th,
ABB 78th) barely moved and remains pinned near the top of its own year;
AstraZeneca at the **32nd percentile** is still the cheapest name in the book
within its own 52-week band. The two index funds (Avanza Global 59.4% of
capital, Auto 3 8.0%) are deliberately buy-and-hold, carry no fund NAV in this
snapshot, and need no comment.

**Two data corrections that carry into every number below.**

1. **The ETH line is stale.** `position_report.py` still does not reprice
   self-custody crypto (S7, confirmed unfixed, root-caused in the S-item). The
   portfolio agent computed it correctly from today's snapshot: **8,875.88 SEK**
   (-0.4% vs the 8,911 printed). Every weight in this memo uses 8,875.88.
2. **COIN-XBT.ST is carried at a user-relayed price from 2026-08-03, now 8
   days old.** A BTC-proxy directional estimate implies roughly 2,528.71/unit
   (~15,172 SEK) today — i.e. a slight *decline*, not an increase. That is an
   estimate and is not used in any weight; the 15,240 relayed figure is. Get a
   fresh quote from Avanza before 2026-09-03.

---

## 2. What should change

Five things. One is a trade, one is a reversal of yesterday's routing, two are
decisions you owe an answer to, one is system work.

1. **Deploy the idle ISK cash into AstraZeneca, not Avanza Global** — 1 share,
   ~1,543.50 SEK of the ~1,743.61 available. This reverses last sweep's
   destination (not the decision to deploy). Reason: last sweep's routing
   rested on the premise that "the medium tier has no vetted candidate today,"
   and that premise is factually wrong — AZN has a written thesis (executed
   2026-08-06), status INTACT, and is the only individual holding thesis-review
   would buy today. See Headline call 1. **If you have already placed the
   Avanza Global order, leave it** — the difference is the destination of 0.86%
   of capital and does not justify a second trade.
2. **Resolve D2 — where new contributions go.** `portfolio.json.targets` and
   `investor_profile.json` currently give literally opposite instructions for
   the next krona. Recommended resolution and options in Headline call 3 and
   Open decisions.
3. **Resolve D1 — PayPal routing (P3).** Two weeks open, and the number just
   got sharper: ~1,970-2,630 SEK/yr of recurring drag on top of ~563 SEK to
   clear today's balance. It also now has a second-order effect: PayPal's
   14,079.79 SEK is what keeps the crypto trip-wire from firing (Headline
   call 2). Concrete option in call 4.
4. **Run `swedish-equity-review` retroactively on ATCO-B.ST, ALFA.ST, ABB.ST.**
   P6's own stated next step, named for a fifth straight sweep, still never run.
   23 days to the 2026-09-03 thesis deadline.
5. **No trims, no rotations, no new candidates.** The crypto wire is not due
   until 09-03 and the certificate price is stale; `scout` was correctly not
   invoked (emphasis is portfolio-tending, four owned positions are still
   thesis-free, and the Watchlist has not changed).

---

## 3. Portfolio health scorecard

Carried over from the portfolio agent verbatim. Denominator: **Convention A
("classified capital") = 201,895.91 SEK** — HB tax reserve + checking, Avanza
ISK, ETH wallet; excludes PayPal, Revolut and the frozen SEB fund. See
Headline call 2 for why this convention is *not* the same thing as the pinned
trip-wire denominator, and why that distinction matters this week.

| Dimension | Status | Detail |
|---|---|---|
| Asset allocation vs targets | **WATCH** | Equity 78.36% vs 85% (-6.6pp), crypto 11.94% vs 10% (+1.9pp, at the top of the 12% trip-wire band with no cushion), cash 6.49% vs 5% (+1.5pp). |
| Equity sector concentration | **ACT** | Industrials (Volvo + Atlas Copco + Alfa Laval + ABB) = 65.1% of the individual-stock sleeve, above the 45% ACT line; 65.5% last sweep, so unchanged in substance. |
| Geography | **WATCH** | Stock sleeve 59% Sweden-listed, no direct EM; mitigated structurally by Avanza Global, but the stock-picking sleeve is home-biased. |
| Currency exposure | **UNKNOWN** | No revenue-by-region data; not graded. |
| Single-position concentration | **WATCH** | Avanza Global 55.6-59.4% of total (denominator-dependent), breaches the 15% cap by construction — product/operational concentration across hundreds of underlying names, not stock risk. No individual stock exceeds ~4%. |
| Institution concentration | **WATCH** | Avanza ~84-90% of classified capital, above the 80% cap — the expected consequence of the AF→ISK exit, and it will keep rising as contributions land. |
| Fee drag | **OK** | 564.14 SEK/yr ≈ 0.28% of classified capital, under the 0.4% cap. COIN-XBT.ST alone is 2.5%/yr (381 SEK/yr), 5x the next-highest fee. |
| Wrapper efficiency | **OK** | No sellable capital in taxable AF; ISK headroom ≈118,344 SEK vs an assumed ~300k threshold (unverified, P7). |
| Drawdown-tolerance fit | **UNKNOWN** | No backtest exists (S5, still open). |

**The scorecard is provisional in three named places**, and none of them are
TBDs in `investor_profile.json` — the profile is complete. The gaps are:

1. **Does the adopted 85/10/5/0 target respect your stated -30% max drawdown
   tolerance?** Never tested (S5). An 85% equity + 10% crypto book plausibly
   draws down more than 30% in a bad year. Until `backtest` runs, the WATCH row
   measures drift against a number that has itself never been validated.
2. **What is the portfolio's currency exposure?** No revenue-by-region data
   exists for any holding, so the row cannot be graded at all — which matters
   more than usual because your future liability currency is unknown (SEK or
   EUR, per `investor_profile.json.horizon.currency_note`).
3. **Where is the 3-6 month emergency buffer actually held?** The profile
   asserts one exists and is separate from the portfolio, but the only cash
   named anywhere in `portfolio.json` is a tax reserve owed to Skatteverket
   (10,752.76) plus 611 SEK of checking. This is load-bearing for Headline
   call 3, which recommends routing 0% of new money to cash.

**Structure (levers 1-2), one line, still closed:** all capital in the ISK, fee
drag 0.28% against a 0.4% cap, nothing broke. The one open fee item is the 2.5%
BTC certificate (P4), blocked on S1.

---

## 4. Headline calls

### Call 1 — Route the idle ISK cash to AstraZeneca, not Avanza Global

Yesterday's memo decided this cash goes to Avanza Global, and justified it with
one sentence: *"the alternative use (the medium tier) has no vetted candidate
today."* That sentence is wrong, and it was wrong when it was written. AZN.ST
is in the book, has a written thesis executed on 2026-08-06 via a prior Council
call, is graded **INTACT** by both `portfolio.json` and thesis-review's fresh
read, is the only individual holding thesis-review answers **YES** to on "would
I buy today," is graded **Cheap/Fair** by valuation (PEG 1.38, four straight
years of rising revenue, ~17% stable net margin, 32nd percentile of its own
52-week range), and is the one position macro-regime explicitly declines to
flag — calling it "correctly positioned as defensive ballast for this exact
bifurcated regime." Four lenses, no dissent.

> **The Contrarian.** You are re-opening a decision made yesterday, on the one
> day AZN went up, and "the name every lens likes" is exactly how a single-stock
> overweight begins. Discovering that last week's premise was wrong is not the
> same as evidence that AZN is a better buy today than it was yesterday — and
> 1,543 SEK into one pharma concentrates where the index fund diversifies.
>
> **First Principles.** Strip the history: there is unallocated cash and two
> destinations. The question is not "which decision did we already make" but
> "which holding would we choose to own more of with no prior." Thesis-review
> answers that directly and only once: AZN. Meanwhile the risk-tier framework —
> which `investor_profile.json` itself calls "the OPERATING allocation control"
> — has the secure tier slightly *over* 60% and the medium tier ~17pp *under*
> 30%.
>
> **The Expansionist.** Ignore the SEK constraint: if 50,000 SEK landed
> tomorrow, would any of it go to AZN? Yes — it is the only defensive,
> non-industrial, thesis-intact individual position in a stock sleeve that is
> 65% industrials, which is the sole **ACT** row on the scorecard. The
> maximum-upside version and the 1,743 SEK version point the same way.
>
> **The Outsider.** Described cold: you own seven stocks, four of which do
> broadly the same thing, one of which you can actually explain, and that one is
> also the cheapest of the seven within its own year. You have a little spare
> cash. Buying more of the one you can explain is not clever, it is obvious.
>
> **The Executor.** Monday: buy 1 share of AZN.ST with the available ISK cash —
> use the broker's real balance, not the computed 1,743.61 (it excludes
> courtage and is not broker-confirmed). Leftover ~200 SEK stays as cash; do not
> place a second order for it.

```
ACTION: ADD — 1 share AZN.ST (~1,543.50 SEK), funded from idle ISK cash
POSITION: AZN.ST 3.82% of classified capital (7,717.50 SEK, 5 shares);
          idle ISK cash 0.86% (1,743.61 SEK)
TARGET: AZN.ST ~4.6% (9,261 SEK, 6 shares) — still the largest individual
        stock but far inside the 15% single-position cap. Equity moves
        78.36% -> 79.12% against the 85% target.
REASON: (1) last sweep's routing rested on a premise that is factually
        wrong — the medium tier does have a vetted candidate, and it is the
        only holding in the book that four independent lenses rate
        positively with no dissent; (2) it is the only lever available this
        week that improves the single ACT scorecard row (industrials 65.1%
        of the stock sleeve -> ~61.8%) without selling anything; (3) the
        risk-tier framework has the medium tier ~17pp under target and the
        secure tier already over — the destination this cash was assigned to
        is the one that is already full.
THESIS STATUS: INTACT. portfolio.json thesis_status = INTACT; thesis-review's
        fresh read = INTACT, "no weakening," every stated leg re-verified
        (beta 0.211, 4 straight years of rising revenue, margins intact,
        PEG 1.38 vs 1.33 on 08-06). No disagreement to disclose.
WHAT CHANGED: not the company — the reasoning. The "no vetted candidate"
        premise behind yesterday's routing was checked this sweep and does
        not survive. Separately, AZN was the only riser (+1.4%) in a red
        tape, which is the low-beta behaviour its thesis claims and the
        first live datapoint for it.
BREAK CONDITION: quoted from portfolio.json — revenue growth or margins
        deteriorate structurally; the dividend is cut; or it re-rates to a
        premium indistinguishable from the growth assets it is meant to
        diversify against. None triggered.
CONFIDENCE: Medium. High on "deploy this cash into equity" (unanimous, and
        already decided last sweep); Medium on AZN over Avanza Global as the
        destination, because half that case rests on the risk-tier
        framework, which is itself in dispute (Call 3 / D2).
HORIZON: Long (3y+) — the holding's own stated horizon is 3-5 years.
```

**One honest gap on this call:** the earnings-calendar fetch is broken (S3,
root-caused, unfixed), so this buy has **not** been checked against an
AstraZeneca reporting date. No date is estimated. At ~1,543 SEK the exposure to
a print-timing accident is small, but the check genuinely did not happen.

### Call 2 — Crypto trip-wire: no trim, the pinned denominator stands — and the reason it is not firing is PayPal

The 2026-08-06 Council set the rule and the 2026-08-10 Council pinned its
denominator: trim COIN-XBT.ST if crypto exceeds **12% of investable capital**,
evaluated **2026-09-03**, where investable capital = total less the confirmed
tax reserve (10,752.76) and hb-checking (611). Today, three readings of the
same 24,115.89 SEK of crypto:

| Reading | Denominator | Crypto weight |
|---|---|---|
| **Pinned definition (2026-08-10)** — total less tax reserve and checking, PayPal included | 204,611.94 | **11.79%** |
| Convention A (portfolio agent's proposed standing convention) — classified capital, tax reserve and checking **in**, PayPal **out** | 201,895.91 | **11.94%** |
| Convention C — Avanza ISK + ETH wallet only | 190,532.15 | **12.66% — breached** |

Two things must be said plainly rather than averaged. **First, the portfolio
agent's Convention A is not the pinned definition.** It says it "most closely
matches last week's pinned 205,009 SEK denominator" — it matches by *magnitude*
and contradicts by *definition*: the pin excludes the tax reserve and checking
and includes PayPal; Convention A does exactly the reverse. Two conventions can
land within 0.15pp of each other today and diverge whenever PayPal moves.
**Second, and sharper: the pinned reading is the most permissive of the three,
and the 14,079.79 SEK of PayPal money is what buys the cushion.** Strip PayPal
out and the wire is already breached. A limit that holds only because money you
cannot access without paying ~4% is counted as investable is a limit worth
naming, not one worth quietly leaning on.

> **The Contrarian.** The pin is being defended because it is a pin. Notice
> which way it leans: it is the loosest of the three readings, and what keeps
> crypto under 12% is a PayPal balance you cannot move cheaply. On the strictest
> honest reading the trim is already due, and waiting 23 days is a choice to be
> governed by the most convenient arithmetic.
>
> **First Principles.** What is the wire measuring? Whether crypto is a larger
> share of the capital you control than you decided to tolerate. That is a
> question about ownership and claims: the tax reserve fails it (it is
> Skatteverket's money), PayPal passes it (it is yours, just badly wrapped and
> expensive to move). On that logic the pin is principled, not merely permissive
> — but it is one unresolved routing decision away from being wrong.
>
> **The Expansionist.** Unconstrained, is there an upside case for being *over*
> 12% crypto today? Macro says no, unambiguously: Fear & Greed 29, BTC -48.9%
> off ATH, ETH -61.8%, dollar index 119.06. The maximum-upside version of this
> portfolio does not add to the one sleeve every lens agrees is on the wrong
> side of its own regime.
>
> **The Outsider.** You wrote the rule down yesterday and today the person
> applying it wants to change how it is measured. Whether or not the new way is
> better, changing the ruler mid-measurement means you can no longer trust
> either number.
>
> **The Executor.** No trade. Keep the pinned definition and write it into
> `portfolio.json`'s COIN-XBT.ST `break_conditions` as words, not as a SEK
> figure that goes stale. Before 09-03: get a fresh certificate quote from
> Avanza, and settle D1 — both feed straight into the check.

```
ACTION: NO ACTION on the position; REAFFIRM the pinned denominator; REJECT
        the proposed redefinition until after 2026-09-03
POSITION: crypto 11.79% (pinned) / 11.94% (Convention A) / 12.66%
          (Convention C) — COIN-XBT.ST 15,240 SEK + ETH 8,875.88 SEK =
          24,115.89 SEK
TARGET: 10%; trim trigger unchanged at >12%, evaluated 2026-09-03
REASON: (1) the check is 23 days away and re-defining its denominator now,
        when the definition is outcome-relevant, is exactly what pinning it
        in advance was meant to prevent — in either direction; (2) the
        certificate price is 8 days stale and user-relayed, so any trim
        sized today would be sized off a guess; (3) the pinned definition
        survives a principled test (tax reserve is not yours, PayPal is),
        which is why it stands rather than merely wins on seniority.
THESIS STATUS: COIN-XBT.ST = WEAKENING. portfolio.json and thesis-review's
        fresh read agree. ETH = UNTESTED, both agree. One key risk eased
        marginally (Fear & Greed 29 vs 25 on 08-06); one did not (BTC -48.9%
        off ATH vs -48.2%).
WHAT CHANGED: the crypto weight did NOT fall this week. The standing
        narrative — "denominator growth will dilute it" — is failing in
        practice: 11.91-11.94% today vs 11.28-11.91% last sweep, flat to
        up. And the newly-computable PayPal balance revealed that the
        cushion under the pinned reading is entirely PayPal-funded.
BREAK CONDITION: quoted from portfolio.json COIN-XBT.ST — "Still above 12%
        of investable capital at the 2026-09-03 sweep -> trim." Denominator
        as pinned 2026-08-10. If a trim fires, trim the certificate, not
        ETH: an ISK sale is tax-free, an ETH disposal is a 30% K4 event with
        an unknown cost basis (P1).
CONFIDENCE: Medium. High on the governance logic; Medium on the weight
        itself, which rests on a stale relayed price and on BTC, which moves
        10% in a week.
HORIZON: Short (<6mo) — tactical, capped at 10% of portfolio per CLAUDE.md,
        and correctly not carrying High confidence.
```

### Call 3 — D2: route 100% of new contributions to equity, and write it down

Two adopted documents now give opposite instructions for the next krona.
`portfolio.json.targets` (adopted 2026-07-27) treats 5% cash as a standing
ballast target, implying every contribution routes some cash.
`investor_profile.json`'s risk-tier framework says the secure tier is
"still INVESTED, not cash sitting idle" and its own `open_items` says new money
routes "100% to secure tier by default" — i.e. 0% to cash. This is no longer
hypothetical: the assumption that crypto's weight self-corrects via denominator
growth is *failing* (Call 2), which means how new money is routed now has a
live consequence.

> **The Contrarian.** Routing 0% to cash assumes the 3-6 month emergency buffer
> really exists outside this portfolio. The profile asserts it does but never
> says where — and the only cash named anywhere in `portfolio.json` is money
> owed to Skatteverket plus 611 SEK of checking. If that buffer is thinner than
> assumed, the "invest everything" rule funds itself by selling equity in a
> drawdown.
>
> **First Principles.** A 5% cash *target* and a "5% of every deposit" *routing
> rule* are different objects: one describes the standing shape of the
> portfolio, the other the marginal krona. Cash is currently 6.49% — above
> target — so the marginal krona has no business going to cash under *either*
> document. The conflict is smaller than it looks; what it needs is a written
> resolution so it stops recurring.
>
> **The Expansionist.** No version of maximum upside routes new money into a
> 0%-yielding SEK balance while equity sits 6.6pp (13,415 SEK) under target
> inside a tax-free wrapper.
>
> **The Outsider.** Two files in the same folder tell you opposite things about
> where your salary goes. Whichever you prefer, one of them has to be edited or
> you will have this exact conversation next month.
>
> **The Executor.** Adopt the portfolio agent's reading. One sentence into
> `portfolio.json.targets.notes`, one annotation on
> `investor_profile.json.risk_tier_framework_proposed.open_items`, done.

```
ACTION: NO ACTION on holdings; resolve D2 — route 100% of new
        contributions to equity while cash sits at or above the 5% target
POSITION: cash 6.49% (13,107.37 SEK) vs 5% target; equity 78.36% vs 85%
TARGET: cash falls passively toward 5% as contributions land in equity; the
        5% line is re-read as "don't let ISK cash sit idle," not "carve 5%
        out of every deposit"
REASON: (1) cash is already above target, so both documents agree on the
        marginal krona even though they disagree on the rule; (2) the
        equity gap is 13,415 SEK and closes in ~4-13 months of 1,000-3,000
        SEK contributions with no sale required; (3) leaving the conflict
        unwritten guarantees it is re-litigated every sweep, which is how
        the "crypto dilutes passively" assumption survived unexamined for
        three weeks.
THESIS STATUS: not applicable — this is an allocation-policy decision, not
        a holding. No thesis_status to cross-check.
WHAT CHANGED: the portfolio agent stated the conflict precisely for the
        first time and showed its practical consequence — the passive
        self-correction both documents rely on is not happening.
BREAK CONDITION: cash falls below 5% of classified capital, or the property
        goal firms up with a date inside ~3 years (the glidepath re-anchor
        trigger in investor_profile.json) -> re-engage a cash/ballast
        routing rule.
CONFIDENCE: Medium. The direction is well-supported; the confidence cap is
        the unverified location of the emergency buffer (scorecard gap 3).
HORIZON: Long (3y+) — this is lever 3, allocation.
```

### Call 4 — PayPal (P3/D1): stop deciding, price it

Two weeks open, three options on the table, no movement. The number is now
sharper than it was: **14,079.79 SEK** today (first sweep both FX rates were
simultaneously fresh), ~563 SEK to clear at the 4% worst-case planning figure,
and — the part that matters — **~1,970-2,630 SEK/yr recurring** on the
4,500-6,000 EUR/yr that arrives this way.

> **The Contrarian.** Two weeks of memo space on a 14,000 SEK balance while
> 120,000 SEK sits in one fund is misallocated attention, and the "test
> transfer" recommendation has itself now been carried unexecuted for a week —
> repeating it is not progress.
>
> **First Principles.** This is not an amount problem, it is a rate problem. A
> recurring 4% toll on a permanent inflow is lever 2 (fee drag), which this
> system ranks above every stock pick in the memo. The blocker is a missing
> price — Revolut's real spread has never been measured — not a missing
> preference, and no amount of deliberation produces the missing number.
>
> **The Expansionist.** Unconstrained, the prize is not the 563 SEK on this
> balance; it is closing a leak that runs for as long as the inflow does. At
> 2,300 SEK/yr midpoint over even five years that is ~11,500 SEK — larger than
> any individual stock position in this portfolio.
>
> **The Outsider.** You are paying a fee you have not measured to a company you
> did not choose for this purpose, on money you already own. Measure it once.
>
> **The Executor.** Move ~100 EUR out of PayPal to Revolut in native currency,
> convert it there, and write down the all-in SEK received. That is a
> ten-minute task and it converts a permanent open question into a number.

```
ACTION: NO ACTION on holdings; EXECUTE the P3 test transfer (option C)
POSITION: PayPal 14,079.79 SEK (1,177.49 USD + 266.88 EUR), outside every
          wrapper, earning nothing
TARGET: full balance routed into the ISK by the cheapest measured route,
        and a standing route for the recurring ~750-1,000 EUR / ~2 months
REASON: (1) the drag is recurring and structural (lever 2), ~1,970-2,630
        SEK/yr, which outweighs the one-off ~563 SEK everyone anchors on;
        (2) the blocker is a missing price, and only a transfer produces it;
        (3) it now also has a portfolio-governance consequence — this
        balance is what keeps the crypto trip-wire from firing on the
        strictest reading (Call 2), so D1 should close before 2026-09-03.
THESIS STATUS: not applicable — idle cash, no thesis.
WHAT CHANGED: the recurring cost became computable for the first time
        (both FX rates fresh in one snapshot), and the balance acquired a
        second-order role in the crypto trip-wire arithmetic.
BREAK CONDITION: Revolut's measured all-in spread comes in at or above
        PayPal's ~4% -> route A (convert inside PayPal) wins and the item
        closes that way instead.
CONFIDENCE: High on "measure before committing"; Low on which route wins,
        because that is the unmeasured thing.
HORIZON: Long (3y+) — a permanent fee decision, not a market call.
```

### Call 5 — ATCO-B, ALFA, ABB, ETH: hold, 23 days left, nothing changed

**This call is genuinely one-sided and I am not going to manufacture tension in
it.** All five voices landed the same way last sweep, nothing in this sweep's
data disturbs any of them, and the situation is identical: four positions with
every thesis field null, 23 days to the 2026-09-03 deadline. Compressed:
*Contrarian* — a missing thesis is a paperwork state, not a business defect,
and none of these companies has deteriorated. *First Principles* — a holding
with no `break_conditions` has no exit rule and can only ever be sold on feel.
*Expansionist* — unconstrained, you would not concentrate further into
global-industrial-cycle exposure at PEG 2.4-2.9 with the tailwind already in
the price. *Outsider* — four companies doing broadly the same thing, bought in
one week, no reason recorded, now two thirds of the picked sleeve. *Executor* —
run `swedish-equity-review` on the three so the sentence is written against
real numbers instead of a blank page.

```
ACTION: HOLD (no add, no trim) on all four; run swedish-equity-review
        retroactively on ATCO-B.ST, ALFA.ST, ABB.ST
POSITION: ATCO-B 2.45% (4,951.80) / ALFA 2.54% (5,137.20) / ABB 1.91%
          (3,848.00) = 6.90% combined, 13,937.00 SEK. ETH 4.40%
          (8,875.88 SEK), quantity frozen at 0.50185.
TARGET: unchanged weights; no adds to any of the four until each has a
        written thesis
REASON: (1) nothing about the businesses deteriorated, so selling on a
        documentation gap takes a real loss for a process reason;
        (2) valuation grades all three Expensive (P/E 33.5 / 28.5 / 37.5,
        PEG 2.41 / 2.92 / 2.70) and thesis-review answers "would I buy
        today" NO on all three, so there is no case to add either;
        (3) ETH cannot even be sold cleanly — cost basis is null (P1), so
        the K4 gain is uncomputable.
THESIS STATUS: UNTESTED on all four. portfolio.json and thesis-review's
        fresh read agree on every one; thesis-review explicitly refused to
        answer "would I buy today" for ETH rather than invent a thesis to
        grade against, which is the correct answer.
WHAT CHANGED: nothing — and that is the finding, one week on and 23 days
        from the deadline. One genuine new datapoint on ABB: forward P/E
        36.7x is flat against trailing 37.5x despite 14.2% revenue growth,
        which is a margin-compression flag and belongs in whatever thesis
        eventually gets written.
BREAK CONDITION: cannot be quoted — break_conditions is null on all four,
        which is precisely the defect. Substitute process condition, unchanged
        and binding: no written thesis by the 2026-09-03 sweep -> all four
        move to the rotation list, ineligible for adds, ranked against the
        Watchlist on the next scout run.
CONFIDENCE: High — every lens and every voice agrees on both halves
        (don't sell, don't add).
HORIZON: Medium (6mo-3y)
```

---

## 5. Where the agents disagreed

1. **Crypto: "cheap on cycle position" vs "wrong side of its own regime" —
   unresolved, and it should stay unresolved.** The stored COIN-XBT.ST
   `valuation_reason` in `portfolio.json` still reads "BTC still -48.2% off its
   ATH — the 'cheap vs history' leg still holds directionally," and the original
   user thesis is "positive buy-in signals now." Macro-regime says the opposite
   about *this specific sleeve*: crypto is the one genuinely Risk-Off part of a
   bifurcated picture (Fear & Greed 29, BTC -48.9% off ATH, ETH -61.8%, dollar
   index 119.06 at a level that historically pressures crypto), and it named
   this tension itself, asking that it not be smoothed over. Note that
   **valuation refused to take the cheap side this sweep** — it said explicitly
   that ATH-distance is cycle position, not a valuation call — so the "cheap"
   framing now lives only in the stored thesis, not in a live agent read.
   Cheap-in-a-fear-regime-with-a-strong-dollar frequently gets cheaper first.
   **Resolution: neither add nor pre-emptively trim; the pre-committed 09-03
   trip-wire settles it. Confidence Low-to-Medium, explicitly regime-dependent
   and capable of flipping on one BTC print.**
2. **Denominator: the portfolio agent's recommended standing convention
   contradicts the pinned trip-wire definition.** Detailed in Call 2. Convention
   A includes the tax reserve and excludes PayPal; the pin does the reverse.
   They agree today to within 0.15pp and would diverge the moment PayPal moves
   — and a third reading (Convention C) is already over the line. **Resolution:
   the pin governs the trip-wire; Convention A may be used for scorecard drift
   **only if labelled as a different number**. Confidence High on the
   governance, Medium on which convention is philosophically right.**
3. **Two adopted documents, opposite instructions for new money.** `targets`
   says 5% cash ballast; `investor_profile.json` says 100% to the secure tier,
   0% cash. **Resolution: Call 3, route to equity. Confidence Medium** — and
   this needs writing into the files, not arbitrating again next week.
4. **Industrials: favoured by the regime, expensive on fundamentals, untestable
   on thesis.** Macro says cyclicals/industrials are what this regime rewards
   (VIX 15.46, 10y-2y +0.46, no recession signal) — *and in the same breath*
   flags that this read rests on thin, reversible signals and that the cluster
   is concentration into the less-certain side. Valuation grades three of four
   Expensive. Thesis-review has three of four at UNTESTED. **Resolution: hold,
   no adds, thesis deadline stands. Confidence High.**
5. **INVE-A: valuation refuses to grade it, thesis-review grades it WEAKENING.**
   Valuation says "insufficient data to call cheap/fair/expensive" — the 4.8x
   P/E is a holding-company artifact and the real metric, NAV discount/premium,
   has never been obtained (S6). Thesis-review calls it WEAKENING. Read the
   fine print: that WEAKENING rests on *price position* (97th percentile — the
   "good upside" the user cited has been captured) and on the *absence* of NAV
   data, **not** on deteriorating fundamentals (ROE 27.3%, lowest leverage in
   the book at D/E 11.6%). **Do not read INVE-A as a deteriorating business.**
   Same shape applies to SHB-A: valuation calls it Fair on a 12.2x multiple;
   thesis-review calls it WEAKENING because that multiple is cheap *because*
   revenue is falling 3.8% YoY and consensus is "underperform." Combined
   position: 2,218.35 SEK, 1.10% of capital. **Resolution: no action, this is
   process, not economics. Confidence High.**
6. **One disagreement closed this sweep, worth recording.** S11 flagged that
   valuation/thesis-review reported price ÷ 52-week high while calling it "% of
   range," against `position_report.py`'s true percentile. This sweep the two
   agree by construction: valuation reports AZN at "31.9% of range (true
   percentile)" against the report's 32%, and ABB at 78.0% against 78%.
   Thesis-review still uses "% of 52-week high" (ATCO-B "99.0%") but now
   **labels it as such**, which is the other half of the S11 fix. The
   spot-check S11 asked for passes.

---

## 6. Broken theses requiring a decision

None broken. Pulled from thesis-review unsoftened; no stored `thesis_status`
disagreed with this sweep's independent re-test.

| Holding | Status | Would I buy today? |
|---|---|---|
| AZN.ST | **INTACT** | YES — every stated leg checks out (beta 0.211, 4yr rising revenue, margins intact, PEG 1.38, 32nd percentile) |
| Avanza Global | **INTACT** | YES — cheapest holding, no break condition triggered |
| Avanza Auto 3 | **INTACT** | YES |
| VOLV-B.ST | **TOO_EARLY** | YES BUT SMALLER — TTM revenue growth turned positive (+2.7%) after a 2-year decline; D/E still 147 |
| SHB-A.ST | **WEAKENING** | NO — valuation. Now only 1.9% below its 52w high: the "good upside" leg is captured, not pending |
| INVE-A.ST | **WEAKENING** | HOLD ONLY — no fresh entry defensible near a 52w high with no NAV data (S6) |
| COIN-XBT.ST | **WEAKENING** | NO — valuation; cheaper certificate identified but pending (P4) |
| ATCO-B.ST / ALFA.ST / ABB.ST | **UNTESTED** | NO on all three — valuation |
| ethereum | **UNTESTED** | UNKNOWN — thesis-review refused to answer rather than invent a thesis to grade against |

**The one genuinely new item here:** Volvo's TTM revenue growth turned
**positive (+2.7%)** after two years of decline. That is consistent with the
recovery thesis, not confirmation of it — the break condition requires 3+
months and the position is ~1 week old. It is the first piece of evidence in
that position's favour, and it is worth noticing precisely because the price
went the other way (-2.0% today, -3.5% vs cost).

---

## 7. Rebalancing actions

From the portfolio agent, tax-priority order, with the Council's ruling:

| Step | Action | Amount | Council ruling |
|---|---|---|---|
| a | Deploy idle Avanza ISK cash | ~1,743.61 SEK (computed, excludes courtage, not broker-confirmed) | **DO IT — but to AZN.ST (1 share, ~1,543.50), not Avanza Global.** Call 1. If the Avanza Global order is already placed, leave it. |
| b | ISK/KF sales (crypto trim) | ~0-3,926 SEK depending on reading | **NOT NOW** — Call 2. The 09-03 wire governs; the certificate price is 8 days stale. If it fires, trim COIN-XBT.ST, never ETH. |
| c | AF sales | — | None available; the only AF holding is the frozen SEB Osteuropafond. |
| d | Self-custody crypto sale | — | **NOT PROPOSED** — ETH has no thesis (P5) and no cost basis (P1); the K4 gain is literally uncomputable. Do not open a taxable event to answer an allocation question that has not been confirmed. |
| — | PayPal routing (P3) | 14,079.79 SEK, ~1,970-2,630 SEK/yr recurring drag | **BLOCKED on D1** — not a rebalancing action, but the most time-sensitive money item on the page. Call 4. |

**Residual equity gap after step (a): ~11,872 SEK (-5.9pp).** That closes via
ordinary 1,000-3,000 SEK/month contributions in roughly 4-12 months. **No sale
is needed to reach the equity target** — worth stating plainly, because
"equity 78.4% vs 85%" reads like a corrective trade and is not one.

**One thing step (a) does *not* do:** it moves cash into equity inside the same
denominator, so it leaves the crypto weight unchanged at 11.94%. Only new money
or market moves shift that.

---

## 8. Open actions (things you can just go do)

| ID | Action | Amount / deadline |
|---|---|---|
| — | Buy 1 share AZN.ST with the available ISK cash | ~1,543.50 SEK, Monday. Use the broker's real balance, not the computed 1,743.61. |
| P3 | Move ~100 EUR out of PayPal to Revolut in native currency, convert there, record the all-in SEK received | Before 2026-09-03 — it feeds the crypto denominator as well as closing D1 |
| P6 | Get a fresh COIN-XBT.ST price from Avanza | **Before 2026-09-03** — the trip-wire check needs a real number; the current one is 8 days stale |
| P4 / S1 | Get verified tickers + current fees for cheaper Nordic BTC ETPs on Avanza; add them to the Excel Watchlist tab | No deadline; saves ~230 SEK/yr. Tickers must not be guessed. |
| — | Write one sentence each for ATCO-B, ALFA, ABB, ETH in `portfolio.json` | **2026-09-03.** Format that counts as complete: "own it because X; expect Y to drive it; sell if Z." |
| P1 | Dig out the ETH cost basis | No deadline, but it gates any sale and any return figure |
| P7 | Confirm the ISK allowance threshold with Skatteverket | Low priority — ~181k ISK against an assumed ~300k, so this is confirmation, not a live problem |

System work, not yours: run `swedish-equity-review` retroactively on ATCO-B.ST,
ALFA.ST, ABB.ST (P6, named for the fifth sweep running); P2's two remaining
ports (discovery funnel, consolidated sweep report) are still open and are not
blocking anything this week.

## 9. Open decisions (forks the data does not settle)

**D1 — PayPal routing (P3). 14,079.79 SEK, plus ~4,500-6,000 EUR/yr arriving
the same way.**

| Option | Trade-off |
|---|---|
| **A.** Convert inside PayPal, transfer SEK to Avanza, buy | Done this week. Costs ~563 SEK now and sets the precedent for ~1,970-2,630 SEK/yr forever. |
| **B.** Transfer out in native currency to Revolut, convert there | Plausibly much cheaper, entirely unpriced — Revolut's real spread has never been measured. Adds days and one unknown. |
| **C.** Test transfer (~100 EUR) via B, price it, then move the rest by whichever wins | Costs one more week and a few SEK of friction; converts a permanent recurring cost into a measured number once. **Council's recommendation (Call 4).** |

**D2 — Where new contributions go.** Two adopted documents, opposite
instructions.

| Option | Trade-off |
|---|---|
| **(a)** Route 100% to equity until cash falls below 5%; write it into `portfolio.json.targets.notes` and annotate `investor_profile.json`'s conflicting `open_items` line | **Council's recommendation (Call 3).** Closes the equity gap fastest; assumes the 3-6 month emergency buffer really sits outside the portfolio (unverified — scorecard gap 3). |
| **(b)** Keep a literal 5%-of-each-deposit cash carve-out | Builds ballast you may not need, on top of cash already above target, inside a tax-free wrapper earning nothing. Defensible only if the emergency buffer turns out to be thinner than the profile claims. |
| **(c)** Leave both documents as-is and let the Council arbitrate each sweep | Status quo. It has now produced one live conflict and one failed assumption in two weeks; it will recur monthly. |

**D3 — Which denominator governs the 2026-09-03 crypto check.** New this sweep;
it must be settled **before** 09-03, not on the day.

| Option | Trade-off |
|---|---|
| **(a)** Keep the 2026-08-10 pin — total less tax reserve less checking, PayPal included. Crypto = **11.79%**, wire does not fire | **Council's ruling (Call 2).** Principled (PayPal is your money, the tax reserve is not) and set before it was outcome-relevant — but it is the loosest of the three readings and its cushion is entirely PayPal-funded. |
| **(b)** Adopt Convention C — Avanza ISK + ETH wallet only. Crypto = **12.66%**, wire is **already breached**, trim ~5,000 SEK of COIN-XBT.ST | The strictest honest reading of "investable capital," since PayPal money cannot be deployed today without paying ~4%. Costs a tax-free ISK sale and ~125 SEK/yr of saved fees; the price to size it against is 8 days stale. |
| **(c)** Adopt Convention A as the single standing convention for everything. Crypto = **11.94%** | Ends the two-numbers problem — but it changes the pin's *definition* while landing near its *magnitude*, which is the least transparent of the three moves. |

---

## 10. Cost of being wrong

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| 1 — Buy 1 AZN.ST instead of Avanza Global | A 20-30% global drawdown on the new 1,543.50 SEK: **310-460 SEK**. The genuine incremental risk over the index-fund alternative is single-name pharma risk (pipeline/patent event) on the whole 9,261 SEK position: **1,850-2,780 SEK**. | Yes. Long horizon, no leverage, and the position stays under 5% of capital. |
| 2 — No trim, wait for 09-03 | Crypto is 3,926 SEK above its 10% target. A 30% BTC fall inside 23 days costs roughly **1,180 SEK** versus having trimmed today. | Fully. The countervailing cost of overriding a pinned rule early is not SEK-denominated but recurs every week. |
| 3 — Route 100% of new money to equity | Direct cost ≈ **0 SEK** while cash is above target. The real downside is behavioural: if the emergency buffer is thinner than the profile claims, a cash need in a drawdown forces an equity sale at the wrong time — realistically **1,000-3,000 SEK** of avoidable loss on one such sale. | Yes, and preventable by confirming where the buffer is held. |
| 4 — Test transfer before committing | One week of delay plus a few SEK of test friction: **~10-50 SEK**. Doing nothing instead costs **~563 SEK now and ~1,970-2,630 SEK/yr**. | Yes. This is the one row where inaction is the expensive option. |
| 5 — Hold ATCO-B/ALFA/ABB/ETH with no thesis | A de-rating from PEG 2.4-2.9 toward market multiples on 13,937 SEK is **3,480-4,180 SEK**. A 50% crypto drawdown on ETH is **~4,440 SEK** (maximum 8,875.88). The unrecoverable part is structural: with `break_conditions` null, nothing tells you when to exit, so a slow de-rating gets held all the way down. | Yes on the money. No on the time spent holding four positions you cannot grade. |

---

## 11. Data quality notes this sweep

- **Swedish CPI is period 2025M12**, over 7 months stale (S4). Macro correctly
  declined to compute a Swedish real rate at all rather than publish one
  against a stale input.
- **`position_report.py` still does not reprice self-custody crypto** (S7,
  confirmed unfixed, fix is specified in the S-item). ETH corrected by hand to
  8,875.88 SEK in this memo, as it was last sweep.
- **COIN-XBT.ST**: no working ticker (permanent, not an outage). Price is
  user-relayed from 2026-08-03, 8 days stale, and is load-bearing for the
  crypto weight.
- **Earnings dates: none, for any ticker** (S3, root-caused — `fetch_calendar.py`
  still routes through yfinance's client). Call 1 recommends a single-stock
  purchase that has not been checked against a reporting date. Stated, not
  estimated.
- **Dollar index 119.06 is a level with no prior fetched**, so macro could not
  confirm a trend — the "elevated dollar pressures crypto" read is a
  level-based claim, not a momentum one.

---

## 12. Learning notes

- **A limit that only holds because of money you can't reach isn't holding.**
  The crypto trip-wire reads 11.79%, 11.94% or 12.66% depending on the
  denominator — and the only reason the loosest reading clears 12% is that
  14,079.79 SEK of PayPal balance is counted as investable capital. That money
  is genuinely yours (so counting it is defensible) but costs ~4% to move (so
  excluding it is also defensible). The general lesson: when a threshold is
  close, look at *what is in the bottom of the fraction* and ask whether you
  could actually spend it. Here, an unresolved fee decision (D1) is quietly
  underwriting a risk limit (D3) — two items that look unrelated on the list.
- **Beta is a claim until a red day tests it.** AstraZeneca's thesis says
  "lower-beta than high-valuation growth" and its measured beta is 0.211,
  meaning it should move about a fifth as much as the market. Today six of
  seven stocks fell and AZN rose 1.4%. One day proves nothing statistically,
  but it is the difference between a thesis you asserted and a thesis you have
  seen behave — which is exactly what `thesis_status: INTACT` is supposed to
  mean, and why it carries more weight than the four positions marked UNTESTED.
- **"Would I buy this today?" catches errors that "is the thesis intact?"
  misses.** Last sweep routed cash to the index fund because "the medium tier
  has no vetted candidate." Thesis-review's would-buy-today column said YES to
  AZN.ST that same sweep — the candidate was sitting in the book. Re-asking a
  holding as a fresh purchase decision, rather than as a position to maintain,
  is what surfaced the mistake. This is a reason to read that column as a *buy
  list*, not just a health check.
- **Same label, different definition — the S11 problem moved up a level.** The
  "% of 52-week range" ambiguity got fixed this sweep (valuation now reports the
  true percentile and thesis-review labels its own metric distinctly). But the
  identical failure immediately reappeared one level up: two "investable
  capital" denominators that agree to 0.15pp today and would diverge whenever
  PayPal moves. The fix is the same both times — pin the *definition* in words,
  not the number, because the number goes stale and the definition is what you
  are actually arguing about.

---

*Nothing in this memo executes. You decide.*
