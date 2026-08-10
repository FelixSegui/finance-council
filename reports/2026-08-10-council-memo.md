# Council memo — 2026-08-10

*Structured synthesis of this system's own agents (market-data, valuation,
macro-regime, portfolio, thesis-review, calendar). Not advice from a licensed
advisor. Every number traces to `data/cache/snapshots/20260810T061323.json`,
`data/portfolio.json`, or an agent output from this session.*

Snapshot: `20260810T061323.json` (2026-08-10 06:13 UTC) · previous:
`20260806T130256.json` · no Excel import this sweep.

---

## 1. Position report

## Position report — 2026-08-10

Snapshot: `20260810T061323.json` · previous: `20260806T130256.json`

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 148.90 | +0.8% | +15.2% | 98% | 148.90 | fetched |
| Investor A (stock) | 415.80 | +0.0% | +43.3% | 98% | 2,079.00 | fetched |
| Volvo B | 362.00 | -1.2% | -1.5% | 90% | 4,706.00 | fetched |
| Atlas Copco B | 183.80 | -0.1% | +1.4% | 98% | 4,962.60 | fetched |
| AstraZeneca | 1,522.50 | -1.5% | +0.8% | 28% | 7,612.50 | fetched |
| Alfa Laval | 572.40 | +0.9% | -0.3% | 89% | 5,151.60 | fetched |
| ABB | 964.60 | -0.5% | +1.9% | 79% | 3,858.40 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| CoinShares XBT Provider Bitcoin Tracker One (certificate) | no data | no data | no data | - | 15,240.00 | FETCH FAILED |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| ETH (self-custody wallet) | no data | no data | no data | - | 8,911.00 | user-relayed |

*52w range: 0% = at the 52-week low, 100% = at the 52-week high.*

### Crypto context (spot, from CoinGecko)

| Coin | Price (EUR) | Δ vs prev snapshot | 7d | 30d | vs ATH |
|---|---|---|---|---|---|
| bitcoin | 56,384.00 | +1.1% | +3.7% | +1.5% | -47.6% |
| ethereum | 1,665.14 | +1.3% | +3.6% | +7.1% | -60.6% |

*Bitcoin is the agreed directional proxy for the XBT certificate, which has no working ticker. It indicates direction, not the certificate's actual price — that comes from the user.*

**Reading it.** Nothing moved enough to matter. The widest four-day swing in
the individual-stock sleeve is AstraZeneca at -1.5%, and every other name is
inside ±1.2% — this is noise, not signal, and no move this week contradicts
any holding's thesis. Volvo B (-1.2%, now -1.5% vs cost) is the only position
underwater, and at roughly one week held that is exactly the "too early to
read anything into" state thesis-review assigns it. The index funds (Avanza
Global 55.5% of the portfolio, Auto 3 7.5%) are deliberately buy-and-hold and
carry no fund NAV in this snapshot; nothing to say about them.

**Two data corrections you should see, both of which cut in your favour.**

1. **The ETH line above is stale and understated.** `position_report.py` did
   not reprice the self-custody wallet from today's fetched crypto data — it
   carried the 2026-08-03 book value. Correct figure from today's snapshot:
   0.50185 ETH × 1,665.14 EUR × 10.9739 SEK/EUR = **~9,170 SEK**, +259 SEK
   (+2.9%) versus the 8,911 printed. Every weight in this memo uses 9,170.
   This is a real system gap — the script reprices fetched equities but not
   user-held spot crypto — and it is flagged below as an S-item candidate for
   `meta`, not silently patched here.
2. **The "52w range" column and the valuation agent's "% of 52w range" are
   two different measurements.** The table above reports a true percentile
   within the 52-week low-to-high band; valuation and thesis-review report
   price divided by the 52-week high while calling it "range." For AstraZeneca
   that is the difference between "79.1% of 52w range" (sounds mid-pack) and
   **28th percentile** (near the bottom of its own year). The percentile is
   the more informative number, and it makes AZN look better, not worse. See
   *Where the agents disagreed*.

---

## 2. What should change

Six things, in order. Three are actions you take, two are system work, one is
a decision you owe an answer to.

1. **Deploy the 1,743.61 SEK of idle ISK cash into Avanza Global.** Monday
   morning, one order, zero friction, zero tax event. It is the only cash in
   the portfolio with no competing claim on it.
2. **Run `swedish-equity-review` retroactively on ATCO-B.ST, ALFA.ST and
   ABB.ST.** This is P6's own stated next step and it has never been done.
   It is system work, not your work — it produces the evidence baseline that
   a thesis can actually be written against, instead of the memo asking you a
   fourth time for prose with nothing behind it.
3. **Write one sentence each for ATCO-B, ALFA, ABB and ETH — deadline
   2026-09-03.** Default if not done: all four move to the rotation list and
   stop being eligible for adds. See Headline call 1 and 2.
4. **Answer the PayPal routing question (P3).** 14,146.43 SEK is sitting
   outside every wrapper earning nothing, and the route out has been an open
   item for a week. Options in *Open decisions*.
5. **Pin the crypto trip-wire denominator before 2026-09-03.** Done in this
   memo (Headline call 3) — the check is closer to firing than the headline
   percentage suggests, and it must not be decided by an accounting choice.
