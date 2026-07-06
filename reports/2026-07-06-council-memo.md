# Finance Council Decision Memo — 2026-07-06

*This memo is not investment advice from a licensed advisor. It is structured
synthesis of this session's own agent outputs (valuation, macro-regime,
portfolio, thesis-review) — nothing here executes anything.*

---

## Open blocking question (per CLAUDE.md — must open here)

**Question 1 (open_structural_questions, portfolio.json): is the
Handelsbanken account (hb-main, 134,000 SEK, 69.6% of the portfolio) an ISK
or a fondkonto?**

This is unresolved. Until it is answered, no allocation conclusion, no
drift number, no tax conclusion, and no rebalancing action touching
hb-main is trustworthy — 70% of the portfolio is riding on an unknown. If
it is a fondkonto, portfolio.json's own note calls it "the largest
structural inefficiency in the portfolio" (30% tax on gains, plus likely
1.2–1.6% fund fees). If it is an ISK, none of that applies. This is the
single highest-value open item in the whole system and outranks every
other call below. Answer this before anything else.

---

## Portfolio health scorecard (carried over verbatim from portfolio agent)

Provisional — `investor_profile.json` reference_targets are still null, so
several rows below are UNKNOWN because there is nothing to grade against
yet, not because the portfolio is confirmed fine.

| Dimension | Grade | Note |
|---|---|---|
| Asset allocation vs profile targets | UNKNOWN | targets null in both files |
| Equity sector concentration | UNKNOWN | no sector data, equities snapshot empty |
| Geography / home bias | UNKNOWN | no country field |
| Currency exposure | UNKNOWN | no revenue-currency data for 93.5% of portfolio |
| Single-position concentration | UNKNOWN / partial | only Swedbank fund (5.2%, OK) and ETH (6.5%, OK) gradable; Avanza ISK aggregate shows 18.7% but is a non-itemization artifact, not a confirmed breach; hb-main's internal split unknown (open Q3) |
| Institution concentration | OK, with caveat | Handelsbanken 69.6% of total, below the 80% threshold — but this is a size fact only; it says nothing about the account's tax status, which is the open blocking question above |
| Fee drag | UNKNOWN | fee data known for only 1 of 5 holdings (ETH = 0%); 180,000 SEK / 93.5% ungraded against the 0.4% max ceiling; graded UNKNOWN not OK because bank-managed portfolios are the category most likely to breach it |
| Wrapper efficiency | **ACT** | Swedbank fund (10,000 SEK) sits in confirmed-taxable AF with ~264,000 SEK of unused ISK headroom; separately, hb-main wrapper status is the open blocking question above |
| Drawdown-tolerance fit | UNKNOWN | no backtest run this sweep against the stated -30% tolerance |

Unanswered questions driving the UNKNOWNs above: `reference_targets` in
`investor_profile.json` (all null), hb-main wrapper type (Q1), hb-main
equity/bond split (Q3), fee data for 4 of 5 holdings, cost basis for the
Swedbank fund (Q5) and for ETH (Q4).

---

## Headline calls

1. **Resolve the Handelsbanken wrapper before any other portfolio
   decision.** This blocks 69.6% of the book. No workaround exists — it
   requires contacting Handelsbanken or checking the account statement,
   not more analysis.
2. **Route new contributions to Avanza ISK, not AF or hb-main.** Confirmed
   clean wrapper, ~264,000 SEK of headroom, no tax event. This is a
   default forced by data gaps (nowhere else is confirmed-clean), not a
   drift-closing calculation — there is no target to close drift against
   yet.
3. **Get real cost basis for the Swedbank fund (Q5) before moving it to
   ISK.** Tax on disposal is bounded between ~0 SEK (if cost basis ≈
   value) and ≤3,000 SEK (worst case, cost basis → 0, on a 10,000 SEK
   position) — small in absolute terms either way, but not a real number
   without the basis.
