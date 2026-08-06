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
