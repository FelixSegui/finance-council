# Council Memo — 2026-07-06

This is structured synthesis of this system's own agent outputs, not advice from a
licensed advisor. It exists to force disagreements into the open and attach a
confidence/horizon tag to every call — it does not execute anything.

---

## Open first: Handelsbanken wrapper (blocking question #1)

Per CLAUDE.md's blocking-questions rule, this must open every memo while
unresolved, and it is still unresolved. **134,000 SEK — 69.6% of the entire
portfolio — sits in a Handelsbanken wrapper of unknown type.** If it is
ISK/KF, tax-sheltered capital is up to ~170,000 SEK. If it is fondkonto/depa,
confirmed tax-sheltered capital stays at 36,000 SEK (Avanza only). That is a
swing of over 100,000 SEK on a single unanswered question, and it makes
every allocation, tax, and rebalancing conclusion touching that account
untrustworthy until answered. Action: ask Handelsbanken directly, or check
whether any sale in that account has ever generated capital-gains tax in a
prior deklaration. This is not new this week — it is the standing #1 item
in `portfolio.json`'s `open_structural_questions` and nothing this week
resolves it.

## Operational fact this week: total data outage

The market-data fetch (`data/snapshots/20260706T121553.json`) failed
completely — every field (equities, crypto, macro, sentiment) returned 403
errors. This was diagnosed as an **organization-level network egress
policy** blocking Yahoo Finance/yfinance, CoinGecko, FRED, Riksbank SWEA,
ECB Data Portal, SCB PxWeb, and alternative.me simultaneously — not a
per-ticker or data-quality issue, and not fixable by retrying inside this
session. Valuation, macro-regime, and thesis-review all returned "no data"
as a direct result. This is an environment configuration problem: these
six domains need to be allowlisted for this environment before next week's
sweep can produce a real valuation, regime, or thesis read. Until that is
fixed, this system is running on one leg — the structural/portfolio lens,
which uses only user-maintained figures and does not depend on external
fetches.

---

## Portfolio health scorecard

Carried over verbatim from the portfolio agent. **Provisional** — four of
eight rows are UNKNOWN because `investor_profile.json`'s `reference_targets`
(equity_pct, crypto_pct, fixed_income_pct, cash_pct) are still null and
`portfolio.json` holdings carry placeholder "TBD" tickers instead of
itemized positions. Unanswered questions driving the UNKNOWNs: the 5 items
in `open_structural_questions` (HB wrapper, HB fees, HB equity/bond split,
ETH cost basis/dates, Swedbank cost basis) plus the unset `reference_targets`.

- **Asset allocation vs profile targets:** UNKNOWN (targets null; 88% of
  portfolio has no verified equity/bond split)
- **Equity sector concentration:** UNKNOWN (no sector data — fetch failed,
  Avanza ISK unitemized)
- **Geography (home bias):** UNKNOWN (no country data)
- **Currency exposure:** UNKNOWN (no per-holding currency data; even
  sek_per_usd errored)
- **Single-position concentration: ACT** — confirmed math, not a guess:
  the two Handelsbanken sub-portfolios sum to 134,000 SEK; 15% of total =
  28,875 SEK; for both to be ≤28,875 SEK their sum would need to be
  ≤57,750 SEK, but it's 134,000 SEK — at least one HB sub-portfolio MUST
  exceed the 15% max-single-position threshold regardless of the actual
  split. Only which one (or both) needs itemization.
- **Institution concentration: WATCH** — Handelsbanken = 69.6% of total,
  below the 80% ceiling but the largest counterparty concentration in the
  file, compounded by the wrapper being unconfirmed.
- **Fee drag:** UNKNOWN — `annual_fee_pct` null on every holding except
  ETH (0%); cannot compute SEK/year drag; declining to substitute a
  "typical" bank-fund rate.
