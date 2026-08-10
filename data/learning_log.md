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
