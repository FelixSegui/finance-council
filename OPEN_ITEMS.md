# Open Items — single review surface

**This is the one place to look.** It replaces the old split between
`data/portfolio.json.open_structural_questions` (portfolio questions) and
`IMPROVEMENTS.md` (system changes), which forced you to check two places to
see what was outstanding. Consolidated 2026-08-03 at the user's request.

Two sections, one list:

- **P-items — your portfolio.** Things about your money. You decide these.
- **S-items — the system.** Things about this tool. The `meta` agent
  proposes them; nothing self-applies; you approve with "apply S3".

Each item says what it's blocking, so you can tell at a glance whether it
actually matters or is just paperwork. Every Council memo pulls its open
actions from this file. When an item closes, move it to the bottom log with
a one-line resolution — never delete an item silently.

**Status values:** `open` · `blocked (on what)` · `decided — pending execution` · `closed`

---

## This sweep's recommended emphasis

**Emphasis:** portfolio-tending
**Set by meta, 2026-08-24 (supersedes the 2026-08-18 call — the same
signal, now stronger, not resolved):** Every condition that drove the
2026-08-18 call is still live and has compounded rather than cleared.
**AZN.ST's BUY is now the Council's top call for a THIRD consecutive sweep
(2026-08-17, 2026-08-18, 2026-08-24) at High conviction, and this is the
first sweep the delay has a real, quantifiable price tag** — the position
moved from below blended cost to +3.4% above it while waiting, on
unchanged fundamentals. **P3 (PayPal routing) is decided but unexecuted
for a third consecutive sweep too**, and this sweep changed its funding
destination (GOOGL → META), adding a stale cross-reference in P3's own
note on top of the execution gap. **ABB.ST escalated from HOLD-WATCH to
its first-ever SELL call this sweep** — on the break condition's quieter
second clause (a materially better alternative surfaced), not the insider
clause everyone had been watching — which needs an actual decision, not
continued monitoring. And this sweep opened **three brand-new decision
forks (D-a, D-b, D-c)**: what to do with ABB's freed-up slot, whether to
finally source Investor A's NAV discount/premium (S6/P5, second
consecutive sweep a voice wanted to act and couldn't), and whether the
user has any stated portfolio exclusions at all (the reason the ESG
scorecard row is stuck at UNKNOWN). None of this is a prospecting gap:
`scout`'s screen ran cleanly this sweep — after a mid-sweep scale-bug
catch, see S19 — across the full 43-name candidate universe and surfaced a
well-evidenced new BUY (META) without difficulty; idle cash is already
earmarked (AZN.ST + META), not sitting with no plan. The constraint on
returns right now is human-execution lag on calls already made, not a
shortage of candidates. Per the rubric: three consecutive sweeps of an
unexecuted High-conviction call, a newly escalated SELL, and three fresh
open decisions is portfolio-tending's own definition, not a coin flip.
Revisit toward balanced/prospecting once AZN.ST and P3 execute (or are
explicitly declined) and D-a/D-b/D-c get answers — an explicit "no" closes
an open loop as well as a "yes"; continued silence does not.

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

## S — System items

### S1 — Verified SEK crypto-certificate tickers in the Watchlist
- **Status:** open — now directly blocking P4's verification, not P4's
  search. **2026-08-17 update:** P4's search itself is done — the user
  bought a Valour Bitcoin Zero SEK certificate (ISIN CH0585378661)
  directly. This item's remaining job for that specific instrument: find
  its real Avanza ticker (do not guess from the product name — verify),
  add it to the Watchlist tab with the ISIN, and let the same fee/backing
  verification P4 needs flow from a proper import rather than manual
  entry.
- Nordic crypto ETP tickers (Virtune, Valour, XBT Provider, Coinshares) change
  and must be confirmed on Avanza rather than guessed. **Updated 2026-08-06:**
  the destination for these is now the Watchlist tab in the user's Excel
  workbook, not `data/universe.json` (retired for this purpose — see the
  2026-08-06 closed-item log entry above). Until verified tickers are added
  there and imported via `scripts/import_excel_holdings.py`, the cheaper-
  certificate search can't be screened automatically. This used to be a
  nice-to-have; P4 makes it load-bearing.
- **Confirmed 2026-08-12, still a distinct problem:** the Watchlist's new
  `crypto_usd_proxies` category (added 2026-08-12) added `BTC`/`ETH`
  tickers, but these resolve to Grayscale mini-trust products (US-listed
  ETF-style wrappers), not Nordic-listed BTC/ETH certificates purchasable
  on Avanza inside the ISK. That's a different instrument in a different
  market — it does not close S1, and the two should stay cleanly separated:
  the 2026-08-12 CRYPTO & CERTIFICATE DETAIL Excel capability (see S7 in
  the Closed log) solved *pricing* for the certificate already held; S1 is
  about *discovering and verifying tickers for a replacement* certificate —
  still genuinely open, still the load-bearing blocker for P4.
- **2026-08-17 note:** the crypto-proceeds candidate offered this session
  (BITC, US-listed, ARCX) was rejected by Council specifically because it
  is not a verified Nordic/EU physically-backed BTC vehicle — the exact
  gap this item names. 12,853 SEK is earmarked and waiting on this, with a
  hard 2026-09-03 default to Avanza Global if nothing verified by then.
- **2026-08-18 note:** no progress this sweep — still `no price feed (S1)`
  in the position report, still blocking automated repricing/drift-checking
  of a 9,183 SEK (4.2% of portfolio) position. No new evidence, status
  unchanged.
- **2026-08-23 — a real ticker found, but NOT yet trusted as a live feed.**
  master-6.xlsx's Universe tab resolved this instrument via Excel's Stocks
  data type to `BTC0E.AS` (Euronext Amsterdam), consistent across its CORE
  HOLDINGS and CRYPTO & CERTIFICATE DETAIL blocks - `data/portfolio.json`'s
  ticker field updated accordingly. `scripts/fetch_market_data.py` confirms
  Yahoo recognizes this ticker. **Red flag, not yet resolved: Yahoo's own
  price (47.292 EUR, roughly 523 SEK at current FX) doesn't reconcile with
  the real known value (~73.54 SEK/unit per Avanza) - about 7x off - and
  its 52-week high/low are identical, suggesting thin/stale Yahoo data.**
  Do not wire this up as an automated feed until someone verifies on
  Avanza whether BTC0E.AS is genuinely the right listing and why the
  price disagrees this much. Position stays on the Excel-CRYPTO-DETAIL/
  user-relayed price path until then.
- **2026-08-24 note:** no progress this sweep. Position report still
  carries this as "no data"/user-relayed. Status unchanged.

### S6 — No source for holding-company NAV discount/premium
- **Status:** open — blocks half of P5
- Investor A and Industrivärden can't be valued on P/E; the real metric is NAV
  discount/premium, and no free automated source for it has been found.
  Options: parse the quarterly report PDF (the `pdf` skill can do this if you
  supply the report), or read it off Investor's IR page manually.
- **2026-08-18 note:** Council's Excel-improvement prompt now carries a
  concrete, one-time ask for exactly this (request H, 2026-08-18 block in
  `claude_excel_prompt.txt` — NAV per share for Investor A and Latour, from
  the monthly IR report, into the Manual Data sheet). This is S6's own
  Option 1, now phrased as a ready-to-paste user ask rather than just a
  standing item here. Status otherwise unchanged — still open, still
  blocking a testable INVE-A.ST thesis.
- **2026-08-24 note:** second consecutive sweep the Contrarian voice
  wanted to act on INVE-A.ST (96.9% of its 52-week range, upside cited at
  purchase already captured) and could not, purely on this missing metric
  — resolved HOLD again for the same reason. Now also tracked as open
  decision **D-b** in this sweep's memo. Status and fix unchanged; the
  Excel request H ask is still outstanding.

### S9 — Excel import script: three data-quality flags (cross-field plausibility + purchase-without-thesis + Excel-vs-confirmed-override conflicts)
- **Status:** partially closed 2026-08-23 — **fix (c) implemented and
  verified** (a CONFIRMED-marker check in `process_core_holdings` and
  `process_crypto_certificate_detail`, before any quantity/cost-basis/
  market-value delta is applied — if the holding's `thesis`/
  `thesis_narrative` text contains the literal word "CONFIRMED", the
  conflicting delta now goes to `flags` instead of silently overwriting).
  Verified against the live `master-5.xlsx` dry-run, still parses cleanly.
  **(a) and (b) remain open** — no cross-field ticker/name/price
  plausibility check, no purchase-without-thesis flag. Three real
  instances of gap (c) had occurred in six weeks before this fix (see
  below); this was the most-repeated, best-evidenced failure mode in the
  backlog, so it was fixed first rather than all three at once. **New
  2026-08-24: a fourth data-quality gap (d) confirmed, see below.**
