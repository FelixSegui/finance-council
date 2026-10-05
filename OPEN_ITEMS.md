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

**Emphasis:** portfolio-tending

**Set by the 2026-10-05 review.** Three dated, live capital questions are
open at once, and none of them need more analysis from this system — they
need the user's one-line decisions. **D-c (the BTC0E.AS trim) is re-opened**
this sweep: the 2026-09-28 memo wrote "Applied: Option 1 — trim ~2,500 SEK"
for a trade this system never executed — `portfolio.json` still shows the
pre-trim 150 units, and that same sweep's own SESSION_LOG said plainly "User
decisions: none." The position is unchanged; the only blocker is the user
confirming current status in one line, not a missing number (see S27 below).
**D-a (SELL ABB.ST / BUY 17 VICI) now carries an explicit lapse condition**:
this sweep's Chairman re-tested the SELL from scratch rather than carrying it
an eighth time, and it survives at lower conviction (7→6) — but if it has not
executed before ABB's **2026-10-20** earnings print, 15 days from today, the
call lapses outright and the next memo re-decides ABB fresh rather than
carrying a streak. **S6's NAV re-entry trigger lands in two days**
(2026-10-07, Investor AB and Industrivärden Q3 reports) — closing an
eight-sweep-old gap that has cost a Council voice its call every single
sweep, for about ten minutes of work. Underneath all three, **AZN.ST's BUY
remains unfunded** (845.43 SEK of ISK cash against a 1,599.00 SEK share) and
**P3 (the PayPal conversion) is still unexecuted for a 9th-plus consecutive
sweep**, now the binding constraint on the AZN share, gold tranche 2, and the
cash overweight at once. None of this calls for new Council depth — the
analysis already exists, repeatedly — it calls for the user reviewing three
converging dates and either acting, declining, or explicitly re-deciding.
Discovery stays a secondary watch item this sweep: the funnel is VALID with
genuine production at the margin (5 names genuinely first-seen this run —
CTVA, GPN, PLTR, EOG, TEL2-B.ST, per this sweep's correction to how "new"
should be read, see the Closed log below), but the head of the funnel (APP,
SNDK, NVDA, MA, V, TSM, INDU-C.ST, VICI) has now held top-10 in all 7 runs on
record with nothing new to chase there this week — attention is better spent
on the dated decisions above than on re-running discovery depth that would
surface the same frozen head again.

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
  is NAV discount/premium and it has never been obtained. See S6.
