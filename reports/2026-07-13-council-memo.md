# Council Memo — 2026-07-13

*This is not investment advice from a licensed advisor — it is structured
synthesis of this system's own agent outputs, built only from data fetched
this session. Where data is missing, that is stated; nothing below is
estimated from training knowledge.*

## Open structural question #1 — still blocking (read this first)

**The Handelsbanken wrapper (`hb-main`, 134,000 SEK, 69.6% of the
portfolio) is still unconfirmed as ISK/KF vs. fondkonto/depå.** This has
now blocked three consecutive sweeps (2026-07-06 ×2, 2026-07-13). Every
number in this memo touching `hb-main` — tax treatment, fee drag, wrapper
efficiency, drawdown fit — is provisional until this is resolved. The
other three accounts (Avanza ISK, Swedbank fund, ETH wallet) are analyzed
in full below. **Action: ask Handelsbanken directly, or check whether any
sale in this account has ever generated capital-gains tax in a
deklaration.** This is the single largest lever in the system and it
remains unpulled.

## Portfolio health scorecard

*Carried over verbatim from the portfolio lens. Total portfolio value:
192,500 SEK.*

| Dimension | Grade | Why |
|---|---|---|
| Asset allocation vs. profile targets | **UNKNOWN** | `investor_profile.json` `reference_targets` for equity/crypto/fixed-income/cash are all `null`. No target is invented — see proposed glidepath below. |
| Equity sector concentration | **UNKNOWN** | Snapshot equities are empty; `avanza-isk` not itemized by ticker. |
| Geography (home bias) | **UNKNOWN** | Same cause. |
| Currency exposure | **UNKNOWN** | No equity tickers to check revenue currency against. |
| Single-position concentration (cap 15%) | **UNKNOWN (partial)** | Swedbank fund 5.19%, ETH 6.49% — both clean. HB's two sub-portfolios have no per-portfolio split — ungradable. **Avanza ISK's 36,000 SEK is one un-itemized line at 18.70% of total — if it is a single stock/fund, it already breaches the 15% cap.** |
| Institution concentration (cap 80%) | **OK** | Handelsbanken 134,000/192,500 = 69.61%, below cap. Graded fresh this sweep, strictly off current file — resolves last sweep's flip-flop on the same number. |
| Fee drag (cap 0.4%/yr) | **ACT (data gap)** | `annual_fee_pct` is `null` on 74.8% of the portfolio (HB + Swedbank). Only ETH (0%) is known. This is CLAUDE.md's #2 priority lever and it is the biggest blind spot in the system right now. |
| Wrapper efficiency | **WATCH** | 10,000 SEK sits taxed (Swedbank AF) against 264,000 SEK of unused ISK headroom. HB's wrapper status keeps 70% of the portfolio ungraded here too. |
| Drawdown-tolerance fit (-30% max) | **UNKNOWN** | 74.8% of the portfolio is "mixed" with no known equity/bond split — no basis for even a qualitative drawdown estimate. |

## Headline calls

1. **Resolve the Handelsbanken wrapper before any further action on that account.** Confidence: **High** (that this is the top priority) · Horizon: **Long**
2. **Route all new contributions (1,000–3,000 SEK/mo) to Avanza ISK, not AF or hb-main.** Uses existing 264,000 SEK of tax-free headroom at zero tax cost, doesn't grow exposure to an unconfirmed-wrapper institution. Confidence: **High** · Horizon: **Long**
3. **Itemize the `avanza-isk` 36,000 SEK line before the next sweep.** It is currently one un-itemized entry at 18.70% of the portfolio — above the 15% single-position cap if it turns out to be a single holding. This is a real possible breach hiding behind a data gap, not a hypothetical. Confidence: **High** (that this needs checking now) · Horizon: **Long**
4. **No action on ETH this sweep — valuation and macro-regime disagree on how to read the same numbers (see below), and no thesis for holding it has ever been written.** Confidence: **Low** · Horizon: **Medium**
5. **Swedbank AF→ISK move: directionally sound, blocked on real cost-basis data.** Worst-case tax bound is 3,000 SEK; the move is plausibly net-positive at that bound but should not be executed on an assumed number. Confidence: **Medium** (that the move is worth doing once cost basis is in hand) · Horizon: **Long**

## Where the agents disagreed

**Valuation vs. macro-regime on ETH — the one real conflict this sweep.**
Valuation reads ETH's -63.07% drawdown from ATH, combined with its
intact #2 market-cap rank, as consistent with a mid-cycle position rather
than fundamental deterioration — momentum modestly positive (30d
+8.65%). It explicitly does **not** call this "cheap" (crypto has no
earnings to value against) but frames it as a reasonable cycle position,
and flags Fear & Greed at 28 as arguably too negative relative to recent
price action.

Macro-regime reads the same setup differently: dollar index at 120.69
(unusually strong) combined with Fear & Greed 28 is, in its read, **not**
a contradiction to resolve in ETH's favor — it's confirmation. A strong
dollar is a tightening-of-financial-conditions signal that specifically
punishes crypto, and sentiment agrees rather than overreacting. Macro-regime
explicitly warns against reading "-63% from ATH" as a discount in this
particular regime.

**Neither lens is wrong on its own terms — they're reading the same two
numbers (drawdown + Fear&Greed) through different lenses (cycle position
vs. macro headwind) and reaching opposite implications for whether this is
a moment to add or to stay cautious.** That disagreement is the reason
call #4 above carries Low confidence rather than a directional call.

## Broken theses requiring a decision

None of the five holdings has a thesis that has "broken" in the technical
sense, because **none of the five has a thesis that was ever tested at
all**:

