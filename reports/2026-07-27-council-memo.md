# Council Memo — 2026-07-27

This memo is structured synthesis of this system's own four analyst agents
(market-data, valuation, macro-regime, portfolio, thesis-review) — it is not
investment advice from a licensed advisor. Nothing here executes anything;
the user is the human-in-the-loop for every action.

---

## Portfolio health scorecard

Carried over verbatim from the portfolio agent (`/tmp/.../portfolio-2026-07-27.md`).
This is the standing "am I well balanced?" answer and appears every sweep.

| Dimension | Grade | Number behind it |
|---|---|---|
| Asset allocation vs. tier targets (60/30/10) | **WATCH** | Actual: Secure ~161,240 (79.1%), Medium ~3,639 (1.8%), High-risk ~29,003 (14.2%) of 203,754. Medium is dramatically under target only because Q16's ~59,050 SEK migration hasn't started; secure is "overweight" only because that same money sits as undeployed cash, not because of genuine risk-avoidance. |
| Equity sector concentration | **UNKNOWN** | No sector field available — equities fetch is 403'd again; can't grade until it's repaired. |
| Geography | **UNKNOWN** | Same gap — no country field for SHB-A.ST/INVE-A.ST/Auto3/Tundra, and 71% of the base (144,864 SEK cash) has no fund chosen yet, so most of the portfolio's geography is literally undetermined, not just unmeasured. |
| Currency exposure | **WATCH** | ~43,300 SEK (≈19% of the 227,679 grand total) sits in literal non-SEK instruments: PayPal 14,296.72 SEK (USD+EUR cash) + crypto 29,003.12 SEK (USD-denominated BTC/ETH underlying). Revenue-currency exposure inside the funds/stocks is additional and not quantifiable this session. |
| Single-position concentration (cap 15%) | **ACT** | Avanza ISK uninvested cash = 144,864 SEK = **71.1%** of the 203,754 base, over the 15% cap by the letter of the rule. Not market risk (it's cash) — it's a deployment-lag flag, but flagged as instructed. |
| Institution concentration (cap 80%) | **WATCH** | Avanza = 181,254 / 227,678.72 grand total = **79.6%**, just under the cap. On the narrower investable-base view (203,754) it's **88.9%** (would be ACT). Either recommended efficiency fix (Swedbank AF→ISK, PayPal→ISK) pushes it over 80% — see the concentration tension below. |
| Fee drag (cap 0.4%) | **OK aggregate / ACT two holdings** | Total fee drag = 517.09 SEK/yr = **0.254%** of base, under cap. But Tundra (2.6%) and COIN-XBT.ST (2.5%) individually blow past the 0.5% single-fund threshold. |
| Wrapper efficiency | **WATCH** | Clean overall (HB exit fully executed). One residual: Swedbank fund, 10,000 SEK, still in AF with ~118,746 SEK of ISK headroom (vs. ~300k threshold, unverified) unused. |
| Drawdown-tolerance fit (-30%) | **UNKNOWN / qualitative WATCH** | No backtest file found in `data/backtests/` this session — can't produce an actual historical drawdown number. Qualitatively: once the 144,864 SEK cash deploys under near-zero fixed income plus a ~10% crypto sleeve, there is very little true ballast against a -30% profile tolerance. Recommend running `backtest` before next sweep. |

**This scorecard is still partly provisional.** `investor_profile.json`'s exposure-class
`reference_targets` (equity_pct/crypto_pct/fixed_income_pct/cash_pct) are explicitly
superseded and effectively null — the operating control is now the 60/30/10 tier
framework, not those fields. Two profile questions remain genuinely unanswered and
should be named every sweep until resolved: (1) `horizon.primary_goal` — nature of
the property purchase is still explicitly uncertain (apartment vs. Mediterranean
vacation property, SEK vs. EUR liability currency); (2) `horizon.years_until_needed`
— a soft 3-7y range, not a fixed date, which is itself the control variable for when
the glidepath's de-risking schedule should re-engage.

---

## Headline calls

1. **Two decided, tax-free rebalancing actions are 5 days overdue and now sit
   directly in front of tomorrow's FOMC decision.** Tundra full sale (~1,563 SEK)
   and the COIN-XBT.ST trim (3 of 6 units, ~8,251.56 SEK) were both decided
   2026-07-22 and are still unexecuted. The tax math doesn't change with FOMC
   timing; the crypto trim's execution price does.
2. **Valuation and macro-regime read this week's crypto data in opposite
   directions.** Valuation calls ETH's momentum-outpacing-sentiment gap a
   re-accumulation signal. Macro-regime calls the same setup — strong dollar
   (120.53), Fear & Greed at 30, FOMC as a binary catalyst tomorrow — a
   risk-off configuration for exactly this asset class. See "Where the agents
   disagreed" below; this is not resolved by averaging.
3. **154,678.56 SEK is undeployed with no chosen instrument** (144,864 SEK
   existing cash + 9,814.56 SEK in tax-free proceeds from the two pending
   trims above). This is now the single largest open item in the entire
   portfolio, larger than every invested position combined.
4. **ETH's thesis field has been blank for ~10 consecutive sweeps** (since
   2026-07-06) despite fresh data fetched every time. This is a process
   failure, not a market call, and it needs a one-line written answer this
   session — not deferred again.