- **2026-08-18 note:** Council's Contrarian voice this sweep independently
  flagged INVE-A.ST as SELL-worthy on exactly this gap ("the opposite of a
  contrarian holding — it is a crowded one I cannot measure"), resolved to
  HOLD only because the missing metric, not confidence, is the reason. Adds
  weight to S6 without changing P5's own status.
- **2026-08-24 note:** the Contrarian voice flagged it again — second
  consecutive sweep the same gap blocked a real call — resolved to HOLD on
  the same missing-data grounds. Now also tracked as open decision **D-b**
  below: get the NAV per share (Excel request H, ~10 min), sell on
  absence-of-evidence, or keep holding and stop re-flagging.
- **2026-08-31 note:** third consecutive sweep the same gap blocked the same
  voice's call (Contrarian again, plus Copycat reading only "acquisitions,
  no disposals"). D-b unchanged, now costing a voice's attention every
  single sweep — see S6.
- **2026-09-07 note:** fourth consecutive sweep, and now a genuine
  disagreement rather than a single blocked voice — Contrarian still wants
  to sell (91% of range, no measurable valuation) while Copycat's FI pull
  shows the CEO buying personally and repeatedly through 2026 at rising
  prices (most recently 850 sh above today's price, 2026-09-01). The
  Chairman's pick is Option 1 (get the NAV number) — see D-b.
- **2026-09-14 note:** fifth consecutive sweep, and the disagreement moved
  rather than resolved. The Contrarian voice stood down this sweep on new
  primary evidence — Jacob Lund bought 1,000 A-shares at 399.13 SEK on
  2026-09-09, within 0.1% of today's price — the first datapoint suggesting
  someone who can see the NAV thinks this price is acceptable. That is not
  the missing number itself, and the Council memo says so plainly: it
  "resolves nothing, it just moves the deadlock." D-b unchanged; see S6.
- **2026-09-21 note:** sixth consecutive sweep, and the Copycat case
  strengthened further — three separate insiders bought in the last three
  weeks (CEO Cederholm, Jacob Lund, Ulrika Elfving), five distinct
  individuals through 2026 at rising prices, zero disposals. Valuation and
  Fundamental still have no usable metric at all. The Chairman's own words:
  "the insider evidence got stronger this sweep... which makes the missing
  number more expensive, not less necessary." Chairman's pick is still
  Option 1 (get the NAV, Q3 report lands 2026-10-07); stated fallback if a
  seventh sweep passes with nothing done is Option 3 (stop re-flagging).
  See S6, D-b.
- **2026-09-28 note:** seventh consecutive sweep, and the pre-committed
  fallback fired as stated. No new NAV number arrived, so this sweep's
  Council formally applied **D-b Option 3**: hold the 5 shares, stop
  re-flagging until the NAV exists. Single re-entry trigger: a NAV figure
  recorded from Investor AB's **2026-10-07** Q3 report — nine days from this
  review. See S6.

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
    the three (P/E 37.3x, forward P/E essentially flat at 36.9x despite
    14.2% ttm revenue growth — a margin-compression flag), thinnest FCF
    conversion (~4.4% margin), a raw-data currency-mismatch finding (Yahoo's
    P/S 49.3x / P/B 110.9x are USD/SEK-unit artifacts — FX-corrected to
    ~5.2x / ~11.7x, see `data/company_profiles/ABB.ST.json`), and a recent
    (last 2-3 weeks) insider-selling cluster: senior executive Peter
    Terwiesch made three separate disposals (~48,800 shares / ~CHF 3.85M,
    07/31-08/14) plus a board-member disposal.
  - None breach the 15% single-position cap or even reach the "normal" 3-8%
    band — each is ~1.8-2.4% of the portfolio, so this is a quality/rotation
    call, not a sizing one. **Recommendation:** do not add to any of the
    three at current valuations (all PEG > 2); hold ATCO-B.ST and ALFA.ST
    (thesis intact on fundamentals, just expensive); treat ABB.ST as the
    active rotation candidate if/when better-vetted capital needs a home —
    the weakest score, richest and most data-flagged valuation, and the only
    one with a live insider-selling signal.
  - Full scored detail, sourcing, and quality-state flags for every figure:
    `data/company_profiles/ATCO-B.ST.json`, `ALFA.ST.json`, `ABB.ST.json`
    (`review_history`, dated 2026-08-17).
- **2026-08-17, same-day live session — the review's finding became
  operational without yet triggering a trade.** Council's Call 4: hold all
  three, no adds/trims, with ABB explicitly first in line if/when capital
  needs a home from any source other than new money. ABB's own
  `break_conditions` (written the same morning from the FI data) require the
  insider-selling pattern to continue into a *second* FI pull before firing
  as an active reduce signal — this was the first pull, so the Chairman
  declined to override a condition written from real data on its first
  observation. Watch for the next FI pull before 2026-09-03.
- **2026-08-18 note — the second FI pull still has not run, second
  consecutive sweep.** Council resolved ABB.ST to HOLD-WATCH again on the
  same untested-condition grounds, three of six voices would SELL on
  valuation/beta/cash-conversion grounds independent of the insider signal.
  This is now the concrete action item most directly ahead of the
  2026-09-03 date.
- **2026-08-23 — second FI pull RUN, break condition resolved: NOT
  triggered.** `scripts/fetchers/fetch_insiders_se.py --issuer ABB` (this
  environment's marknadssok.fi.se access, previously believed blocked, is
  confirmed reachable again as of today) returned the same Peter Terwiesch
  disposal cluster already on record (48,799 sh combined, 07/29-08/13) plus
  David Meline's 2,456 sh disposal — no new transactions in the 10 days
  since. The break condition ("insider selling continues into a second
  pull") requires the pattern to *continue*; it has gone quiet instead.
  ABB.ST stays HOLD-WATCH on its existing valuation/FCF-conversion
  concerns, not escalated to an active reduce signal from insider activity.
  **This closes out the 2026-09-03 default date — no further FI pull is
  needed for this condition.** Full detail:
  `data/company_profiles/ABB.ST.json`'s `insider_activity_cache`.
- **2026-08-24 — ESCALATED to SELL, on the break condition's *other*
  clause.** Clause one (insider selling continuing) tested negative
  2026-08-23 and closes in ABB's favour. Clause two, written the same
  morning — "re-test if a materially better-positioned Nordic-industrial
  alternative surfaces via screening" — has now been quietly satisfiable
  for three sweeps, and this sweep's Council formally acted on it: SELL
  all 4 shares (~3,775 SEK), proceeds proposed to fund META (see the
  memo's Top 5 #2/#3 and new open decision **D-a** below for the three
  live options on where the freed-up slot goes). Not yet executed by the
  user.
- **2026-08-31 note — SELL reaffirmed a second consecutive sweep**, price
  essentially flat (938.40, -0.6% week-over-week), conviction 7. Proceeds
  now proposed for VICI rather than META — third destination in three
  sweeps (GOOGL → META → VICI), none executed. See D-a.
- **2026-09-07 note — SELL reaffirmed a third consecutive sweep, conviction
  7, and the record finally caught up with the decision.** ABB's
  `thesis_status` field was corrected from WEAKENING to BROKEN this session —
  it had not been updated after the 2026-08-24/08-31 escalations, leaving it
  contradicting the system's own live SELL call for two full sweeps. ABB's
  own numbers actually improved slightly since the 2026-08-17 review (P/E
  37.3 → 35.3, PEG 2.71 → 2.11); the field changed because the record was
  finally written, not because the business deteriorated further. This
  sweep's FI pull also confirms the insider-selling clause has now tested
  negative *twice* (2026-08-23 and 2026-09-07 both return the identical
  Terwiesch/Meline transactions already on record since 2026-08-23) — the
  SELL now stands on valuation alone. Proceeds still proposed for VICI
  (second consecutive sweep at that destination) — see D-a. Still not
  executed.
- **2026-09-14 note — SELL reaffirmed a fourth consecutive sweep, conviction
  7, cost of the delay still near zero.** ABB was 924.60 on 2026-08-25 and is
  926.60 today, +0.2% — the point is not that waiting is costly, it is that a
  decision reaching a fourth sweep unactioned stops being a decision.
  Thesis-review independently reached BROKEN from this sweep's own numbers,
  without being shown the Council's prior calls — an independent
  confirmation, not a repeated opinion. Proceeds still proposed for VICI
  (third consecutive sweep at that destination) — see D-a. Still not
  executed.
- **2026-09-21 note — SELL reaffirmed a fifth consecutive sweep, conviction
  7, and ABB's price finally crossed above its own cost basis (948.40 vs
  946.96), which does not weaken the case — this is a valuation/cash-
  conversion SELL, not a momentum call.** The Chairman's own words: "a call
  reaching a fifth sweep unexecuted is no longer a decision, it is a
  habit." Proceeds still proposed for VICI (fourth consecutive sweep at
  that destination) — see D-a. `portfolio` §1 now rates equity sector
  concentration formally ACT (Industrials 54.05% of the stock sleeve, >45%
  line); executing this SELL and the linked VICI BUY takes Industrials to
  42.6%, below the ACT threshold for the first time. Still not executed.
- **2026-09-28 note — SELL reaffirmed a sixth consecutive sweep, conviction
  7, and the Chairman named this the last sweep the call is carried as a
  live recommendation.** ABB rose again (966.20 vs 948.40, +1.9%), still not
  vindication — this is a valuation/cash-conversion SELL and a higher price
  only raises the proceeds. **The sale's timing and destination are now
  explicitly decoupled:** sell before ABB's **2026-10-20** print regardless
  of what happens with VICI; the Industrials-concentration fix (53.98% of
  the stock sleeve, ACT) still needs the VICI leg specifically — holding the
  proceeds as cash only gets Industrials to ~47.9%, still ACT. If this has
  not executed before the 10-20 print, the 2026-10-05 memo re-tests the call
  from scratch rather than carrying it a seventh time. See D-a.
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
  backed with a real physical-delivery right (1g gold per note, not a
  cash-settled synthetic), extremely low cost (official PRIIPs cost
  disclosure: 0.07%/yr in year 1, 0.01%/yr annualized over 5 years — near
  the cheapest instrument in the portfolio), listed on a regulated
  exchange (Frankfurt). Disclosed risk 5/7 and issuer/counterparty
  exposure (an unsecured claim on the SPV issuer if it can't perform) are
  real but standard for the entire ETC asset class, not a defect specific
  to this instrument. **This is OK to buy.** Only remaining check: confirm
  it's searchable/orderable on Avanza (very likely — Xetra-Gold is one of
  the most commonly held gold ETCs among Nordic retail investors).
- Sizing: with ISK cash now confirmed at 11,288 SEK (P8, closed below),
  the ~7,500 SEK tranche 1 is comfortably funded without touching anything
  else. Long-run target 5% of total portfolio (~11,400 SEK), hard ceiling
  7.5%, tranche 2 funded via P3's PayPal conversion or a future
  contribution. Not fundable/not warranted: the full 25,000 SEK
  top-of-range size or buying via Revolut (unsecured claim on the
  issuing fintech, defeats the point of a systemic-stress hedge).
- **Structural gap, still open:** `portfolio.json.targets` has no
  `gold_pct` field, and gold doesn't fit any of `investor_profile.json`'s
  three 60/30/10 tiers (not "secure" — a 1.66x twelve-month high/low range
  is risk-asset volatility, not ballast). Recommended carve: equity 85 ->
  80, new gold line at 5 — apply once the first tranche actually executes,
  not before (no target line for a position that doesn't exist yet).
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

### S6 — No source for holding-company NAV discount/premium
- **Status:** open — blocks half of P5, and a Council voice wanted it on
  seven consecutive sweeps and couldn't act
- **Reviewed 2026-08-31: valuable soon.** This is the item costing the most
  live attention per sweep of anything on this list — a real voice, every
  sweep, reaches a real conclusion it cannot act on. The fix is ~10 minutes
  of human work (Excel request H), not a code change; recommending it
  directly rather than waiting for it to keep resurfacing.
- **Reviewed 2026-09-07: valuable soon, escalating.** Fourth consecutive
  sweep the same gap blocked a real call — this time not just one silenced
  voice but a genuine disagreement neither side can settle without the
  number: Contrarian wants to sell INVE-A.ST on unmeasurable valuation (91%
  of 52-week range), Copycat cites the CEO buying personally and repeatedly
  through 2026 at rising prices (most recently above today's price,
  2026-09-01) as evidence against. The Chairman's own pick this sweep is
  Option 1 — get the NAV number. Recommending directly again: ~10 minutes of
  human work with a real, compounding cost of not doing it.
- **Reviewed 2026-09-14: valuable soon, fifth consecutive sweep — and the
  deadlock moved rather than resolved.** The Contrarian voice stood down
  this sweep, but on new *primary* evidence rather than on the missing
  number ever being obtained: Jacob Lund bought 1,000 A-shares at 399.13 SEK
  on 2026-09-09, within 0.1% of today's price — the first datapoint the
  voice has ever had suggesting someone who can see the NAV thinks this
  price is acceptable. The Council memo is explicit that this "resolves
  nothing, it just moves the deadlock" back onto this item and D-b.
  Recommending a fifth time: this is now a real voice reaching an
  unresolved position on this holding in five consecutive sweeps it has
  been asked to render one, for the cost of a single number.
- **Reviewed 2026-09-21: valuable soon, sixth consecutive sweep, and the
  evidence got stronger while the number still doesn't exist.** Copycat's
  case strengthened further this sweep — three separate insiders (CEO
  Cederholm, Jacob Lund, Ulrika Elfving) bought in the last three weeks,
  five distinct individuals through 2026 at rising prices, zero disposals —
  while Valuation and Fundamental still return no usable metric at all
  (trailing P/E 4.68 and PEG 4.91 are holding-company pass-through
  artifacts). Chairman's own words: "the insider evidence got stronger this
  sweep, which makes the missing number more expensive, not less
  necessary." The Council itself now names an explicit fallback if a
  seventh sweep passes with nothing done: switch to Option 3 (stop
  re-flagging, per D-b). Q3 report lands 2026-10-07 — the next real chance
  to close this before that fallback becomes the honest call.
- **Reviewed 2026-09-28: valuable soon, but the acute cost has changed
  shape.** A seventh sweep passed with the NAV still unobtained, and this
  sweep's Council formally applied the pre-committed fallback (**D-b Option
  3**): hold the 5 shares, stop re-flagging, single re-entry trigger is a
  NAV figure recorded from Investor AB's **2026-10-07** Q3 report. That is
  the right process outcome — it stops a real voice burning a cycle every
  sweep on a question it cannot answer — but the underlying gap (no free
  automated NAV/discount source) is exactly as unresolved as at the first
  review. The next nine days are the cheapest window this item will get:
  recording the number from that report closes this item outright rather
  than letting the fallback quietly become permanent.
- **Reviewed 2026-10-05: valuable soon, trigger now imminent (2 days).**
  Investor AB and Industrivärden both report Q3 on **2026-10-07**. This is
  the cheapest window this item will ever get — record one NAV figure per
  company into `data/company_profiles/INVE-A.ST.json` (and the
  Industrivärden equivalent) directly from the report, closing an
  eight-sweep-old gap in about ten minutes. If the window passes again with
  nothing recorded, the Option-3 fallback (hold, stop re-flagging) in force
  since 2026-09-28 should be treated as this system's durable position on
  the holding, not a temporary stand-down.
- **Why:** Investor A and Industrivärden cannot be valued on P/E; the real
  metric is NAV discount/premium, and no free automated source has been found.
  The funnel's `value` lens has the same blind spot — it ranks these names on
  earnings yield and price/book, neither of which means what it usually means
  for a holding company.
- **How:** parse the quarterly report PDF (the `pdf` skill can, given the
  report), or read it off Investor's IR page and record it in
  `data/company_profiles/INVE-A.ST.json` with source and date. One number,
  refreshed quarterly, not a fetcher.

### S21 — [prospecting] Nordic coverage: 107 names, and a data asymmetry underneath
- **Status:** open — the headline problem is fixed; a quieter one it exposed is not
- **Reviewed 2026-08-31: valuable soon — reconfirmed independently by the
  scorecard, not just by memo narrative.** `reports/system-scorecard.md`'s
  DATA pillar this run measures `fwd_pe` coverage at 68% Sweden vs 100% US —
  a 32pp spread, flagged by the scorecard's own >15pp rule — the same
  distortion this item named on 2026-08-24 (then measured at 35% missing on
  Swedish names). Two runs now show the same gap by two different
  measurement methods; this has moved from "a finding" to "a standing,
  reproducible property of the data," which raises the case for actually
  building option 1 (per-market coverage surfaced alongside each lens
  shortlist) rather than continuing to only note it.
- **Reviewed 2026-09-07: valuable soon, third measurement, same gap, and it
  now decided a screen status directly.** This sweep's scorecard: `fwd_pe`
  67% Sweden vs 100% US, a 33pp spread — essentially unchanged from 2026-08-31
  (32pp) and 2026-08-24 (35% missing, earlier method). Three independent
  measurements, same distortion. This sweep it stopped being abstract:
  VOLCAR-B.ST — the one candidate this sweep with a genuine multi-insider
  buying signal (CEO + two other insiders, all buying above today's price) —
  screens MISSING rather than PASS/FAIL purely because of the absent forward
  multiple, ranking it on fewer fields than any US peer.
- **Reviewed 2026-09-14: valuable soon, fourth measurement, same gap, and
  this sweep the predicted harm went from partial to total.** This sweep's
  scorecard: `fwd_pe` 69% Sweden vs 100% US, a 31pp spread — essentially
  unchanged across four independent measurements (35% missing on 2026-08-24,
  32pp on 2026-08-31, 33pp on 2026-09-07, 31pp today). VOLCAR-B.ST, the exact
  name this item flagged last sweep as screening MISSING because of the
  absent forward multiple, has now **dropped out of the candidate set
  entirely**, without the underlying question — genuine buy candidate or
  not — ever being resolved. A gap that used to cost a name its ranking now
  costs it its presence in the funnel at all. Raises, again, the case for
  building option 1 or 2 rather than continuing to only measure it.
- **Reviewed 2026-09-21: valuable soon, fifth measurement, same gap, and it
  is now shaping most of a full sweep's MISSING block.** This sweep's
  scorecard: `fwd_pe` 69% Sweden vs 100% US, a 31pp spread — unchanged from
  2026-09-14. This sweep's screen: 10 of 17 MISSING rows are Nordic names
  missing `forward_pe` or `debt_to_equity` (INVE-A.ST, INDU-C.ST, SHB-A.ST,
  SWED-A.ST, SEB-A.ST, LUND-B.ST, ERIC-B.ST, ASSA-B.ST, LATO-B.ST,
  BURE.ST), and the Council named it directly: AZN.ST — the portfolio's
  largest individual stock — has had no forward multiple in any of the five
  runs on record, which is part of why the funnel ranks it 59-61 while
  three voices independently call it a BUY. Five independent measurements,
  same magnitude, now visibly distorting both the discovery funnel and a
  live holding's mechanical rank simultaneously.
- **Reviewed 2026-09-28: valuable soon, sixth measurement, unchanged
  magnitude, and the cost is now on the portfolio's largest single
  holding.** This sweep's scorecard: `fwd_pe` 69% Sweden vs 100% US, a 31pp
  spread — identical to 2026-09-21, sixth consecutive measurement of the
  same gap. AZN.ST — the largest individual stock in the portfolio — has had
  no forward multiple in any of the six scout runs on record, and the funnel
  ranks it 59-62 of ~75 while three Council voices independently call it a
  BUY. Six unchanged measurements of a >15pp scorecard-flagged spread, now
  visibly distorting a live holding's mechanical rank rather than only a
  discovery-stage candidate, is enough evidence to build option 1 (surface
  per-market coverage alongside each lens shortlist) rather than measure a
  seventh time.
- **Reviewed 2026-10-05: valuable soon, 7th measurement, same magnitude,
  still unbuilt.** This sweep's scorecard: `fwd_pe` 72% Sweden vs 100% US, a
  28pp spread — within the same unchanged band as every prior measurement
  (28-35pp across seven sweeps) and still above the scorecard's own >15pp
  flag threshold. AZN.ST again has no forward multiple in any of 7 runs,
  depressing its funnel rank to 59 while three Council voices call it a BUY.
  Seven unchanged measurements with no build attempted is itself evidence
  that repeating the recommendation again will not move this without
  someone actually picking it up — not escalating the wording further, since
  the wording has not been the limiting factor for several sweeps running.
- **2026-08-24 (evening):** the user supplied a 120-row Swedish ticker CSV.
  `scripts/watchlist.py universe-import` verified it and the universe went
  from 538 names (20 Nordic) to 622 (107 Nordic, 17%). Swedish names now
  reach the lens shortlists on their own merits — AZA.ST, INDU-C.ST, ORX.ST,
  CATE.ST, BALD-B.ST, BURE.ST, CORE-B.ST, BETS-B.ST, KNOW.ST all appeared in
  the first run. The original "discovery barely works for the market the user
  actually invests in" complaint is answered.
- **What remains, and it is a real distortion, not a cosmetic gap:** Yahoo's
  fundamentals coverage is not symmetric across markets. Measured on the
  2026-08-24 candidate set: `forward_pe` is missing for **9 of 26 Swedish
  names (35%) and 0 of 37 US names (0%)**. `fcf_yield` is missing for 23% of
  Swedish names vs 11% of US ones. The Valuation and Growth lenses both rank
  partly on forward multiples, so **a Swedish company can lose a shortlist
  slot for having no forward estimate rather than for being less attractive**
  — a systematic tilt toward US names that no one would see in the output.
  The `MISSING` label is honest per name; the aggregate bias is invisible.
- **How:** two options, neither large. (1) Make each lens report per-market
  coverage alongside its shortlist, so the tilt is at least visible to the
  Council. (2) Better: z-score each lens *within* a coverage cohort, or drop
  forward-looking fields from a lens's inputs when coverage for a name's
  market is below a threshold, so names are compared on fields they can all
  actually be measured on. Option 1 is an afternoon; option 2 is the real fix.
- **Also still open:** no free Nordic/European *constituent feed* is
  reachable (Wikipedia and Nasdaq Nordic are proxy-blocked), so the Nordic
  block stays user-maintained. That is now a maintenance question, not a
  capability gap — `universe-import` makes adding a batch a one-command job.

### S26 — [data] Drawdown backtest window contains no real shock to test the stated tolerance
- **Status:** open — new 2026-08-31, narrowed successor to the closed S5
- **Reviewed 2026-09-07: valuable soon, and now gating a live decision, not
  just a scorecard caveat.** This sweep's portfolio lens changed the
  drawdown-tolerance row from OK to **WATCH-unverified-not-OK**, based on its
  own stress arithmetic (explicitly labelled NOT a backtest) showing the
  current 80/10/5/5 mix at roughly -36% against the stated -30% tolerance.
  That produced a new open decision, **D-c** (trim crypto now / wait for
  S26's real shock-window backtest / change the tolerance), with the
  Chairman's own pick being to wait for this item's fix before deciding.
  This item is no longer purely structural — it is now the named gate on a
  live portfolio call, which raises its priority without changing what needs
  building.
- **Reviewed 2026-09-14: valuable soon, and now directly underwriting a
  concrete rebalancing proposal, not just gating a decision.** This sweep's
  portfolio lens proposed a specific reallocation (crypto 10%→7%, gold
  5%→8%) explicitly contingent on "a real stress-tested backtest including
  crypto's realistic drawdown distribution" — i.e. this item's own fix —
  plus the user's direct confirmation. D-c is now deferred a **third**
  consecutive sweep, and the timing argument sharpened this session: crypto
  Fear & Greed moved from 29 ("Fear") to 57 ("Greed") in three weeks while
  ETH ran +33.6% over 30 days — exactly the setup where momentum gets
  misread as confirmation. The backtest this item asks for is no longer a
  scorecard caveat; it is the stated precondition on a live rebalancing
  proposal.
- **Reviewed 2026-09-21: valuable soon, and this sweep the Council attached
  an explicit deadline rather than deferring again on the same terms.**
  D-c is now deferred a fourth sweep, crypto is 11.24% against the 10%
  target with Fear & Greed at 70 ("Greed", up from 57 last sweep and 29
  three weeks before) and ETH +7.8% this week alone. The Chairman's stated
  default: "if S26 is not run before the next sweep, Option 1 [trim the
  crypto leg] becomes the default." This is the first sweep this item has
  had a stated trigger date rather than an open-ended "valuable soon" —
  next sweep is the deadline this item's own backlog created.
- **Reviewed 2026-09-28: valuable soon, and this sweep is the clearest
  possible evidence this item matters — its own missed deadline just fired a
  live capital decision.** Last sweep's Chairman set an explicit default:
  "if S26 is not run before the next sweep, Option 1 [trim the crypto leg]
  becomes the default." S26 did not run, and this sweep's Council carried
  out the pre-committed default — trimming ~2,500 SEK of BTC0E.AS — purely
  because the backtest this item has asked for since 2026-08-31 still
  doesn't exist. That is a mechanical rule substituting for the actual
  analysis it was meant to gate. The trim itself is reasonable risk
  management, but the system now has a live precedent for a capital action
  executing on a default rather than a tested number, which is exactly the
  failure mode S26 was opened to prevent. **Recommending this as the
  top-priority build for the next session, ahead of every other open item on
  this list.**
- **Reviewed 2026-10-05: still the top-priority build, and this sweep found
  the one existing "pass" has no file behind it at all.** `portfolio`'s own
  check this sweep found `data/backtests/` does not exist on disk — the
  −20.62% max-drawdown figure quoted in `portfolio.json` and repeated in
  every prior scorecard/memo has no traceable backing file. This is a
  harder, more specific finding than every prior sweep's critique (the
  window not containing a real shock): there is now **no verifiable
  evidence at all** behind the only number that has ever supported "the
  80/10/5/0/5 target respects the −30% tolerance." Also discovered this
  sweep: the 09-28 "precedent of a capital action executing on a default"
  described above did not actually occur — the trim was never executed (see
  S27) — so S26's own gap has not yet caused a wrong capital action, only a
  wrong *record* of one. The reference-target review this sweep keeps the
  target labelled PROVISIONAL and names S26 as the first build, explicitly
  ahead of everything else on this list.
- **Why:** S5 (does the adopted 85/10/5/0 target respect the -30% drawdown
  tolerance) was marked resolved 2026-08-17 and reaffirmed within 0.7pp this
  sweep: a 90/10 equity/crypto proxy over 2019-06 to 2026-08 (86 months)
  shows max drawdown -20.62%, inside the -30% line. **But the window's own
  worst equity drawdown is -19.14%** — the data contains no crash on the
  scale the -30% tolerance was written to describe. "-20.62% clears -30%"
  from a window whose deepest hole is -19% does not actually validate the
  tolerance; it says the tolerance was not tested. This is a data-reliability
  issue: the number is real and correctly computed, but the portfolio-health
  scorecard's "Drawdown-tolerance fit: OK" row currently implies more than
  the backtest can support. A second, smaller finding from the same run:
  the 10% BTC sleeve "barely registered" in the result because monthly
  rebalancing dilutes crypto's path, while the real portfolio is not
  rebalanced monthly and crypto has been allowed to drift to 9.4-11.2% —
  so the backtest also does not test the scenario the crypto position
  actually poses (a sustained drift above target, then a crash).
- **How:** run `backtest.py` over a fixed window that actually contains a
  real >=-30% equity shock (e.g. 2007-2009 or 2020-02/03), using whatever
  longest-history equity-index proxy is available — VWCE.DE itself does not
  reach back that far, so a longer-history substitute (e.g. an MSCI
  World/ACWI-tracking series) is needed. First confirm whether
  `backtest.py` already supports a fixed `--start`/`--end` (the V2 roadmap's
  Phase 6 entry says this was previously missing; this sweep's
  fixed-looking date range suggests it may already work and just needs
  verifying). Report the result as a second, clearly-labelled "shock
  window" figure alongside the existing rolling-lookback one — not a
  replacement for it, since both answer different questions. **Write the
  output to `data/backtests/`** — this sweep found that directory does not
  exist, so even a correctly run backtest currently leaves no traceable file.
- **Improves:** data reliability (the scorecard/portfolio-health row rests
  on a window that cannot test what it claims to, and currently has no
  backing file at all) and decision quality (the crypto sleeve — the
  position most likely to actually blow through a shock scenario — is the
  one part of the target this backtest tests least, and is now the direct
  precondition on a live rebalancing proposal, with an explicit next-sweep
  deadline attached).

### S27 — [process] The scheduled task's stored prompt drifts stale against real file state, and this is now the seventh confirmed occurrence
- **Status:** open — new 2026-09-07, opened without further deliberation per
  the standing instruction left in this file's own closed log 2026-08-31
  ("if a third occurs, open the S-item without further deliberation")
- **2026-09-07 meta review — cap resolved without touching this item, as
  instructed.** S20 closed this session (its own stated exit condition — "if
  not reachable, say so and stop" — was met: SEC EDGAR's CIK-mapping fetch,
  the same `www.sec.gov` gateway S20 asked about, returned a confirmed 403
  rather than an untested unknown). S25 closed as a downstream symptom of
  that same confirmed block, not a distinct live problem (see Closed log for
  both). One new item, S28, opened from this session's AZN.ST
  capital-timing-lag finding. Net: 8 open S-items (S1, S6, S21, S23, S24,
  S26, S27, S28).
- **2026-09-14 meta review — fourth confirmed occurrence, and the two stale
  lines are now verbatim-identical across three consecutive sweeps.** The
  scheduled prompt that launched this sweep again asserted the Handelsbanken
  wrapper question is unresolved and the memo must open with it, and again
  asserted `investor_profile.json.reference_targets` are null. Both false,
  both self-caught and corrected in today's memo (section 9, item 9), the
  same as 2026-08-31 and 2026-09-07. No new premises drifted this time — it
  is the identical two lines, unedited, a third time running, which argues
  the prompt text simply has not been touched since it was last flagged.
  Net this session: S1 closed under cap pressure (unchanged, workaround
  stable), S29 opened (52-week high/low gap) — 8 open S-items (S6, S21, S23,
  S24, S26, S27, S28, S29).
- **2026-09-21 meta review — fifth confirmed occurrence, and the proposed
  fix has now sat unapplied across two full sweeps since this item was
  opened.** The scheduled prompt that launched this sweep again asserted the
  identical two premises verbatim (Handelsbanken wrapper "unresolved, memo
  MUST open with it"; `reference_targets` "are null"), both false on the
  same two files, both self-caught and corrected in this sweep's memo
  (opening section) with no wrong action taken. This is the fifth time the
  same self-mitigation pattern has held — which is itself now the evidence
  that matters: the "How" section's fix (asking the scheduler-prompt owner
  to remove the two stale lines) was proposed at the third occurrence
  (2026-09-07) and has had zero effect across the 2026-09-14 and 2026-09-21
  sweeps. This item cannot fix itself — it is outside `meta`'s write access
  — so the only escalation available here is naming plainly that the
  recommended fix has not been applied, not repeating the recommendation in
  new words. Flagging directly to the user: this needs a five-minute manual
  edit to the scheduled task's stored prompt text, outside this repository.
- **2026-09-28 meta review — sixth confirmed occurrence, plus two new
  same-session instances of the same underlying pattern (stored/asserted
  text vs. live state), widening this item's scope.** The scheduled prompt
  again asserted the Handelsbanken wrapper is unresolved and
  `reference_targets` are null; both false, self-caught in the memo's
  opening section a sixth time, with the proposed scheduler-text edit still
  unapplied across four sweeps since first recommended (2026-09-07). New
  this session, inside a single sweep rather than across sweeps: (a) the
  orchestrating session's prompt to the `council` subagent mis-substituted
  shell variables, delivering literal `$(cat ...)` strings instead of the
  four lens outputs — `council` caught this and read the source files
  directly rather than reasoning from the broken text; (b) the same
  orchestrator's prompt asserted "7 consecutive runs" for the top-10 streak
  when `candidate_history.csv` holds 6 — also self-caught. Neither caused a
  wrong call, matching every prior occurrence. **Scope widened, same ID:**
  this item now covers any orchestration-layer text — the external
  scheduler prompt or an in-session prompt assembled for a subagent — that
  asserts a fact instead of being read live from the file it claims to
  summarize. The scheduler-text fix remains the priority recommendation
  (still a five-minute edit outside this repository); the two new
  in-session instances additionally argue that any prompt text built by
  shell substitution or by hand-counted claims should instead pass a file
  path for the receiving agent to read directly, and any streak/count claim
  should be computed from the live CSV, not asserted.
- **2026-10-05 meta review — 7th confirmed occurrence of the external
  scheduled-prompt drift, plus a new, more serious same-family instance
  that originated *inside* the repository rather than in the external
  prompt — scope widened a second time, same ID.** The scheduled prompt
  again asserted the Handelsbanken wrapper is unresolved and
  `reference_targets` is null; both false, both self-caught in this sweep's
  opening section, the recommended scheduler-text edit still unapplied
  across 5+ sweeps since first recommended (2026-09-07). Separately and more
  seriously: the 2026-09-28 Council memo wrote "**Applied:** Option 1 — trim
  ~2,500 SEK of BTC0E.AS" for a trade this system never executed, and that
  false "executed" framing propagated from the memo into `OPEN_ITEMS.md`'s
  own emphasis paragraph and into S26's 2026-09-28 review text — stored text
  *inside this repository* asserting a fact that `portfolio.json` and that
  same sweep's own SESSION_LOG ("User decisions: none") directly
  contradicted. This sweep's Council caught it and D-c is re-opened. This is
  the identical failure shape S27 already tracks (stored/asserted text
  diverging from live file state instead of being read live), but it is the
  first confirmed instance of the *Council's own memo* producing the drift
  rather than an external scheduled prompt or an in-session shell
  substitution — folded in here rather than opened as a new item, per this
  item's own 2026-09-28 precedent of widening scope on a repeat of the same
  shape rather than proliferating IDs. A third, minor same-session instance:
  this sweep's own launch note mis-stated the occurrence count as "8th" when
  this file's own count was 6 through 2026-09-28 (making this the 7th) —
  self-caught, no wrong action, the identical pattern this item exists to
  track applied to itself. **New "How" for the in-repository variant:**
  `council.md`'s memo template should use "Recommended" / "Selected as
  default" language for any action this system did not itself perform —
  never "Applied" or "Executed" — and any future text claiming a capital
  action is done must cite the specific user-confirmation line that
  authorizes it, not just assert it. Separately, still unresolved and
  compounding the same family of gaps: `council` still has no shell, so
  `position_report.py`'s output could not be handed to it directly this
  sweep either (§1 of the memo was hand-reconstructed again, matching the
  real script's output only because the orchestrator happened to check
  afterward) — the same "pass a file path, don't reconstruct or assert" fix
  this item already recommends for orchestrator prompts, just unapplied for
  a different subagent.
- **Why:** the scheduled prompt that launches this weekly sweep is stored
  text, edited by hand outside a session, and it does not update itself when
  the facts it assumes change. Five confirmed occurrences now, each caught
  and corrected in the memo itself rather than causing a wrong action, which
  is exactly why this sat at "considered, not opened" for two of them:
  - **2026-08-17:** contradicted CLAUDE.md's canonical flow (specifics not
    re-litigated here; see that date's SESSION_LOG entry).
  - **2026-08-31:** asserted the Handelsbanken wrapper question was still
    unresolved and required the memo to open with it (resolved
    2026-07-07/2026-08-03); asserted `investor_profile.json.reference_targets`
    were still null (adopted 2026-07-27, written 2026-08-03); asserted this
    sweep's backtest was the first ever run (one ran 2026-08-17).
  - **2026-09-07:** the identical two premises from 2026-08-31 recurred
    verbatim — Handelsbanken wrapper "unresolved, memo MUST open with it"
    and reference_targets "are null" — both still false on the same two
    files (`data/portfolio.json.open_structural_questions` is `null`, moved
    to `OPEN_ITEMS.md` 2026-07-07/2026-08-03;
    `investor_profile.json.reference_targets` carries adopted, non-null
    values plus the 2026-08-25 gold-tranche amendment). The prompt text was
    not refreshed between the second and third occurrence despite the
    2026-08-31 closed-log entry naming exactly this fix.
  - **2026-09-14:** the identical two premises recurred a third time
    verbatim — no new drift, the same unedited text. Self-caught and
    corrected in the memo's section 9 a fourth time overall.
  - **2026-09-21:** the identical two premises recurred a fourth time
    verbatim, again self-caught and corrected, this time in the memo's
    opening section rather than buried in a numbered list — a fifth
    confirmed occurrence overall, and the two full sweeps since the fix was
    first named show the recommendation alone does not close this without
    someone actually editing the scheduler text.
  - **2026-09-28:** the identical two premises recurred a fifth time
    verbatim, self-caught a sixth time overall, plus the two new
    within-session instances described above.
  - **2026-10-05:** the identical two premises recurred a sixth time
    verbatim, self-caught a seventh time overall, plus the new
    in-repository "Applied"-as-execution variant described above.
- **How:** whatever stores this scheduled task's prompt (outside this
  repository — a trigger/routine configuration, not a file `meta` can edit)
  needs its two stale lines removed or rewritten to reference the *current*
  resolution status rather than restating a snapshot of facts from whenever
  the prompt was last authored. Concretely: drop the Handelsbanken-wrapper
  framing entirely (closed, two months resolved) and rewrite the
  reference_targets line to ask "does the currently adopted target still
  look right given the horizon/drawdown/glidepath considerations," not
  "propose one from null." This is outside `meta`'s write access (it edits
  `OPEN_ITEMS.md`, not the scheduler), so the fix is a recommendation to the
  user, not a self-applying change — and after five sweeps of the
  recommendation sitting unapplied, it is worth the user treating this as a
  direct five-minute action item rather than a background note. Separately,
  in-session: any prompt assembled for a subagent should pass file paths for
  the receiving agent to read directly rather than shell-substituting file
  contents into a string, and any streak/count claim should be computed from
  the live CSV rather than typed by hand. And now, in-repository: `council.md`
  should never write that an action was "Applied"/"Executed" for something
  this system did not itself do.
