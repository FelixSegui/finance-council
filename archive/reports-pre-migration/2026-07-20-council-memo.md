# Council Memo — 2026-07-20

*This is not investment advice from a licensed advisor — it is structured
synthesis of this system's own agent outputs, built only from data fetched
this session. Where data is missing, that is stated; nothing below is
estimated from training knowledge.*

## Blocking-question status (read this first)

CLAUDE.md's blocking-questions rule requires this memo to open with open
structural question #1 (the Handelsbanken wrapper) **while it is
unresolved**. It is no longer unresolved: `portfolio.json` confirms
resolution on 2026-07-07 (wrapper = AF/fondkonto) and the fund sale
executed 2026-07-12. That blocking condition is cleared — this memo does
not need to open with it, and the current position-1 item in
`open_structural_questions` (Auto 50/75 equity-bond split) is itself moot,
since Auto 50/75 no longer exist as holdings (sold).

**What actually dominates the portfolio's structure this sweep instead:**
the cash from that same resolved plan — **136,611.83 SEK (hb-main) +
17,382.43 SEK (seb-fund) = 154,559.26 SEK, ~68% of the entire portfolio —
has been sitting untransferred to Avanza ISK for 8 days** since both
sales settled (2026-07-12/13). The transfer itself is already
Council-approved from the 2026-07-07 sweep; nothing new needs deciding,
it needs *executing*. Every allocation number below is downstream of
this one fact.

## Portfolio health scorecard

*Carried over verbatim from the portfolio lens. Total portfolio value:
≈226,905 SEK (portfolio.json's own header estimate: ~226,935.29 SEK;
30 SEK variance is immaterial, likely PayPal FX rounding).*

| Dimension | Grade | Why |
|---|---|---|
| Asset allocation vs. profile targets | **ACT** | Cash 74.4% vs. 5% target (+69.4pp); confirmed equity 1.6% vs. 50% (-48.4pp); confirmed fixed income **0%** vs. 40% (-40pp — no dedicated FI holding exists anywhere); crypto 12.4% vs. 5% (+7.4pp). Almost entirely an execution-lag artifact of the unexecuted HB/SEB transfer, not a selection problem. |
| Equity sector concentration | **UNKNOWN** | Sector field failed to fetch this sweep (equities blocked). Immaterial in SEK terms today (confirmed pure equity is only 3,639 SEK) but must close before the equity sleeve scales toward its ~113k SEK target. |
| Geography (home bias) | **UNKNOWN** (directional flag: home-biased) | Country field failed to fetch. Both confirmed equities (SHB-A, Investor A) are Sweden-domiciled by company identity, not fetched data. |
| Currency exposure | **UNKNOWN** (equity revenue mix); known cash FX | Revenue-currency field unavailable for equities. Known and unhedged: 1,177.49 USD + 266.88 EUR idle in PayPal (≈14,291 SEK). |
| Single-position concentration (cap 15%) | **ACT** | `hb-main` settled cash = 136,611.83 SEK = **60.2% of total** — breaches the cap. It's cash-in-transit, not a security bet, but it is today's largest single line by a wide margin. No actual security breaches 15% (largest: Avanza Auto 3 at 7.2%). |
| Institution concentration (cap 80%) | **WATCH** | Handelsbanken 60.2% of total — under the 80% ACT cap, but only because it's cash mid-transfer; the approved plan already sends this toward ~0%. |
| Fee drag (cap 0.4%/yr) | **UNKNOWN (data gap)** | Confirmed drag = 0 SEK (stocks + self-custody ETH carry no % fee). But 33,479 SEK (14.8% of portfolio — Avanza Auto 3, Tundra, COIN-XBT.ST) has **no confirmed `annual_fee_pct`** — cannot be graded against the cap until factsheets land (open question 8). |
| Wrapper efficiency | **ACT** | 154,559.26 SEK approved for ISK transfer 8+ days ago, still sitting in AF-domiciled accounts. ISK allowance headroom is not the constraint (projected post-transfer ISK total ≈180–182k SEK, well under the ~300k allowance — verify current threshold with Skatteverket). This is a pure execution gap on the system's largest lever. |
| Drawdown-tolerance fit (-30% max) | **UNKNOWN** | No `data/backtests/` file exists for the adopted 50/40/5/5 glidepath. Cannot compare against the stated tolerance this sweep. Qualitative flag carried from 2026-07-07: the glidepath's own adoption rationale says 50% equity sits "at the -30% tolerance with zero slack" — a real backtest is owed before increasing equity further. |

