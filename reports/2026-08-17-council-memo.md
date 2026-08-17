# Council memo — 2026-08-17

*Structured synthesis of this system's own agents' analysis. Not advice from a
licensed advisor. Every number below traces to
`data/cache/snapshots/20260817T061032.json`, `data/portfolio.json`,
`data/cache/calendar/` (fetched today), or the carried-forward
`data/cache/excel_import/latest-summary.json` (2026-08-13), all read this sweep.*

`journal` ran in session-start mode at the top of this session. Per `OPEN_ITEMS.md`
P2 item 3, the journal-before-council ordering rule does not transplant as a hard
stop in this architecture — reconciliation is a separate end-of-sweep artifact in
`SESSION_LOG.md`, not a section of this memo — so it is not treated as a blocker.

**Blocking-question check.** No open item holds blocking status this sweep. The
Handelsbanken wrapper — the original and only instance — was resolved 2026-07-07
and the account fully exited (confirmed in `portfolio.json`'s
`resolved_structural_questions` and by its absence from `OPEN_ITEMS.md`'s P-list).
Per CLAUDE.md's 2026-08-03 phase shift, this memo leads with how the positions are
behaving and what should change.

---

## 1. Position report

Snapshot `20260817T061032.json` · previous `20260812T225321.json`

| Position | Price | Δ vs prev sweep | Δ vs cost | 52w percentile | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A | 147.60 | +0.7% | +14.2% | 93.6% | 147.60 | fetched |
| Investor A | 407.00 | -1.1% | +40.2% | 91.7% | 2,035.00 | fetched |
| Volvo B | 340.10 | -2.8% | **-7.5%** | 73.5% | 4,421.30 | fetched |
| Atlas Copco B | 182.50 | -0.4% | +0.7% | 95.1% | 4,927.50 | fetched |
| AstraZeneca | 1,514.00 | -1.0% | +0.3% | 26.6% | 7,570.00 | fetched |
| Alfa Laval | 562.80 | -0.2% | -2.0% | 82.9% | 5,065.20 | fetched |
| ABB | 981.60 | +1.4% | +3.7% | 82.5% | 3,926.40 | fetched |
| Avanza Auto 3 (fund) | no data | — | +65.2% | — | 16,191.00 | book value |
| **COIN-XBT.ST (certificate)** | **2,581.34/unit — 4 days stale** | **no data** | +28.0% | — | 15,488.04 | Excel 2026-08-13, **carried, not repriced** |
| Avanza Global (fund) | no data | — | +0.0% | — | 119,999.00 | book value |
| ETH (self-custody) | 17,942.14/unit | +0.7% | no data (P1) | — | 9,004.85 | fetched (CoinGecko × sek_per_eur 10.9523) |

Investable capital (Convention B: Avanza ISK + ETH wallet) **188,775.43 SEK**;
full portfolio **214,218.98 SEK** — both quoted from the portfolio lens.
Crypto spot: ethereum 1,638.23 EUR (-61.3% off ATH; 24h +1.0%, 7d -0.9%, 30d
+3.0%). **Bitcoin: no data** — three CoinGecko attempts, all HTTP 429.
Fear & Greed 31 ("Fear").

**Reading it.** A quiet week in the equity book: nothing moved more than 3%, and
the largest single move (Volvo -2.8%) is noise at this size. The one position
that genuinely matters this week is the one nobody could price — **COIN-XBT.ST
failed on both of its independent price paths simultaneously** (its permanently
broken ticker 404'd, and the BTC directional proxy that exists precisely to cover
that gap was rate-limited three times). The 15,488.04 SEK in the table is the
2026-08-13 Excel figure carried forward, and the entire crypto trip-wire
arithmetic rests on it. That is a real, compounding data gap, not a footnote —
see Call 1 for the sensitivity check I ran instead of pretending it isn't there.

**Does anything contradict a thesis?** Two things. **Volvo B now trades below both
its cost basis (340.10 vs 367.50, -7.5%) and the board member's ~360 SEK insider
buy from 2026-07-27** — the single strongest signal behind the purchase has not
paid off. Thesis-review's read is "watch, not break," and I agree: revenue growth
just flipped positive (+2.7%) after two years of -13% decline, forward P/E 13.7 and
analyst "buy" are intact, and TOO_EARLY means what it says at ~2 weeks held.
Second, and larger: **all five WEAKENING names now sit at 92-99% of their 52-week
high at the same moment** (SHB-A 98.6%, INVE-A 97.2%, ATCO-B 98.5%, ALFA 95.0%,
ABB 92.7%, on price÷high). The active ingredient in four of those five theses is
"still shows good upside" or "strong track record" — Call 2. **AstraZeneca at the
26.6th percentile of its own range is the sole exception and the only holding all
three lenses like.** The broad index funds (Avanza Global 63.57% of investable
capital, Auto 3) are deliberately buy-and-hold, both INTACT, nothing to do.

---

## 2. What should change

**Four things. One is executable Monday; one is a governance stop; two are
overdue homework with a date now attached.**

1. **Execute the COIN-XBT.ST 1-unit trim that was decided last sweep and never
   done.** Last sweep's Call 1 was High confidence with "execute Monday
   2026-08-17" attached — that Monday is today, and `portfolio.json` still shows
   6 units. The call re-derives to the identical answer on today's data. Call 1.
2. **Do not adopt either proposed target allocation. Run the real backtest
   first.** This sweep produced the first-ever drawdown estimate against the
   stated -30% tolerance, and it says both the current mix (≈-42.3%) and the
   adopted 85/10/5/0 target (≈-45.75%) breach it. That estimate is explicitly
   *not* a backtest — S5 still has never run. Call 3.
3. **Run `swedish-equity-review` on ATCO-B.ST / ALFA.ST / ABB.ST, with a
   2026-09-03 default attached.** Seventh consecutive sweep of the identical
   unexecuted recommendation. Call 2.
4. **Stop deliberating PayPal; the fallback now has a date.** Fourth consecutive
   sweep. Call 4.

**Proposed target allocation — ADVISORY ONLY, nothing written to any file.** This
closes the standing "reference_targets" task, with one correction from the
portfolio lens worth stating: `investor_profile.json`'s `reference_targets` are
*not* null — they are already populated at 85/10/0/5, mirroring
`portfolio.json.targets`. The live gap was never the missing number; it is that
the number has never been validated against the -30% tolerance. Two options were
produced, both advisory:

| Option | Allocation | Est. severe-case drawdown | The problem with it |
|---|---|---|---|
| 1 — profile-strict | equity 50 / crypto 5 / cash 5 / short-duration 40 | ≈-26.25% (fits) | Reverts to the v1 glidepath the user **explicitly overrode** 2026-07-22 ("I don't mind" equity above 70%). Contradicts a direct instruction. |
| 2 — preference-first | equity 82 / crypto 6 / cash 12 / FI 0 | ≈-41.4% (still breaches) | Better than current and close to stated appetite, but still fails the same test — buying a target that fails at a lower score. |

The portfolio agent's own recommendation, which I endorse: **treat neither as the
answer.** A correlation-aware backtest will likely produce a materially less
punitive number than this crude sum-of-worst-cases method, especially for the
63.57% sitting in a diversified global index fund. Adopting a target on a
deliberately pessimistic estimate is the wrong order of operations.

**No new candidates this sweep.** `scout` was correctly not invoked — the standing
emphasis is portfolio-tending for a fifth consecutive sweep, nothing was screened,
and ISK cash is confirmed 0. **No Candidate Evaluation method was run because no
candidate was surfaced.**

---

## 3. Portfolio health scorecard

Carried over from the portfolio agent verbatim.

| Dimension | Grade | Detail |
|---|---|---|
| Asset allocation vs targets | **WATCH** | Crypto 12.97% of investable capital (Convention B, 188,775.43 SEK) vs 10% target — **above the 12% trip-wire** set 2026-08-06 for the 2026-09-03 sweep. Under the full-portfolio denominator (214,218.98 SEK) it is 11.43%, below 12%. First sweep the two conventions disagree on whether the trip-wire fires |
| Equity sector concentration | **ACT** | Industrials 65.29% of the stock sleeve; industrials + financials 73.06% |
| Geography | **WATCH** | 59.07% Sweden in the stock sleeve |
| Currency exposure | **WATCH / partial-UNKNOWN** | No revenue-by-currency data |
| Single-position concentration | **WATCH** | Avanza Global 63.57% of investable capital — but a diversified index fund, not single-company risk. Largest true single-company bet is AZN.ST at 4.01% |
| Institution concentration | **ACT** | Avanza 95.23% of investable capital, breaches the 80% cap — the direct, accepted cost of ISK consolidation |
| Fee drag | **OK** | 570.34 SEK/yr = 0.30% of investable capital, under the 0.4% cap. COIN-XBT.ST alone is 387.20 SEK/yr at 2.5% |
| Wrapper efficiency | **OK** | All real capital in the ISK |
| Drawdown-tolerance fit | **UNKNOWN** | Real backtest (S5) has never run. An illustrative back-of-envelope this sweep — **explicitly not a backtest** — puts the current mix at ≈-42.3% and the adopted target at ≈-45.75%, both breaching the stated -30% tolerance under a crude sum-of-worst-cases method |

**This scorecard is provisional on three named gaps, and the unanswered questions
are these:**
- **S5 / `investor_profile.json`:** is -30% a real constraint the user would act
  on, or a figure written down once and never tested? The adopted 85/10/5/0 target
  has never been checked against it, and the only check ever attempted says it
  fails. Unanswered.
- **`horizon.years_until_needed` = "3-7 (SOFT)", `primary_goal` explicitly
  uncertain.** If the Mediterranean-apartment option firms up, the future
  liability is EUR, not SEK — which reverses the rationale for the 59% Nordic
  tilt entirely (`horizon.currency_note`). Unanswered.
- **The emergency buffer's location is unrecorded.** "3-6 months" is stated;
  which account holds it is not. Load-bearing for D3, because it decides whether
  HB checking is buffer or investable capital.

**Structure (levers 1-2): nothing broke.** All capital in the ISK, fee drag 0.30%
inside the cap. The one open fee item is P4 (the 2.5% certificate, blocked on S1);
Call 1 shrinks it as a side effect.

---

## Headline calls

Four calls. Each ran the six-voice Investment Council method; the voices are
compressed, the Chairman's decision is the content.

### Call 1 — Execute the COIN-XBT.ST 1-unit trim. It was decided last sweep for today and has not happened.

**Contrarian:** You are re-issuing a High-confidence call on the one position in
the book you cannot price this week — two independent feeds failed on the same
holding. The 12.97% rests on a 4-day-old figure and a denominator the user has
never confirmed. Saying it louder is not the same as it being more right.

**First Principles:** Two questions are still hiding in one. How much crypto to
own is arguable and genuinely affected by the stale price. Whether to own it
through a wrapper charging 2.5%/yr is not, and the staleness does not touch it.
At 12.2% or 13.8%, this is still the most expensive krona in the portfolio.

**Expansionist:** Ignore the SEK constraint and the maximum-upside version is to
trim nothing and let contributions dilute — which points the *opposite* way on
sizing. But even that version says get out of the 2.5% wrapper. The genuine
maximum version is P4: replace the certificate outright, saving ~230 SEK/yr. That
is blocked on S1 and has been for weeks. The trim is the affordable fraction of
the right answer.

**Outsider:** You decided five days ago to sell one of six identical units, for
reasons that have not changed, with a specific date attached. That date is today.
Nothing new argues against it. Do the thing you already decided.

**Executor:** Monday: check the live Avanza quote first (the system cannot price
this), then sell 1 unit COIN-XBT.ST at market, ~2,581 SEK. Buy Avanza Global with
the full proceeds. Both inside the ISK, tax-free, one round trip.

**Chairman.** The Contrarian's staleness objection is the only genuinely new
argument this sweep, and it deserves an answer rather than a dismissal. So I
tested it, as a sensitivity check on the portfolio lens's own figures rather than
by fetching anything: **the certificate would have to be trading ~13.5% below its
carried price for the trip-wire not to fire at all, and ~26.7% below for a 1-unit
trim to push crypto under the 10% target.** A 13.5% BTC move in four days is
possible; 26.7% is not realistically. So the staleness can make the trim
*unnecessary*; it cannot plausibly make it *harmful*. That asymmetry is what
resolves it — combined with the fact that the un-priceability cuts both ways, and
the position could equally be at 13.8%.

Sizing re-derives independently to the same answer as last sweep, now against this
sweep's two conventions rather than three:

| Convention | Crypto now | After 1-unit trim | After 2-unit trim |
|---|---|---|---|
| B — investable-only (188,775.43) | **12.97%** (fires) | 11.61% (clears, above target) | 10.24% (at target) |
| Full portfolio (214,218.98) | 11.43% (does not fire) | 10.23% (above target) | **9.02% (below target)** |

One unit is the only size that clears the trip-wire and stays at or above the 10%
target under **both** denominators. Two units creates an underweight on the
full-portfolio reading — fixing one deviation with another. **The call is
therefore independent of D3**, which remains unconfirmed by the user, and that is
deliberate.

Routing: proceeds to Avanza Global per `investor_profile.json`'s
`profit_recycling_rule` (high-risk-tier realizations default to the secure tier).
D4 — whether that rule applies to gross proceeds or the realized gain only — is
still unconfirmed; Council recommended gross proceeds on 2026-08-12 and I am not
re-litigating a governance recommendation on zero new evidence. It stays an open
decision below.

```
ACTION: REDUCE
POSITION: COIN-XBT.ST 6 units, 15,488.04 SEK (carried at the 2026-08-13 price)
          = 8.20% of investable capital. Crypto class 24,492.89 SEK =
          12.97% (Convention B) / 11.43% (full portfolio)
TARGET: 5 units — crypto class to 11.61% / 10.23%, clearing the 12% trip-wire
        and holding above the 10% target on both denominators
REASON: (1) This is an unexecuted decision from 2026-08-12, dated for today,
        with no new evidence against it; (2) the 12% trip-wire fires on
        Convention B and the sensitivity check shows it would take a ~13.5%
        BTC drop since 08-13 for that to be wrong; (3) 2.5%/yr makes this the
        most expensive holding in the book, and the trim cuts 64.53 SEK/yr of
        guaranteed drag while the zero-fee ETH wallet carries the crypto
        conviction untouched. Tax-free inside the ISK.
THESIS STATUS: WEAKENING — but flagged honestly: portfolio.json carries
        WEAKENING and thesis-review CARRIED IT FORWARD UNCONFIRMED this sweep,
        because it had no BTC data to test against. The two do not disagree;
        one of them simply could not check. That is a weaker basis than last
        sweep's, and it is why confidence drops a notch.
WHAT CHANGED: Nothing in the position's favour or against — the change is that
        the position became un-priceable on two independent paths at once
        (ticker 404, CoinGecko 429 ×3), and that the decision to trim it sat
        unexecuted for five days through its own stated execution date.
BREAK CONDITION: The holding's own recorded condition — "still above 12% of
        investable capital at the 2026-09-03 sweep -> trim." It is above 12%
        now on Convention B, 17 days early. A live Avanza quote materially
        below ~2,234 SEK/unit (13.5% under carried) means the trip-wire does
        not fire and the trim can wait for 2026-09-03.
CONFIDENCE: Medium
HORIZON: Long
```

Confidence is **Medium**, down from last sweep's High, for one honest reason: the
price is stale and unverifiable by this system, and thesis-review could not
confirm the status. The action is robust to that; the evidence base is thinner.
**Execution note: verify the live Avanza quote before placing the order** — if it
is materially below ~2,234 SEK/unit, the premise has changed and this waits.

**Capital-availability check:** verified against this sweep's portfolio-agent
output — Avanza ISK cash is **0 SEK**, confirmed in `portfolio.json`. This call
does not assume otherwise; it *generates* 2,581.34 SEK and redeploys it inside the
same round trip. No funding premise to be wrong about.

### Call 2 — Five names, one rationale, all at highs: hold, no adds, and the review now has a default

**Contrarian:** "All five near their highs" describes a portfolio of good
companies in a rising market. That is what winning looks like. Treating the
simultaneity as a problem is pattern-matching on a coincidence — and macro-regime
explicitly declines to grade Swedish industrials, so there is no regime case
underneath it either.

**First Principles:** Strip the framing. The finding is not "these are expensive."
It is that the *same rationale* — track record, backing Swedish industry — was
used five times, and every instance now sits where that rationale's active
ingredient, remaining upside, has been consumed. That is one bet placed five
times, not five bets.

**Expansionist:** If the goal really is backing Swedish industry, the
maximum-conviction version is more capital in *fewer* names — the best one. You
still cannot name the best one, because the review that would rank them has never
run. Seven sweeps.

**Outsider:** Someone shows you seven stock picks. Five were chosen for the same
reason, five sit within 8% of their yearly peak, and the one that is cheapest and
most defensive is the only one anyone has a specific argument for. You would ask
why the other five need to exist separately.

**Executor:** No trades. Run `swedish-equity-review` on ATCO-B.ST, ALFA.ST and
ABB.ST this week. Direct the next contribution to Avanza Global or AZN.ST, not to
a fifth industrial.

**Chairman.** HOLD, no trades. The Contrarian is right on both counts and neither
changes the answer. A high 52-week percentile is not a sell signal, and
macro-regime genuinely cannot grade this sector — it says so explicitly ("no clean
call"), and its Swedish inputs are compromised anyway (S4: `se_cpi_yoy` is period
2025M12, ~8 months stale, and macro correctly refused to compute a Swedish real
rate off it). A rotation built on a lens that admits it cannot grade would be
worse than doing nothing.

The binding constraint is what the First Principles and Outsider voices name from
different angles: **construction, not price.** Industrials are 65.29% of the stock
sleeve and industrials+financials 73.06% — ACT-rated, a fact about the portfolio
rather than an opinion about any company. That is fixable with new money, not with
sales.

What I am escalating is the review. It has now been the system's own recommended
next step for seven consecutive sweeps. The deadline-plus-default mechanism
demonstrably works — it is what finally closed the thesis half of P6 on 2026-08-12
after three sweeps of asking. So attach the same mechanism here, using the
holdings' own recorded language rather than inventing one: **if
`swedish-equity-review` has not run on ATCO-B/ALFA/ABB by the 2026-09-03 sweep,
those three are treated as rotation candidates ineligible for adds** — which is
precisely what their own `break_conditions` already say.

```
ACTION: HOLD (SHB-A.ST, INVE-A.ST, ATCO-B.ST, ALFA.ST, ABB.ST) — no adds, no trims
POSITION: Stock sleeve 28,093 SEK = 14.9% of investable capital. Industrials
          18,340.40 SEK = 65.29% of the sleeve; +financials = 73.06%
TARGET: Industrials below 45% of the stock sleeve — reached by growing the
        sleeve elsewhere (Avanza Global / AZN.ST), not by selling these
REASON: (1) Concentration is the binding problem and it is correctable with new
        money rather than sales; (2) no vetted alternative exists, because the
        review that would produce one has never run — rotating into an unvetted
        name to fix concentration trades a known problem for an unknown one;
        (3) macro cannot grade Swedish industrials while S4 leaves the Swedish
        inflation input 8 months stale, so a regime-driven sell would rest on a
        known-bad number.
THESIS STATUS: WEAKENING on all five. portfolio.json and thesis-review agree on
        every one — I checked each; no silent picking required.
WHAT CHANGED: The captured-upside pattern went from three names to five, all
        simultaneously at 92-99% of their 52-week high. Thesis-review's own
        framing, which I am adopting: this is a portfolio-level concentration
        of captured upside, not five independent stories.
BREAK CONDITION: Their own recorded condition — a materially better-positioned
        Nordic-industrial alternative surfacing via swedish-equity-review or
        screening, industrials/financials concentration needing correction, or
        genuine fundamental deterioration (declining margins/revenue), which
        would remove even the track-record rationale.
CONFIDENCE: High
HORIZON: Medium
```

**On VOLV-B.ST specifically, kept separate because its status is different:**
TOO_EARLY, and now below both cost (-7.5%) and the board member's ~360 SEK insider
buy. Thesis-review calls it "watch, not break" and I agree — revenue growth flipped
positive (+2.7%) for the first time after two years of -13% decline, forward P/E
13.66 / PEG 1.42, analyst "buy." Its own break condition is "3+ months with no
sign of the expected earnings recovery"; it is at ~2 weeks. No action, and no
pretending two weeks is evidence.

**And on SHB-A.ST, restated because it is still true:** one share, 147.60 SEK,
0.08% of investable capital. It cannot affect returns and costs a line of
attention every sweep. Not worth a trade on its own — build it up or close it out
at the next natural rebalancing rather than carrying it as a token.

### Call 3 — The adopted target may contradict the stated tolerance. Do not fix it by adopting a different unvalidated target.

**Contrarian:** The -42.3% figure comes from summing worst cases as if every asset
crashes together, which is a method engineered to breach any threshold. Acting on
it — cutting equity to 50% — would reverse a direct user instruction on the
strength of a number the agent that produced it explicitly labelled *not* a
backtest.

**First Principles:** Two separate facts, and they should not be merged. (1) The
-30% tolerance has never been checked against the adopted target, six weeks after
adopting it. (2) The only check ever attempted says it fails. Neither is a reason
to change the allocation. Both are reasons the check is now the highest-value
unexecuted item in the system.

**Expansionist:** Ignore the constraints. The maximum version is not a smaller
equity sleeve — it is a *correct tolerance*. -30% on 188,775 SEK is roughly 56,600
SEK. If the honest answer is that an 85/10 book can draw -42%, the real choice is
to revise the tolerance upward deliberately (the user has already accepted equity
above 70%) or revise the allocation. Which one is a conversation, not a
calculation.

**Outsider:** You wrote down how much loss you would accept, then built a
portfolio and never checked it against your own rule. The first rough check says
it fails. That is not an emergency, but it is obviously the next thing to do.

**Executor:** Run `backtest` (S5) before the 2026-09-03 sweep. Write neither
proposed target into `portfolio.json` or `investor_profile.json`. No trades.

**Chairman.** NO ACTION on allocation targets. Adopt neither option.

The Expansionist frames the live question correctly and it is not the one the
options are answering: is the -30% figure a real constraint, or a number written
down once in July and never revisited? The user has already, explicitly and in
writing, overridden the conservative allocation that -30% implies ("The push of
equity above 70% is fine. I don't mind," 2026-07-22). That makes **Option 1
disqualified on the ground the portfolio agent itself named** — it contradicts a
direct user instruction, and this system does not quietly recommend against a
stated preference.

**Option 2 is directionally defensible and still wrong to adopt**, for a reason
worth being blunt about: its own estimate (≈-41.4%) *still breaches* -30%. Adopting
it would buy a target that fails the identical test at a slightly better score.
That is motion, not progress.

The Contrarian's methodological objection is also correct and is why this is a
governance stop rather than an alarm: a sum-of-worst-cases assumes perfect
correlation across a book that is 63.57% diversified global index fund. A real
correlation-aware backtest will almost certainly produce a smaller number. **But
"the estimate is pessimistic" is not the same as "the target is fine" — and after
six weeks of an adopted, unvalidated target, the difference between those two
sentences is exactly what S5 exists to settle.**

```
ACTION: NO ACTION (governance stop — no trade, no file write)
POSITION: Current mix, estimated severe-case drawdown ≈-42.3%; adopted
          85/10/5/0 target ≈-45.75%; stated tolerance -30% (≈56,600 SEK on
          188,775.43 SEK of investable capital)
TARGET: Unchanged at 85/10/5/0 until S5 runs. Neither proposed option adopted.
REASON: (1) Option 1 contradicts a direct 2026-07-22 user instruction;
        (2) Option 2 breaches the same tolerance it is meant to fix;
        (3) the only evidence on the table is explicitly not a backtest, and
        its method (sum of worst cases, implicit perfect correlation) is
        biased toward breaching for a book that is mostly one diversified
        global index fund.
THESIS STATUS: n/a — allocation governance, not a holding
WHAT CHANGED: For the first time in the system's history, a drawdown figure
        exists for the adopted target. It says the target and the tolerance
        contradict each other. That is genuinely new information even though
        it is not decision-grade.
BREAK CONDITION: `backtest` (S5) runs. If a correlation-aware result still
        exceeds -30%, then the target and the tolerance genuinely conflict and
        one of them must be changed deliberately — that becomes a real decision
        with the user's input, not an agent's proposal.
CONFIDENCE: High (on not adopting either option) / Low (on what the true
        drawdown number is — that is the entire point)
HORIZON: Long
```

### Call 4 — PayPal: fourth sweep. The recommendation gets a default now.

**Contrarian:** Four sweeps of identical unexecuted advice means the
recommendation is wrong-sized for the person, not that the person is negligent. A
test transfer with an unclear payoff is exactly the kind of task that never gets
done. At some point the system should pick a default rather than re-ask.

**First Principles:** You do not know the price of the alternative. Further
deliberation costs nothing and resolves nothing. One transfer resolves it.

**Expansionist:** ~1,970-2,630 SEK/yr, forever. Over the 3-7 year horizon that is
6,000-18,000 SEK — larger than any single stock call this system has ever made,
and it exceeds the entire portfolio's annual fee drag (570.34 SEK) by a factor of
three to five.

**Outsider:** 14,079.79 SEK sits in an account that pays nothing and charges ~4%
to leave, for the fourth week running. Described cold, that is the most obviously
broken thing here.

**Executor:** PayPal → Revolut, 50 EUR. Record EUR sent and SEK received. Compare
against the snapshot's `sek_per_eur` of 10.9523. Ten minutes.

**Chairman.** The Contrarian's diagnosis is now the finding, and I am changing the
recommendation rather than repeating it a fifth time. **Attach a default: if the
test transfer has not happened by the 2026-09-03 sweep, execute Option A instead —
convert the full balance inside PayPal, accept the ~563 SEK cost, and route the
proceeds into the ISK.** Paying 563 SEK once to stop a permanent leak beats a
fifth sweep of deliberation. A measured decision is better than an unmeasured one;
an unmeasured decision executed beats an unmade one indefinitely deferred.

Note the second-order effect, because it connects two items that look unrelated:
this balance is also what keeps the crypto trip-wire from firing on the
full-portfolio denominator. Routing it into the ISK collapses the D3 disagreement
entirely — the two conventions converge.

```
ACTION: NO ACTION on holdings; execute a measurement, with a dated fallback
POSITION: 1,177.49 USD + 266.88 EUR = 14,079.79 SEK, 6.57% of full-portfolio
          capital, earning nothing, outside every wrapper
TARGET: Full balance routed into the ISK by the cheapest measured path — or, by
        2026-09-03, by the unmeasured path rather than not at all
REASON: (1) The blocker is a missing price, not a missing preference; (2) the
        leak recurs every ~2 months forever, which is what makes it lever-2
        structural rather than a 563 SEK one-off; (3) routing it also collapses
        the D3 denominator disagreement as a side effect.
THESIS STATUS: n/a — cash routing
WHAT CHANGED: Nothing on the portfolio. What changed is the recommendation: a
        fourth identical unexecuted ask is evidence the framing is wrong, so
        the ask now carries a default rather than a repeat.
BREAK CONDITION: Revolut's measured spread comes in at or above PayPal's ~4%
        -> Option A wins on the merits, and D1 closes with a different answer,
        which is still a closed decision.
CONFIDENCE: High on "stop deliberating" / Low on which route wins
HORIZON: Long
```

---

## Where the agents disagreed

**1. The D3 denominator disagreement is decision-relevant for the first time.**
This sweep the portfolio lens's two conventions give *opposite answers to the same
question*: crypto is 12.97% of investable capital (Convention B — trip-wire fires)
and 11.43% of the full portfolio (does not fire), for the identical 24,492.89 SEK.
Every previous sweep the conventions merely differed by a margin; today they
disagree on the outcome. **I resolved this by refusing to depend on it** — Call 1
is sized so that one unit is correct under both readings. That is a workaround, not
a resolution. D3 has been Council-recommended (Convention B) since 2026-08-12 and
still has no user confirmation. It must be settled before 2026-09-03, when the
trip-wire's stated evaluation date arrives and the workaround may not be available.

**2. Crypto: valuation and thesis-review say the long-term case is intact; macro
says this is precisely the wrong regime. Macro pre-empted the smoothing, and it
was right to.** Valuation reports ETH -61.3% off ATH with flat momentum and a
stable #2 market-cap rank; thesis-review grades ethereum **INTACT** on the user's
own stated 3y+ conviction. Macro-regime's warning is worth quoting because it
anticipated exactly this memo: *"if valuation or thesis-review argue ETH/BTC look
cheap or oversold here, that is not a contradiction to resolve quietly — a strong
dollar plus a Fear print is precisely the combination under which crypto has
historically kept bleeding rather than bottoming."* DXY 119.06, crypto F&G 31,
against VIX 14.63 — equity vol shows no comparable stress. **I am not resolving
the direction; nobody here has the data to.** What I did is separate two things
the memo keeps apart deliberately: **confidence in the crypto direction is Low;
confidence in the action is Medium**, and the action was sized so the direction
cannot flip it. Note also that thesis-review itself flagged that ETH's INTACT
status is *not* a portfolio-fit argument for adding — so on the actual decision,
thesis-review and portfolio do not conflict at all.

**3. Thesis-review's captured-upside finding vs macro-regime's refusal to grade
Swedish industrials.** Thesis-review produces a clear portfolio-level finding:
five WEAKENING names simultaneously at 92-99% of their highs, one rationale used
five times, upside consumed. Macro-regime, asked about the same 65% of the stock
sleeve, returns **"mixed, no clean call"** — dollar strength is a translation
tailwind for SEK exporters and simultaneously a drag on the global capex cycle
those four names sell into, and its Swedish inflation input is 8 months stale (S4).
These do not cancel out; they answer different questions. Thesis-review is right
that the *reason for owning* has been consumed. Macro is right that it *cannot
tell you where the sector goes next*. That combination supports "no more," not
"sell" — which is Call 2, and it is the second consecutive sweep where S4's stale
input is a named reason a rotation call stayed HOLD.

**4. thesis-review could not confirm COIN-XBT.ST at all, and the reason is a
compounding data failure worth naming.** Its WEAKENING grade is *carried forward
unconfirmed* — the snapshot had no BTC data when it ran, and BTC still came back
"no data" after three CoinGecko 429s. So the position that carries this sweep's
only trade recommendation is un-priceable on **two independent grounds at once**:
its own permanently broken ticker (P4/S1), and the directional proxy adopted
specifically to cover that gap. This is not two views disagreeing; it is one lens
unable to look. Flagged for `meta` — the proxy exists precisely so the broken
ticker isn't a single point of failure, and this sweep it was.

**Where they agree, stated briefly because it is uncommon and it matters.**
**AstraZeneca is the one name with no dissent across three lenses.** Valuation:
Cheap (PEG 1.34, fourth straight year of rising revenue, 26.6th percentile of its
own range, ~21% off its high). Thesis-review: the only clean **INTACT** among the
recent buys, no break condition triggered. Macro-regime: beta 0.211, explicitly on
the right side of the regime — defensive ballast is what a calm-but-possibly-
underpriced-VIX environment rewards. Three lenses, no tension. It is not a call
this sweep only because ISK cash is 0 and the trim proceeds are governed by the
profit-recycling rule (D4) — see Open decisions. **If a contribution lands before
next sweep, AZN.ST is where the medium-tier krona goes.**

---

## Broken theses requiring a decision

**None broken.** From thesis-review, unsoftened:

- **WEAKENING (6):** SHB-A.ST, INVE-A.ST, ATCO-B.ST, ALFA.ST, ABB.ST, COIN-XBT.ST.
  Only COIN-XBT.ST carries an action this sweep (Call 1), and it is the only one
  whose recorded break condition has actually triggered.
- **INTACT (4):** AZN.ST, Avanza Auto 3, Avanza Global, ethereum.
- **TOO_EARLY (1):** VOLV-B.ST — below cost and below the insider's buy price, but
  ~2 weeks held against a 3-month break condition. Watch, not break.
- **Cross-holding pattern, thesis-review's own framing, carried unsoftened:** all
  five WEAKENING equities sit at 92-99% of their 52-week high simultaneously. This
  is a portfolio-level captured-upside concentration, not five independent stories,
  and it means the rotation question is portfolio-wide rather than name-by-name.
- **Status agreement check:** `portfolio.json` and thesis-review agree on every
  holding this sweep. The single caveat is COIN-XBT.ST, where thesis-review carried
  the status forward **unconfirmed** for lack of data rather than re-testing it —
  that is a gap, not a disagreement, and Call 1 says so explicitly.

---

## Rebalancing actions

From the portfolio agent, with my amendments marked.

| # | Action | SEK | Tax | Status |
|---|---|---|---|---|
| 1 | **Sell 1 unit COIN-XBT.ST, buy Avanza Global with full proceeds** | **2,581.34** (realizes 564.67 SEK gain vs 2,016.67 cost basis) | Tax-free (ISK) | **Execute Monday — verify the live Avanza quote first** |
| 2 | Route idle PayPal (1,177.49 USD + 266.88 EUR) into the ISK | 14,079.79 gross / ~13,517 net at 4% worst case | No tax event | **Blocked on D1** — Call 4, fallback dated 2026-09-03 |
| 3 | 2-unit trim (5,162.68 SEK, crypto → 10.24% on Convention B) | 5,162.68 | Tax-free (ISK) | **Not recommended** — see amendment |
| 4 | ETH wallet | — | Uncomputable (30% K4, no cost basis) | **Do not execute** — P1 blocks the tax math |

**Amendment to line 3, stated openly.** The portfolio agent presented 1-, 2- and
3-unit options without picking one. Two units lands crypto at 10.24% on Convention
B — near-perfect against target — but at **9.02% on the full-portfolio
denominator, below the 10% target.** Since D3 is unconfirmed, the correct size is
the one that is right under both readings, and that is one unit. Three units
(8.87% / 7.82%) undershoots badly on both and is not on the table.

**Net effect if line 1 executes alone** (the realistic Monday case): crypto 12.97%
→ 11.61% on Convention B, 11.43% → 10.23% on the full portfolio; annual fee drag
falls by 64.53 SEK; equity exposure rises by the same 2,581.34 SEK. That is worth
doing on its own, and it is the only line here not blocked on something.

---

## Confidence and horizon per call

| Call | Confidence | Horizon | What caps it |
|---|---|---|---|
| 1 — Trim 1 unit COIN-XBT.ST | **Medium** | Long | Position un-priceable on two independent paths; thesis-review could not confirm its status. Sized to be denominator-independent, so D3 cannot flip it — the staleness can only make it unnecessary, not harmful |
| 2 — Hold the five, run the review, 2026-09-03 default | **High** | Medium | S4's 8-month-stale Swedish CPI prevents a confident regime read — a reason for caution, not for action |
| 3 — Adopt neither target; run S5 | **High** on not adopting / **Low** on the true drawdown | Long | The only drawdown evidence in existence is explicitly not a backtest, and its method biases toward breaching |
| 4 — PayPal: measure, with a dated fallback | **High** on stopping deliberation / **Low** on which route wins | Long | Revolut's spread has never been measured — that is the entire point |

No Short-horizon calls this sweep, so the 10% tactical cap and the never-High-
confidence rule are not engaged.

---

## Cost of being wrong

| Call | If wrong, realistic downside in SEK | Recoverable? |
|---|---|---|
| 1 — Trim 1 unit COIN-XBT.ST | BTC re-rates sharply: forgone gain on 2,581.34 SEK of exposure (a BTC double costs ~2,581 SEK of upside). If the stale price was wrong and no trim was needed: courtage plus a marginally underweight crypto sleeve, immaterial | **Yes, fully.** 21,911.55 SEK of crypto (5 units + 0.50185 ETH) still participates; proceeds sit in equity, not cash |
| 2 — Hold the five at highs | Industrials correct 30%: the 18,340.40 SEK sleeve loses ~5,502 SEK, 2.9% of investable capital. Add financials and a 30% drawdown on the full 20,523 SEK cluster is ~6,157 SEK | **Yes**, over the 3-7y horizon. The mirror risk — selling near highs and watching quality compounders run — is similar in size, which is why the call is hold and not sell |
| 3 — Adopt neither target, run S5 first | If the ≈-42.3% estimate is directionally right and a severe drawdown lands before S5 runs: ~79,300 SEK on 188,775 SEK, against a stated tolerance of ~56,600 SEK — roughly **22,700 SEK beyond stated tolerance** | **Financially yes**, over a long horizon. **Behaviourally, this is the one that may not be** — the real risk of exceeding a stated tolerance is capitulating at the bottom. Cost of running the backtest instead: zero |
| 4 — PayPal measure-then-default | Test transfer at 4%: ~22 SEK on 50 EUR to learn. Fallback Option A: ~563 SEK once. Cost of a fifth sweep of nothing: **~1,970-2,630 SEK/yr, indefinitely** | **Yes, trivially.** The recoverable cost is two orders of magnitude below the cost of continued inaction |

---

## Timing collisions

`calendar` ran today (`fetch_calendar.py --days 45`) and was checked explicitly
against every contemplated action. **No collision.**

- **Central bank:** Riksbank rate decision **2026-08-20** (3 days out), Riksbank
  minutes 08-25, FOMC 09-15/16, Riksbank Business Survey 09-16, Riksbank rate
  decision 09-24, minutes 09-30.
- **Earnings:** ABB 10-20, SHB-A 10-21, ATCO-B 10-22, VOLV-B 10-23, ALFA 10-27 —
  **all beyond the 45-day window.** AZN.ST's only listed date (2026-07-27) is
  already past. INVE-A.ST returned no earnings date.
- **Assessment:** the only action recommended for execution is a BTC-certificate
  trim, which has no earnings exposure by construction. One nuance worth naming
  rather than hiding: COIN-XBT.ST is SEK-denominated and tracks a USD-priced
  asset, so **the 08-20 Riksbank decision will move both the certificate's SEK
  value and the SEK denominator it is measured against.** The two move in
  partially offsetting directions and the net effect on the crypto percentage is
  small and ambiguous in sign — that is not a reason to hurry the trade before
  08-20, nor to wait for it. Recorded so it is not mistaken for a missed
  consideration later.
- **Gap:** no forward earnings date exists for AZN.ST or INVE-A.ST. Neither has an
  action attached this sweep, so nothing here is exposed.

---

## Open actions

Things to go do. Pulled from `/OPEN_ITEMS.md` by ID.

| ID | Action | Amount / detail | By when |
|---|---|---|---|
| — | **Sell 1 unit COIN-XBT.ST, buy Avanza Global with the full proceeds.** Check the live Avanza quote first — the system could not price it this week | ~2,581.34 SEK | **Monday 2026-08-17** (this was already today's date last sweep) |
| **P6** | Run `swedish-equity-review` on ATCO-B.ST, ALFA.ST, ABB.ST retroactively | — | **2026-09-03** — after that, all three become rotation candidates ineligible for adds |
| **P3 / D1** | Execute a 50 EUR test transfer PayPal → Revolut, convert to SEK, record both figures | 50 EUR | **2026-09-03** — after that, execute Option A (convert inside PayPal, ~563 SEK) instead |
| **S5** | Run the `backtest` agent against the 85/10/5/0 target and the -30% tolerance | — | Before 2026-09-03; it is the highest-value unexecuted item in the system |
| **S12 / D3 / D4** | Confirm the two conventions so they can be pinned in words in `data/cache/definitions.json` | — | **Before 2026-09-03** — D3 is now outcome-relevant, not just cosmetic |
| — | Fix the Excel workbook items below (the 1,743.61 SEK cash figure especially) | — | Before next sweep |
| **P1** | Dig up the ETH cost basis when convenient | — | Not urgent unless selling |
| **P7** | Verify the ISK allowance threshold with Skatteverket | — | Low priority; confirmation, not a live problem |
| **S1 / P4** | Verify cheaper Nordic BTC ETP tickers on Avanza and add them to the Excel Watchlist tab | — | Unblocks P4 (~230 SEK/yr saving); no progress in weeks |

## Open decisions

Forks where the data does not pick a single answer. Each gets concrete options.

**D3 — which denominator governs the crypto trip-wire.** *This is no longer
theoretical: this sweep the two readings disagree on whether the trip-wire fires
(12.97% vs 11.43%). Council recommended Option 1 on 2026-08-12; it still has no
user confirmation. Call 1 is deliberately sized to work under either, but that
workaround is not guaranteed to be available on 2026-09-03.*
1. **Convention B — investable-only (Avanza ISK + ETH wallet, 188,775.43 SEK).**
   Trade-off: strictest, so trip-wires fire earliest — but it counts only capital
   you can actually reallocate today, and it converges with Option 2 automatically
   once PayPal routes. **Recommended.**
2. **Full portfolio (214,218.98 SEK).** Trade-off: simplest and most stable, but it
   counts 11,363.76 SEK already owed to Skatteverket and 14,079.79 SEK of PayPal
   that costs ~4% to move — both flatter every risk percentage with money that is
   not really allocatable.
3. **Defer to 2026-09-03 and decide then.** Trade-off: costs nothing today because
   Call 1 is denominator-independent, but it means arguing the definition on the
   day the rule is checked — the exact failure this system flagged on 2026-08-10.

**D4 — does `profit_recycling_rule` apply to gross trim proceeds or the realized
gain only?** Selling 1 unit at 2,581.34 SEK against a 2,016.67 SEK cost basis
realizes a 564.67 SEK gain; the rest is return of capital. *Council recommended
Option 1 on 2026-08-12; unconfirmed. Call 1 assumes it.*
1. **Whole proceeds to the secure tier** (2,581.34 SEK → Avanza Global).
   Trade-off: one order, satisfies the rule under either reading, leaves no idle
   cash to go stale — a failure mode this system has hit twice. **Recommended.**
2. **Realized gain only to secure** (564.67 SEK → Avanza Global; 2,016.67 SEK free
   for the medium tier). Trade-off: the literal reading of "money I make," and it
   would fund AZN.ST — the one name with no dissent across three lenses this sweep
   — but 2,016.67 SEK does not buy a 1,514 SEK share plus meaningful change, and it
   adds a second order for a ~2,000 SEK routing difference.
3. **Pin "gross proceeds" as a standing convention** in `data/cache/definitions.json`
   per S12. Trade-off: closes the question permanently for all future trims, at the
   cost of slightly over-weighting the secure tier on every recycling event.

**The target-allocation question is a decision, not a recommendation, and it now
has real evidence attached.** Options 1 and 2 are laid out in full in section 2
above with their estimated drawdowns; Call 3's recommendation is to adopt neither
until S5 runs. If you want to decide sooner rather than wait for the backtest, the
honest third option is to **revise the -30% tolerance itself** — you have already
overridden the allocation it implies, so it may simply be a stale number. That is
your call and not the system's.

**D2 remains resolved** (route 100% of new contributions to equity while cash sits
at or above its 5% target). No re-litigation.

---

## Excel data gaps

**No fresh Excel import ran this sweep.** `data/cache/excel_import/latest-summary.json`
is dated **2026-08-13 18:54 UTC** — carried forward, not regenerated. That matters
more than usual this week, because the COIN-XBT.ST price underpinning the entire
crypto trip-wire arithmetic comes from that file's CRYPTO & CERTIFICATE DETAIL
block and is now four days old with no alternative source. Flags carried verbatim,
with what to do:

1. **The stale 1,743.61 SEK Avanza ISK cash figure is still in the workbook.** The
   carried summary's `portfolio_deltas` still reads
   `CASH_SEK (avanza-isk): quantity 0 -> 1743.61 (from Excel)`. You confirmed
   directly on 2026-08-11 that this cash is gone; `portfolio.json` correctly
   carries 0 (your direct statement outranks the workbook). **This is the single
   Excel item with a track record of producing a wrong recommendation** — it
   funded the incorrect 2026-08-11 AZN.ST call. Set it to 0 in the workbook by
   hand. Second sweep of asking.
2. **ATCO-B.ST: P/E 2.05 is outside the 3-80 sanity range — suspect.** *Not used
   anywhere in this memo*; valuation ran on the Yahoo figure (33.2x). Refresh that
   cell's Stocks data type. Same bad value first caught 2026-08-06 — the sanity
   check is working; the underlying cell is still wrong.
3. **ALFA.ST / ATCO-B.ST / SHB-A.ST / VOLV-B.ST: no 52-week range in Excel.**
   Confirmed data-provider gap for some Nordic-primary tickers, not a formula bug.
   No action available; the 52w figures in the position report come from Yahoo.
   Do not chase these.
4. **Twelve Watchlist tickers carry a space instead of an exchange suffix**
   (NOVO B, ERIC B, ASSA B, INVE B, INDU C, LATO B, KINV B, HEXA B, SEB A, SWED A,
   HM B, SAAB B). These are Excel's raw entity names, not fetchable symbols — they
   will fail every screen and valuation fetch until corrected. Replace each with
   its real exchange-suffixed symbol (`SEB A` → `SEB-A.ST`), verifying the exchange
   per name (Novo Nordisk is `.CO`, not `.ST`). **This silently caps `scout`'s
   effective universe at 33 of 45 entries** — relevant the moment the emphasis
   flips back to prospecting.
5. **Refresh the workbook and re-import before next sweep**, specifically so
   COIN-XBT.ST gets a current price. Two independent price paths failed this week;
   the workbook is the only remaining one.

---

## Learning notes

- **Five positions all near their highs at once is one fact, not five — and that
  distinction changes what you do about it.** Read name-by-name, "Atlas Copco is at
  98% of its range" is unremarkable; strong companies spend a lot of time near
  their highs. Read together, five holdings chosen for the *same* stated reason
  ("strong track record", "Swedish industrial champion") all arriving at 92-99% of
  their highs in the same week is a single bet that has already largely played out,
  placed five times. The technical name for what makes them move together is
  correlation — Volvo, Atlas Copco, Alfa Laval and ABB all sell equipment into the
  same global capex cycle, so they are far less independent than four tickers
  suggest. This is exactly why the memo's constraint on them is *concentration* (a
  measurable fact: 65.29% of the stock sleeve) rather than *valuation* (an opinion),
  and why the answer was "no more" rather than "sell."
- **Beta is the number that put AstraZeneca on the right side of the regime while
  ABB sits on the wrong one.** Beta measures how much a stock has historically
  moved relative to the market: 1.0 means it moves with it, above 1.0 means it
  amplifies it, below means it dampens it. AZN's beta is 0.211 — roughly a fifth of
  market movement — against ABB at 1.011 and Atlas Copco at 1.071. With VIX at 14.63
  (calm, arguably complacent), macro-regime's read is that cheap volatility is
  exactly when defensive ballast is worth owning, because you are being asked to pay
  very little for protection nobody currently wants. That single number, not a view
  on drug pipelines, is why the defensive name is the one macro declined to flag.
- **A drawdown estimate built by summing worst cases is wrong in a known
  direction, and saying so is more useful than reporting the number.** This sweep's
  -42.3% figure assumes every asset has its worst year simultaneously — that is,
  perfect correlation. Real portfolios do not behave that way, and this one
  especially: 63.57% of it is a single globally diversified index fund whose
  internal holdings partly offset each other. So the true number is almost
  certainly better than -42.3%. But "the estimate is pessimistic" and "the target
  is fine" are different statements, and the gap between them is what a real
  backtest (S5) exists to close. The correct response to a biased estimate is to
  run the unbiased test, not to average the bias away or to act on the biased
  number — which is why Call 3 is a governance stop rather than an allocation
  change.
- **A backup data source that fails at the same time as the primary was never
  really a backup.** COIN-XBT.ST has no working ticker — a known permanent fact —
  so this system adopted spot bitcoin from CoinGecko as a directional proxy
  precisely so that gap would not be a single point of failure. This week both
  failed at once (ticker 404, CoinGecko rate-limited on three attempts), leaving
  the trip-wire resting on a four-day-old spreadsheet cell. The right response was
  not to estimate the price from training knowledge or from ETH's move — it was to
  record "no data," then ask a different question: *how far off would the stale
  price have to be for the decision to change?* The answer (~13.5% to make the trim
  unnecessary, ~26.7% to make it harmful) turned an unanswerable question into a
  decidable one. When you cannot get the number, test how much the number matters.

---

*Portfolio valued this sweep at **214,218.98 SEK** (full) / **188,775.43 SEK**
(investable, Convention B) — append a row to `data/valuations.csv` before closing
the session.*
