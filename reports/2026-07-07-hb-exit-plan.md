# Handelsbanken AF Exit Plan — 2026-07-07

**Status:** PROPOSED — awaiting user execution. This document analyzes; it executes nothing.
**Horizon:** Long. **Owner levers:** #1 wrapper efficiency, #2 fee drag (the two largest, structural, certain levers).

## What changed today

The blocking question open since 2026-07-03 is resolved: **the Handelsbanken account
(hb-main) is a fondkonto (AF)**, confirmed by the user, with confirmed holdings and fees:

| Fund | Cost basis (anskaffningsvärde) | Market value 2026-07-07 | Unrealized gain | Annual fee (total cost) |
|---|---|---|---|---|
| Handelsbanken Auto 50 Criteria (A1 SEK) | 78,441.28 | 98,492.98 | 20,051.70 | 0.66% |
| Handelsbanken Auto 75 Criteria (A1 SEK) | 27,029.93 | 36,401.26 | 9,371.33 | 0.67% |
| **Total** | **105,471.21** | **134,894.24** | **29,423.03** | ~0.66% blended |

This is ~70% of the total portfolio, and it sits in the worst available wrapper.

## Tax math (30% flat capital gains, AF)

- Tax on full disposal: 30% × 29,423.03 = **8,826.91 SEK**
  (Auto 50: 6,015.51 · Auto 75: 2,811.40)
- Net proceeds: **126,067.33 SEK** — though no tax is withheld at sale; the full
  ~134,894 arrives in cash, and 8,827 is owed with the deklaration the following spring.
- Method: genomsnittsmetoden (average cost). Every partial sale realizes gain
  proportionally (~20.4% of each SEK sold in Auto 50, ~25.7% in Auto 75). **There is no
  "sell the cost basis first" move available.**

## Why sell everything in one step (the tax-optimized answer)

Sweden's 30% capital gains rate is **flat with no annual exemption**, so phasing sales
across calendar years does not reduce total tax by one öre — it only defers part of it.
The embedded 8,827 SEK is owed eventually no matter what. So the real comparison is:

**Cost of accelerating the tax now:** the return the deferred 8,827 SEK would have
earned. At an illustrative 6%/yr (assumption, not data): ~530 SEK/yr.

**Cost of staying in the AF (per year, on ~134,900):**
- Fee drag vs ~0.2% index fund: ~0.46% ≈ **620 SEK/yr**
- Fondskatt (0.4% schablonintäkt × 30% = 0.12%): ≈ **160 SEK/yr**
- 30% tax accruing on all *future* gains (at 6%: ~8,100 SEK/yr gains → ~2,430 SEK/yr
  future tax), vs **zero** inside an ISK under the allowance.

Staying costs roughly **3,200 SEK/yr** against a deferral benefit of ~530 SEK/yr.
There is no breakeven horizon — the single-step exit wins immediately and the gap
compounds. Phasing only makes sense as a behavioral comfort choice, and it should be
labeled as that, not as tax optimization.

## Where the money goes

Avanza ISK. Current ISK balance ~36k; the account notes record ~264k SEK of allowance
headroom. Post-move ISK total ≈ **171k SEK — fully under the allowance**, so ongoing
tax on this capital inside the ISK is zero at current values. This converts a
taxed-forever wrapper into a tax-free one in a single move. (Verify the current
allowance threshold with Skatteverket before execution; the direction of the plan
doesn't change if it shifts, only the magnitude.)

## Steps

1. **Confirm no exit fees** with Handelsbanken (Swedish funds typically have none —
   the 0.66/0.67% is annual, not exit — but confirm before step 2).
2. **Sell both funds in full**, same order round.
3. **Transfer proceeds to Avanza ISK.** Minimize time out of market — days, not weeks.
   Market timing is explicitly not part of this plan; the edge is structural.
4. **Reinvest in a broad, low-fee (~0.2%) index fund** per the Council's target
   allocation. Selection is lever #4 — do not let a perfect-pick search stall the
   wrapper+fee fix. The Auto 50/75 mix implies the current de facto risk level
   (~57% equity blended, name-implied); the Council should confirm the replacement
   allocation against `investor_profile.json`, whose reference targets are still null.
5. **Earmark 8,827 SEK for Skatteverket** (buffer account). It is due with the
   deklaration next spring and is not investable money.
6. **After execution: update `portfolio.json`** — zero out hb-main, itemize the new
   ISK holdings with actual sale/purchase values, mark plan EXECUTED.

## Coordination notes

- **Loss netting:** same-year losses on listed shares/funds offset these fund gains
  100% (aktiefållan). If any listed holding is exiting at a loss anyway, do it in the
  same calendar year.
- **ETH:** crypto losses net at only 70% (K4 section D). Do not sell ETH at a loss
  just to offset these gains — the ETH decision stands on its own. ETH cost basis is
  still an open question.
- **Swedbank AF (~10k):** same wrapper logic applies; once its cost basis is known
  (open question 3), fold it into the same move — the ISK headroom comfortably covers it.

## What would change this plan

- An exit fee or lock-up discovered in step 1 (recompute, direction likely unchanged).
- A confirmed near-term cash need that the buffer can't cover (then proceeds partly
  stay liquid rather than reinvesting — the *sale* logic is unaffected).
- Legislative change to the ISK allowance (recheck magnitude, not direction).

## Data provenance

Holding values, cost bases, and fees: user-provided Handelsbanken statement,
2026-07-07 — not a fetched snapshot. Actual execution values will differ with market
moves. Tax parameters (30% rate, fondskatt formula, average-cost method) are
structural rules, not market data; ISK allowance figure to be verified with
Skatteverket before execution.
