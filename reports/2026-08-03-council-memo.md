# Council Memo — 2026-08-03

*This is structured synthesis of this session's four analyst agents (valuation,
macro-regime, thesis-review, portfolio), not investment advice from a licensed
advisor. Nothing here executes anything.*

Snapshot: `data/snapshots/20260803T060716.json`. Calendar:
`data/calendar/20260803-events.json`. Open structural question #1
(Handelsbanken wrapper) is resolved (confirmed 2026-07-07) and does not open
this memo.

**Two data-pipeline gaps this sweep, distinct from each other:**
1. **COIN-XBT.ST price fetch failed (404)** — a live crypto-certificate
   position (last known 16,218 SEK, 2026-07-28, now 6 days stale) has no
   current price. This is a live-position pipeline defect, not a hold/sell
   signal. Every crypto-weight number below that includes COIN-XBT.ST is
   built on a stale figure.
2. **Earnings-date fetch failed for all three tickers** (connection reset) —
   no earnings-calendar collision data exists this sweep. Say so; don't
   infer from silence.

---

## Portfolio health scorecard (carried verbatim from portfolio agent)

Profile is populated, not TBD — scorecard is not provisional. One caveat:
`horizon.primary_goal` is explicitly "soft"/undecided, which the adopted
85/10/5/0 target already flags as unconfirmed against the -30% drawdown
tolerance (no backtest exists yet).

| Dimension | Grade | Reason |
|---|---|---|
| Asset allocation vs target | ACT | Equity 60.16% vs 85% target = -24.84pp. Driven by undeployed cash (Q16, 26,400.30 SEK) and idle PayPal cash (~14,369 SEK), not market losses. |
| Equity sector concentration | UNKNOWN | Only SHB-A.ST/INVE-A.ST have sector data (both Financial Services, 0.98% of total, immaterial). Avanza Global (91% of equity sleeve) has no sector look-through. |
| Geography (home bias) | UNKNOWN | Direct Sweden-listed = 0.98% of total. Avanza Global's country breakdown not fetched. |
| Currency exposure | UNKNOWN | No revenue-currency-mix data fetched for any holding. |
| Single-position concentration | ACT | Avanza Global = 119,999/219,194.49 = 54.7% of total vs 15% max. Diversified fund lowers idiosyncratic risk but the rule is still breached. |
| Institution concentration | ACT | Avanza = 180,961.45/219,194.49 = 82.55% vs 80% max — 2.55pp breach, direct byproduct of the (correct) wrapper-consolidation move. |
| Fee drag | WATCH | Known drag 468.60 SEK/yr = 0.21% of total, under 0.4% cap — but Avanza Global's TER unconfirmed (Q17) and it's 54.7% of portfolio, so the real number is currently unknowable and could push this to ACT. |
| Wrapper efficiency | OK (related WATCH) | No capital in taxable AF; exit fully executed. ISK headroom ~119k vs assumed 300k threshold (unverified). ~14,369 SEK sits in PayPal outside any wrapper (Q6). |
| Drawdown-tolerance fit | UNKNOWN | No backtest exists for current or adopted 85/10/5/0 allocation. |

---

## PROPOSED target allocation (standing item — not yet written into portfolio.json)

The 85% equity / 10% crypto / 5% cash / 0% fixed-income target used by the
portfolio lens this sweep is a **proposal**, derived from investor_profile.json's
house-deposit 3–7y soft horizon, -30% max-drawdown tolerance, and glidepath
consideration. It was user-approved in chat 2026-07-27
(`reference_targets.ADOPTED_2026-07-27`) but `portfolio.json.targets` is still
`null`. This memo continues to treat it as the operating target per standing
instruction, but the write-back gap itself is an open action (below).

| Class | Current | Proposed target | Drift |
|---|---|---|---|
| Equity | 60.16% | 85% | -24.84pp |
| Crypto | 13.10% | 10% | +3.10pp |
| Cash | 23.78% | 5% | +18.78pp |
| Fixed income | 2.95% | 0% | +2.95pp |

