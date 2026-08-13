# Council memo — 2026-08-12

*Structured synthesis of this system's own agents' analysis. Not advice from a
licensed advisor. Every number below traces to
`data/cache/snapshots/20260812T225321.json`, `data/portfolio.json`, or
`data/cache/excel_import/latest-summary.json`, all read this sweep.*

`journal` ran in session-start mode earlier today, before this session's
reconciliation work. Rather than block, I read `OPEN_ITEMS.md` and
`SESSION_LOG.md` directly for the post-reconciliation state. Per P2 item 3,
the journal-before-council ordering rule does not transplant as a hard stop
in this architecture — reconciliation is a separate end-of-sweep artifact
here, not a section of this memo.

---

## 1. Position report

Snapshot `20260812T225321.json` · previous `20260812T001709.json`

| Position | Price | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|
| Handelsbanken A | 146.60 | +13.4% | 91% | 146.60 | fetched |
| Investor A | 411.70 | +41.9% | 95% | 2,058.50 | fetched |
| Volvo B | 350.00 | -4.8% | 81% | 4,550.00 | fetched |
| Atlas Copco B | 183.15 | +1.0% | 96% | 4,945.05 | fetched |
| AstraZeneca | 1,529.00 | +1.3% | 29% | 7,645.00 | fetched |
| Alfa Laval | 564.20 | -1.8% | 84% | 5,077.80 | fetched |
| ABB | 967.80 | +2.2% | 79% | 3,871.20 | fetched |
| Avanza Auto 3 (fund) | no data | +65.2% | - | 16,191.00 | book value |
| COIN-XBT.ST (certificate) | 2,581.34/unit | +28.0% | - | 15,488.04 | Excel CRYPTO & CERTIFICATE DETAIL block, live data type |
| Avanza Global (fund) | no data | +0.0% | - | 119,999.00 | book value |
| ETH (self-custody) | 17,825.96/unit | no data (P1) | - | 8,945.96 | fetched (CoinGecko via sek_per_eur) |

Crypto spot: bitcoin 54,966 EUR (-48.9% vs ATH, 7d -1.9%, 30d +2.1%),
ethereum 1,627.6 EUR (-61.5% vs ATH, 7d -1.6%, 30d +6.4%). Fear & Greed 27 (Fear).

**Reading it.** No same-day move column this sweep — the "previous" snapshot
was today's earlier 6-ticker candidate-test file, so every real holding reads
"no data" on Δ vs prev. That is a comparison gap, not a price gap; next sweep
diffs normally. **The two positions that actually moved are the two that were
never being measured properly:** COIN-XBT.ST now carries a genuinely live
price (15,488.04 SEK) instead of an 8-day-stale user-relayed 15,240 SEK, and
ETH reprices for the first time ever (8,945.96 vs the 8,911 book value carried
since 2026-08-03, S7 fix live). Nothing in the equity book moved enough to
matter week-over-week.

**Does anything contradict a thesis?** One real tension: **six of seven
individual stocks sit in the upper half of their 52-week ranges, three of them
at 91-96%** (SHB-A, INVE-A, ATCO-B) — and all three of those are graded
WEAKENING on a thesis whose active ingredient was "still shows good upside" or
"strong track record." Upside that has been captured is not upside that
remains. AZN.ST at 29% of range is the sole exception and the sole holding
thesis-review would buy today. The broad index funds (Avanza Global 56% of
capital, Auto 3) are deliberately buy-and-hold, both INTACT, nothing to do.

---

## 2. What should change

**Three things, one of them executable Monday.**

1. **Trim COIN-XBT.ST by exactly one unit (2,581.34 SEK) and route the
   proceeds to Avanza Global.** The crypto trip-wire is functionally breached
   today on real data for the first time. Full reasoning in Headline call 1;
   the sizing is deliberately chosen to work under all three competing
   denominators at once.
2. **Direct the next contribution away from Nordic industrials.** Industrials
   are 65.2% of the 28,294 SEK individual-stock sleeve, past the 45% ACT line,
   and the four names in it (Volvo, Atlas Copco, Alfa Laval, ABB) all sell into
   the same global capex cycle. This is a construction fact, not a view on any
   one company. D2's standing resolution already routes new contributions to
   equity; this narrows it — to Avanza Global or AZN.ST, not a fifth industrial.
3. **Price the PayPal route (D1/P3).** Third consecutive sweep with the same
   unexecuted recommendation. Headline call 3.

**No new candidates this sweep.** `scout` was correctly not invoked — the
standing emphasis is portfolio-tending, the Watchlist has grown but nothing was
screened, and there is zero idle capital to deploy into a new name. No
Candidate Evaluation method was run, because no candidate was surfaced.

---

## 3. Portfolio health scorecard

Carried over from the portfolio agent verbatim.