- **Why (a)/(b), from 2026-08-06:** the Transactions sheet has a row pairing
  ticker "ethereum" with a certificate's name/price/quantity (`BUY,
  ethereum, 1 unit, 2016.67 SEK/unit`) — a likely copy-paste artifact next
  to the real COIN-XBT.ST 6th-unit purchase row. The import script only does
  per-field bounds checks (P/E sanity range, week52 range) and has no
  cross-field check (does the ticker plausibly match the row's own
  name/price), so it imported the bad row as-is into
  `data/transactions.csv`. Separately, four positions (ATCO-B, AZN, ALFA,
  ABB) were added to `portfolio.json` 2026-08-03/04 with no thesis, and
  nothing flagged it until a full Council run noticed — the same pattern
  that already happened once before with SHB-A.ST/INVE-A.ST (2026-08-03).
  (This second gap closed in substance 2026-08-12 when the user wrote
  theses for ATCO-B/ALFA/ABB/ETH — see P6/P5 — but the mechanism that
  should have caught the gap automatically at write-time still doesn't
  exist and will recur on the next unvetted purchase.)
- **Why (c), new 2026-08-12:** the workbook still carried the stale 1,743.61
  SEK Avanza ISK cash figure this sweep, and the import script applied it as
  a `portfolio_deltas` entry — the same class of write as any other Excel
  update. The only reason it didn't land in `data/portfolio.json` is that a
  human/agent noticed the conflict against the user's direct 2026-08-11
  statement (cash = 0) and rejected it by hand before committing. The
  script itself has **no mechanism to catch or flag this** — verified in
  `process_core_holdings`/`process_crypto_certificate_detail`, which apply
  every numeric delta unconditionally unless dry-run. Worse, because the
  conflict never became a `flags` entry, it never reached
  `data/cache/excel_import/claude_excel_prompt.txt` — the one Excel item
  with an actual track record of producing a wrong recommendation (it
  funded the incorrect 2026-08-11 "ADD 1 share AZN.ST" call) is invisible
  to the tool meant to help the user fix exactly this kind of Excel error.
- **Why (c), continued — 2026-08-17, a second confirmed instance in the
  same live session that closed several other items.** The 11:11 UTC Excel
  import wrote a further `CASH_SEK (avanza-isk): quantity 15366 -> 20366
  (from Excel)` delta. Only 15,366 SEK traces cleanly to the day's
  confirmed COIN-XBT.ST sale — the extra 5,000 SEK has no documented
  source, and, exactly as in the 2026-08-12 instance, never became a
  `flags` entry (confirmed directly against
  `data/cache/excel_import/latest-summary.json`, which lists four
  unrelated data-quality flags but not this delta). This time Council's own
  cross-examination caught it and explicitly sized every call against the
  traceable 15,366 rather than the Excel-carried 20,366 — so no wrong
  recommendation resulted — but it is the second time in three sweeps this
  exact gap has produced an unflagged, user-unconfirmed cash figure a memo
  had to work around by hand. Raises this from "worth doing" to "worth
  doing soon."
- **2026-08-18 note — the 5,000 SEK delta is unresolved and carried, not
  new (no Excel import ran this sweep to produce fresh evidence either
  way); but a distinct, independent confirmation of gap (a)'s general
  failure shape turned up in a different fetch path.** This sweep's memo
  flags that watchlist ticker `MC` (intended as LVMH) resolved to a
  completely different entity — roughly 4.9bn market cap, Financial
  Services sector — via `fetch_market_data.py`'s equity fetch, not the
  Excel import path. Same class of silent wrong-entity resolution gap
  (a)'s cross-field plausibility check (does the ticker's returned
  name/sector match what's on record) was designed to catch, just
  triggered outside Excel. The fix location for this specific ticker is
  the Watchlist tab itself (add the correct exchange suffix, likely
  `MC.PA`), not the import script — but it confirms the general pattern
  (an unverified/ambiguous ticker silently returning the wrong company's
  data) recurs across more than one code path, strengthening the case for
  (a)'s cross-field check as a standing guard, not a one-off.
- **Why (c), continued — 2026-08-22, a third confirmed instance.** The
  10:20 UTC Excel import wrote `CASH_SEK (avanza-isk): quantity 11183 ->
  20366 (from Excel)`. The gap (9,183 SEK) equals the un-logged Valour
  Bitcoin Zero certificate purchase exactly — `data/transactions.csv` has
  no BUY row for that purchase at all — and again this never became a
  `flags` entry. Same root cause as the two prior instances, third
  occurrence in six weeks: this is no longer an edge case, it's the
  script's most reliable failure mode. See P8 for the user-facing action
  (verify the real Avanza balance); this entry is the systemic fix still
  not built.
- **Why (d), new 2026-08-24 — a distinct manifestation of the same
  failure family, this time in the Watchlist itself rather than a
  transaction row.** This sweep's Council memo (section 12, data-gap #3)
  found three held tickers structurally absent from `scout`'s own screen
  digest: SHB-A.ST and ATCO-B.ST are held, but the Watchlist carries
  INVE-B.ST (a different share class than the held INVE-A.ST) and
  ATCO-A.ST (a different share class than the held ATCO-B.ST) instead,
  and there is no Handelsbanken row in the Watchlist at all. Three of the
  portfolio's seven individual holdings therefore got zero numeric triage
  from any of the six Council voices this sweep and had to be reasoned
  about from `valuation`'s prose alone — confirmed directly against
  `data/cache/watchlist.json`'s categories, not just the memo's own
  observation. Same root shape as (a) (an unverified/ambiguous ticker
  silently diverging from reality with nothing to catch it), just
  surfacing at the Watchlist-build step instead of the transaction-import
  step — a second, independent code path with the same defect class,
  strengthening the case that a standing cross-field/cross-file check
  belongs in this script generally, not only at the one spot (a) already
  names.
- **How:** in `scripts/import_excel_holdings.py`: (a) in
  `process_transactions`, add a bounded plausibility check — if a row's
  `holdings_ticker` matches a known ticker in `data/company_profiles/` or
  `portfolio.json` holdings, flag if `price_per_unit` is off by a large
  multiple (e.g. >5x) from that ticker's last known price, or if the row's
  `name` shares no token with the ticker's recorded name; (b) in
  `process_core_holdings`, when a holding's `quantity` moves from
  null/0 to a positive number (a new position) and its `thesis` field is
  null or `"TBD"`, add a flag naming the ticker; (c) in
  `process_core_holdings` and `process_crypto_certificate_detail`, before
  applying a numeric delta, check whether the target holding's own notes
  contain a direct-user-confirmation marker (a simple substring check for
  the literal word "CONFIRMED", already used throughout `portfolio.json`'s
  prose, is enough — no new schema needed) whose stated value conflicts
  with the incoming Excel figure; if so, add the conflict to `flags`
  (which reaches the prompt file) instead of silently overwriting it —
  same direction as this system's existing "a direct user statement
  outranks Excel" rule, just enforced in code instead of relying on a
  human noticing every time; (d), new 2026-08-24, in whichever function
  builds `data/cache/watchlist.json` from the Universe/Watchlist tab,
  cross-check the resulting ticker list against `portfolio.json`'s held
  tickers after each import: flag any held ticker absent from the
  Watchlist entirely, and flag any Watchlist entry that shares a company
  name/base ticker with a held position but a different share-class
  suffix (e.g. held ATCO-B.ST vs Watchlist's ATCO-A.ST). All four reuse
  the existing `flags` list already surfaced in `latest-summary.json` and
  read into the council memo — no new plumbing needed.

### S12 — Canonical definitions for ambiguous shared terms
- **Status:** open — one known small gap only (D3 and D4 both closed).
  **D3 CLOSED 2026-08-17** — user picked the full-portfolio convention,
  pinned in `data/cache/definitions.json` (`investable_capital_convention`).
- **D4 CLOSED 2026-08-23** — adopted reading 1 (target governs sizing;
  `profit_recycling_rule` only governs the surplus above target) as
  standing policy: this was Council's own recommendation across two
  sweeps with no dissent, and is now moot in practice anyway, since real
  broker data (P8, closed) makes the actual spendable cash a fact, not a
  reading. **Override available:** if the user wants gross-proceeds
  recycling instead (reading 2) on a future sale, say so and this gets
  amended — but nothing is blocked waiting on it now.
- **Known small gap, not yet fixed:** `definitions.json`'s current wording
  for `investable_capital_convention` reads broader than intended — it
  would also govern `backtest`'s risk-simulation base, which used the
  investable-only figure (188,839 SEK) the same day D3 pinned the
  full-portfolio figure (218,826 SEK) for allocation math. Defensible as
  two genuinely different purposes (a backtest can't simulate a tax
  reserve sitting outside the market), but should get a second, narrower
  `risk_simulation_base` entry rather than share one label. `meta`'s to
  pick up, not Council's file to self-edit.
- Full deliberation history (the three prior competing denominator
  readings, the 2026-08-11/12 timeline):
  `data/portfolio_history_archive.md#s12-full-deliberation-history-archived-2026-08-17-d3-closed-d4-still-open-but-consolidated`.

### S13 — CoinGecko crypto fetch has no retry/backoff; a single 429 kills the entire crypto price path
- **Status:** open
- **Why:** confirmed in code — `fetch_crypto()` in
  `scripts/fetch_market_data.py` makes exactly one HTTP request per call;
  any exception (including a transient HTTP 429) is caught and returned as
  `{"error": str(e)}` immediately, with no retry. In the 2026-08-17 morning
  sweep, three separate attempts to fetch bitcoin — the agreed directional
  proxy for the permanently-dead COIN-XBT.ST ticker (404, known since
  2026-08-03) — all returned HTTP 429. The only reason any recovery was
  attempted at all was three manual retries with `sleep` reconstructed ad
  hoc at the orchestration layer, which is not reusable and won't run
  automatically next time.
- **2026-08-18 note:** no incident this sweep — both BTC and ETH fetched
  cleanly. Still open on the strength of the earlier confirmed incident;
  judged "useful, can wait" in this sweep's roadmap review, not urgent —
  small, cheap, real, but low-stakes (a secondary directional-proxy input,
  not the basis of a live buy/sell call).
- **2026-08-24 note:** no incident this sweep either (BTC/ETH both fetched
  cleanly, +18.8%/+27.4% moves recorded). Status unchanged — still "useful,
  can wait."
- **How:** in `scripts/fetch_market_data.py`'s `fetch_crypto()`, wrap the
  single request in a small retry loop (2-3 attempts) with short
  exponential backoff (e.g. 2s, then 5s) specifically on
  `urllib.error.HTTPError` with `e.code == 429`, before falling back to the
  existing `{"error": ...}` shape unchanged. Keep the "no data is fine,
  never estimate" contract intact — this only makes the one existing fetch
  call more resilient to a transient rate limit; it does not add a new
  data source (see the 2026-08-12 `meta` debate for why a second live
  provider was considered and rejected).

### S15 — journal.md's instruction text lags behind its own already-correct behavior (SESSION_LOG.md prepend-safety AND data/valuations.csv append)
- **Status:** open — four sweeps of evidence now, including a third
  distinct corruption/near-miss incident on the same file this sweep (see
  the 2026-08-24 note below) — this is the single most-evidenced defect
  in the backlog. (This item absorbed S14 in an earlier session, see the
  Closed log — same defect shape, two different fields `journal` owns,
  one instruction file.)
- **Why (SESSION_LOG.md half, originally S15):** this session's [2026-08-17]
  `journal` subagent end-of-sweep write to `reports/SESSION_LOG.md` did not
  append/prepend correctly — it replaced the entire ~660-line append-only
  history with only the new entry. Caught immediately via a git diff and
  fixed by hand: full history restored, the new entry re-inserted above it
  in the documented format, committed as `1a2bef3`. No data was
  permanently lost (git history had the prior version), but the failure
  was **silent** — the subagent's own summary reported success, with no
  self-detected error, on the one file CLAUDE.md calls "the system's only
  calibration mechanism." The same day's later prepend (a second memo the
  same day) was done correctly and self-checked — but by ad hoc care in
  that turn, not because `journal.md`'s instructions were actually edited
  to require it.