6. **Nothing else.** No buys beyond item 1, no trims, no rotations, no new
   candidates. `scout` was not invoked and should not have been — the
   emphasis is portfolio-tending, four owned positions are unreviewed, and
   adding candidates on top of that would make the backlog worse.

---

## 3. Portfolio health scorecard

Carried over from the portfolio agent verbatim. Total investable capital
~216,373 SEK (up from ~214,175 on 2026-08-04), with ETH repriced to 9,170 SEK.

| Dimension | Status | Detail |
|---|---|---|
| Asset allocation vs targets | **WATCH** | Equity 73.14% vs 85% target (-11.86pp / -25,684 SEK); crypto 11.28% vs 10% (+1.28pp); cash 12.60% vs 5% (+7.60pp) — driven mostly by undeployed cash, not market moves. |
| Equity sector concentration | **ACT** | Industrials 65.49% of the individual-stock sleeve, down from 68.99% last sweep but only via price drift, not a structural fix — 4 of 7 individual stocks are Industrials. |
| Geography | **OK** | Stock sleeve is 100% Nasdaq Stockholm but only 13.2% of total; Avanza Global at 55.5% of total offsets home bias at the whole-portfolio level. |
| Currency exposure | **UNKNOWN** | No revenue-currency breakdown available for fund underlyings. |
| Single-position concentration | **WATCH** | Avanza Global 55.46% of total technically breaches the 15% cap by letter, but is a diversified index fund, not single-company risk — flagged, not ACT. Largest individual stock is AZN.ST at 3.52%. |
| Institution concentration | **ACT** | Avanza 83.97% of total, breaches the 80% cap — real platform/counterparty concentration. |
| Fee drag | **OK** | 0.26% of total, under the 0.4% cap. COIN-XBT.ST at 2.5%/yr (381 SEK/yr) is the one holding over the 0.5%-per-fund flag threshold — already P4. |
| Wrapper efficiency | **OK** | All active capital in ISK, ~118,307 SEK headroom vs the unverified ~300k threshold. Only AF position is the frozen, immaterial SEB Osteuropafond. PayPal's 14,146.43 SEK idle cash is a deployment gap, not a wrapper mismatch. |
| Drawdown-tolerance fit | **UNKNOWN** | No backtest exists — S5, still open. |

**The scorecard is provisional in one place, and it is the same place as last
week.** `investor_profile.json` has no TBDs blocking it, but the adopted
85/10/5/0 target (written in 2026-08-03 on your explicit instruction) has
**never been tested against your stated -30% max drawdown tolerance** (S5).
An 85% equity + 10% crypto portfolio plausibly draws down more than 30% in a
bad year. Unanswered question: *does the target you adopted actually respect
the risk limit you stated?* Until `backtest` runs, "Asset allocation vs
targets = WATCH" is measuring drift against a number that has itself never
been validated.

**Denominator caveat on the WATCH row — this matters and is not cosmetic.**
The 12.60% cash figure includes 11,363.76 SEK that is not yours to allocate:
the confirmed tax reserve (10,752.76) plus the Handelsbanken checking balance
(611). Actual deployable idle cash is 15,890.04 SEK. Strip the committed money
from both sides and the picture is: equity 77.18% (gap -7.8pp / ~16,000 SEK,
not -11.86pp / 25,684), cash 7.75%, **crypto 11.91%**. The equity gap is
smaller than the scorecard implies and the crypto weight is larger. That
second number is the subject of Headline call 3.

**Structure (levers 1-2), one line, closed:** all capital in the ISK, fee drag
0.26% against a 0.4% cap, nothing broke this week. The one open fee item is
the 2.5% BTC certificate (P4), blocked on S1.

---

## 4. Headline calls

### Call 1 — ATCO-B, ALFA and ABB: hold, but the process gap now gets a deadline and a default

This is the week where three separate lenses land on the same three names for
three different reasons, and the memo's job is to say so rather than average
it out. **Thesis-review**: UNTESTED, all thesis fields null, "sharpest
UNTESTED case this sweep," would-I-buy-today NO on all three. **Valuation**:
all three Expensive — ATCO-B P/E 33.43x / PEG 2.40, ALFA P/E 28.74x / PEG
2.92, ABB P/E 37.04x / PEG 2.69 with P/B 109.54x and FCF conversion of ~4.4%
against a 16.9% operating margin. **Macro-regime**: industrials sit on the
favoured side of the current regime — no recession signal, no curve
inversion, VIX 15.15 — *but* every one of them trades within a few percent of
its 52-week high, so "the regime tailwind is already priced in, not fresh
support."

