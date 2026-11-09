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

**Emphasis:** portfolio-tending.

**Why:** discovery is not the constraint this sweep — S38's cross-check found
this sweep's discovery count genuinely improved on last sweep's zero (12
names entered the candidate set, with WDC, ECHO and MPC confirmed first-seen
across all 12 recorded runs) — while what has already been decided keeps
aging unexecuted. (1) **P3 (PayPal routing) is unexecuted a 14th consecutive
sweep**, and even though two names dropped out of its funding queue this
sweep (AZN.ST and SHB-A.ST both withdrawn on valuation/portfolio-fit
grounds), what's left — gold tranche 2 (~4,930 SEK) and 1 NVDA share — still
sits waiting on the same unexecuted conversion. (2) **Two thesis-status
record-update flags have now sat unapplied across multiple sweeps** (ABB.ST
BROKEN, VOLV-B.ST TOO_EARLY->INTACT) **and a third landed fresh this sweep**
(AZN.ST INTACT->WEAKENING) — three live `portfolio.json` edits waiting on the
user, not a system defect, but worth surfacing together rather than letting
each re-flag separately next sweep. (3) **The DECISION pillar's own numbers
make the case directly**: 21 open BUY calls, median age 35 days, oldest
(VICI) 70 days, with real cost to the delay already visible in the
price-drift table — AZN.ST has moved +11% to +21% away from six separate
unexecuted entry points over the last 9 weeks. (4) **S1 (BTC0E.AS / gold ETC
pricing) enters a 5th consecutive sweep with no live price for either** — a
standing data gap on two live positions, not a new finding, but aging
alongside everything else above. None of this is capital-allocation work
`meta` can do — it is exactly the "human attention" this emphasis field
exists to route.

**Judgement pillar — the pre-committed third-sweep bar is now met. Direct
verdict: this does not lift "the Council must not be weighted," but it does
open the narrower differential-per-voice-trust question the system's own
prior entries said it would.**

This sweep's scorecard: Chairman n=22, median +9.6%, beat baseline 82% — a
third consecutive sweep clearing the n=20 floor, and the best of the three
(n=20/+2.8%/60% -> n=21/+5.4%/71% -> n=22/+9.6%/82%). The Chairman's
synthesis sits at or above every individual voice this sweep except macro
(contrarian +9.5%/77%, defensive +8.6%/82%, macro +12.8%/80%, valuation
+4.4%/61%, copycat +6.1%/69%, fundamental +0.0%/46%, growth -0.3%/42%) — not
just above the voices' median, which is the stronger of the two synthesis
claims this item has been tracking.

The 2026-10-26 entry set an explicit two-part trigger for revisiting the
weighting rule on a third sweep: (a) a reading similar-or-better than the
prior two, and (b) the same per-voice dispersion pattern repeating a third
time (the same voices consistently strong/weak, not noise reshuffling).
**Both conditions are met.** (a) is unambiguous — this is the best of the
three readings. (b) also holds: growth and fundamental are the two weakest
voices a third straight sweep (growth -0.3%/42%, fundamental +0.0%/46% —
still weak, though less negative than the -7.0%/16% and -4.2%/40% seen
across the prior two), while macro and defensive are the two strongest a
third straight sweep (macro +12.8%/80%, defensive +8.6%/82%).

Per the trigger's own stated logic, meeting both conditions does not
authorize a blanket "weight the Council over the mechanical shortlist"
rule — it authorizes taking up the narrower question next: **differential
per-voice trust**. Concretely, the next step worth proposing (not applying —
this is a design change to `council.md`'s Chairman synthesis guidance, for
the user to approve) is to have the Chairman's synthesis explicitly treat
macro and defensive as higher-trust voices and growth and fundamental as
lower-trust voices when they disagree, rather than treating all seven as
equally weighted inputs. This is categorically different from weighting the
Council's output over scout's mechanical shortlist (S33's "ranking is not
adding signal" finding is about the screen, not the Council, and stays
completely untouched by this). **"The Council must not be weighted" (as a
block) stays in force.** Three sweeps of real-n evidence support the
narrower claim already established — that the synthesis step itself adds
value over the voices it's handed — not the broader one, that the
seven-voice block as a whole deserves more weight than the mechanical
shortlist it was handed.

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
- **2026-10-26 note:** still not executed, now a 12th-plus consecutive
  sweep. The funding queue grew to five names (gold tranche 2, AZN.ST, VICI,
  NVDA, and newly SHB-A.ST, sequenced last). Merit unchanged; only the count
  and the queue keep growing.
