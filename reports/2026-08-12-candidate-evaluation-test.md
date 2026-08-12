# Candidate Evaluation — method test, 6 scout survivors

**2026-08-12 · STANDALONE METHOD TEST — NOT a weekly sweep memo.**
Deliberately named outside the `YYYY-MM-DD-council-memo.md` pattern so
`journal`'s reconciliation does not mistake it for a sweep. No `journal`
session-start run preceded it, no position report leads it, no scorecard,
no open-items pull. Nothing here has been executed or should be treated as
a sweep decision.

This is structured synthesis of this system's own agents' analysis. It is
not investment advice from a licensed advisor.

**Inputs used, none fetched by this agent:** valuation agent output against
snapshot `data/cache/snapshots/20260812T001709.json`; macro-regime agent
output against the same snapshot (regime as of 2026-08-10);
`data/portfolio.json` (last_updated 2026-08-04); `data/investor_profile.json`;
`OPEN_ITEMS.md`.

**Capital status, applied per Step 3 only:** no confirmed idle cash exists
(`portfolio.json` avanza-isk cash = 0, user-confirmed 2026-08-11). This
appears in execution notes and nowhere else. It has not been allowed to
touch a single ACTION or CONVICTION below.

---

## Standing portfolio facts these six were judged against

Figures from `portfolio.json`, priced 2026-08-04/08-06 — approximate, not
a fresh statement.

- **Individual-stock sleeve ≈ 28,372 SEK**, seven names: SHB-A 146.80,
  INVE-A 2,047, VOLV-B 4,802.20, ATCO-B 4,781.70, AZN 7,727.50, ALFA
  5,101.20, ABB 3,765.60. Industrials + financials ≈ 65% of it — rated
  **ACT** by the portfolio agent's own scorecard on 2026-08-11.
- **Avanza Global ≈ 119,999 SEK**, roughly 56% of a ~214k SEK portfolio.
  Broad global index; it certainly carries the three US mega-caps below at
  meaningful weight. *The exact per-name weights have never been fetched
  and are deliberately not asserted here* — see the denominator problem
  below, which is where this matters.
- **Medium tier is structurally underweight.** Target 30% of portfolio
  (~64k SEK); actual individual-stock sleeve ~28k SEK. Future contributions
  (1,000–3,000 SEK/mo) are the intended filler. So "which name deserves the
  next 3,000 SEK" is a live, recurring question even with zero cash today.
- **Position cap 15%** of portfolio, per `investor_profile.json`. None of
  the six comes close at any realistic size — concentration objections
  below are about *sector*, never about the single-position rule.
- **AZN.ST was bought explicitly as a diversifier** away from the
  industrials/tech concentration (its `thesis_narrative` says so directly).
  That intent is a standing constraint on what earns the next slot.

### The denominator problem, named once up front

It recurs in three of the six evaluations, so it is stated here rather
than re-argued each time. **Sector concentration measured against the
individual-stock sleeve and measured against total investable capital give
opposite signs for US mega-cap tech.**

- *Sleeve denominator:* the sleeve is 65% Nordic industrials/financials and
  holds zero US technology. AMZN/GOOGL/META are pure diversifiers.
- *Total-portfolio denominator:* Avanza Global at ~56% of the portfolio
  already delivers heavy US mega-cap exposure. On this reading the sleeve's
  industrial tilt is a *counterweight* to the index, and adding US mega-caps
  makes total concentration worse, not better.

Both readings are internally coherent. The system has not pinned which one
governs — this is the same failure class as **S12** (`OPEN_ITEMS.md`), one
level over from the "investable capital" denominator conflict that produced
three different crypto weights on 2026-08-11. Where it changes a call
below, it is named in that call's Chairman reasoning and it caps size, not
direction.

---

# 1. AMZN — Amazon.com

**Evidence:** Fair (valuation). Trailing P/E 21.9x, **forward P/E 26.4x —
the multiple expands forward**, PEG 1.48 on 19.6% revenue growth. Price
$278.09 in a $196.00–$287.20 52-week range = **90th percentile**. Macro:
USD-denominated, high beta, positive real US 10y ~+0.99% is a live
headwind to further multiple expansion on long-duration names.
`interest_expense` missing (all six).

### The five independent views

**The Contrarian**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** A forward P/E *above* trailing means consensus expects
  earnings to fall or be spent — and the market is paying the 90th
  percentile of a year's range for that. Buying a rising multiple at a
  rising price is paying twice for the same optimism.
- **KEY RISKS:** AWS reacceleration is real and the capex is building the
  thing that reaccelerates; sitting out means missing it entirely.
- **WHAT WOULD CHANGE MY MIND:** Forward P/E crossing back below trailing —
  that single flip inverts my whole objection.

