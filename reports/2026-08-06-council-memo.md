# Council Memo — 2026-08-06

*Structured synthesis of your own agents' analysis. Not advice from a
licensed advisor. Nothing here executes; you decide and you place every
trade.*

Snapshot: `20260806T130256.json` (previous `20260804T160037.json`).
First Council memo since 2026-08-03 — the 08-04 and 08-05/06 sessions did
system work (Excel pipeline, model tiering, Council-method restore) without
a memo. Reconciliation of 08-03's calls is at the bottom of section 1.

---

## 1. Position report

| Position | Price | Δ vs prev | Δ vs cost | 52w range | Value (SEK) | Source |
| Handelsbanken A | 147.70 | +0.6% | +14.3% | 94% | 147.70 | fetched |
| Investor A | 415.80 | +1.6% | +43.3% | 98% | 2,079.00 | fetched |
| Volvo B | 366.40 | -0.8% | -0.3% | 96% | 4,763.20 | fetched |
| Atlas Copco B | 184.00 | +3.9% | +1.5% | 99% | 4,968.00 | fetched |
| AstraZeneca | 1,545.50 | +4.9% | +2.6% | 32% | 6,182.00 | fetched |
| Alfa Laval | 567.40 | +0.1% | -1.2% | 86% | 5,106.60 | fetched |
| ABB | 969.00 | +2.9% | +2.3% | 80% | 3,876.00 | fetched |
| Avanza Auto 3 | no data | no data | +65.2% | - | 16,191.00 | book |
| COIN-XBT.ST | no data | no data | +26.0% | - | 15,240.00 | user-relayed |
| Avanza Global | no data | no data | +0.0% | - | 119,999.00 | book |
| ETH wallet | no data | no data | no data | - | 8,911.00 | user-relayed |

Crypto context: bitcoin 55,771 EUR (+0.3% / -0.6% / +1.6% over 24h/7d/30d,
-48.2% vs ATH); ethereum 1,644.50 EUR (+1.2% / -1.3% / +6.7%, -61.1% vs ATH).

**Reading it.** Nothing moved enough to matter. The largest move in the
table — AstraZeneca +4.9% — is about 290 SEK on a 6,182 SEK position; the
whole stock sleeve (27,122 SEK, 14.3% of investable capital) moved by
roughly a rounding error against a 214,863 SEK book. No move contradicts a
thesis, and two are mildly confirming: AZN is the one name valuation calls
cheap and it rose the most while still sitting only 32% up its 52-week
range, and Volvo B is flat since purchase, which is exactly what
thesis-review says it should be at three days old — nothing to test yet.
Atlas Copco B at 99.7% of its 52-week range after +3.9% is the one to
watch, for the reason in section 5 (expensive, and no stated reason for
owning it).

**The real finding in this table is what isn't in it.** Avanza Global
(119,999), Auto 3 (16,191) and COIN-XBT.ST (15,240) have no live price —
151,430 SEK, **70.5% of total capital, is carried at book or at a
user-relayed figure up to nine days old**. The four broad/passive lines
(Global, Auto 3) are deliberately buy-and-hold and need no commentary
beyond that; but "how are my positions behaving" currently has a
verifiable answer for 29.5% of the money.

**Reconciliation vs 2026-08-03.** That sweep's calls have held: the P6
medium-tier build executed (five names, 24,656.69 SEK), all five are
within ±2.6% of cost three days on; the 85/10/5/0 target was written into
`portfolio.json`; Avanza Global's TER confirmed at 0.10%; the ETH quantity
correction (0.50185 ETH, ~29% overstatement removed) is reflected in every
figure here. Two 08-03 calls have *not* progressed: P4 (cheaper BTC
certificate, still blocked on S1) and the retroactive
`swedish-equity-review` on the five new positions.

---

## 2. What should change

Four things, in order of size of the problem, not size of the trade.

**(a) Five positions get a written thesis this session — four stocks and
ETH.** ATCO-B, AZN, ALFA and ABB were bought 2026-08-03/04 with
`portfolio.json` recording only "part of the P6 medium-tier build." That
is not a weak thesis; it is no claim at all, so nothing can be tested
against it at any future sweep. ETH has had `thesis: TBD` for 10+ sweeps.
Together that is 29,242 SEK — 15.4% of investable capital — that the
system structurally cannot evaluate. This is the most important item this
sweep and it is a process failure, not a market call.

