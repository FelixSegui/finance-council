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

## 2026-08-17 — `reports/2026-08-17-council-memo.md`

- **Five positions all near their highs at once is one fact, not five — and that
  distinction changes what you do about it.** Read name-by-name, "Atlas Copco is
  at 98% of its range" is unremarkable; strong companies spend a lot of time near
  their highs. Read together, five holdings chosen for the *same* stated reason
  ("strong track record", "Swedish industrial champion") all arriving at 92-99% of
  their highs in the same week is a single bet that has already largely played
  out, placed five times. The technical name for what makes them move together is
  correlation — Volvo, Atlas Copco, Alfa Laval and ABB all sell equipment into the
  same global capex cycle, so they are far less independent than four tickers
  suggest. This is exactly why the memo's constraint on them is *concentration* (a
  measurable fact: 65.29% of the stock sleeve) rather than *valuation* (an
  opinion), and why the answer was "no more" rather than "sell."
- **Beta is the number that put AstraZeneca on the right side of the regime while
  ABB sits on the wrong one.** Beta measures how much a stock has historically
  moved relative to the market: 1.0 means it moves with it, above 1.0 means it
  amplifies it, below means it dampens it. AZN's beta is 0.211 — roughly a fifth
  of market movement — against ABB at 1.011 and Atlas Copco at 1.071. With VIX at
  14.63 (calm, arguably complacent), macro-regime's read is that cheap volatility
  is exactly when defensive ballast is worth owning, because you are being asked
  to pay very little for protection nobody currently wants. That single number,
  not a view on drug pipelines, is why the defensive name is the one macro
  declined to flag.
- **A drawdown estimate built by summing worst cases is wrong in a known
  direction, and saying so is more useful than reporting the number.** This
  sweep's -42.3% figure assumes every asset has its worst year simultaneously —
  that is, perfect correlation. Real portfolios do not behave that way, and this
  one especially: 63.57% of it is a single globally diversified index fund whose
  internal holdings partly offset each other. So the true number is almost
  certainly better than -42.3%. But "the estimate is pessimistic" and "the target
  is fine" are different statements, and the gap between them is what a real
  backtest (S5) exists to close. The correct response to a biased estimate is to
  run the unbiased test, not to average the bias away or to act on the biased
  number — which is why Call 3 was a governance stop rather than an allocation
  change.
- **A backup data source that fails at the same time as the primary was never
  really a backup.** COIN-XBT.ST has no working ticker — a known permanent fact —
  so this system adopted spot bitcoin from CoinGecko as a directional proxy
  precisely so that gap would not be a single point of failure. This week both
  failed at once (ticker 404, CoinGecko rate-limited on three attempts), leaving
  the trip-wire resting on a four-day-old spreadsheet cell. The right response was
  not to estimate the price from training knowledge or from ETH's move — it was to
  record "no data," then ask a different question: *how far off would the stale
  price have to be for the decision to change?* The answer (~13.5% to make the trim
  unnecessary, ~26.7% to make it harmful) turned an unanswerable question into a
  decidable one. When you cannot get the number, test how much the number matters.

---

## 2026-08-17 (memo 2, live session) — `reports/2026-08-17-council-memo-2.md`

- **"Fully BTC-backed" is a claim about a fund's *structure*, and structure is the
  one thing a price feed can never tell you.** Three different products can carry
  bitcoin in the name and behave completely differently: a **physically-backed ETP**
  holds actual BTC in custody and tracks spot almost exactly; a **futures/strategy
  fund** holds derivatives and can bleed value through roll costs or trend-following
  whipsaw even when spot goes sideways; and a **treasury-company fund** holds shares
  in businesses that own bitcoin, which adds equity risk, management decisions and
  leverage on top. BITC's name — "TRND BITCN TRSR STRGY" — reads as the second or
  third kind, not the first. The reason this mattered more than the fee arithmetic:
  the whole trade was justified by saving 2.35 percentage points a year, which is
  only a saving if you end up owning the same asset. **Optimizing the small number
  while unknowingly changing the big one is the most common way a "cost-cutting"
  trade destroys value.**
- **Why you can buy Apple at Avanza but generally can't buy a US-listed ETF.**
  Under EU rules (MiFID II / PRIIPs, in force since 2018), a fund sold to EU retail
  investors must publish a short standardised **KID** — Key Information Document —
  in a local language. US-domiciled ETFs publish a US prospectus instead and mostly
  haven't bothered producing KIDs, so European brokers block them for retail
  clients. Individual *shares* aren't caught by the rule, which is why the
  restriction feels arbitrary until you know the mechanism. The practical takeaway
  for your ISK: when a US ticker looks attractive, check whether it is a **company**
  or a **fund** first — it changes whether the question is even askable.