- **2026-11-02 note:** still not executed, now a 13th consecutive sweep.
- **2026-11-09 note:** still not executed, now a 14th consecutive sweep.
  The queue actually shrank this time — AZN.ST and SHB-A.ST both dropped off
  on valuation/portfolio-fit grounds — leaving gold tranche 2 (~4,930 SEK)
  and 1 NVDA share as what's waiting on the conversion. Merit unchanged;
  fewer names waiting does not mean less urgency, since the fee drag itself
  recurs every ~2 months regardless.
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
- **2026-10-26 — decided fresh, as that rule required, and the result is
  genuinely inconclusive.** The window closed at the 10-20 print (ABB fell
  915.40→825.60, −9.8%, over print week — executing the un-renewed SELL
  before the print would have beaten today's mark by ~90 SEK/share).
  Neither leg of the Chairman's own retire/revive test passed cleanly:
  retire needs op margin >16.9% (passes, 18.67%) **and** forward P/E
  clearly below trailing (fails, 31.01 vs 31.51); revive needs FCF/revenue
  ~4–5% (5.53%, now outside the band, moving toward retirement) **and** a
  flat forward gap (holds). Chairman reads this as inconclusive, not a
  clean mechanical result — SELL ABB.ST, all 4 shares (~3,302.40 SEK at
  825.60), proceeds to 13 VICI, stands at Low confidence, conviction 4,
  fresh judgement rather than a renewed streak.
- **2026-11-09 — the SELL is retired to NO_ACTION, Council correcting its
  own prior case.** The "richest PEG of the trio, 2.71" fact that drove the
  original BROKEN thesis has reversed to 1.24, now cheapest of the three. A
  `thesis_status` edit (BROKEN -> WEAKENING) is flagged for the user to
  apply in `portfolio.json` directly, still unapplied as of this sweep.
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
- **Status:** open — valuable soon, 11th measurement, same conclusion, no
  build attempted
- **Why:** Yahoo's fundamentals coverage is not symmetric across markets.
  The Valuation and Growth lenses both rank partly on forward multiples, so
  a Swedish company can lose a shortlist slot for having no forward
  estimate rather than for being less attractive — a systematic tilt toward
  US names invisible in the output. Full history (eight prior measurements,
  each naming a concrete per-name cost — VOLCAR-B.ST dropping out of the
  candidate set, AZN.ST ranking 59-62 of ~75 despite three Council BUY
  calls) preserved in git log of this file, not re-quoted here.
- **Reviewed 2026-11-09:** unchanged. This sweep's scorecard: `fwd_pe` 69%
  Sweden vs 100% US (31pp spread), `fcf_yield_pct` 19pp spread — both still
  above the scorecard's own >15pp flag threshold, the same band measured
  every sweep since 2026-08-24. AZN.ST's `fwd_pe` is missing again this
  sweep (GAPS section). Eleven unchanged measurements with no build
  attempted; not re-arguing a case already made eleven times.
- **How:** two options, neither large, both fully specified in prior
  entries (git log): (1) report per-market coverage alongside each lens's
  shortlist so the tilt is visible; (2) z-score each lens within a coverage
  cohort, or drop forward-looking fields from a lens's inputs when a name's
  market coverage is below a threshold.
- **Also still open:** no free Nordic/European constituent feed is
  reachable (Wikipedia and Nasdaq Nordic are proxy-blocked), so the Nordic
  block stays user-maintained — a maintenance question, not a capability gap.
- **Improves:** data reliability, decision quality.

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
- **Reviewed 2026-10-26: valuable soon, continuing, unchanged conclusion.**
  TSM's `fcf_yield_pct` sits at 55.43% this sweep (vs 56.22% last sweep,
  same order of magnitude), still completely unflagged. No code fix
  attempted yet; not re-arguing the case, flagging only that it is
  unchanged.
- **Reviewed 2026-11-02: valuable soon, no fresh evidence this sweep —
  carried forward unchanged.** Nothing in this sweep's Council or lens
  output named a new TSM/EVO.ST/HEXA-B.ST data point; not re-arguing a case
  already made.
- **Reviewed 2026-11-09:** valuable soon, no fresh TSM/EVO.ST/HEXA-B.ST
  evidence this sweep — carried forward unchanged.
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
- **Reviewed 2026-10-26: still open, same conclusion.** This sweep's
  scorecard again reads "RANKING IS NOT ADDING SIGNAL" (top-half median
  −2.7% vs bottom-half +0.6%), the same conclusion every sweep since this
  item opened. No new build attempted.