- **Improves:** decision quality (a stale premise that goes uncaught, unlike
  the seven confirmed self-mitigated instances, would produce a wrong
  action, not just wasted words) and process reliability (this is the
  system's own scheduling, orchestration, and now memo-writing text drifting
  out of sync with live state — the exact "process for its own sake" failure
  mode CLAUDE.md warns about, just running in reverse: not too much process,
  but pieces of it going stale unattended).

### S29 — [data] Candidates CSV carries `pct_52w_range` but not the 52-week high/low endpoints, capping a real Top-5 conviction
- **Status:** open — new 2026-09-14
- **Reviewed 2026-09-21: valuable soon, fifth sweep unfixed, and the
  Council named it directly as the cheapest fix on the table.** APP — the
  funnel's #1-ranked name for five consecutive runs — again resolves to NO
  ACTION on the identical gap: quality metrics are pristine (ROIC 65.5%,
  operating margin 77.7%, revenue +52.8%) while the price sits at 5% of its
  52-week range, and this system still cannot see from what level or when
  that drawdown happened. The same missing pair of fields also produced two
  different-looking "% of 52-week range" figures for AZN.ST and INVE-A.ST in
  the same memo (candidates CSV vs. thesis-review conventions) that read
  like a contradiction and are not one. This is now a repeat, quantifiable
  cost (a Top-5 conviction score held below what the underlying metrics
  would otherwise support) for a one-column, no-new-fetch fix — worth
  actually building rather than carrying to a sixth sweep.