## Headline calls

1. **Execute the already-approved HB+SEB → Avanza ISK cash transfer: 154,559.26 SEK combined (128,155.97 SEK net HB + at least 16,182.43–17,382.43 SEK net SEB pending the avräkningsnota).** No new decision required — this was Council-approved 2026-07-07. It is simply 8 days overdue. Confidence: **High** · Horizon: **Long**
2. **Trim COIN-XBT.ST (BTC certificate, 15,540 SEK / 6 units) toward the 5% crypto target.** Open structural question #7 set this sweep as the deadline: no written thesis was filed, so the standing Council default activates — trim the certificate, never ETH (unknown cost basis, real K4 tax exposure). Tax-free, ISK-internal. All three lenses that touch crypto this sweep point the same direction (see "Where the agents agreed," below) — this is not a contested call. Caveat: the 15,540 SEK price is **7 days stale** (equities fetch blocked this sweep) — re-verify the live price before executing. Confidence: **Medium** (direction is rule-driven and lens-confirmed; exact SEK amount needs a fresh price) · Horizon: **Long**
3. **Force a decision on the risk-tier framework (70/20/10) vs. the adopted glidepath (50/40/5/5) — third consecutive sweep this has been flagged and punted.** See reconciliation attempt below; a straight read shows the frameworks are genuinely in tension, not just differently labeled. Confidence: **Low** that either framework is being followed correctly while this stays open · Horizon: **Long**
4. **Equities data blackout this sweep is a system-level defect, not a one-off.** Yahoo Finance (yfinance's `fc.yahoo.com` crumb endpoint) is blocked by this environment's org egress policy — confirmed via the agent-proxy status endpoint as a policy 403, not a transient failure. SHB-A.ST, INVE-A.ST, and COIN-XBT.ST (21,112 SEK combined, 9.3% of portfolio) have no live price or fundamentals this sweep; valuation and thesis-review are both structurally blocked on all three. This will recur every sweep until fixed — flag for the `meta` agent's improvement backlog. Confidence: **High** (that this is the cause, verified against the proxy's own failure log) · Horizon: N/A (process/infrastructure)
5. **No action on the Swedbank fund (10,000 SEK, AF) this sweep — still blocked on cost basis.** Worst-case tax bound to move it to ISK remains 3,000 SEK; likely lower given "low cost basis" note. Low urgency given the small size relative to the HB/SEB transfer above. Confidence: **Medium** · Horizon: **Long**

## Where the agents agreed

**Crypto sizing — full alignment, worth stating plainly rather than
manufacturing tension that isn't there.** Macro-regime independently
flags ETH and COIN-XBT.ST as sitting on the wrong side of this sweep's
strong-dollar regime (dollar index 120.50) and bearish sentiment (Fear &
Greed 29). Thesis-review independently finds COIN-XBT.ST has missed its
thesis-filing deadline, triggering the standing trim default. Portfolio's
own sizing math independently shows crypto at 12.4% vs. a 5% target. Three
lenses, three different methods, same conclusion: trim the certificate.
Valuation does not contradict this — it could not assess COIN-XBT.ST at
all this sweep (data blackout) and its only live crypto read (ETH, "Fair"
on cycle-position terms, not a buy signal) doesn't argue against trimming
the certificate specifically.

## Where the agents disagreed

**Valuation vs. macro-regime on ETH — the same tension flagged last
sweep, unchanged by new data.** Valuation reads ETH's -61.71% drawdown
from ATH, stable #2 market-cap rank, and positive 7d/30d momentum
(+3.76%/+7.78%) as "not obviously overheated" — a cycle-position read, not
a buy signal, but not bearish either. Macro-regime reads the same
momentum against a strong-dollar backdrop (dollar index 120.50) and
Fear & Greed 29 as **confirmation** of a headwind, not something the
"cheap" framing should override — a strong dollar is a direct, mechanical
pressure on crypto independent of on-chain momentum. Neither lens is
wrong on its own terms; they weight the same two numbers differently. This
is why call — "no forced action on ETH itself this sweep" — stays
implicit rather than becoming a headline call: the position is small
(~12,500 SEK est., quantity still unrecorded in `portfolio.json` — see
data gap below) and the disagreement is unresolved, exactly as CLAUDE.md's
horizon policy would predict for a regime-dependent read.