- **Wrapper efficiency: ACT** — HB wrapper (134,000 SEK, 70% of portfolio)
  still unconfirmed, the single largest open item in the system.
  Separately, confirmed-AF Swedbank fund (10,000 SEK) sits taxable while
  ISK headroom exists.
- **Drawdown-tolerance fit:** UNKNOWN — no backtest file available this
  session to compare against the -30% max drawdown tolerance.

---

## Headline calls

All headline calls this week are structural/**Long horizon** — the
Medium-horizon lenses (valuation, thesis health, regime positioning) could
not run at all this week, so there is nothing at that horizon to call.

1. **Resolve the HB wrapper before any further contribution or
   rebalancing decision touching that account.** Long horizon. Confidence:
   High that this is the top-priority action (the >100k SEK swing is
   confirmed math); confidence in what the answer will turn out to be:
   none — that's the point of asking.
2. **Treat the single-position ACT flag as real, not hypothetical.**
   At least one Handelsbanken sub-portfolio already breaches the 15%
   max-single-position threshold by confirmed arithmetic, independent of
   any itemization. Long horizon. Confidence: High (math, not modeling).
3. **Institution concentration at Handelsbanken (69.6%) stays on WATCH,
   not ACT** — under the 80% ceiling, but the largest single-counterparty
   exposure in the portfolio, and it compounds the wrapper question rather
   than being independent of it. Long horizon. Confidence: Medium (the
   69.6% figure is solid; whether it deserves escalation to ACT depends on
   the wrapper answer).
4. **ETH's actual weight (6.5% of portfolio, 12,500/192,500 SEK) already
   exceeds the proposed default glidepath crypto ceiling** under the
   current-default phase (see proposed glidepath below, 0-3% given the
   unresolved 3-7y horizon). Long horizon (allocation policy), though the
   underlying asset is volatile. Confidence: Medium — the percentage is
   simple arithmetic on user-maintained figures, not a live price; the
   ceiling itself is a proposal pending horizon narrowing.
5. **Swedbank AF→ISK move remains correctly deferred, not decided.** The
   fund (10,000 SEK) sits taxable while ISK headroom exists, but cost
   basis is unknown, so the one-time tax cost of realizing the gain can't
   be sized against the permanent benefit of tax-free compounding. Long
   horizon. Confidence: Low to act this week (missing input), High that
   the missing input — cost basis — is the actual blocker.

## Where the agents disagreed

There is no ordinary fundamentals disagreement to report this week, and
manufacturing one would be worse than admitting there isn't one:
valuation, macro-regime, and thesis-review all independently returned "no
data" for the same reason (the network egress failure), so there is
nothing for them to disagree about on direction, pricing, or thesis
health.

The real tension this week is structural, not fundamental: **the portfolio
lens's concentration and wrapper math stands on its own, fully computed
from user-maintained `approx_value_sek` figures, with zero dependency on
the failed fetch — while every other lens is completely dark.** That is
not "the agents agree" and it is not "the agents disagree" — it is that
one lens (portfolio) had inputs that didn't require live data and the
other three didn't. Do not read the silence from valuation/macro/thesis as
implicit confirmation that "everything looks fine" on those fronts. The
macro-regime agent was explicit on this point: every regime-dependent read
this sweep — ETH (~12,500 SEK), Avanza ISK equity (~36,000 SEK),
Handelsbanken mixed portfolios (~134,000 SEK) — carries **zero macro
confirmation**, and any bullish/bearish framing on these assets from
elsewhere this week is unconfirmed by rates or dollar data. There is
nothing to frame bullishly or bearishly from this sweep's other lenses in
any case, since they returned no output — but the caveat is recorded so it
isn't silently dropped next week when data returns and framing resumes.

## Broken theses requiring a decision

Pulled straight from thesis-review, unsoftened. **All 5 holdings fail
thesis-review this week**, for two distinct, compounding reasons that
should not be blurred together:

1. **Pre-existing structural gap, independent of this week's outage:** 4
   of 5 holdings have no thesis recorded at all — Handelsbanken risky
   (thesis = "TBD"), Handelsbanken conservative (thesis = "TBD"), Avanza
   ISK holdings (thesis field is a placeholder instruction, not itemized
   per-holding), ETH (thesis = "TBD"). The Swedbank fund is the exception:
   its thesis explicitly states "Legacy childhood savings - no active
   thesis" — an honest recorded absence of conviction, still functionally
   "no thesis to test."
2. **This week's total data outage:** even where a thesis existed, no
   holding's fundamentals could be re-tested this week — no
   Intact/Weakening/Broken/Played-out status can be honestly assigned to
   anyone this week.

Decision required, not a data problem: write an actual thesis (even if it's
"my bank put me in it" for the HB accounts, or itemize Avanza ISK holding
by holding) so that thesis-review has something to test once data access
is restored. This is a one-time input cost, not something waiting on the
network fix.

## Rebalancing actions

Pulled straight from the portfolio agent, with SEK amounts. **None
computed this week** — no targets exist anywhere: `portfolio.json`'s
`targets` block and `investor_profile.json`'s `reference_targets` are both
null (target-setting was deliberately deferred to this Council sweep, see
proposed glidepath below), and 88% of portfolio value has no verified
exposure breakdown to rebalance against in any case. The one live wrapper
decision in the file (Swedbank AF→ISK) cannot be sized without cost basis.
**The single actionable lever right now is the recurring monthly
contribution (1,000-3,000 SEK), tax-neutral wherever it lands** — it does
not require the wrapper question resolved and does not require live
prices.

---

## Proposed target allocation (glidepath) — PROPOSAL ONLY

This section is a **proposal for consideration**, not a fetched-data-backed
number, and it has **not** been written to `portfolio.json` or
`investor_profile.json`. It is pure policy/planning reasoning applied to
the user's own stated facts in `investor_profile.json` — no market data
claim is made here. Per CLAUDE.md's scope rule, individual bonds/options/
alts stay out of scope even in this proposal: "fixed income/cash" below
means cash and cash-like vehicles the user would select themselves, not a
specific bond product recommendation.

**Governing facts:** goal is a house deposit needed in 3-7 years (a range,
not a fixed date); stated max drawdown tolerance is -30% (~57,750 SEK at
current 192,500 SEK size); the profile's own recorded tension is that this
-30% tolerance applies **now**, not in year 5+, because a hard-deadline
goal means usable risk shrinks as the date approaches; monthly
contributions of 1,000-3,000 SEK continue; the 3-6mo emergency buffer is
confirmed separate from this portfolio, so the portfolio's risk budget is
genuine, not partly a safety net.

Standard goal-based glidepath convention applies: taper growth assets as
the deadline nears, and because the deadline is an uncertain range, treat
the **short end (3 years)** as the effective planning deadline until
narrowed — being wrong short (running out of recovery time before a
forced withdrawal) is worse than being wrong long (holding a bit too
conservative for a few extra years).

| Phase | When it applies | Equity | Crypto | Cash/cash-like |
|---|---|---|---|---|
| 1 — Growth | Only once the range is narrowed toward the long end (e.g., confirmed 6-7y out) | 55-70% | 0-5% | 25-40% |
| 2 — Mid-approach (**current default, given the unresolved range**) | 2-4y out, and where this portfolio should sit today because 3 years cannot be ruled out | 35-50% | 0-3% | 50-65% |
| 3 — Final approach | Final 12 months before the deposit is needed | 0-15% | 0% | 85-100% |

Because the 3-7y range has not been narrowed, this portfolio cannot be run
as if Phase 1 applies — 3 years remains possible, so Phase 2 is the
correct current default until told otherwise. Under that default, ETH's
current 6.5% weight already sits above the 0-3% crypto ceiling (see
headline call #4).

**Explicit recommendation:** narrow the 3-7y range to a firmer number.
This single fact changes which phase this portfolio should sit in — and
therefore the growth/cash split on 192,500 SEK plus every future monthly
contribution — more than any other input available this sweep.

---

## Confidence and horizon per call

| Call | Confidence | Horizon |
|---|---|---|
| Resolve HB wrapper | High (that it's top priority) | Long |
| Single-position ACT (≥1 HB sub-portfolio >15%) | High (confirmed math) | Long |
| Institution concentration WATCH (HB 69.6%) | Medium | Long |
| ETH overweight vs. proposed default ceiling | Medium | Long |
| Swedbank AF→ISK move | Low (blocked on cost basis) | Long |
| Proposed glidepath phase assignment | Medium (policy logic solid; phase depends on unresolved horizon) | Long |
| Any valuation/regime/thesis read | N/A — no data this week | Medium (would be, once restored) |

Per CLAUDE.md's horizon policy, no Short-horizon (<6mo) tactical call is
made this week — there is no live pricing to support one, and the free-data
system carries no demonstrated short-term edge in any week, let alone one
with zero data.

## Cost of being wrong

One row per headline call with a stateable SEK downside. Calls without a
stateable downside are not included, per this memo's own rule.

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| HB wrapper turns out to be fondkonto (taxable), acted on late | Ongoing fee drag ~1.2-1.6%/yr on 134,000 SEK ≈ 1,600-2,150 SEK/yr vs. an ISK-typical index fee, plus 30% tax on any unrealized gain if ever sold outside ISK (magnitude unknown, no cost basis — likely the largest single line item in the portfolio) | Fee drag: yes, by switching. Tax on past gains inside the wrong wrapper: no, that's sunk once realized |
| Single-position ACT flag ignored (no itemization, no trim) | Up to 134,000 SEK (69.6% of portfolio) concentrated in one bank-managed strategy if the split turns out lopsided, vs. a 28,875 SEK (15%) ceiling | Yes, once itemized — but any move inside HB may itself trigger tax if the wrapper turns out to be AF/fondkonto |
| Institution concentration (69.6% at HB) not diversified | Single-institution operational/counterparty risk on 134,000 SEK if something goes wrong at the institution level (not a market-return scenario) | Only by diversifying future flows elsewhere — existing balance can't be un-concentrated without a wrapper-aware move |
| ETH left at 6.5% against a 0-3% proposed ceiling | Excess crypto exposure of roughly 6,750-12,500 SEK depending on which ceiling applies; at -50% to -80% drawdown scenarios historically seen in this asset class, that's an incremental 3,400-10,000 SEK of portfolio-level downside beyond what the proposed policy intends | Yes — reversible by trimming, but only after a taxable K4 disposal event (30% on any gain) |
| Swedbank AF→ISK move deferred another week | Continued 30% tax drag on this fund's future gains vs. 0% in ISK; base is only 10,000 SEK so absolute SEK at stake is small this week | Yes, fully — small position, no urgency cost |
| No rebalancing targets exist; monthly 1,000-3,000 SEK contributions land un-targeted | Over a year, 12,000-36,000 SEK of new money could land in an unintended exposure (e.g., adding to an already-overweight HB sub-portfolio) | Yes — flow-based, easy to redirect once targets and itemization exist |

## Timing collisions

No contemplated rebalancing action exists this week (none was computed —
see Rebalancing actions above), so there is nothing to collide with the
upcoming macro calendar. Stated explicitly per this memo's own rule against
flagging a false collision. For reference, the next macro prints are:
**2026-07-28/29 FOMC meeting** and **2026-08-20 Riksbank rate decision +
Monetary Policy Report**. The FOMC dates are flagged in
`data/macro_calendar.json` as "written from model knowledge — one-time
verification pending" (IMPROVEMENTS #2) — treat those two dates as
provisional until verified against the Fed's published calendar, and
re-check before scheduling any future action near them.

---

**Journal must run next.** This memo is not logged until `journal` appends
this sweep to `reports/SESSION_LOG.md` — an unlogged memo is invisible to
the next session and can never be reconciled against future data.