- **Why (valuations.csv half, originally S14):** `journal.md` Mode 2
  (previously step 3, now folded into this item) says to "remind the user"
  to append a row to `data/valuations.csv`, even though `journal` already
  has Write tool access and could append it directly. The 2026-08-12 gap
  documents, in its own note field, that no row exists for that date "even
  though a council memo ran that day" — a confirmed, permanent gap in the
  performance-tracking series (append-only, cannot be backfilled).
- **2026-08-17 and 2026-08-18 note — both halves have now been executed
  correctly, ad hoc, without the instruction file changing, three sweeps
  running for the SESSION_LOG.md half and two for the valuations.csv
  half.** The 2026-08-17 live session's `journal` run appended the
  valuations.csv row directly instead of only reminding (per that
  session's own note, "computed directly rather than only reminded, per
  S14"), and this sweep's (2026-08-18) `SESSION_LOG.md` entry reads clean
  as a correct prepend, and the same sweep's `journal` run again appended
  the valuations.csv row directly ("the `data/valuations.csv` row has been
  appended directly by this `journal` run per S14, not just reminded").
  This is now the clearest pattern in the backlog of "the agent already
  knows the right behavior and keeps re-deriving it correctly by hand, but
  the instruction file itself was never actually edited to require it" —
  three correct manual executions in a row is stronger, not weaker,
  evidence that the fix should land in the instruction text before a
  fourth sweep happens to skip the ad hoc care.
- **2026-08-24 note — a second, independently-discovered SESSION_LOG.md
  corruption instance, of a different kind than the 2026-08-17 full
  rewrite, plus a self-inflicted near-miss of the identical artifact
  caught mid-write the same session.** While writing this sweep's own
  entry, `journal` found the file's prior end carried two stray leaked
  lines — literally `</content>` and `</invoke>`, tool-call syntax that
  had been written into the file itself rather than staying inside a
  prior write's own transcript — removed as corruption, not preserved as
  a real entry. Then, writing *this* entry, the same artifact was
  reintroduced by mistake on the first attempt and only caught by a
  post-write read-back before the sweep closed (per `SESSION_LOG.md`'s own
  2026-08-24 entry, which documents both incidents directly). That is now
  a third distinct corruption/near-miss event on this one file
  (2026-08-17 full overwrite; 2026-08-24 leaked XML found; 2026-08-24
  leaked XML re-introduced and caught), combined with a fourth-plus
  consecutive sweep of the correct SESSION_LOG.md/valuations.csv behavior
  being re-derived by hand rather than required by the instruction file.
  The fix S15 already specifies (a coded post-write self-check: line
  count increased, prior top entry's date still present) would have
  caught the leaked-XML instance mechanically instead of relying on a
  human/agent noticing it by eye, exactly as it would have caught the
  original 2026-08-17 overwrite. Cheap, well-specified, now evidenced
  three times on the one file CLAUDE.md calls the system's only
  calibration mechanism.
- **How (two edits, same file, same PR):** (1) in `journal.md`'s Mode 2,
  make the SESSION_LOG.md-write instruction explicit that it is a targeted
  insert — read the current file, prepend the new entry above the existing
  content (keeping the format-block header and all prior entries verbatim),
  write the concatenated result back — not phrased loosely enough ("write a
  new entry to the file") to be read as a full rewrite; add a post-write
  self-check: after writing, re-read the file and confirm (a) line count
  increased versus the pre-write read, and (b) the previous top entry's
  date/headline still appears somewhere in the new content; report the
  failure explicitly if either check fails, instead of a silent success
  summary. (2) change Mode 2's valuations.csv step from reminding the user
  to `journal` computing `total_value_sek` itself (sum `portfolio.json`
  holdings' market values against the snapshot used that sweep, same
  full-portfolio convention `position_report.py`/`portfolio` already use)
  and appending the row directly via Write, with an auto-generated `note`
  field in the same style as existing rows; keep a fallback — if `journal`
  can't confidently compute the total that sweep, it still reminds the
  user instead of guessing, same "no data is fine, don't estimate" rule
  that governs everything else in this system.

### S16 — No dependency manifest — a missing Python package silently broke a live fetch this session
- **Status:** open — no new evidence this session, status unchanged
- **Why:** this session's `swedish-equity-review` run on
  ATCO-B.ST/ALFA.ST/ABB.ST hit `No module named 'bs4'` on its first
  attempt at the Finansinspektionen insider-transaction fetch —
  `beautifulsoup4` was not installed in the environment, and nothing in
  the repo would have caught that before the run started. Confirmed: there
  is no `requirements.txt`, `pyproject.toml`, or `setup.py` at the repo
  root. Fixed by hand mid-session (installed, then the run repeated
  cleanly, per `SESSION_LOG.md`'s 2026-08-17 P6-review entry), but the
  failure surfaced mid-script rather than being caught up front — the same
  class of "fail clearly before doing partial work" problem this system
  already guards against for fetched data (`{"error": ...}` shapes, never
  silently estimating) but not yet for its own runtime environment.
- **How:** add a `requirements.txt` at the repo root enumerating the actual
  third-party imports used across `scripts/` and the skills/agents that
  shell out to them (at minimum `beautifulsoup4`, `openpyxl`; audit the
  rest via a quick grep for third-party `import`/`from` statements and
  cross off stdlib modules) with loose version pins. Optionally, pair it
  with a small startup check (a few lines in `fetch_market_data.py` or a
  standalone `scripts/check_env.py`) that attempts to import each required
  third-party module and reports which are missing in one clear line
  before any fetch begins, instead of failing partway through a specific
  skill's specific data source. Small, first confirmed instance — keep the
  fix proportionate.

### S17 — scout's digest CSV drops an already-fetched `currency` field, making `fcf_b`/`mcap_b` silently non-comparable across tickers
- **Status:** open — SECOND consecutive sweep of confirmed evidence
  (2026-08-18, 2026-08-24), root cause confirmed in code, fix unchanged
  and unapplied
- **Why:** this session's Council memo names, as its first Step-0 finding,
  that the digest's `fcf_b` (free cash flow, billions) and `mcap_b` (market
  cap, billions) are not on a consistent currency basis for the same
  ticker set — Ericsson's ratio (30.71/317 ≈ 9.7%) is plausible,
  Alphabet's (22.67/4,207 ≈ 0.5%) and TSMC's (730.83/2,235 ≈ 33%) are not,
  because market caps read USD-converted while cash-flow figures stay in
  the reporting currency. This made the Valuation voice's FCF-yield proxy
  (the system's stand-in for a missing EV/EBIT field) "unusable this
  sweep except where currency is confirmed identical" — directly degrading
  one of the six analyst lenses on every non-SEK candidate. **Confirmed in
  code, not just in the memo's own observation:**
  `scripts/fetch_market_data.py`'s `_fetch_fundamentals_direct()` already
  fetches and returns a `currency` field per ticker (`summary.get(
  "currency")`, the same currency `market_cap` and `free_cashflow` are
  quoted in) — but `scripts/funnel/screen_candidates.py`'s `DIGEST_COLUMNS`
  list (and its `row()` helper) never includes it, so the field is
  silently dropped between the full JSON and the digest CSV `council`
  actually reads. This is not a missing-data problem needing a new fetcher
  or a slower, user-dependent Excel round-trip (Excel request E, 2026-08-18,
  asks for the same thing via the workbook) — the data already exists in
  this sweep's own snapshot and just isn't being carried through.
- **2026-08-24 note — second consecutive sweep this exact gap has
  degraded the Valuation voice, root cause and fix unchanged.** This
  sweep's digest again produced non-credible FCF-yield ratios for every
  non-SEK mega-cap under discussion (GOOGL 0.54%, MSFT 0.46%, META 1.54%,
  AMZN 0.12%) — only SEK-denominated pairs (VOLV-B 3.4%, ERIC-B 9.7%) were
  usable. Nothing about the fix has changed since it was identified in
  code; this is now the strongest case in the backlog for a one-line
  change with a proven, repeated, real cost.
- **How:** in `scripts/funnel/screen_candidates.py`, add `"currency"` to
  `DIGEST_COLUMNS` and to the `row()` dict (`fields.get("currency")`, no
  transformation needed). This alone lets `council`'s Valuation voice see
  which tickers share a currency before treating an `fcf_b`/`mcap_b` ratio
  as comparable, instead of inferring it from the numbers looking
  implausible after the fact. Not required for this fix, but a reasonable
  follow-on: have the digest-writer null the ratio's *comparability* (not
  the field itself) when two tickers under discussion don't share a
  `currency` value — the exposed field alone is enough for the personas'
  own reasoning (council.md's existing "say explicitly when you're
  approximating" rule) to self-correct without it.

### S18 — [prospecting] scout's own discretionary candidate suggestions have no channel into the Excel Watchlist-addition request, and stay unscreened indefinitely
- **Status:** open — new evidence this session, confirmed directly against
  the live Watchlist and the Excel prompt file
- **Why:** on 2026-08-17, `scout` (acting on a direct user request for buy
  ideas) surfaced five discretionary tickers not derived from a numeric
  screen — MSCI, SNPS, ARM as gap-fillers against the 65.5% industrials
  concentration, SCCO and STL flagged as worsening it. None were added to
  the Watchlist, and the 2026-08-17 emphasis note explicitly named
  "screen them next sweep" as the plan. **Confirmed this session
  (2026-08-18): none of the five appear anywhere in
  `data/cache/watchlist.json`'s categories** (checked directly against the
  file), **and none appear in
  `data/cache/excel_import/claude_excel_prompt.txt`'s COUNCIL DATA
  REQUESTS blocks** (checked directly — neither the 2026-08-17 A-D block
  nor the 2026-08-18 E-H block names them) — the one channel this system
  already uses to turn a system-side finding into a user-actionable Excel
  edit (see request C, 2026-08-17, which successfully asked for a new
  Holdings row for the Valour certificate) was never used for these five
  tickers. This is a mechanism gap, not user procrastination: unlike an
  executable trade (AZN.ST, entirely the user's own broker action), getting
  a new ticker into the Watchlist requires the *system* to write the
  request somewhere the user will actually see it, and `council.md`'s
  Consolidated Excel-improvement prompt section currently only gathers
  per-pick "Excel data request" lines about missing *fields* on
  already-listed tickers — never `scout`'s own suggestions for tickers to
  *add*.
- **2026-08-24 note:** no new evidence this sweep — `scout` ran its
  standard numeric screen, not a discretionary pass, so the five
  2026-08-17 tickers (MSCI, SNPS, ARM, SCCO, STL) remain neither added to
  the Watchlist nor superseded. Status unchanged.
- **How:** in `.claude/agents/council.md`'s "Consolidated Excel-improvement
  prompt" section, add one instruction: if `scout`'s output this sweep
  names discretionary candidate tickers not already present in the
  Watchlist (distinct from the digest's own Passed/Missing/Failed lists,
  which are already-listed tickers), include a short "ADD TO WATCHLIST"
  block in `claude_excel_prompt.txt` naming each ticker, a suggested
  category, and the one-line reason `scout` gave for it — same imperative,
  ready-to-paste style already used for requests A-D. This wires up what
  `scout.md`'s own Job step 4 already half-anticipates ("tell them to add
  tickers to the Watchlist tab — or add them yourself if the user gave
  explicit tickers") to the one channel already proven to reach the user.

### S19 — [prospecting] scout's `--max-debt-to-equity` flag accepts a decimal-scale threshold silently, producing a false "zero passed" screen
- **Status:** open — new evidence this session, caught and corrected
  before use, concrete fix identified
- **Why:** this sweep's first screen run (`20260824T061207`) was invoked
  with `--max-debt-to-equity 2.0` against a field that
  `scripts/fetch_market_data.py` reports on a percentage-point scale (a
  real D/E in this universe runs well into the double or triple digits,
  not low single digits) — the threshold rejected every single candidate,
  producing zero Passed names. `scripts/funnel/screen_candidates.py`'s own
  docstring example already uses `--max-debt-to-equity 150`, confirming
  the intended scale — this is a unit/parsing gap, not a data problem. It
  was caught only because a human-in-the-loop step happened to review the
  digest before council consumed it; a genuinely quiet market and a
  silently-broken filter produce an identical, indistinguishable output
  (an empty screen) with no error raised either way. This is exactly the
  "was the screen wrong, or was the universe just thin" ambiguity the
  prospecting-capability check exists to catch — confirmed this sweep to
  be the screen, not the universe (the corrected run, `20260824T061349`,
  cleared 43 candidates through to council normally).
- **How:** in `scripts/funnel/screen_candidates.py`'s argument parsing,
  range-validate `--max-debt-to-equity` (and any other flag on the same
  known percentage-point scale) at parse time: if the supplied value is
  below a threshold that's implausible for the field (e.g. <5, since a
  real D/E ceiling in this system's usage has always been 100+), reject
  with a clear error message naming the expected scale and the docstring's
  own example, rather than silently proceeding to produce a screen with
  zero or near-zero Passed names. Keep this a hard parse-time error, not a
  warning, so a scheduled/automated run (like this sweep's) fails loudly
  instead of quietly producing an empty candidate pool that looks like
  "the market has nothing good in it."

---

## V2 Roadmap — user-authored, not meta-proposed

Full spec: `docs/v2-upgrade-spec.md` (verbatim, received 2026-08-09). This
is a user roadmap, not evidence-driven S-items — it sits outside the
≤10-open-S-items cap and `meta` doesn't prune it; it only moves as phases
actually get built. `journal`/`meta` should surface it at session start
alongside the S-items, not silently.

- **Phase 1 (foundation) — DONE 2026-08-09.** Structured thesis schema
  (`why_owned`/`expected_driver`/`valuation_reason`/`key_risks`/
  `break_conditions`/`thesis_status`/`last_reviewed` on every active
  holding in `portfolio.json`), Council's structured Chairman action
  format (ACTION/POSITION/TARGET/REASON/THESIS STATUS/WHAT CHANGED/BREAK
  CONDITION/CONFIDENCE/HORIZON), per-field data-quality states + a
  5-tier source hierarchy in `data/company_profiles/`, and new Layer A/B
  company metrics (`scripts/derived_metrics.py`; `ebitda`/`total_cash`/
  `total_debt`/`operating_cashflow`/`capex`/`ebit`/`equity_book`/
  `invested_capital`/`roic_pct` in `scripts/fetch_market_data.py`).
  Spec sections 4-5, 9 (partial - schema only, Fair Value Gap itself is
  Phase 2), 18-20, 24-25.
- **Phase 2 — not started.** Explicit Quality score vs Valuation score as
  two separate numbers (extends `swedish-equity-review`'s existing
  Score/Coverage rubric with real data underneath, now available via
  Phase 1), Fair Value Gap (`valuation_gap_estimate` with methodology/
  confidence/source/date, `UNKNOWN` when unreliable), PEG reframed as one
  input among several, never a hard rule. Spec sections 7-9.
- **Phase 3 — not started.** Wire the already-working
  `scripts/funnel/rank_candidates.py` (proven at 510-name scale, currently
  parked on the retired `data/cache/universe.json`) at the live
  `data/cache/watchlist.json` instead; add quality factors (ROIC/FCF
  margin/stability) using Phase 1's new metrics; make the funnel's
  threshold counts (~540→150-250→50-75→...) configurable in
  `config/settings.py`, not hardcoded; `scout` outputs a compact candidate
  dataset instead of prose. Spec sections 6, 10, 26, 28. **2026-08-17
  update:** the Watchlist is now a materially healthier input than when
  this phase was written — 67 entries (up from 32 on 2026-08-06, 45 on
  2026-08-12), 19 categories, and the format issue that used to cap it
  (12 malformed tickers) is now confirmed fixed — see the Closed log. This
  phase is more tractable than at any prior check. **2026-08-18 note:**
  `scout` now genuinely does output a compact candidate dataset (the
  digest CSV, shipped 2026-08-17) — the last clause of this phase's spec
  line is effectively already true in substance, even though it landed as
  part of the Stock Selection Council redesign rather than as a
  dedicated Phase 3 build. The funnel-wiring and quality-factor portions
  remain not started.
- **Phase 4 — not started.** `risk_factor_exposure` risk-bucket
  classification (Global industrial cycle / Defensive healthcare /
  Financials / etc.) distinct from sector — directly targets the Volvo +
  Atlas Copco + Alfa Laval + ABB correlated-industrial-risk problem this
  system already flagged (65.48% of the individual-stock sleeve as of
  2026-08-18, still ACT-rated). Portfolio-fit scoring for candidates ("does
  owning this improve the portfolio," not just "is it individually
  attractive") is now substantially live via `portfolio`'s expanded scope
  and the Chairman's PORTFOLIO-FIT REASONING stage (2026-08-17 redesign) —
  the risk-bucket classification itself is the part still not started.
  Spec sections 11-12, 23, 33.
- **Phase 5 — not started.** Macro Regime Engine expansion: new fetchers
  for BOJ policy rate, USD/JPY, credit spreads, PMI, unemployment/GDP,
  and a computed real-yield field — confirmed genuinely missing from
  `scripts/fetchers/fetch_macro.py` (2026-08-09 exploration). Multi-
  dimension regime classification (Liquidity/Inflation/Growth/Credit/
  Market risk/Currency-funding), `macro_fit`/`macro_sensitivity` per
  candidate, dynamic BUY thresholds (regime-dependent, configurable,
  never auto-selling on a regime shift alone). Spec sections 13-17, 31,
  34 (crypto-specific macro monitoring). **2026-08-18 note:** the
  no-commodity-price/no-credit-spread gap was named again this sweep, by
  the Macro/Regime voice itself, as the specific limit on its TTE/energy
  reasoning — live, current evidence this phase still matters, not
  historical only.
- **Phase 6 — not started.** Sell discipline (the 7 legitimate sell
  triggers + "would I buy it today?" - the latter already added to
  `thesis-review.md` in Phase 1, the former still open), crisis-window
  backtesting (`scripts/backtest.py` currently only supports a rolling
  N-year lookback from today, no fixed `--start`/`--end` - a real 2008
  test is likely blocked anyway by the current Watchlist's short-history
  proxies, confirmed 2026-08-09), portfolio risk-narrative section in the
  Council memo, `meta`'s expanded monitoring scope (data quality/model
  quality/AI quality/portfolio behavior/system efficiency), and the
  score-calibration framework (log scores now, correlate against realized
  returns later - there's no historical score data yet to backtest
  against, so this phase starts as instrumentation, not a real backtest).
  Spec sections 21-22, 29-30, 32, 37. **2026-08-17 note:** the ordinary
  rolling-lookback form of `backtest` (no crisis-window fixed dates
  needed) was sufficient to run S5 against the -30% tolerance, and S5 is
  now closed on that basis — a crisis-window (2008) test remains open
  here as a genuinely different, harder question ("what does the worst
  historical case do to this book," not "does a representative recent
  window clear the bound").
- **Phase 7 — Council architecture, five items, user-prioritized
  2026-08-18 (superseding the rough 2026-08-17 draft below with a
  precise spec).** The user's explicit priority order, kept verbatim as
  the sequencing for 7a-7d: (1) voice/Chairman isolation, (2) data
  quality and missing metrics — **already tracked, not a new item, see
  below**, (3) Copycat/Smart Money voice, (4) formal disagreement
  tracking, (5) historical tracking of recommendations/conviction. Build
  in this order; don't jump to 7b-7d before 7a lands, since 7b is
  specified as an isolated voice from the start (build it inside 7a's
  architecture, not bolted into the current single-agent `council.md`
  and rebuilt later).

  - **Phase 7a (priority 1) — Voice and Chairman isolation.** Today,
    `council`'s six analyst personas are role-played sequentially by one
    subagent invocation sharing one context window and, in practice, my
    own hand-written prompts have fed each analyst-lens agent (valuation,
    macro-regime, etc.) a summary of *other* agents' findings and prior
    sweeps' conclusions for context — real independence is enforced by
    instruction ("draft all X in isolation"), not by the architecture or
    the data-access boundary. The target design, precisely:
    - Each voice is a **separate agent invocation** (the orchestrating
      session spawns them, e.g. seven parallel `Agent` tool calls to
      dedicated agent definitions — `council-fundamentalist.md`,
      `council-valuation.md`, `council-growth.md`, `council-defensive.md`,
      `council-contrarian.md`, `council-copycat.md` once 7b lands,
      `council-macro.md`), each with its own tools/frontmatter so
      per-voice access grants are real restrictions, not just prompt
      instructions.
    - Every voice receives the **same core inputs**: the raw
      financial/candidate data (scout's digest + full screen JSON, the
      latest snapshot), and the portfolio data where relevant
      (`portfolio.json`, `investor_profile.json`) for context on existing
      holdings (needed to flag SELLs and avoid recommending something
      already massively held) — but explicitly NOT for portfolio-fit
      judgment, which stays downstream at the Chairman stage per 7's
      item 4 (see below).
    - A voice gets **explicitly named additional access** only if its
      role requires it — e.g. Copycat/Smart Money (7b) needs
      insider/institutional data beyond what's fetched today, so it
      would be the one voice granted `WebSearch`/`WebFetch` in its own
      agent definition, not a blanket grant to all seven.
    - Voices must **not** see: other voices' recommendations or
      reasoning, prior Council memos or `data/learning_log.md` (to avoid
      anchoring on last sweep's conclusions before forming this sweep's
      independent view), or the Chairman's analysis. Each voice's prompt
      is built from primary data files only — no "here's what happened
      last sweep" narration, which is how every voice prompt in this
      system has been written so far and would need to change.
    - The **Chairman** (`council-chairman.md`) is a separate final
      invocation, receiving only the seven voices' completed outputs
      (ideally each voice writes its structured output to a dated file —
      see 7d, this doubles as the historical record) plus the raw data
      and portfolio/OPEN_ITEMS context it's always had. It evaluates
      argument quality, not vote count — unchanged from today's design.
    - **Tradeoffs, unchanged from the 2026-08-17 draft, still real:**
      true isolation likely *increases* total token cost (each
      invocation loads its own copy of shared context instead of one
      subagent reading it once) and roughly doubles the number of agent
      invocations per sweep (7 voices + 1 Chairman vs. today's 1). It
      buys independence and per-voice tunability, not cheapness — accept
      that cost deliberately, don't discover it as a surprise.
    - **Status: roadmapped, not built**, per the explicit instruction to
      preserve the current architecture and not add complexity without
      evidenced need. The 2026-08-18 production sweep (first real run of
      the digest-based six-voice design) produced genuine, substantive
      disagreement with no visible sign of one voice's conclusions
      anchoring another's — one data point against urgency, not proof
      the failure mode can't occur. Build when the user says so
      explicitly, given the real cost tradeoff above.

  - **Phase 7 priority 2 — data quality and missing metrics: not a new
    item, already tracked.** Phases 2 (Fair Value Gap/Quality-vs-
    Valuation split), 3 (funnel wiring, quality factors), 4 (risk-bucket
    classification), and 5 (Macro Regime Engine expansion) below all
    cover this ground, plus the live S-items (S17: digest currency field,
    S18: unscreened discretionary candidates, and the Excel
    `COUNCIL DATA REQUESTS` items E-H: FX rates including DKK, per-row
    currency, watchlist 52-week ranges, holding-company NAV). The user's
    priority order asks that this ground get real attention before 7b-7d
    are built, not that a new phase be authored for it.

  - **Phase 7b (priority 3) — Copycat / Smart Money Analyst, a new
    Council voice.** Primary question: *what are informed insiders and
    sophisticated investors actually doing?* Focus: insider buying/
    selling (size, frequency, multiple insiders acting the same
    direction, CEO/CFO/board transactions vs. routine compensation —
    this system already fetches SEC Form 4 counts (US, `--insiders`) and
    Finansinspektionen Insynsregister direction-known trades (Sweden,
    `--fi-issuers`), a real head start), institutional ownership changes,
    major shareholder/activist positions, accumulation/distribution
    patterns. Assess the *quality and context* of a signal rather than
    treating every insider transaction as bullish/bearish by default (a
    CFO selling to cover a tax bill is not the same signal as a
    CEO buying on the open market — this system's insider-analysis
    findings this session, e.g. ABB.ST's insider-selling cluster and
    ALFA.ST's 10-for-10 open-market buys, already model this
    distinction; Copycat generalizes it into its own dedicated lens).
    Should also surface emerging meta-trends visible through insider/
    institutional positioning before they're an obvious consensus
    narrative. Same Council requirements as every other voice: >=3 BUY
    picks when the data supports it, SELL flags, conviction 1-10,
    concise reasoning, risks, missing-data notes. Institutional-ownership
    and activist-position data is **not currently fetched by any script
    in this system** — this voice is the one that would need an explicit
    `WebSearch`/`WebFetch` grant (see 7a) or a new fetcher, not silent
    reliance on training knowledge. **Status: roadmapped, build as the
    eighth isolated voice once 7a's architecture exists**, not bolted
    into the current single-agent `council.md`.

  - **Phase 7c (priority 4) — formal Disagreement Register in the
    Chairman's output.** For each candidate under real discussion (not
    just the Top 5), the Chairman states explicitly: degree of
    consensus/disagreement, strongest argument FOR, strongest argument
    AGAINST, the key disagreement between voices (named, not
    paraphrased into agreement), missing/conflicting data, and what
    information or event would change the call. This does not replace
    today's "Where the agents disagreed" memo section — it formalizes it
    into a per-candidate structured block rather than prose, and makes
    explicit what's already a stated rule (`council.md`: "don't average
    away disagreement" — see the Rules section) into a checked format
    the Chairman must fill in, not just a norm it's expected to follow.
    Consequence, already true in principle, worth restating because the
    user asked for it explicitly: a candidate can resolve to NO ACTION
    even with several voices favorably disposed, if the opposing
    argument or a real data gap makes the thesis impossible to
    underwrite — see 2026-08-18's ABB.ST call (held despite 3/6 voices
    favoring sell) and NOVO-B.CO (held despite standalone appeal, on a
    missing SEK/DKK rate) for two live examples of exactly this pattern
    already happening informally. **Status: roadmapped** — this one is
    lower-risk to build inside the *current* single-agent `council.md`
    if the user wants it sooner than 7a/7b, since it's a Chairman-output
    format addition, not an isolation-dependent change.

  - **Phase 7d (priority 5) — historical tracking of voice
    recommendations and conviction.** Log each voice's picks
    (ticker/action/conviction/date) somewhere queryable over time — the
    natural implementation is each voice writing its structured output
    to `data/cache/council_voices/<timestamp>-<voice>.json` once 7a
    exists (this doubles as the Chairman's input file and the historical
    record in one write, no separate logging step). Without 7a, a
    lighter version is still possible: extract the Top 5 + conviction
    scores from each dated Council memo into a running CSV/JSON, though
    that only captures the Chairman's synthesis, not each voice's raw
    call — a real loss of signal for score-calibration work (this is
    also Phase 6's "log scores now, correlate against realized returns
    later" instrumentation goal — the two phases would share one data
    store, not duplicate it). **Status: roadmapped, sequenced last** —
    depends on 7a for full value, has a degraded but real fallback
    without it.

  - **Item 4 of the user's 2026-08-18 request — keep portfolio analysis
    distinct from stock selection — is already satisfied, not a new
    build.** The user's exact pipeline: SWEEP → LENSES/FUNDAMENTAL SCREEN
    → BROAD CANDIDATE UNIVERSE → INDEPENDENT COUNCIL VOICES → CHAIRMAN →
    PORTFOLIO FIT → FINAL ACTION. This is precisely what the 2026-08-17
    redesign built: `council.md`'s Steps 0-2 find the best opportunities
    across the full universe (every holding + every watchlist entry, all
    three scout statuses) on standalone merit; `portfolio`'s
    diversification breakdown is consulted once, by the Chairman, in the
    dedicated `PORTFOLIO-FIT REASONING` field — *after* the opportunity
    is ranked, not before. Confirmed working as designed in the
    2026-08-18 production sweep: NOVO-B.CO ranked highest on standalone
    merit and still resolved to HOLD-WATCH for a portfolio/data reason
    (no SEK/DKK rate to size it), not a contradiction but the two-stage
    split doing its job. No action needed here beyond keeping it this
    way when 7a is eventually built — isolate the voices, but don't let
    portfolio-fit creep back into their scope.

  **Original 2026-08-17 draft, archived verbatim:**
  `data/portfolio_history_archive.md#v2-roadmap-phase-7-original-2026-08-17-draft-superseded-2026-08-18-by-the-users-detailed-5-item-spec-archived-verbatim`
  — same seven-parallel-plus-Chairman shape, same token-cost tradeoff,
  not duplicated here now that 7a supersedes it with a precise spec.

---

## Closed

Resolutions kept short; full history in `data/portfolio_history_archive.md`
and `reports/SESSION_LOG.md`.

- **2026-08-24 — considered, not opened as a new S-item: thesis-review
  incorrectly asserted OPEN_ITEMS.md hadn't been updated with ABB's
  2026-08-23 second FI-pull result, when it actually had been.** This
  sweep's Council memo (section 6) caught and corrected it directly — P6
  already carries the full 2026-08-23 entry recording the pull (no
  escalation, pattern quiet, 2026-09-03 default closed); only
  `data/company_profiles/ABB.ST.json` was still dated 2026-08-17. Notable
  as the *opposite* failure mode from the usual pattern this system
  catches (true staleness going unflagged) — here a genuinely current
  file was wrongly flagged as stale. Single instance, no diagnosed root
  cause (which specific check in `thesis-review.md` produced the false
  claim is unknown), self-corrected the same sweep with no downstream
  harm. Same treatment as the 2026-08-18 precedent for single,
  unconfirmed-pattern data mismatches: watch for a second instance before
  opening a formal item.
- **2026-08-24 — considered and rejected: restructuring `reports/
  SESSION_LOG.md` away from one growing markdown file to eliminate the
  overwrite/corruption risk S15 already tracks.** Raised after a second
  independently-discovered corruption instance (leaked tool-call XML,
  `</content>`/`</invoke>`, found and removed) plus a self-inflicted
  near-miss of the identical artifact caught mid-write the same session —
  see S15. Rejected: changing the file's read/write contract (e.g. one
  file per entry, concatenated at read time) would touch every place that
  already reads this file — `journal`'s own session-start read, this
  session's own reconciliation read — to solve a problem S15's existing,
  narrower proposal (a coded post-write self-check: line count increased,
  prior top entry's date still present) already solves at far lower cost
  with no format migration. Strengthens the case for landing S15 soon
  rather than for a bigger rebuild.
- **2026-08-23 (second pass, same day) — import_excel_holdings.py updated
  for master-6.xlsx's restructured workbook.** The user replaced master-5
  with a rebuilt master-6.xlsx (dropped the standalone Watchlist tab,
  merged everything - held positions and watchlist candidates alike -
  into one "Universe" tab distinguished by a `status` column). Added a
  Universe-tab reader (falls back to the old Watchlist tab if a workbook
  doesn't have Universe) - watchlist.json regenerated cleanly, 67
  candidates, no capability lost. Also fixed two real bugs surfaced by
  the new workbook: (1) a closed position with quantity 0 (COIN-XBT.ST)
  was being flagged every run as "held but missing from Excel" - it's
  correctly absent, not a gap; (2) a broker-verified fundamentals
  correction (ATCO-B.ST's P/E) got silently overwritten back to Excel's
  known-bad value on the very next import, since only the portfolio-delta
  path had the 2026-08-23-morning CONFIRMED-marker protection, not the
  fundamentals path - added the same protection there (a value already
  sourced from a lower/better source_tier than Excel's now gets flagged,
  not clobbered).
- **2026-08-23 — P8 closed: ISK cash reconciled to 11,288 SEK, real
  broker figure.** The 20,366 SEK Excel-import figure was wrong (a
  pre-Valour-purchase balance carried in the workbook). Resolved directly
  from the user's own Avanza screenshot ("Tillgangligt for kop: 11,288
  kr") — closer to the previously-computed 11,183 SEK reading than to the
  Excel figure. `portfolio.json` updated; the missing Valour BUY
  transaction (the actual root cause — see S9) added to
  `data/transactions.csv` retroactively, along with a missing 5,000 SEK
  2026-08-22 deposit and a fee/PnL correction on the COIN-XBT.ST sale row,
  all reconciled against the user's real Avanza transaktioner export.
- **2026-08-23 — S12/D4 closed: adopted "target governs sizing" as
  standing policy for `profit_recycling_rule`, moot in practice once P8
  gave a real cash figure.** Three consecutive sweeps of the same open
  question resolved by policy default (Council's own twice-repeated,
  undissented recommendation) rather than a fourth sweep of workaround
  sizing. User can override on a future sale by saying so.
- **2026-08-23 — S4 closed: Swedish CPI fetcher fixed and verified.**
  Root cause found: `KPItotM` (the table the fetcher used) was silently
  discontinued by SCB after 2025M12 — confirmed via the table's own
  metadata, which labels it "(no update after 2025M12)." Switched to
  `KPI2020M`, reading SCB's own precomputed annual-change content code
  directly instead of manually diffing an index ratio (which had its own
  latent bug — the default content code is blank for most historical
  months). Verified live: returns 0.2% for 2026M07, current to ~1 month
  rather than 8. Four consecutive sweeps had cited this as a live
  confidence cap on 65%+ of the stock sleeve.
- **2026-08-23 — S9(c) implemented** (the most-repeated of S9's three
  gaps — three confirmed instances in six weeks): `import_excel_holdings.py`
  now checks for a "CONFIRMED" marker in a holding's thesis/notes before
  applying an Excel-sourced quantity/cost-basis/market-value delta, and
  flags the conflict instead of silently overwriting. (a) and (b) remain
  open — see S9.
- **2026-08-23 — P6's ABB.ST second FI pull run, break condition resolved
  NOT triggered.** marknadssok.fi.se, previously believed blocked in this
  environment, is reachable again — confirmed live. Same insider-selling
  cluster already on record, no new disposals in 10 days. Closes out the
  standing 2026-09-03 default date for this specific condition.
- **2026-08-23 — Three company_profiles P/E figures corrected against
  real broker data** (Avanza terminal screenshot + cross-check against
  Yahoo's independent trailing_pe): ATCO-B.ST 2.05 -> 32.63 (the exact
  figure this session's Excel-import flagged as suspect), AZN.ST 22.98 ->
  25.49, INVE-A.ST 6.56 -> 4.76. ABB.ST/ALFA.ST/SHB-A.ST/VOLV-B.ST already
  agreed closely with the broker figures - left unchanged.
- **2026-08-23 — P2 closed: remaining item (discovery funnel) is a
  duplicate of V2 Roadmap Phase 3, not a distinct open item.** Two of
  three original items were already done (2026-08-06); the third
  (`scripts/funnel/build_universe.py`, index-sourced universe + factor
  ranking) is word-for-word the same work item as Phase 3's "wire the
  already-working `rank_candidates.py`... at the live watchlist instead."
  Tracking it in two places was the actual redundancy — kept only in the
  V2 Roadmap now, where it already lived.
- **2026-08-23 — `IMPROVEMENTS.md` deleted.** Pure stub since 2026-08-03,
  pointing to this file; kept no independent content. Referencing files
  (`CLAUDE.md`, `journal.md`, `meta.md`) updated to say it's gone rather
  than pointing at a stub.
- **2026-08-18 — S8 closed under cap pressure (10-item limit reached this
  session, two new evidence-backed items added), not because the
  underlying risk resolved.** Zero incidents of S8's specific failure mode
  (a git merge silently dropping a critical file) since the original
  2026-08-03 event, across roughly 15 sessions of routine
  `check_unmerged_work.py` runs finding nothing — the closest thing to
  evidence this specific risk has receded, though absence of an incident
  is weaker evidence than a landed fix. S15 (expanded this session, see
  below) already implements the more precise half of what S8's own
  2026-08-17 note proposed generalizing toward — a post-write
  line-count/content self-check — for the one file that has actually
  broken (`SESSION_LOG.md`, via a different root cause: agent overwrite
  behavior, not a git merge). S8's remaining distinct scope — a manifest
  check across all five named critical files, specifically at the
  git-merge boundary — is not implemented anywhere and is not covered by
  S15. **If a git-merge-boundary file-loss incident recurs, reopen this as
  a fresh item rather than assuming it's covered** — this closure is a
  documented backlog trade-off under the cap, not a claim the original
  risk is gone. Full original text preserved in this file's git history.
- **2026-08-18 — S14 closed, merged into S15.** Same defect shape as S15
  (journal.md's Mode 2 instruction text lags behind behavior the agent has
  already executed correctly, ad hoc, multiple sweeps running) applied to
  a different field journal.md owns (`data/valuations.csv`'s append,
  vs. S15's `SESSION_LOG.md` prepend-safety). Both fixes land in the same
  file in the same edit, so one `apply S15` now closes both gaps in a
  single pass rather than two separate approvals for the same instruction
  file. See S15 above for the merged Why/How.
- **2026-08-18 — considered and rejected: a new mechanism to prompt/remind
  the user to execute an unexecuted headline call between sweeps.**
  AZN.ST's BUY has now been the Council's top or near-top call for two
  consecutive sweeps (2026-08-17, 2026-08-18) at High/zero-dissent
  conviction, unexecuted both times — the same shape as the PayPal routing
  pattern (4+ sweeps) and the pre-closure `swedish-equity-review` pattern
  (7 sweeps) already in this system's history. Rejected for the same
  reason the equivalent 2026-08-17 proposal was deferred: CLAUDE.md is
  explicit that this system "produces analysis and flags; it never
  executes trades" and has no channel to reach the user outside a sweep —
  the mechanism already in place (re-deriving the call fresh from new data
  each sweep, with escalating language in the memo and in `journal`'s
  reconciliation — this session's SESSION_LOG entry calls it "the
  strongest version of 'the call didn't age badly, it just didn't get
  acted on' this log has recorded") is doing its job: the call is not
  stale, it is awaiting the human-in-the-loop action this system is
  deliberately designed to require, not a system failure to communicate.
  Distinguish from the dated-deadline-plus-hard-default mechanism used for
  PayPal/ABB, which exists because those specific cases had a genuine
  cost-of-waiting or a data-quality trigger to hang a date on — AZN.ST has
  no such trigger, and forcing one would manufacture urgency the data
  doesn't support. Revisit only if a third consecutive sweep produces the
  identical unexecuted call with literally no user engagement at all,
  which would suggest the flagging isn't reaching the user, not that it
  isn't loud enough. **2026-08-24 note: this is now the third consecutive
  sweep of the identical unexecuted AZN.ST call — but not revisited,
  because the stated revisit condition ("no user engagement at all") did
  not fire.** The user has been actively engaged with the system across
  the intervening off-cycle sessions (2026-08-22/23: confirmed the real
  ISK cash balance, executed the Valour BTC certificate swap, reviewed
  and cleared the gold instrument, fixed several data-quality bugs) — the
  flagging is reaching the user; this reads as a deliberate non-action on
  this specific call, not a communication failure. The three-sweep
  pattern is tracked as this sweep's portfolio-tending emphasis signal
  instead (see the top of this file), not reopened as a system defect.
- **2026-08-18 — considered and rejected: giving `council` the `Edit` tool
  instead of just `Read`/`Write`, to simplify its append to
  `data/learning_log.md`.** `council.md` already carries the exact
  safe-append workaround this needs (read the full file, concatenate,
  write back; if that feels unsafe in one pass, say so explicitly and let
  the orchestrating session apply it by hand instead of risking a silent
  partial write) — added after S15's `SESSION_LOG.md` incident, and used
  correctly this session (this sweep's learning-log append was staged for
  the orchestrating session to apply, per the memo's own report, not
  written incorrectly). This is the safeguard working as designed, not a
  defect surfacing: the one failure mode it exists to prevent (a silent,
  incorrect partial overwrite) did not happen. Adding `Edit` would remove
  one manual step but also widens the tool surface of the single
  highest-stakes agent in this system for a convenience gain, not a
  correctness one. Revisit only if the read-then-write pattern itself
  produces an incorrect append (not just an extra manual staging step) in
  a future sweep.
- **2026-08-18 — two data-consistency findings this session, judged not
  yet a pattern worth a new S-item; watching for a second confirmed
  instance of each, not opening on one.** (1) `valuation`'s prose
  described VOLV-B.ST as a "3rd straight year of revenue decline on
  trailing" against the same snapshot's own four-year series showing two
  consecutive declines and a trailing flip to +2.7% growth — a one-off
  phrasing drift, caught and correctly overridden by Council's own
  cross-examination (the fetched series was treated as primary), first
  occurrence of this specific lens-summary-vs-fetched-data mismatch.
  (2) A sharper version on TTE: this sweep's digest reports +27.8%
  revenue growth while last sweep's full-JSON multi-year series showed
  four consecutive declining years for the same ticker — a genuine
  system-internal data contradiction (not just prose drift), correctly
  resolved to NO ACTION rather than picking a side, with a concrete
  one-pull re-test named for next sweep. Neither opened as an S-item: (1)
  is a single phrasing slip with no code defect identified; (2) doesn't
  yet have a diagnosed root cause (a ticker-resolution error, like this
  same sweep's confirmed `MC`≠LVMH mismatch — see S9 — is one plausible
  explanation, but unconfirmed for TTE specifically) — writing a "How"
  before next sweep's re-pull would be guessing. Revisit if either
  recurs, or once TTE's re-pull reveals a specific, fixable root cause.
- **2026-08-17 — S5 resolved: the `backtest` agent ran for real (its first
  execution ever) and both the current mix and the adopted 85/10/5/0
  target clear the -30% drawdown tolerance.** Over an 86-month window
  (2019-06 to 2026-08, `data/cache/backtests/20260817T111722.json`,
  `111730.json`, `111736.json`): current mix max drawdown -14.6%, adopted
  target -19.95% — the opposite of the same-day morning memo's
  illustrative (explicitly non-backtest) -42.3%/-45.75% estimate.
  **Read this as "clears one real test," not "validated":** the window
  excludes 2008 entirely, produced a 15.0% CAGR (roughly double a
  realistic long-run global-equity return — itself a sign of an unusually
  generous period), models no fees/taxes/FX, and the target's max
  drawdown equals its worst rolling 12 months — the whole fall happened
  inside a single year, the hardest kind to sit through behaviourally.
  Council's own memo (`reports/2026-08-17-council-memo-2.md`, Call 5)
  says this explicitly and moved the scorecard's drawdown row to "OK
  (provisional)," not "validated." A genuine crisis-window test (fixed
  `--start`/`--end` covering 2008) stays open under V2 Roadmap Phase 6,
  not reopened as a new S-item.
- **2026-08-17 — real code bug found and fixed: `scripts/backtest.py` had
  never actually worked in this environment.** Its yfinance client failed
  the same way CLAUDE.md already documents for `fetch_market_data.py` —
  curl_cffi's browser-TLS-fingerprint impersonation gets connection-reset
  by Yahoo's anti-bot layer on this network. Fixed with the same pattern
  already used elsewhere: direct `urllib` calls to Yahoo's v8 chart
  endpoint via a cookie jar, bypassing yfinance's own client entirely.
  Confirmed in code and validated against the script's own known-good
  example before the new S5 result was trusted (per this session's
  `SESSION_LOG.md` entry). This is what made S5 possible to actually run,
  not just propose — recorded as its own resolved defect since it's a
  distinct, previously-undiscovered bug, not simply "S5 got done."
- **2026-08-17 — Watchlist 12-ticker malformed-format issue CONFIRMED
  FIXED, closing the same-day addendum above.** A fresh Excel import this
  session (11:11 UTC, `data/cache/excel_import/latest-summary.json`,
  watchlist grown from 45 to 67 entries) shows all 12 previously-malformed
  tickers now carry proper exchange suffixes — verified directly in
  `data/cache/watchlist.json` (`SEB-A.ST`, `SWED-A.ST`, `HM-B.ST`,
  `SAAB-B.ST`, `NOVO-B.CO` and the rest all present, correctly suffixed,
  under `nordic_financials`/`nordic_consumer_retail`/
  `nordic_aerospace_defense`/`nordic_large_cap`). User-side Excel fix,
  same as the original S10 closure — `meta` didn't drive it. One caveat:
  the same day's Council memo's own "Excel data gaps" section still
  describes the 12 tickers as "still unfetchable," which is stale by the
  time of the 11:11 import — a minor memo-authoring inconsistency (that
  Council run had no shell access and likely didn't re-read the freshest
  import summary for that specific section) rather than a data-pipeline
  defect. Not worth a new S-item; noted here for the record.
- **2026-08-17 — proposal: a standing guardrail checking whether a
  portfolio-agent rebalancing recommendation conflicts with an open
  blocking P-item (e.g. recommending an ETH add while P1/cost-basis is
  open) — deferred, not opened.** Real and correctly caught this session:
  the portfolio agent listed "more self-custody ETH" as an equivalent
  fallback to "stays in cash" if BITC turned out unbuyable; Council
  rejected it because P1 (ETH cost basis) being open means every future
  ETH disposal is an uncomputable 30% K4 event, and adding units makes a
  solvable record-keeping gap permanently harder. Same precedent this
  file already applies elsewhere (see the 2026-08-11 capital-availability
  entry below): one occurrence, caught the same sweep by Council's own
  adversarial method before it reached the user, isn't yet a pattern.
  Revisit if a second, independent instance of a portfolio-agent
  recommendation conflicting with an open blocking item turns up.
- **2026-08-17 — P7 closed: ISK allowance threshold confirmed by the user
  at 300,000 SEK.** The system had been assuming ~300k unverified; the user
  confirmed the figure directly (no Skatteverket lookup needed). Current ISK
  total (~194k SEK as of this sweep) has comfortable headroom under it — see
  `data/portfolio.json`'s `avanza-isk` account notes.
- **2026-08-17 — D3 (crypto trip-wire denominator, S12) decided by the user:
  full-portfolio convention, not Council's recommended investable-only
  reading.** User's words: "It should be option 2 - on Full portfolio
  (214,218.98 SEK)." Pinned in `data/cache/definitions.json`
  (`investable_capital_convention`). Consequence: under this convention the
  12% crypto trip-wire did NOT fire on the 2026-08-17 numbers (11.43% vs.
  Convention B's 12.97%) — recompute future trip-wire checks against the
  full-portfolio denominator, not Convention B. S12 itself stays open for
  the D4 sub-question (gross-proceeds vs. realized-gain-only for profit
  recycling) — this was first thought moot given the COIN-XBT.ST full sale,
  but the same day's second Council memo caught that the opposite is true
  (a full sale makes the two readings' gap the largest it has ever been) and
  REOPENED D4 rather than closing it — see the S12 entry above and P4.
- **2026-08-17 — Watchlist 12-ticker malformed-format issue confirmed
  still open, addendum to the 2026-08-12 S10 closure (not a reopening).**
  S10's closure was correct on its own terms — the four named entries (HM
  B, SEB A, SWED A, SAAB B) are genuinely present in the Watchlist for
  category coverage. Separately, the most recent Excel import (2026-08-13,
  `data/cache/excel_import/latest-summary.json`) confirms all 12
  space-instead-of-suffix tickers flagged 2026-08-11/12 — including these
  same four — are still unfetchable; the existing `claude_excel_prompt.txt`
  mechanism (CLAUDE.md flow step 1a) already surfaces the exact fix to the
  user each import. No new S-item: this is a pending user-side Excel edit
  already correctly flagged by the system, not a code gap.
  **Superseded same day, see the new 2026-08-17 entry above — the 12
  tickers are now confirmed fixed.**
- **2026-08-17 — proposal (Maverick, this session's debate): add a second
  live crypto price source as a tertiary fallback to CoinGecko —
  rejected.** Confirmed real evidence this session (CoinGecko 429×3) but
  the Minimalist's counter won: retry-with-backoff on the existing single
  source (S13) addresses the actual failure mode (transient rate-limiting)
  more cheaply than a second live provider, which would double the
  plausibility-check surface for a feed that is already secondary
  (directional proxy only) on a position about to shrink via its own trim.
  Revisit only if 429s recur even after S13's retry logic ships.
- **2026-08-17 — proposal: visually distinguish previously-dated-but-
  unexecuted Council calls in the memo format — deferred, not opened.**
  Real pattern this session (now two instances: the COIN-XBT.ST trim dated
  "execute Monday" and not executed; PayPal's 4th consecutive sweep of
  identical advice) but Council's own escalation mechanism (dated deadline
  + hard default, already used for ATCO-B/ALFA/ABB since 2026-08-12 and
  now for PayPal) appears to be handling this adequately without a format
  change. Revisit if a 2026-09-03 deadline itself passes with no user
  action, which would suggest the escalation mechanism alone isn't
  sufficient.
- **2026-08-17 — the scheduled task's stored prompt text contradicting
  CLAUDE.md (twice this session) — not opened as an S-item, flagged
  directly to the user instead.** Real, recurring friction (a stale
  `--crypto ethereum`-only fetch flag, and a false "memo MUST open with the
  Handelsbanken wrapper" premise resolved 2026-07-07) but the fix lives
  entirely outside this repo — in whatever external tool stores the
  scheduled task's prompt — and `meta` has no file in this repo to propose
  a concrete "how" against. Both instances were correctly caught and
  overridden by following CLAUDE.md this session, so there is no
  data-integrity harm yet, but the pattern will keep recurring on every
  future firing until the user edits the stored prompt directly.
- **2026-08-12 — S3 fixed and confirmed (earnings calendar fetch failing).**
  `scripts/fetch_calendar.py`'s `fetch_earnings_dates()` now calls
  `_yahoo_session.fetch_quote_summary(t, modules="calendarEvents")` — the
  same direct-urllib + crumb/cookie-jar bypass `fetch_market_data.py`
  already uses for fundamentals — instead of `yf.Ticker(t).calendar`, which
  routed through yfinance's own client and got connection-reset by Yahoo's
  anti-bot layer on this network. Confirmed in code this session and
  confirmed live against real tickers (AZN.ST/VOLV-B.ST/AMZN, per
  2026-08-12's `SESSION_LOG.md` entry) — the earnings-date fetch is
  genuinely available for the first time since 2026-08-03.
- **2026-08-12 — S7 fixed and confirmed (self-custody crypto never
  repriced in `position_report.py`).** `scripts/position_report.py` now has
  a dedicated `spot_crypto_row()`, wired into `main()` via a check for
  `instrument_type == "spot_crypto"` — pulls `cur_snap["crypto"]`, converts
  via `sek_per_eur`, matches `equity_row`'s shape. Confirmed in code and
  confirmed live this sweep: ETH reprices to 8,945.96 SEK in the position
  report instead of carrying the stale 2026-08-03 book value the portfolio
  agent had been correcting by hand for two prior sweeps.
- **2026-08-12 — S10 resolved, not just improved.** All three specific
  gaps the item named are directly fixed in the Watchlist as of the
  2026-08-12 Excel import: `HM B` (category `nordic_consumer_retail`),
  `SEB B` + `SWED A` (category `nordic_financials`), and `SAAB B` (category
  `nordic_aerospace_defense`) are all present, each with a note explaining
  what gap it fills. The `broad_index_etfs` category's US-domiciled entries
  (VOO, QQQ, IWDA) are no longer the only option — a new
  `eu_ucits_etf_alternatives` category (CSPX, EQQQ, VWCE) sits alongside
  them, each row's note explicitly cross-referencing which US-domiciled
  ticker it substitutes for if that one isn't purchasable on Avanza.
  Watchlist entry count also grew from 32 (2026-08-06) to 45, above the
  ~43-ticker `universe.json` it replaced. Verified directly in
  `data/cache/watchlist.json` this session, not just from the import
  summary's entry count. This is a user-curated-content fix (the Watchlist
  tab), not a code change, and the user made it before `meta` even proposed
  it — recorded here as resolved evidence, not as a `meta`-driven fix.
  **See the 2026-08-17 addendum above: category coverage is genuinely
  fixed, and as of the second 2026-08-17 addendum, the ticker-format issue
  is now also fixed.**
- **2026-08-12 — Transaction-dedup bug found and fixed the same session,
  never carried forward as an open item.**
  `scripts/import_excel_holdings.py`'s `key_val()` compared numeric fields
  as raw strings, so `"1520.50"` and `"1520.5"` were treated as different
  values — the same real AZN.ST trade got logged twice (once via manual
  entry, once via Excel import) because the two `price_per_unit` strings
  differed only in a trailing zero. Fixed at the root: `key_val()` now
  normalizes numerics via `float()` comparison before falling back to a
  plain string compare, with the incident documented directly in the
  function's own comment. Confirmed in code this session.
- **2026-08-12 — Capital-availability premise check (deferred 2026-08-11
  as "one occurrence isn't a pattern") — now resolved and confirmed
  working.** Not via a new S-item: a "Capital-availability premise check"
  paragraph is now written directly into `council.md`'s Investment Council
  method, explicitly citing both the 2026-08-10 (Avanza Global routing) and
  2026-08-11 (AZN.ST funded from cash that didn't exist) incidents as the
  evidence for it. This session's Call 1 (trim COIN-XBT.ST) used it
  correctly: rather than assuming idle cash was available, it explicitly
  verified `portfolio.json`'s ISK cash figure against this sweep's own data
  (confirmed 0) before finalizing a call that generates and redeploys
  capital — see the memo's "Capital-availability check" line. Two
  occurrences (2026-08-10→11, 2026-08-11→12) were both caught before
  execution by `journal`'s reconciliation; the standing guardrail now
  closes the gap going forward instead of relying on reconciliation to
  catch it after the fact each time. No further S-item needed unless the
  guardrail itself is bypassed in a future sweep. **2026-08-18 note:** used
  again this sweep, correctly — confirmed the 11,183 SEK ISK cash figure
  and its D4-dependent spendable subset directly against this sweep's own
  portfolio-agent output before sizing any call.
- **2026-08-12 — D4 (profit-recycling gross-vs-realized-gain ambiguity)
  folded into S12, not opened as a separate item.** Same "ambiguous shared
  definition" failure class S12 exists to solve, and S12's own original
  text anticipated extending to exactly this kind of third instance.
- **2026-08-11 — S11 fixed and confirmed (two "% of 52-week range"
  definitions).** Valuation and thesis-review now both compute the true
  low-to-high percentile and agree with `position_report.py` by
  construction — spot-checked this sweep: AZN 31.9% (valuation) vs 32%
  (position_report), ABB 78.0% vs 78%. Thesis-review still separately
  reports price-÷-52w-high for a different purpose but now labels it
  distinctly, which was the other half of the original ask. The general
  failure pattern this item named ("same label, different definition")
  recurred immediately one level up, in denominator conventions — tracked
  as new item S12, not a reason to reopen S11 itself.
- **2026-08-11 — the AZN-vs-Avanza-Global cash-routing premise check
  (raised as a possible new S-item, deferred, not opened).** 2026-08-10's
  routing call rested on a checkable-but-unchecked premise ("no vetted
  candidate") that this session's Council found false on the same data
  that was available the day before. This was caught and corrected within
  one sweep by the system's own reconciliation mechanism — arguably that
  mechanism doing its job, not failing. One occurrence isn't a pattern;
  `meta` is deliberately not proposing a standing "would-buy-today
  pre-flight checklist" on a single instance. Revisit if a second,
  independent instance of a headline call resting on an unchecked-but-
  checkable premise turns up in a future sweep. **Superseded 2026-08-12:**
  a second instance did turn up (2026-08-11's own AZN.ST call, funded from
  cash that turned out not to exist) — see the 2026-08-12 entry above for
  the resolution.
- **2026-08-10 — S2 rejected (Form-4 buy/sell direction parsing), cut to
  hold the ≤10-open-S-items cap.** The item's own text already conceded
  "lower value than it looks": it's US-only, and the system's actual
  working insider signal is Finansinspektionen's Insynsregister for
  Swedish names, which already gives direction and amount today. No
  session across several sweeps has produced evidence this gap actually
  blocked a call. Revisit only if a US-name insider signal becomes
  decision-relevant to a real holding or candidate.
- **2026-08-06 — `reports/SESSION_LOG.md` lost in the 2026-08-03 merge,
  unnoticed for 3 days**: recreated this session from `OPEN_ITEMS.md`'s
  closed-item log, `data/portfolio.json`, and surviving dated memo files.
  Root cause understood (the merge commit's explicit restore list omitted
  this file). File itself is fixed; the forward-looking guard against a
  repeat is S8, closed 2026-08-18 (see above — folded into S15's stronger
  evidence base under cap pressure, not because the underlying risk is
  gone).
- **2026-08-06 — Excel import pipeline dry-run bugs found and fixed before
  the first real run**: a ticker-collision bug (multiple holdings sharing
  ticker "TBD"), a P/E sanity check that only bounded high values and
  missed an implausibly low one (Atlas Copco read 2.05), and a dedup bug
  writing literal "None" strings for blank cells were all caught in this
  session's own dry-run testing and fixed before touching real data.
  Verified in `scripts/import_excel_holdings.py`: `_match_key()` folds
  holding name into the key for "TBD" tickers, `EXCEL_PE_SANITY_RANGE`
  has both a floor and a ceiling, and `key_val()` normalizes `None` and
  empty-string consistently on both sides of the dedup comparison. A
  distinct, still-open gap found in the same pipeline (no cross-field
  ticker/name/price plausibility check) is now S9.
- **2026-08-03 — The two-branch fork**: merged. `main` and
  `claude/project-status-briefing-0528tx` had diverged since 2026-07-22 with
  ~25 commits each, invisible to each other. Everything is now on `main`;
  the JSON files stayed authoritative, the branch's capabilities came across.
  **Guard added so it cannot recur:** `scripts/check_unmerged_work.py` runs at
  the end of every sweep and fails loudly on any stranded branch, uncommitted
  change, or unpushed commit. A branching rule is now written into `CLAUDE.md`.
- **2026-08-03 — Excel as a maintenance burden**: reversed. `master.xlsx` is
  now generated from the JSON by `scripts/build_workbook.py` and read back by
  nothing. You look at it to confirm the totals add up; you never update it.
  The `Manual Data` sheet survives rebuilds.
- **2026-08-03 — Target allocation written into the files**: on your explicit
  instruction, `portfolio.json.targets` now holds equity 85 / crypto 10 /
  cash 5 / fixed income 0. Approved 2026-07-27, recorded 2026-08-03. The
  drawdown caveat (was S5, now closed 2026-08-17) is untouched by this.
- **2026-08-03 — ETH quantity**: 0.50185 ETH confirmed. The position now
  reprices from live data instead of a fixed estimate. **This produced a real
  correction:** it had been carried at ~12,500 SEK and is actually worth
  ~8,911 SEK — about 29% overstated — so every crypto-weight and total-value
  figure before today was too high. Cost basis (P1) is still open.
- **2026-08-03 — Theses for Handelsbanken A and Investor A**: recorded in your
  words, including that both were bought without comparison shopping. Both are
  now treated as rotation candidates rather than conviction holdings.
- **2026-08-03 — Excel `Stocks` data type as a live source**: investigated and
  ruled out as a *pipeline* source (needs a live Microsoft 365 Excel session
  to refresh; nothing headless can trigger it, and openpyxl does not preserve
  linked data types across a save). Confirmed empirically — the workbook
  currently contains no linked-data parts at all. Still useful as a *manual*
  gap-filler via the Manual Data sheet.
- **2026-08-06 — SUPERSEDES the above, doesn't contradict it.** The
  "nothing headless can trigger a refresh" conclusion stands — that's still
  true and unchanged. What changed: whether the CACHED values behind an
  already-refreshed live cell are reliably *readable* headlessly turned out
  to be yes, not no. A raw file download via the Google Drive connector
  (`mcp__Google_Drive__download_file_content`) plus a real
  `openpyxl(data_only=True)` parse returns clean cached fundamentals (P/E,
  sector, market cap, etc.) reliably. The earlier "no linked-data parts at
  all" finding was against a different, plainer workbook — the user's
  richer `master-5.xlsx` does carry them, and Drive's own web-preview/
  text-conversion (not the file, not openpyxl) is what had made it look
  broken in an earlier check this same day. New live path:
  `scripts/import_excel_holdings.py`, read-only, documented in CLAUDE.md's
  flow step 1a. `data/universe.json` is retired in favor of a Watchlist tab
  in the same workbook — see S1.

- **2026-08-03 — Avanza Global TER** (was the most urgent open item):
  confirmed **0.10%/yr**. The largest holding is also the cheapest; fee drag
  is a non-issue there. Portfolio-wide known drag falls to ~0.27%, inside the
  0.4% cap.
- **2026-08-03 — Full account inventory** (was two separate questions): you
  confirmed the complete list — Avanza ISK, two Handelsbanken accounts, PayPal,
  ETH wallet, one frozen SEB fund, and Revolut for everyday spending. No more
  surprise accounts. Revolut is recorded but deliberately excluded from all
  portfolio math (it's a current account, not capital).
- **2026-08-03 — The unexplained SEB fund**: identified as SEB Osteuropafond,
  unsellable because of the war in Ukraine. Cost basis 0.25 SEK, so this is
  bookkeeping, not an investment. It also withdraws an earlier wrong guess
  that its "sale proceeds" explained an ~82 SEK discrepancy — it was never sold.
- **2026-08-03 — Bitcoin certificate vs. self-custody**: decided — staying in
  the certificate (keeps the ISK shelter), switching to a cheaper one instead.
  Became P4.
- **2026-08-03 — Swedish candidate tickers**: confirmed by you; Swedbank
  (SWED-A.ST) and Kinnevik (KINV-B.ST) added to `universe.json`.
- **2026-08-03 — Tax-reserve shortfall (~130 SEK)**: closed, you'll have the
  money when the declaration is due.
- **2026-08-03 — FOMC 2026 dates**: verified against your list — the dates
  already in the file were correct. Riksbank calendar extended to full-year
  2026 including minutes, business surveys and the stability report.
- **2026-08-03 — Bitcoin certificate price feed**: COIN-XBT.ST has no working
  ticker and never will — stopped treating it as a transient outage. Now
  tracked via spot BTC from CoinGecko as a directional proxy, with your
  reported price as the real figure.
- **2026-07-28 — Avanza ISK itemization**: done, all holdings priced
  individually.
- **2026-07-28 — Handelsbanken wrapper** (the original blocking question):
  confirmed AF/fondkonto, fully exited into the ISK. This was the single
  largest structural win the system has produced.
- **2026-07-12 — Riksbank meeting dates**: supplied, now extended to full-year
  2026.