5. **Proposed target allocation, replacing the stale null glidepath:** 85%
   equity / 5% cash-ballast / ~0% fixed income / 10% crypto (portfolio
   agent's draft, translating the adopted 60/30/10 tier framework into
   exposure-class terms). **This is a proposal only** — it has not been
   written to `portfolio.json` or `investor_profile.json`, and no backtest
   yet confirms it fits the -30% drawdown tolerance.

---

## Open actions (things to go do)

- **SELL Tundra Sustainable Frontier in full** — ~1,563 SEK proceeds (verify
  current price before placing; stale since 2026-07-13). Decided 2026-07-22,
  now 5 days overdue. Tax-free (ISK). Recycle proceeds to the secure tier per
  the adopted profit-recycling rule.
- **TRIM COIN-XBT.ST, sell 3 of 6 units** — ~8,251.56 SEK at the last
  confirmed 2,750.52/unit price (verify before placing; stale 5 days).
  Decided 2026-07-22, now 5 days overdue. Tax-free (ordinary exchange sale
  inside ISK, no issuer redemption fee applies). Execute either before FOMC
  day 1 tomorrow (accept pre-decision volatility) or after the 2026-07-29
  statement (accept a 1-2 day delay for clarity) — either timing is
  acceptable per macro-regime's own read; do not let this slide into a third
  week.
- **Recycle both proceeds (9,814.56 SEK combined) to the secure tier**, per
  the profit-recycling rule already adopted 2026-07-22.
- **Get Swedbank fund's cost basis from Swedbank** (open Q3) — no AF→ISK
  decision can be executed responsibly without it.
- **Confirm PayPal's actual conversion fee schedule** (open Q6) before
  routing the ~14,296.72 SEK balance — do not assume a 3-4% spread.
- **Top up hb-main's residual ~115.28 SEK tax-reserve gap** before 2027
  deklaration prep begins — low priority, already substantially covered by
  the pending 1,750 SEK inflow, no near-term deadline.

## Open decisions (forks — options given, not left bare)

**A. Where should the 154,678.56 SEK undeployed cash go?**
1. Broad low-fee (~0.2%) global index fund inside Avanza ISK — simplest,
   matches the secure-tier definition, but pushes Avanza to ~88-89% of the
   investable base, worsening the institution-concentration flag.
2. Split it — core chunk to a low-fee Avanza global index fund, remainder
   through a second ISK provider — respects the 80% institution cap, adds
   one more account to manage.
3. Phase the deployment over 2-3 sweeps rather than lump-sum, deliberately
   stepping around the FOMC/Riksbank event windows (2026-07-28/29,
   2026-08-20) — lowest tactical-timing risk, slowest to close the gap.

**B. Swedbank fund (10,000 SEK, AF wrapper) — move to ISK or leave?**
1. Get the cost basis (Q3), then move to Avanza ISK — bounded tax 0-3,000
   SEK, fixes a structural wrapper inefficiency, but adds to the Avanza
   concentration problem.
2. Move it to a different ISK provider instead of consolidating into
   Avanza — same tax math, avoids compounding institution concentration.
3. Leave it in AF for now — no tax event, but the inefficiency (≈83 SEK/yr
   forgone ISK efficiency, approximate) persists indefinitely and lever #1
   stays unaddressed for this holding.

**C. COIN-XBT.ST certificate vs. self-custody BTC (open Q13)?**
1. Sell the remaining 3 units in the ISK now (tax-free) and move proceeds
   to self-custody BTC — matches the user's stated "real bitcoin"
   preference, but permanently exits the ISK shelter for that capital;
   every future BTC disposal becomes a 30% K4 event.