> **The Contrarian.** The strongest reason this framing fails: "no written
> thesis" is a paperwork state, not a business defect. Atlas Copco, Alfa Laval
> and ABB are three of the highest-quality industrial franchises in Europe, and
> a memo that has spent two sweeps escalating a documentation gap into a
> quasi-sell-signal is confusing its own process failure with a portfolio
> problem. Nobody has produced a single fact suggesting any of these companies
> is deteriorating.
>
> **First Principles.** Strip the framing: you own three businesses and cannot
> state why. That is not a filing problem — it means there is no condition
> under which you would ever sell them, because there is no claim to falsify.
> A position you can't be wrong about is a position you can't manage, and at
> high multiples that is where permanent capital loss comes from: not from the
> drawdown, but from having no rule that tells you whether to add or exit.
>
> **The Expansionist.** Ignore the SEK constraint. If capital were unlimited,
> would you concentrate into these? No — and that is the tell. The
> maximum-upside version of this portfolio does *not* put more money into
> global-industrial-cycle exposure at PEG 2.4-2.9 with the cycle tailwind
> already in the price; it puts it into whichever asset still has an unpriced
> claim. The expansive answer and the modest one point the same way: don't add.
>
> **The Outsider.** Described cold: a person bought four companies that do
> broadly the same thing — sell capital equipment into global industry — inside
> one week, without recording a reason, and they now make up two thirds of the
> individually-picked part of the portfolio. That sounds like one bet made four
> times, not four decisions. Nobody needs an investing background to find that
> odd.
>
> **The Executor.** Constraints back on: you cannot force prose out of yourself
> on a schedule, but the system can produce the evidence. Monday, run
> `swedish-equity-review` on ATCO-B.ST, ALFA.ST and ABB.ST — P6 has listed this
> as the next step since 2026-08-03 and it has never run. Then writing one
> sentence each is a five-minute job against real numbers instead of a blank
> page.

```
ACTION: HOLD (no add, no trim) + run swedish-equity-review retroactively
POSITION: ATCO-B 2.29% (4,962.60 SEK) / ALFA 2.38% (5,151.60) / ABB 1.78%
          (3,858.40) — 6.46% combined, 13,972.60 SEK
TARGET: unchanged weights; no adds until each has a written thesis
REASON: (1) nothing about the businesses has deteriorated, so selling on a
        documentation gap would be a real loss taken for a process reason;
        (2) but three of the four industrials are Expensive on PEG with the
        regime tailwind already priced, so there is no case to add either;
        (3) the escalation the situation warrants is evidence, not another
        request for prose — the retroactive review has been the stated next
        step for a week and has never run.
THESIS STATUS: UNTESTED (all three). portfolio.json thesis_status and
        thesis-review's fresh read agree — no disagreement to disclose.
WHAT CHANGED: nothing in the holdings, and that IS the finding. One week
        after being named the #1 issue, why_owned / expected_driver /
        valuation_reason / key_risks / break_conditions are all still null on
        all three. Meanwhile ATCO-B sits at the 98th percentile of its
        52-week range, ALFA the 89th, ABB the 79th — so the "we bought at a
        decent entry" argument that could have been written retroactively is
        weaker now than it was on 2026-08-06.
BREAK CONDITION: cannot be restated from the file — break_conditions is null
        for all three, which is precisely the defect. Substitute process
        condition, which now binds: no written thesis by the 2026-09-03
        sweep -> all three move to the rotation list, ineligible for adds,
        and are ranked against the Watchlist on the next `scout` run.
CONFIDENCE: High — all five voices and all three lenses agree on both halves
        (don't sell, don't add).
HORIZON: Medium (6mo-3y)
```

### Call 2 — ETH: hold, freeze the quantity, first reduction candidate once P1 closes

Eleven-plus sweeps at `thesis: TBD`. This is the standing P5 example and it
has now outlasted every other open item on the list.

> **The Contrarian.** ETH is 9,170 SEK — 4.2% of the portfolio. Two sweeps of
> memo real estate on a position whose entire value is less than one month's
> movement in Avanza Global is misallocated attention, and the "no thesis"
> complaint is being applied more harshly here than the amount justifies.
>
> **First Principles.** The size argument is exactly backwards. The reason ETH
> matters is not its weight, it is that it is the cleanest test of whether this
> system's thesis discipline is real or decorative. If a position can sit at
> "TBD" for eleven sweeps with no consequence, the requirement is theatre and
> every other thesis field is optional too.
>
> **The Expansionist.** Unconstrained: ETH is -60.6% off its all-time high and
> +7.1% over 30 days, outrunning BTC's +1.5% — the maximum-upside read is that
> this is the more beaten-down, faster-recovering asset of the two and deserves
> to be the crypto sleeve's core, not its orphan. But that argument cannot be
> made, because there is no stated reason to prefer ETH over BTC, so there is
> nothing to be right about.
>
> **The Outsider.** If someone said "I hold this, I don't know why, I don't
> know what I paid, and I can't say what would make me sell," the natural
> response is not to build a policy around it — it is to ask why it is still
> there. The honest answer is inertia plus a missing cost basis.
>
> **The Executor.** Do not sell: cost basis is null (P1), so the K4 gain cannot
> even be computed, and selling a position whose tax consequence is unknowable
> is worse than holding one whose rationale is unwritten. Freeze it — never add
> — and put one sentence in `portfolio.json` this month.