- **Reviewed 2026-09-28: valuable soon, sixth sweep unfixed, still
  measurably capping conviction on a live Top-5 name.** APP — again this
  sweep's #1-ranked mechanical name — sits at a conviction constrained by
  the same S29 gap (3% of range, six consecutive runs, still unresolvable to
  a level or a date without the 52-week endpoints). The same missing pair of
  fields this sweep also left ALL's and CHTR's one-week price collapses
  uninterpretable (no way to see whether either is now near a multi-month
  low or still well off one). Six sweeps of the same one-column,
  no-new-fetch fix producing a repeat, quantifiable conviction cost is as
  strong a case as this backlog has for something to actually build next,
  alongside S26.
- **Reviewed 2026-10-05: valuable soon, 7th sweep unfixed, same name, same
  measurable cost.** APP — the funnel's #1-ranked name in most runs — made
  fresh 52-week lows this week (−10.0%) and the system still cannot see from
  what level or when the underlying drawdown began, because only the
  percentage-of-range field is carried, not the endpoints. This capped the
  Chairman's conviction on this sweep's #5 opportunity directly again. Seven
  sweeps of a one-column, no-new-fetch fix producing a repeat, named,
  quantifiable cost is as strong a case as this backlog has ever had for
  something to build; not escalating the words further, since the words
  have been sufficient and specific since the 2026-09-21 review — only the
  build is missing.