**Macro-regime also flags a second, lower-confidence disagreement with
the portfolio-wide "risk-on" framing implicit in the US rate data:**
Sweden's own real policy rate is +1.45% (Riksbank 1.75% vs. SE CPI 0.3%)
— restrictive, the opposite of the US's near-zero real rate. SHB-A.ST and
INVE-A.ST shouldn't inherit a US-framed risk-on read by default. No
competing valuation read exists to weigh against this (equities data
blocked), so this stays a flag, not a call.

## Attempted reconciliation: risk-tier framework vs. adopted glidepath

This has been carried unreconciled since 2026-07-12 (raised), 2026-07-13
(flagged PENDING, not adjudicated), and now 2026-07-20. Per
`investor_profile.json`'s own note, the Council must define which
holdings map to which risk tier before producing SEK numbers — that
mapping is attempted here, not invented:

- A literal read maps "secure/non-volatile" → cash + fixed income. At the
  adopted glidepath's `now_T5plus` column, that's 40% + 5% = **45%** —
  25 percentage points **below** the user's stated 70% target. This is
  the same gap flagged in `investor_profile.json` and it does not
  resolve on its own; the two frameworks disagree about how conservative
  the starting allocation should be, not just about labels.
- A broader read — crediting diversified/index equity exposure as
  "secure" and reserving "high risk" for concentrated single-stock and
  crypto positions — is the only way to narrow the gap, but **this
  portfolio currently holds zero index-fund equity exposure**; both
  itemized equities (SHB-A.ST, INVE-A.ST) are single stocks, which would
  count as higher-risk under most reasonable readings of "secure," not
  lower. The broader read doesn't rescue the reconciliation with the
  holdings as they stand today.
- The risk-tier framework's 10% "high risk, actively traded weekly/daily"
  tier describes a trading *behavior* the portfolio doesn't currently
  have — no holding is being actively traded on that cadence. Adopting
  this tier is a request for new activity, not a relabeling of existing
  exposure. CLAUDE.md's own short-horizon rule already caps this exact
  behavior at 10%, never High confidence, tactical-only — so the
  *guardrail* is compatible, but the *decision to start* is not
  something this system can make on the user's behalf.

**This memo does not adopt either framework.** The gap is real and
quantified above; resolving it requires a direct user answer to which of
the two "now" starting points (50/40/5/5 vs. 70/20/10-with-an-undefined-
mapping) is actually intended, not another sweep of re-flagging.

## Broken theses requiring a decision

No thesis has "broken" in the technical sense this sweep, because most of
the portfolio's non-cash holdings never had one to break:

- **SHB-A.ST, INVE-A.ST, Avanza Auto 3, Tundra Sustainable Frontier,
  COIN-XBT.ST, ETH** — six of six non-cash, non-legacy holdings have no
  recorded thesis. That is itself the finding, not a null result.
