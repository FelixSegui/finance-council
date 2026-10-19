# Open Items — single review surface

**This is the one place to look.**

- **P-items — your portfolio.** Things about your money. Only you close these;
  `meta` must never edit them.
- **S-items — the system.** Things about this tool. `meta` proposes; nothing
  self-applies; you approve by saying "apply S3".

Every Council memo pulls its open actions from this file and references items
by ID. Closed items move to the index at the bottom with a one-line
resolution — never deleted, full text in
`data/portfolio_history_archive.md`.

**Status values:** `open` · `blocked (on what)` · `decided — pending execution` · `closed`

**Blocking-question rule:** if an open item makes a conclusion untrustworthy,
the memo leads with it rather than burying it.

---

## This sweep's recommended emphasis

**Emphasis:** portfolio-tending, with a process-reliability note the user
should read even though it isn't capital-allocation work.

**Set by the 2026-10-19 review.** One decision is binary and dated
**tomorrow**: ABB.ST's SELL (4 shares, ~3,661.60 SEK) is not renewed under
the 2026-10-12 Chairman's own non-renewable rule — it is still executable
today as *last week's* decision, or it lapses outright at ABB's 2026-10-20
earnings print, and either is a legitimate outcome for the user to choose,
not the system. **P3 (PayPal -> SEK -> ISK) is unexecuted for an 11th-plus
consecutive sweep** and is now the funding constraint on four names at once
(gold tranche 2, the AZN.ST share, VICI if ABB is unsold, and NVDA — newly
promoted from HOLD-WATCH to BUY this sweep on a corrected process error, not
new merit). **D-c's crypto-sizing band was corrected onto the pinned
full-portfolio convention** (trim trigger moved from ~11,730 to ~14,080 SEK)
but stays unevaluable for a second consecutive sweep because no BTC price
was fetched — reading the live Avanza value of the BTC0E.AS position is a
two-minute check only the user can do.

**Read the process-reliability findings below even though they aren't
P-items.** This sweep found the most severe S27-family occurrence yet (the
scheduled prompt omitted `scripts/scout.py` entirely — a mandatory pipeline
stage, not a stale fact — caught only because the orchestrating session ran
it anyway) and a new, distinct failure mode: the 2026-10-12 sweep skipped
`journal` and `meta` entirely, with no self-catch inside that session at
all — it was invisible for a full week until this sweep's orchestrator
noticed a snapshot file newer than the latest log entry. Neither of these is
something more Council depth fixes; both point at the scheduled task's
stored prompt text (outside this repository) and at the absence of any
mechanical check that a sweep actually completed its mandatory steps before
ending. See S27 and the new S34 below.

Discovery stays a secondary watch item: scout ran VALID (74 candidates, 35
`source=new`, 2 genuinely first-seen — AZA.ST, FSLR), the frozen head
(APP/SNDK/NVDA/MA/V/TSM/VICI) continues to dominate top-10, and nothing this
sweep argues for more discovery depth over the dated decisions above.

---

## P — Portfolio items

### P1 — ETH cost basis
- **Status:** blocked (on user — needs time to dig it up)
- **Quantity is now CLOSED** (0.50185 ETH, confirmed 2026-08-03) and the
  position reprices from live data. What remains is only the cost basis.
- **Blocks:** any sale, any tax math, any return figure for the position.
  Swedish K4 requires cost basis; without it a sale can't be reported properly.
  **2026-08-17 note:** it now also blocks more than tax math — Council this
  session rejected "add more self-custody ETH" as a fallback crypto vehicle
  specifically because P1 being open means adding units makes an
  already-unsolvable tax problem permanently worse. See the Closed log for
  why this stayed a same-sweep correction rather than a new S-item.
- **Not urgent** unless you intend to sell.

### P3 — PayPal routing (the fee is now known; the route isn't)
- **Status:** decided — pending execution. **2026-08-17 (user):** "No I am
  not going to do that, we are counting with the 4% conversion rate." User
  declined the Revolut test-transfer option — selects **Option A**
  directly: convert the full PayPal balance (1,177.49 USD + 266.88 EUR)
  inside PayPal at the confirmed worst-case 4% spread (~563 SEK on the
  balance at disclosure, recurring on the ~750-1,000 EUR/~2mo inflow
  going forward), then route the converted SEK into the ISK.
- **Next step:** user executes the PayPal conversion + ISK transfer; once
  done, zero out the paypal holdings in `portfolio.json` and close this
  item.
