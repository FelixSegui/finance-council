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
**Set by meta, 2026-08-17 (unchanged for a fifth consecutive sweep,
escalating):** No signal argues for prospecting this sweep — ISK cash is
confirmed 0 SEK again, and even this sweep's own headline call (trim
COIN-XBT.ST) generates and redeploys capital inside the same call rather
than adding to an idle pool. Every portfolio-tending signal from last
sweep is not just present but has hardened: `swedish-equity-review` on
ATCO-B.ST/ALFA.ST/ABB.ST is now unexecuted for a **seventh** consecutive
sweep (a hard 2026-09-03 default now attaches a real consequence —
rotation-candidate status, not just another ask); PayPal routing (P3/D1)
is a **fourth** consecutive sweep of identical unexecuted advice, now also
carrying a 2026-09-03 dated fallback; and this sweep's own headline trim,
dated for execution "today" by the 2026-08-12 sweep, was itself found
unexecuted and had to be re-issued at lower confidence. New and
higher-priority than anything named last sweep: the portfolio lens
produced this system's first-ever (illustrative, not a real backtest)
drawdown estimate against the user's stated -30% tolerance, and **both**
the current mix (~-42.3%) and the adopted 85/10/5/0 target (~-45.75%)
breach it — which makes running `backtest` against S5 the single
highest-value unexecuted item in the system right now, not a footnote.
Two governance items (D3, D4) still await the user's actual confirmation,
both on the same 2026-09-03 deadline, and D3 is now decision-relevant
rather than cosmetic (the two denominator conventions disagree on whether
the crypto trip-wire fires: 12.97% vs 11.43% on the identical figure).
None of this is a prospecting gap — the Watchlist itself is unchanged and
adequate (still 45 entries; the 12 malformed-ticker entries flagged
2026-08-11/12 remain a pending Excel-side fix, not a coverage gap, per
this session's `meta` check). Revisit at 2026-09-03: once
`swedish-equity-review` has actually run, PayPal is routed, D3/D4 are
settled, and `backtest` has actually run against the -30% tolerance, that
combination is what flips this back to balanced.

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
- **Status:** open — two weeks with no movement, three options on the table
- **Confirmed 2026-08-03:** PayPal's conversion spread is 3-4%. Planning
  figure is **4%** (your instruction: assume worst case).
- **What it costs:** ~563 SEK to convert the current 1,177.49 USD + 266.88 EUR
  through PayPal (14,079.79 SEK total). And it recurs — you receive
  ~750-1,000 EUR every ~2 months, so this is a permanent leak
  (~1,970-2,630 SEK/yr), not a one-off.
- **Still to decide:** the cheapest path out. 2026-08-11 Council's read: the
  actual blocker is a missing price (Revolut's real FX spread has never been
  measured), not a missing preference — recommends a small test transfer via
  Revolut to price it once, then route the rest by whichever option wins.
  This exact recommendation was also made 2026-08-10 and not executed —
  worth naming plainly as the second straight sweep of repeating advice with
  no action. Options remain: (A) convert inside PayPal and accept ~563 SEK
  now plus the same % forever; (B) transfer out in native currency to
  Revolut and convert there, unpriced; (C) a small test transfer via B to
  measure the real cost before committing the rest.
- **Why it matters more than the amount suggests:** this is a fee-drag problem,
  which is lever #2 in the system's priority order. Recurring forever beats
  large-and-once.
- **Stripe idea checked 2026-08-11, doesn't appear to work as a route.**
  You floated routing PayPal → Stripe → SEK on the idea that Stripe's
  conversion is cheaper than PayPal's. Stripe does support SEK and does
  have an "instant currency conversion" feature, and individuals can open
  a Stripe account without a registered business — but that conversion
  feature works on funds already sitting in a Stripe balance, which comes
  from Stripe *processing payments as a merchant*, not from an external
  transfer-in. There's no product for moving an existing PayPal balance
  into Stripe to convert it. Sources: [Instant currency conversion —
  Stripe docs](https://docs.stripe.com/instant-currency-conversion),
  [Can I use Stripe as an individual? — Picter Help
  Center](https://support.picter.com/en/articles/2488302-can-i-use-stripe-as-an-individual-not-a-company).
  Treat this path as ruled out unless you find a specific mechanism that
  contradicts this — the small Revolut test-transfer (already the live
  plan above, and you already hold a Revolut account) remains the
  simplest way to actually measure a cheaper route. It also now has a second-order effect: this balance is
  what keeps the crypto trip-wire (D3) from firing on the strictest honest
  reading — see S12.
- **2026-08-17: fourth consecutive sweep unexecuted.** Council attached a
  dated fallback: if the 50 EUR Revolut test transfer hasn't happened by
  2026-09-03, execute Option A instead (convert inside PayPal, ~563 SEK
  cost, route to ISK) rather than deliberate a fifth sweep.

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
- **ETH still has no thesis** after 12+ sweeps, on the same 2026-09-03
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
  cash. The remaining ~1,743.61 SEK (computed, not broker-confirmed) is
  recommended this sweep for a 6th AZN.ST share (2026-08-11 Council call,
  reversing 2026-08-10's routing to Avanza Global — see Closed log).
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
  against. Named as the system's own recommended next step for a **seventh
  straight sweep** (2026-08-17) and has still never run — now the single
  most-repeated unexecuted recommendation in the system, escalated
  2026-08-17 to a hard 2026-09-03 default: if not run by then, these three
  become rotation candidates ineligible for adds.
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

### S4 — Swedish CPI is returning a stale period
- **Status:** open
- `se_cpi_yoy` comes back as period 2025M12 — roughly 7 months stale — so every
  "real Swedish rate" figure is computed against old inflation. The data is
  honest (it carries its own period label) but it's old. Fix is to switch the
  SCB PxWeb table (try KPIF) in `fetch_se_cpi_yoy()`.
- **Why it matters:** the macro lens used this to call SEK cash's real yield
  positive. That conclusion rests on a stale input. **2026-08-12 note:** this
  session's Council named the same gap as a live reason for caution on a
  much larger stake than a cash-yield footnote — macro cannot confidently
  regime-grade Swedish industrials (65.2% of the individual-stock sleeve)
  while the underlying Swedish inflation input is 8 months stale, and that
  was one of two explicit reasons Call 4 stayed HOLD rather than considering
  a regime-driven rotation. Worth prioritizing now that it touches a
  majority-SEK sleeve, not just a footnote.

### S5 — Backtest the 85/10/5/0 target against the -30% drawdown tolerance
- **Status:** open — the `backtest` agent exists and has never been run
- Your stated tolerance is -30%. The adopted target has never been tested
  against it. An 85% equity + 10% crypto portfolio plausibly draws down
  more than 30% in a bad year, which would mean the target and the tolerance
  contradict each other — and you'd find out at the worst possible time.
- Pairs with P2: ideally test before formally writing the target in.
- **2026-08-11 note:** this session's scorecard again lists "drawdown-tolerance
  fit" as UNKNOWN and flags it as one of three named provisional gaps in the
  memo — no new evidence beyond that, but it's the gap that keeps recurring
  in every scorecard while remaining the one lever-3 (allocation) question
  nothing has ever actually tested. See step 5 review in this session's
  `meta` report for why this is judged "worth implementing soon."
- **2026-08-12 note:** unchanged, same scorecard gap named again this sweep.
- **2026-08-17 note — this session materially raises this item's priority,
  not just repeats the gap.** The portfolio lens produced the system's
  first-ever drawdown estimate against the target (explicitly labeled
  illustrative, not a real backtest): current mix ≈-42.3%, the adopted
  85/10/5/0 target ≈-45.75% — both breach the stated -30% tolerance. Two
  alternative targets were checked and also rejected (a 50/5/5/40 option
  reverts to a glidepath the user already overrode; an 82/6/12/0 option
  still breaches at ≈-41.4%). `SESSION_LOG.md`'s own 2026-08-17 entry names
  this "the highest-value unexecuted item in the system." Judged in this
  session's roadmap review as **particularly valuable, worth implementing
  soon** — see this session's `meta` report.

### S6 — No source for holding-company NAV discount/premium
- **Status:** open — blocks half of P5
- Investor A and Industrivärden can't be valued on P/E; the real metric is NAV
  discount/premium, and no free automated source for it has been found.
  Options: parse the quarterly report PDF (the `pdf` skill can do this if you
  supply the report), or read it off Investor's IR page manually.

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
- **2026-08-11 note:** no incident this session; judged "useful, can wait"
  in this sweep's roadmap review — see the `meta` report.
- **2026-08-12 note:** no incident this session; same judgment holds.
- **2026-08-17 note — a related but distinct incident occurred this
  session, tracked separately as S15, not folded in here.** The `journal`
  subagent itself overwrote `reports/SESSION_LOG.md` (full-file rewrite
  instead of prepend), not a git merge dropping the file — a different
  root cause (agent write behavior, not merge hygiene) even though it hits
  the same file. S8's manifest-check design (file exists, above a trivial
  size threshold) is a weak backstop for this specific failure shape (a
  single fresh entry could still clear a "trivial" threshold) — worth
  revisiting whether S8's "how" should also assert line-count
  monotonically increases, not just non-triviality, once S15 is scoped.

### S9 — Excel import script: three data-quality flags (cross-field plausibility + purchase-without-thesis + Excel-vs-confirmed-override conflicts)
- **Status:** open — new evidence this session (a real instance of gap (c)
  was caught by hand, not by the script)
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
  outranks Excel" rule, just enforced in code instead of relying on a human
  noticing every time. All three reuse the existing `flags` list already
  surfaced in `latest-summary.json` and read into the council memo —
  no new plumbing needed.

### S12 — Canonical definitions for ambiguous shared terms: recurred a third time, now spans two conventions
- **Status:** open — D3 (the original trigger) proposed-resolved 2026-08-12
  pending user confirmation, and is now decision-relevant rather than
  cosmetic; D4 folds into this item rather than opening separately
- **Why:** the 2026-08-11 sweep's crypto trip-wire check (D3) produced
  **three different "investable capital" denominators for the identical
  24,115.89 SEK of crypto**: the 2026-08-10 pinned definition (204,611.94
  SEK -> 11.79%, does not fire), the portfolio agent's proposed standing
  "Convention A" (201,895.91 SEK -> 11.94%, does not fire), and a third
  reading, "Convention C" (190,532.15 SEK -> 12.66%, **already breached**).
  This is the identical failure class S11 already fixed one level down: two
  agents computing "% of 52-week range" two different ways under one
  label. S11's fix was confirmed working the same sweep — but the same
  ambiguity pattern immediately reappeared at the denominator level, which
  is exactly what the 2026-08-11 Council memo names in its own Learning
  notes: "pin the definition in words, not the number, because the number
  goes stale and the definition is what you are actually arguing about."
- **2026-08-12 update:** Council's Call 2 proposed resolving D3 by adopting
  Convention B (investable-only: Avanza ISK + ETH wallet, 188,918.15 SEK)
  and pinning it in words in `data/cache/definitions.json` — not yet
  written, pending the user's actual confirmation (the Chairman's
  recommendation is not the same as the user deciding). **A third instance
  of the identical failure class surfaced the same sweep, D4:** does
  `investor_profile.json`'s `profit_recycling_rule` ("money I make from
  this should... go into the safer tiers") apply to the *gross proceeds*
  of a trim, or only the *realized gain*? Selling 1 unit of COIN-XBT.ST at
  2,581.34 SEK against a 2,016.67 SEK cost basis realizes a 564.67 SEK
  gain — the rest is return of capital — and the rule reads either way.
  This recurs on every future trim, not just this one. Per this item's own
  original text ("extend this pattern... only if a third instance of the
  same failure class shows up"), that bar is now met — D4 is folded into
  this item rather than becoming a new S-item.
- **2026-08-17 note — D3 is now decision-relevant, not cosmetic; the two
  conventions disagree on the actual outcome.** On the identical 24,492.89
  SEK of crypto exposure this sweep, Convention B (investable-only, still
  unconfirmed by the user) reads 12.97% and fires the 12% trip-wire; the
  full-portfolio reading reads 11.43% and does not fire. Every prior sweep
  the two conventions differed only by margin; this is the first time they
  disagree on the fired/not-fired outcome itself. Council sized this
  sweep's trim (1 unit) to be correct under both readings rather than wait
  for D3 to resolve — a workaround, not a substitute for the user's actual
  confirmation, which both D3 and D4 still need before the 2026-09-03
  deadline.
- **How:** keep this narrow — a small `definitions` dictionary, not a new
  schema or framework. Add a `definitions` object to `portfolio.json` (or,
  if `portfolio.json` should stay lean per CLAUDE.md's token-hygiene note,
  a new `data/cache/definitions.json`) naming each standing convention in
  words, e.g.:
  `"investable_capital_convention_2026-08-12": {"includes": ["avanza_isk",
  "eth_wallet"], "excludes": ["tax_reserve", "paypal", "hb_checking"],
  "value_sek": 188918.15, "pinned_date": "2026-08-12"}` for D3 (once the
  user confirms Convention B — Council's recommendation, not yet the
  user's decision), and a second entry,
  `"profit_recycling_proceeds_convention": {"applies_to": "gross_proceeds"
  | "realized_gain_only", "pinned_date": "..."}`, for D4 (Council
  recommends "gross proceeds" — option 1 in the 2026-08-12 memo — again
  pending the user's actual choice). Any agent computing either threshold
  cites the named convention instead of recomputing its own reading each
  sweep. Extend this pattern to a fourth ambiguous term only if a genuinely
  new instance of the same failure class shows up — the dictionary should
  grow one entry at a time, evidence-driven, not pre-built.

### S13 — CoinGecko crypto fetch has no retry/backoff; a single 429 kills the entire crypto price path
- **Status:** open
- **Why:** confirmed in code — `fetch_crypto()` in
  `scripts/fetch_market_data.py` makes exactly one HTTP request per call;
  any exception (including a transient HTTP 429) is caught and returned as
  `{"error": str(e)}` immediately, with no retry. This session, three
  separate attempts to fetch bitcoin — the agreed directional proxy for the
  permanently-dead COIN-XBT.ST ticker (404, known since 2026-08-03) — all
  returned HTTP 429. The only reason any recovery was attempted at all was
  three manual retries with `sleep` reconstructed ad hoc at the
  orchestration layer, which is not reusable and won't run automatically
  next time. This left the sweep's only executable trade recommendation
  (the COIN-XBT.ST trim) resting on a 4-day-old Excel price with zero live
  corroboration on either of its two price paths (own ticker 404, backup
  proxy 429×3) at once — flagged directly in this session's
  `SESSION_LOG.md` entry: "a backup that fails with the primary was never
  really a backup."
- **How:** in `scripts/fetch_market_data.py`'s `fetch_crypto()`, wrap the
  single request in a small retry loop (2-3 attempts) with short
  exponential backoff (e.g. 2s, then 5s) specifically on
  `urllib.error.HTTPError` with `e.code == 429`, before falling back to the
  existing `{"error": ...}` shape unchanged. Keep the "no data is fine,
  never estimate" contract intact — this only makes the one existing fetch
  call more resilient to a transient rate limit; it does not add a new
  data source (see this session's `meta` debate for why a second live
  provider was considered and rejected).

### S14 — journal only "reminds" the user to append valuations.csv instead of appending it itself — confirmed to have actually dropped a row
- **Status:** open
- **Why:** `journal.md` Mode 2 step 3 currently says to "remind the user"
  to append a row to `data/valuations.csv`, even though `journal` already
  has Write tool access and could append it directly. This session's own
  2026-08-17 `valuations.csv` row documents, in its own note field, that
  no row exists for 2026-08-12 "even though a council memo ran that day" —
  a confirmed, permanent gap in the performance-tracking series
  (append-only, cannot be backfilled). This is the mechanism the CSV
  itself effectively names as the cause: a manual reminder that depends on
  the user acting on it, not an automated write.
- **How:** in `journal.md`'s Mode 2, change step 3 from reminding the user
  to `journal` computing `total_value_sek` itself (sum `portfolio.json`
  holdings' market values against the snapshot used that sweep, same
  full-portfolio convention `position_report.py`/`portfolio` already use)
  and appending the row directly via Write, with an auto-generated `note`
  field in the same style as existing rows (comparability caveats,
  data-completeness flags). Keep a fallback: if `journal` can't confidently
  compute the total that sweep, it still reminds the user instead of
  guessing — same "no data is fine, don't estimate" rule that governs
  everything else in this system.

### S15 — journal overwrote SESSION_LOG.md instead of appending (first observed failure of the system's only calibration mechanism)
- **Status:** open
- **Why:** this session, the `journal` subagent's end-of-sweep write to
  `reports/SESSION_LOG.md` did not append/prepend correctly — it replaced
  the entire ~660-line append-only history (2026-08-06 through 2026-08-12)
  with only the new 2026-08-17 entry. Caught immediately via a git diff
  (656 deletions on a file CLAUDE.md defines as append-only, "the system's
  memory across sessions") and fixed by hand: full history restored from
  the prior commit, the new entry re-inserted above it in the documented
  format, committed as `1a2bef3` ("Fix: journal agent overwrote
  SESSION_LOG.md instead of prepending"). No data was permanently lost —
  git history had the prior version — but the failure was **silent**: the
  subagent's own summary reported success, with no self-detected error,
  on the one file CLAUDE.md calls "the system's only calibration
  mechanism." This is a first-time-observed failure mode, distinct from
  S8 (which guards against a *git merge* dropping a file entirely) — here
  the file existed and was written to, just with the wrong operation (full
  rewrite instead of insert-above).
- **How:** two changes, both small, in `journal.md`'s Mode 2 step 2: (1)
  make the instruction explicit that this is a targeted insert — read the
  current file, prepend the new entry above the existing content (keeping
  the format-block header and all prior entries verbatim), and write the
  concatenated result back — not phrased loosely enough ("write a new
  entry to the file") to be read as a full rewrite; (2) add a post-write
  self-check: after writing, re-read the file and confirm (a) line count
  increased versus the pre-write read, and (b) the previous top entry's
  date/headline still appears somewhere in the new content; if either
  check fails, report the failure explicitly instead of a silent success
  summary. This closes the "silent" half of the failure specifically — the
  wrong write already happened once with the agent reporting success
  regardless.

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
  dataset instead of prose. Spec sections 6, 10, 26, 28. **2026-08-12 note
  for whoever picks this up:** the Watchlist is now a healthier input than
  when this phase was written (45 entries, 12 categories, sector gaps
  filled — see the S10 closed-log entry) — worth a fresh look at whether
  wiring the funnel to it is now more tractable than it was 2026-08-09.
  **2026-08-17 caveat:** 12 of those 45 entries still carry a malformed
  ticker (space instead of exchange suffix) as of the 2026-08-13 import —
  see the 2026-08-17 addendum in the Closed log under S10. Whoever wires
  Phase 3 to the Watchlist should confirm those are fixed first, or the
  funnel will silently drop ~27% of entries on the first fetch.
- **Phase 4 — not started.** `risk_factor_exposure` risk-bucket
  classification (Global industrial cycle / Defensive healthcare /
  Financials / etc.) distinct from sector — directly targets the Volvo +
  Atlas Copco + Alfa Laval + ABB correlated-industrial-risk problem this
  system already flagged (65.2% of the stock sleeve, still ACT-rated as of
  2026-08-12). Portfolio-fit scoring for candidates ("does owning this
  improve the portfolio," not just "is it individually attractive"). Spec
  sections 11-12, 23, 33.
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
  Spec sections 21-22, 29-30, 32, 37. **2026-08-17 note:** the ordinary
  rolling-lookback form of `backtest` (no crisis-window fixed dates
  needed) is already sufficient to run S5 against the -30% tolerance —
  don't block S5 on this phase.

---

## Closed

Resolutions kept short; full history in `data/portfolio_history_archive.md`
and `reports/SESSION_LOG.md`.

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
  `SEB A` + `SWED A` (category `nordic_financials`), and `SAAB B` (category
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
  fixed, but 12 of the 45 entries (including these same four) still carry
  an unfetchable ticker format as of the most recent import.**
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
  guardrail itself is bypassed in a future sweep.
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