2. Stay in the certificate — no per-trade tax ever, but carries the ongoing
   ~206 SEK/yr fee (post-trim) plus CoinShares/XBT Provider issuer-
   counterparty risk (an unsecured note obligation, not BTC held in trust).

**D. ETH thesis — what is the actual view?**
1. Adopt the same cycle-position thesis already recorded for COIN-XBT.ST
   (crypto "pretty low valued," 2028 halving, "positive buy-in signals") —
   consistent, but then ETH should face the same cap-discipline logic that
   just trimmed COIN.
2. State explicitly that ETH is held for diversification only, no active
   market view — removes it from future thesis re-testing, but still needs
   a written rebalance/exit trigger tied to the risk-tier cap.

---

## Where the agents disagreed

**Headline disagreement — crypto, this week.** Valuation reads ETH's
30-day momentum (+24.57%) outrunning its sentiment (Fear & Greed still 30)
as a re-accumulation signal — price recovering faster than sentiment,
"not a reversal." Macro-regime reads the same data alongside a
historically strong dollar (120.53) and an unresolved FOMC decision
tomorrow as precisely the combination that has historically produced
*more* crypto downside, not a bottom confirmation, and explicitly says
"not this week" to leaning further into the bullish thesis. These are not
reconcilable into one number — they are different lenses on the same
data pointing in different directions. **Confidence: Low. Wait for the
FOMC statement (2026-07-29) before treating either read as the operative
one.** The already-decided trim (cap discipline) happens to be
macro-consistent, but that is a coincidence of the cap rule, not
evidence either agent is "right."

**A completeness gap that could be misread as agreement.** Macro-regime
states no macro objection to SHB-A.ST, INVE-A.ST, or Avanza Auto 3 given
a positive 10y-2y spread and moderate VIX. Thesis-review separately
flags that SHB-A.ST and INVE-A.ST have **no recorded thesis at all**
(open Q9, since 2026-07-13) and valuation cannot grade either (data
outage). Read carefully: "no macro objection" is not "thesis confirmed" —
there is no thesis to confirm. Do not let the clean macro read stand in
for due diligence that hasn't happened.

**No disagreement on the overdue-execution items.** Thesis-review and
portfolio both independently classify the Tundra sale and COIN-XBT.ST
trim as pure execution backlog, not open thesis questions — this is
genuine agreement, stated plainly rather than manufactured tension.

---

## Broken theses requiring a decision

Pulled directly from thesis-review, unsoftened:

- **SHB-A.ST (Handelsbanken A), 1 share** — no thesis recorded, open since
  2026-07-13 itemization (open Q9).
- **INVE-A.ST (Investor A), 5 shares** — no thesis recorded, same flag,
  same open question.
- **ethereum (eth-wallet)** — no thesis recorded; thesis field literally
  reads "TBD." Unwritten across ~10 consecutive sweeps (2026-07-06 through
  today) despite fresh data fetched every sweep, flagged repeatedly
  (07-06, 07-07 x2, 07-12, 07-13 x2, 07-20, 07-22) without resolution. This
  is now a chronic process failure, not a one-off gap.
- **Swedbank fund (legacy)** — no active thesis ("no active thesis" is the
  stated text); further blocked from any real re-test by an unknown cost
  basis (open Q3).

---

## Rebalancing actions

Pulled directly from the portfolio agent, SEK amounts as stated:

- **SELL Tundra Sustainable Frontier in full** — ~1,563 SEK proceeds
  (verify, stale since 2026-07-13). Tax: 0 SEK (ISK). Recycle to secure
  tier.
- **TRIM COIN-XBT.ST, 3 of 6 units** — ~8,251.56 SEK proceeds at
  2,750.52/unit (verify, stale 5 days). Tax: 0 SEK (ISK exchange sale).
  Leaves 3 units (~8,251.56 SEK), crypto falls to ~20,751.56 SEK (~10.2%
  of base — at the risk-tier cap). Recycle to secure tier.
- **Combined tax-free proceeds this sweep: 9,814.56 SEK**, joining the
  existing 144,864 SEK cash → **154,678.56 SEK** awaiting secure-tier
  instrument selection.
- **Swedbank fund AF→ISK, 10,000 SEK** — not recommended to execute yet;
  tax bounded 0-3,000 SEK pending cost basis (Q3).
