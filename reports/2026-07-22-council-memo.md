# Council Memo — 2026-07-22 (follow-up sweep: how to deploy new cash)

*This is not investment advice from a licensed advisor — it is structured
synthesis of this system's own agent outputs, built only from data fetched
this session. Where data is missing, that is stated; nothing below is
estimated from training knowledge.*

*Triggered by user-supplied updates, not the regular cadence: the HB+SEB
transfer landed, real tax figures came in, and the risk-tier framework
(secure/medium/high-risk-active) was clarified enough to act on. This
memo's job is narrower than a full sweep: what to do with the cash, and
what else is now open.*

## Blocking-question status

Resolved, unchanged from 2026-07-20 (Handelsbanken wrapper confirmed
2026-07-07, funds exited 2026-07-12) — no blocking preamble required.

## Portfolio health scorecard

*Carried over verbatim from the portfolio lens. Total portfolio value:
≈227,703 SEK.*

| Dimension | Grade | Reason |
|---|---|---|
| Asset allocation vs. targets | **ACT** | Cash 74.1% vs. 5% target (+69pp); equity 1.6% vs. 50% (-48pp); fixed income 0% vs. 40% (-40pp); crypto 12.3% vs. 5% (+7pp) — driven almost entirely by the 144,864 SEK sitting undeployed. This sweep's deployment directly fixes most of it. |
| Equity sector concentration | **UNKNOWN** | Equities fetch blocked 3 sweeps running. |
| Geography / home bias | **UNKNOWN** (qualitative: home-biased) | SHB-A.ST, INVE-A.ST Swedish by identity; no fetched country-weight data. |
| Currency exposure | **UNKNOWN** (partial) | SEK-dominant by account; PayPal (~14.3k SEK) and crypto add real, unquantified FX exposure. |
| Single-position concentration (cap 15%) | **OK** | Largest non-cash position: Avanza Auto 3 at 7.2% (stale price). |
| Institution concentration (cap 80%) | **WATCH** | Avanza = 181,254 / 227,703 = **79.6%** — essentially no slack left under the cap. Mostly the correct byproduct of ISK consolidation, worth naming. |
| Fee drag (cap 0.4%/yr) | **UNKNOWN** | 43,479 SEK (19.1% of portfolio — Auto 3, Tundra, COIN-XBT.ST, Swedbank fund) has zero confirmed fee data. Cheapest high-value fix in the system: four factsheet pulls. |
| Wrapper efficiency | **WATCH** | ISK consolidation essentially done. Two open items: Swedbank fund (10,000 SEK, AF) blocked on cost basis; tax-reserve shortfall (see below). |
| Drawdown-tolerance fit (-30% max) | **UNKNOWN** | No backtest exists for the adopted 50/40/5/5 glidepath. Qualitative flag stands: the profile's own text says 50% equity sits at the -30% tolerance "with zero slack" — argues against overshooting equity in this deployment. |

## Risk-tier snapshot (the operating framework, adopted 2026-07-20)

Tier-eligible capital (excludes the tax reserve, checking cash, and PayPal, whose routing is undecided) = **203,754 SEK**.

| Tier | Current | % of tier-eligible capital | Target |
|---|---|---|---|
| Secure — actually invested (Avanza Auto 3) | 16,376 SEK | 8.0% | 70% |
| Secure — cash awaiting deployment | 144,864 SEK | 71.1% | (part of 70%) |
| Medium — confirmed (SHB-A.ST + INVE-A.ST) | 2,076 SEK | 1.0% | 20% |
| Medium — candidate, tier fit unconfirmed (Tundra) | 1,563 SEK | 0.8% | (part of 20%) |
| Unmapped (Swedbank fund) | 10,000 SEK | 4.9% | — |
| High-risk-active (COIN-XBT.ST + ETH) | 28,040 SEK | 13.8% | 10% (hard cap) |