```
ACTION: HOLD — quantity frozen at 0.50185 ETH, no adds under any condition
POSITION: 4.24% of total (9,170 SEK); part of a crypto sleeve at 11.3-11.9%
TARGET: no change now; first reduction candidate once P1 (cost basis) closes
REASON: (1) selling is blocked on P1 — a self-custody disposal is a 30% K4
        event and the taxable gain literally cannot be computed today;
        (2) the ISK trim route (Call 3) achieves the same crypto-weight goal
        at zero tax cost, so ETH is not the cheap leg to cut regardless of
        thesis status; (3) freezing costs nothing and stops the position
        growing while it remains unjustified.
THESIS STATUS: UNTESTED. portfolio.json and thesis-review agree. Thesis-review
        answers "would I buy today" as UNKNOWN and says so plainly rather
        than guessing — that is the correct answer, not an evasion.
WHAT CHANGED: repriced +259 SEK (+2.9%) to ~9,170 SEK once the stale carry was
        corrected; ETH's 30-day move (+7.1%) is now materially ahead of BTC's
        (+1.5%). Neither fact can support a thesis call, because there is no
        thesis to support.
BREAK CONDITION: null in the file. Substitute, two-part: (a) no written thesis
        by 2026-09-03 -> ETH is classified as held-by-inertia and becomes the
        default reduction target the moment P1 resolves; (b) P1 resolving at
        any time -> re-open the sell question on its merits.
CONFIDENCE: High on the hold (tax mechanics are not a judgment call); Low on
        anything about ETH's prospects, because nothing has been claimed.
HORIZON: Medium
```

### Call 3 — Crypto trip-wire: not fired, but closer than the headline number says. Pin the denominator now.

The 2026-08-06 Council set the rule: trim COIN-XBT.ST if crypto is still above
**12% of investable capital at the 2026-09-03 sweep**. Today is 2026-08-10;
the check is three weeks out and is **not due**. But this sweep produced three
different values for the same holdings:

| Denominator | Crypto weight | Source |
|---|---|---|
| Total incl. tax reserve + checking (216,373) | 11.28% | portfolio agent |
| 2026-08-04 account definition (214,394) | 11.4% | thesis-review |
| Deployable capital, tax reserve + checking excluded (205,009) | **11.91%** | Council arithmetic on the portfolio agent's own figures |

Same 24,410 SEK of crypto, a 0.63pp spread, and a trip-wire at 12.00%. The
third figure is 0.09pp from firing.

There is also a live disagreement to name: **the portfolio agent proposes
trimming COIN-XBT.ST by ~2,772.72 SEK today** (Step 2 of its rebalancing plan,
to hit 10% exactly) — which would override a standing Council decision three
weeks before its own evaluation date.

> **The Contrarian.** The trip-wire is arbitrary. 12% is a number this system
> invented; there is no evidence a 11.9% crypto sleeve is riskier than a 10%
> one in any way that matters, and the portfolio agent is right that trimming
> to target today is cheap, tax-free and removes the argument entirely.
>
> **First Principles.** What is a trip-wire actually for? It exists to stop a
> weekly re-litigation of the same position on noise — to convert "how do I
> feel about crypto this Monday" into a pre-committed rule. Overriding it three
> weeks early, on no new evidence, does not just make one trade; it destroys
> the mechanism, and then next week's crypto question is open again.
>
> **The Expansionist.** Ignore the constraint: is there an upside case for
> being *over* 10% crypto right now? Macro says no, unambiguously — Fear &
> Greed 30, BTC -47.6% off ATH, dollar index 119.70 elevated, and its verdict
> was that crypto is "on the wrong side of its own regime, full stop." The
> maximum-upside version of this portfolio is not a bigger crypto sleeve.
>
> **The Outsider.** Told cold: you set a rule three weeks ago, the number is
> under the rule's threshold, and someone wants to act anyway. That is not a
> new decision, that is not following the rule you made. Either the rule was
> wrong when you made it — say so — or wait three weeks.
>
> **The Executor.** No trade this week. Write the denominator into the trip-wire
> so the 09-03 check is arithmetic, not a judgment call: **deployable capital,
> tax reserve and checking excluded — 205,009 SEK today.** On that basis crypto
> is 11.91% and the wire has not fired. Get a fresh COIN-XBT.ST price from
> Avanza before 09-03 so the check runs on a real number, not a 4-week-old
> relayed one.

```
ACTION: NO ACTION on the position; SPECIFY the trip-wire denominator
POSITION: crypto 11.28% (total denom) / 11.91% (deployable denom) —
          COIN-XBT.ST 15,240 SEK + ETH 9,170 SEK = 24,410 SEK
TARGET: 10%; trim trigger unchanged at >12% evaluated 2026-09-03
REASON: (1) the wire has not fired on any of the three denominators, and
        overriding a pre-committed rule three weeks early on zero new
        evidence is the exact churn the rule exists to prevent; (2) the
        weight is drifting toward the threshold, not away, so the check on
        09-03 is live and must not be decided by an accounting choice —
        hence the denominator is pinned now, before it is outcome-relevant;
        (3) COIN-XBT.ST's price is user-relayed and 7 days stale, so any
        trim sized today would be sized off a guess.
THESIS STATUS: COIN-XBT.ST = WEAKENING. portfolio.json and thesis-review
        agree. One key risk eased marginally: Fear & Greed 30 ("Fear") vs 25
        ("Extreme Fear") on 08-06, and BTC -47.6% off ATH vs -48.2%.
WHAT CHANGED: the denominator sensitivity itself — this is the first sweep
        where the choice of denominator moves the answer by more than the
        distance to the threshold. Also: the portfolio agent now recommends
        an immediate trim, which last sweep's Chairman ruling does not
        authorise.
BREAK CONDITION: quoted from portfolio.json COIN-XBT.ST break_conditions —
        "Still above 12% of investable capital at the 2026-09-03 sweep ->
        trim." Now specified: "investable capital" = total less the
        confirmed tax reserve (10,752.76) and hb-checking (611).
CONFIDENCE: Medium. The rule-following logic is High-confidence; the weight
        itself rests on a stale user-relayed certificate price and on BTC,
        which can move 10% in a week.
HORIZON: Short (<6mo) — tactical, capped at 10% of portfolio per CLAUDE.md,
        and correctly not carrying High confidence.
```