4. **Do not act on ETH this sweep.** Valuation reads it as fair-to-cheap
   on cycle position; macro-regime reads the current regime as hostile to
   exactly this asset; thesis-review finds no documented thesis for it at
   all. Three lenses, three different answers, zero basis to net them into
   a single call today. See disagreement section below.
5. **Write an actual ETH thesis now, while the setup is legible** (per
   thesis-review) — price up double digits over 7d/30d while Fear & Greed
   reads 24/Extreme Fear is an unusual, nameable divergence. This is a
   documentation action, not a trade.

---

## Where the agents disagreed

**ETH: valuation vs macro-regime vs thesis-review — a real three-way
split, not noise.**

- *Valuation* calls ETH fair-to-cheap, but explicitly on cycle-position
  signal only (distance from ATH -64.05%, momentum +10.35% 7d / +11.51%
  30d) — it says outright this is not a valuation call, since crypto has
  no earnings/cash-flow anchor. It flags the Fear & Greed 24 / rising
  price divergence as worth attention, not as "buy the fear."
- *Macro-regime* calls the current regime "transitional, tilted risk-off
  for dollar-sensitive assets," driven by DXY at 120.89 (extreme
  strength, well above the 90–110 historical range) and a yield curve
  that just un-inverted (+0.31 spread, still inside the late-cycle
  stress window, not an all-clear). It explicitly flags ETH (~6.5% of
  portfolio) as sitting on the wrong side of this regime, and states
  directly: "cheap and in extreme fear during a strong-dollar regime is
  not the same as regime-supportive" — a direct rebuttal aimed at any
  "buy the dip" reading of the valuation output above.
- *Thesis-review* finds no thesis exists for ETH to test either framing
  against. There is real data (price, drawdown, sentiment, momentum) but
  no documented view on what ETH is for in this portfolio or what would
  change the holder's mind — so "cheap" and "hostile regime" are both
  floating without a claim to attach to.

Net: the cycle-position signal says maybe-cheap, the regime signal says
headwind, and there is no written thesis to arbitrate between them.
**Confidence: Low. No action on ETH sizing this sweep; wait for regime
clarity (VIX at 16.59 has not yet caught up to what crypto sentiment is
already pricing at Extreme Fear — that cross-asset gap could resolve
either direction) and write the missing thesis in the meantime.**

**Institution concentration "OK" vs wrapper-unknown — a clean number is
not a clean bill of health.** Portfolio agent grades Handelsbanken
institution concentration OK (69.6%, under the 80% threshold). That
number is real, but it answers a different question than "is this
account safe to hold as-is." A concentration grade cannot substitute for
the wrapper answer — an OK-concentration, unknown-tax-status account is
still a blocking issue, and this memo treats it as one (see blocking
question above), not as a clean row that happens to sit next to an
unrelated open item.

**Everywhere else, agreement is not real agreement — it is absence of
data.** Valuation, macro-regime, and thesis-review all return
"insufficient data" / "unscoreable" / "broken by absence" for the
Handelsbanken funds and the Avanza ISK holdings. That is not four lenses
converging on a view — it is four lenses independently confirming the
same missing tickers. Do not read that as "the rest of the portfolio
looks fine."

---

## Broken theses requiring a decision (unsoftened, from thesis-review)

- **Handelsbanken risky fund, Handelsbanken conservative fund, Avanza ISK
  holdings (3 of 5 holdings):** Broken, by absence. No thesis recorded
  (the thesis field is an unfilled instruction, not a claim), and no
  ticker recorded either, so there is no fundamental basis to check even
  if a thesis existed. Fix is populating `portfolio.json` (ticker,
  thesis) — not a re-test, there is nothing yet to re-test.
- **Swedbank fund:** Broken, by absence — but explicit. The thesis field
  honestly states "no active thesis." This is correctly a decision
  holding (keep vs. move to ISK), not a conviction holding, and should
  not be scored as if it were failing a live investment case.
- **ETH:** No thesis recorded, so status cannot even be classified as
  "broken" — there is nothing to break. But real, current data exists
  (price €1,520.44, -64.05% from ATH, +10.35%/7d, +11.51%/30d, Fear &
  Greed 24) that a thesis, once written, would immediately have to
  contend with. Action: write it now.