| Dimension | Grade | Detail |
|---|---|---|
| Asset allocation vs targets | **WATCH** | Equity 73.7% vs 85% (-11.3pp, split-adjusted for Auto 3's ~60/40 mix); cash 11.9% vs 5% (+6.9pp, mostly idle PayPal + tax reserve, not deliberate) |
| Crypto trip-wire (12%) | **WATCH/ACT** | Borderline breached — see D3 detail; this is the headline finding |
| Equity sector concentration | **ACT** | Industrials 65.2% of the 28,294 SEK individual-stock sleeve, past the 45% ACT line |
| Geography | **OK** | Stock sleeve 59% Sweden (deliberate), but that sleeve is only 13.2% of total capital; Avanza Global (56%) is globally diversified |
| Currency exposure | **UNKNOWN** | No revenue-by-currency data, not graded |
| Single-position concentration | **ACT (technical)** | Avanza Global 56.0% of total, over the 15% cap by construction — but a diversified index fund, not single-stock risk. No action indicated |
| Institution concentration | **ACT** | Avanza 84.0% of total, over the 80% cap. Correct byproduct of ISK consolidation, not a mistake, but real counterparty exposure |
| Fee drag | **OK** | 570.34 SEK/yr (0.27% of total), under the 0.4% cap. COIN-XBT.ST alone 387.20 SEK/yr (2.5%/yr), the only holding above the 0.5% single-fund flag |
| Wrapper efficiency | **OK** | All real capital in ISK, ~120,028 SEK headroom vs the assumed ~300k threshold (P7, unverified) |
| Drawdown-tolerance fit | **UNKNOWN** | No backtest exists (S5, still open) |

**This scorecard is provisional on three named gaps**, two of which sit in
`investor_profile.json`:
- The adopted 85/10/5/0 target has never been tested against the stated -30%
  max drawdown tolerance (S5). An 85% equity + 10% crypto book plausibly
  exceeds -30% in a bad year, which would mean the target and the tolerance
  contradict each other.
- `horizon.years_until_needed` is "3-7 (SOFT)" and `primary_goal` is explicitly
  uncertain. If the Mediterranean-apartment option firms up, the future
  liability is EUR, not SEK, which reverses the rationale for the Nordic tilt
  entirely (`horizon.currency_note`).
- The emergency buffer's actual location is unverified — 3-6 months is stated,
  but which account holds it is not recorded. This is load-bearing for D3,
  because it determines whether HB checking is buffer or investable capital.

**Structure (levers 1-2): nothing broke.** All capital in the ISK, portfolio
fee drag 0.27%. The one open fee item is P4 (the 2.5% certificate), and
Headline call 1 shrinks it as a side effect.

---

## Headline calls

Four calls. Each ran the six-voice Investment Council method; the voices appear
compressed, the Chairman's decision is the content.

### Call 1 — Trim COIN-XBT.ST by exactly one unit

**Contrarian:** You are selling a 49%-drawdown asset into a Fear reading of 27
to satisfy a percentage rule whose denominator you admit you have not agreed
on. That is the textbook retail error, and the 12% line is a number this system
chose, not a risk measurement.

**First Principles:** Strip the trip-wire framing. Two separate questions are
hiding in one: how much crypto do you want (arguable, you have said you can
afford to lose this tier), and should you own it through a wrapper charging
2.5%/yr (unambiguous no). The second question is what makes *this specific
unit* the right thing to sell.

**Expansionist:** Ignoring SEK constraints, the maximum-upside version is not
to trim at all — let equity contributions dilute crypto naturally while you own
the drawdown. That points the *opposite* way on sizing but the *same* way on
the vehicle: even the max-upside case says hold BTC through something that
isn't bleeding 2.5%/yr.

**Outsider:** You hold six identical units of one product. You sell one. You
still hold five, plus a separate crypto wallet. Your exposure to the underlying
idea is essentially unchanged; you just pay less in fees. Easy yes.

**Executor:** Monday: one sell order, 1 unit COIN-XBT.ST at market (~2,581 SEK).
One buy order, full proceeds into Avanza Global. Both inside the ISK. No tax
event, no cash left sitting idle.

**Chairman.** The Contrarian and Expansionist converge on the same real point
from opposite ends: the *sizing* case is arguable, the *vehicle* case is not. I
resolve it by choosing the smallest trim that satisfies every denominator
simultaneously, which makes the call independent of D3 rather than hostage to
it.

The portfolio agent's recommended 3,000-5,500 SEK band is not executable as
stated — the certificate trades in whole units of 2,581.34 SEK, so the real
choice is 1 unit or 2. **Two units overshoots**: it drops crypto to 8.99% on
Convention A, a full point below the 10% target, selling into fear to fix a
problem that no longer exists. One unit lands it at:

| Convention | Crypto after 1-unit trim | vs 12% trip-wire | vs 10% target |
|---|---|---|---|
| A (total classified, 214,361.70) | 10.19% | clear | at target |
| B (investable-only, 188,918.15) | 11.57% | clear | above |
| C (excl. tax reserve, 202,997.94) | 10.76% | clear | above |

One unit is the only size that clears the trip-wire on all three conventions
while staying at or above the 10% target on all three. That is the answer, and
it does not require D3 to be settled first.

**Routing the proceeds — this differs from last sweep's call, for a stated
reason.** `investor_profile.json`'s `profit_recycling_rule` is a standing user
instruction: gains realized in the medium and high-risk tiers default toward
the *secure* tier ("considered as a monetising machine sort of"). COIN-XBT.ST
is the high-risk tier. The 2026-08-11 memo routed money to AZN.ST, but that
was medium-tier build residual, not trim proceeds — different provenance, rule
didn't apply. It applies here. Proceeds go to Avanza Global, 0.10%/yr, which
also happens to be the destination that does not add to the ACT-rated
industrials concentration.

```
ACTION: REDUCE
POSITION: COIN-XBT.ST 15,488.04 SEK — 7.23% of total classified capital
          (8.20% of investable-only); crypto class 24,434.00 SEK =
          11.40% / 12.93% / 12.04% on Conventions A / B / C
TARGET: 5 units, 12,906.70 SEK — crypto class to 10.19-11.57% across all
        three conventions
REASON: (1) Trip-wire breached on two of three defensible denominators on
        genuinely fresh data for the first time, and the standing 2026-08-06
        Council decision already committed to trimming above 12%; (2) the
        2.5%/yr fee makes this the most expensive krona in the portfolio to
        hold, so trimming here cuts 64.53 SEK/yr of drag while the zero-fee
        ETH wallet carries the crypto conviction untouched; (3) tax-free
        inside the ISK, so execution costs nothing but courtage.
THESIS STATUS: WEAKENING — portfolio.json and thesis-review agree, no conflict.
        Both cite the same three things: position +28% vs cost (upside partly
        captured), Fear & Greed 27 vs the "positive buy-in signals" at
        purchase, and the 2.5% fee.
WHAT CHANGED: The Excel import gained a CRYPTO & CERTIFICATE DETAIL block,
        producing the first genuinely live price this position has ever had
        (2,581.34 SEK/unit vs an 8-day-stale 2,540). The position was always
        this size — the system just could not see it. D3's arithmetic moved
        from estimate to fact as a result.
BREAK CONDITION: The holding's own recorded break condition — "still above 12%
        of investable capital at the 2026-09-03 sweep -> trim." Today's real
        data says it is above 12% now on two of three readings, so the
        condition is met three weeks early. A BTC move that drops crypto below
        10% on all three conventions before execution cancels this trim.
CONFIDENCE: High
HORIZON: Long
```

Confidence is **High**, one notch above last sweep's Medium, for two specific
reasons: the price is real rather than relayed, and the recommended size is
correct under every competing denominator, so the one genuinely unresolved
question (D3) cannot flip it. Note this is a rebalancing action against an
adopted target — lever 3, allocation — so it is Long-horizon, not the tactical
short-horizon framing used on 2026-08-11. That reclassification is what lifts
the confidence cap.

**Capital-availability check:** not applicable in the usual direction — this
call *generates* 2,581.34 SEK rather than spending it. No funding premise to
verify. Verified separately that `portfolio.json` carries ISK cash at 0 and
that no part of this call assumes otherwise.

### Call 2 — Settle D3 now: adopt Convention B

**Contrarian:** Pinning the strictest denominator locks in a rule that fires
trip-wires more often on a portfolio that is supposed to be long-horizon — and
you will be tempted to re-litigate it the first time it produces an answer you
dislike.

**First Principles:** A denominator should answer one question: capital you can
actually reallocate today. The tax reserve is owed to Skatteverket. PayPal
costs ~4% to move. Both fail that test on their own terms.

**Expansionist:** The maximum version is to make PayPal routable (D1) — at
which point B and C converge and this entire argument disappears permanently.
The definition fight is a symptom of the unrouted balance, not a governance
problem.

**Outsider:** If someone told you your crypto weight is "either 11.4% or 12.9%
depending on which of your own spreadsheets you read," you would fix the
spreadsheet before trading on either number.

**Executor:** One entry in `data/cache/definitions.json` per S12's spec, naming
Convention B in words with today's date. Five minutes. D3 closes.

**Chairman.** Adopt **Convention B** (investable-only: Avanza ISK + ETH wallet,
188,918.15 SEK today). The Contrarian's objection is real but time-limited and
answered by the Expansionist: once PayPal routes into the ISK, B and C
converge, so the strictness is a temporary artifact of an unrouted balance.
Convention A is ruled out on a principle this system already established on
2026-08-06 — money already owed to Skatteverket is not yours to allocate, and
including it would flatter every risk percentage.

Pin it **in words, not the number** — the number goes stale weekly, the
definition is what is actually being argued about. This is the second instance
of the same failure class in three weeks (S11 fixed it one level down, at "% of
52-week range"), which is why S12 exists.

```
ACTION: NO ACTION (governance decision, no trade)
POSITION: n/a — this fixes the denominator, not a holding
TARGET: Convention B written into data/cache/definitions.json, D3 closed
REASON: Excludes money owed to the state and money that costs 4% to move —
        both fail the "capital I can reallocate today" test. Converges with
        Convention C automatically once D1 resolves.
THESIS STATUS: n/a
WHAT CHANGED: D3 became decidable — the crypto figures are real for the first
        time, so all three conventions are now computed from live data rather
        than one live and two estimated.
BREAK CONDITION: PayPal routed into the ISK -> B and C merge; re-pin then, as
        a mechanical update rather than a fresh argument.
CONFIDENCE: Medium
HORIZON: Long
```

Confidence Medium rather than High for one honest reason: Convention B's
treatment of the HB checking account (611 SEK) depends on where the emergency
buffer actually sits, which is unverified — the third named scorecard gap.
The amount is immaterial today; the principle is not.

### Call 3 — PayPal: stop deliberating, price it

**Contrarian:** Three sweeps of identical unexecuted advice usually means the
advice is wrong-sized for the person, not that the person is negligent. A
100 EUR test transfer has an unclear payoff and real friction, which is exactly
why it keeps not happening.

**First Principles:** You do not know the price of the alternative. Further
deliberation costs nothing and resolves nothing. One transfer resolves it.

**Expansionist:** ~1,970-2,630 SEK/yr, forever, compounded across the 3-7 year
horizon, is 8,000-15,000+ SEK. That is larger than any single stock call this
system has ever made.

**Outsider:** You hold ~14,000 SEK in an account that pays nothing and charges
4% to leave. Described cold to someone with no priors, that is the most
obviously broken thing in this portfolio.

**Executor:** PayPal → Revolut, 100 EUR. Note EUR received. Convert to SEK in
Revolut. Note SEK received. Compare against the snapshot's `sek_per_eur`. Two
numbers, ten minutes.

**Chairman.** The Contrarian's diagnosis is probably correct and changes the
framing rather than the action. If 100 EUR is the friction point, make it
50 EUR — the measurement quality barely degrades and the activation energy
halves. What does not change: this is a lever-2 problem (fee drag, the second-
largest return lever at this portfolio size), and it is the only open item
where the annual cost exceeds the entire portfolio's current fee drag.

```
ACTION: NO ACTION on the portfolio; execute a measurement
POSITION: 1,177.49 USD + 266.88 EUR = 14,079.79 SEK, 6.57% of total capital,
          earning nothing, outside every wrapper
TARGET: The full balance routed into the ISK by the cheapest measured path
REASON: (1) The blocker is a missing price, not a missing preference —
        Revolut's real spread has never been measured; (2) the leak recurs
        every ~2 months forever, which is what makes it structural rather
        than a 563 SEK one-off; (3) routing this balance is also what closes
        over half the 24,200 SEK equity shortfall without a single sale.
THESIS STATUS: n/a — cash routing, not a holding
WHAT CHANGED: Nothing this sweep. That is itself the finding: third
        consecutive sweep, same recommendation, no movement.
BREAK CONDITION: Revolut's measured spread comes in at or above PayPal's ~4%
        -> option A wins (convert inside PayPal, accept the cost) and D1
        closes with a different answer, which is still a closed decision.
CONFIDENCE: High on "measure before committing"; Low on which route wins
HORIZON: Long
```

### Call 4 — Swedish industrials: hold, no adds, get the review done

**Contrarian:** Grading ATCO-B, ALFA and ABB "Expensive" is grading a
patriotism thesis on a metric it never claimed. The user said plainly this was
about track record and backing Swedish industry, not price. Selling quality
compounders near highs on a PEG reading is a well-documented way to
underperform.

**First Principles:** The question is not whether these are good companies. It
is whether 65.2% of your stock-picking concentrated in one correlated cycle is
a position you would choose starting from scratch today. It is not — and that
is a construction fact, independent of any individual name's merit.

**Expansionist:** If you genuinely want to back Swedish industry, the
maximum-conviction version is more capital in *fewer* names — concentrated in
the best one. You cannot identify the best one, because the review that would
rank them has never run.

**Outsider:** You own four companies that all sell equipment into the same
global capex cycle, and the portfolio describes this as diversified because
they have different names.

**Executor:** No trades. Run `swedish-equity-review` on ATCO-B.ST, ALFA.ST and
ABB.ST before next sweep. Point the next contribution somewhere else.

**Chairman.** HOLD, no trades. The Contrarian is right that valuation cannot
break a preference thesis — a stated preference is not falsifiable by a PEG
ratio, and this system should not pretend otherwise. But it does not need to:
the binding constraint is **concentration**, which the Outsider states most
clearly and which is a fact about the portfolio, not an opinion about the
stocks. That is why the action is "no more," not "sell."

Two things I am explicitly not doing. I am not recommending a rotation, because
there is no vetted replacement — `swedish-equity-review` has now been the
system's own recommended next step for **six consecutive sweeps** without
running, and rotating into an unvetted name to fix concentration would trade a
known problem for an unknown one. And I am not treating the three fresh WEAKENING
grades as new bad news: they were set today, deliberately, to match the thin
non-differentiated rationale — that is the system recording reality accurately,
not a deterioration.

One position worth naming plainly: **SHB-A.ST is a single share worth 146.60
SEK, 0.07% of capital.** It cannot affect returns and costs a line of attention
every sweep. It is not worth a trade on its own; it should be either built up
or closed out at the next natural rebalancing rather than carried indefinitely
as a token.

```
ACTION: HOLD (ATCO-B.ST, ALFA.ST, ABB.ST, VOLV-B.ST) — no adds, no trims
POSITION: Industrials 18,444.05 SEK = 65.2% of the 28,294.15 SEK stock sleeve,
          8.6% of total capital
TARGET: Industrials below 45% of the stock sleeve — reached by growing the
        sleeve elsewhere, not by selling these
REASON: (1) Concentration is the binding problem, not valuation, and it is
        fixable with new money rather than sales; (2) no vetted alternative
        exists because swedish-equity-review has never run; (3) macro cannot
        grade Swedish industrials with confidence until S4 (stale SE CPI) is
        fixed, so a regime-driven sell would rest on a known-bad input.
THESIS STATUS: WEAKENING on all three of ATCO-B/ALFA/ABB (portfolio.json and
        thesis-review agree — both set today, no conflict). VOLV-B.ST
        TOO_EARLY (~9 days held).
WHAT CHANGED: Theses were written today for all three, closing the 2026-09-03
        P6 deadline for these tickers. That converts them from UNTESTED to
        testable, and the recorded break condition explicitly names them
        rotation candidates rather than conviction holds.
BREAK CONDITION: Their own recorded condition — a materially better-positioned
        Nordic-industrial alternative surfacing via swedish-equity-review or
        screening, industrials/financials concentration needing correction, or
        genuine fundamental deterioration (declining margins/revenue), which
        would remove even the track-record rationale.
CONFIDENCE: High
HORIZON: Medium
```

---

## Where the agents disagreed

**1. Crypto: valuation says cheap, macro says wrong side of the regime. This is
the real one.** Valuation's cycle-position read is that BTC sits -48.9% off its
ATH and ETH -61.5% — directionally supporting the portfolio's own recorded
"cheap vs history" framing. Macro-regime says the opposite is the operative
signal right now: DXY at 119.06 (historically strong) paired with crypto Fear &
Greed at 27 is a combination that historically *compounds* crypto weakness
rather than offsetting it, and it explicitly flags COIN-XBT.ST and the ETH
wallet as the one part of the book squarely on the wrong side of the current
regime. **I am not resolving this** — nobody has the data to. What I did
instead was size Call 1 so the answer does not depend on it: a one-unit trim
leaves crypto at or above its 10% target on every denominator, so you stay
long the cheap-vs-history thesis while removing the trip-wire breach and the
most expensive fee in the book. **Confidence in the crypto direction itself:
Low. Confidence in the action: High.** Those are different things and the memo
keeps them apart deliberately.

**2. Thesis-review grades the two crypto positions differently — correctly.**
COIN-XBT.ST WEAKENING, ethereum INTACT, on overlapping macro. Not a
contradiction: the ETH thesis rests on a stated 3y+ conviction about BTC/ETH
being the most secure cryptocurrencies, with neither break condition triggered;
the certificate's thesis rests on a cycle-timing claim ("positive buy-in
signals now") that Fear & Greed 27 argues with, plus a 2.5% fee the wallet does
not pay. **This asymmetry is exactly why the trim lands on the certificate and
not the wallet** — and it is reinforced by P1: the ETH cost basis is unknown,
so any ETH disposal has uncomputable tax. Both lenses point to the same
vehicle.

**3. The user's thesis and the valuation lens are measuring different things on
ATCO-B/ALFA/ABB.** Valuation: Expensive, PEG 2.41 / 2.92 / 2.70. The recorded
thesis explicitly declines to make a valuation claim ("None stated — the user
did not cite valuation as a reason for buying"). These do not actually
conflict; they are non-overlapping. The genuine finding is that **a thesis with
no valuation leg cannot be broken by valuation** — which is why Call 4 rests on
concentration instead. Worth saying rather than smoothing over: this makes
those three holdings structurally harder to falsify than AZN.ST, whose thesis
names specific, testable break conditions.

**4. Portfolio's own three denominators disagree with each other.** 11.40% /
12.93% / 12.04% for the identical 24,434.00 SEK. Two of three breached. That
internal disagreement *is* D3, and Call 2 settles it.

**5. Macro flags its own Swedish conclusions as untrustworthy.** SE CPI is
stuck at period 2025M12 (S4), roughly eight months stale, so every SEK real-
rate figure rests on a bad input. Macro said so rather than reporting a number.
That matters more than usual here because the majority of the individual-stock
sleeve is SEK-denominated — **any regime-driven call on Swedish industrials
would be built on a known-stale input, which is a second reason Call 4 is HOLD
rather than a rotation.**

---

## Broken theses requiring a decision

**None broken.** From thesis-review, unsoftened:

- **WEAKENING (6):** SHB-A.ST, INVE-A.ST, ATCO-B.ST, ALFA.ST, ABB.ST,
  COIN-XBT.ST. Only COIN-XBT.ST carries an action this sweep (Call 1); it is
  also the only one whose recorded break condition has actually triggered.
- **INTACT (4):** AZN.ST, Avanza Auto 3, Avanza Global, ethereum.
- **TOO_EARLY (1):** VOLV-B.ST, ~9 days held.
- **Cross-holding pattern, thesis-review's own flag:** SHB-A.ST, INVE-A.ST and
  ATCO-B.ST are all within 1.6% of their 52-week highs simultaneously — three
  separate cases of captured upside sitting on a thin, non-differentiated
  thesis at the same moment. That is the clearest single pattern in this
  sweep and it argues that the rotation question is portfolio-wide, not
  name-by-name.
- **`portfolio.json` and thesis-review agree on every status this sweep.** No
  silent picking required. I checked each one.

---

## Rebalancing actions

From the portfolio agent, in tax-priority order, with my amendments marked.

| # | Action | SEK | Tax | Status |
|---|---|---|---|---|
| 1 | Route idle PayPal (1,177.49 USD + 266.88 EUR) into the ISK, deploy to equity | 14,079.79 gross / ~13,516.60 net at 4% worst case | No tax event | **Blocked on D1** — Call 3 |
| 2 | Trim COIN-XBT.ST, reinvest in equity inside the ISK | **2,581.34 (1 unit)** — amended down from the agent's 3,000-5,500 band | Tax-free (ISK) | **Execute Monday** |
| 3 | AF sales | n/a | n/a | Nothing sellable |
| 4 | ETH wallet | — | Uncomputable | **Do not execute** — P1 blocks tax math |

**Amendment to line 2, stated openly.** The portfolio agent's 3,000-5,500 SEK
band is not executable — the certificate trades in whole units of 2,581.34 SEK.
The band's upper end (2 units, 5,162.68 SEK) would push crypto to 8.99% on
Convention A, below the 10% target. One unit clears the trip-wire on all three
conventions and stays at or above target on all three. Proceeds to Avanza
Global per `investor_profile.json`'s `profit_recycling_rule`, not to an
individual stock.

**Net effect if both 1 and 2 execute:** ~16,098 SEK into equity, tax-free,
narrowing the ~24,200 SEK equity shortfall to ~8,100 SEK — closeable in three
months of planned 1,000-3,000 SEK contributions with no further sales. **If
only line 2 executes** (the realistic Monday case): equity moves 73.7% → 74.9%,
shortfall 24,200 → 21,618 SEK, and the trip-wire clears. That is the entire
value of line 2 on its own, and it is worth doing on its own.

---

## Confidence and horizon per call

| Call | Confidence | Horizon | What caps it |
|---|---|---|---|
| 1 — Trim COIN-XBT.ST by 1 unit | **High** | Long | Nothing material — sized to be denominator-independent; the unresolved valuation/macro split on crypto direction cannot flip it |
| 2 — Adopt Convention B, close D3 | **Medium** | Long | Emergency-buffer location unverified, which determines HB checking's treatment |
| 3 — Price the PayPal route | **High** on measuring; **Low** on which route wins | Long | Revolut's spread has never been measured — that is the entire point |
| 4 — Hold industrials, no adds, run the review | **High** | Medium | S4 (stale SE CPI) prevents a confident regime read on Swedish names; this is a reason for caution, not for action |

No Short-horizon calls this sweep, so the 10% tactical cap and the
never-High-confidence rule are not engaged.

---

## Cost of being wrong

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| 1 — Trim 1 unit COIN-XBT.ST | BTC re-rates sharply; forgone gain on 2,581.34 SEK of exposure. A BTC double costs ~2,581 SEK of upside | **Yes, fully.** 21,852 SEK of crypto (5 units + 0.50185 ETH) still participates; proceeds sit in equity, not cash |
| 2 — Convention B | Too strict: trip-wires fire earlier than needed, forcing ~2,500 SEK trims slightly sooner than optimal | **Yes.** Re-pinnable; converges with C automatically once PayPal routes |
| 3 — Revolut test transfer | Revolut is as bad as PayPal: ~4% of 100 EUR ≈ 44 SEK lost to learn it | **Yes, trivially.** Cost of *not* doing it: ~1,970-2,630 SEK/yr indefinitely |
| 4 — Hold industrials | Industrials correct 30%: the 18,444 SEK sleeve loses ~5,533 SEK, ~2.6% of total capital | **Yes**, over a 3-7y horizon. The mirror risk (selling and watching them compound) is similar in size, which is why the call is hold |

---

## Timing collisions

Not run this sweep — `calendar` was not invoked, so no earnings or central-bank
collisions were checked. Notable: **S3's fix was applied and verified working
today**, so the earnings-date fetch is genuinely available for the first time
since 2026-08-03. Call 1 (a crypto certificate trade) has no earnings exposure
by construction, so nothing in this memo is materially exposed to the gap. Run
`calendar` next sweep — it will work now.

---

## Open actions

Things to go do. Pulled from `/OPEN_ITEMS.md`.

| ID | Action | Amount / detail | By when |
|---|---|---|---|
| — | **Sell 1 unit COIN-XBT.ST, buy Avanza Global with the full proceeds.** Both inside the ISK | ~2,581.34 SEK | Monday 2026-08-17 |
| **P3 / D1** | Execute a small test transfer PayPal → Revolut, convert to SEK, record both figures | 50-100 EUR | Before next sweep (third sweep of asking) |
| **P6** | Run `swedish-equity-review` on ATCO-B.ST, ALFA.ST, ABB.ST retroactively | — | Before next sweep (sixth sweep of asking) |
| **S12** | Write the Convention B definition into `data/cache/definitions.json`, in words, dated | — | This week; closes D3 |
| — | Fix the Excel workbook items in section "Excel data gaps" below | — | Before next sweep |
| **P1** | Dig up the ETH cost basis when convenient | — | Not urgent unless selling |
| **P7** | Verify the ISK allowance threshold with Skatteverket | — | Low priority; confirmation, not a live problem |

**P6's thesis half closed today.** Theses now exist for ATCO-B, ALFA, ABB and
ETH, ahead of the 2026-09-03 deadline. What remains open under P6 is only the
retroactive review.

## Open decisions

Forks where the data does not pick a single answer. Each gets concrete options.

**D3 — which denominator governs the crypto trip-wire.** *(Council recommends
Option 1; the choice is yours.)*
1. **Convention B, investable-only (Avanza ISK + ETH wallet, 188,918.15 SEK).**
   Trade-off: strictest, so trip-wires fire earliest — but it measures only
   capital you can actually reallocate today, and it converges with Option 2
   automatically once PayPal routes.
2. **Convention C, classified capital excluding the tax reserve (202,997.94
   SEK).** Trade-off: a truer long-run picture of investable net worth, but it
   counts 14,079.79 SEK of PayPal you cannot move without paying ~4% — so it
   flatters every risk percentage using money that is not really spendable.
3. **Convention A, all classified capital (214,361.70 SEK).** Trade-off:
   simplest and most stable, but it counts 11,363.76 SEK already owed to
   Skatteverket as capital you can allocate. This system ruled against that
   principle on 2026-08-06.

**D4 (new) — does `profit_recycling_rule` apply to gross proceeds or to the
realized gain only?** Selling 1 unit of COIN-XBT.ST at 2,581.34 against a
2,016.67 cost basis realizes a 564.67 SEK gain; the other 2,016.67 SEK is
return of capital. Your stated rule — "the money I make from this should to the
greatest extent go into the safer tiers" — reads either way. This is the same
ambiguity class as D3 and S12, and it recurs on every future trim.
1. **Whole proceeds to the secure tier** (2,581.34 SEK → Avanza Global).
   Trade-off: simplest, one order, satisfies the rule under either reading, and
   leaves no idle cash to go stale — a failure mode this system has hit twice.
   **Recommended, and what Call 1 assumes.**
2. **Realized gain only to secure** (564.67 SEK → Avanza Global; 2,016.67 SEK
   free for the medium tier, e.g. 1 AZN.ST share at 1,529 SEK). Trade-off:
   literal reading of "money I make," and AZN.ST is the only individual name
   thesis-review would buy today — but it leaves ~488 SEK idle and adds a
   second order for a ~2,000 SEK routing difference.
3. **Declare the rule applies to gross proceeds as a standing convention** and
   write it into `investor_profile.json`. Trade-off: closes the question
   permanently for all future trims, at the cost of slightly over-weighting the
   secure tier on every recycling event.

**D2 remains resolved** (route 100% of new contributions to equity while cash
sits at or above its 5% target). No re-litigation.

---

## Excel data gaps

A fresh Excel import ran this sweep (`data/cache/excel_import/latest-summary.json`,
generated 2026-08-12 22:52 UTC). Fundamentals refreshed for seven tickers;
`portfolio_deltas` empty; `transactions_appended` 0 (consistent with today's
dedup fix); `watchlist_entries` **45**. Flags, verbatim from that file:

1. **ATCO-B.ST: P/E 2.05 is outside the 3-80 sanity range — treat as suspect,
   verify in Excel before using it.** *Not used anywhere in this memo* —
   valuation ran on the Yahoo figure (33.4x). Refresh that cell's Stocks data
   type; it is the same bad value first caught 2026-08-06, so the sanity check
   is working and the underlying cell is still wrong.
2. **ALFA.ST / ATCO-B.ST / SHB-A.ST / VOLV-B.ST: no 52-week range in Excel.**
   Confirmed data-provider gap for some Nordic-primary tickers, not a formula
   bug. No action available; the 52w figures in the position report come from
   the Yahoo snapshot instead. Do not chase these.

**One gap the auto-generated flags did not catch, and it is the most
consequential.** `data/cache/excel_import/claude_excel_prompt.txt` (written
this run) lists only the five flags above. It does **not** include the stale
**1,743.61 SEK Avanza ISK cash** figure — which the workbook still carries and
which you confirmed directly on 2026-08-11 is gone. That figure funded a live
recommendation on 2026-08-11 and had to be retracted. It is correctly recorded
as flagged-not-applied in `portfolio.json` (cash stays at 0, your direct
statement outranks the workbook), but the workbook itself still needs it
corrected to 0 by hand. **Do this before the next sweep** — it is the single
Excel item with a track record of producing a wrong recommendation. That the
conflict surfaced as a portfolio-delta rejection rather than a `flags` entry,
and so never reached the paste-ready fix prompt, is evidence worth handing to
`meta`.

**Positive note for `meta`:** the Watchlist has grown from 32 entries
(2026-08-06) to **45**, now larger than the ~43-ticker `data/universe.json` it
replaced. That is direct evidence against S10's core complaint. Whether the
specific gaps S10 named (a Nordic consumer name, a bank alternative to SHB-A.ST,
EU-UCITS-domiciled ETFs rather than unpurchasable US-domiciled ones) were
actually filled is a question for `scout`/`meta`, not answerable from the
summary's entry count alone.

---

## Learning notes

- **Choosing a trim size is a different question from choosing a trim
  direction, and the second one is where the leverage is.** Four independent
  lines pointed at trimming crypto this sweep, but the agent-recommended
  3,000-5,500 SEK band would have overshot: at two units the position drops to
  8.99% of capital on the broadest denominator, a full point *below* your own
  10% target. You would have cleared a trip-wire by creating an underweight —
  fixing one deviation with another. The right move was to find the size that
  satisfies every competing measurement at once. When a rule and a target pull
  in opposite directions, solve for the overlap rather than picking a side.
- **Sell the wrapper, not the idea.** The strongest argument against trimming
  was genuinely good: BTC is 49% off its high with sentiment at Fear, and
  selling drawn-down assets into fear is the classic retail mistake. What
  dissolves that objection is noticing the position has two separable
  properties — exposure to bitcoin, and a 2.5%/yr certificate fee. You hold
  bitcoin exposure through the expensive vehicle *and* ethereum through a
  zero-fee wallet. Trimming the expensive one preserves the conviction and
  removes 64.53 SEK/yr of guaranteed drag. A guaranteed cost beats an uncertain
  gain when you can separate them.
- **Where money came from determines where it should go — the provenance
  rule.** Last sweep routed spare ISK cash to AstraZeneca; this sweep routes
  crypto trim proceeds to Avanza Global instead. That looks like a reversal and
  is not. Your own `profit_recycling_rule` says gains from the high-risk tier
  default into the secure tier — "a monetising machine." Last sweep's money was
  leftover build cash, which the rule does not cover; this sweep's is a
  high-risk-tier realization, which it does. Rules that key on the *source* of
  capital rather than its amount are what stop a portfolio from silently
  ratcheting up risk with every profitable trade.
- **A thesis with no valuation leg cannot be broken by valuation — and that is
  a weakness, not a defence.** ATCO-B, ALFA and ABB are all "Expensive" on
  PEG, and the recorded thesis explicitly makes no price claim ("strong track
  record… want to promote Swedish stocks"). Those two statements do not
  contradict each other; they never touch. The consequence is that these three
  holdings are structurally *harder to falsify* than AstraZeneca, whose thesis
  names testable break conditions (margins deteriorate, dividend cut, re-rates
  to a growth premium). An unfalsifiable thesis is comfortable to hold and
  impossible to be wrong about, which is exactly why the binding constraint on
  those names had to come from somewhere else — portfolio concentration, which
  is a fact rather than an opinion.