**Timing collision (from calendar):** the 2026-09-03 trip-wire check falls
between the 2026-08-20 and 2026-09-24 Riksbank decisions. An 08-20 rate or
SEK move changes the SEK value of both crypto legs *and* the denominator
before the check is evaluated. Pinning the denominator today removes half of
that ambiguity; the other half is genuine market risk and stays.

### Call 4 — Deploy the 1,743.61 SEK of idle ISK cash into Avanza Global

> **The Contrarian.** 1,743.61 SEK is 0.8% of the portfolio. This is a rounding
> error dressed up as a decision, and the figure is not even broker-confirmed —
> it is computed from the P6 build and excludes courtage, so the real balance
> may be lower and the order may bounce.
>
> **First Principles.** The question is not "is 1,744 SEK material" but "is
> there any reason for this money to be cash." There isn't: it is inside the
> ISK, it is not the tax reserve, it has no earmark since the AZN buy executed
> on 08-06, and cash held without a reason is a decision made by default.
>
> **The Expansionist.** Unconstrained, the interesting version of this call is
> not the 1,744 — it is the 14,146 SEK trapped in PayPal, eight times larger,
> outside every wrapper, earning nothing, and leaking ~4% on the way out. Same
> direction, much bigger number. See Open decisions.
>
> **The Outsider.** Money you have decided to invest is sitting not invested,
> in the account you already invest from, in the fund you already own. There is
> no question here.
>
> **The Executor.** Monday: buy Avanza Global for the full available ISK cash
> balance (use the broker's actual figure, not 1,743.61). One order, no tax
> event, 0.10% ongoing fee.

```
ACTION: BUY — Avanza Global, full available ISK cash
POSITION: Avanza Global 55.46% of total (119,999 SEK); ISK cash 1,743.61 SEK
TARGET: equity 85% exposure-class. This closes ~0.8pp of a gap that is
        -7.8pp (~16,000 SEK) on the deployable denominator, -11.86pp
        (25,684 SEK) on the portfolio agent's total denominator.
REASON: (1) the only cash in the portfolio with no competing claim on it;
        (2) zero tax event, zero decision cost, 0.10%/yr — cheapest holding
        you own; (3) the alternative use (the medium tier) has no vetted
        candidate today, so parking is the honest choice, not the lazy one.
THESIS STATUS: INTACT (Avanza Global). portfolio.json and thesis-review agree.
WHAT CHANGED: the 1,743.61 SEK lost its earmark when the 1-share AZN.ST buy
        executed on 2026-08-06. It is now genuinely unallocated.
BREAK CONDITION: from portfolio.json — "A structurally cheaper equivalent
        core holding becomes available with the same diversification
        profile." Nothing suggests one has.
CONFIDENCE: High
HORIZON: Long (3y+)
```

**One disagreement to name inside this call.** The portfolio agent routes all
new money to Avanza Global on the *exposure-class* target (equity 85%). The
*risk-tier* framework — which `investor_profile.json` calls "the OPERATING
allocation control" — says something different: the secure tier (Avanza Global
55.46% + Auto 3 7.48%) is already **62.9% against a 60% target**, i.e. slightly
over, while the medium tier (individual stocks) is **13.18% against 30%** —
nearly 17pp under. On the tier framework, new money belongs in individual
stocks, not the index fund. The reason the Chairman still routes to Avanza
Global: thesis-review answers "would I buy today" as **NO on five of the seven
individual holdings**, the three cheapest-to-justify candidates are the very
names in Call 1 with no thesis, and `scout` has screened nothing against the
Watchlist (S10). Buying into the medium tier today would mean buying something
unvetted to satisfy a percentage. **This is parking, labelled as parking** —
not a judgment that the secure tier should keep growing.

---

## 5. Where the agents disagreed

1. **Industrials: favoured sector, unfavourable entry, no stated reason —
   three lenses stacking on the same three names.** Macro-regime says
   cyclicals/industrials are what this regime rewards (no inversion,
   10y-2y +0.44, VIX 15.15). Valuation says ATCO-B, ALFA and ABB are all
   Expensive (PEG 2.40 / 2.92 / 2.69). Thesis-review says all three are
   UNTESTED with every field null. Macro itself supplies the reconciliation
   and it should not be softened: *the tailwind is already in the price.* A
   sector being favoured is a statement about the business cycle; a stock at
   the 98th percentile of its 52-week range at PEG 2.40 is a statement about
   what you pay for it. **Resolution: hold, no adds, deadline on the theses.
   Confidence High.**