Risk-tier cross-check (60/30/10 operating control): Secure 74.2% vs 60%
target (overweight, mostly idle cash), Medium 0.98% vs 30% target (~63,605
SEK gap — the single largest structural gap in the portfolio), High-risk
13.10% vs 10% target.

---

## Headline calls

1. **COIN-XBT.ST price fetch is broken on a live ~16,218 SEK position.**
   Retry before next sweep — no crypto-weight, fee-drag-on-crypto, or
   thesis number involving this holding is fully trustworthy until fixed.
2. **Avanza Global's TER is still unconfirmed (Q17) on 54.7% of the
   portfolio.** This single unknown determines whether the fee-drag grade
   is WATCH or ACT. Resolving it is the highest-leverage open item this
   sweep, ahead of any stock-level question.
3. **The ISK-cash deployment plan directs 4,000-7,000 SEK to the high-risk
   sleeve, which works against the portfolio agent's own standing decision**
   (2026-07-27) to let new equity contributions dilute the crypto overweight
   rather than trim it. That's an internal inconsistency in this sweep's own
   plan, not a cross-agent disagreement — flagged for a decision below.
4. **Three positions carry no recorded thesis** — SHB-A.ST, INVE-A.ST, and
   ETH. ETH's gap (~12,500 SEK, ~5.7% of portfolio) has now persisted 10+
   sweeps and is a standing process failure, independent of price.
5. **SHB-A.ST: valuation and thesis-review read the same facts in opposite
   directions.** Valuation calls it fair-leaning-expensive on fundamentals
   (PEG ~20, revenue -3.8%, Yahoo "underperform"); thesis-review notes
   Chairman + board member bought >750M SEK combined within 48 hours
   (2026-07-20/21). Neither agent resolves this — it's the headline
   tension on this name, not a footnote.

---

## Open actions (things to just go do)

- **Retry the COIN-XBT.ST price fetch** before the position is treated as
  current in any weight or fee calculation. No deadline pressure but it's a
  live position — do this before next sweep.