**First Principles**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** Strip the name away and this is: pay 26.4x next
  year's earnings for 19.6% top-line growth, with no free-cash-flow series
  available (CLAUDE.md's documented Yahoo gap) and no interest-coverage
  read. For a business whose entire current story is capital intensity,
  having no FCF trend is not a minor gap — it is the missing variable.
- **KEY RISKS:** Judging a capex-heavy compounder on P/E is the wrong lens;
  the answer might be obvious on FCF and I cannot see it.
- **WHAT WOULD CHANGE MY MIND:** A real multi-year FCF series from the
  company's own cash flow statement (the `pdf` skill can extract it).

**The Expansionist**
- **ACTION:** Buy · **CONVICTION:** Low
- **MAIN REASONING:** Unconstrained, the maximum-upside case is that AWS
  plus advertising are two secular businesses hidden inside a retailer's
  multiple, and 19.6% growth at this scale is genuinely rare. If you are
  buying a 10-year hold, the difference between the 60th and 90th
  percentile of one 52-week range is noise.
- **KEY RISKS:** "Percentile is noise over ten years" is true and is also
  the sentence that precedes every bad entry.
- **WHAT WOULD CHANGE MY MIND:** Evidence that growth is decelerating
  rather than being reinvested — that would make the high multiple a
  structural problem, not a timing one.

**The Outsider**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** Described cold: a very large, very well-known company,
  currently priced near the top of everything it has traded at this year,
  where the people forecasting next year expect it to earn *relatively
  less* than it does now. Nothing about that combination says "act today."
- **KEY RISKS:** "Everyone knows it" is not an argument against owning it.
- **WHAT WOULD CHANGE MY MIND:** The price coming meaningfully off its high
  without the business changing.

**The Executor**
- **ACTION:** Watch · **CONVICTION:** High
- **MAIN REASONING:** There is nothing to execute. Zero free cash, a
  candidate at the 90th percentile of its range, and no trigger. The
  concrete Monday action is to set the trigger, not place an order.
- **KEY RISKS:** A trigger nobody checks is the same as no trigger.
- **WHAT WOULD CHANGE MY MIND:** Nothing about AMZN — only a change in
  what is available to deploy and a better price.

### Chairman

The disagreement that matters is Expansionist vs. Contrarian, and it is
**not** about whether Amazon is a good business — all five voices concede
it is. It is about whether an expanding forward multiple at a 90th-
percentile price is a timing detail or a signal. I weight the Contrarian,
for a specific reason the Expansionist's ten-year framing cannot dissolve:
this portfolio's medium tier gets filled at ~1,000–3,000 SEK a month, so
entry price is not a rounding error — it is most of what a small,
slow-accumulated position's return will be determined by. First
Principles' point compounds it: the one metric that would justify paying up
for a capex-heavy business is FCF, and we structurally cannot see it.

```
FINAL ACTION: Watch
CONVICTION: Medium
WHY: Weighted the Contrarian over the Expansionist. Forward P/E (26.4x)
     above trailing (21.9x) at the 90th percentile of the 52-week range is
     paying for optimism twice, and PEG 1.48 gives no growth-adjusted
     discount to offset it. First Principles' gap is decisive as a
     secondary: for a business defined by capital intensity, no multi-year
     FCF series exists in free data, so the metric that would justify the
     premium is unavailable. Not a quality objection — a price-and-
     visibility one.
KEY RISKS / BREAK CONDITION: Converts to Buy if (a) forward P/E falls back
     below trailing, or (b) price re-enters the lower half of its 52-week
     range with growth intact. Wrong if AWS reacceleration re-rates it from
     here and the entry never comes.
```
**Execution note:** nothing to fund; this is a monitoring call.

---

# 2. ASSA-B.ST — Assa Abloy B

**Evidence:** **Expensive** (valuation). Trailing P/E 24.5x on **3.3%
revenue growth**, PEG 1.7, D/E 64.1%. Market cap, forward P/E and P/S all
missing — valuation flagged reduced confidence. Macro: does not fight the
current regime, but walks straight back into the Nordic-industrials basket
AZN.ST was bought to diversify away from, on top of a restrictive Swedish
real policy rate (~+1.45%).

### The five independent views

**The Contrarian**
- **ACTION:** Reject · **CONVICTION:** High
- **MAIN REASONING:** 24.5x for 3.3% growth is a quality premium being paid
  in full, in advance, with no growth to grow into it. The assumption to
  attack is that Assa Abloy's compounding reputation entitles it to the
  multiple regardless of the current growth rate — that is exactly how
  quality names de-rate.
- **KEY RISKS:** It has held a premium multiple for a decade; betting on
  de-rating has been a losing trade repeatedly.
- **WHAT WOULD CHANGE MY MIND:** Revenue growth reaccelerating to
  high-single-digits, which would make PEG 1.7 a trough reading.

**First Principles**
- **ACTION:** Reject · **CONVICTION:** Medium
- **MAIN REASONING:** Rebuilt from scratch, the question is: what does
  adding this to *this* portfolio do? It adds a Swedish industrial with
  64% leverage to a sleeve that is 65% Swedish industrials and financials,
  at a full price. The portfolio-fit answer and the valuation answer point
  the same way independently, which is rare and worth respecting.
- **KEY RISKS:** Assa Abloy's cycle is construction/renovation, genuinely
  different from Volvo's truck cycle or ABB's automation cycle — "Nordic
  industrial" may be too coarse a bucket.
- **WHAT WOULD CHANGE MY MIND:** A real risk-factor classification (V2
  Roadmap Phase 4) showing its cycle is uncorrelated with the existing
  four. Sector labels are not risk factors.

**The Expansionist**
- **ACTION:** Watch · **CONVICTION:** Low
- **MAIN REASONING:** The strongest bull case, unconstrained: Assa Abloy is
  a serial-acquisition compounder with genuine pricing power in an
  installed-base business, and 3.3% is a trough organic rate, not the
  through-cycle rate. Buying compounders only when the growth optics are
  good is how you never own them. But even at maximum size and maximum
  optimism, this points at *the same* Nordic industrial exposure the
  portfolio is already saturated with — the aggressive version and the
  modest version agree on direction, which for once is a reason to stop.
- **KEY RISKS:** Missing a decade-long compounder over a one-year multiple.
- **WHAT WOULD CHANGE MY MIND:** A materially lower entry, or the
  industrials concentration being resolved first.

**The Outsider**
- **ACTION:** Reject · **CONVICTION:** Medium
- **MAIN REASONING:** Told cold: this company is growing about 3% a year
  and costs about 25 times its earnings, while carrying meaningful debt —
  and the person buying it already owns four other Swedish machine
  companies. I would ask why this one, and I do not hear an answer specific
  to it.
- **KEY RISKS:** Cold reading misses durable-franchise quality that does
  not show up in a growth rate.
- **WHAT WOULD CHANGE MY MIND:** A reason it is better than the four
  already held, stated in one sentence.

**The Executor**
- **ACTION:** Reject · **CONVICTION:** High
- **MAIN REASONING:** Constraints on: no cash, missing forward P/E and
  market cap so it cannot even be sized properly, and it duplicates an
  ACT-rated concentration. There is no version of Monday morning where this
  is the trade.
- **KEY RISKS:** None to the decision itself.
- **WHAT WOULD CHANGE MY MIND:** Nothing at this price.

### Chairman

**This one is genuinely one-sided and I will say so rather than
manufacture tension.** Four voices reject; the Expansionist — whose job is
to find the maximum-upside case — built the strongest steelman available
(installed-base compounder, trough organic growth) and *still* landed on
Watch, explicitly because the aggressive version points at the same
saturated exposure as the modest one. When the bull case's own logic
terminates in the bear case's conclusion, that is a real result, not a
consensus artifact. Two independent disqualifiers each sufficient alone:
PEG 1.7 on 3.3% growth is a full price for no growth, and this is the
exact exposure AZN.ST was bought to dilute.

```
FINAL ACTION: Reject
CONVICTION: High
WHY: The Expansionist's own maximum-upside case terminates in the same
     objection as the bear case — more Nordic industrial exposure into a
     sleeve already 65% industrials/financials and rated ACT. On top of
     that, valuation calls it outright Expensive (PEG 1.7 on 3.3% growth,
     D/E 64.1%), with market cap, forward P/E and P/S all missing, so it
     could not be underwritten cleanly even if the fit were right. Two
     independent disqualifiers, either sufficient.
KEY RISKS / BREAK CONDITION: Wrong if organic growth reaccelerates to
     high-single-digits and PEG 1.7 proves a trough reading, or if a real
     risk-factor classification (V2 Phase 4) shows its construction/
     renovation cycle is genuinely uncorrelated with Volvo/ABB/Alfa Laval/
     Atlas Copco. Reopen on either, not before.
```
**Execution note:** none — nothing to fund and nothing to fund it with.

---

# 3. GOOGL — Alphabet

**Evidence:** **Cheap** (valuation). PEG 0.97 — lowest of the six — on
24.2% revenue growth and 34.0% operating margin, trailing P/E 17.3x.
**Caveat carried by valuation itself:** net margin 54.8% far exceeds
operating margin 34.0%, likely non-operating gains inflating net income, so
**trailing P/E is not trustworthy and forward P/E 23.3x is the real read.**
No 52-week percentile was reported for this name. Macro: USD, high beta,
positive real 10y headwind to long-duration multiples.

### The five independent views

**The Contrarian**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** The "cheap" verdict and the PEG 0.97 that generated
  it are both computed off a trailing P/E that valuation *itself* says is
  contaminated by non-operating gains. Strip that out and you are paying
  23.3x forward — respectable, not cheap. The screen surfaced this name on
  a number the analyst has already disowned.
- **KEY RISKS:** 23.3x for 24% growth and 34% operating margins is still a
  reasonable price; I may be rejecting a good entry over a labelling issue.
- **WHAT WOULD CHANGE MY MIND:** A clean PEG recomputed on forward earnings
  rather than contaminated trailing earnings.

**First Principles**
- **ACTION:** Buy · **CONVICTION:** Medium
- **MAIN REASONING:** Rebuild it: a business growing 24% with a 34%
  operating margin, priced at 23.3x forward earnings. That is a fair-to-good
  price for genuinely excellent economics, independent of what the screen
  called it. Its search/advertising/cloud cash generation correlates with
  nothing in this portfolio's Nordic industrial sleeve.
- **KEY RISKS:** AI disruption of search is the one existential question,
  and no free data source can price it.
- **WHAT WOULD CHANGE MY MIND:** Evidence of search revenue actually
  decelerating rather than the narrative that it might.

**The Expansionist**
- **ACTION:** Buy · **CONVICTION:** Medium
- **MAIN REASONING:** Maximum-upside version: this is the cheapest
  large-scale AI infrastructure owner that also owns the distribution
  (Search, Android, YouTube, Cloud, TPUs) — an integration nobody else has.
  At full size that is a core position, not a nibble, and 23.3x forward
  would look absurd in hindsight if the integration converts.
- **KEY RISKS:** Regulatory break-up risk is the specific thing that
  destroys the integration argument, and it is live.
- **WHAT WOULD CHANGE MY MIND:** A structural remedy actually ordered
  rather than argued.

**The Outsider**
- **ACTION:** Watch · **CONVICTION:** Low
- **MAIN REASONING:** Cold: I am told this is the cheapest of six, then told
  in the same paragraph that the number making it cheapest is unreliable,
  and I am not told whether the price is high or low compared to its own
  recent history — a fact that was reported for three of the other five.
  I would want the missing number before agreeing.
- **KEY RISKS:** Waiting on one field while a good price passes.
- **WHAT WOULD CHANGE MY MIND:** The 52-week position. It is in the
  snapshot already; it just was not reported.

**The Executor**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** Concrete Monday action: pull GOOGL's 52-week
  percentile out of `20260812T001709.json` — it costs one lookup, no fetch
  — and recompute PEG on forward earnings. Both are minutes of work and
  both are load-bearing. No cash to deploy this week regardless.
- **KEY RISKS:** The lookup gets deferred forever and this stalls.
- **WHAT WOULD CHANGE MY MIND:** The two numbers.

### Chairman

Two Buys, three Watches — and I am not counting. The disagreement that
decides this is Contrarian/Outsider vs. First Principles, and it is
narrower than it looks: **nobody thinks 23.3x forward for 24% growth is a
bad price.** The split is over *corroboration*. First Principles is right
that the business economics justify the multiple on their own. But the
single reason this name outranked the others on the screen — PEG 0.97 —
was computed off a trailing P/E the valuation agent explicitly disowned in
the same breath, and the one independent check that would corroborate
cheapness from a different direction, the 52-week position, was reported
for AMZN, LUND-B and META and silently omitted here.

That is not a reason to reject Alphabet. It is a reason not to convert a
contaminated input into a purchase in the same sweep it was flagged. The
gap is one lookup in a file already on disk, and it is genuinely
decision-flipping: a GOOGL trading in the lower half of its range with 24%
growth and 34% operating margins is a Buy on this evidence, and one at the
90th percentile is AMZN's situation with a better margin profile.

```
FINAL ACTION: Watch
CONVICTION: Medium
WHY: Weighted the Contrarian and Outsider over First Principles/
     Expansionist — not on business quality, which all five concede, but on
     corroboration. PEG 0.97 rests on a trailing P/E valuation itself calls
     untrustworthy (net margin 54.8% vs operating 34.0%), and the one
     independent cross-check — 52-week position — was reported for three
     other names in this set and omitted for this one. Converting a
     flagged-unreliable input straight into a buy is the exact failure this
     system exists to prevent.
KEY RISKS / BREAK CONDITION: Converts to Buy the moment two numbers are
     produced from the existing snapshot — GOOGL's 52-week percentile in
     the lower half of its range, and PEG recomputed on forward (not
     trailing) earnings still under ~1.3. If the percentile comes back near
     its highs, this stays Watch. Wrong if it re-rates upward while the
     lookup sits undone.
```
**Execution note:** the resolving step needs no capital and no fetch — one
read of `data/cache/snapshots/20260812T001709.json`. Do it before the next
sweep, not during it.

---

# 4. HEXA-B.ST — Hexagon B

**Evidence:** Fair (valuation), with two flags. Trailing P/E 11.2x looks
cheap but **forward P/E jumps 62% to 18.1x** (PEG 1.22) — valuation would
not call that clean cheapness versus an expected earnings step-down or a
one-off. Separately, **P/S 47x and P/B 46x in the snapshot are implausible**
— likely a revenue unit/currency mismatch — and were correctly excluded
from the verdict. Macro: Nordic industrial basket, restrictive Swedish real
policy rate.

### The five independent views

**The Contrarian**
- **ACTION:** Reject · **CONVICTION:** Medium
- **MAIN REASONING:** A 62% forward multiple jump is not a nuance, it is
  the headline: consensus expects earnings to drop by roughly a third. The
  assumption everyone is making is that this is a data artifact or a
  one-off — it may simply be an accurate forecast of deterioration.
- **KEY RISKS:** If it *is* a one-off (divestment gain, tax item), I am
  rejecting a genuinely cheap industrial-technology asset.
- **WHAT WOULD CHANGE MY MIND:** The actual reconciliation from the
  company's own quarterly report, showing whether trailing earnings
  contained a non-recurring item.

**First Principles**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** Two of the four standard valuation inputs (P/S, P/B)
  are known-broken in this snapshot, and the two that survive tell opposite
  stories 62% apart. Stripped of framing, this candidate has not actually
  been valued yet — it has been *screened*. Those are different things and
  only one of them supports a purchase.
- **KEY RISKS:** Waiting for perfect data on a name whose direction is
  already clear enough.
- **WHAT WOULD CHANGE MY MIND:** A clean snapshot with plausible P/S and
  P/B, plus an explanation of the forward gap.

**The Expansionist**
- **ACTION:** Buy · **CONVICTION:** Low
- **MAIN REASONING:** Unconstrained: Hexagon is not a machine company. It
  is measurement, sensors, metrology and design/simulation software — a
  recurring-revenue technology business wearing an industrial label. If the
  62% gap is a one-off and the real forward figure is nearer trailing, this
  is the only name in the set that is both cheap *and* structurally
  different from what the portfolio owns.
- **KEY RISKS:** "It's really a software company" is a story, and the
  broken P/S is precisely the metric that would test it.
- **WHAT WOULD CHANGE MY MIND:** A corrected P/S confirming software-like
  revenue economics rather than industrial ones.

**The Outsider**
- **ACTION:** Watch · **CONVICTION:** High
- **MAIN REASONING:** Cold, this is simple: two of the numbers I was handed
  are described as impossible, and the two remaining ones disagree with each
  other by more than half. No one should buy anything on that. This has
  nothing to do with the company and everything to do with not having read
  it yet.
- **KEY RISKS:** None to waiting.
- **WHAT WOULD CHANGE MY MIND:** Numbers that are not flagged as broken.

**The Executor**
- **ACTION:** Watch · **CONVICTION:** High
- **MAIN REASONING:** Concrete action exists and it is not a trade: this is
  a named candidate for `swedish-equity-review`, the skill built exactly for
  Nordic names, which has now been the system's recommended next step for
  five consecutive sweeps without running (P6). Running it on a candidate
  is cheaper than running it retroactively on something already bought.
- **KEY RISKS:** Adding a sixth item to a queue that already has five
  unexecuted ones.
- **WHAT WOULD CHANGE MY MIND:** Nothing — the review is the action.

### Chairman

The tension worth resolving is Expansionist vs. Contrarian on what Hexagon
*is*. The Expansionist raises the one genuinely interesting point in this
evaluation: if Hexagon is metrology and design software rather than
machinery, then the blanket "Nordic industrial, already saturated"
objection that kills ASSA-B does **not** automatically apply here, and this
would be a diversifier inside a sector label that looks like duplication.
That deserved a hearing and it is why this does not get ASSA-B's Reject.

But the Expansionist's own test defeats it for now: the metric that would
confirm software-like economics is P/S, and P/S is one of the two numbers
in this snapshot known to be wrong. Meanwhile the Contrarian's point stands
unanswered — a 62% forward multiple expansion means consensus is forecasting
a material earnings decline, and nothing available distinguishes "one-off
in the trailing figure" from "deterioration ahead." Two of four valuation
inputs broken and the other two 62% apart is not a valuation. Note the
difference from ASSA-B, which is deliberate: **ASSA-B fails on the numbers
we have; HEXA-B fails on numbers we do not have.** Those warrant different
verdicts.

```
FINAL ACTION: Watch
CONVICTION: Medium
WHY: Weighted the Expansionist's framing enough to withhold a Reject — if
     Hexagon is genuinely metrology/design software rather than machinery,
     the sector-duplication objection that disqualifies ASSA-B does not
     transfer, and it would be a real diversifier. But the Expansionist's
     own test (P/S confirming software-like revenue economics) cannot run:
     P/S 47x and P/B 46x are known-broken in this snapshot. With those two
     out and trailing vs forward P/E 62% apart, this candidate has been
     screened, not valued. The Contrarian's unanswered question — is the
     forward jump a one-off or a forecast of decline — is the crux.
KEY RISKS / BREAK CONDITION: Resolve by running `swedish-equity-review` on
     HEXA-B.ST (the skill exists for exactly this) plus a reconciliation of
     the trailing-vs-forward earnings gap from the company's own quarterly
     report via the `pdf` skill. Converts to Buy if the gap proves a
     non-recurring item AND corrected P/S supports the software-economics
     read. Reverts to Reject if the forward figure reflects genuine
     deterioration. Wrong either way if the data is never fixed and this
     just sits.
```
**Execution note:** the unblocking step is analysis, not capital. It queues
behind ATCO-B/ALFA/ABB, which need the same review retroactively on money
already spent — those outrank a candidate.

---

# 5. LUND-B.ST — L E Lundbergföretagen B

**Evidence:** Fair (valuation). Trailing P/E 10.4x and P/B ~1.06x (near
book) look inexpensive, but price sits at the **86.5th percentile** of its
52-week range and forward P/E is missing. Multi-year revenue history in the
snapshot is stale (2010–2013) and was correctly not used. Macro: Nordic
conglomerate, same basket AZN.ST was bought to diversify away from.

### The five independent views

**The Contrarian**
- **ACTION:** Reject · **CONVICTION:** High
- **MAIN REASONING:** The assumption to break is that P/E 10.4x means
  anything at all here. This is a holding company: its P/E is an accounting
  artifact of consolidated subsidiary earnings, exactly as `portfolio.json`
  already records for INVE-A — "the 4.71x P/E is an accounting artifact and
  must not be read as cheap." The system has written that lesson down once
  and is being offered the chance to repeat it with a different ticker.
- **KEY RISKS:** P/B ~1.06 is a more honest holding-company signal than P/E
  and it is not obviously expensive.
- **WHAT WOULD CHANGE MY MIND:** An actual NAV discount figure. Not a proxy.

**First Principles**
- **ACTION:** Reject · **CONVICTION:** High
- **MAIN REASONING:** Ask what is actually being bought. Lundbergs is a
  wrapper around Swedish industrials, forestry, real estate and — via its
  large Industrivärden and Handelsbanken stakes — assets this portfolio
  *already holds directly*: Handelsbanken (SHB-A) and, through
  Industrivärden, Volvo. Buying it layers a second holding-company wrapper
  onto a sleeve that already contains one (INVE-A) plus its underlying
  exposures, and adds a management fee layer for the privilege.
- **KEY RISKS:** Lundbergs' real-estate and forestry assets are genuinely
  absent from the current portfolio.
- **WHAT WOULD CHANGE MY MIND:** A look-through analysis showing the
  overlap with SHB-A/INVE-A/VOLV-B is small. I doubt it is.

**The Expansionist**
- **ACTION:** Watch · **CONVICTION:** Low
- **MAIN REASONING:** The maximum-upside case is specific and real: buying a
  disciplined family-controlled compounder at a wide discount to NAV is one
  of the few structurally repeatable edges in Nordic equities — you get the
  underlying assets for less than they are worth and the discount can close
  on top of asset growth. P/B ~1.06 hints the discount is not wide today.
- **KEY RISKS:** Discounts can persist for decades; "cheap on NAV" is not a
  catalyst.
- **WHAT WOULD CHANGE MY MIND:** A confirmed wide (>25%) NAV discount would
  make this a genuine value case rather than a duplication.

**The Outsider**
- **ACTION:** Reject · **CONVICTION:** Medium
- **MAIN REASONING:** Explained cold: this is a company whose business is
  owning shares in other companies, and the buyer already owns shares in
  some of those same companies, and also already owns a different company
  whose business is owning shares in other companies. That is three layers
  doing one job. And it is near its yearly high.
- **KEY RISKS:** Professional capital allocation has value the cold reading
  dismisses.
- **WHAT WOULD CHANGE MY MIND:** A reason this allocator beats the ones
  already owned.

**The Executor**
- **ACTION:** Reject · **CONVICTION:** High
- **MAIN REASONING:** It cannot be sized or underwritten: forward P/E
  missing, revenue history stale by twelve years, NAV discount unobtainable
  (S6, open and blocking half of P5 already). No cash, no metric, no slot.
- **KEY RISKS:** None to the decision.
- **WHAT WOULD CHANGE MY MIND:** S6 closing.

### Chairman

The disagreement that matters is the Expansionist's, and it is the only one
here worth real weight: buying a family-controlled compounder at a wide NAV
discount is a genuine, repeatable edge, and if that discount were confirmed
wide this would be a legitimate value case rather than a duplication.
I am rejecting it anyway, on grounds independent of the discount.

**Two blockers, and closing the second would not clear the first.** First
Principles' overlap point is structural: Lundbergs' NAV is substantially
Industrivärden, Handelsbanken, Holmen, Hufvudstaden and Indutrade, and this
portfolio already owns Handelsbanken directly, holds Investor A as an
existing holding-company wrapper, and holds Volvo — an Industrivärden
position — directly. Even at a 30% NAV discount, that is paying to
concentrate further into the exposure the scorecard rates ACT and that
AZN.ST was explicitly bought to dilute. Second, S6 (`OPEN_ITEMS.md`) means
the NAV discount cannot be obtained at all, which is *already* the reason
INVE-A's thesis is recorded as plausible-but-not-testable. Adding a second
untestable holding-company position while the first one's blocker sits open
is not diversification; it is doubling an open item.

```
FINAL ACTION: Reject
CONVICTION: Medium
WHY: Weighted First Principles' look-through overlap over the
     Expansionist's NAV-discount edge, because the overlap objection is
     independent of the discount and survives it. Lundbergs' NAV is largely
     Industrivärden/Handelsbanken/Holmen/Hufvudstaden/Indutrade — this
     portfolio already holds SHB-A directly, VOLV-B directly, and INVE-A as
     an existing holding-company wrapper. Separately, the only metric that
     can value a holding company (NAV discount/premium) is unobtainable per
     open item S6, which is already why INVE-A's own thesis is untestable;
     a second untestable wrapper compounds an open item rather than
     resolving one. P/E 10.4x here is an accounting artifact, the identical
     trap `portfolio.json` already documents for INVE-A's 4.71x. Price at
     the 86.5th percentile removes any urgency argument.
KEY RISKS / BREAK CONDITION: Reopen only if BOTH conditions hold — S6
     closes with a real NAV discount figure (Lundbergs' own annual report
     via the `pdf` skill, or its IR page) showing a wide discount, AND the
     sleeve's industrials/financials concentration is materially reduced so
     the look-through overlap no longer compounds an ACT rating. Wrong if
     the discount is genuinely wide and closes while this sits — that is a
     real, acknowledged cost of the call.
```
**Execution note:** none. Note that closing S6 has independent value for
INVE-A regardless of this rejection — that is the higher-priority reason to
do it.

---

# 6. META — Meta Platforms

**Evidence:** **Cheap** (valuation). PEG 0.89 — lowest in the set — on
**28% revenue growth, the highest of the six**, and 34.8% operating margin.
**Forward P/E 17.2x falls below trailing 22.6x — the only one of the six
where the multiple compresses forward.** Price $594.92 in a $520.26–$796.25
range = **27th percentile**. Macro: USD, high beta (1.24–1.45), positive
real 10y headwind to long-duration multiples; index-overlap concentration
point applies.

### The five independent views

**The Contrarian**
- **ACTION:** Watch · **CONVICTION:** Medium
- **MAIN REASONING:** Strong fundamentals plus a price 25% off its high is
  not "cheap" — it is a market disagreeing with the fundamentals we can
  see, and we have no access to *why*. A forward multiple below trailing
  can equally mean consensus has not cut estimates yet. Every value trap
  looks exactly like this on a snapshot.
- **KEY RISKS:** If the drawdown is sentiment rather than substance, this
  is the best entry in the set and I talk the user out of it.
- **WHAT WOULD CHANGE MY MIND:** An identifiable, bounded reason for the
  drawdown — a specific capex guide or regulatory event — rather than an
  unexplained gap between price and fundamentals.

**First Principles**
- **ACTION:** Buy · **CONVICTION:** Medium
- **MAIN REASONING:** Rebuilt from nothing: pay 17.2x next year's earnings
  for a business growing revenue 28% at a 34.8% operating margin. That is
  the arithmetic, and it is the best in this set by a clear margin without
  needing a story. The forward multiple compressing means the earnings are
  expected to *arrive*, which is the opposite of AMZN's situation.
- **KEY RISKS:** Meta has previously spent a large share of that operating
  margin on projects with no revenue attached; margin is a choice
  management can reverse.
- **WHAT WOULD CHANGE MY MIND:** A capex/opex step-up that consumes the
  forward earnings the 17.2x depends on.

**The Expansionist**
- **ACTION:** Buy · **CONVICTION:** High
- **MAIN REASONING:** Constraints off: 28% growth at a 34.8% operating
  margin, priced at 17.2x forward, at the 27th percentile of its own range,
  is the setup you size *up* into, not nibble at. Roughly 4 billion users
  and an advertising engine that converts AI spend directly into
  measurable revenue — this is the rare case where the aggressive version
  and the cautious version point the same direction, differing only in size.
- **KEY RISKS:** High beta means a market drawdown hits this harder than
  anything in the current portfolio.
- **WHAT WOULD CHANGE MY MIND:** Evidence that the ad engine's growth is
  regulatory-capped rather than demand-capped.

**The Outsider**
- **ACTION:** Buy · **CONVICTION:** Medium
- **MAIN REASONING:** Cold and without priors: growing fastest of the six,
  earning the second-highest margin, priced at the bottom quarter of its own
  year, and the forecast says it will earn *more* next year relative to
  price. Of the six descriptions I was handed, this is the only one where
  every number points the same way.
- **KEY RISKS:** Being told a story is coherent is not the same as it being
  right; a cold reading cannot see what the market knows.
- **WHAT WOULD CHANGE MY MIND:** Learning the price fell for a reason that
  invalidates one of those numbers.

**The Executor**
- **ACTION:** Buy · **CONVICTION:** Medium
- **MAIN REASONING:** Practically: this is a single Avanza order in USD
  inside the existing ISK, no new account, no new wrapper, no tax event. At
  a 2,000–3,000 SEK size it is ~1% of the portfolio and nowhere near the
  15% single-position cap. There is no cash today, so this is a
  next-contribution instruction, not a Monday trade.
- **KEY RISKS:** FX conversion cost on a small USD order and Avanza's
  courtage on a sub-3,000 SEK ticket eat a real percentage.
- **WHAT WOULD CHANGE MY MIND:** Courtage/spread proving material at this
  ticket size — which argues for one larger purchase, not several small ones.

### Chairman

Four Buys, one Watch, and the Watch is the one I have to answer rather than
outvote. The Contrarian's objection is the strongest argument in this entire
document: strong fundamentals at the 27th percentile of a 52-week range
means the market is actively disagreeing with the numbers in our snapshot,
and free data cannot tell us why. That is exactly the shape of a value trap
and it must not be waved through.

What answers it, partially: the direction of the forward multiple. **Of the
six candidates, META is the only one where the forward multiple compresses
below trailing** — consensus expects earnings to grow into the price. A
classic value trap has the opposite signature, the AMZN signature: a forward
multiple *expanding* as estimates get cut. So the two independent signals we
do have — price position and estimate direction — corroborate each other
rather than conflict. That is more than any other name here offers, and it
is why this is a Buy and not a Watch.

What it does not answer, and what caps this at Medium rather than the
Expansionist's High: we still cannot name the reason for the drawdown, and
the macro lens's positive-real-10y headwind lands hardest on precisely this
profile. On the denominator problem stated at the top — Avanza Global
already carries META — the honest reading is that this caps *size*, not
direction: on the sleeve denominator it is the sleeve's first non-Nordic,
non-industrial growth exposure; on the total-portfolio denominator it is
incremental duplication. A ~2,000–3,000 SEK position is defensible under
both readings simultaneously, which is precisely why the size, not the
call, is where the unresolved denominator gets absorbed.

```
FINAL ACTION: Buy — small, ~2,000–3,000 SEK (~1% of portfolio)
CONVICTION: Medium
WHY: Answered the Contrarian rather than outvoting him. His value-trap
     objection is real — 27th percentile of the 52-week range means the
     market disagrees with our fundamentals and free data cannot say why.
     What defeats it here specifically: META is the only one of the six
     whose forward P/E (17.2x) falls BELOW trailing (22.6x). A value trap
     has the opposite signature — expanding forward multiples as estimates
     get cut. Price position and estimate direction therefore corroborate
     each other instead of conflicting, on top of the set's highest revenue
     growth (28%), a 34.8% operating margin and the lowest PEG (0.89). Held
     at Medium not High because the drawdown remains unexplained and the
     positive real US 10y is a direct headwind to this exact profile. Size
     kept small because the sleeve-vs-total-portfolio denominator question
     (S12 class) is unresolved and a ~1% position is defensible under both
     readings.
KEY RISKS / BREAK CONDITION: Wrong if the forward multiple compression
     reflects estimates that have not yet been cut rather than earnings
     that will arrive — watch for the forward P/E rising toward or above
     trailing on the next snapshot, which inverts the entire case. Also
     wrong if a capex/opex step-up consumes the forward earnings the 17.2x
     depends on. Hard stop on adding: no second tranche until a reason for
     the 25% drawdown from the high is actually identified.
```
**Execution note (Step 3 — does not affect Action or Conviction above):**
no idle capital is confirmed in the portfolio this session
(`portfolio.json` avanza-isk cash = 0, user-confirmed 2026-08-11). **Flag
for the next monthly contribution.** Two execution details for whoever
funds it: get a broker-confirmed ISK cash balance first rather than
trusting a computed figure — that premise has failed twice already
(2026-08-10, 2026-08-11) — and check courtage plus FX spread on a sub-3,000
SEK USD ticket, since at this size transaction cost is a material fraction
of the first year's expected return. No earnings-date collision check was
possible: `scripts/fetch_calendar.py` is still broken (S3).

---

## Post-hoc note — deliberately outside the six evaluations

The six above were run independently, as instructed: no candidate's verdict
was formed with reference to any other. The following is written *after*
all six were complete and formed no part of any of them. It is recorded
separately so the independence of the evaluations is not retroactively
compromised.

Read together, the six sort into three distinct failure or success modes,
and the modes are more informative than the verdicts:

1. **Priced for optimism** — AMZN, ASSA-B. Both carry a full price against
   their own growth rate. Different severity (AMZN Fair, ASSA-B Expensive),
   same shape.
2. **Cannot be underwritten** — GOOGL, HEXA-B, LUND-B. Each blocked by a
   *specific, nameable* missing number: GOOGL's 52-week percentile and a
   forward-based PEG (both derivable from a file already on disk),
   HEXA-B's corrected P/S plus the trailing-forward reconciliation, LUND-B's
   NAV discount (S6). Three of six candidates blocked on data quality rather
   than on merit is itself the finding.
3. **Corroborated** — META alone. The only name where two independent
   signals (price position, estimate direction) agree.

If a single follow-up gets done, it is the GOOGL lookup: it needs no fetch,
no capital and no new capability, and it is the only one of the five
non-Buys that could convert to a Buy within one sweep.

---

## Learning notes

- **A forward P/E above trailing and one below trailing are opposite
  statements, and this test turned on that distinction twice.** Trailing
  P/E uses earnings already reported; forward uses what analysts expect
  next year. When forward is *higher* (AMZN: 26.4x vs 21.9x), the market
  expects earnings to shrink or be spent — you are paying more per unit of
  future profit than of past profit. When forward is *lower* (META: 17.2x
  vs 22.6x), earnings are expected to grow into the price. This is why
  META's low price in its range reads as an opportunity while AMZN's high
  price reads as a warning: the multiple's direction tells you which way
  estimates are moving, and a genuine value trap almost always shows the
  AMZN signature, not the META one.
- **PEG is only as good as the P/E underneath it, which is why GOOGL's
  0.97 did not earn a Buy.** PEG divides P/E by the growth rate to ask
  whether a high multiple is justified by fast growth. But if the P/E in
  the numerator is contaminated — GOOGL's net margin (54.8%) far exceeds
  its operating margin (34.0%), meaning non-operating gains are inflating
  net income and deflating the P/E — then the PEG inherits the
  contamination and looks cheaper than reality. The screen ranked GOOGL
  best of six on a number the valuation agent disowned in the same
  paragraph. A ratio is not evidence; the inputs to the ratio are.
- **A holding company's P/E is an accounting artifact, not a valuation.**
  LUND-B's 10.4x and INVE-A's 4.71x both look cheap and neither means
  anything: a holding company consolidates subsidiary earnings in ways that
  make the ratio incomparable to an operating business. The metric that
  actually works is NAV discount/premium — what the shares cost versus what
  the underlying assets are worth. This system cannot obtain it from any
  free source (open item S6), which is exactly why INVE-A's thesis is
  recorded as "plausible but not testable" and why LUND-B was rejected
  rather than scored.
- **"Concentrated" depends entirely on what you divide by, and that
  changed the sign of three calls here.** US mega-cap tech is a diversifier
  against the individual-stock sleeve (65% Nordic industrials/financials,
  zero US tech) and duplication against the total portfolio (Avanza Global
  is ~56% of everything and certainly holds all three names). Both
  computations are correct; they answer different questions. This is the
  same failure class as S12, where three defensible "investable capital"
  denominators produced three different crypto weights, one of which
  breached a trip-wire. The practical resolution used here: when the
  denominator is genuinely unsettled, let it govern *position size* rather
  than the buy/don't-buy decision — a size defensible under both readings
  does not require you to settle the argument first.