2. **Crypto: cheap on cycle position, wrong side of its own regime.**
   Valuation's cycle note (BTC -47.6% off ATH, ETH -60.6%, both with positive
   30-day momentum) and macro's verdict (Fear & Greed 30, dollar index 119.70,
   "on the wrong side of its own regime, full stop") point opposite ways.
   Macro pre-empted the averaging: cheap-in-a-fear-regime-with-a-strong-dollar
   often gets cheaper first. **Resolution: neither add nor pre-emptively trim
   — the pre-committed 09-03 trip-wire is what settles it. Confidence Medium,
   explicitly regime-dependent.**
3. **Portfolio agent vs. the standing Council ruling on the crypto trim.** The
   portfolio agent's Step 2 recommends trimming ~2,772.72 SEK today; the
   2026-08-06 Chairman set the evaluation date at 2026-09-03. Not a data
   conflict — a governance one. **Resolution: the standing rule wins.
   Confidence High.**
4. **Exposure-class target vs. risk-tier framework on where new money goes.**
   Detailed in Call 4. Both are recorded, adopted targets; they give different
   answers because "equity" does not distinguish an index fund from a
   single stock. **Resolution: Avanza Global, explicitly as parking.
   Confidence Medium** — this contradiction should be resolved properly, and
   is a candidate S-item.
5. **Two different "52-week range" measurements in circulation.** Valuation
   and thesis-review report price ÷ 52-week high; `position_report.py` reports
   the true percentile within the low-to-high band. Effects: AZN is "79.1% of
   range" on one and the **28th percentile** on the other — the second is a
   much stronger cheap-within-its-own-year signal and *strengthens* AZN's
   INTACT status. Conversely ABB, described as being near its high at 91.1%,
   is at the **79th percentile** — genuinely elevated but not pinned to the
   high the way ATCO-B (98th) is. **The stacking argument in Call 1 is
   therefore strongest for ATCO-B and weakest for ABB.** S-item candidate:
   standardise the metric and its label across agents.
6. **Data-quality flag on Investor A, from thesis-review.** The
   `revenue_growth` field reads +117% YoY while the fiscal-year revenue series
   shows FY2025 *below* both FY2024 and FY2023 — almost certainly realized
   gains landing in the revenue line for a holding company, not a bullish
   signal. Do not let this figure reach any screen or ranking. INVE-A remains
   structurally untestable until S6 (NAV discount/premium) is resolved.

---

## 6. Broken theses requiring a decision

None broken. Pulled from thesis-review unsoftened:

| Holding | Status | Would I buy today? |
|---|---|---|
| AZN.ST | **INTACT** | YES — revenue +6.4% YoY, 4yr rising, op margin 23.5%, PEG 1.38, dividend 1.98% at 47.4% payout, 28th percentile of its 52w range |
| Avanza Global | **INTACT** | YES |
| Avanza Auto 3 | **INTACT** | YES |
| VOLV-B.ST | **TOO_EARLY** | HOLD ONLY — ~1 week held, flat vs cost, insider-vs-fundamentals tension unresolved |
| SHB-A.ST | **WEAKENING** | NO — 98th percentile of 52w range, revenue -3.8% YoY, PEG 20.29 (worse than 08-06), consensus "underperform"; insider signal 3 weeks stale |
| INVE-A.ST | **WEAKENING** | NO — 98th percentile, "upside already captured," NAV discount still never obtained (S6) |
| COIN-XBT.ST | **WEAKENING** | NO — already above the 10% crypto target with P4 unexecuted |
| ATCO-B.ST / ALFA.ST / ABB.ST | **UNTESTED** | NO on all three |
| ethereum | **UNTESTED** | UNKNOWN — cannot be answered honestly without a stated reason to own it |

No stored-vs-computed `thesis_status` disagreements this sweep.

**On SHB-A and INVE-A:** both WEAKENING, both a NO on "buy today," and the
2026-08-06 Chairman declined to rotate on survivorship-bias grounds. Nothing
material has changed, and the combined position is 2,227.90 SEK — 1.03% of
the portfolio. Economically this is not worth a headline; the real issue is
process, and it is the same process issue as Call 1. **No action.**

---

## 7. Rebalancing actions

From the portfolio agent, tax-priority order, with the Council's ruling on each:

| Step | Action | Amount | Council ruling |
|---|---|---|---|
| 1 | Deploy idle ISK cash → Avanza Global | 1,743.61 SEK | **DO IT** — Call 4 |
| 1b | Deploy PayPal balance → Avanza Global | 14,146.43 SEK gross / ~13,580.57 net after ~566 SEK (4%) PayPal conversion friction | **BLOCKED on the routing decision (P3)** — see Open decisions. Do not convert inside PayPal by default. |
| 2 | Trim COIN-XBT.ST to hit 10% crypto exactly | ~2,772.72 SEK (≈1 unit at the stale 2,540 SEK/unit relayed price) | **NOT NOW** — Call 3. The 09-03 trip-wire governs. Side benefit noted for later: ~69 SEK/yr fee saving. |
| 3 | AF-account rebalancing | — | None available; the only AF holding is the frozen SEB Osteuropafond |
| 4 | ETH self-custody sale | — | **NOT PROPOSED** — cost basis is null (P1), so the taxable gain cannot be quantified; the ISK route achieves the same goal at zero tax cost. This is a wrapper decision, not a view that ETH is worse to hold. |