- **PayPal conversion, ~14,296.72 SEK** — routing not finalized; confirm
  fee schedule (Q6) first, and consider a non-Avanza destination given the
  institution-concentration tension.

### Proposed target allocation (proposal only — not written to any file)

| Class | Proposed target | Rationale |
|---|---|---|
| Equity (secure index core ~55pp + medium individual stocks ~30pp) | **85%** | Secure tier is broad equity minus a small ballast; medium tier is 100% equity by definition. |
| Cash / short-duration ballast | **5%** | The small, non-traditional-bond ballast the user asked for. |
| Traditional fixed income | **~0%** | Explicit user override 2026-07-22: equity above 70% is fine. |
| Crypto | **10%** | Matches the adopted high-risk tier cap. |

This is materially more aggressive than the original 50/40/5/5 glidepath
and only holds while the property goal stays soft. It has **not** been
written to `portfolio.json` or `investor_profile.json`. No backtest
exists to confirm it respects the -30% drawdown tolerance — treat as
unresolved, not confirmed-fine.

---

## Confidence and horizon per headline call

| Call | Confidence | Horizon |
|---|---|---|
| Execute Tundra sale now | High | Medium (rebalancing serving a long-horizon fee fix) |
| Execute COIN-XBT.ST trim (timing flexible around FOMC) | Medium | Medium (cap-discipline rebalancing; execution price is short-term FOMC-sensitive, the decision itself is not a tactical bet) |
| Hold off adding new crypto money until FOMC clarity | Low | Short (<6mo) — tactical by definition, capped, never High confidence |
| Deploy the 154,678.56 SEK secure-tier cash | Medium | Long (3y+) — structural allocation |
| Adopt the proposed 85/5/0/10 target | Low-Medium | Long (3y+), contingent on the goal staying soft |
| Write the ETH thesis this session | High (process fix, not a market call) | N/A |

---

## Cost of being wrong

| Headline call | If wrong | Downside (SEK) | Recoverable? |
|---|---|---|---|
| Execute Tundra sale now vs. wait | Stale 5-day price differs materially from execution price | Bounded by position size, max ~1,563 SEK | Yes — trivial size, ISK, no tax event either way |
| Execute COIN trim now vs. after FOMC | Crypto swings sharply on the FOMC print before/after execution | Position at stake ~8,251.56 SEK; a 15% adverse swing ≈ 1,200 SEK | Yes — cap-discipline trim, not a directional bet; residual 3 units exposed regardless of timing |
| Hold off adding new crypto vs. lean into the bullish thesis now | BTC/ETH rallies through FOMC week while sidelined | Opportunity cost only, sized to whatever new money would have been added | N/A — no capital put at risk by waiting |
| Deploy 154,678.56 SEK lump-sum vs. phased | Adverse market move right after a lump-sum entry into FOMC-week turbulence | Full 154,678.56 SEK exposed; a 10% adverse move ≈ 15,468 SEK | Yes, long horizon, recoverable over the 3-7y soft window |
| Adopt the proposed 85/5/0/10 target now | Property goal firms up earlier than the 3-7y soft range while the book is still 85% equity/10% crypto | Bounded by the stated -30% tolerance, up to roughly 65,000-68,000 SEK on a ~215-227k SEK base | Not cleanly recoverable if forced to sell near a trough to fund a firm deadline — this is the real risk in adopting the proposal now |

---

## Timing collisions

- **FOMC 2026-07-28/29** (tomorrow, day after) collides directly with the
  overdue COIN-XBT.ST trim execution and with any decision to add new
  crypto exposure — flagged by macro-regime, carried here.
- **Riksbank rate decision 2026-08-20** — no collision with any action
  decided this sweep, but directly relevant to Swedish-equity medium-tier
  buys (SHB-A.ST, INVE-A.ST candidates); flag for whichever sweep lands
  closest to that date.
- **Equities earnings calendar fetch also failed today** (403, same
  outage as the price fetch) — no fresh earnings dates for SHB-A.ST,
  INVE-A.ST, or COIN-XBT.ST this sweep. This is a data gap, not a clean
  "no collision": an earnings-date collision with any of these three
  cannot be ruled out until the fetch is repaired.

---

**Reminder: journal must run next.** This memo is not logged anywhere
until `journal` appends the session entry to `reports/SESSION_LOG.md` —
an unlogged sweep is invisible to the next session and cannot be
reconciled against future data.
