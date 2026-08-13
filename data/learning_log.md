# Learning log

Cumulative record of the "Learning notes" section from each council memo —
the reasoning behind decisions and concepts touched that sweep, in plain
terms. Not a course, not comprehensive; a byproduct of the sweeps that
happens to build into a personal reference over time. Read it top-to-bottom
occasionally, or search it for a term you've forgotten the reasoning behind.

Added by `council` automatically each sweep — see its "Learning notes"
section in `.claude/agents/council.md` for the rule. Entries are append-only
and dated; nothing here is a source of truth for a decision, that's still
`data/portfolio.json` and the dated memo in `reports/`.

---

## 2026-08-06 — `reports/2026-08-06-council-memo.md`

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
  measure them against. This is why the rotation call declined to treat
  "two lenses independently flagged these" as a signal: one of those flags
  was an artifact of which positions happen to be testable.
- **Wrapper, not asset, decides which crypto leg is cheap to trim.** The
  crypto trip-wire names COIN-XBT.ST rather than ETH, and that is a tax
  point, not a market view. Selling inside an ISK is tax-free with no K4
  reporting; selling self-custody ETH is a 30% capital-gains event that
  requires a cost basis you do not currently have (P1) — and in Swedish
  crypto tax, *every* disposal counts, including token swaps, not just
  sales for SEK. Two positions with near-identical exposure can have
  completely different costs to exit.

---

## 2026-08-10 — `reports/2026-08-10-council-memo.md`

- **A threshold rule is only as solid as its denominator, and this week the
  denominator moved the answer more than the market did.** The same 24,410 SEK
  of crypto is 11.28%, 11.4% or 11.91% depending on whether the tax reserve and
  checking cash sit in the bottom of the fraction — a 0.63pp spread against a
  trip-wire set at 12.00%. Bitcoin would have to fall meaningfully to change
  the answer; an accounting choice changes it for free. That is why the
  denominator got pinned in this memo three weeks *before* the check, rather
  than on the day: a rule you can satisfy by choosing how to count is not a
  rule, it is a preference with a number attached. (Direct extension of the
  2026-08-06 denominator note above — same lesson, now with a live threshold
  attached to it.)
- **"The regime favours this sector" and "this is a good time to buy it" are
  different sentences, and the 52-week percentile is what separates them.**
  Macro says industrials are what this environment rewards — no yield-curve
  inversion, VIX at 15, no recession signal. But Atlas Copco sits at the 98th
  percentile of its own 52-week range at PEG 2.40. The favourable regime is the
  *reason* it is at the 98th percentile; you are not buying the tailwind, you
  are buying the price the tailwind already produced. A high 52-week percentile
  is not a sell signal on its own — it usually reflects real strength — but it
  does mean the cheap way to express a view has already gone.
- **Two portfolios can sit in two different regimes at the same time, and this
  one does.** Equity volatility is calm (VIX 15.15, curve positively sloped,
  real Fed funds ~-0.10%) while crypto sits in Fear (F&G 30, BTC -47.6% off
  ATH) with an elevated dollar (119.70) working against it. There is no single
  "risk-on / risk-off" number for this portfolio, and any framing that produced
  one would be hiding the more useful fact: the 87% of capital in equities and
  the 11% in crypto are being driven by different things right now, so they
  should not be sized off the same view.
- **UNTESTED is a statement about your records, not about the company — which
  is exactly why it justified a deadline rather than a sale.** Atlas Copco,
  Alfa Laval and ABB are strong businesses and nothing in this sweep suggests
  otherwise. The problem is that a holding with no written `break_conditions`
  has no exit rule, which means the position can only ever be sold on feel. The
  right response to a missing thesis is to produce the evidence to write one
  (the retroactive `swedish-equity-review`), not to sell a good business to
  resolve a paperwork state — but it does need a date attached, because
  "eventually" has now failed twice.

---

## 2026-08-11 — `reports/2026-08-11-council-memo.md`

- **A limit that only holds because of money you can't reach isn't holding.**
  The crypto trip-wire reads 11.79%, 11.94% or 12.66% depending on the
  denominator — and the only reason the loosest reading clears 12% is that
  14,079.79 SEK of PayPal balance is counted as investable capital. That money
  is genuinely yours (so counting it is defensible) but costs ~4% to move (so
  excluding it is also defensible). The general lesson: when a threshold is
  close, look at *what is in the bottom of the fraction* and ask whether you
  could actually spend it. Here, an unresolved fee decision (D1) is quietly
  underwriting a risk limit (D3) — two items that look unrelated on the list.