- **Reviewed 2026-11-02: open, same aggregate conclusion, but with a
  genuine counter-example worth recording rather than filing away.** This
  sweep's scorecard again reads "RANKING IS NOT ADDING SIGNAL" (top-half
  median -0.5% vs bottom-half +2.8%), unchanged in sign and magnitude from
  every sweep since this item opened — the aggregate finding stands. But
  VICI's mechanical rank fall (9th->13th->28th across three sweeps) was
  twice waved off under this item's own framing as "just a price effect,"
  and this sweep's Council re-check found real fundamental deterioration
  behind the third fall (trailing EPS -17%, net margin 67.5%->56.5%, net
  debt/EBITDA 4.82->5.46). This does not reverse the aggregate conclusion —
  one name is not a sample — but it is a concrete instance of this item's
  own "ranking carries zero evidentiary weight" framing being applied too
  bluntly twice before being checked a third time. **Refining "how" item 1:**
  the operational rule should read "mechanical rank alone is not evidence"
  rather than "a rank move is never worth a look" — a falling rank is still
  a free, cheap prompt to check the underlying fundamentals before
  dismissing it, even though the rank number itself carries no score.
- **Reviewed 2026-11-09: still open, same aggregate conclusion.** This
  sweep's scorecard again reads "RANKING IS NOT ADDING SIGNAL" (top-half
  median +2.2% vs bottom-half +4.8%), unchanged in sign and magnitude from
  every sweep since this item opened. No new build attempted.
- **How, two parts, not mutually exclusive:**
  1. **Make the non-predictiveness operational, not just descriptive.**
     State as an explicit rule (not left to each sweep's Chairman to
     rediscover informally) that mechanical rank carries zero evidentiary
     weight once the Council is handed a shortlist — it is a surfacing
     mechanism, not a signal. **Refined 2026-11-02:** the rule should
     distinguish "rank carries no score" from "a rank move is never worth
     checking" — VICI's third fall was a free, correct prompt to verify
     fundamentals, not noise to ignore.
  2. **Investigate the value lens specifically**, since it is the one
     consistently anti-correlated lens, not merely flat. Candidate
     hypotheses worth testing against `candidate_history.csv`: value's
     z-score inputs reward falling prices; or value's trailing-multiple
     inputs systematically lag a market already pricing in deterioration.
- **Improves:** decision quality (prevents treating a non-predictive rank as
  if it carries information, while still using a rank move as a free trigger
  to check fundamentals) and system reliability (the MECHANICAL pillar's
  stated purpose currently reads a repeated "no" without any proposal in
  response).

### S34 — [process] No mechanism verifies mandatory pipeline/session outputs actually meet their own stated contract before a sweep ends — now five confirmed specific shapes of the same gap
- **Status:** open — new 2026-10-19, widened 2026-10-26, 2026-11-02 and
  2026-11-09
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
- **Reviewed/widened 2026-10-26: same underlying gap, a different specific
  defect — not closed, not opened as a new ID.** This session's `journal`
  subagent's first draft of today's entry silently rewrote and condensed
  every `SESSION_LOG.md` entry older than 2026-09-07 — collapsing
  historical prose under its own output-length limits — while its own text
  claimed only those pre-09-07 entries were touched; on inspection even the
  entries it called "near-verbatim" (2026-10-12, 2026-10-19) were measurably
  shortened versus the committed original. No number or conclusion was
  altered (verified by direct comparison), but this breaks CLAUDE.md's
  explicit append-only guarantee for the one file this system treats as its
  memory across sessions. Caught by the orchestrating session diffing
  against the pre-session git commit, not by any agent or mechanical check;
  the full original history was restored and re-committed as a clean
  44-line-insertion-only change. This is the same defect shape S34 already
  tracks — nothing mechanically verifies `journal`'s output meets its own
  stated contract before the session is considered done — but a different
  specific failure (content-integrity of an append-only file, not a dropped
  pipeline step). Widening S34 rather than opening a new ID, per this file's
  own precedent for widening on a repeat of the same underlying shape (S27).
- **Reviewed/widened 2026-11-02: a third specific failure shape, same
  underlying gap, no new ID.** This sweep's universe went 34 days stale,
  pushing scout's first run to status DEGRADED; the universe was refreshed
  and scout re-run to VALID. The superseded DEGRADED run had already
  appended its rows to `data/candidate_history.csv` before the refresh —
  those duplicate rows were identified and removed by the orchestrating
  session before the VALID re-run's rows were appended, so this sweep is
  recorded exactly once, not twice. But this was caught by a
  human/orchestrator manually comparing row counts, not by anything
  mechanical — the same defect shape S34 already tracks (a mandatory step's
  output integrity checked by luck, not by design), applied here to a third
  file (`candidate_history.csv`) rather than `SESSION_LOG.md` or the
  journal/meta completion marks. This is also not the first occurrence of
  this specific sub-shape: a same-day scout re-run produced an identical
  orphaned-duplicate-row-block problem on 2026-09-28, closed at the time as
  "no recurrence since, not reopening." It has now recurred. Widening S34's
  "How" with a third check rather than reopening that closed note under a
  fresh ID, since the underlying gap is identical.