- **A backtest's window is part of its answer, and a suspiciously good CAGR is the
  tell.** This sweep's real backtest says the 85/10/5/0 target's worst drawdown was
  -19.95% — comfortably inside the -30% tolerance, and the opposite of the crude
  estimate it replaced. But it also reports a **15.0% annual return** over 7.2
  years, roughly double a realistic long-run global equity return. That is not good
  news about the allocation; it is information about the period, which began in
  2019 and excludes 2008 entirely. One more detail worth internalising: the target's
  **max drawdown equalled its worst rolling 12 months**, meaning the entire fall
  happened inside a single year. A slow -20% and a fast -20% are the same number and
  very different experiences — the fast one is what makes people sell. This is why
  the scorecard row moved to "OK (provisional)" rather than "validated."
- **Rebalancing back to a target is not the same thing as timing the market, and
  the distinction decides whether macro gets a vote.** Macro-regime flagged a real
  headwind for crypto — strong dollar, US policy rate well above the ECB's,
  sentiment at "Fear." It then drew the line itself: that warning applies to *sizing
  up* on a "good entry" read, and is *irrelevant* to restoring an allocation you
  already decided to hold. Restoring crypto from 4.13% to its written 10% is
  mechanical compliance with a target you adopted; deciding that now is a great
  moment to own more bitcoin would be a forecast, which this system doesn't make.
  Same trade, two different justifications, and only one of them is defensible on
  free data.
- **When two of your own written rules collide, the collision is the finding.**
  Your `profit_recycling_rule` says gains from the risky tier flow to the safe tier.
  Your target says hold 10% crypto. Applied to a *partial* trim those never touch —
  but applied to the *full* sale executed today, the recycling rule would
  mechanically prevent you from ever holding 10% crypto again. Nobody decided that;
  it would just happen. The general lesson is that rules written for one situation
  quietly acquire consequences in another, and the moment to notice is when a rule
  starts producing an outcome you would not have chosen if someone asked you
  directly.

---

## 2026-08-17 (memo 3, Stock Selection Council test run) — `reports/2026-08-17-council-memo-3-stock-selection-test.md`

- **When forward P/E sits *above* trailing P/E, the market is telling you it
  expects earnings to fall.** This showed up four separate times across one
  76-name universe and is one of the cheapest sanity checks available. Tele2
  looks like a 6.37%-yield defensive holding until you see trailing 11.4 against
  forward 25.0 — consensus expects earnings to roughly halve, which is *why* the
  yield is high. The same signature appears at Avanza Bank (22.4 → 30.8), Lifco
  (37.3 → 39.6) and, in its flat form, ABB (37.6 → 37.1 *while revenue grew
  14.2%*, which is the margin-compression version of the same message). The
  reverse is equally informative: Nvidia at 34.5 → 17.6 and TotalEnergies at
  11.1 → 9.2 are consensus saying earnings are rising fast.
- **P/E and PEG can point opposite ways on the same stock, and that conflict is
  the analysis, not a problem to resolve.** Novo Nordisk trades at a P/E of 11.2
  — cheap — and a PEG of 3.11 — expensive. Both are correct: P/E asks "what am I
  paying per krona of *current* earnings," PEG asks "per krona of *growth*." A
  company with strong current earnings and stalled growth reads cheap on one and
  expensive on the other. The whole investment question then collapses to which
  number describes the future, and the honest answer here was "one more quarter
  of revenue will tell you" — which is why a candidate four of seven analyst
  lenses picked still resolved to WATCH rather than BUY.
- **Buying an index fund's largest holdings individually concentrates your
  portfolio — it does not diversify it.** Avanza Global is 54.84% of this
  portfolio, and Meta, Alphabet, Nvidia, Microsoft, Apple and six others are
  already inside it. Adding one individually takes on single-company risk (that
  one firm's lawsuit, product miss, executive departure) in exchange for zero new
  economic exposure. That single structural fact removed eleven of the thirty-two
  names that passed the numeric screen — more than any valuation judgment did. It
  is also why the honest response to liking a mega-cap is usually to buy more of
  the index fund, not the stock.
- **A screening threshold that is right on average is wrong for specific business
  models, and knowing which is a real skill.** The screen used debt/equity above
  150 as a fail. That is sensible for a manufacturer and meaningless for a bank,
  whose entire business *is* leverage — which is why SEB and Swedbank got labelled
  "missing data" rather than properly screened. Likewise profit margin for an
  investment company (Kinnevik failed at 0.0%), and a 40x P/E cap for a defence
  contractor whose order book runs years ahead of reported earnings (Saab). The
  right response is not to abandon the threshold — it catches real problems most
  of the time — but to be able to say *why* it does not apply to a specific name,
  and to accept that "I can argue the screen is wrong here but I still cannot
  underwrite the company without the data" is a legitimate place to stop.

---
