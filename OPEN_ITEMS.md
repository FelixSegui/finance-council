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

**Emphasis:** balanced

**Set by the 2026-08-24 discovery-funnel refactor.** The previous
portfolio-tending call was made when discovery was structurally capped at a
43-name list, so "there is no shortage of candidates" was true only inside
that list. The funnel now screens ~540 names and produced 35 candidates that
are neither held nor previously watchlisted — the discovery side of the
system changed materially and its first live output needs looking at. The
portfolio-tending signals that drove the last call are still live and still
matter: **AZN.ST's BUY has been the top call for three consecutive sweeps**
and the delay now has a price tag (the position moved from below blended cost
to +3.4% above it on unchanged fundamentals); **P3 (PayPal routing) is decided
but unexecuted for a third sweep**; **ABB.ST escalated to its first SELL call**
on 2026-08-24 and needs an actual decision, not more monitoring; and the three
2026-08-24 decision forks (ABB's freed slot, Investor A's NAV source, whether
any portfolio exclusions exist at all) are still unanswered. Balanced, not
prospecting: execute the standing calls *and* review what the wider funnel
surfaced. Revisit once AZN.ST and P3 execute or are explicitly declined — an
explicit "no" closes a loop as well as a "yes"; silence does not.

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
  tradeable ticker for live pricing of the Valour certificate (S1) — a
  pricing convenience, not a reason to reopen this item. Full
  deliberation history: `data/portfolio_history_archive.md#p4-deliberation-history-full-text-archived-2026-08-17-item-is-closed`.

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
- **Two flags carried forward, still relevant to what remains uninvested:**
  Spiltan Aktiefond Investmentbolag structurally overlaps your existing
  Investor A position; Swedbank Robur Technology A is a concentrated
  single-sector active fund with higher fees. Neither is disqualifying,
  both should be conscious choices if the remaining ~1,744 SEK (or future
  contributions) go toward them.

### P7 — Gold: new exposure class, instrument verified, ready to execute
- **Status:** decided, instrument verified — pending only the user's actual
  buy order. Council's Portfolio Governance call (2026-08-22): BUY, first
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

### S1 — Verified SEK crypto-certificate ticker for the held Valour position
- **Status:** open — blocks P4's verification (not P4's search, which is done)
- **Why:** the user holds a Valour Bitcoin Zero SEK certificate (ISIN
  CH0585378661). master-6.xlsx's Universe tab resolved it to `BTC0E.AS`
  (Euronext Amsterdam) and Yahoo recognises that ticker, but **the price does
  not reconcile**: Yahoo returns 47.292 EUR (~523 SEK) against a real known
  value of ~73.54 SEK/unit per Avanza — roughly 7x off — with identical
  52-week high and low, which suggests thin or stale data on that listing.
  Nordic crypto-ETP tickers (Virtune, Valour, XBT Provider, CoinShares) change
  and must be confirmed on Avanza, never guessed.
- **How:** verify on Avanza whether `BTC0E.AS` is genuinely this instrument's
  listing and why the price disagrees. Until then the position stays on the
  user-relayed price path and is excluded from automated repricing/drift
  checks — a 9,183 SEK position (~4.2%) with no live feed.
- **Note:** `python scripts/watchlist.py add/universe-add` now refuses to
  write a ticker that doesn't resolve to real price data, which prevents a
  *wrong* ticker being added — it cannot tell you whether a resolving ticker
  is the *right* instrument. That still needs a human at Avanza.

### S6 — No source for holding-company NAV discount/premium
- **Status:** open — blocks half of P5, and a Council voice wanted it on two
  consecutive sweeps and couldn't act
- **Why:** Investor A and Industrivärden cannot be valued on P/E; the real
  metric is NAV discount/premium, and no free automated source has been found.
  The funnel's `value` lens has the same blind spot — it ranks these names on
  earnings yield and price/book, neither of which means what it usually means
  for a holding company.
- **How:** parse the quarterly report PDF (the `pdf` skill can, given the
  report), or read it off Investor's IR page and record it in
  `data/company_profiles/INVE-A.ST.json` with source and date. One number,
  refreshed quarterly, not a fetcher.

### S9 — Excel import: two remaining data-quality checks
- **Status:** open — part (c) implemented and verified 2026-08-23
- **Why:** `import_excel_holdings.py` catches stale `as_of` dates, implausible
  P/E values and unfetchable tickers, and (since 2026-08-23) refuses to
  overwrite a CONFIRMED broker-sourced value with an Excel one. Two checks are
  still missing: **(a)** cross-field plausibility (a market cap and a share
  count that can't both be right), and **(b)** a flag when a new position
  appears in the workbook with no thesis recorded anywhere — a purchase the
  system has no stated reason for is exactly what `thesis-review` exists to
  catch, and it currently arrives silently.
- **How:** two more checks in the same `flags` mechanism, which already routes
  into `claude_excel_prompt.txt`. No new file, no new agent.

### S20 — [prospecting] Copycat/Smart Money has only half its data
- **Status:** open — new 2026-08-24, evidence is the voice's own named gaps
- **Why:** the Copycat voice was added to `council.md` this sweep. Two of its
  four named inputs are fetched (SEC Form 4 counts via `--insiders`,
  Finansinspektionen Insynsregister via `--fi-issuers`). **Institutional
  ownership changes, activist positions and 13F filings are fetched by no
  script in this system.** The voice is instructed to write `MISSING` rather
  than reason from training knowledge, which is correct but means it runs at
  roughly half strength on every US name.
- **How:** evaluate whether SEC EDGAR's 13F endpoints are reachable through
  this environment's proxy (`www.sec.gov` currently returns 403 through the
  tunnel; `data.sec.gov` untested). If reachable, a `--institutional` fetch of
  13F holder counts and quarter-over-quarter change per ticker would close
  most of the gap. If not reachable, say so in the item and stop — a blocked
  source that is honestly labelled beats a half-source that gets guessed at.