- **Why:** `scout.py`'s candidate CSV outputs the derived `pct_52w_range`
  percentage only, not the underlying `52w_high`/`52w_low` fields — even
  though this sweep's snapshot already carries both per ticker
  (`data/cache/snapshots/20260914T060927.json`). This sweep's #4 Top-5
  opportunity, APP, has sat at "4% of range" for four consecutive sweeps
  while the price itself barely moved (305.77 → 314.49, +2.9%) — meaning the
  52-week high is far above the current price and the drawdown that
  produced it happened before this system started watching, but the system
  cannot see what, when, or from what level, because the only range field it
  carries is the percentage. The Chairman's own conviction on APP (5, the
  lowest of the Top 5, on the mechanical funnel's #1-ranked name out of 614)
  was explicitly capped by exactly this gap: "That is not a reason to
  disbelieve the quality metrics; it is a reason not to commit capital on
  them." The same missing pair of fields also underlies item 2 in this
  sweep's "Data gaps for meta" section — two different %-of-52-week-range
  conventions (candidates CSV vs thesis-review) reading like a contradiction
  in the same memo, which a shared source-of-truth pair of endpoints would
  resolve alongside `data/definitions.json` naming both formulas.
- **How:** add `week52_high` / `week52_low` columns to `scout.py`'s candidate
  CSV output, sourced from fields the snapshot already fetches — no new data
  source, no new fetch. The Council's own memo calls this "the cheapest
  high-value fix on this memo's list."
- **Improves:** decision quality (a Top-5 conviction score was measurably
  reduced by an interpretability gap a one-column change removes) and data
  reliability (closes the gap between what the snapshot captures and what
  reaches the lenses and voices).

### S31 — [process] `journal.md` instructs itself to run `scripts/scorecard.py --write`, but journal has no Bash tool
- **Status:** open — new 2026-09-21, now a 4th confirmed occurrence of the
  same friction as of this review