- **Widened 2026-11-09: two more specific instances of the same underlying
  gap, no new ID.**
  (d) **`SESSION_LOG.md`'s own size is now a recurring operational
  problem, not a one-off.** This is the second consecutive sweep
  (2026-11-02, now 2026-11-09) where `journal`'s own write-safety rule
  (read the whole file before rewriting) could not be satisfied in one
  LLM-context pass — the file is now 2807 lines. Both times the
  orchestrating session had to splice the entry in via a script-level
  head/cat/tail instead of `journal` writing it directly (verified
  byte-identical on the untouched portion both times, so no data was
  lost) — but the mechanism is fragile and gets worse every sweep the file
  grows, and this is the exact failure mode behind the 2026-10-26 near-miss
  this item already tracks (journal's own draft silently condensing
  pre-2026-09-07 history). Likely fix: roll older entries into a dated
  archive the way `portfolio_history_archive.md` already does for
  `portfolio.json`, or give journal an append-only tool that doesn't
  require a full read.
  (e) **`check_unmerged_work.py` — the exact script this item's own "How"
  section names as the natural home for these checks — has a real blind
  spot, found pre-sweep.** It only checks named branches (`refs/heads`,
  `refs/remotes/origin`) against `main`; it never checks whether HEAD
  itself is detached and holding commits invisible to both. This sweep
  found the entire 2026-11-02 sweep (5 commits) had been made on a detached
  HEAD, never reached `main`/`origin`, and the script had reported "Clean"
  the whole time those commits sat one `git` operation away from
  unreachable. Fast-forwarded `main` onto them and pushed before this sweep
  started — no work was lost, but the detection gap is real. One-line fix:
  check if `git symbolic-ref -q HEAD` fails (detached) and, if so, whether
  HEAD holds commits not on `main`.
- **How:** deterministic, no new agent, five checks now.
  (a) The original S34 check: before the session is allowed to be
  considered complete, verify (i) `reports/SESSION_LOG.md`'s newest entry
  date matches the latest market-data snapshot's date; (ii)
  `reports/system-scorecard.md`'s generation timestamp is on or after the
  latest Council memo's; (iii) `OPEN_ITEMS.md` was modified in the same
  session as the latest memo, or an explicit "no changes this sweep" is
  recorded. (b) The content-integrity check: diff the new `SESSION_LOG.md`
  against the previous commit's full content and assert the old file's
  entire text still appears, unmodified, as a prefix of the new file — not
  just a line-count floor, since a rewrite that keeps overall length roughly
  similar would pass a count check but fail a real diff. Concretely: compare
  the new file's content against `git show HEAD:reports/SESSION_LOG.md`
  (the pre-session commit) and assert the old content is an exact prefix of
  the new one. (c) Before appending scout's output rows to
  `data/candidate_history.csv`, check whether a row block for the same
  run-date (or snapshot timestamp) already exists in the file and either
  skip the append or flag it loudly rather than silently duplicating — a
  few lines in `scripts/scout.py` or `watchlist.py history`, checked
  against the file's own run-date column before writing. (d) Before the
  session is considered done, check `SESSION_LOG.md`'s line count against a
  threshold (e.g. 2,000 lines) and flag loudly that older entries should be
  rolled into a dated archive file, rather than relying on journal
  successfully reading an ever-growing file every sweep. (e) Add the
  detached-HEAD check described above to `check_unmerged_work.py`. If any
  check fails, flag it loudly (a printed warning, a non-zero exit) rather
  than silently ending — the same philosophy CLAUDE.md's step 7
  (`check_unmerged_work.py`) already applies to the two-branch-fork
  problem, applied here to five related failure shapes instead of one. A
  few lines added to `check_unmerged_work.py` or a sibling script would
  catch all five mechanically next time rather than by luck.
- **Improves:** system reliability (a dropped mandatory stage, a silently
  corrupted memory file, a duplicated history row, an ever-growing log file
  journal can no longer safely read, or an invisible detached-HEAD fork are
  currently only detectable by luck) and, indirectly, decision quality
  (every pillar the scorecard measures depends on every sweep being
  logged, intact, and reconciled exactly once — an invisible, corrupted,
  doubled or unmerged sweep is a silent gap in the only calibration
  mechanism this system has).

### S38 — [discovery/data] `source=new` mislabels how many candidates are genuinely first-seen, and this sweep the miscount reached zero — the scorecard's own DISCOVERY pillar inherits the error
- **Status:** open — new 2026-11-02, promoted from a standing watch note
  first flagged 2026-10-05 and left unopened under cap pressure for five
  consecutive sweeps