### S21 — [prospecting] Nordic coverage: 107 names, and a data asymmetry underneath
- **Status:** open — the headline problem is fixed; a quieter one it exposed is not
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

### S22 — [data] 12 real Swedish companies still cannot be screened
- **Status:** open — needs the user, not code
- **Why:** the 2026-08-24 import could not resolve 12 rows. Seven do not
  exist under any symbol Yahoo indexes and could not be found by company
  name either (BIOT.ST/Biotage, COLLE.ST/Collector, CONC.ST/Concentric,
  HALD.ST/Haldex, NYF.ST/Nyfosa, RESURS.ST/Resurs, SNDR.ST). Five resolve to
  a **different company** than the CSV names them: `MEKO.ST` is Meko AB
  (Mekonomen renamed, so the ticker is right and the CSV name is stale),
  `IVSO.ST` is Invisio (CSV typo "Invisibleio"), `VITR.ST` is Vitrolife (NOT
  Sobi — Sobi is `SOBI.ST`), `MEAB-B.ST` is Malmbergs Elektriska,
  `ALIF-B.ST` is AddLife. Three more are correctly excluded as no longer
  trading (Kindred, Probi, SAS).
- **How:** for each name still wanted, confirm the symbol on Avanza and add
  it with `python scripts/watchlist.py universe-add <TICKER> --name "<name>"`,
  which verifies before writing. Two are already known and safe to add:
  `SOBI.ST` (Sobi) and `MEKO.ST` (Meko AB). The rest need a human with a
  broker screen — the system deliberately will not guess a suffix.

### S23 — [measurement] Pillars 3, 4 and 5 have no data yet, and that is the binding constraint
- **Status:** open — structural, resolves only with elapsed time
- **Why:** `scripts/scorecard.py` now measures six pillars, and three of them
  correctly report "insufficient evidence": MECHANICAL needs at least two
  scout runs with recorded prices before a rank can be tested against what
  happened next, and JUDGEMENT and DECISION need `data/decisions.csv` to have
  rows, which only happens once `council` starts writing its picks file. **The
  scorecard's threshold is 20 observations per bucket and it withholds the
  number below that** — at one sweep a week with a handful of picks, the
  earliest a per-voice figure can mean anything is several months out.
- **How:** nothing to build. Run the sweep, let `council` write
  `data/picks/<date>-picks.csv`, record it, and wait. The failure mode to
  guard against is impatience: quoting a provisional median as though it were
  a finding, or lowering `MIN_OBSERVATIONS` to make the report look fuller.
  Both would defeat the entire purpose of the pillar.
- **Explicitly blocked on this:** any weighting of the Council. Until pillar 4
  shows the voices beating the mechanical shortlists they were handed, a
  weighted Council would be fitting weights to noise.

### S24 — [data] Nine metrics per sweep are real numbers with the wrong meaning
- **Status:** open — mitigated in code, root cause is upstream
- **Why:** the 2026-08-25 run flagged nine values outside plausible ranges,
  including Industrivärden at 1198% "revenue growth" (Yahoo counts investment
  gains as revenue for a holding company), Orexo at a 2775% profit margin, and
  ASML at a price/book of 1456. These are not fetch errors — they are correctly
  transmitted figures that do not mean what their field name says. Before this
  was caught, ORX.ST was placing on two lens shortlists on the strength of one
  of them.
- **Mitigated, not fixed:** implausible values are now withheld from lens
  scoring (so they cannot earn a shortlist slot) and shown with a `suspect`
  flag (so nothing is hidden or silently corrected). The name still reaches the
  Council, with less conviction, which is the honest outcome.
- **The real fix is an `entity_type` column** — holding company / bank / REIT /
  operating company — which no free source provides but a human can fill in
  once. It is request A1 in `reports/excel-upgrade-prompt.md`. With it, the
  screen can apply the right metrics per entity type instead of flagging
  healthy companies as data gaps: banks legitimately have no debt-to-equity,
  and holding companies legitimately have no meaningful revenue line.

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
  supports a rolling N-year lookback, no fixed `--start`/`--end`), and score
  calibration. `data/candidate_history.csv` is the calibration store this
  phase asked for — mechanical rank per candidate per run, correlatable
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
    missing institutional/activist data is now tracked as S20.
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