Residual equity gap after Step 1 and an eventual Step 1b: ~7,021-10,360 SEK on
the portfolio agent's figures. Closes via ordinary 1,000-3,000 SEK/month
contributions over roughly 3-7 months. **No further sale is needed to reach
the target** — that is worth stating plainly, because "equity 73% vs 85%
target" reads like a large corrective trade and it isn't one.

---

## 8. Open actions (P-items — things you can just go do)

| ID | Action | Amount / deadline |
|---|---|---|
| — | Buy Avanza Global with the full available ISK cash balance | ~1,743.61 SEK, Monday 2026-08-11. Use the broker's actual figure — the 1,743.61 is computed and excludes courtage. |
| P4 / S1 | Get verified tickers + current fees for cheaper Nordic BTC ETPs on Avanza, and add them to the Excel Watchlist tab | No deadline; saves ~230 SEK/yr. Blocked on you looking them up on Avanza — tickers must not be guessed. |
| P6 | Get a fresh COIN-XBT.ST price from Avanza | Before 2026-09-03 — the trip-wire check needs a real number, the current one is user-relayed from 2026-08-03 |
| P1 | Dig out the ETH cost basis | No deadline, but it now gates Call 2's reduction path as well as any sale |
| P7 | Confirm the ISK allowance threshold with Skatteverket | Low priority — current ISK ~181k against an assumed ~300k, so this is confirmation, not a live problem |
| — | Write one sentence each for ATCO-B, ALFA, ABB, ETH in `portfolio.json` | **2026-09-03.** Format that counts as complete: "own it because X; expect Y to drive it; sell if Z." |

## 9. Open decisions (forks the data does not settle)

**D1 — PayPal routing (P3). 14,146.43 SEK, recurring ~750-1,000 EUR every
~2 months. Open for a week; the cost of indecision is real.**

| Option | Trade-off |
|---|---|
| **A.** Convert USD+EUR inside PayPal, transfer SEK to Avanza, buy Avanza Global | Done this week. Costs ~566 SEK (4% planning figure, your instruction to assume worst case) and sets the precedent for every future inflow — a permanent leak, since this recurs indefinitely. |
| **B.** Transfer out in native currency to Revolut, convert there, then send SEK to Avanza | `OPEN_ITEMS.md` P3 states Revolut "does FX far cheaper than PayPal," but the actual rate has never been priced — that is the gap. Adds a few days and one unknown; if it saves even 2pp it is ~283 SEK on this transfer and recurring forever. Requires you to check Revolut's live FX spread and any monthly free-conversion limit. |
| **C.** Split: move a small test amount (e.g. 100 EUR) via route B, price the real all-in cost, then move the rest via whichever route won | Costs one extra week and a few SEK of test friction. Converts a recurring open question into a measured number once, which is what a permanent leak deserves. |

Council's read: **C** is the option that actually closes the item, because the
blocker is a missing price, not a missing preference. But this is your call —
the data cannot choose it for you until Revolut's rate is known.

**D2 — Exposure-class target vs. risk-tier framework (see Call 4).** Two
adopted targets currently give conflicting instructions for new money.
Options: (a) declare the exposure-class 85/10/5/0 the sole operating control
and retire the 60/30/10 tiers to reference; (b) keep the tiers as the
operating control and treat 85/10/5/0 as a derived check; (c) leave both and
accept that the Council arbitrates case by case. (c) is the status quo and it
worked this week only because the medium tier had no vetted candidate — it
will not resolve so cleanly next time. Recommend resolving this as an S-item.

---

## 10. Cost of being wrong

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| 1 — Hold ATCO-B/ALFA/ABB with no thesis | A de-rating from PEG 2.4-2.9 toward market-average multiples on 13,972.60 SEK is roughly -25% to -30%: **3,500-4,200 SEK**. Worse case is the second-order one: with no `break_conditions`, there is no rule that tells you to exit, so a slow de-rating gets held all the way down. | Yes on the money (quality businesses, long horizon, no portfolio leverage). The unrecoverable part is the *time* spent holding something you can't grade. |
| 2 — Hold and freeze ETH | A 50%-from-here crypto drawdown is historically ordinary: **~4,600 SEK**. Absolute maximum loss is the full 9,170 SEK. | Yes but slow. Capped and small; the wrong-way risk of *selling* today is worse — an unquantifiable K4 filing. |
| 3 — No trim now, wait for 09-03 | ~2,773 SEK sits above target for 3 more weeks. A 30% BTC fall in that window costs **~830 SEK** versus having trimmed. | Fully. The countervailing cost of trimming early — destroying the trip-wire mechanism — is not measurable in SEK but recurs every week. |
| 4 — Deploy 1,743.61 into Avanza Global | A 20% global drawdown on the new money: **~350 SEK**. | Fully, and the alternative (idle cash) carries a certain drag rather than a possible one. |
| D1-A — Convert inside PayPal | **~566 SEK, certain, on this transfer alone**, plus ~4% on every future inflow indefinitely. | **No.** A fee is gone. This is the one number on this page that is not a risk but a cost. |