**(b) Deploy the 1,743.61 SEK of idle ISK cash into AstraZeneca.** Three
lenses point independently at AZN: valuation calls it the only Cheap name
of the seven (PEG 1.33, 32% up its range), macro says the regime rewards
developed-market dividend-paying low-beta equity, and the sector scorecard
says do not add industrials — AZN is healthcare. One share, ~1,546 SEK.

**(c) The "let crypto dilute" instruction gets a deadline.** Crypto is
+2.83pp / ~5,361 SEK over target on investable capital, macro flags it as
sitting on the wrong side of the current regime, and dilution has produced
nothing in three sweeps because no contribution has landed. Keep the
instruction, attach a trip-wire (section 4, call C).

**(d) Nothing to do on SHB-A / INVE-A.** Both are flagged as rotation
candidates by thesis-review, but combined they are 2,226.70 SEK — 1.2% of
investable capital — and selling either would push the already-ACT
industrials concentration higher, not lower. Held, with a revisit trigger.

No new candidates this week — `scout` was not invoked and the Watchlist
tab (32 entries) has only just gone live.

---

## 3. Portfolio health scorecard

Carried from the portfolio agent verbatim.

| Dimension | Grade | Note |
|---|---|---|
| Asset allocation vs targets | **WATCH** | Raw: equity 73.0% vs 85% (-12pp). On investable capital only (Avanza ISK + ETH wallet, 189,352.79 SEK): 82.82% vs 85% (-2.18pp, ~4,114 SEK short) — essentially on target. **Use the investable reading for any action.** |
| Equity sector concentration | **ACT** | Industrials 68.99% of the stock-picking sleeve (Volvo, Atlas Copco, Alfa Laval, ABB) vs a 45% threshold. Diluted to ~12.7% of total equity exposure by Avanza Global. |
| Geography (home bias) | **WATCH** | Stock sleeve 62.9% Sweden; ~11.6% of total equity after the global fund. Nominally conflicts with the 2026-07-07 global-unhedged-neutral stance. |
| Currency exposure (revenue) | **UNKNOWN** | No data. |
| Single-position concentration | **WATCH** | Avanza Global 55.85% of total capital — downgraded from literal ACT because it is a diversified index fund, not single-company risk. |
| Institution concentration | **ACT** | Avanza 83.91% of total capital, over the user's own 80% cap. Direct consequence of the ISK consolidation; not reversible without giving up the ISK shelter. |
| Fee drag | **OK** | 564.14 SEK/yr = 0.26% of total, under the 0.4% cap. Worst offender COIN-XBT.ST at 2.5%/yr (381 SEK/yr = 67.5% of all fee drag, on 7.1% of the portfolio). |
| Wrapper efficiency | **OK** | AF fully exited. ISK headroom ≈119,704 SEK vs an assumed ~300k allowance (UNVERIFIED — P7). |
| Drawdown-tolerance fit | **UNKNOWN** | No backtest has ever been run (S5). |

**This scorecard is provisional.** `investor_profile.json` still carries
TBDs that change what "balanced" means: (i) the property goal is
explicitly uncertain and could be a EUR liability, which would reverse the
home-bias reading entirely; (ii) `constraints.exclusions` is empty and
`notes: "None stated yet"`; (iii) monthly-contribution routing was never
finalised into a field; (iv) the -30% drawdown tolerance has never been
tested against the adopted 85/10 target — the two may contradict each
other and you would find out in a bad year, not now.

*Structure (levers 1-2): wrapper closed, fee drag 0.26% and inside cap.
Nothing broke this week. One item outstanding — P4, the 2.5% certificate.*

---

## 4. Headline calls

Each ran through the six-voice Council method. The voices are shown for
transparency; the Chairman line is the decision.

### Call A — Write theses for ATCO-B, AZN, ALFA, ABB and ETH, this session

- **Contrarian:** Writing a thesis after you already own the thing invites
  post-hoc rationalisation — you will construct a story that justifies the
  purchase, which is worse than a blank field because it *feels* like
  diligence. A thesis written to fill a checkbox will not be honoured when
  it breaks.
- **First Principles:** A thesis is only a falsifiable sentence: why I own
  this, and what would make me stop. Without it, "hold" is not a decision,
  it is inertia — you cannot tell a position that is working from one you
  forgot about. Five of eleven lines are currently in that state.