**If the full 144,864 SEK goes to secure, secure rises to ~79% — itself over its own 70% target — while medium stays at ~1-2% against a 20% target.** This is a known tradeoff, not an oversight: medium-tier growth needs individual-stock theses (a valuation/thesis-review workstream, not a cash-deployment one), and the alternative — holding cash "waiting" for stock picks — directly contradicts your own instruction not to let money sit idle. Flagged as an open decision below, not silently resolved.

## Headline calls

1. **Deploy the 144,864 SEK ISK cash into the secure tier now — no reason to phase it.** Macro-regime finds nothing in current conditions (non-restrictive real rates, low VIX, non-inverted curve) that argues for waiting; lump-sum is defensible on regime grounds alone. Confidence: **High** (on timing/not-waiting) · **Medium** (on the specific split — see open decision #1) · Horizon: **Long**
2. **Trim COIN-XBT.ST — full agreement across all four lenses.** Macro, thesis-review, and portfolio all independently point the same direction; valuation couldn't assess it (data blocked) but doesn't contradict. The open question is *how much* — the 5% glidepath target and the 10% tier cap disagree on the number (see open decision #2). Confidence: **Medium** (direction) · Horizon: **Long**
3. **Tax-reserve shortfall is confirmed, not estimated: 11,493.28 SEK owed vs. 9,017 SEK reserved.** Concrete, low-urgency action below — this is real money already owed, not a market call. Confidence: **High** · Horizon: **Long** (2027 deklaration)
4. **Equities data blackout has now persisted 3 consecutive sweeps (2026-07-20, 2026-07-22 ×2) — confirmed non-transient, an infrastructure defect, not noise.** It's starting to constrain real decisions (can't verify COIN-XBT.ST's live price before trimming it). Confidence: **High** · Horizon: N/A (process)
5. **Institution concentration (Avanza 79.6%) is now touching its own cap.** Not actionable today — it's the correct result of consolidation — but any further move of outside capital (e.g. the Swedbank fund) into Avanza should be weighed against this. Confidence: **High** · Horizon: **Long**

## Open actions (no decision needed — just do these)

1. **Top up the hb-main tax reserve.** Confirmed shortfall against the confirmed 11,493.28 SEK HB+SEB tax bill: **726.28 SEK** once the pending 1,750 SEK inflow lands (recommended default — let it land first, then top up), or **2,476.28 SEK** now if you'd rather close it immediately. Either way, fund this from outside the 144,864 SEK ISK pool — different wrapper, different purpose. Deadline: before the 2027 deklaration (not urgent).
2. **Get the Swedbank fund's cost basis** (a statement/login check, same pattern as the resolved HB/SEB exits). Nothing can be decided about that 10,000 SEK AF holding until this exists — it's the single blocker on an otherwise-simple AF→ISK move.
3. **Pull factsheets for Avanza Auto 3, Tundra, COIN-XBT.ST, and the Swedbank fund** — annual fee %, needed to close the fee-drag scorecard row (19.1% of the portfolio currently ungraded).
4. **Confirm COIN-XBT.ST's live price before executing any trim** — the 15,540 SEK / 2,590-per-unit figure used in this memo's math is 9 days stale.

## Open decisions (each with concrete suggested options — your call)

**1. How to split the 144,864 SEK deployment between equity index and fixed income.**

| Option | Equity | Fixed income | Why you'd pick it |
|---|---|---|---|
| **A — glidepath-matched (recommended default)** | 80,480 SEK (55.6%) | 64,384 SEK (44.4%) | Matches the already-adopted 50:40 target ratio directly — closes both gaps proportionally. |
| B — simple 50/50 | 72,432 SEK | 72,432 SEK | Slightly more conservative given fixed income is starting from literally 0 SEK. |
| C — FI-priority | 60,000 SEK (41.4%) | 84,864 SEK (58.6%) | Most conservative — leans into the profile's own flag that 50% equity already sits at the -30% drawdown tolerance with zero slack. |

Fund categories (not specific tickers — equities data is blocked, and none of these are in any fetched snapshot; pick from Avanza's own fund search):
- Equity: a broad global/all-country low-fee index fund (~0.2%/yr) is the default, consistent with the already-adopted "plain global unhedged, no currency tilt" stance.
- Fixed income: a short-duration SEK investment-grade bond index fund fits the soft 3-7y horizon best; a global aggregate SEK-hedged fund is the broader-diversification alternative.

**2. Crypto sizing: hold to the 5% glidepath target, or use the 10% risk-tier cap as the actionable near-term number?**

The two adopted frameworks disagree here: ETH alone (12,500 SEK, 5.49% of total) already exceeds the 5% glidepath before counting the certificate at all, and closing that fully would mean touching ETH — which the standing ruling explicitly avoids (K4 tax on an unknown cost basis). The 10% tier cap is achievable tax-free, today, by trimming only the certificate.

| Option | Action | Trade-off |
|---|---|---|
| **1 — use the 10% tier cap as binding now (recommended default)** | Trim COIN-XBT.ST by ~5,270 SEK (~2 of 6 units at stale pricing — confirm live price first); proceeds route to the secure-tier deployment per the profit-recycling rule | Achievable immediately, tax-free, consistent with the "trim, don't dump" pattern of the last two sweeps. Leaves crypto at ~10%, not 5%. |
| 2 — hold to the stricter 5% glidepath | Same trim as above, PLUS start the ETH cost-basis project (open question 2) so a future partial ETH sale becomes tax-computable | Gets to the "real" target eventually, but forces the ETH question sooner than the standing ruling intended, and still can't fully close the gap this sweep either way. |
| 3 — defer the trim entirely this sweep | No action on crypto | Leaves the standing default (open question 7) unexecuted for a third sweep running — not recommended, given all four lenses agree on direction. |

**3. Does Tundra Sustainable Frontier belong in the medium tier?**

Your own description of medium was "normal stocks... good trend and good figures" — Tundra is an actively-managed frontier-market *fund*, a different risk profile.

| Option | Classification | Note |
|---|---|---|
| **1 — classify as medium anyway (recommended default)** | Medium | Smallest position (1,563 SEK) in the portfolio; low stakes either way, and it's equity-flavored risk like the rest of medium. |
| 2 — exclude from the tier framework until the factsheet lands | Unmapped, like the Swedbank fund | More precise, but adds a third "unmapped" bucket for a 1,563 SEK holding — arguably more bookkeeping than the position warrants. |
| 3 — reclassify as high-risk-active | High-risk-active | Frontier markets can be more volatile than "normal stocks," but this tier is defined by active weekly trading behavior, which doesn't fit a buy-and-hold fund position. |

**4. What to do about the persistent equities data block.**

| Option | Action | Trade-off |
|---|---|---|
| 1 — request a policy exception for `fc.yahoo.com` | Ask whoever manages this environment's egress policy | Fixes it properly, but outside this system's control — needs a human with admin access. |
| **2 — accept the gap, rely on your own periodic live checks (recommended default for now)** | You report live prices/values when you have them (as you did for the Avanza total this session) | No fix needed on your end; already working in practice, just manual. |
| 3 — add an alternate free data source as a fallback for these three tickers | Engineering change to `fetch_market_data.py` | Real fix, but a system change, not a today decision — flag for `meta`. |

## Where the agents agreed

**Full alignment on the crypto trim, worth stating plainly.** Macro-regime (strong dollar + Fear & Greed 33 is a headwind, not a "buy the dip" signal), thesis-review (the standing trim default is triggered and still unexecuted), and portfolio (concrete tax-free math showing the 10% cap is achievable today) all point the same direction. Valuation couldn't independently verify (data blocked) but raised no contradiction. This is the second consecutive sweep with this alignment — not manufactured tension, genuine agreement.

**Macro and portfolio also agree on deployment timing:** nothing in current conditions argues for phasing the 144,864 SEK purchase — lump-sum into the secure tier is not fighting the regime.

## Where the agents disagreed (or left tension unresolved)

**Valuation vs. macro on ETH specifically — same tension as last sweep, unchanged by new data, and not actionable this sweep either way.** ETH's cycle-position read continues to improve (ATH drawdown -60.4%, was -61.7%; 30d momentum +10.81%, was +7.78%) while macro's dollar-strength/sentiment headwind is unchanged. Thesis-review adds a new angle: under the newly-adopted high-risk-active tier, which expects weekly engagement, a *rising* un-thesis'd ETH position is arguably a bigger behavioral gap than a falling one — nothing is forcing a decision while price moves. No action follows from this; it's a flag for whenever ETH's cost basis question (open question 2) gets picked up.

## Broken theses requiring a decision

Unchanged in substance from 2026-07-20: SHB-A.ST, INVE-A.ST, Avanza Auto 3, Tundra, COIN-XBT.ST, and ETH all still have no recorded thesis. Thesis-review adds a sharper point this sweep: **the medium tier's own definition ("demonstrated good trend and fundamentals," moved only "if better off elsewhere") is itself an implicit, untested thesis for SHB-A.ST and INVE-A.ST** — and it can't currently be tested at all, since the equities fetch that would supply trend/fundamentals evidence has failed 3 sweeps running. This makes the two Swedish stocks more overdue than Tundra or Auto 3, whose target tiers aren't even settled yet (see open decision #3).

## Rebalancing actions — summary (tax-priority order)

1. **ISK-internal, no tax event:** deploy 144,864 SEK per open decision #1's chosen split; trim COIN-XBT.ST ~5,270 SEK per open decision #2 (proceeds added to the deployment pool).
2. **AF, taxable — not executed, blocked:** Swedbank fund move, pending cost basis (open action #2).
3. **Self-custody crypto:** no ETH disposal.
4. **Cash management, outside any wrapper:** top up hb-main tax reserve per open action #1.

## Cost of being wrong

| Headline call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| Lump-sum deploying 144,864 SEK now vs. phasing | If markets drop sharply right after deployment, a 10% correction on the equity portion (~80,480 SEK under Option A) ≈ **8,048 SEK** paper loss | Yes — long horizon (3-7y soft goal), fully recoverable on a multi-year view |
| Trimming COIN-XBT.ST to the 10% tier cap instead of the 5% glidepath | If crypto rallies hard, foregone upside is smaller than a full trim to 5% would have missed — roughly proportional to the ~5,270 SEK difference between the two targets, so a 20% rally missed on that delta ≈ **~1,050 SEK** | Yes — tax-free inside ISK, position can be rebuilt |
| Deferring the hb-main top-up until the 1,750 SEK inflow lands | No downside beyond the 2,476.28 SEK sitting briefly under-reserved for a few days — the tax isn't due until spring 2027 | Yes, fully recoverable, just timing |
| Not yet resolving Tundra's tier classification | Immaterial in isolation (1,563 SEK); the real cost is bookkeeping drift if left unresolved across many sweeps | Yes, trivially |
| Equities data blackout persisting | Continues to force trims/purchases on stale (9+ day old) prices; on COIN-XBT.ST specifically, a mispriced trim could be off by low hundreds of SEK if the live price has moved materially | Yes — re-verify before executing, not a structural loss |

## Timing collisions

- **FOMC meeting, 2026-07-28 to 07-29** — 6-7 days out. Recommend executing both the deployment and the COIN-XBT.ST trim before then: crypto in particular tends to move on FOMC statements, and there's no reason from macro-regime to wait, so there's no benefit to letting this land during FOMC-week volatility.
- **Riksbank rate decision + Monetary Policy Report, 2026-08-20** — outside this sweep's action window.
- No equity earnings collisions checked — fetch blocked, same as market-data (open action noted above).

---

**Journal must run next to log this sweep.** An unlogged memo is
invisible to the next session and can never be reconciled against future
data.