Thesis-review's own count stands: **4 of 5 holdings are broken-by-absence.**
Not softened to "worth monitoring" here either.

---

## Rebalancing actions (from portfolio agent, tax-priority order, SEK amounts)

**(a) New contributions (1,000–3,000 SEK/mo):** direct to Avanza ISK.
Confirmed clean wrapper, ~264,000 SEK of headroom, no tax event. This is
the only unambiguous no-regret action in this memo — it does not require
the wrapper question or the reference targets to be resolved first.

**(b) ISK/KF sales:** none indicated. No confirmed target allocation
exists to close drift against.

**(c) AF sale — Swedbank fund, 10,000 SEK, move to ISK:** tax on
disposal = 30% × (value − cost basis). Cost basis is null (Q5), so the
exact figure is not computable. Bound: worst case (cost basis → 0) tax ≤
3,000 SEK; best case (cost basis ≈ value) tax ≈ 0 SEK. Portfolio.json's
own note suggests a low cost basis / high gain%, but the absolute tax is
small given the position size regardless — likely outweighed by moving
into a tax-free wrapper, but get the real cost basis from Swedbank before
executing.

**(d) ETH (self-custody, 12,500 SEK):** no adjustment proposed this
sweep. Cost basis is null (Q4) and there is no confirmed target crypto
weight to size against. Framework only: a wallet sale today triggers 30%
× (value − cost basis), unknown amount. A certificate-in-ISK move is
**not** tax-neutral either — it requires disposing of the wallet ETH
first (a K4 event now), plus an ongoing certificate fee (~2%/yr reference
point, unverified TER) plus issuer/counterparty risk, versus the wallet's
0% running fee but fully taxable future disposals. Get ETH cost basis
before this comparison is real.

---

## Proposed target allocation (PROPOSAL ONLY — not written to any file this sweep)

Portfolio agent produced an illustrative target this session, driven by
the profile's 3–7 year house-deposit window and its own noted tension
that the stated -30% drawdown tolerance is a "now" number that must
shrink as the deadline approaches:

| Bucket | Illustrative range |
|---|---|
| Equity | 35–45% |
| Crypto (satellite) | 0–5% |
| Fixed income | 30–40% |
| Cash (deposit-specific, separate from emergency buffer) | 15–25% |

Recommended sizing point: the **short end** of the 3–7y range now, with
re-risking upward only if the deposit timeline is later confirmed
longer — not the reverse. Glidepath: reduce equity+crypto / increase cash
and short-duration starting no later than ~24 months before the actual
purchase date, reaching near-100% cash/short-duration by T-minus 6–12
months.

This is a proposal to consider adopting into `investor_profile.json`, not
a drift calculation against the current book — it cannot be made precise
today because the equity/bond split inside the 74.8% "mixed" hb-main
bucket is unknown (Q3). **Nothing has been written to `portfolio.json` or
`investor_profile.json` this sweep.**

---

## Confidence level per call

| Call | Confidence | Why |
|---|---|---|
| Resolve hb-main wrapper before other decisions | High | Not a judgment call — a fact-finding action with a single unambiguous next step |
| Route new contributions to Avanza ISK | High | Confirmed wrapper, confirmed headroom, no tax event, no dependency on unresolved data |
| Get Swedbank cost basis before AF→ISK move | Medium | Direction (favor ISK) is likely right; exact tax cost unknown, so "execute now" is not yet supported |
| No action on ETH sizing this sweep | Low | Valuation, macro-regime, and thesis-review point three different directions; genuinely regime-dependent, could flip on the next DXY or VIX print |
| Write an ETH thesis now | Medium | Documentation action, not a market call — "medium" because acquisition-date/cost-basis data is still missing, so the thesis can't be fully grounded yet |
| Proposed target allocation (glidepath) | Low | Cannot be verified against the current book while hb-main's internal split (Q3) and profile reference_targets are both unknown |