- **Why:** `scout.py`'s `source=new` label means "not currently held or
  watchlisted," not "first seen in `candidate_history.csv`." This has been
  independently caught and corrected in the Council memo's own prose every
  single sweep since 2026-10-05 — 10-05 (only 5 of 35 genuinely new), 10-12
  (only GM of 33), 10-19 (only AZA.ST/FSLR of 35), 10-26 (only WIHL.ST of
  34) — with zero downstream wrong action each time. The 2026-11-02 sweep's
  count reached zero: of 34 rows carrying `source=new`, cross-referenced
  against all 12 recorded runs at the time, none were genuinely first-seen.
  Every prior sweep's miscount was at least framed as "fewer new names than
  the label implies"; that sweep's true answer was a legitimate "we found
  nothing new," which is exactly the kind of result CLAUDE.md says must
  never be conflated with "the funnel is working normally" — and the
  current label hides that distinction. It also means the scorecard's
  DISCOVERY pillar line itself is not just imprecise, it can be wrong about
  the one number that pillar exists to report.
- **Reviewed 2026-11-09:** mislabel still unfixed, but this sweep's
  underlying discovery count was genuinely better than last sweep's zero.
  Of the 12 `source=new` rows, WDC, ECHO and MPC are confirmed first-seen
  across all 12 recorded runs (the other 9 weren't individually checked).
  This is evidence the funnel is surfacing fresh names again, not evidence
  the label problem is fixed — `source=new` still conflates "genuinely
  new" with "not held/watchlisted," so the count still needs a manual
  cross-check every sweep until the column itself is fixed.
- **How:** rename the column (e.g. `source=not_held`) or add a true
  `first_seen_date` column, populated by checking `candidate_history.csv`'s
  full run history before writing a row's status — the fix already
  specified in the 2026-10-05 note, unchanged and still cheap. No design
  question remains; this needs code, not more deliberation.
- **Improves:** data reliability (the DISCOVERY pillar's headline figure is
  currently wrong, not just loosely worded) and decision quality (a human
  reading a "new" count assumes the funnel is actively surfacing fresh
  opportunity when that has not always been true).

### S39 — [data] Avanza Global and Avanza Auto 3 — roughly 80% of the equity sleeve by value — have gone 14-15 weeks with no price-mark refresh, and no pipeline step owns fund NAVs
- **Status:** open — new 2026-11-02
- **Why:** this sweep's `portfolio` lens found Avanza Global and Avanza
  Auto 3 — together ~80% of the equity sleeve, ~136,000 SEK of the
  ~223,644 SEK total portfolio value the scorecard's OUTCOME pillar reports
  — have not had their price marks refreshed since 2026-07-24/07-28 (14-15
  weeks). `fetch_market_data.py` refreshes individual-stock prices every
  sweep but has no equivalent step for fund NAVs, so these two holdings have
  been silently carried at a mark that is three-and-a-half months old while
  every other position in the portfolio is repriced weekly. This is a
  bigger single-field blind spot than any other data gap currently tracked:
  every allocation percentage, every ACT/WATCH concentration flag, and the
  scorecard's own OUTCOME figure implicitly rest on a stale mark for the
  majority of the portfolio's measured value.
- **How:** check whether Yahoo quoteSummary (or another free source already
  used elsewhere in this system) exposes a NAV field for these two fund
  ISINs/tickers; if so, add them to `fetch_market_data.py`'s regular fetch
  list the same way individual equities are handled. If no free source
  reaches them, the gap should be named explicitly — a `KNOWN_STALE` flag on
  the holding in `portfolio.json`, the same treatment S1 already applies to
  BTC0E.AS — rather than silently carried at a 15-week-old mark with no
  indication anywhere that it is stale.
- **Improves:** data reliability (the single largest coverage gap found on
  real portfolio value this session) and decision quality (every
  allocation and concentration call this sweep implicitly assumed a price
  that is 14-15 weeks old for most of the money it was weighing).

### S40 — [process] FI insider `bs4` dependency failure reopened a third time; this time the structural fix was actually applied to `session-start.sh`
- **Status:** open — new 2026-11-09 (fresh ID per S36's own closing
  instruction); watching for a second clean sweep to confirm durability,
  not yet "fixed"
- **Why:** S36 closed 2026-11-02 on two consecutive clean sweeps, with an
  explicit warning that the structural fix (`.claude/hooks/session-start.sh`'s
  bare `pip install` -> `python3 -m pip install`) had never actually been
  applied to the repo, and instructed: "apply the one-line `session-start.sh`
  fix at [the next failure] rather than relying on the environment holding
  by luck a third time." This sweep the `bs4` import failed again on the FI
  insider fetch — exactly the predicted recurrence. Fixed the same way as
  before mid-session (`python3 -m pip install beautifulsoup4`), and this
  time the orchestrating session also applied the actual structural fix:
  `.claude/hooks/session-start.sh`'s bare `pip install -q -r requirements.txt`
  changed to `python3 -m pip install -q -r requirements.txt`
  (`requirements.txt` already lists `beautifulsoup4>=4.12`).
- **How:** fix applied this session; nothing further to do except confirm
  it holds. Status should read "watching," not "fixed," until a sweep runs
  cleanly with the new `session-start.sh` line already in place from the
  start, not applied mid-session again.
- **Improves:** data reliability (the FI insider fetch, used for Swedish
  holdings) and system reliability (a dependency-install bug that has now
  cost three sweeps of mid-session manual recovery).

### S41 — [data] Price and EPS fields in the snapshot are not drawn from the same fetch moment, overstating absolute P/E on names that moved sharply the same week
- **Status:** open — new 2026-11-09
- **Why:** during an AI/memory-hardware sell-off week (VIX 17.2 -> 28.18),
  Council found that for several of the week's biggest fallers (NVDA, MU,
  SNDK, AVGO, FIX), the implied trailing AND forward EPS each moved by a
  percentage matching that name's own price move for the week (-6.2% to
  -16.4%) — a pattern consistent with EPS being derived from price rather
  than fetched independently, rather than price and EPS-derived fields
  being captured at the same instant within a single fetch. Net effect:
  absolute P/E multiples on names that moved sharply this week are
  overstated by roughly the price move's own percentage. Forward/trailing
  ratios and PEG-style reasoning, which depend on the ratio between two
  EPS-derived figures rather than an absolute multiple, are unaffected —
  this is a fetch-moment-skew mechanism, not the currency-unit mechanism
  S32 already tracks, so it is opened fresh rather than folded in.