- **Expansionist:** Ignore the constraint and the maximum version is the
  full retroactive `swedish-equity-review` on all five new names plus the
  INVE-A NAV discount — a real scoring baseline, making future rotation
  mechanical instead of impressionistic. Same direction, just bigger.
- **Outsider:** You bought five things in two days and cannot say why you
  own four of them. At 25,000 SEK that is survivable; as a habit it is not
  defensible to anyone, including yourself in six months.
- **Executor:** Monday: one sentence per name, in your own words, into the
  `thesis` field. Fifteen minutes. ETH included — "diversification, hold
  3+ years, sell if X" is complete and testable.
- **Chairman — DECISION:** **No portfolio transaction.** Write five
  one-sentence theses (ATCO-B, AZN, ALFA, ABB, ETH) into
  `data/portfolio.json`, each with an explicit break condition, before the
  next sweep. Then run `swedish-equity-review` retroactively on the five
  P6 names. **The teeth:** if you cannot produce a sentence for a name,
  that name moves to the rotation list rather than getting a
  reverse-engineered story. Biggest risk to monitor: post-hoc
  rationalisation — the break condition is the part that cannot be faked,
  so it is mandatory, not optional. Immediate next step: dictate the five
  sentences.
- Confidence **High** · Horizon **Medium**

### Call B — Act on the SHB-A / INVE-A rotation candidacy, or note it?

- **Contrarian:** The "two lenses converging" is an artifact, not a
  signal. SHB-A and INVE-A are the only two positions with recorded
  theses, so they are the only two that *can* be graded as weakening. The
  four untested names are unflagged because there is nothing to test, not
  because they are healthy. This is survivorship of the flag.
- **First Principles:** Rotation means selling X to fund a better-vetted
  Y. Combined, X is 2,226.70 SEK — 1.2% of investable capital, one of it a
  single share. The question is not "are these the weakest" but "is 2,227
  SEK worth transacting," and it is not.
- **Expansionist:** With no size constraint — building the medium tier
  from scratch today — INVE-A probably makes the cut (a diversified
  Swedish holding company is a cheap proxy for exactly what you want),
  SHB-A probably does not (revenue -3.8% YoY, analyst "underperform," a
  rate environment that pressures bank NIM). That splits the pair, which
  the modest version does not.
- **Outsider:** You own one share of a bank. That is not a position, it is
  a souvenir. No amount of analysis makes one share matter.
- **Executor:** No trade. Fold it into the next contribution: when you add
  to the medium tier, add to a name you have vetted, not to SHB-A.
- **Chairman — DECISION:** **No action — hold both, do not rotate this
  sweep.** Two reasons, and the second is the one that matters: size
  (1.2% of investable capital, courtage on sub-1,000 SEK tickets eats any
  edge), and direction (SHB-A and INVE-A are the *only* non-industrial
  Swedish names in the sleeve besides AZN — selling either pushes the
  ACT-rated 68.99% industrials concentration up, so the rotation flag and
  the concentration flag point opposite ways). Biggest risk: this "no
  action" hardens into permanent inertia. **Trigger to prevent that:**
  revisit if either position exceeds 3% of investable capital, or if the
  retroactive review scores a new name materially above SHB-A's 58/100.
  Immediate next step: obtain INVE-A's NAV discount from Investor's Q2 IR
  page (S6) — it is the single datum that would make this decidable
  instead of impressionistic.
- Confidence **Medium** · Horizon **Medium**

### Call C — Does the crypto/macro tension change the "let it dilute" instruction?

- **Contrarian:** "Let it dilute" was adopted in a different regime and is
  effectively unfalsifiable — it converts every adverse data point into
  "hold anyway." Note also that your own `profit_recycling_rule` says
  high-risk-tier gains should flow to the secure tier, and it has never
  once been executed. COIN-XBT.ST is +26% vs cost; there is real profit to
  recycle and a stated rule saying to recycle it.
- **First Principles:** Two questions are being conflated. (1) Is BTC
  going up next? — this system has no edge there and says so. (2) Is 12.8%
  of investable capital the right size for crypto? — you have a stated
  answer: 10%. Sizing is decidable; direction is not. The overweight is
  5,361 SEK.
- **Expansionist:** The maximum-upside version is *adding* on Fear & Greed
  25, historically a buy zone. But that maximises exposure to precisely
  what macro flags and blows through the 10% cap — it points the opposite
  way from the modest version, and that divergence is itself evidence this
  is not a high-conviction add.