- **HB risky, HB conservative, Avanza ISK holdings:** no ticker, no
  fetched data, no thesis recorded. Structurally blocked, not broken.
- **Swedbank fund:** thesis is explicitly "no active thesis" — an honest
  non-decision (legacy childhood fund), not a failed call.
- **ETH:** this is the one case worth flagging on its own. Real data
  *does* exist for ETH this sweep (price, momentum, sentiment, cycle
  position), but `portfolio.json` records its thesis field as literally
  `"TBD"`. There was never a stated reason for holding it to test against
  the data. This is a distinct, human-side gap — not a data-fetch
  failure — and it should be closed before the next sweep, independent of
  whatever the valuation/macro disagreement above resolves to.

## Rebalancing actions

All target weights are currently `null`, so there is no allocation drift
to close this sweep. The actions below are wrapper/fee-driven structural
fixes, in tax-priority order:

1. **New contributions → Avanza ISK.** No tax event. Uses existing
   headroom. Do this on the next contribution regardless of any other
   open question.
2. **ISK-internal rebalancing:** none specified — `avanza-isk` isn't
   itemized and there are no targets to rebalance toward yet.
3. **Swedbank fund (10,000 SEK, AF) → ISK:** taxable disposal, 30% on
   the gain. Cost basis is unknown (open question #5); **worst-case
   bound is 3,000 SEK** if cost basis were 0. **Do not execute until the
   real cost basis is retrieved from Swedbank** — but at the worst-case
   bound this is still plausibly net-positive against permanent tax-free
   ISK compounding on 10,000 SEK.
4. **ETH (12,500 SEK, self-custody):** no disposal this sweep. Two
   framed options for later, neither actioned:
   - *Sell in wallet:* K4 taxable event, 30% on gain. Worst-case bound
     3,750 SEK if cost basis were 0.
   - *Swap into an ISK-wrapped crypto certificate:* removes future
     per-trade tax, costs ~2%/yr (~250 SEK/yr on current value) plus
     issuer counterparty risk — and still triggers the same disposal tax
     event to get there. Cost basis unknown (open question #4) for
     either path.

## Cost of being wrong

| Headline call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| Deprioritizing HB wrapper resolution | If HB turns out to be taxable with fees at the 1.2–1.6% range noted in `portfolio.json`'s own note (not fetched, not used above), unaddressed drag vs. a ~0.2% index fund ≈ 1.0–1.4% × 134,000 SEK ≈ **1,300–1,900 SEK/year, compounding** | Yes, but every quarter of delay is a real, non-refundable cost |
| Routing contributions to Avanza ISK | Near-zero — ISK is tax-free by construction; worst case is a marginal opportunity cost if HB is later confirmed ISK and preferable, ~**0 SEK** realized loss | Fully reversible next contribution |
| Not yet itemizing Avanza ISK's 36,000 SEK line | If it is a single position and it drops 30%, realized concentration loss ≈ **10,800 SEK** (5.6% of portfolio) | Yes, once itemized and diversified |
| No action on ETH this sweep | If macro-regime's read is right and the dollar stays strong, a further -30% drawdown on 12,500 SEK ≈ **3,750 SEK** (1.9% of portfolio) | Yes — small absolute position |
| Deferring Swedbank AF→ISK move | Doesn't increase tax owed on the existing gain; cost is delayed start of tax-free compounding, order of magnitude **tens of SEK/year** in foregone tax-free growth vs. taxed | Yes, fully recoverable, just delayed |

## Timing collisions

Calendar fetch (45-day window) found no equity earnings collisions — no
equity tickers exist to check. Two macro events fall inside the window:

- **FOMC meeting, 2026-07-28 to 07-29** (statement day 2) — 15–16 days
  out. No rebalancing action in this memo is scheduled to execute before
  then (both the Swedbank and ETH moves are explicitly deferred pending
  missing data), so there is no direct collision. Flag for awareness:
  if either move gets unblocked before 07-29, the regime read (currently
  "Transitional/Divergent" per macro-regime) could shift on the
  statement — re-check macro-regime before executing.
- **Riksbank rate decision + Monetary Policy Report, 2026-08-20** — outside
  any planned action window this sweep.

## Standing task — proposed target allocation (glidepath)

`investor_profile.json` `reference_targets` remain `null`. Per the
standing instruction, this is a **proposal only** — nothing is written to
`portfolio.json` or `investor_profile.json`.

No new data this sweep changes the inputs behind this proposal (goal:
house deposit, 3–7y; max drawdown -30%; contributions 1,000–3,000 SEK/mo).
Two consecutive sweeps (2026-07-06) produced two *different*-shaped
proposals with no data justification for the change — that inconsistency
was flagged in last sweep's reconciliation as a system defect. This memo
**deliberately carries forward the second 2026-07-06 proposal unchanged**
rather than re-deriving a third shape from the same static inputs:

- **Equity: 35–45%**
- **Crypto: 0–5%** (satellite only — ETH is currently at 6.49%, already
  above this ceiling)
- **Fixed income: 30–40%**
- **Cash: 15–25%**

Sized to the short end of the 3–7y range (i.e., closer to the 3y case),
per the profile's own noted tension: a -30% drawdown tolerance is not
recoverable if realized in year 6 of a 3–7y goal, so usable risk should be
budgeted as if the deadline were near, not far, until the range is
narrowed. This framework should now be **stabilized in
`investor_profile.json` rather than re-proposed from scratch** — the user
can adopt it (or a revision) to give future sweeps a fixed reference
point instead of a moving target.

---

**Journal must run next to log this sweep.** An unlogged memo is
invisible to the next session and can never be reconciled against future
data.