- **How:** locate where `fetch_market_data.py` or `derived_metrics.py`
  derives `trailing_eps`/`forward_eps` versus where `price` is read — check
  whether EPS is being computed by dividing a cached/trailing price by a
  separately-fetched P/E rather than pulling Yahoo's own
  `epsTrailingTwelveMonths`/`epsForward` fields directly, which would
  explain exactly this symptom (EPS tracking a price move it shouldn't).
  Confirm against one name (e.g. NVDA) by comparing the snapshot's raw
  `quoteSummary` response fields directly.
- **Improves:** data reliability (an overstated absolute multiple on
  exactly the names most likely to be under Council scrutiny in a sell-off
  week) and decision quality (valuation reasoning on fast-moving names
  during volatile weeks).

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
  supports a rolling N-year lookback, no fixed `--start`/`--end` — see S26,
  downgraded to a quiet watch item but not yet re-tested), and score
  calibration. `data/candidate_history.csv` is the calibration store this
  phase asked for — mechanical rank per candidate per run, correlatable
  against realised returns later. It records the funnel's ranks, not each
  voice's conviction; that is Phase 7d.
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
    its own inputs. The Chairman-vs-voices comparison, which is what would
    justify ever weighting the Council, cleared n=20 for the first time
    2026-10-26 (n=20, median +2.8%, beat 60%), cleared it a second, better
    time 2026-11-02 (n=21, +5.4%, beat 71%), and cleared it a third, better
    time still 2026-11-09 (n=22, median +9.6%, beat baseline 82%) — the
    pre-committed third-sweep bar (set 2026-10-26) is now met. See this
    file's "This sweep's recommended emphasis" block for the full verdict:
    the Council-as-a-block weighting rule stays in force, but the narrower
    differential-per-voice-trust question (macro/defensive consistently
    strong, growth/fundamental consistently weak across all three sweeps) is
    now live, not yet applied. **The Council must still not be weighted as a
    block; differential per-voice trust is the next question, not yet
    applied.**

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
outstanding rather than what is finished. Nothing was deleted — earlier
closures' full text is preserved in this file's own git history.

### Closed by the 2026-11-09 session