---

## 11. Timing collisions (from calendar)

- **2026-08-20 Riksbank rate decision + Monetary Policy Update**, ~7-8 trading
  days out. Affects all seven Swedish-listed equities, AZN.ST indirectly via
  SEK, and COIN-XBT.ST via SEK/USD. **No call in this memo lands in that
  window** — the only trade recommended is a broad global index fund purchase
  on Monday 08-11, which has minimal SEK-rate sensitivity. Not a blocker.
- **2026-09-03 crypto trip-wire falls between the 08-20 and 09-24 Riksbank
  decisions.** An 08-20 SEK move shifts both the crypto SEK value and the
  denominator before the check runs. Flagged against Call 3.
- **FOMC 09-15/16** is outside the 5-day collision window; longer-lag relevance
  to AZN.ST and COIN-XBT.ST only.
- **Earnings dates: NO DATA for all 8 tickers** — network fetch failure
  (connection reset), not a ticker problem. Last successful verification
  2026-08-03, now 7 days stale. No estimates made. No call this sweep depends
  on an earnings date, so this does not block anything — but if the retroactive
  `swedish-equity-review` on ATCO-B/ALFA/ABB produces an action, earnings
  timing needs re-fetching first. Standing gap: US and Swedish CPI release
  dates are absent from the calendar entirely.

---

## 12. Data quality notes this sweep

No Excel import ran — no fresh workbook was available. Nothing downstream
blocks on it. The following are this session's own data limitations:

- **Structural Yahoo gaps (not fetch failures):** `interest_expense` null
  everywhere; `forward_pe` null for INVE-A.ST, ATCO-B.ST, AZN.ST;
  `debt_to_equity` and `free_cashflow` null for SHB-A.ST. SHB-A.ST's gross and
  EBITDA margins read 0.0 — **treat as no-data, not literal zero.**
- **COIN-XBT.ST 404** — expected and permanent, not an outage. Price is
  user-relayed from 2026-08-03 and now 7 days stale.
- **Swedish CPI is period 2025M12**, ~7-8 months old (S4). Every "real Swedish
  rate" conclusion in the macro read rests on that stale input and macro
  flagged it rather than treating it as current.
- **`position_report.py` does not reprice self-custody crypto** — carried ETH
  at its 2026-08-03 book value while the snapshot had live data. Corrected
  manually in this memo (+259 SEK). S-item candidate for `meta`.
- **"52-week range" means two different things across agents** — see
  disagreement 5. S-item candidate.

---

## 13. Learning notes

- **A threshold rule is only as solid as its denominator, and this week the
  denominator moved the answer more than the market did.** The same 24,410 SEK
  of crypto is 11.28%, 11.4% or 11.91% depending on whether the tax reserve and
  checking cash sit in the bottom of the fraction — a 0.63pp spread against a
  trip-wire set at 12.00%. Bitcoin would have to fall meaningfully to change
  the answer; an accounting choice changes it for free. That is why the
  denominator got pinned in this memo three weeks *before* the check, rather
  than on the day: a rule you can satisfy by choosing how to count is not a
  rule, it is a preference with a number attached.
- **"The regime favours this sector" and "this is a good time to buy it" are
  different sentences, and the 52-week percentile is what separates them.**
  Macro says industrials are what this environment rewards — no yield-curve
  inversion, VIX at 15, no recession signal. But Atlas Copco sits at the 98th
  percentile of its own 52-week range at PEG 2.40. The favourable regime is the
  *reason* it is at the 98th percentile; you are not buying the tailwind, you
  are buying the price the tailwind already produced. A high 52-week percentile
  is not a sell signal on its own — it usually reflects real strength — but it
  does mean the cheap way to express a view has already gone.
- **Two portfolios can sit in two different regimes at the same time, and this
  one does.** Equity volatility is calm (VIX 15.15, curve positively sloped,
  real Fed funds ~-0.10%) while crypto sits in Fear (F&G 30, BTC -47.6% off
  ATH) with an elevated dollar (119.70) working against it. There is no single
  "risk-on / risk-off" number for this portfolio, and any framing that produced
  one would be hiding the more useful fact: the 87% of capital in equities and
  the 11% in crypto are being driven by different things right now, so they
  should not be sized off the same view.
- **UNTESTED is a statement about your records, not about the company — which
  is exactly why it justified a deadline rather than a sale.** Atlas Copco,
  Alfa Laval and ABB are strong businesses and nothing in this sweep suggests
  otherwise. The problem is that a holding with no written `break_conditions`
  has no exit rule, which means the position can only ever be sold on feel. The
  right response to a missing thesis is to produce the evidence to write one
  (the retroactive `swedish-equity-review`), not to sell a good business to
  resolve a paperwork state — but it does need a date attached, because
  "eventually" has now failed twice.

---

*Nothing in this memo executes. You decide.*