- **COIN-XBT.ST specifically has now missed its thesis deadline** (open
  question #7) — see headline call #2 above; the standing default
  (trim) is active, not hypothetical.
- **Swedbank fund** — thesis field honestly states "no active thesis"
  (legacy childhood fund). Not a failure, an accurate non-decision.

## Rebalancing actions (tax-priority order)

1. **New contributions (1,000–3,000 SEK/mo) → Avanza ISK.** No tax
   event, uses existing headroom. Both cash and crypto are already over
   target — do not route new money there.
2. **ISK-internal, no tax event:**
   - Trim COIN-XBT.ST in full: **15,540 SEK** (6 units — re-verify price
     before executing, see call #2). Leaves crypto sleeve as ETH-only,
     ≈5.5% of total, close to the 5% target; the residual ~0.5pp is not
     worth a taxable ETH sale to close.
   - Complete the HB transfer: **128,155.97 SEK** net (8,455.86 SEK tax
     reserve stays in a separate sparkonto, not invested).
   - Complete the SEB transfer: **at least 16,182.43 SEK** net (pending
     firm figure on the ~1,200 SEK illustrative tax reserve, open
     question #4).
   - Total newly deployable inside ISK: **≈160,443 SEK** (565 existing
     cash + the three items above).
3. **AF, taxable — deferred, not executed:** Swedbank fund (10,000 SEK)
   move to ISK. Cost basis unknown; worst-case tax bound 3,000 SEK.
   Get the real anskaffningsvärde before acting (open question #3).
4. **Self-custody crypto:** no ETH disposal this sweep. Cost basis
   unknown (open question #2); any sale or swap is a taxable K4 event at
   30% on gains — do not sell to fine-tune the sub-1,200 SEK residual
   crypto gap left after the COIN-XBT.ST trim.
5. **PayPal (execution, not tax math):** convert ≈14,291 SEK
   (1,177.49 USD + 266.88 EUR) via lowest-spread path once PayPal's
   actual fee schedule is confirmed (open question #6, still open).

**Verify current ISK allowance and 30% AF capital-gains rate with
Skatteverket before executing any of the above.**

## Cost of being wrong

| Headline call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| Executing the HB+SEB transfer now (vs. further delay) | Primarily an execution-risk/opportunity-cost item, not a directional bet: further delay leaves 154,559.26 SEK earning ~0% and keeps single-institution concentration at 60%+ past the plan's intent. Order of magnitude a few hundred to ~1,000+ SEK/month in foregone market return, growing the longer it's delayed | Yes — fully recoverable by executing; no principal at risk |
| Trimming COIN-XBT.ST toward the 5% crypto target | If crypto rallies right after the trim, foregone upside on 15,540 SEK — a 10–20% missed rally ≈ **1,554–3,108 SEK** | Yes — tax-free inside ISK, position can be rebuilt |
| Leaving the risk-tier framework unreconciled | If the user actually intends the 70% "secure" target and the system keeps deploying toward the glidepath's 50/40/5/5, up to ~**45,381 SEK** (20pp of the ≈226,905 SEK portfolio) sits in a more volatile allocation than intended, which under the stated -30% drawdown tolerance could produce a materially larger felt loss in a downturn than the user signed up for | Yes, but only once reconciled — every sweep it stays open is a sweep where this gap could be live |
| Equities data blackout feeding stale-price decisions (esp. the COIN-XBT.ST trim) | If COIN-XBT.ST's live price has moved materially since 2026-07-13, the stated 15,540 SEK trim amount is off by that margin; SHB-A.ST/INVE-A.ST (3,639 SEK combined) can't be fundamentally re-assessed this sweep at all | Yes — re-verify prices before executing; not a structural loss, an execution-precision risk |
| Deferring the Swedbank AF→ISK move | Doesn't increase tax owed on the existing gain; cost is delayed start of tax-free compounding, order of magnitude tens of SEK/year foregone | Yes, fully recoverable, just delayed |

## Timing collisions

Calendar fetch (45-day window) **could not check equity earnings** for
SHB-A.ST, INVE-A.ST, or COIN-XBT.ST this sweep — same org egress block
that hit the market-data fetch. None of this sweep's actions are
single-stock trades in those names, so this is a caveat, not a live
collision, but it means an earnings surprise landing in the next 45 days
would go undetected by this system until the block is fixed.

Two macro events fall inside the window:

- **FOMC meeting, 2026-07-28 to 07-29** — 8–9 days out. The HB/SEB
  transfer is already 8 days overdue; recommend completing it before
  07-28 rather than adding FOMC-week volatility to an already-delayed
  execution. The COIN-XBT.ST trim carries the same consideration —
  crypto is typically volatile around FOMC statements; executing before
  07-28 avoids that noise on top of the stale-price issue already
  flagged above.
- **Riksbank rate decision + Monetary Policy Report, 2026-08-20** —
  outside this sweep's action window.

## Standing task — proposed target allocation status

The runbook instruction for this recurring task assumes
`investor_profile.json`'s `reference_targets` are still `null`. **They
are not** — they were adopted by Council ruling 2026-07-07 (same-day
amendment to `reports/2026-07-07-council-memo.md`) and recorded in
`investor_profile.json` as a full glidepath table (`now_T5plus`: equity
50% / fixed income 40% / cash 5% / crypto 5%, tapering through T3y/T2y/T1y
to the deposit year). This memo does not re-derive a new proposal from
scratch, since the inputs behind it (goal: property purchase, still soft,
3–7y; -30% max drawdown; 1,000–3,000 SEK/mo contributions) have not
changed since adoption, and last sweep's own reconciliation flagged
re-deriving a *different* shape from the same static inputs as a system
defect to avoid repeating. The drift table in the scorecard above grades
the portfolio against this already-adopted target, which is the correct
standing reference point going forward — not a null one. The genuinely
open allocation question this sweep is the risk-tier reconciliation
above, not a missing glidepath.

---

**Journal must run next to log this sweep.** An unlogged memo is
invisible to the next session and can never be reconciled against future
data.