- **S27 — closed under cap pressure (room needed for new evidence-backed
  items this session: S40, S41), not because resolved.** At least a
  twelfth confirmed occurrence this sweep (the Handelsbanken-wrapper/
  `reference_targets` premises again declined before running anything; the
  narrowed ethereum-only crypto-fetch variant again fetched bitcoin too
  anyway per CLAUDE.md's canonical command). Every occurrence across twelve-
  plus sweeps has self-mitigated before any wrong action, and the lever (the
  scheduled task's stored prompt) is outside this repository, with the
  user, fully specified since 2026-09-07. Logging a thirteenth identical
  occurrence count was adding nothing new. Reopen (fresh ID) if a future
  occurrence is NOT self-caught — i.e., if the drift is ever found to have
  actually driven a wrong action rather than being caught and corrected or
  overridden first.
- **S35 — closed under cap pressure (room needed for new evidence-backed
  items this session: S40, S41), not because resolved.** Unapplied for
  nine consecutive sweeps; 2026-11-02 instructed "stop re-deriving S35" and
  this sweep correctly did not (see the Considered-not-opened note below —
  no fresh re-derivation was attempted). The one-line JSON fix remains
  fully specified and can be applied directly by the user at any time, no
  further deliberation needed. Reopen (fresh ID) only if a future sweep
  shows live disagreement return, or if the stale file is ever shown to
  have actually driven a wrong ACT/WATCH read rather than just prompting a
  redundant confirmation.

### Considered by the 2026-11-09 session, not opened

- **S31 recheck — confirmed NOT a reopening; the predicted harmless
  workaround held again.** This sweep's `journal` agent was invoked with no
  Bash tool and could not run `scripts/scorecard.py --write` itself; the
  orchestrating session ran it afterward — exactly the pattern S31's
  2026-10-19 closure anticipated and accepted ("every occurrence was a
  correctly-sequenced manual workaround... reopen only if a future
  SESSION_LOG entry is ever found to have quoted a stale scorecard figure as
  current"). No mislabeled or stale figure was quoted this sweep. S31's
  underlying cause (`journal.md`'s Mode 2 step 4 instructs journal to run
  `scorecard.py`, which it structurally cannot do with Read/Write-only
  tools) is still unfixed in the repo, but the closure's own reopen bar was
  not met — not reopening.
- **Council self-corrected three of its own prior-sweep errors this
  session** (thesis-review's stale "larger insider volumes" claim on
  SHB-A.ST/VOLV-B.ST; portfolio's wrong "S26 still open" claim; a minor
  ABB.ST board-count error) — the adversarial Council-over-lenses check
  working as designed, zero downstream wrong action. Not an S-item;
  recorded as a positive data point alongside the JUDGEMENT pillar's
  quantitative case, since it is a different kind of evidence for the same
  question (does the Council's existence earn its keep).

### Closed by the 2026-11-02 session

- **S36 — closed: stable, two consecutive clean sweeps.** The FI insider
  `bs4` failure first seen 2026-10-12 recurred identically 2026-10-26 (fixed
  mid-session via `python3 -m pip`) and then did **not** recur at all this
  sweep — all 7 Swedish issuers fetched cleanly on the first attempt. This
  close is on observed stability, not on the originally-diagnosed structural
  fix landing: `.claude/hooks/session-start.sh` still runs the bare `pip
  install -q -r requirements.txt` the fix recommended changing to `python3
  -m pip install`, unapplied in the repo as of this session. Reopen (fresh
  ID) on the next `bs4`/FI-insider dependency failure, and apply the
  one-line `session-start.sh` fix at that point rather than relying on the
  environment holding by luck a third time. **It did recur — see new S40,
  2026-11-09, which also applied the structural fix this note called
  for.**
- **S37 — closed: the scope-widening fix this item asked for was applied
  and worked.** This sweep's calendar fetch was extended beyond
  holdings-only to the full focus/candidate set (per S37's own "How") and
  surfaced real collisions the holdings-only scope would have missed — APP,
  SMCI, FIS and TPL earnings colliding with the 11-04 Riksbank decision. The
  residual finding — all 5 Swedish-industrial holdings still return
  already-past earnings dates even under the widened scope — is a
  different root cause (Yahoo data staleness specific to those 5 tickers,
  confirmed by the scope-fix working correctly for every other name) and
  has not been shown to cost a live decision the way the original
  holdings-only gap cost VICI's FOMC-week visibility. Reopen (fresh ID) if a
  live decision is ever shown to depend on a correct forward-looking Swedish
  earnings date while the Yahoo staleness is still blocking it.
  **Addendum 2026-11-09, not a reopening:** this sweep several non-Swedish
  US names (ECHO, FIS, TPL, APP) also returned already-past earnings dates,
  and Council's read is that Yahoo likely just returns the last-reported
  date until the next one is scheduled/confirmed — i.e., APP's "past" date
  was literally last week's real print, not a data gap. If this holds up,
  the residual finding this item's 2026-11-02 closure called
  "Nordic-specific staleness" may actually be a general Yahoo-field
  behavior, not specific to the five Swedish-industrial holdings. Unproven;
  not reopening without a case where it's shown to actually cost a live
  decision, per this item's own already-stated reopen bar.

### Considered by the 2026-11-02 session, not opened

- **ABB.ST's May insider "buying" cluster (six directors, one identical
  price, one identical date) looks like a scheduled board-fee share
  allocation, not conviction buying — a mechanical artifact in the FI
  insider feed, not a real signal.** First confirmed instance of this
  specific pattern; not opened on one occurrence, per this file's own
  standing bar. Watching for a second instance of a board-fee-shaped cluster
  (several insiders, one price, one date) being read as a conviction signal
  on any name before proposing a mechanical filter (e.g. flag clusters where
  three or more insiders trade at an identical price on an identical date as
  "scheduled," not "buying").
- **Two small Council self-reported process issues, both caught and fixed
  before reaching `decisions.csv`, neither opened.** (1) The picks CSV wrote
  "NO ACTION" instead of the required `NO_ACTION` enum value — caught and
  fixed by the orchestrating session before recording. (2) The Fundamental
  voice's memo prose lists APP before NVDA despite NVDA's higher score
  (2.541 vs 2.532) — a display-order slip only, the underlying figures are
  correct. Both low-severity, both self-caught with zero downstream effect.
  Watching for recurrence of either before proposing a fix (a stricter
  picks-CSV validator for (1); nothing proposed for (2), it is cosmetic).

### Closed by the 2026-10-26 session

- **S29 — closed under cap pressure (8-item cap; new S36/S37 opened this
  session), not because resolved.** Two consecutive sweeps (2026-10-19,
  2026-10-26) produced no fresh evidence of the `pct_52w_range` gap capping
  a live Top-5 conviction — APP, the name this item was argued on, did not
  even surface the issue this sweep. The one-column fix (`week52_high`/
  `week52_low` in `scout.py`'s candidate CSV, sourced from fields the
  snapshot already fetches) remains fully specified and can be applied at
  any time without further deliberation. Reopen (fresh ID) if a future
  sweep again shows a live conviction score measurably capped by this gap.
- **S26 — closed under cap pressure (8-item cap; new S36/S37 opened this
  session), not because resolved.** Two consecutive reviews (2026-10-19
  "can wait, downgraded from top-priority"; 2026-10-26 "no fresh forcing
  evidence, unchanged") found nothing new: `data/backtests/` is presumed
  still absent, and the −30% drawdown tolerance is still unverified against
  any real shock. D-c's own acute pressure, which is what escalated this
  item in the first place, is now tied purely to the BTC0E.AS pricing gap
  (unevaluable a third consecutive sweep, S1-adjacent), not to this item's
  backtest-window gap. The already-specified fix (a fixed-window backtest
  over a real >=-30% shock, written to `data/backtests/`) remains unapplied
  and fully specified. Reopen (fresh ID) if D-c's new band is ever shown at
  risk of firing without a real backtest behind it, or if the property-goal
  glidepath re-anchor trigger arrives first.

### Closed by the 2026-10-19 session

- **S6 — closed under cap pressure (two new evidence-backed items opened
  this session: S34, S35), not because the underlying gap is resolved.** No
  free NAV/discount source for INVE-A.ST or Industrivärden has been found.
  But the 2026-09-28 Option-3 fallback (hold the 5 shares, stop
  re-flagging) has now held for three consecutive sweeps including through
  the 2026-10-07 trigger window, and this sweep's SESSION_LOG confirms it was
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
  actually fails. **Rechecked 2026-11-09: recurred identically, still a
  harmless workaround, reopen bar still not met — see the Considered-not-
  opened note for that session.**

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
  since 2026-10-05, with zero wrong action on any occurrence. **Update
  2026-10-26: a fifth explicit catch** — of 34 `new` rows, only WIHL.ST is
  genuinely first-seen. **Superseded 2026-11-02 — see new item S38**,
  opened once the miscount reached zero genuinely-new names and was shown to
  directly corrupt the scorecard's own DISCOVERY pillar figure, not just
  memo prose.

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
  opened as a new item.** **Update 2026-11-02: it recurred** (a DEGRADED->
  VALID re-run produced the identical shape, caught and removed manually
  again) — see widened **S34**, which now carries this specific sub-shape
  going forward rather than this closed note.
- **The calendar fetch covered portfolio holdings only this sweep, and a
  live Top-5 BUY (VICI) lost its earnings date as a result — not opened as a
  new item.** **Update 2026-10-19:** this has now recurred every sweep
  since (calendar holdings-only again 2026-10-05, 10-12, 10-19), a
  standing regression rather than a one-off. Still not opened as a formal
  S-item under the 8-item cap this session, since it has not yet been shown
  to cost a live decision the way VICI's missing date did the first time it
  was observed — but this is now a repeated, not single, occurrence, and
  should be opened on the next sweep where a live candidate's earnings date
  gap is shown to matter, without further deliberation. **Update
  2026-10-26: it just did, and it is now S37** (cap room made via S26's
  closure, see above) — VICI lost its date again, inside FOMC week, and the
  gap also blocked a clean post-print retest of ABB.ST. **Closed 2026-11-02
  — see the 2026-11-02 Closed-by session above.**

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
  `.claude/hooks/session-start.sh` installs it at session start. **Note
  2026-10-26: the install mechanism itself turned out to have a latent bug
  — see new S36 — so this closure covered the manifest's existence, not the
  reliability of its installation.** **Note 2026-11-02: S36 is now itself
  closed (stable two consecutive sweeps), but the underlying `session-start.sh`
  one-liner this note flagged is still unapplied — see S36's closed entry.**
  **Note 2026-11-09: the one-liner is now actually applied — see new S40.**
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
</content>