- **Outsider:** Someone tells you their plan for being overweight is "I'll
  fix it by buying other things later." That is fine, if later happens. It
  has not — no contribution has landed since the target was written in.
- **Executor:** No crypto sale. Route the 1,743.61 SEK and the next
  monthly contribution to equity — that cuts crypto weight mechanically,
  with no disposal and no K4 event on ETH, whose cost basis you cannot
  compute anyway (P1).
- **Chairman — DECISION:** **Hold crypto. No sale, no add.** The macro
  read and the COIN-XBT thesis genuinely contradict each other and neither
  side is strong enough to force a trade — but the dilution instruction
  now carries a deadline instead of running open-ended. Concretely:
  deploy the 1,743.61 SEK to equity now (call D) and route the next
  monthly contribution (1,000-3,000 SEK) to equity. **Trip-wire: if crypto
  is still above 12% of investable capital at the 2026-09-03 sweep, "let
  it dilute" has failed on its own terms and is replaced by a trim of
  COIN-XBT.ST** — the certificate, not ETH, because an ISK disposal is
  tax-free while a self-custody ETH sale is a 30% K4 event needing a cost
  basis you do not have. Biggest risk: BTC drops 30%+ while the plan waits
  on contributions. Immediate next step: P1 (ETH cost basis) stays the
  higher-priority crypto item — it is the binding constraint on ever
  acting on the ETH leg at all.
- Confidence **Medium** · Horizon **Medium**

### Call D — Deploy the 1,743.61 SEK idle ISK cash

- **Contrarian:** AZN at 32% of its 52-week range is not "cheap," it is a
  stock the market is marking down for a reason free data cannot see —
  pipeline, patent cliff, litigation. And PEG 1.33 rests on an analyst
  growth estimate you did not verify.
- **First Principles:** 1,744 SEK is 0.9% of investable capital; whatever
  you buy cannot change the portfolio's risk. The only real question is
  whether cash should sit idle inside an investment wrapper at all. It
  should not — it earns nothing and still counts toward the ISK capital
  base (currently harmless only because the balance sits under the
  *assumed* allowance, P7, unverified).
- **Expansionist:** With the constraint off, the answer is the same name —
  more of the only holding three lenses independently favour. Modest and
  maximum versions agree, which is mild confirmation.
- **Outsider:** You have 1,744 kr doing nothing in an investment account.
  Put it in whatever your own analysis says is best value. This is not
  complicated.
- **Executor:** Monday: buy 1 share AZN.ST at ~1,545.50, leaving ~198 SEK
  residual. Courtage on a ticket that size is a few SEK — immaterial.