- **Get Avanza Global's actual TER** from the fund factsheet/Avanza's own
  page — this is a lookup, not an open-ended research task, and it flips
  the fee-drag grade. Treat as urgent (portfolio agent's own framing).
- **Get PayPal's actual currency-conversion spread** before moving the
  ~14,369.28 SEK idle balance into ISK — don't assume 3-4%, confirm it.
- **Verify the ~300k SEK ISK allowance figure with Skatteverket** — rules
  changed recently and the current 30% AF/K4 tax-math assumption rests on
  this being right.
- **Continue monthly contributions (1,000-3,000 SEK) into the equity/secure
  tier** per the investor profile — at the top of that range, this closes
  the residual equity gap in ~5 months without any tax event.
- **Verify the FOMC 2026-09-15/16 dates** — the calendar file flags these as
  model-knowledge, not confirmed against a live Fed calendar source.
- **Write the adopted 85/10/5/0 target into `portfolio.json.targets`** (it's
  approved but still `null`) — this is a bookkeeping action, not a new
  decision; it just needs to happen so future sweeps stop re-deriving drift
  against a target that technically isn't recorded anywhere but the memo.

## Open decisions (data doesn't pick a single answer — options below)

**A. What to do with the ~18-20k SEK medium-tier slice of ISK cash (Q16).**
Neither vetted candidate is clean: Spiltan Aktiefond Investmentbolag likely
holds Investor AB, doubling up on the existing INVE-A.ST position; Swedbank
Robur Technology A is a single-sector active bet with higher fees.
- *Option 1:* Proceed with Spiltan anyway — accepts partial overlap with
  INVE-A.ST in exchange for simple, low-effort execution.
- *Option 2:* Proceed with Robur Technology A — adds sector diversification
  away from financials/holding-companies but concentrates in tech and raises
  the active-fee-drag profile.
- *Option 3:* Defer the medium-tier question and route the 18-20k into the
  existing Avanza Global position instead — closes the equity gap
  immediately at known low cost, but does nothing to build out the
  under-target medium-risk tier (0.98% vs 30%) and slightly worsens the
  single-position concentration ACT flag (already 54.7% vs 15% max).

**B. What to do with the 4,000-7,000 SEK high-risk slice of ISK cash (Q16).**
- *Option 1:* Execute as originally planned — adds to the crypto certificate,
  but directly works against the standing 2026-07-27 decision to dilute the
  crypto overweight (13.10% vs 10% target) via new equity money, not new
  crypto money.
- *Option 2:* Redirect the full amount to the medium/secure equity tier —
  closes more of the 54,448.57 SEK equity gap and stops deepening the
  crypto overweight; consistent with the portfolio agent's own stated
  reasoning against this slice.
- *Option 3:* Split it — a token amount to crypto, majority to equity —
  adds execution complexity for a position this small without a clear
  benefit over Option 2.

**C. SHB-A.ST — no recorded thesis, and fundamentals vs. insider signal
disagree.** Position is small (144.15 SEK, one share) so capital at risk is
trivial; the actual issue is process, not money.
- *Option 1:* Write down an explicit thesis tied to the insider-buying
  signal (event-driven, small conviction bet) — makes the position
  accountable to a testable claim going forward.
- *Option 2:* Trim/exit on the fundamentals read (PEG ~20, "underperform")
  — removes the position but discards real information (concentrated
  insider buying) that public financials don't capture.
- *Option 3:* Hold with no thesis, revisit next sweep — cheapest to
  execute, but repeats the exact failure mode ETH has been running for 10+
  sweeps.

**D. INVE-A.ST — no recorded thesis, NAV discount/premium unknown, near
52-week high (94% of range).** The real valuation call is blocked until the
NAV figure exists.
- *Option 1:* Get Investor's IR page or Q2 2026 report (via the `pdf` skill)
  before making any thesis decision — this is the actual missing input, not
  a judgment call.
- *Option 2:* Hold unchanged pending that data, don't treat the 4.71x P/E as
  a signal either way (it's explicitly a known accounting artifact for
  holding companies).

**E. ETH — no thesis after 10+ sweeps, ~12,500 SEK, ~5.7% of portfolio.**
- *Option 1:* Document an explicit thesis (e.g., long-horizon asymmetric
  diversification bet, accept the current regime headwind as noise on a
  3y+ horizon) — formalizes existing behavior, no capital action, but
  finally gives the position a falsifiable claim to test each sweep.
- *Option 2:* Reduce the position on the "undocumented conviction is itself
  the risk" reasoning — cuts exposure but the cost basis is unknown (Q2),
  so a wallet sale triggers an unquantifiable K4 gain calculation.
- *Option 3:* Convert wallet ETH into an ISK-wrapped certificate (mirroring
  the COIN-XBT.ST structure) — brings it under wrapper efficiency at a
  cost of ~2.5%/yr fee plus counterparty risk, but this move is also
  blocked by the same unknown cost basis (a wallet-to-certificate
  conversion is itself a taxable disposal) and does not by itself fix the
  missing-thesis problem — it's a wrapper move, not a conviction move.

---

## Where the agents disagreed

**SHB-A.ST: valuation vs. thesis-review, unresolved.** Valuation reads the
fundamentals as cautious-to-expensive (PEG ~20 on -3.8% revenue growth,
forward P/E 12.77x exceeding trailing 12.17x, Yahoo "underperform," near
83% of 52-week range). Thesis-review surfaces a directly opposing signal:
Chairman Pär Boman and board member Fredrik Lundberg together bought >750M
SEK of stock within 48 hours (2026-07-20/21) — real information, not
sentiment. Macro-regime separately calls SHB "reasonably well-positioned"
for the current regime on curve/dividend grounds, a third framing that
doesn't fully engage with either the fundamentals caution or the insider
signal. No agent resolves the conflict between deteriorating operating
fundamentals and concentrated insider buying. **Confidence: low. This is
not a call the free data can settle — it needs the user's own read on how
much weight insider buying carries versus a genuine "underperform" from
the fundamentals, or it needs to wait for a next-quarter print.**

**Crypto direction: macro-regime vs. valuation's background framing.**
Macro-regime is explicit and current-data-based: strong dollar (120.71) +
Fear & Greed 28 is "a 'gets cheaper here' setup, not 'more attractive'" —
a real regime headwind specific to dollar-correlated, no-yield assets.
Valuation floats a competing frame as an explicit caveat, not a data claim:
historically, Fear + stable market-cap rank is "more often
contrarian-accumulation than capitulation" — flagged by valuation itself
as background knowledge, not live data. These two readings point in
opposite directions on what Fear & Greed 28 means right now.
**Confidence: low on direction either way.** This is procedurally moot for
action this sweep, though: crypto is already 13.10% against a 10% proposed
target, so neither reading supports adding to the position regardless of
who's right about the regime call.

**Internal portfolio-lens tension (not cross-agent, but real).** The
portfolio agent's own rebalancing plan allocates part of the ISK cash to
the high-risk sleeve while, in the same document, flagging that doing so
works against its own 2026-07-27 decision to dilute the crypto overweight
via new equity money rather than new crypto money. Carried into Open
Decision B above rather than resolved here.

---

## Broken theses requiring a decision (unsoftened, from thesis-review)

- **COIN-XBT.ST** — Weakening, partially untestable. Original thesis was
  "BTC pretty low valued" — that premise is unverifiable this sweep (404),
  and the last confirmed price (2026-07-28) already showed +34.03% since
  cost basis, which cuts against "still cheap" even before the fetch broke.
  Halving-cycle limb (2028) unaffected, too early to score.
- **SHB-A.ST** — No thesis was ever recorded for this position. See
  disagreement above.
- **INVE-A.ST** — No thesis was ever recorded for this position. The one
  number that would let a thesis be tested (NAV discount/premium) has never
  been obtained.
- **ETH** — No thesis recorded across 10+ consecutive sweeps on a live,
  non-trivial (~5.7% of portfolio) position. This has crossed from "not yet
  filled in" to a standing system defect — should also be raised with
  `meta` as a recurring process failure, not just re-flagged here again.

Clean: Avanza Auto 3 (intact) and Avanza Global (intact, TER caveat aside)
are the only positions with a stated, currently-unbroken thesis this week.
Tundra closed 2026-07-28 on its fee-drag thesis playing out as expected —
resolved, not open.

---

## Rebalancing actions (from portfolio agent, SEK amounts)

Equity gap to close: 186,315.32 SEK target (85% of 219,194.49) vs 131,866.75
current = **54,448.57 SEK short**.

1. **Monthly contributions** (1,000-3,000 SEK/mo per profile) → equity/secure
   tier, no tax event. At the top of the range, closes the residual gap in
   ~5 months.
2. **Deploy the 26,400.30 SEK already inside Avanza ISK — zero tax cost,
   highest priority, do first.** Per Q16 plan: ~18-20k to medium-tier
   candidates (see Open Decision A, neither candidate vetted clean), ~4-7k
   to high-risk (see Open Decision B, flagged as working against the
   standing crypto-dilution decision).
3. **Move PayPal idle cash (~14,369.28 SEK) into ISK.** No ISK-side tax
   event; whether the currency conversion itself is a taxable disposal is
   uncertain — get the actual conversion spread first (open action above),
   don't assume 3-4%.
4. **No sales required.** Steps 2+3 = 40,769.58 SEK of the 54,448.57 SEK
   gap at zero tax cost. The residual ~13,678.99 SEK closes via 5-14 months
   of ongoing contributions.
5. **Self-custody ETH** — informational only, no capital action recommended
   this sweep beyond the thesis decision in Open Decision E.

Standing disclaimer carried from portfolio agent: all tax math assumes a
30% AF/K4 rate and ~300k SEK ISK allowance — unverified, confirm with
Skatteverket (open action above) before acting on any of the above.

---

## Confidence and horizon per headline call

| Call | Confidence | Horizon |
|---|---|---|
| Retry COIN-XBT.ST price fetch | High (it's a fix, not a forecast) | N/A — pipeline task |
| Resolve Avanza Global TER (Q17) | High (it's a lookup, not a forecast) | N/A — data task |
| Redirect the 4-7k high-risk ISK slice to equity | Medium (agents agree directionally; size is small) | Short — tactical sizing decision, capped, not high-confidence by policy |
| Deploy 18-20k ISK cash to medium tier | Low (both candidates have unresolved structural flaws) | Medium (6mo-3y horizon on entry, per valuation/thesis ownership) |
| SHB-A.ST hold/trim/document-thesis | Low (valuation and insider signal directly conflict, unresolved) | Medium |
| INVE-A.ST hold pending NAV data | Medium (data gap, not disagreement — clear what's missing) | Medium |
| ETH thesis documentation | Medium (the action itself is low-risk; the underlying price call stays Low per the crypto direction conflict) | Long (3y+, per profile's soft house-deposit horizon and the system's own crypto-cycle framing) |
| PayPal → ISK move | Medium (mechanics are clear, spread is unknown) | Short (execution timing), but the underlying wrapper-efficiency logic is Long |
| Monthly contribution pacing | High (structural, no forecasting involved) | Long |

---

## Cost of being wrong

| Call | Realistic downside if wrong | Recoverable? |
|---|---|---|
| SHB-A.ST hold-without-thesis | Position is 144.15 SEK (one share) — immaterial in absolute SEK either way | Yes, trivially |
| Avanza Global TER assumed low when it's actually high | If TER is ~1% instead of the assumed ~0.2-0.4%, extra drag ≈ 700-960 SEK/yr recurring on 119,999 SEK, compounding silently until detected | Yes — switch fund once confirmed, but drag accrues invisibly until Q17 is resolved |
| COIN-XBT.ST price blackout goes undetected | Stale figure (16,218 SEK) used in weight/fee calcs; realistic drift is a few hundred to low-thousands SEK of misstated position value; tail case (issuer/counterparty event) could be larger and currently invisible | Yes once fetch is fixed, but currently unmonitored |
| 4-7k redirected to crypto instead of equity (Open Decision B, Option 1) | Deepens the existing 3.10pp/≈6,800 SEK crypto overweight against the regime headwind macro-regime flagged; principal at risk ≈ 4,000-7,000 SEK | Yes, fully liquid position, but works against the portfolio's own stated dilution plan |
| ETH left undocumented and price falls further | Position is ~12,500 SEK total — that's the full capital at risk regardless of thesis status; the real cost of "undocumented" is a governance gap (no defined hold/exit criteria), not incremental SEK | Capital is recoverable (liquid); the process gap does not shrink until documented |
| Equity gap (54,448.57 SEK) left unaddressed | Opportunity cost of cash sitting idle while equities show no stress (VIX 17.09, SHB/INVE both near 52-week highs) — foregone return, not a loss | Fully recoverable via the already-identified zero-tax deployment path |

---

## Timing collisions

- **Riksbank rate decision — 2026-08-20 (17 days out, inside window).**
  Matters directly for two things this memo touches: SEK cash's currently
  positive real yield (+1.45%, cited above as a reason cash isn't a drag),
  and SHB-A.ST's NIM outlook. A cut compresses both. Sequence the
  medium-tier ISK-cash deployment (Open Decision A) with this date in mind
  if precise cash-yield timing matters to the user; not a hard blocker.
- **FOMC meeting — 2026-09-15/16 (43-44 days out, edge of window).**
  Calendar file flags these dates as model-knowledge, not independently
  verified — treat as provisional until confirmed (open action above).
  Matters for dollar trajectory, which is the mechanism behind the crypto
  headwind flagged in the macro-regime disagreement.
- **Earnings-date fetch failed for all three tickers this sweep**
  (connection reset). No earnings-date collision data exists — this is a
  genuine gap, not a "no collisions found" result. Don't read the absence
  of an earnings flag as confirmation there isn't one.
- **COIN-XBT.ST price fetch (404)** is a separate, live-position pipeline
  gap from the earnings-calendar failure above — repeated here because it
  is the most consequential data gap this sweep and should not be
  conflated with the (lower-stakes) earnings-calendar miss.

---

*Journal must run next to log this sweep — an unlogged memo is invisible to
the next session and cannot be reconciled.*
