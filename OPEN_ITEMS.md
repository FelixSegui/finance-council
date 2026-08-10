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
a one-line resolution — never delete it silently.

**Status values:** `open` · `blocked (on what)` · `decided — pending execution` · `closed`

---

## This sweep's recommended emphasis

**Emphasis:** portfolio-tending
**Set by meta, 2026-08-10 (unchanged from 2026-08-06, reinforced not
flipped):** every signal this session still points at unfinished
portfolio-tending work, and nothing new argues for prospecting. ATCO-B,
ALFA, ABB and ETH remain at zero thesis a full week after the 2026-08-06
call, now carrying a hard 2026-09-03 deadline the next sweep must check
against. PayPal routing (P3/D1) has sat open a full week with three named
options on the table and no movement — a real, recurring ~4% fee leak
(lever 2) going unresolved is a stronger claim on attention than finding
new candidates. A new structural decision surfaced this session and needs
resolving before it recurs badly (D2: `portfolio.json`'s exposure-class
target and `investor_profile.json`'s risk-tier framework now give opposite
instructions for new money — see the memo and S11's neighbor discussion).
Against all that, there is no prospecting counter-signal: the one pool of
idle cash (1,743.61 SEK) is already earmarked for Monday's Avanza Global
buy, not sitting undeployed with no plan, and the Watchlist has not
changed since 2026-08-06 (no fresh Excel import ran this sweep) — nothing
new to screen it against even if `scout` were invoked. Revisit at the
2026-09-03 check-in: if the four theses are written and the retroactive
`swedish-equity-review` has run by then, that is what flips this back to
balanced.

---

## P — Portfolio items

### P1 — ETH cost basis
- **Status:** blocked (on user — needs time to dig it up)
- **Quantity is now CLOSED** (0.50185 ETH, confirmed 2026-08-03) and the
  position reprices from live data. What remains is only the cost basis.
- **Blocks:** any sale, any tax math, any return figure for the position.
  Swedish K4 requires cost basis; without it a sale can't be reported properly.
- **Not urgent** unless you intend to sell.

### P2 — Port what's worth keeping from the merged branch
- **Status:** open — two of three ported 2026-08-06, one still open
- The Excel branch is merged into `main` (2026-08-03) and nothing is lost.
  Its runtime — `run.py`, `data/sync/`, `scripts/fetchers/`,
  `scripts/funnel/` — stays **merged but parked**, not wired into the live
  flow, because it assumes Excel is the source of truth and the live system
  still doesn't work that way (Excel is a read-only *input* as of 2026-08-06,
  which is different — `portfolio.json` remains authoritative).