- **Chairman — DECISION:** **Buy 1 share of AstraZeneca (AZN.ST), ~1,546
  SEK, from the idle ISK cash.** This is the one place three lenses
  converge for real (unlike call B's false convergence): valuation's only
  Cheap rating, macro's rewarded profile, and the sector scorecard's
  instruction not to add industrials. It closes ~38% of the 4,114 SEK
  equity underweight and nudges the sleeve's industrials share from 69.0%
  to ~65.3%. **Condition: write AZN's thesis (call A) before or at the
  time you buy** — do not add to a position you still cannot describe.
  Biggest risk: AZN's 32%-of-range position is information-bearing and
  free data cannot see what it knows. Immediate next step: execute Monday.
- Confidence **Medium** · Horizon **Medium**

---

## 5. Where the agents disagreed

**1. Atlas Copco B — two separate problems, do not merge them into "hold."**
Excel's imported profile shows P/E 2.05; the live snapshot shows 33.7x.
Valuation explicitly resolves this: **use 33.7x and disregard the Excel
figure as a data error** (33.7x is consistent with Atlas Copco's normal
25-35x compounder multiple; 2.05 is not a plausible P/E for anything).
That is problem one — a data-hygiene error that would have made an
expensive stock look like the cheapest thing you own. Problem two is
independent: ATCO-B has **no testable thesis at all**, and it is trading at
99.7% of its 52-week range on a PEG of 2.35. So: this is the
highest-multiple, highest-in-range, least-justified position in the sleeve,
and it is 4,968 SEK. Not a sell call — a "write the thesis first, and be
honest that you are paying up" call. Confidence **High** on the data point,
**Medium** on the expensive rating.

**2. Crypto — carried undiluted, as flagged.** Valuation says cycle
position only: BTC -48.2% off ATH, ETH -61.1%, no rank collapse and no
trend reversal, momentum flat-to-mildly-positive. Macro says the opposite
in effect: a strong dollar (DXY 119.70) plus crypto Fear & Greed at 25
"Extreme Fear" against a calm VIX 16.50 is a bifurcated regime — **stress
concentrated in crypto specifically** — and this is the environment where
cheap crypto gets cheaper before it gets more expensive, not where
"buy-the-dip" gets vindicated on any timetable. Thesis-review sides with
macro: the position's own stated claim ("BTC pretty low valued, positive
buy-in signals now") is harder to sustain today than at purchase, with the
position already +26%. **Resolution: hold, do not add, trip-wire at 12%
(call C). Confidence Low on direction — this is regime-dependent and could
flip on a single DXY or CPI print.**

**3. The equity gap has two readings and only one is actionable.** Raw:
equity 73.0% vs 85% target, -12pp. Investable-capital-only: 82.82%,
-2.18pp (~4,114 SEK). **Act on the second.** The raw reading treats three
things as "cash you chose to hold" that are nothing of the sort: the
11,363.76 SEK tax reserve (money already owed to Skatteverket), 611 SEK of
checking, and ~14,146 SEK sitting in PayPal that cannot be routed until P3
is decided. None of those are allocation decisions, so counting them
manufactures a 12-point gap that would justify a ~25,000 SEK buy you do
not need. This is a data-hygiene finding, not a number: **the denominator
is a choice, and choosing it wrong produces a real trade.** The same
mechanism explains why macro reports crypto at 11.3% and portfolio reports
it +2.83pp over a 10% target — different denominators, both correct.

**4. Handelsbanken A — fundamentals and insiders point opposite ways, and
valuation says so out loud.** Trailing P/E 12.5x is reasonable-to-cheap for
a bank, but the price is at 98% of its 52-week range while revenue fell
3.8% YoY and the analyst tag is "underperform." Valuation's read: the
July 2026 insider buying (Chairman Pär Boman + Fredrik Lundberg, >750M SEK
combined) is doing the work of explaining the price strength, **not the
fundamentals**. Thesis-review independently grades the thesis "Weakening"
on the "still shows good upside" limb. These agree in direction and are
resolved in call B on size grounds, not on merit. Confidence **Medium**.

**5. Investor A — "insufficient data" and "played out" are the same
answer.** Valuation refuses to rate it: P/E 4.88 and PEG 4.91 are
holding-company accounting artifacts, **not cheap signals**, and the NAV
discount that would actually settle it has never been obtained (S6).
Thesis-review says the cited upside has already been captured (+43.3% vs
cost, within 0.5% of the 52-week high). Neither supports adding. Neither
supports selling either, given size. Confidence **Medium**, and it will
stay Medium until S6 closes.

**6. A disagreement neither lens named, worth surfacing.** Macro says the
current regime *rewards* precisely the profile of the medium-tier build —
developed-market, dividend-paying, low-beta industrials and healthcare.
Valuation says three of those four new names (ALFA PEG 2.91, ABB PEG 2.58
at ~37x, ATCO-B PEG 2.35 at 33.7x) are **Expensive**, bought at 80-99% of
their 52-week ranges. Both can be true: the regime is favourable *and* you
paid a full price for it. The practical consequence is that this sleeve's
return now depends more on multiples holding than on the businesses
performing — which is exactly the kind of claim a written thesis (call A)
would have forced you to state before buying. Confidence **Medium**.

---

## 6. Broken theses requiring a decision

From thesis-review, unsoftened. Nothing is strictly Broken this sweep.

- **ATCO-B.ST, AZN.ST, ALFA.ST, ABB.ST — no testable thesis on record at
  all.** Not weakening, not broken: there is no claim to test. 20,132 SEK.
- **ETH — thesis field literally "TBD" after 10+ sweeps.** 8,911-9,057 SEK.
  The blocker is you, not data.
- **SHB-A.ST — Weakening.** "Stable, good track record" holds (beta 0.504,
  5.42% dividend). "Still shows good upside" is under pressure: 98.7% of
  range, "underperform," revenue -3.8% YoY, PEG 20.2, rates a headwind for
  bank NIM.
- **INVE-A.ST — Played out.** +43.3% vs cost, within 0.5% of the 52-week
  high; the cited upside has been captured. NAV discount still never
  obtained.
- **COIN-XBT.ST — Weakening.** "BTC pretty low valued... positive buy-in
  signals now" — the -48.2%-off-ATH half survives, the "positive buy-in
  signals" half is harder to sustain at Fear & Greed 25 with the position
  already +26%.
- **VOLV-B.ST — intact / too early.** Bought three days ago into an
  unresolved tension (revenue decline + D/E 147 vs a large insider buy).
  Flat since. Nothing to call.
- **Avanza Global, Auto 3 — intact**, structural core roles unchanged.

---

## 7. Rebalancing actions

From the portfolio agent, in tax-priority order.

| # | Action | SEK | Tax cost |
|---|---|---|---|
| a | Route new monthly contributions to equity | 1,000-3,000/mo | None |
| b | Deploy idle ISK cash to equity (→ 1 share AZN.ST, call D) | 1,743.61 | None (ISK) |
| b' | P4 certificate swap — **do not execute**, blocked on a verified ticker (S1) | saves ~228.60/yr | None (ISK) |
| c | AF account — nothing sellable | — | — |
| d | Crypto disposal — **not recommended** | — | — |
| — | PayPal routing (P3) — outside the tax ladder, worth doing | ~566 saved | None |

Notes: (a) closes the 4,114 SEK investable-capital equity underweight in
1.4-4 months at the low end of the contribution range. (d) crypto is only
mildly overweight on the number that matters (+2.83pp / ~5,361 SEK on
investable capital); the standing instruction is dilution, not sale, and
ETH's unknown cost basis (P1) blocks the tax math for any real sale anyway.

---

## 8. Cost of being wrong

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| A — write five theses | ~0 SEK direct. Real cost is a rationalised story locking in a bad position; the mandatory break condition is the guard. | Yes |
| B — hold SHB-A + INVE-A | Both drift while better names exist. A 20% fall on 2,226.70 SEK = **-445 SEK**. | Yes, trivially |
| C — hold crypto, trip-wire at 12% | A 30% crypto drawdown on ~24,150 SEK = **-7,245 SEK** (-3.8% of investable capital). Inside the -30% tolerance at portfolio level. | Yes |
| D — buy 1 AZN.ST | Full 30% fall on 1,545.50 SEK = **-464 SEK**. | Yes, trivially |
| Data risk (not a call) | Acting on the raw -12pp reading instead of -2.18pp would have justified a ~25,000 SEK equity buy funded from money already owed to Skatteverket. **Not recoverable in the same way** — it would create a tax-payment shortfall. | Avoided this sweep |

---

## 9. Open actions

Things you can just go do. IDs match `/OPEN_ITEMS.md`.

1. **Deploy 1,743.61 SEK** → 1 share AZN.ST (call D). Monday.
2. **P6 — run `swedish-equity-review` on the five new positions**
   (VOLV-B, ATCO-B, AZN, ALFA, ABB). Retroactive baseline, not
   second-guessing the trade. Before next sweep.
3. **Write five theses** (call A) — ATCO-B, AZN, ALFA, ABB, ETH. Fifteen
   minutes, one sentence + one break condition each.
4. **P1 — find the ETH cost basis.** Blocks every disposal, tax figure and
   return number on 0.50185 ETH. Not urgent unless you intend to sell —
   but call C's trip-wire makes that less hypothetical than it was.
5. **S1/P4 — add verified Nordic crypto-ETP tickers (Virtune, Valour, XBT
   Provider, CoinShares) with current fees to the Excel Watchlist tab**,
   then re-run the import. Until that exists, P4 cannot be screened and
   ~228.60 SEK/yr stays on the table.
6. **P3 — price the Revolut route out of PayPal.** ~566-575 SEK on the
   current 1,177.49 USD + 266.88 EUR, and it recurs every ~2 months
   forever. Macro adds a second reason: that USD balance is exposed to
   further SEK weakening if dollar strength persists.
7. **P7 — verify the ISK allowance threshold and rate with Skatteverket.**
   Small, but the ~300k figure is load-bearing in all headroom math.
8. **Monthly contribution** — that decision runs on its own cadence via
   the `monthly-contribution` skill, not this sweep. Routing it to equity
   is what makes calls C and the equity underweight resolve.

---

## 10. Open decisions

Forks the data does not settle. Each gets concrete options.

**D1 — SHB-A.ST and INVE-A.ST (2,226.70 SEK combined).**
- *(a) Hold both, revisit at the 3%-of-investable-capital trigger.*
  Chairman's call. Costs nothing; risk is drift by inertia.
- *(b) Sell the single SHB-A share and fold it into the next
  contribution.* Removes a one-share souvenir, but ~148 SEK makes courtage
  a meaningful fraction of the trade, and it nudges industrials
  concentration up.
- *(c) Get INVE-A's NAV discount/premium from Investor's Q2 report (S6)
  and decide on real data.* ~20 minutes with the `pdf` skill; converts an
  impressionistic call into a measurable one.

**D2 — What the 1,743.61 SEK buys.**
- *(a) 1 share AZN.ST (~1,546 SEK).* Chosen. Only Cheap rating, cuts
  industrials to ~65.3%, leaves ~198 SEK residual.
- *(b) Avanza Global.* Zero courtage, cheapest fee in the book, buys the
  whole amount — but worsens the 55.85% single-fund and 83.91% institution
  concentrations and does nothing for the industrials ACT flag.
- *(c) Hold as dry powder for the P4 swap.* Not a real option — the swap
  is funded by the certificate's sale proceeds inside the ISK, not by
  cash, and P4 is blocked on S1 regardless.

**D3 — The crypto overweight (+5,361 SEK over target).**
- *(a) Dilution with a 12% trip-wire at the 2026-09-03 sweep.* Chosen.
  No tax event, no disposal, but it depends on contributions actually
  landing.
- *(b) Trim COIN-XBT.ST by ~5,361 SEK now to hit 10% exactly.* Tax-free
  inside the ISK, honours the `profit_recycling_rule` that has never once
  been executed, cuts the 2.5%/yr fee on the trimmed portion — but sells
  into Fear & Greed 25, historically the wrong side of that indicator.
- *(c) Leave "let it dilute" open-ended.* Simplest; it is also the status
  quo that has produced zero dilution across three sweeps.

**D4 — The medium tier's multiple risk.** Three of four new names were
bought at 80-99% of range on PEGs above 2.3.
- *(a) Accept it as the price of a quality sleeve, hold, and let the
  written theses (call A) define what would break them.* Chosen by
  default via call A.
- *(b) Cap further medium-tier additions at names with PEG < 2.0 until the
  retroactive reviews land.* A concrete rule; the cost is possibly sitting
  out a name you would otherwise want.

---

## 11. Timing collisions

**None checked this sweep — and that is itself the flag.** The `calendar`
agent was not invoked, so the AZN.ST purchase in call D is **not verified
against AstraZeneca's next earnings date**. S3 (no Alpha Vantage/FMP key)
means Nordic earnings dates are unreliable from Yahoo anyway; the earnings
fetch failed outright on 2026-08-03. Riksbank's rate is current as of
today (1.75%, 2026-08-06), so no near-term Riksbank collision is known.
On a 1,546 SEK ticket this does not change the decision, but do not read
the absence of a collision flag as an all-clear.

---

## 12. Excel data gaps

Verbatim from `data/cache/excel_import/latest-summary.json` flags. This is
a to-do list for you in the workbook, not a data failure — the memo stands
without it. Fundamentals updated cleanly for all seven Nordic tickers
(as_of 2026-08-05), and 32 Watchlist entries are now live across 7
categories, superseding `data/universe.json` for `scout`'s purposes.

1. **ALFA.ST, ATCO-B.ST, SHB-A.ST, VOLV-B.ST — no 52-week range in Excel.**
   Confirmed data-provider gap for some Nordic-primary tickers, not a
   formula bug. Not blocking (the snapshot supplies range for these).
2. **ATCO-B.ST — P/E 2.05 is outside the 3-80 sanity range.** Treat as
   suspect; verify in Excel before using it. The live snapshot's 33.7x is
   what this memo used (see section 5, item 1).
3. **COIN-XBT.ST is held but missing from Excel's STOCK DETAIL block.**
   Add it with the Stocks data type for next sweep — this is the position
   with no working price feed anywhere, so the workbook is the only place
   it could get one.
4. **A transactions row needs correcting.** A row reading `BUY, ethereum,
   1 unit, 2016.67 SEK/unit` pairs the ticker "ethereum" with the
   name/price/quantity of the COIN-XBT.ST 6th-unit purchase — a
   near-duplicate of the row directly above it. 2,016.67 SEK is not a
   plausible ETH price; this looks like a copy-paste artifact, not a real
   trade. It was imported into `transactions.csv` as-is (no cross-check
   exists yet) and needs you to verify or correct it in Excel. Left
   uncorrected, it will corrupt any future attempt to derive P1 (the ETH
   cost basis) from the transaction history.

---

## 13. Missing data

What this memo could not see, stated so it does not read as confidence.

- **No `swedish-equity-review` has been run on the five new positions
  since purchase** (P6's outstanding item). VOLV-B and ATCO-**A** have
  2026-07-28 pre-purchase profiles; ATCO-**B** (the share actually held),
  AZN, ALFA and ABB have no `data/company_profiles/` entry at all. There
  is no scored baseline to test any of them against at the next check-in.
- **70.5% of total capital carries no live price** this sweep (Avanza
  Global at 2026-07-28 book, Auto 3 at 2026-07-24 NAV, COIN-XBT.ST
  user-relayed 2026-08-03).
- **ETH value is carried at two figures** — 8,911 SEK in the position
  report (as_of 2026-08-03) and 9,056.68 SEK in the portfolio lens's
  total. ~146 SEK, immaterial to every conclusion here, but it means the
  ETH line is repriced inconsistently between artifacts.
- **Swedish CPI is 8 months stale** (0.3% YoY, period 2025-12 — S4). Any
  "real Swedish rate" figure rests on it. Not used as load-bearing here.
- **No backtest exists** (S5) — the 85/10/5/0 target has never been tested
  against the stated -30% drawdown tolerance. Drawdown-tolerance fit stays
  UNKNOWN on the scorecard.
- **INVE-A's NAV discount/premium** has never been obtained (S6) — the
  only metric that would make Investor A properly testable.
- **Currency-of-revenue exposure: no data** for any holding.
- **The ~1,743.61 SEK ISK cash figure is computed, not broker-confirmed**,
  and does not account for courtage on the five P6 purchases. Verify
  against the actual Avanza statement before placing the AZN order — the
  real figure may be slightly lower.

---

## 14. Learning notes

- **PEG is why AZN reads "cheap" and Atlas Copco reads "expensive" even
  though both are quality names.** PEG divides the P/E by the growth rate,
  so it asks how much you pay *per unit of growth* rather than per unit of
  current earnings. AZN's 23.9x P/E over a 1.33 PEG implies roughly 18%
  expected growth; ATCO-B's 33.7x over a 2.35 PEG implies about 14%. You
  are paying nearly twice as much per point of growth for Atlas Copco.
  That single ratio is doing the work behind two opposite ratings, which
  is also why a raw P/E comparison between them would have told you
  nothing useful.
- **Choosing the denominator is a decision, not bookkeeping.** The same
  portfolio was 12 percentage points underweight equity on one denominator
  and 2.18 points underweight on another. The difference is whether you
  count the tax reserve, checking cash and unroutable PayPal balance as
  "cash you chose to hold." Money already owed to Skatteverket is not
  yours to allocate — including it would have justified a ~25,000 SEK buy
  funded partly from the tax bill. When a percentage looks alarming,
  check what is in the bottom of the fraction before acting on it.
- **Absence of a red flag is not a clean bill of health — sometimes it is
  absence of a test.** SHB-A and INVE-A look like the weakest holdings
  this sweep, but they are also the only two with a written thesis, so
  they are the only two that *can* be graded as weakening. The four
  unflagged new positions are unflagged because there is nothing to
  measure them against. This is why call B declined to treat "two lenses
  independently flagged these" as a signal: one of those flags was an
  artifact of which positions happen to be testable.
- **Wrapper, not asset, decides which crypto leg is cheap to trim.** The
  crypto trip-wire names COIN-XBT.ST rather than ETH, and that is a tax
  point, not a market view. Selling inside an ISK is tax-free with no K4
  reporting; selling self-custody ETH is a 30% capital-gains event that
  requires a cost basis you do not currently have (P1) — and in Swedish
  crypto tax, *every* disposal counts, including token swaps, not just
  sales for SEK. Two positions with near-identical exposure can have
  completely different costs to exit.

---

*End of memo.*