---

## Horizon tag per call

| Call | Horizon | Note |
|---|---|---|
| Resolve hb-main wrapper | Long (3y+) | Structural, owned by portfolio agent per CLAUDE.md priority order |
| Route contributions to ISK | Long (3y+) | Wrapper/fee-drag category, highest edge per CLAUDE.md |
| Swedbank AF→ISK move | Long (3y+) | Structural wrapper efficiency, not a timing trade |
| ETH sizing decision | Medium (6mo–3y) | Regime-positioning call, owned jointly by valuation/macro-regime/thesis-review; explicitly not short-term tactical, and given the three-way disagreement it cannot be High confidence regardless of horizon |
| Write ETH thesis | N/A (documentation, not a market call) | — |
| Proposed glidepath allocation | Long (3y+), with a Medium-horizon trigger point | The glidepath is a long-horizon structural plan, but its trigger (T-minus 24 months from a 3–7y-out deposit) falls inside the medium-horizon band and needs the deposit date narrowed before it can be actioned |

No call in this memo carries a Short-horizon tag. No tactical overlay is
proposed this sweep, so the 10%-of-portfolio cap / never-High-confidence
rule for Short-horizon calls does not currently apply to anything above.

---

## Cost of being wrong

| Headline call | If wrong, realistic downside (SEK) | Recoverable? |
|---|---|---|
| hb-main assumed ISK (or left unresolved) when it is actually a fondkonto | Full 134,000 SEK exposed to 30% tax on unrealized gains at eventual disposal, plus ongoing 1.2–1.6% fund fees vs ~0.2% index compounding over years | Fee drag: recoverable by switching. Tax on gains already accrued in the wrong wrapper: not recoverable once realized |
| Contributions routed to Avanza ISK instead of held pending target clarity | Opportunity-cost only — 1,000–3,000 SEK/month exposed to Avanza ISK's current (unitemized) holdings rather than a confirmed target mix | Fully recoverable — future contributions can be redirected any month, no lock-in |
| Swedbank fund moved to ISK before confirming cost basis, tax lands at the ≤3,000 SEK worst-case bound | Up to ~3,000 SEK one-time tax cost on a 10,000 SEK position | Recoverable — bounded, small in absolute terms, and avoidable entirely by checking basis first |
| ETH treated as "cheap, buy the dip" per valuation's cycle-position framing while macro-regime's risk-off flag is live | Full 12,500 SEK (6.5% of portfolio) exposed to further downside if the strong-dollar/risk-off regime persists or deepens; no thesis exists to define a stop or a re-entry rule | Recoverable in that 12,500 SEK is a small absolute amount, but there is currently no documented exit rule, so a bad entry has no defined unwind point |
| Proposed glidepath allocation adopted now, before hb-main's equity/bond split (Q3) is known | Portfolio could be unknowingly under- or over-risked relative to the proposed 35–45% equity target, since 74.8% of the book's actual composition is unverified | Recoverable — a targeting/labeling error, not a realized loss, correctable the moment Q3 is answered |

---

## Timing collisions

Calendar agent flagged two macro events inside the 45-day lookahead:
**FOMC meeting 2026-07-28/29** and **Riksbank rate decision
2026-08-20.** No rebalancing action in this memo is being executed this
sweep, so no action lands near either date — but both dates are directly
relevant to the one live regime-dependent call above (ETH / risk-off
positioning): a Fed decision in three weeks and a Riksbank decision in
six weeks are both plausible triggers for the "next macro print" that
could move that call out of Low confidence in either direction. No
equity earnings collisions to report — there are no itemized equity
tickers yet to check against.

---

**Full agreement check:** the four agents do not agree cleanly on
anything this sweep that matters. Where they appear to agree — 4 of 5
holdings return "insufficient data" / "unscoreable" / "broken by
absence" — it is because the same tickers are missing from
`portfolio.json` across every lens, not because the lenses converged on
a view. That is treated above as a data gap, not a clean bill of health.