- **Beta is a claim until a red day tests it.** AstraZeneca's thesis says
  "lower-beta than high-valuation growth" and its measured beta is 0.211,
  meaning it should move about a fifth as much as the market. Today six of
  seven stocks fell and AZN rose 1.4%. One day proves nothing statistically,
  but it is the difference between a thesis you asserted and a thesis you have
  seen behave — which is exactly what `thesis_status: INTACT` is supposed to
  mean, and why it carries more weight than the four positions marked UNTESTED.
- **"Would I buy this today?" catches errors that "is the thesis intact?"
  misses.** Last sweep routed cash to the index fund because "the medium tier
  has no vetted candidate." Thesis-review's would-buy-today column said YES to
  AZN.ST that same sweep — the candidate was sitting in the book. Re-asking a
  holding as a fresh purchase decision, rather than as a position to maintain,
  is what surfaced the mistake. This is a reason to read that column as a *buy
  list*, not just a health check.
- **Same label, different definition — the S11 problem moved up a level.** The
  "% of 52-week range" ambiguity got fixed this sweep (valuation now reports the
  true percentile and thesis-review labels its own metric distinctly). But the
  identical failure immediately reappeared one level up: two "investable
  capital" denominators that agree to 0.15pp today and would diverge whenever
  PayPal moves. The fix is the same both times — pin the *definition* in words,
  not the number, because the number goes stale and the definition is what you
  are actually arguing about.

---

## 2026-08-12 — `reports/2026-08-12-council-memo.md`

- **Choosing a trim size is a different question from choosing a trim
  direction, and the second one is where the leverage is.** Four independent
  lines pointed at trimming crypto this sweep, but the agent-recommended
  3,000-5,500 SEK band would have overshot: at two units the position drops to
  8.99% of capital on the broadest denominator, a full point *below* the 10%
  target. You would have cleared a trip-wire by creating an underweight —
  fixing one deviation with another. The right move was to find the size that
  satisfies every competing measurement at once (one unit: 10.19% / 11.57% /
  10.76% across the three conventions). When a rule and a target pull in
  opposite directions, solve for the overlap rather than picking a side.
- **Sell the wrapper, not the idea.** The strongest argument against trimming
  was genuinely good: BTC is 49% off its high with sentiment at Fear, and
  selling drawn-down assets into fear is the classic retail mistake. What
  dissolves that objection is noticing the position has two separable
  properties — exposure to bitcoin, and a 2.5%/yr certificate fee. Bitcoin
  exposure is held through the expensive vehicle *and* ethereum through a
  zero-fee wallet. Trimming the expensive one preserves the conviction and
  removes 64.53 SEK/yr of guaranteed drag. A guaranteed cost beats an uncertain
  gain when you can separate them.
- **Where money came from determines where it should go — the provenance
  rule.** Last sweep routed spare ISK cash to AstraZeneca; this sweep routes
  crypto trim proceeds to Avanza Global instead. That looks like a reversal and
  is not. `investor_profile.json`'s `profit_recycling_rule` says gains from the
  high-risk tier default into the secure tier — "a monetising machine." Last
  sweep's money was leftover build cash, which the rule does not cover; this
  sweep's is a high-risk-tier realization, which it does. Rules that key on the
  *source* of capital rather than its amount are what stop a portfolio from
  silently ratcheting up risk with every profitable trade.
- **A thesis with no valuation leg cannot be broken by valuation — and that is
  a weakness, not a defence.** ATCO-B, ALFA and ABB are all "Expensive" on PEG
  (2.41 / 2.92 / 2.70), and the recorded thesis explicitly makes no price claim
  ("strong track record… want to promote Swedish stocks"). Those two statements
  do not contradict each other; they never touch. The consequence is that these
  three holdings are structurally *harder to falsify* than AstraZeneca, whose
  thesis names testable break conditions (margins deteriorate, dividend cut,
  re-rates to a growth premium). An unfalsifiable thesis is comfortable to hold
  and impossible to be wrong about, which is exactly why the binding constraint
  on those names had to come from somewhere else — portfolio concentration,
  which is a fact rather than an opinion.

---