- **Three things were flagged as worth having, in priority order — status now:**
  1. The **discovery funnel** (`scripts/funnel/build_universe.py`,
     index-sourced universe + factor ranking) — **still open, not done by
     the 2026-08-06 Excel-input work.** That work retired `data/universe.json`
     in favor of a hand-maintained Watchlist tab, which is a narrower thing
     than automated index-sourced discovery — don't conflate the two.
  2. The **consolidated one-file sweep report** (one `sweep.md` per day
     instead of a memo plus separate coverage output) — **still open.**
  3. The **journal-before-council ordering rule** — **investigated
     2026-08-06, does NOT transplant as-is.** The archived branch's rule
     guarded against council writing an empty reconciliation section
     *inside its own report* — but the live system's `journal` writes
     reconciliation to `SESSION_LOG.md` as a separate end-of-sweep
     artifact, not a section of council's memo, so that failure mode
     doesn't exist here. First drafted as a hard stop in `council.md`,
     caught and corrected before the first real sweep ran under it.
  - Also done 2026-08-06, not originally itemized here but from the same
    archive: the **6-voice Investment Council method** (`core-council.md`'s
    investment-decision mode) and the **standing system-persona debate**
    (`core-council.md`'s system-health mode, ported into `meta.md`) — both
    restored and now run every sweep/session, not gated behind a threshold.
- Full notes in `archive/agents-from-excel-branch/README.md`. Port the
  remaining two deliberately, one at a time — do not bulk-restore.

### P3 — PayPal routing (the fee is now known; the route isn't)
- **Status:** open — one week with no movement, three options on the table
- **Confirmed 2026-08-03:** PayPal's conversion spread is 3-4%. Planning
  figure is **4%** (your instruction: assume worst case).
- **What it costs:** ~575 SEK to convert the current 1,177.49 USD + 266.88 EUR
  through PayPal. And it recurs — you receive ~750-1,000 EUR every ~2 months,
  so this is a permanent leak, not a one-off.
- **Still to decide:** the cheapest path out. 2026-08-10 Council's read: the
  actual blocker is a missing price (Revolut's real FX spread has never been
  measured), not a missing preference — recommends a small test transfer via
  Revolut to price it once, then route the rest by whichever option wins.
  Options remain: (A) convert inside PayPal and accept ~566 SEK now plus the
  same % forever; (B) transfer out in native currency to Revolut and convert
  there, unpriced; (C) a small test transfer via B to measure the real cost
  before committing the rest.
- **Why it matters more than the amount suggests:** this is a fee-drag problem,
  which is lever #2 in the system's priority order. Recurring forever beats
  large-and-once.

### P4 — Replace the Bitcoin certificate with a cheaper one
- **Status:** decided — pending research
- **Decided 2026-08-03:** you will NOT move to self-custody real bitcoin. You
  want to stay inside the ISK wrapper and cut the fee instead. (This closes
  the old certificate-vs-self-custody question, and it's the right call on
  tax mechanics alone — leaving the ISK would turn every future disposal into
  a 30% K4 event.)
- **The target:** COIN-XBT.ST costs **2.5%/yr** on ~15,240 SEK ≈ 380 SEK/yr.
  Cheaper Nordic BTC ETPs exist; a switch to ~1% would save roughly 230 SEK/yr.
- **What's needed:** verified tickers and current fees for the alternatives on
  Avanza. Tickers must not be guessed — see S1, which is the same problem.
- **Watch out:** selling inside the ISK is tax-free, so the switch itself is
  cheap, but check the spread/courtage on a thin certificate before assuming
  the fee saving survives the transaction cost.

### P5 — ETH thesis (the two stocks are now done)
- **Status:** open for ETH only
- **SHB-A.ST and INVE-A.ST are CLOSED** (2026-08-03): recorded as "good track
  record, secure/stable with upside", bought without comparing alternatives
  because there was spare cash to put to work. That candour matters and is
  recorded — it makes both **rotation candidates** rather than conviction
  holdings, which is directly relevant to the P6 medium-tier build.
- **ETH still has no thesis** after 11+ sweeps, now on the same 2026-09-03
  hard deadline as ATCO-B/ALFA/ABB (2026-08-10 Council call). Quantity is
  frozen — no adds under any condition — until either a thesis is written or
  P1 (cost basis) closes, whichever comes first. The blocker is genuinely
  you, not data: the system can price it but cannot invent why you hold it.
  One sentence is enough — "diversification, hold 3+ years, sell if X" is
  complete and testable.
- **INVE-A.ST keeps a separate open blocker:** its thesis is plausible but not
  properly *testable*, because the metric that matters for a holding company
  is NAV discount/premium and it has never been obtained. See S6.

### P6 — Build the medium tier (~26,400 SEK available)
- **Status:** decided — pending execution confirmation and post-purchase review
- **EXECUTED 2026-08-03/04** (user-reported): bought Volvo B (13sh @ 367.50),
  Atlas Copco B (27sh @ 181.25), AstraZeneca (4sh @ 1507), Alfa Laval
  (9sh @ 574.40), ABB (4sh @ 946.96) — 24,656.69 SEK of the 26,400.30 SEK
  cash, leaving ~1,743.61 SEK (computed, not broker-confirmed, courtage not
  accounted for — 2026-08-10 Council call: deploy this into Avanza Global,
  it has lost its earmark since the 2026-08-06 AZN buy executed).
- **Not run through `swedish-equity-review` before buying** — 5 of the 10
  candidates were picked without a documented comparison, and AstraZeneca,
  Alfa Laval, and ABB have no `data/company_profiles/` entry at all (Volvo
  and Atlas Copco A do, from the 2026-07-28 pre-purchase screen — note Atlas
  Copco's existing profile is for the A share, this purchase is the B share).
  AstraZeneca's thesis was written and executed 2026-08-06 (Council call D);
  ATCO-B, ALFA and ABB remain without one, now on the 2026-09-03 deadline.
- **Next step:** run `swedish-equity-review` on ATCO-B.ST, ALFA.ST and
  ABB.ST retroactively — not to second-guess the trade, but so there's a
  real baseline (score, coverage, insider activity) to test the thesis
  against. Named as the system's own recommended next step for a fourth
  straight sweep (2026-08-10) and has still never run.
- **Two flags carried forward, still relevant to what remains uninvested:**
  Spiltan Aktiefond Investmentbolag structurally overlaps your existing
  Investor A position; Swedbank Robur Technology A is a concentrated
  single-sector active fund with higher fees. Neither is disqualifying,
  both should be conscious choices if the remaining ~1,744 SEK (or future
  contributions) go toward them.

### P7 — Verify the ISK allowance threshold with Skatteverket
- **Status:** open — small, but it's an assumption load-bearing in the tax math
- All ISK headroom math assumes a ~300,000 SEK threshold and a 30% K4 rate.
  Both are assumptions the system has never verified, and ISK rules changed
  recently. Current ISK total is ~181,000 SEK, so there's comfortable headroom
  under the assumed figure — this is confirmation, not a live problem.

---

## S — System items

### S1 — Verified SEK crypto-certificate tickers in the Watchlist
- **Status:** open — now directly blocking P4
- Nordic crypto ETP tickers (Virtune, Valour, XBT Provider, Coinshares) change
  and must be confirmed on Avanza rather than guessed. **Updated 2026-08-06:**
  the destination for these is now the Watchlist tab in the user's Excel
  workbook, not `data/universe.json` (retired for this purpose — see the
  2026-08-06 closed-log entry above). Until verified tickers are added there
  and imported via `scripts/import_excel_holdings.py`, the cheaper-
  certificate search can't be screened automatically. This used to be a
  nice-to-have; P4 makes it load-bearing.

### S3 — Earnings calendar fetch failing — root cause now diagnosed, not just "blocked on a key"
- **Status:** open — no longer solely blocked on the user; a free, no-key fix is now identifiable
- **Updated 2026-08-10, new evidence:** this is the second outright failure
  of the earnings-date fetch (also failed 2026-08-03), and this session
  confirmed the mechanism: `scripts/fetch_calendar.py`'s
  `fetch_earnings_dates()` calls `yf.Ticker(t).calendar` — i.e. it still
  routes through **yfinance's own client**, which CLAUDE.md already
  documents as unreliable on this network (its curl_cffi browser-TLS
  fingerprinting gets connection-reset by Yahoo's anti-bot layer).
  `scripts/fetch_market_data.py` solved exactly this problem for equity
  fundamentals by bypassing yfinance's client entirely and talking to
  Yahoo's quoteSummary API directly via `urllib` + a cookie jar/crumb —
  documented in CLAUDE.md's yfinance note. `fetch_calendar.py` never got
  the same fix. Macro events "fetch cleanly" every week for a trivial
  reason — `load_macro_events()` only filters a local, manually-maintained
  JSON file and never touches the network — so its reliability says
  nothing about the earnings path's health.
- **How:** in `scripts/fetch_calendar.py`, replace `fetch_earnings_dates()`'s
  `yf.Ticker(t).calendar` call with the same direct-urllib +
  crumb/cookie-jar pattern already working in
  `scripts/fetch_market_data.py` (Yahoo's quoteSummary API exposes a
  `calendarEvents` module with earnings dates via the same endpoint used
  for fundamentals). This requires no new API key and reuses code that
  already works reliably on this network. The optional Alpha Vantage/FMP
  key (original S3 scope) stays open as a secondary/fallback source, not
  the primary fix — it's still blocked on the user creating a key and is
  no longer the highest-value next step here.

### S4 — Swedish CPI is returning a stale period
- **Status:** open
- `se_cpi_yoy` comes back as period 2025M12 — roughly 7 months stale — so every
  "real Swedish rate" figure is computed against old inflation. The data is
  honest (it carries its own period label) but it's old. Fix is to switch the
  SCB PxWeb table (try KPIF) in `fetch_se_cpi_yoy()`.
- **Why it matters:** the macro lens used this to call SEK cash's real yield
  positive. That conclusion rests on a stale input.

### S5 — Backtest the 85/10/5/0 target against the -30% drawdown tolerance
- **Status:** open — the `backtest` agent exists and has never been run
- Your stated tolerance is -30%. The adopted target has never been tested
  against it. An 85% equity + 10% crypto portfolio plausibly draws down
  more than 30% in a bad year, which would mean the target and the tolerance
  contradict each other — and you'd find out at the worst possible time.
- Pairs with P2: ideally test before formally writing the target in.

### S6 — No source for holding-company NAV discount/premium
- **Status:** open — blocks half of P5
- Investor A and Industrivärden can't be valued on P/E; the real metric is NAV
  discount/premium, and no free automated source for it has been found.
  Options: parse the quarterly report PDF (the `pdf` skill can do this if you
  supply the report), or read it off Investor's IR page manually.

### S7 — Per-position performance tracking: self-custody crypto is never repriced (confirmed bug, not just a gap)
- **Status:** open — a specific, concrete bug identified 2026-08-10, upgraded from the general 2026-08-03 framing
- **Why:** `scripts/position_report.py` was added 2026-08-03 to show
  per-position movement each sweep. The original framing ("thin, improves
  automatically as P1 closes") undersold what's actually wrong: this
  session confirmed the script **never reprices self-custody crypto at
  all**, independent of P1. ETH's holding has `ticker: "ethereum"` and
  `instrument_type: "spot_crypto"` — because that ticker isn't a key in
  `cur_snap["equities"]`, `main()` routes it to `manual_row()`, which only
  reads `market_value_sek` (a stale book value) and never looks at
  `cur_snap["crypto"]`, even though the crypto section (fetched fresh every
  sweep, e.g. `ethereum.price_eur`) is sitting right there in the same
  snapshot file. This carried ETH at its 2026-08-03 book value (8,911 SEK)
  in the 2026-08-10 report when the correct repriced figure was ~9,170 SEK
  (+2.9%) — caught and corrected by hand in that sweep's Council memo, not
  by the script.
- **How:** in `scripts/position_report.py`, add a branch (parallel to
  `equity_row`/`manual_row`) for holdings with `instrument_type ==
  "spot_crypto"`: look up `cur_snap["crypto"].get(ticker)` (ticker is
  already the CoinGecko id, e.g. `"ethereum"`), pull `price_eur`, and
  convert via `cur_snap["macro"]["sek_per_eur"]["value"]` — mirroring the
  existing SEK-conversion pattern already used elsewhere in this codebase
  for ETH (see `data/portfolio.json`'s eth-wallet holding notes for the
  exact formula: `quantity * price_eur * sek_per_eur`). Compute
  `since_prev` the same way using `prev_snap["crypto"]`, matching
  `equity_row`'s existing pattern. This is a narrow, single-branch fix —
  there is exactly one self-custody crypto holding today (ETH); don't
  generalize into a pluggable pricing-source framework for a problem of
  size one.
- Separately, still true and unrelated to this bug: funds (Auto 3, Avanza
  Global) have totals but no per-unit basis or acquisition date, so they
  correctly show "no data" for return figures — that part genuinely does
  improve automatically as those gaps close and doesn't need a code change.

### S8 — Guard against critical files silently dropping during a branch merge
- **Status:** open
- **Why:** `reports/SESSION_LOG.md` — the system's only calibration
  mechanism per CLAUDE.md — was dropped by the 2026-08-03 merge commit
  (`445479b`), which explicitly restored `CLAUDE.md`, `data/portfolio.json`
  and `data/investor_profile.json` but omitted this file from that list. It
  went undetected across at least two sweep-adjacent sessions (~3 days)
  until this session's `journal` run reported a read failure instead of
  quietly reconstructing from other files. `scripts/check_unmerged_work.py`
  guards against stray/unmerged branches, a different failure mode — it does
  not check that a defined set of critical files still exist after a merge
  actually lands.
- **How:** extend `scripts/check_unmerged_work.py` (or add a small companion
  check run at the same point, CLAUDE.md flow step 7) with a hardcoded
  manifest of critical files — `CLAUDE.md`, `data/portfolio.json`,
  `data/investor_profile.json`, `reports/SESSION_LOG.md`, `OPEN_ITEMS.md` —
  and verify each exists and is above a trivial size/line-count threshold
  every time the script runs. Exit non-zero and name the missing or emptied
  file if any check fails.
- **2026-08-10 note:** a *different*-shaped git incident occurred this
  session (local `main` ref 10 commits behind the actual checked-out HEAD)
  and resolved cleanly — `origin/main` already had all the commits, nothing
  was lost, no S8-style guard was even needed to catch it. Confirmed no
  update to this item's text or status is warranted; recorded here only so
  it isn't mistaken for new evidence about S8 itself.

### S9 — Excel import script: two new data-quality flags (cross-field plausibility + purchase-without-thesis)
- **Status:** open
- **Why:** two real gaps surfaced in this session's import run. (1) The
  Transactions sheet has a row pairing ticker "ethereum" with a
  certificate's name/price/quantity (`BUY, ethereum, 1 unit, 2016.67
  SEK/unit`) — a likely copy-paste artifact next to the real COIN-XBT.ST
  6th-unit purchase row. The import script only does per-field bounds
  checks (P/E sanity range, week52 range) and has no cross-field check
  (does the ticker plausibly match the row's own name/price), so it
  imported the bad row as-is into `data/transactions.csv`, where it will
  corrupt any future attempt to derive P1 (the ETH cost basis) from
  transaction history. (2) Four positions (ATCO-B, AZN, ALFA, ABB) were
  added to `portfolio.json` 2026-08-03/04 with no thesis, and nothing
  flagged it until this sweep's full Council run noticed — the same
  pattern that already happened once before with SHB-A.ST/INVE-A.ST
  (2026-08-03). This is now a recurring, worsening gap (5 positions,
  29,242 SEK, 15.4% of investable capital, ETH included) that the import
  script's existing "flags, never block" mechanism could catch
  automatically instead of relying on a full sweep to notice it.
- **How:** in `scripts/import_excel_holdings.py`: (a) in
  `process_transactions`, add a bounded plausibility check — if a row's
  `holdings_ticker` matches a known ticker in `data/company_profiles/` or
  `portfolio.json` holdings, flag if `price_per_unit` is off by a large
  multiple (e.g. >5x) from that ticker's last known price, or if the row's
  `name` shares no token with the ticker's recorded name; (b) in
  `process_core_holdings`, when a holding's `quantity` moves from
  null/0 to a positive number (a new position) and its `thesis` field is
  null or `"TBD"`, add a flag naming the ticker. Both reuse the existing
  `flags` list already surfaced in `latest-summary.json` and read into the
  council memo (section 12) — no new plumbing needed.

### S10 [prospecting] — Watchlist regression: narrower than the retired universe.json and lost sector diversifiers
- **Status:** open — no new evidence this session (no fresh Excel import ran; `scout` correctly not invoked)
- **Why:** the new Watchlist (`data/cache/watchlist.json`, 32 entries / 7
  categories, live for the first time 2026-08-06) is smaller than the
  `data/universe.json` it replaces (~43 tickers) and dropped names that
  mattered for exactly the gaps this sweep's own scorecard flagged: H&M
  (`HM-B.ST`, the only non-industrial/non-financial Nordic consumer name
  in the old universe) is gone entirely; `SEB-A.ST` and `SWED-A.ST` (bank
  alternatives to the ACT/WATCH-adjacent `SHB-A.ST`) are gone; Saab
  (`SAAB-B.ST`) is gone. Separately, `broad_index_etfs` swapped EU-UCITS-
  domiciled funds (`VWCE.DE`, `EUNL.DE`, `IS3N.DE`) for US-domiciled ones
  (`VOO`, `VTI`, `QQQ`) — US-domiciled ETFs are frequently not legally
  purchasable by EU retail investors without a PRIIPS KID, which most
  don't provide, so this category may now be screening candidates the
  user cannot actually buy on Avanza. The 2026-08-10 scorecard still rates
  equity sector concentration **ACT** (industrials 65.49%, down only via
  price drift not a structural fix) and geography **WATCH** — the same
  gaps this narrower Watchlist would help correct, and hasn't. This is a
  universe problem, not a screen problem — `scout` has not been invoked
  since the Watchlist went live, so still no screen-calibration evidence
  exists; don't conflate the two.
- **Confirmed 2026-08-10, not a defect:** `data/cache/watchlist.json` is
  deliberately gitignored (regenerated fresh each sweep from the Excel
  Watchlist tab, not persisted) and is genuinely absent between Excel
  imports — this session found it missing on disk. That's by design, not
  a new gap: `scout.md`'s own instructions and `screen_candidates.py`
  already document and implement an automatic fallback to
  `data/universe.json` when the Watchlist file doesn't exist. Verified in
  code this session. No action needed here.
- **How:** this is user-curated content (the Watchlist tab, per CLAUDE.md
  1a), not a script bug — no code change to propose. Concrete action: next
  time the Excel workbook is edited, consider re-adding a non-industrial/
  non-financial Nordic name (e.g. H&M or another consumer/healthcare
  name) for sector diversification, one bank alternative to SHB-A.ST
  (SEB-A or Swedbank) so the P5/Call-B rotation comparison has something
  real to compare against, and either swap `broad_index_etfs` back to
  EU-UCITS-domiciled tickers or confirm with Avanza that the US-domiciled
  ones are actually purchasable before `scout` screens them as real
  candidates.

### S11 — Two different "% of 52-week range" definitions in circulation, same label, different numbers
- **Status:** open
- **Why:** `scripts/position_report.py` computes the true percentile within
  the 52-week low-to-high band (`(price - low) / (high - low)`); the
  valuation and thesis-review agents compute price ÷ 52-week high and also
  call the result "% of range." This produced a real, materially different
  analytical read in the 2026-08-10 sweep: AstraZeneca read as "79.1% of
  range" (price ÷ high — sounds mid-pack) versus the true **28th
  percentile** (sounds cheap within its own year) — the second reading
  measurably strengthens AZN's case, it doesn't just phrase it differently.
  ABB similarly: "91.1%" (price ÷ high) versus the true **79th percentile**.
  Both readings appeared side-by-side in the same memo (2026-08-10, section
  1 and section 5, disagreement #5) and had to be manually reconciled by
  the Council rather than agreeing by construction. This is exactly the
  "confident structure built on stale or hallucinated numbers" risk CLAUDE.md
  names as the system's biggest single risk — except here neither number is
  wrong, they're just answering different questions under an identical label.
- **How:** standardize on the true low-to-high percentile — it's the more
  informative number (distinguishes "near its high because it never fell"
  from "near its high after round-tripping the whole range") and
  `position_report.py` already computes it correctly. Concrete steps: (1)
  in `valuation.md` and `thesis-review.md`, change the instruction to
  compute `(price - 52w_low) / (52w_high - 52w_low)` instead of `price /
  52w_high`, using the same field names already present in the snapshot
  (`52w_low`, `52w_high`); (2) if any agent still wants the price-÷-high
  ratio for a different purpose, it must use a distinct label (e.g. "% of
  52-week high") so it's never confused with the percentile again; (3) spot
  check the next sweep's memo for AZN and ABB to confirm the two numbers
  now agree.

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
  dataset instead of prose. Spec sections 6, 10, 26, 28.
- **Phase 4 — not started.** `risk_factor_exposure` risk-bucket
  classification (Global industrial cycle / Defensive healthcare /
  Financials / etc.) distinct from sector — directly targets the Volvo +
  Atlas Copco + Alfa Laval + ABB correlated-industrial-risk problem this
  system already flagged (69% of the stock sleeve). Portfolio-fit scoring
  for candidates ("does owning this improve the portfolio," not just "is
  it individually attractive"). Spec sections 11-12, 23, 33.
- **Phase 5 — not started.** Macro Regime Engine expansion: new fetchers
  for BOJ policy rate, USD/JPY, credit spreads, PMI, unemployment/GDP,
  and a computed real-yield field — confirmed genuinely missing from
  `scripts/fetchers/fetch_macro.py` (2026-08-09 exploration). Multi-
  dimension regime classification (Liquidity/Inflation/Growth/Credit/
  Market risk/Currency-funding), `macro_fit`/`macro_sensitivity` per
  candidate, dynamic BUY thresholds (regime-dependent, configurable,
  never auto-selling on a regime shift alone). Spec sections 13-17, 31,
  34 (crypto-specific macro monitoring).
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
  Spec sections 21-22, 29-30, 32, 37.

---

## Closed

Resolutions kept short; full history in `data/portfolio_history_archive.md`
and `reports/SESSION_LOG.md`.

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
  repeat is S8, still open.
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
  drawdown caveat (S5) is untouched by this and still open.
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