- **Reviewed 2026-09-28: now a third confirmed occurrence, matching this
  system's own standing threshold for moving from "noted" to "apply the
  fix."** This sweep's SESSION_LOG entry states it plainly: "Standing
  finding for meta, now a 3rd occurrence" — `journal` (Read/Write only, no
  Bash) again could not run `scripts/scorecard.py --write` itself, and the
  orchestrating session ran it as a separate step. This time the ordering
  happened to work out (the scorecard was refreshed before `journal` drafted
  its entry), but that was a property of this session's manual sequencing,
  not of anything the fix below addresses. Three real occurrences of the
  identical instruction/tool mismatch is the same bar this system used to
  escalate S27 to "open without further deliberation" at its third
  occurrence — recommending the same treatment here: apply both halves of
  the proposed fix (reorder CLAUDE.md's step 5a ahead of step 5, and reword
  `journal.md`'s Mode 2 step 4) now rather than waiting for a fourth
  occurrence where the ordering doesn't happen to work out.
- **Reviewed 2026-10-05: 4th confirmed occurrence, fix still unapplied.**
  This sweep's SESSION_LOG again states the standing finding ("`journal`
  still only has Read/Write, no Bash") as the orchestrating session ran
  `scripts/scorecard.py --write` as a separate manual step for at least the
  4th time since this pattern was first logged (2026-09-07). This sweep's
  ordering happened to work (the scorecard was refreshed before `journal`
  drafted its entry), which is exactly the property this item warns is not
  guaranteed by anything in the instructions as written — it worked by the
  orchestrator's manual sequencing, not by anything structural. Four
  occurrences is double the threshold this system has used elsewhere (S27
  opened at three) to move from "noted" to "fix it." Recommending the
  two-part fix be applied now rather than carried to a fifth occurrence.
- **Why:** `journal.md`'s own Mode 2 (sweep-end) instructions, step 4, say:
  "Run `python scripts/scorecard.py --write` and quote its Status lines into
  the entry." But `journal`'s declared tools are `Read, Write` only — no
  Bash — so it structurally cannot do what its own step 4 tells it to do.
  CLAUDE.md's canonical flow lists the scorecard command as a separate
  top-level step, **5a**, positioned *after* step 5 (`journal`), which is
  presumably meant to be run by the orchestrating session — but nothing
  reconciles that ordering against `journal.md`'s own text, which reads as
  if `journal` will produce a scorecard-informed entry itself. This
  session's SESSION_LOG entry names the resulting workaround directly: "for
  the second time in three sweeps, `journal` (Read/Write tools only) could
  not itself run `scripts/scorecard.py --write` and had to hand off to the
  orchestrating session as a separate step," and the practical cost is
  visible in the entry itself — this sweep's "Scorecard status" section had
  to quote the *prior* sweep's (2026-09-14) pillar figures, correctly
  labelled as stale, because the current scorecard wasn't refreshed until
  after `journal` had already drafted the entry. That is not a wrong number
  reaching a decision (it was labelled honestly), but it is a real,
  repeating instruction/tool mismatch inside a single agent file — exactly
  the "instruction contradicting another file" pattern this review is
  built to catch, and it has now surfaced four times in five sweeps rather
  than once.
- **How:** two small, compatible fixes, neither a new agent. (1) Reorder
  CLAUDE.md's canonical flow so `scripts/scorecard.py --write` (currently
  5a) runs *before* `journal`'s sweep-end pass, not after — e.g. as step 4b,
  right after `decisions.py basis --write` and before `journal`. (2) Reword
  `journal.md`'s Mode 2 step 4 from "Run `python scripts/scorecard.py
  --write`" (an action journal cannot perform) to "Read the freshly-written
  `reports/system-scorecard.md` (refreshed by the orchestrating session
  immediately before this step) and quote its Status lines" — matching what
  `journal` can actually do with its granted tools. This removes the
  handoff friction and, more importantly, lets `journal`'s entry quote the
  *current* sweep's pillar figures instead of the prior sweep's.
- **Improves:** data reliability (the SESSION_LOG entry — the system's only
  cross-session memory — currently risks quoting one-sweep-stale scorecard
  figures purely because of step ordering, not because the data doesn't
  exist yet) and system reliability (removes a recurring instruction/tool
  mismatch inside `journal.md` rather than letting it resolve itself as an
  ad hoc handoff every time it's hit).

### S32 — [data] Currency-unit mismatch in `fcf_yield_pct` (and possibly `price_to_sales`/`price_to_book`) for issuers that report in a different currency than their listing — absorbs S24
- **Status:** open — new 2026-10-05, absorbs S24 (same root-cause family,
  root cause now identified for at least two names)
- **Why:** `fcf_yield_pct` for ABB.ST and AZN.ST divides free cash flow
  reported in the company's own reporting currency (USD, for both) by a
  market cap computed in the listing currency (SEK), with no FX conversion.
  Verified by arithmetic this sweep: AZN.ST's real FCF yield is ~2.0%
  (4.905B USD × 9.9047 SEK/USD = 48.6B SEK ÷ 2,441B SEK market cap), not the
  0.20% every prior sweep computed and fed into `z_value`; ABB.ST's real
  figure is ~0.87% (1.5705B × 9.9047 = 15.6B SEK ÷ 1,792B SEK), not 0.09%.
  This is not a rounding or calibration issue — it is a missing currency
  conversion, understating both figures by roughly the SEK/USD rate (~9.9x).
  It directly fed the funnel's rank, and it was literally last sweep's
  "strongest case against" AZN.ST and inflated the case against ABB.ST
  roughly tenfold, across at least the 2026-09-28 and 2026-10-05 sweeps.
- **Absorbs S24's TSM instance — unverified hypothesis, not yet confirmed.**
  S24 tracked TSM's unflagged `roic_pct` 183.7% / `fcf_yield_pct` ~29.8% as
  an implausible-value detector gap for 5 consecutive sweeps, treated as a
  plausibility-bounds calibration problem. This sweep's Council proposes a
  sharper explanation: TSM reports in TWD and is priced in USD, so the same
  currency-conversion bug (TWD free cash flow/equity over a USD market cap)
  would produce exactly this shape of error. **Not verified this sweep** —
  needs checking against TSM's actual reported TWD figures and the TWD/USD
  rate before it can be called confirmed.
- **Also check:** whether `price_to_sales` and `price_to_book` share the same
  pattern for the same dual-currency issuers (ABB.ST's `price_to_book`
  113.06 is independently suspect-flagged every sweep — worth checking
  whether it is the identical bug, not a separate implausibility).
- **How:** find where `fcf_yield_pct` (and `price_to_sales`/`price_to_book`)
  is computed in `scripts/fetch_market_data.py` or `derived_metrics.py`.
  Confirm whether the numerator (FCF, revenue, or book equity) is sourced in
  the company's reporting currency while market cap is sourced in listing
  currency. Fix by converting the numerator to the listing currency using
  the matching FX rate already present in the macro snapshot (`sek_per_usd`,
  etc.) before dividing — not by re-deriving market cap, since that is the
  one figure already denominated the way the ratio needs. Then re-test TSM
  specifically: if its figures normalize into a plausible range once the
  currency fix is applied, S24's TSM instance is explained and this
  absorption is complete; if they do **not** normalize, S24 was tracking a
  genuinely separate plausibility-bounds gap and should be reopened under a
  fresh ID with that narrower scope (TSM only, bounds-calibration, not
  unit-conversion). Do not conflate with ALL's `fcf_yield_pct` 26.79% (S24's
  other open instance) — hypothesised to be an insurer-float distortion, a
  different mechanism, and should stay tracked separately if S24 is
  reopened.
- **Improves:** data reliability (a verified, fixable code bug, not a
  judgement call) and decision quality (this single error supplied the
  strongest argument against buying more AZN.ST and materially inflated the
  case against ABB.ST, across at least two sweeps of Council reasoning that
  fed directly into live BUY/SELL calls).

### S33 — [mechanical] Lens ranking has shown no predictive signal for many consecutive sweeps, now with n well over the scorecard's own threshold
- **Status:** open — new 2026-10-05
- **Why:** `scripts/scorecard.py`'s MECHANICAL pillar has read "RANKING IS
  NOT ADDING SIGNAL" for many consecutive sweeps, and this sweep's numbers
  are no longer a provisional, noisy read — every lens individually clears
  n=20+ (contrarian n=55, defensive n=82, growth n=76, quality n=129, value
  n=86) and the top-half/bottom-half split (median −4.7% vs −2.0%) is itself
  built on hundreds of observations. The value lens is the most consistently
  damaging: its beat-rate against baseline has read 8-10% across multiple
  sweeps, meaning value's own ranking is close to actively anti-correlated
  with outcomes rather than merely uninformative. This is the exact "five
  lenses that sort names but not outcomes" failure mode CLAUDE.md names as
  how the MECHANICAL pillar fails silently, and it has now been visible, at
  real n, for long enough that another sweep of only noting it adds nothing
  new.
- **How, two parts, not mutually exclusive:**
  1. **Make the non-predictiveness operational, not just descriptive.**
     CLAUDE.md and `council.md` already treat mechanical rank as a
     candidate-surfacing mechanism in spirit ("judgement is spent on names
     that survived"), but nothing currently tells the Chairman's synthesis
     to give rank itself zero evidentiary weight once it is handed a
     shortlist — the Chairman already does this informally (e.g. this
     sweep explicitly weighing voices over the frozen top-10), but it
     should be stated as a rule rather than left to each sweep's Chairman
     to rediscover.
  2. **Investigate the value lens specifically**, since it is the one
     consistently anti-correlated lens, not merely flat. Candidate
     hypotheses worth testing against `candidate_history.csv`: value's
     z-score inputs reward falling prices (CHTR's case this sweep: the
     value lens ranked it near the top purely by falling 11.9%+ in weeks
     with deteriorating fundamentals, exactly the pattern the Contrarian
     voice independently flagged as "the fundamentals agree with the
     price" rather than a mispricing); or value's trailing-multiple inputs
     systematically lag a market that is already pricing in deterioration
     the trailing numbers haven't caught up to yet.
- **Improves:** decision quality (prevents the Chairman or a future reader
  from treating a non-predictive rank as if it carries information, and
  explains why "RANK HISTORY: 0 of 7 in the top 10" coexists with multiple
  Top-5 BUY calls this sweep without contradiction) and system reliability
  (the MECHANICAL pillar's own stated purpose — "do the lens rankings
  predict anything" — currently reads a repeated "no" without any proposal
  in response, the exact gap this review exists to close).

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
  supports a rolling N-year lookback, no fixed `--start`/`--end` — **verify
  this against the 2026-08-31 run, whose dates look fixed; see S26**), and
  score calibration. `data/candidate_history.csv` is the calibration store
  this phase asked for — mechanical rank per candidate per run, correlatable
  against realised returns later. It records the funnel's ranks, not each
  voice's conviction; that is Phase 7d.
- **Phase 7 — Council architecture.** User-prioritised 2026-08-18.
  - **7a (voice isolation) — deliberately NOT built.** Seven voices as seven
    separate agent invocations would roughly double invocations per sweep and
    increase total tokens (each invocation reloads shared context). The
    2026-08-18 and 2026-08-24 production sweeps produced genuine, substantive
    disagreement with no visible anchoring between voices. Build it if
    anchoring is ever actually observed — not on principle.
  - **7b (Copycat / Smart Money) — DELIVERED 2026-08-24** as the seventh voice
    in `council.md`, with its data sources and its named gaps explicit. Its
    missing institutional/activist data is now tracked as S20; its narrower
    US-insider fetch-scope gap is tracked separately as S25 (2026-08-31).
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
    its own inputs. What this phase asked for as "log scores now, correlate
    later" is now live; the correlating needs elapsed time (S23).

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
  ("35/36 of 74/75 rows are new — discovery is producing") without this
  correction, meaning the same misreading has likely recurred at least twice
  before being caught. Every instance so far has been self-caught with no
  wrong action (no capital decision has ever rested on the turnover count
  itself), which is why this is not opened outright — but a second explicit
  catch after today's would meet the pattern-recognition bar used elsewhere
  in this file (e.g. S27's three-strikes rule) to open without further
  deliberation. Cheap fix if it recurs: rename the CSV's `source=new` value
  to something unambiguous (e.g. `not_held_not_watchlisted`), or add a true
  `first_seen_date` column (derivable from `candidate_history.csv`, which
  already has per-ticker run history) so "new to the candidate set" and "new
  to this run's output" stop being the same word.

### Considered by the 2026-09-28 session, not opened

- **Portfolio lens computed this sweep's allocation percentages against a
  different denominator than last sweep's, without flagging the change —
  caught by Council before it could mis-size a live trade, not opened as a
  new item.** Last sweep's `portfolio` lens measured allocation against the
  investable base (excluding the 11,363.76 SEK Handelsbanken tax reserve);
  this sweep's measured against total capital. On a like-for-like basis
  crypto actually rose to 11.30%, not fell to 10.73% as the raw comparison
  implied — which nearly under-sized the D-c crypto trim before the Council
  caught it and sized off the corrected figure instead. The important
  detail: `data/definitions.json`'s `investable_capital_convention` (decided
  2026-08-17) already pins the correct answer — full-portfolio, including
  the tax reserve — for exactly this kind of figure. This sweep's number
  (total capital) was actually the *compliant* one; last sweep's
  (investable-only) was the one that quietly violated an already-decided
  convention. That makes this a portfolio-lens consistency bug, not a
  missing-definition gap — the fix is for `portfolio.md` to explicitly cite
  `investable_capital_convention` when it computes allocation percentages,
  so the denominator can't drift sweep to sweep. A second, related finding
  in the same scorecard: the geography rating tightened from WATCH (49.10%)
  to ACT (48.83%) with the underlying number barely moving, meaning the
  WATCH/ACT threshold itself changed between runs, undocumented. First
  confirmed occurrence of this exact drift; watching for a second before
  opening a formal item, per the standing pattern used for the
  `reference_targets` and `thesis_status` staleness findings below. Flagged
  directly: `portfolio.md` should state its threshold values explicitly in
  its own output each sweep, not just the rating.
- **A same-day scout re-run left an orphaned duplicate 75-row block in
  `data/candidate_history.csv`, caught and removed before committing — not
  opened as a new item.** This sweep's first scout run came back DEGRADED
  (universe 35 days stale); after `build_universe.py` refreshed it, scout
  was re-run and returned VALID, but the discarded DEGRADED run's output had
  already been appended to `candidate_history.csv`. This file underpins the
  DISCOVERY and MECHANICAL scorecard pillars (rank-per-candidate-per-run
  correlated against later returns), so an uncaught duplicate would have
  quietly double-weighted one day's ranks in every future scorecard read
  from this file onward — a real, if narrowly-averted, data-integrity risk.
  This was a self-caught near-miss with zero actual harm, and the trigger
  condition (a same-day scout re-run) is not yet a repeated pattern. Not
  opening a new item on a single near-miss; if a same-day re-run happens
  again and isn't caught by hand, `scout.py` should either tag each append
  with a run identifier so a superseded same-day run can be identified and
  removed, or refuse to append history for a run whose own candidate
  CSV/JSON got discarded before commit. Separately: this sweep's scout
  DEGRADED→VALID cycle (35-day-stale universe, cleared by running
  `build_universe.py` by hand) worked exactly as designed — a genuine
  mechanical event, not a distrust flag — and needs no fix; noted here only
  so a future DEGRADED reading isn't assumed to be the same class of
  problem as an `INVESTIGATE_ZERO_PASS` failure.
- **The calendar fetch covered portfolio holdings only this sweep, and a
  live Top-5 BUY (VICI) lost its earnings date as a result — not opened as a
  new item.** Last sweep's calendar had VICI's print at 10-29, flagged next
  to the FOMC window; this sweep's did not, for VICI or for any other
  candidate. This reads as a regression rather than a designed scope limit
  (VICI had coverage before), so it may be a one-off gap in this run's fetch
  rather than a standing "candidates are never submitted to the calendar"
  rule — the same ambiguity that made S25 (insiders scope) worth a second
  look before it closed. Not opening an item on a single observed
  regression; watching for a second occurrence before treating this as a
  structural scope gap in `fetch_calendar.py` (which would then need the
  focus-flagged candidate list fed in alongside holdings, the same fix
  pattern S25 proposed for insiders).

### Closed by the 2026-09-21 session

- **S23 — closed under cap pressure (8-item cap reached; two new
  evidence-backed items opened this session, S30/S31), not because the
  underlying measurement gap changed.** This item's own "How" section always
  said "nothing to build. Run the sweep... and wait" — its role was to hold
  the discipline of not quoting a provisional median as a finding until
  n>=20. That discipline is now structurally enforced in two places
  independent of a standing S-item: `scripts/scorecard.py`'s
  `MIN_OBSERVATIONS` threshold (which withholds any figure below 20 and
  prints the count instead) and CLAUDE.md's own stated rule. `meta` reads
  `reports/system-scorecard.md` directly every session regardless, so this
  item's monitoring function is redundant with a review step that already
  exists. This sweep's scorecard again shows MECHANICAL flipping direction
  (now "RANKING IS NOT ADDING SIGNAL," -2.1% vs -0.9%, a fourth different
  read in four sweeps) and JUDGEMENT/DECISION still below n=20 for every
  voice — unchanged in substance from every prior review, which is itself
  the evidence that nothing further needs building here. Reopen (fresh ID)
  only if a future session finds a provisional figure was actually quoted as
  a finding, or `MIN_OBSERVATIONS` was lowered — i.e. if the discipline this
  item existed to protect actually breaks.
- **S28 — closed under cap pressure (8-item cap reached), not because
  resolved but because unbuilt and quiet for three consecutive sweeps.**
  Originated 2026-09-07 from a confirmed second occurrence of a
  capital-availability premise going stale between real-world execution and
  when it was reported (a Council BUY call discarded as `expired` because
  the capital base it was sized against no longer existed). Reviewed
  2026-09-14 ("can wait — no new occurrence"). This sweep's capital figures
  (ISK cash 845.43 SEK, PayPal 14,416.12 SEK) are consistent with the prior
  two sweeps' reconciled numbers — no third occurrence in over a month. The
  proposed mitigation (surface the gap between the portfolio snapshot's
  `as_of` date and today at session-start, or auto-flag a decision whose
  capital assumption a later transaction contradicts) remains unbuilt and
  the underlying risk is unchanged for the next time a real trade lands
  between sweeps and isn't reported promptly. Reopen (fresh ID, per the
  never-reuse-ID rule) on the next confirmed occurrence rather than carrying
  an inactive item through further cap pressure.

### Closed by the 2026-09-14 session

- **S1 — closed under cap pressure (8-item cap reached; one new
  evidence-backed item opened this session, S29), not because resolved.**
  Three consecutive reviews (2026-08-31, 2026-09-07, 2026-09-14) found the
  same unchanged state: the `KNOWN BAD` flag on BTC0E.AS's Yahoo feed
  continues to be applied correctly every sweep, and the broker-confirmed
  figure (150 units @ 73.54 SEK, 2026-08-23) is used in its place, so the
  workaround is stable and no wrong number has reached a decision. Nothing
  further can be built without a human verifying the instrument at Avanza —
  that has not been true of any of the three reviews, and is unlikely to
  become true through further code work. Reopen (fresh ID) if the flag is
  ever missed, or if the position's share of the portfolio grows enough that
  an unverified price starts to matter more than it does today.
- **S25's closed entry — addendum, not a reopening.** This sweep's Council
  memo confirms the scope gap S25 diagnosed (only the 8 portfolio tickers
  are ever submitted to `--insiders`/`--fi-issuers`; zero of this sweep's 34
  `new` candidates were covered) is still real and unfixed, independent of
  S20's gateway block. The memo itself recommends a note here rather than a
  reopening: "worth a note against S25's closed entry rather than a
  reopening." Noted. A fresh evaluation under a new ID is warranted if
  `data.sec.gov` or an equivalent gateway ever becomes reachable and the
  scope gap is still unaddressed at that point — not before.
- **Considered, not opened (second unapplied occurrence):
  `investor_profile.json.reference_targets` still stale against
  `portfolio.json.targets`.** The 2026-09-07 session flagged this directly
  rather than opening an S-item, recommending a one-line fix (update the
  field to 80/10/5/0/5). That fix was not applied, and this session's
  portfolio lens found the same inconsistency independently, this time
  formally rating the row **ACT** in the balance scorecard rather than just
  noting it in prose. Still judged not to warrant a full S-item — the fix is
  a single JSON field, not a process or code gap — but flagged as directly
  as this file allows: apply it before the next sweep, or it will keep
  producing a self-contradictory ACT rating against a target set that
  `portfolio.json` (the correct owner, per CLAUDE.md) already has right. A
  third unapplied occurrence should open an S-item without further
  deliberation, on the same standing pattern used for S27.

### Closed by the 2026-09-07 session

- **S20 — closed: its own question answered.** "Is `www.sec.gov` reachable
  through this proxy?" is no longer untested — this sweep's Copycat voice
  confirmed a `Tunnel connection failed: 403 Forbidden` on the SEC EDGAR
  CIK-mapping fetch, the same gateway this item asked about, and the gap
  landed on a Top-5 BUY (VICI) for the second consecutive sweep. Per this
  item's own stated instruction ("if not reachable, say so and stop"), the
  honest close is: not reachable through this environment's proxy, stop
  pursuing it here. Reopen (under a fresh ID, per the never-reuse rule) only
  if a future session confirms `data.sec.gov` — a distinct host, still
  genuinely untested — is reachable; that would be new evidence, not a
  reopening of this exact question.
- **S25 — closed: superseded by S20's confirmed finding, not resolved on its
  own terms.** S25 diagnosed a fetch-scope gap (US-listed candidates never
  submitted to `--insiders` because the fetch runs before `scout.py`
  produces the focus list) and proposed a second, narrower fetch pass after
  discovery. That second pass was actually run this session and made no
  difference — the CIK-mapping fetch itself is blocked (S20), upstream of
  any ticker list a scope fix could submit. S25's diagnosis was real for the
  sweep it was written on, but this session shows it was not the operative
  cause this time, and no scope fix can reach past a blocked gateway. Not
  reopening a distinct "scope" question under this ID if EDGAR ever becomes
  reachable again — that would need a fresh evaluation of whether the scope
  gap still bites once the gateway works, tracked under a new ID.
- **Considered, not opened: ABB.ST's `thesis_status` field lagging two
  sweeps of live SELL calls before this session's correction (WEAKENING ->
  BROKEN).** A real gap — the record didn't keep up with a decision the
  Chairman had already made twice — but this is its first confirmed
  occurrence, it self-corrected within the same session's memo (the Council
  itself named the discrepancy plainly: "partly a fact about this system's
  record-keeping"), and it caused no wrong action. Per the same standing
  pattern used for the scheduled-prompt drift (not opened as S27 until a
  third occurrence), watching for a second confirmed instance of a stored
  thesis/status field lagging repeated same-direction Chairman calls before
  opening a mechanism to sync it automatically.
- **Considered, not opened: `investor_profile.json.reference_targets` stale
  against `portfolio.json.targets` since the 2026-09-02 gold carve (85/10/5/0
  vs the authoritative 80/10/5/0/5).** Per CLAUDE.md's ownership table,
  `portfolio.json` owns targets and is what every live figure in this
  sweep's memo actually used, so nothing in this sweep's output was wrong.
  This is a one-line stale-copy fix, not a standing system defect — flagged
  directly for a direct correction (update the field to match
  `portfolio.json.targets`, i.e. 80/10/5/0/5) rather than opened as an
  S-item, the same treatment given to the "two stale strings" finding closed
  directly in the 2026-08-31 session's log.

### Closed by the 2026-08-31 session

- **S9 — closed under cap pressure (8-item cap reached; two new
  evidence-backed items opened this session, S25/S26), not because
  resolved.** Parts (a) cross-field plausibility and (b) new-position-with-
  no-thesis flag remain undone. No fresh evidence this session that either
  gap actually bit. Reopen if a future Excel import shows a plausibility
  error or a silent unthesised new position.
- **S22 — closed: the system side of this item is done.** Two safe tickers
  were already identified (SOBI.ST for Sobi, MEKO.ST for Meko AB) with the
  exact verified command to add them; the remaining ten names need a human
  at a broker screen to confirm a listing, which is not further system
  work. Add the two known-safe tickers whenever convenient. Reopen only if
  one of the ten unresolved names starts blocking a live decision (e.g. it
  would otherwise reach the candidate set).
- **S5 amended, not reopened under its own number.** The 2026-08-17 closure
  ("both the current mix and the adopted 85/10/5/0 target cleared") is
  reaffirmed on the number but overstated on the claim: the 2026-08-31
  Council memo found the backtest window's own worst equity drawdown is
  -19.14%, so it never actually contained a shock large enough to test a
  -30% tolerance. Per the never-reuse-an-ID rule, the narrower remaining
  question (a fixed-window test across a real >=-30% shock) is tracked as
  the new **S26**, not as a reopened S5.
- **Considered, not opened as a new S-item: second occurrence of the
  scheduled task's stored prompt containing stale premises.** First
  occurrence 2026-08-17 (contradicted CLAUDE.md, not opened, flagged
  directly to the user). This session's prompt separately (1) asked the
  memo to open with the Handelsbanken wrapper question, resolved
  2026-07-07/2026-08-03; (2) asserted `investor_profile.json.reference_targets`
  were still null, though they were adopted 2026-07-27; and (3) asserted
  this sweep's backtest was the first ever run, though one ran 2026-08-17.
  All three were caught and corrected in the memo itself with no wrong
  action taken, so this still self-mitigates rather than causing bad
  output — the same reasoning that kept the first occurrence off this list.
  But it is now two confirmed occurrences two weeks apart, not one: **if a
  third occurs, open the S-item without further deliberation.** In the
  meantime, whatever stores the scheduled task's prompt text should be
  reviewed and refreshed against current file state — the drift is coming
  from real progress (items closing, targets being adopted) outpacing a
  prompt written once and left alone.

### Closed by the 2026-08-24 discovery-funnel refactor

- **Removed: `data/learning_log.md` and `docs/v2-upgrade-spec.md`.** Both were
  write-mostly. The learning log was append-only and explicitly never a source
  of truth for a decision — the same bullets live in each dated Council memo,
  which is the actual record, and the append instruction was one of the more
  fragile things `council` had to do (read a growing file in full, concatenate,
  rewrite). The V2 spec was superseded: every phase's real status is in the V2
  Roadmap section above. Neither improved a decision. Git history holds both.

- **S12 — canonical definitions for ambiguous shared terms.** Closed: the
  remaining gap (one label covering two different bases) is fixed —
  `data/definitions.json` now carries a separate `risk_simulation_base`
  entry (investable-only, for translating drawdowns into SEK) alongside
  `investable_capital_convention` (full-portfolio, for allocation and
  trip-wires). The file also moved from `data/cache/` to `data/`; it is a
  pinned decision, not a regenerable cache.
- **S13 — CoinGecko fetch had no retry/backoff.** Closed: `fetch_crypto()` now
  retries three times with linear backoff before reporting an error, so a
  single HTTP 429 no longer takes out the whole crypto price path.
- **S15 — journal.md's write-safety instructions lagged its behaviour.**
  Closed: `journal.md` now states the read-whole-file/concatenate/verify
  procedure explicitly for both `SESSION_LOG.md` and `data/valuations.csv`,
  and requires writing nothing (and saying so) rather than risking a partial
  write.
- **S16 — no dependency manifest.** Closed: `requirements.txt` exists
  (`openpyxl`, `beautifulsoup4`) and `.claude/hooks/session-start.sh` installs
  it at session start.
- **S17 — the digest CSV dropped `currency`, making `fcf_b`/`mcap_b`
  non-comparable.** Closed: the candidates CSV carries `currency` and
  `country` per row, alongside `fcf_yield_pct` (a ratio, so
  currency-independent by construction).
- **S18 — [prospecting] scout's discretionary suggestions had no channel into
  the watchlist.** Closed structurally: the watchlist is now a first-class
  persistent file (`data/watchlist.json`) with `scripts/watchlist.py add` and
  `scripts/scout.py --promote`. A name scout surfaces can be recorded in one
  command and is screened on every subsequent sweep.
- **S19 — [prospecting] a decimal-scale `--max-debt-to-equity` silently
  produced a false zero-pass screen.** Closed: `scout.py` range-validates
  percentage-point-scale thresholds at parse time and refuses to run, and
  separately, any zero-pass result now triggers `diagnose_zero_pass()` and a
  status of `INVESTIGATE_ZERO_PASS` rather than a quiet empty screen.
- **Parked Excel-branch architecture retired.** `run.py`, `data/sync/`,
  `scripts/fetchers/`, `scripts/funnel/`, the generated `master.xlsx` and its
  builders, the coverage report, the controller state file and three one-time
  migration scripts are deleted. `scripts/import_excel_holdings.py` is the
  single Excel path, still read-only, and now merges into the persistent
  watchlist instead of overwriting a cache file.

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