- **Why it matters more than the amount suggests:** fee-drag problem
  (lever #2), and it recurs every ~2 months indefinitely, not a one-off.
- **2026-08-18 note:** still not executed; the Council's GOOGL candidate
  (#2 opportunity this sweep) is explicitly proposed to be funded from this
  conversion once it happens — see the 2026-08-18 memo.
- **2026-08-24 note:** still not executed, third consecutive sweep. The
  destination this note names is now stale — this sweep's Council memo
  reverses the funding target from GOOGL to META (forward multiple
  falling vs rising, PEG 0.82 vs 0.93, 28.0% vs 24.2% revenue growth). The
  conversion decision itself is unchanged; only what it eventually buys
  changed.
- **2026-08-31 note:** still not executed, fourth consecutive sweep. Capital
  check re-verified against this sweep's portfolio output: PayPal balance is
  now 14,093.69 SEK at current FX; genuinely deployable total (ISK cash +
  PayPal, excluding the tax reserve and checking float) is 25,381.69 SEK.
  Merits unchanged; the inflow keeps recurring regardless of when this
  executes.
- **2026-09-07 note:** still not executed, fifth-plus consecutive sweep.
  PayPal balance now ~14,268 SEK; ISK cash independently verified at 845.43
  SEK, so this is now the binding constraint on the AZN.ST BUY as well as the
  original fee-drag rationale.
- **2026-09-14 note:** still not executed, sixth-plus consecutive sweep.
  PayPal balance now 14,227.88 SEK at this sweep's FX; ISK cash re-verified
  again at the identical 845.43 SEK. Nothing about the merit or the blocking
  relationship to the AZN.ST BUY has changed since 2026-09-07 — only the
  count of sweeps this has sat unexecuted.
- **2026-09-21 note:** still not executed, seventh-plus consecutive sweep.
  PayPal balance now 14,416.12 SEK at this sweep's FX; ISK cash re-verified
  again at the identical 845.43 SEK. This sweep the AZN.ST BUY it blocks
  acquired a real cost (the stock ran +5.5% this week) and the list of what
  waits on this conversion grew to four: the fee drag itself, the AZN.ST
  share, gold tranche 2, and the cash overweight.
- **2026-09-28 note:** still not executed, eighth-plus consecutive sweep.
  PayPal balance now ~14,631 SEK; ISK cash re-verified again at the identical
  845.43 SEK. `portfolio` this sweep allocates the eventual ~14,046 SEK net
  proceeds across three destinations at once (the AZN share, ~5,611 SEK to
  gold tranche 2 closing the −2.48pp gap to target, and the remainder to
  Avanza Global) — the longer this sits, the more decisions stack up behind
  it.
- **2026-10-05/10-12/10-19 notes:** still not executed, now an 11th-plus
  consecutive sweep. 2026-10-19's net proceeds (~14,177 SEK) are the binding
  constraint on four names at once: gold tranche 2 (~5,578 SEK), the AZN.ST
  share, VICI (if ABB is unsold), and NVDA (newly promoted BUY this sweep).
  Merit unchanged every sweep it has been reviewed; only the queue behind it
  keeps growing.
- Full deliberation history (the Stripe-routing dead end, the
  multi-sweep repeated-advice pattern, the Revolut-balance/D3 cross-link):
  `reports/SESSION_LOG.md`'s 2026-08-10 through 2026-08-17 entries.

### P4 — Replace the Bitcoin certificate with a cheaper one
- **Status: CLOSED 2026-08-17.** COIN-XBT.ST (2.5%/yr) sold in full and
  replaced with a Valour Bitcoin Zero SEK certificate (ISIN
  CH0585378661), user-confirmed 0%/yr fee and genuinely BTC-backed — see
  `data/portfolio.json`'s Valour holding entry. A candidate replacement
  (BITC, a US-listed ETF) was evaluated and rejected first — see
  `reports/2026-08-17-council-memo-2.md`. Only remaining loose end: a
  tradeable ticker for live pricing of the Valour certificate — a pricing
  convenience, not a reason to reopen this item, and the ticker question
  itself was closed under cap pressure this session (see S1's closed-log
  entry, 2026-09-14). Full deliberation history:
  `data/portfolio_history_archive.md#p4-deliberation-history-full-text-archived-2026-08-17-item-is-closed`.

### P5 — ETH thesis (the two stocks are now done)
- **Status:** open for ETH only
- **SHB-A.ST and INVE-A.ST are CLOSED** (2026-08-03): recorded as "good track
  record, secure/stable with upside", bought without comparing alternatives
  because there was spare cash to put to work. That candour matters and is
  recorded — it makes both **rotation candidates** rather than conviction
  holdings, which is directly relevant to the P6 medium-tier build.
- **CORRECTED 2026-08-17: ETH does have a recorded thesis, this line was
  stale.** `data/portfolio.json` has carried a full structured ETH thesis
  since 2026-08-12 (in the user's own words — long-term conviction that
  BTC/ETH are the "most secure" cryptocurrencies, 3y+ horizon), status
  INTACT. This session's Council memo caught the disagreement between this
  file and `portfolio.json` and treated `portfolio.json` as authoritative.
  **The no-adds freeze stays in place regardless** — it was never actually
  gated on the missing-thesis leg alone, and survives on the P1 (cost
  basis) limb: no adds until P1 closes, so a sale/tax event can be reported
  properly.
- **INVE-A.ST keeps a separate open blocker:** its thesis is plausible but not
  properly *testable*, because the metric that matters for a holding company
  is NAV discount/premium and it has never been obtained. See S6's closed
  entry below — the Option-3 durable hold is now this system's standing
  treatment, not a live blocker on P5's status.
- **2026-08-18 through 2026-09-21 notes:** six consecutive sweeps of the
  Contrarian/Copycat disagreement over INVE-A.ST's missing NAV metric — full
  detail preserved in git history of this file. **2026-09-28: the
  pre-committed Option-3 fallback fired** — hold the 5 shares, stop
  re-flagging until a NAV figure exists. **2026-10-05 through 2026-10-19:**
  the 2026-10-07 Q3 NAV window passed with nothing recorded; Option 3 is now
  this system's durable position on the holding, reconfirmed rather than
  reopened each sweep since. Re-entry trigger unchanged: a user-recorded NAV
  figure, or a Cederholm disposal.

### P6 — Build the medium tier (~26,400 SEK available)
- **Status:** retroactive review DONE 2026-08-17 — decision on rotation is now
  a real, numbers-backed call rather than an overdue homework item.
- **EXECUTED 2026-08-03/04** (user-reported): bought Volvo B (13sh @ 367.50),
  Atlas Copco B (27sh @ 181.25), AstraZeneca (4sh @ 1507), Alfa Laval
  (9sh @ 574.40), ABB (4sh @ 946.96) — 24,656.69 SEK of the 26,400.30 SEK
  cash.
- **`swedish-equity-review` RUN 2026-08-17** on the three names that had
  never been through it (ATCO-B.ST, ALFA.ST, ABB.ST — AstraZeneca already had
  a thesis via Council call D 2026-08-06). Fresh data both halves: Yahoo
  quoteSummary fundamentals + Finansinspektionen insider transactions, same
  session. All three scored 6/6 dimensions (100% coverage):
  - **ALFA.ST — 63/100, best of the three.** Consistent 4-year revenue
    growth (no down year), 10/10 real open-market insider buys since 2023
    with zero disposals (strongest insider signal of the three). Still
    expensive (P/E 28.1x, PEG 2.86 — actually the worst growth-adjusted
    value of the three despite the lower headline multiple).
  - **ATCO-B.ST — 62/100.** Excellent underlying business (42% gross
    margin, ROE 25.7%, ROIC ~40% est., low leverage) but FY2025 revenue
    declined -4.8% before a ttm recovery (+9.1%), priced at 98.5% of its
    52-week range (P/E 33.2x, PEG 2.38), and only a thin/dated single-insider
    buy signal.
  - **ABB.ST — 51/100, the clear rotation candidate.** Richest valuation of
    the three, thinnest FCF conversion, a raw-data currency-mismatch finding
    (now tracked under S32), and a recent insider-selling cluster.
  - None breach the 15% single-position cap or even reach the "normal" 3-8%
    band. **Recommendation (2026-08-17):** do not add to any of the three at
    current valuations; hold ATCO-B.ST and ALFA.ST; treat ABB.ST as the
    active rotation candidate if/when better-vetted capital needs a home.
  - Full scored detail: `data/company_profiles/ATCO-B.ST.json`, `ALFA.ST.json`,
    `ABB.ST.json`.
- **2026-08-24 — SELL called on ABB.ST**, proceeds originally proposed for
  META, then VICI. **Reaffirmed every sweep from 2026-08-31 through
  2026-10-12**, conviction drifting 7→5 as two of the original three
  load-bearing facts turned out to be data artifacts (the forward/trailing
  P/E "inversion" and the FCF-yield currency-unit bug, see S32). Destination
  settled on VICI by 2026-08-31 and has not changed since.
- **2026-10-12 — the Chairman declared the call explicitly non-renewable**:
  execute before the 2026-10-20 print or the call lapses outright, with the
  next memo re-deciding ABB fresh rather than carrying a streak.
- **2026-10-19 — per that non-renewable rule, the memo takes no fresh
  position.** The SELL is still executable today as *last week's* decision
  (4 shares, ~3,661.60 SEK) or can lapse at tomorrow's (2026-10-20) print;
  both are legitimate and left as the user's live choice. The 2026-10-26
  memo decides ABB fresh on reported Q3 numbers (test named by the Chairman:
  operating margin >16.9% and forward P/E clearly below trailing retires the
  case; FCF/revenue still ~4–5% with a flat forward/trailing gap revives
  it).
- **Two flags carried forward, still relevant to what remains uninvested:**
  Spiltan Aktiefond Investmentbolag structurally overlaps your existing
  Investor A position; Swedbank Robur Technology A is a concentrated
  single-sector active fund with higher fees. Neither is disqualifying,
  both should be conscious choices if the remaining ~1,744 SEK (or future
  contributions) go toward them.

### P7 — Gold: new exposure class, instrument verified, ready to execute
- **Status: CLOSED — EXECUTED 2026-08-25, recorded 2026-09-02.** User bought
  4 units of Xetra-Gold @ 128 EUR/share, 5,689.22 SEK total, in the Avanza
  ISK — the exact instrument this item cleared. Recorded into
  `data/portfolio.json` (new `DE000A0S9GB0` holding, `exposure_class: gold`)
  and `targets` updated per this item's own pre-approved carve: equity
  85 -> 80, new `gold_pct: 5`. No live price feed found (Yahoo
  `DE000A0S9GB0.SG` 404s) — carried at cost basis, same treatment as
  `S1`/BTC0E.AS, until a working ticker or a broker-screen value turns up.
  **Note for the record:** this purchase (and 3 more AZN.ST shares, same
  day) predates the 2026-08-31 sweep by 6 days but was not reported to the
  system until 2026-09-02, after that sweep's memo had already run — the
  2026-08-31 Council memo's AZN.ST BUY sizing and ISK-cash figure (11,288
  SEK) are superseded; see the AZN.ST holding's `thesis_narrative`. Original
  item text below, kept for history.
- Council's Portfolio Governance call (2026-08-22): BUY, first
  tranche ~7,500 SEK, via an Avanza ISK-held physically-backed gold ETC.
  **2026-08-23: the user's own Xetra-Gold (DE000A0S9GB0) fact sheet
  reviewed and it clears every condition Council set** — physically
  backed with a real physical-delivery right, extremely low cost
  (0.07%/yr year 1, 0.01%/yr annualized over 5 years), listed on a
  regulated exchange (Frankfurt). **This is OK to buy.**
- Sizing: with ISK cash now confirmed at 11,288 SEK (P8, closed below),
  the ~7,500 SEK tranche 1 is comfortably funded without touching anything
  else. Long-run target 5% of total portfolio (~11,400 SEK), hard ceiling
  7.5%, tranche 2 funded via P3's PayPal conversion or a future
  contribution.
- **Structural gap, still open:** `portfolio.json.targets` has a `gold_pct`
  field (5) but `investor_profile.json.reference_targets` does not — see
  new item **S35** below.
- Full reasoning: Council's five-voice governance verdict, 2026-08-22.
- **2026-08-23 user update: skipping for now.** User checked Excel for a
  Swedish-listed gold ticker and found none. Xetra-Gold (DE000A0S9GB0,
  Frankfurt) is still the reviewed/cleared instrument if this gets
  revisited — nothing about the verdict above changed, this is a "not
  right now" from the user, not a rejection of the instrument.

### P9 — AZN.ST: Excel ledger shows 6 shares, real Avanza shows 5
- **Status:** open — blocks nothing today (portfolio.json correctly holds
  5, protected from the wrong Excel figure by a CONFIRMED marker added
  2026-08-23), but will keep re-flagging every sweep until fixed at the
  source.
- The user's own master-6.xlsx workbook README already names this exact
  bug: "AZN NOTE: Holdings follows the ledger, so AZN shows 6 sh / 9,069
  SEK cost (5 OPENING + 1 BUY 2026-08-06). If Avanza says 5 sh, correct
  the AZN Transactions rows." Confirmed against the real Avanza
  transaktioner export: 4 units @ 1,507 SEK (2026-08-04) + 1 unit @
  1,520.50 SEK (2026-08-06) = 5 total, matching portfolio.json exactly.
  The Excel Transactions tab has a phantom extra OPENING row.
- **Action: delete the phantom AZN OPENING row in the Excel Transactions
  tab** (per the workbook's own README instructions) — Holdings will
  follow automatically once the ledger is right.

### P10 — Possible duplicate 5,000 SEK deposit (2026-08-17 vs 2026-08-22)
- **Status:** open — not applied/resolved, needs the user's confirmation
  before either row is touched.
- `data/transactions.csv` carries TWO 5,000 SEK deposit rows: one dated
  2026-08-17 (pre-existing, source "User-confirmed deposit", no matching
  entry anywhere in the real Avanza transaktioner export), and one dated
  2026-08-22 (added 2026-08-23 from that real export, which shows exactly
  one Handelsbanken deposit of 5,000 SEK in the trailing year, dated
  2026-08-22). Master-6.xlsx's own Transactions tab also only shows the
  2026-08-17 version. Likely reading: these are the same real-world
  deposit, mis-dated once. Not merged/deleted without asking, since it's
  real money either way.
- **Action: confirm — was there one 5,000 SEK deposit or two?** If one,
  say which date is right so the wrong row can be removed.

---

---

## S — System items

IDs are never reused — an S-number in an old memo always means the same item.

### S21 — [prospecting] Nordic coverage: 107 names, and a data asymmetry underneath
- **Status:** open — the headline problem is fixed; a quieter one it exposed is not
- **Reviewed 2026-08-31 through 2026-10-05: valuable soon, seven consecutive
  measurements of the same 28-35pp `fwd_pe` Sweden-vs-US coverage spread**,
  each tying the gap to a concrete cost (VOLCAR-B.ST screening MISSING then
  dropping out of the candidate set entirely; AZN.ST — the portfolio's
  largest holding — ranked 59-62 of ~75 while three Council voices call it a
  BUY). Full history preserved in git log of this file; not re-quoted here to
  avoid this item's own text regrowing into an essay.
- **Reviewed 2026-10-19: valuable soon, 8th measurement, same magnitude,
  still unbuilt.** This sweep's scorecard: `fwd_pe` 70% Sweden vs 100% US, a
  30pp spread — within the same 28-35pp band measured every sweep since
  2026-08-24, still above the scorecard's own >15pp flag threshold.
  `fcf_yield_pct` also carries a 17pp spread this sweep, a second field
  showing the same asymmetry. AZN.ST's `forward_pe` is now missing a 9th
  consecutive run. Eight unchanged measurements with no build attempted is
  not new evidence that the problem matters more — that case was already
  made — it is evidence that repeating the recommendation a ninth time will
  not be what moves it. Not escalating the wording further.
- **2026-08-24 (evening):** the user supplied a 120-row Swedish ticker CSV.
  `scripts/watchlist.py universe-import` verified it and the universe went
  from 538 names (20 Nordic) to 622 (107 Nordic, 17%). Swedish names now
  reach the lens shortlists on their own merits.
- **What remains, and it is a real distortion, not a cosmetic gap:** Yahoo's
  fundamentals coverage is not symmetric across markets. The Valuation and
  Growth lenses both rank partly on forward multiples, so **a Swedish
  company can lose a shortlist slot for having no forward estimate rather
  than for being less attractive** — a systematic tilt toward US names that
  no one would see in the output. The `MISSING` label is honest per name;
  the aggregate bias is invisible.
- **How:** two options, neither large. (1) Make each lens report per-market
  coverage alongside its shortlist, so the tilt is at least visible to the
  Council. (2) Better: z-score each lens *within* a coverage cohort, or drop
  forward-looking fields from a lens's inputs when coverage for a name's
  market is below a threshold, so names are compared on fields they can all
  actually be measured on. Option 1 is an afternoon; option 2 is the real fix.
- **Also still open:** no free Nordic/European *constituent feed* is
  reachable (Wikipedia and Nasdaq Nordic are proxy-blocked), so the Nordic
  block stays user-maintained — a maintenance question, not a capability gap.

### S26 — [data] Drawdown backtest window contains no real shock to test the stated tolerance
- **Status:** open — narrowed successor to the closed S5
- **Reviewed 2026-08-31 through 2026-10-05: escalated to top-priority
  build.** `data/backtests/` was confirmed absent on disk; the one "pass"
  figure ever quoted (−20.62% max drawdown) has no traceable backing file;
  the window's own worst equity drawdown (−19.14%) never actually tested the
  −30% tolerance it claims to clear. This item became the stated gate on a
  live decision (D-c, the crypto-sizing trim), and a missed deadline it set
  itself once fired a (later found to be unexecuted) default trim action.
  Full history preserved in git log of this file.
- **Reviewed 2026-10-19: can wait, downgraded from top-priority.** No fresh
  forcing evidence this sweep. More importantly, **D-c's acute pressure was
  relieved this sweep by a different fix**: the crypto-sizing band was
  corrected onto `data/definitions.json`'s already-pinned full-portfolio
  convention (trim trigger moved from ~11,730 to ~14,080 SEK) — a
  denominator bug, not the shock-window gap this item names. That removes
  the immediate reason D-c was escalating sweep over sweep, but it does not
  touch the underlying gap: `data/backtests/` is presumed still absent (not
  re-checked this sweep), and the −30% tolerance is still unverified against
  any real shock. Downgrading priority rather than closing — reopen the
  escalation if D-c's new band is ever actually at risk of firing without a
  real backtest behind it, or if the glidepath re-anchor trigger (the
  property goal firming up) arrives first.
- **Why:** a 90/10 equity/crypto proxy over 2019-06 to 2026-08 (86 months)
  shows max drawdown -20.62%, inside the stated -30% tolerance line — but the
  window's own worst equity drawdown is -19.14%, so the data contains no
  crash on the scale the tolerance was written to describe. The 10% BTC
  sleeve also "barely registered" in that result because monthly rebalancing
  dilutes crypto's path, while the real portfolio is not rebalanced monthly
  and crypto has been allowed to drift to 9.4-11.2%.
- **How:** run `backtest.py` over a fixed window that actually contains a
  real >=-30% equity shock (e.g. 2007-2009 or 2020-02/03), using a
  longer-history index proxy than VWCE.DE. Report the result as a second,
  clearly-labelled "shock window" figure alongside the existing rolling
  lookback one. **Write the output to `data/backtests/`**, which does not
  currently exist on disk.
- **Improves:** data reliability (the scorecard/portfolio-health row rests
  on a window that cannot test what it claims to, and currently has no
  backing file at all) and decision quality (the crypto sleeve is the part
  of the target this backtest tests least).

### S27 — [process] The scheduled task's stored prompt drifts stale against real file state, and this is now the ninth confirmed occurrence
- **Status:** open — widened a third time this sweep, same ID, per this
  item's own precedent of widening scope on a repeat of the same underlying
  shape (stored/asserted instructions diverging from what the system
  actually requires) rather than proliferating IDs
- **2026-09-07 through 2026-10-05 reviews: six confirmed occurrences of the
  external scheduled-prompt drift** (the Handelsbanken-wrapper and
  `reference_targets`-is-null premises, recurring verbatim), **plus three
  same-family in-session instances**: a shell-substitution bug delivering
  literal `$(cat ...)` strings to `council` instead of file contents; a
  hand-counted streak claim ("7 consecutive runs") that didn't match
  `candidate_history.csv`; and the 2026-09-28 Council memo itself writing
  "Applied: Option 1" for a BTC0E.AS trim this system never executed — the
  first confirmed instance of the drift originating *inside* a Council memo
  rather than an external or shell-substitution source. Every occurrence
  through 2026-10-05 was self-caught before any wrong action. Full history
  preserved in git log of this file.
- **2026-10-19 meta review — ninth confirmed occurrence of the external
  drift, plus the most severe variant yet, plus a second recurrence of a
  narrower scheduled-prompt-drift instance folded in from this sweep's
  market-data fetch.** Three distinct findings this sweep, all the same
  underlying shape:
  1. **The scheduled prompt again asserted the Handelsbanken wrapper is
     unresolved and `reference_targets` are null** — both false, both
     declined before any script ran (ninth confirmed occurrence of this
     exact pair of premises).
  2. **The scheduled prompt omitted `scripts/scout.py` entirely**, jumping
     from market-data/calendar straight to "the four lenses." This is
     categorically worse than every prior occurrence: those were stale
     *facts* that got corrected in prose; this one tried to skip a
     *mandatory pipeline stage* that CLAUDE.md states explicitly runs every
     sweep and is never a valid outcome to omit. The orchestrating session
     ran scout anyway, overriding the prompt — self-caught, no wrong action,
     but the closest this family has come to actually degrading the
     pipeline rather than just the prose around it.
  3. **The scheduled prompt's market-data fetch instruction named only
     `ethereum`**, not `ethereum,bitcoin` as CLAUDE.md's own documented
     fetch command specifies — the second consecutive sweep this exact
     narrowing has produced a snapshot with zero BTC price fetched. Unlike
     the first occurrence (2026-10-12, noted but not yet called a pattern),
     this is now a repeat with a named, compounding cost: D-c's corrected
     crypto-sizing band is unevaluable for a second sweep running because
     there is no live BTC price to compare against the new ~14,080 SEK
     trigger.
  All three are the identical failure shape this item exists to track:
  stored prompt text that does not match what the live system actually
  requires, each one self-caught or overridden before causing a wrong
  capital action. **Folding all three into S27 rather than opening new IDs**
  — findings 1 and 3 are straightforward repeats of the external-drift and
  narrowed-fetch-instruction patterns already in scope; finding 2 is a new,
  more severe *degree* of the same shape (a pipeline stage instead of a
  fact), which is exactly the kind of widening this item's own 2026-09-28
  and 2026-10-05 reviews already set the precedent for.
- **Explicitly NOT folded into S27: the 2026-10-12 sweep's skipped
  `journal`/`meta` steps.** That failure has no self-catch at all (it was
  invisible for seven days, found only by the next session noticing a stale
  file timestamp), which breaks the defining feature of every S27 occurrence
  to date — self-mitigation before causing harm. Tracked separately as the
  new **S34** below.
- **Why:** the scheduled prompt that launches this weekly sweep is stored
  text, edited by hand outside this repository, and does not update itself
  when the facts it assumes change or when its own instructions fall out of
  sync with CLAUDE.md's canonical flow. Nine confirmed occurrences of the
  external drift, each caught and corrected (or overridden) before causing a
  wrong action — but the recommended fix (removing/rewriting the two stale
  lines, and now also re-checking the scheduled prompt against CLAUDE.md's
  full step list rather than just its two most commonly stale facts) has sat
  unapplied since first recommended 2026-09-07, across more than ten sweeps.
- **How:** whatever stores this scheduled task's prompt (outside this
  repository) needs: (1) the Handelsbanken-wrapper and stale-`reference_targets`
  lines removed; (2) its step list re-synced against CLAUDE.md's canonical
  flow so a mandatory stage (scout) cannot be omitted again; (3) its
  market-data fetch instruction corrected to request `ethereum,bitcoin`
  together, matching CLAUDE.md's own documented command, not just ethereum.
  None of these are code `meta` can apply — this is a direct recommendation
  to the user, now overdue by more than ten sweeps since first raised.
  Separately, in-repository: any prompt assembled for a subagent should pass
  file paths rather than shell-substituting content, and `council.md` should
  never write "Applied"/"Executed" for an action this system did not itself
  perform.
- **Improves:** decision quality (a stale or incomplete premise that goes
  uncaught would produce a wrong action, not just wasted words — this
  sweep's scout-omission and BTC-fetch-narrowing instances came closer to
  that than any prior occurrence) and process reliability (the system's own
  scheduling and orchestration text drifting out of sync with live state and
  with CLAUDE.md's own mandatory flow).

### S29 — [data] Candidates CSV carries `pct_52w_range` but not the 52-week high/low endpoints, capping a real Top-5 conviction
- **Status:** open — new 2026-09-14
- **Reviewed 2026-09-21 through 2026-10-05: valuable soon, seven consecutive
  sweeps unfixed**, each naming the identical, concrete cost on APP (the
  funnel's #1-ranked name across most runs): pristine quality metrics
  (ROIC 65.5%, operating margin 77.7%, revenue +52.8%) held to a capped
  conviction because the system can see the percentage of 52-week range but
  not the level or timing of the underlying drawdown. The Council's own
  words: "the cheapest high-value fix on this memo's list." Full history
  preserved in git log of this file.
- **Reviewed 2026-10-19: can wait — no fresh forcing evidence this sweep.**
  APP did not appear in this sweep's Top 5 (FSLR, a first-seen name, holds
  the #5 slot instead), so there is no fresh, named instance of this gap
  capping a live conviction score this particular sweep. The underlying code
  gap is unchanged and the fix recommendation stands exactly as specified —
  not re-escalating the wording, since nothing new argues for it this week,
  but flagging that this remains a one-column, no-new-fetch change that
  could be applied at any time without further deliberation.
- **Why:** `scout.py`'s candidate CSV outputs the derived `pct_52w_range`
  percentage only, not the underlying `52w_high`/`52w_low` fields, even
  though the snapshot already carries both per ticker.
- **How:** add `week52_high` / `week52_low` columns to `scout.py`'s candidate
  CSV output, sourced from fields the snapshot already fetches — no new data
  source, no new fetch.
- **Improves:** decision quality (a Top-5 conviction score was measurably
  reduced by an interpretability gap a one-column change removes) and data
  reliability (closes the gap between what the snapshot captures and what
  reaches the lenses and voices).

### S32 — [data] Currency-unit mismatch in `fcf_yield_pct` (and `price_to_sales`/`price_to_book`) for issuers that report in a different currency than their listing — absorbs S24
- **Status:** open — absorbs S24 (same root-cause family); widening with
  each sweep faster than it is being fixed
- **Why:** `fcf_yield_pct` for ABB.ST and AZN.ST divides free cash flow
  reported in the company's own reporting currency (USD, for both) by a
  market cap computed in the listing currency (SEK), with no FX conversion.
  Verified by arithmetic 2026-10-05: AZN.ST's real FCF yield is ~2.0%, not
  the 0.20% every prior sweep computed and fed into `z_value`; ABB.ST's real
  figure is ~0.87%, not 0.09%. This directly fed the funnel's rank and was
  literally a sweep's "strongest case against" AZN.ST.
- **Absorbs S24's TSM instance — unverified hypothesis.** TSM reports in
  TWD and is priced in USD, so the same currency-conversion bug would
  produce exactly this shape of error on its unflagged `roic_pct` /
  `fcf_yield_pct`. Not yet confirmed against TSM's actual reported TWD
  figures.
- **2026-10-12:** AZN.ST's `price_to_sales`/`price_to_book` confirmed to join
  ABB.ST's known unit-mismatch pattern — caught by that sweep's own Council
  review, unflagged by scout.
- **2026-10-19 — widened again, and the detector's partial catch is now
  visible on a single name.** TSM's `fcf_yield_pct` rose to **56.22%** (up
  from 31.08% last sweep) and remains completely unflagged, while TSM's
  `roic_pct` is now correctly suspect-flagged in the same run — meaning
  whatever bounds check catches one implausible field on TSM is not catching
  the other, on the same company, same sweep. **Two new unverified
  hypotheses, not confirmed this sweep:** EVO.ST and HEXA-B.ST's FCF yields,
  both EUR-reporting issuers listed in SEK — the same currency-mismatch
  shape as ABB.ST/AZN.ST/TSM, flagged for the next sweep to check against
  each company's actual reported EUR free cash flow and the EUR/SEK rate,
  not assumed.
- **Also check:** whether `price_to_sales` and `price_to_book` share the
  pattern more broadly — ABB.ST's `price_to_book` 113.06 is independently
  suspect-flagged every sweep.
- **How:** find where `fcf_yield_pct` (and `price_to_sales`/`price_to_book`)
  is computed in `scripts/fetch_market_data.py` or `derived_metrics.py`.
  Confirm whether the numerator is sourced in the company's reporting
  currency while market cap is sourced in listing currency. Fix by
  converting the numerator to the listing currency using the matching FX
  rate already present in the macro snapshot before dividing. Then re-test
  TSM, EVO.ST and HEXA-B.ST specifically: if each normalizes into a
  plausible range once the currency fix is applied, this item closes
  cleanly; any name that does not normalize should be split out under a
  fresh ID as a narrower, bounds-calibration-only gap.
- **Improves:** data reliability (a verified, fixable code bug, not a
  judgement call) and decision quality (this error has supplied the
  strongest argument against or inflated case against at least three live
  holdings across multiple sweeps of Council reasoning).

### S33 — [mechanical] Lens ranking has shown no predictive signal for many consecutive sweeps, now with n well over the scorecard's own threshold
- **Status:** open — new 2026-10-05
- **Why:** `scripts/scorecard.py`'s MECHANICAL pillar has read "RANKING IS
  NOT ADDING SIGNAL" for many consecutive sweeps, and the numbers are no
  longer a provisional, noisy read — every lens individually clears n=20+.
  The value lens has been the most consistently damaging, with beat-rates
  against baseline in the single digits to low teens across multiple
  sweeps, meaning it is close to actively anti-correlated with outcomes
  rather than merely uninformative.
- **Reviewed 2026-10-19: still open, n continuing to grow, same
  conclusion.** This sweep's scorecard: contrarian n=75 (median −1.1%, beat
  45%), defensive n=108 (+0.7%, beat 53%), growth n=102 (−1.0%, beat 46%),
  quality n=174 (+0.4%, beat 52%), value n=111 (−0.8%, beat 48%); top-half
  ranks median −2.2% vs bottom-half +1.4% — the sign of the split has moved
  around between sweeps but the conclusion ("ranking is not adding signal")
  has not changed once since this item opened. No new build attempted; not
  re-arguing why this matters again, since the case was already made at
  real n.
- **How, two parts, not mutually exclusive:**
  1. **Make the non-predictiveness operational, not just descriptive.**
     State as an explicit rule (not left to each sweep's Chairman to
     rediscover informally) that mechanical rank carries zero evidentiary
     weight once the Council is handed a shortlist — it is a surfacing
     mechanism, not a signal.
  2. **Investigate the value lens specifically**, since it is the one
     consistently anti-correlated lens, not merely flat. Candidate
     hypotheses worth testing against `candidate_history.csv`: value's
     z-score inputs reward falling prices; or value's trailing-multiple
     inputs systematically lag a market already pricing in deterioration.
- **Improves:** decision quality (prevents treating a non-predictive rank as
  if it carries information) and system reliability (the MECHANICAL
  pillar's stated purpose currently reads a repeated "no" without any
  proposal in response).

### S34 — [process] No mechanism verifies that `journal`/`meta` actually ran before a sweep ends — the 2026-10-12 sweep skipped both for a full week with zero self-catch
- **Status:** open — new 2026-10-19
- **Why:** the 2026-10-12 sweep ran market-data, scout, calendar and
  council in full — a real memo, real picks, a real scorecard refresh, all
  committed to git (`d1d5434`, `c1d9fb7`, `2306ab6`) — but the session ended
  without running `journal` or `meta`. No `SESSION_LOG.md` entry was written,
  and `OPEN_ITEMS.md` was not touched since the 2026-10-05 review. The
  2026-10-12 memo's own closing line read "`journal` must run next... an
  unlogged memo is invisible to the next session and can never be
  reconciled" — and for seven days, it was exactly that: invisible. The
  2026-10-19 sweep found it only by noticing a snapshot file newer than the
  latest logged entry, then reconstructing the missing week from git
  history. This is a different failure shape than S27: every S27 occurrence
  self-mitigates inside the same session, before causing a wrong action.
  This one had **no self-catch at all** — nothing inside the 2026-10-12
  session, and nothing mechanical anywhere in the system, flagged that two
  mandatory steps had been dropped. It was caught by luck (a timestamp
  comparison the next orchestrator happened to make), not by design.
- **How:** deterministic, no new agent. Add a small check — a few lines in
  `scripts/check_unmerged_work.py`, or a new tiny script run at the very end
  of a sweep — that verifies, before the session is allowed to be considered
  complete: (a) `reports/SESSION_LOG.md`'s newest entry date matches the
  latest market-data snapshot's date; (b) `reports/system-scorecard.md`'s
  generation timestamp is on or after the latest Council memo's; (c)
  `OPEN_ITEMS.md` was modified in the same session as the latest memo, or an
  explicit "no changes this sweep" is recorded. If any check fails, the
  session should flag it loudly (a printed warning, a non-zero exit) rather
  than silently ending — the same philosophy CLAUDE.md's step 7
  (`check_unmerged_work.py`) already applies to the two-branch-fork problem,
  applied here to the dropped-pipeline-stage problem.
- **Improves:** system reliability (a dropped mandatory stage is currently
  only detectable by luck) and, indirectly, decision quality (every pillar
  the scorecard measures depends on every sweep being logged and
  reconciled — an invisible sweep is a silent gap in the only calibration
  mechanism this system has).

### S35 — [data] `investor_profile.json.reference_targets` still carries no `gold_pct` field and stale 85/10/0/5 weights against `portfolio.json.targets`' correct 80/10/5/0/5 — now past its own stated open-an-item threshold
- **Status:** open — new 2026-10-19, opened per the standing rule set
  2026-09-14 ("a third unapplied occurrence should open an S-item without
  further deliberation")
- **Why:** flagged directly (not as an S-item) 2026-09-07, with a one-line
  fix recommended. Found unapplied and flagged a second time 2026-09-14,
  which set the explicit rule above. Found unapplied a third, fourth and
  fifth time through 2026-10-05/10-12/10-19 — this sweep, both `portfolio`
  and `council` independently flagged it as having "passed its own pre-set
  open-an-S-item threshold." Verified directly this session:
  `investor_profile.json.reference_targets` still reads `equity_pct: 85,
  crypto_pct: 10, fixed_income_pct: 0, cash_pct: 5` with no `gold_pct` field
  at all, while `portfolio.json.targets` (the authoritative owner per
  CLAUDE.md's data-ownership table) correctly carries 80/10/5/0/5 including
  the gold carve applied when P7 executed 2026-08-25. This produces a
  self-contradictory ACT/WATCH rating every sweep a lens checks the stale
  file instead of the correct one, and burns a portfolio-lens or Council
  cycle re-explaining the same already-known discrepancy rather than
  reasoning about something new.
- **How:** a one-line (well, four-field) JSON edit: update
  `investor_profile.json.reference_targets`'s `equity_pct`/`crypto_pct`/
  `fixed_income_pct`/`cash_pct` to 80/10/0/5 and add `gold_pct: 5`, matching
  `portfolio.json.targets` exactly — or better, replace the duplicated
  numbers with an explicit pointer/comment stating `portfolio.json.targets`
  is authoritative, so the two files cannot silently diverge again. Not a
  code change; editable directly whenever convenient.
- **Improves:** data reliability (removes a recurring, avoidable
  self-contradiction between two files that are supposed to agree) and
  decision quality (stops a voice/lens repeating the same stale-data
  correction instead of reasoning about something new).

---

## V2 Roadmap — user-authored

The user's roadmap (received 2026-08-09), not evidence-driven S-items;
`meta` does not prune it, and it sits outside the S-item cap. Status updated
2026-08-24. The original verbatim spec lived in `docs/v2-upgrade-spec.md`,
removed 2026-08-24 — every phase's real status is below, and git history
holds the original text if it is ever wanted.

- **Phase 1 — DONE (2026-08-09).** Structured thesis schema on every active
  holding, the Chairman's structured action format, per-field data-quality
  states in `data/company_profiles/`, and Layer A/B company metrics
  (`derived_metrics.py`: ebitda, cash, debt, OCF, capex, EBIT, equity book,
  invested capital, ROIC).
- **Phase 2 — partially delivered.** Quality and Valuation are now genuinely
  separate numbers per candidate (`z_quality` / `z_value` in the candidates
  CSV, computed from different fields). **Still not started:** the Fair Value
  Gap (`valuation_gap_estimate` with methodology/confidence/source/date,
  `UNKNOWN` when unreliable).
- **Phase 3 — DELIVERED 2026-08-24.** This was "wire the parked ranker at a
  real universe, add quality factors, make the funnel thresholds
  configurable, have scout output a compact candidate dataset". All four are
  now true: `scripts/scout.py` ranks a ~540-name universe through five lenses
  including quality (ROIC/ROE/margins/leverage), every threshold and funnel
  width lives in `config/settings.py`, and the output is a compact
  candidates CSV. The parked `scripts/funnel/` implementation it referred to
  has been deleted rather than left as a second copy.
- **Phase 4 — not started.** `risk_factor_exposure` risk-bucket
  classification (Global industrial cycle / Defensive healthcare /
  Financials / …) distinct from sector — aimed squarely at the Volvo + Atlas
  Copco + Alfa Laval + ABB correlated-industrial concentration this system
  keeps flagging. Portfolio-fit scoring for candidates is live (the
  Chairman's PORTFOLIO FIT stage); the risk buckets themselves are not.
- **Phase 5 — not started.** Macro Regime Engine expansion: fetchers for BOJ
  policy rate, USD/JPY, credit spreads, PMI, unemployment/GDP, a computed
  real-yield field; multi-dimension regime classification;
  `macro_fit`/`macro_sensitivity` per candidate. Still live evidence: the
  Macro voice's "no commodity-price and no credit-spread data" gap is named
  again in `council.md` because it is still true.
- **Phase 6 — instrumentation started.** Sell discipline (the seven
  legitimate sell triggers; "would I buy it today?" is already in
  `thesis-review.md`), crisis-window backtesting (`backtest.py` still only
  supports a rolling N-year lookback, no fixed `--start`/`--end` — see S26),
  and score calibration. `data/candidate_history.csv` is the calibration
  store this phase asked for — mechanical rank per candidate per run,
  correlatable against realised returns later. It records the funnel's
  ranks, not each voice's conviction; that is Phase 7d.
- **Phase 7 — Council architecture.** User-prioritised 2026-08-18.
  - **7a (voice isolation) — deliberately NOT built.** Seven voices as seven
    separate agent invocations would roughly double invocations per sweep and
    increase total tokens (each invocation reloads shared context). Multiple
    production sweeps have produced genuine, substantive disagreement with no
    visible anchoring between voices. Build it if anchoring is ever actually
    observed — not on principle.
  - **7b (Copycat / Smart Money) — DELIVERED 2026-08-24** as the seventh voice
    in `council.md`, with its data sources and its named gaps explicit. Its
    missing institutional/activist data is now tracked as S20 (closed); its
    narrower US-insider fetch-scope gap is tracked separately as S25 (closed).
  - **7c (formal disagreement register) — DELIVERED 2026-08-24.** The
    Chairman's per-candidate block now requires KEY DISAGREEMENT, STRONGEST
    CASE FOR, STRONGEST CASE AGAINST, DATA GAPS and WHAT WOULD CHANGE THIS as
    filled fields, not prose norms.
  - **7d (historical tracking) — partially delivered.**
    `data/candidate_history.csv` tracks rank, best lens and screen status per
    candidate per run (`python scripts/watchlist.py history`). Per-voice
    conviction over time still requires 7a's per-voice output files.
  - **Phase 7d (historical tracking) — DELIVERED 2026-08-25.**
    `data/decisions.csv` records every voice pick and Chairman call with
    conviction, horizon and the metrics it was made on, joined from the
    mechanical sweep rather than typed. `scripts/scorecard.py`'s JUDGEMENT
    pillar compares each voice against the benchmark and the Chairman against
    its own inputs. Several voices now read with real n (n>=20); the
    Chairman-vs-voices comparison, which is what would justify ever weighting
    the Council, is still short (chairman n=17, need 20) — see S33's sibling
    JUDGEMENT discussion in the scorecard; **the Council must still not be
    weighted.**

  - **Phase 8 (new, roadmapped 2026-08-25) — a multi-asset specialist voice.**
    One eighth Council voice owning non-equity opportunities: bonds,
    commodities, funds/ETFs, crypto. Preferable to stretching the seven equity
    voices over instruments their metrics do not describe — a P/E-based voice
    has nothing useful to say about a bond, and asking it anyway produces
    confident noise. **Not built, and the blocker is data, not architecture:**
    free sources cover equities well and bonds/options not at all, so the voice
    would reason from scraped or remembered figures. Build when a real feed
    exists for at least one class, with the same evidence rules as every other
    voice — including a `MISSING` label it is expected to use often.

  - **Item 4 (keep portfolio analysis distinct from stock selection) —
    satisfied and now structural**, not just instructed: `portfolio` is
    consumed at the Chairman's PORTFOLIO FIT stage only, and the candidate
    set the voices see is built by `scout.py` from the universe, never from
    the portfolio.

---

## Closed — index

One line each. **Full text of every entry is in
`data/portfolio_history_archive.md`** (section: "OPEN_ITEMS.md closed log,
archived verbatim 2026-08-24"), moved there so this file holds what is
outstanding rather than what is finished. Nothing was deleted.

### Closed by the 2026-10-19 session

- **S6 — closed under cap pressure (two new evidence-backed items opened
  this session: S34, S35), not because the underlying gap is resolved.** No
  free NAV/discount source for INVE-A.ST or Industrivärden has been found.
  But the 2026-09-28 Option-3 fallback (hold the 5 shares, stop re-flagging)
  has now held for three consecutive sweeps including through the
  2026-10-07 trigger window, and this sweep's SESSION_LOG confirms it was
  "reconfirmed, not re-opened" — this item has stopped forcing a live
  decision every sweep, which was its acute cost. Reopen (fresh ID) if the
  user records a NAV figure and wants the fetch/parse formalized, or if a
  Cederholm disposal or other re-entry trigger actually fires.
- **S31 — closed under cap pressure (two new evidence-backed items opened
  this session: S34, S35), not because resolved.** `journal.md`'s Mode 2
  step 4 still tells journal to run `scripts/scorecard.py --write`, which it
  cannot do (Read/Write tools only) — recurred at least six times since
  2026-09-07, including this sweep. It has never caused a wrong number to
  reach a decision; every occurrence was a correctly-sequenced manual
  workaround by the orchestrating session. The well-specified two-part fix
  (reorder CLAUDE.md's step 5a ahead of step 5; reword journal.md's Mode 2
  step 4) remains fully specified and can be applied directly at any time
  without further deliberation. Reopen (fresh ID) if a future sweep's
  SESSION_LOG entry is ever found to have quoted a stale scorecard figure as
  current (mislabeled, not just late) — i.e. if the harmless workaround ever
  actually fails.

### Considered by the 2026-10-19 session, not opened

- **The Chairman's own explicit rule (merit must never be downgraded for
  funding reasons) was violated for a full sweep before self-correcting —
  not opened as a new item, first confirmed occurrence.** Last sweep's
  Chairman held NVDA at HOLD-WATCH on a funding-availability reason, which
  `council.md` explicitly forbids (a BUY should still be output with an
  execution note, not downgraded). This sweep's Chairman caught and
  corrected its own prior application of the rule, promoting NVDA to BUY on
  a named process correction rather than new merit evidence. This is a
  genuine positive finding — the rule existed and a violation of it was
  self-corrected — but it was also live for a full week before being
  caught, which is longer than ideal for a rule that is supposed to apply at
  write time. Not opening an item on a single occurrence, per the standing
  pattern used elsewhere in this file (S27, S31 waited for repeats before
  opening); watching for a second occurrence of the same rule being
  misapplied before proposing a mechanical check (e.g. a flag the Chairman
  must clear explicitly whenever a call's stated reason references
  available capital rather than business merit).

### Closed by the 2026-10-05 session

- **S24 — closed, absorbed into new S32.** TSM's unflagged `roic_pct` 183.7%
  / `fcf_yield_pct` ~29.8% (5 consecutive sweeps unflagged) is now
  hypothesised to be the same currency-unit-conversion bug confirmed this
  sweep on ABB.ST and AZN.ST's `fcf_yield_pct`, not a separate
  plausibility-bounds calibration gap. S24's own root cause was never
  confirmed across 5 reviews; S32 tracks the now-identified root cause and
  names the exact test (does TSM's figure normalize once the currency fix is
  applied) that would either close this absorption cleanly or require
  reopening a narrower, bounds-only item under a fresh ID. ALL's separate
  `fcf_yield_pct` 26.79% instance (hypothesised insurer-float distortion, a
  different mechanism) stays noted under S32 rather than carried forward
  under this closed ID.
- **S30 — closed under cap pressure (8-item cap reached; two new
  evidence-backed items opened this session, S32/S33), not because
  resolved.** The D-series register gap is real (every recent memo still
  reconstructs D-a/b/c from P-item prose) but low-stakes — three consecutive
  reviews found no instance of the reconstruction itself producing a wrong
  fact, only repeated manual effort. Reopen (fresh ID) if a future
  reconstruction is ever shown to have gotten a sweep-count, option, or
  trade-off wrong; the already-written fix (add a "## D — Open decisions"
  section) can also simply be applied whenever convenient, since it needs no
  further deliberation — it was fully specified at opening.

### Considered by the 2026-10-05 session, not opened

- **`source=new` in the candidates CSV is being read as "first seen" when it
  actually means "not held, not watchlisted" — caused repeated miscounts in
  launch notes and memos, not opened as a new item.** This sweep's Council
  memo is the first to name the distinction explicitly and correct the
  count: of 35 rows carrying `source=new`, only 5 (CTVA, GPN, PLTR, EOG,
  TEL2-B.ST) are genuinely first-seen this run; the other 30 are known names
  that simply aren't held or watchlisted. Prior sweeps' SESSION_LOG entries
  (2026-09-21, 2026-09-28) described turnover in the same loose terms
  without this correction, meaning the same misreading has likely recurred
  at least twice before being caught. **Update 2026-10-12/10-19: a third and
  fourth explicit catch of the same miscount** (10-12: only GM genuinely
  first-seen of 33 `new` rows; 10-19: only AZA.ST and FSLR genuinely
  first-seen of 35) — now caught and self-corrected every single sweep
  since 2026-10-05, with zero wrong action on any occurrence. Per the
  pattern-recognition bar used elsewhere in this file, this has now met and
  passed the "second explicit catch" threshold that would normally open an
  item — but because every instance is caught cheaply and correctly in the
  memo's own text with no downstream consequence, and the cheap fix (rename
  `source=new` or add a true `first_seen_date` column) remains fully
  specified, this is being left as a standing watch note rather than
  promoted to a tracked S-item under cap pressure. Apply the rename/column
  fix whenever convenient; it needs no further deliberation.

### Closed by the 2026-09-28 session

- **Portfolio lens computed this sweep's allocation percentages against a
  different denominator than last sweep's, without flagging the change —
  caught by Council before it could mis-size a live trade, not opened as a
  new item.** `data/definitions.json`'s `investable_capital_convention`
  (decided 2026-08-17) pins the correct answer — full-portfolio, including
  the tax reserve — for exactly this kind of figure. **Update 2026-10-19:**
  this sweep's D-c crypto-sizing band was explicitly corrected onto this
  same pinned convention (trim trigger moved from ~11,730 to ~14,080 SEK),
  confirming the convention is being actively used to catch denominator
  drift rather than just documented. Still watching for whether
  `portfolio.md` ever states its threshold values explicitly in its own
  output, which would close this permanently rather than relying on each
  sweep's Council to catch a repeat.
- **A same-day scout re-run left an orphaned duplicate 75-row block in
  `data/candidate_history.csv`, caught and removed before committing — not
  opened as a new item.** No recurrence since. Not reopening.
- **The calendar fetch covered portfolio holdings only this sweep, and a
  live Top-5 BUY (VICI) lost its earnings date as a result — not opened as a
  new item.** **Update 2026-10-19:** this has now recurred every sweep
  since (calendar holdings-only again 2026-10-05, 10-12, 10-19), a
  standing regression rather than a one-off. Still not opened as a formal
  S-item under the 8-item cap this session, since it has not yet been shown
  to cost a live decision the way VICI's missing date did the first time it
  was observed — but this is now a repeated, not single, occurrence, and
  should be opened on the next sweep where a live candidate's earnings date
  gap is shown to matter, without further deliberation.

### Closed by the 2026-09-21 session

- **S23 — closed under cap pressure (8-item cap reached; two new
  evidence-backed items opened this session, S30/S31), not because the
  underlying measurement gap changed.** The discipline it protected
  (never quote a provisional median below n=20) is now structurally
  enforced by `scripts/scorecard.py`'s `MIN_OBSERVATIONS` threshold and
  CLAUDE.md's own stated rule, independent of a standing S-item. Reopen
  (fresh ID) only if a future session finds a provisional figure was
  actually quoted as a finding, or `MIN_OBSERVATIONS` was lowered.
- **S28 — closed under cap pressure (8-item cap reached), not because
  resolved but because unbuilt and quiet for three consecutive sweeps.**
  A capital-availability premise going stale between real-world execution
  and when it was reported. Reopen (fresh ID) on the next confirmed
  occurrence rather than carrying an inactive item through further cap
  pressure.

### Closed by the 2026-09-14 session

- **S1 — closed under cap pressure (8-item cap reached; one new
  evidence-backed item opened this session, S29), not because resolved.**
  The `KNOWN BAD` flag on BTC0E.AS's Yahoo feed continues to be applied
  correctly every sweep, and the broker-confirmed figure is used in its
  place. Reopen (fresh ID) if the flag is ever missed, or if the position's
  share of the portfolio grows enough that an unverified price starts to
  matter more than it does today.
- **S25's closed entry — addendum, not a reopening.** The scope gap S25
  diagnosed (only portfolio tickers are ever submitted to
  `--insiders`/`--fi-issuers`) is still real and unfixed, independent of
  S20's gateway block. A fresh evaluation under a new ID is warranted if
  `data.sec.gov` or an equivalent gateway ever becomes reachable and the
  scope gap is still unaddressed at that point — not before.
- **Considered, not opened (second unapplied occurrence):
  `investor_profile.json.reference_targets` still stale against
  `portfolio.json.targets`.** **Superseded 2026-10-19 — see new item
  S35,** opened per the exact rule set here ("a third unapplied occurrence
  should open an S-item without further deliberation").

### Closed by the 2026-09-07 session

- **S20 — closed: its own question answered.** `www.sec.gov` is confirmed
  not reachable through this environment's proxy (403 Forbidden on the
  CIK-mapping fetch). Reopen (fresh ID) only if a future session confirms
  `data.sec.gov` — a distinct host — is reachable.
- **S25 — closed: superseded by S20's confirmed finding, not resolved on its
  own terms.** The CIK-mapping fetch itself is blocked (S20), upstream of
  any ticker-scope fix. Not reopening a distinct "scope" question under this
  ID if EDGAR ever becomes reachable again — that would need a fresh
  evaluation under a new ID.
- **Considered, not opened: ABB.ST's `thesis_status` field lagging two
  sweeps of live SELL calls before correction.** First confirmed occurrence,
  self-corrected within the same session, no wrong action. Watching for a
  second confirmed instance before opening a mechanism to sync it
  automatically.
- **Considered, not opened: `investor_profile.json.reference_targets` stale
  against `portfolio.json.targets` since the 2026-09-02 gold carve.**
  First occurrence; flagged directly rather than opened. **Superseded
  2026-10-19 — see new item S35.**

### Closed by the 2026-08-31 session

- **S9 — closed under cap pressure (8-item cap reached; two new
  evidence-backed items opened this session, S25/S26), not because
  resolved.** Parts (a) cross-field plausibility and (b) new-position-with-
  no-thesis flag remain undone. Reopen if a future Excel import shows a
  plausibility error or a silent unthesised new position.
- **S22 — closed: the system side of this item is done.** Two safe tickers
  were already identified with the exact verified command to add them; the
  remaining names need a human at a broker screen. Reopen only if one of
  the unresolved names starts blocking a live decision.
- **S5 amended, not reopened under its own number.** The narrower remaining
  question (a fixed-window test across a real >=-30% shock) is tracked as
  the new **S26**, not as a reopened S5.
- **Considered, not opened as a new S-item: second occurrence of the
  scheduled task's stored prompt containing stale premises.** First
  occurrence 2026-08-17, not opened, flagged directly. Second occurrence
  this session, still self-mitigated with no wrong action. **If a third
  occurs, open the S-item without further deliberation** — superseded by
  S27's opening 2026-09-07.

### Closed by the 2026-08-24 discovery-funnel refactor

- **Removed: `data/learning_log.md` and `docs/v2-upgrade-spec.md`.** Both
  were write-mostly and superseded by the dated Council memos and the V2
  Roadmap section above. Git history holds both.
- **S12 — canonical definitions for ambiguous shared terms.** Closed:
  `data/definitions.json` carries both `risk_simulation_base`
  (investable-only) and `investable_capital_convention` (full-portfolio) as
  separate, pinned entries.
- **S13 — CoinGecko fetch had no retry/backoff.** Closed: `fetch_crypto()`
  now retries three times with linear backoff.
- **S15 — journal.md's write-safety instructions lagged its behaviour.**
  Closed: `journal.md` now states the read-whole-file/concatenate/verify
  procedure explicitly.
- **S16 — no dependency manifest.** Closed: `requirements.txt` exists and
  `.claude/hooks/session-start.sh` installs it at session start.
- **S17 — the digest CSV dropped `currency`.** Closed: the candidates CSV
  carries `currency` and `country` per row.
- **S18 — [prospecting] scout's discretionary suggestions had no channel into
  the watchlist.** Closed structurally: `data/watchlist.json` plus
  `scripts/watchlist.py add` and `scripts/scout.py --promote`.
- **S19 — [prospecting] a decimal-scale `--max-debt-to-equity` silently
  produced a false zero-pass screen.** Closed: `scout.py` range-validates
  thresholds and any zero-pass result triggers `diagnose_zero_pass()`.
- **Parked Excel-branch architecture retired.** `scripts/import_excel_holdings.py`
  is the single Excel path, read-only, merging into the persistent
  watchlist.

### Earlier closed items (index)

- 2026-08-24 — considered, not opened as a new S-item: thesis-review incorrectly asserted OPEN_ITEMS.md hadn't been updated with ABB's 2026-08-23 sec...
- 2026-08-24 — considered and rejected: restructuring `reports/ SESSION_LOG.md` away from one growing markdown file to eliminate the overwrite/corrup...
- 2026-08-23 (second pass, same day) — import_excel_holdings.py updated for master-6.xlsx's restructured workbook.
- 2026-08-23 — P8 closed: ISK cash reconciled to 11,288 SEK, real broker figure.
- 2026-08-23 — S12/D4 closed: adopted "target governs sizing" as standing policy for `profit_recycling_rule`, moot in practice once P8 gave a real ca...
- 2026-08-23 — S4 closed: Swedish CPI fetcher fixed and verified.
- 2026-08-23 — S9(c) implemented
- 2026-08-23 — P6's ABB.ST second FI pull run, break condition resolved NOT triggered.
- 2026-08-23 — Three company_profiles P/E figures corrected against real broker data
- 2026-08-23 — P2 closed: remaining item (discovery funnel) is a duplicate of V2 Roadmap Phase 3, not a distinct open item.
- 2026-08-23 — `IMPROVEMENTS.md` deleted.
- 2026-08-18 — S8 closed under cap pressure (10-item limit reached this session, two new evidence-backed items added), not because the underlying ris...
- 2026-08-18 — S14 closed, merged into S15.
- 2026-08-18 — considered and rejected: a new mechanism to prompt/remind the user to execute an unexecuted headline call between sweeps.
- 2026-08-18 — considered and rejected: giving `council` the `Edit` tool instead of just `Read`/`Write`, to simplify its append to `data/learning_log...
- 2026-08-18 — two data-consistency findings this session, judged not yet a pattern worth a new S-item; watching for a second confirmed instance of e...
- 2026-08-17 — S5 resolved: the `backtest` agent ran for real (its first execution ever) and both the current mix and the adopted 85/10/5/0 target cl...
- 2026-08-17 — real code bug found and fixed: `scripts/backtest.py` had never actually worked in this environment.
- 2026-08-17 — Watchlist 12-ticker malformed-format issue CONFIRMED FIXED, closing the same-day addendum above.
- 2026-08-17 — proposal: a standing guardrail checking whether a portfolio-agent rebalancing recommendation conflicts with an open blocking P-item (e...
- 2026-08-17 — P7 closed: ISK allowance threshold confirmed by the user at 300,000 SEK.
- 2026-08-17 — D3 (crypto trip-wire denominator, S12) decided by the user: full-portfolio convention, not Council's recommended investable-only reading.
- 2026-08-17 — Watchlist 12-ticker malformed-format issue confirmed still open, addendum to the 2026-08-12 S10 closure (not a reopening).
- 2026-08-17 — proposal (Maverick, this session's debate): add a second live crypto price source as a tertiary fallback to CoinGecko — rejected.
- 2026-08-17 — proposal: visually distinguish previously-dated-but- unexecuted Council calls in the memo format — deferred, not opened.
- 2026-08-17 — the scheduled task's stored prompt text contradicting CLAUDE.md (twice this session) — not opened as an S-item, flagged directly to th...
- 2026-08-12 — S3 fixed and confirmed (earnings calendar fetch failing).
- 2026-08-12 — S7 fixed and confirmed (self-custody crypto never repriced in `position_report.py`).
- 2026-08-12 — S10 resolved, not just improved.
- 2026-08-12 — Transaction-dedup bug found and fixed the same session, never carried forward as an open item.
- 2026-08-12 — Capital-availability premise check (deferred 2026-08-11 as "one occurrence isn't a pattern") — now resolved and confirmed working.
  **2026-09-07 note: this did not hold.** The same shape of failure recurred
  (2026-08-25 AZN.ST purchase unreported until 2026-09-02, expiring the
  2026-08-31 BUY call) — tracked fresh as **S28**, not reopened under this
  entry, per the never-reuse-ID rule.
- 2026-08-12 — D4 (profit-recycling gross-vs-realized-gain ambiguity) folded into S12, not opened as a separate item.
- 2026-08-11 — S11 fixed and confirmed (two "% of 52-week range" definitions).
- 2026-08-11 — the AZN-vs-Avanza-Global cash-routing premise check (raised as a possible new S-item, deferred, not opened).
- 2026-08-10 — S2 rejected (Form-4 buy/sell direction parsing), cut to hold the ≤10-open-S-items cap.
- 2026-08-06 — `reports/SESSION_LOG.md` lost in the 2026-08-03 merge, unnoticed for 3 days
- 2026-08-06 — Excel import pipeline dry-run bugs found and fixed before the first real run
- 2026-08-03 — The two-branch fork
- 2026-08-03 — Excel as a maintenance burden
- 2026-08-03 — Target allocation written into the files
- 2026-08-03 — ETH quantity
- 2026-08-03 — Theses for Handelsbanken A and Investor A
- 2026-08-03 — Excel `Stocks` data type as a live source
- 2026-08-06 — SUPERSEDES the above, doesn't contradict it.
- 2026-08-03 — Avanza Global TER
- 2026-08-03 — Full account inventory
- 2026-08-03 — The unexplained SEB fund
- 2026-08-03 — Bitcoin certificate vs. self-custody
- 2026-08-03 — Swedish candidate tickers
- 2026-08-03 — Tax-reserve shortfall (~130 SEK)
- 2026-08-03 — FOMC 2026 dates
- 2026-08-03 — Bitcoin certificate price feed
- 2026-07-28 — Avanza ISK itemization
- 2026-07-28 — Handelsbanken wrapper
- 2026-07-12 — Riksbank meeting dates
