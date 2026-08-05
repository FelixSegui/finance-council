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

**Emphasis:** balanced
**Set by meta, 2026-08-04 (seeded, not yet a real evidence-based call):**
mechanism just added — `meta` hasn't run a full session since. P6 (medium-
tier build) just executed with 3 unreviewed new positions (AstraZeneca,
Alfa Laval, ABB) and no `swedish-equity-review` behind them, which argues
for portfolio-tending next; but the ~1,744 SEK residual cash and an
unresolved P4 (cheaper BTC certificate) also argue for continued
prospecting. Genuinely mixed — `meta` should make the real call at the end
of the next full session, not this placeholder.

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
- **Status:** open — the merge itself is DONE, this is the follow-up
- The Excel branch is merged into `main` (2026-08-03) and nothing is lost.
  But its runtime — `run.py`, `data/sync/`, `scripts/fetchers/`,
  `scripts/funnel/` — is **merged but parked**, not wired into the live flow,
  because it assumes Excel is the source of truth and the live system no
  longer works that way.
- **Three things in there are genuinely worth having**, in priority order:
  1. The **discovery funnel** (`scripts/funnel/`) — index-sourced universe
     plus factor ranking. This is real capability for "should I invest in
     anything new", which is one of your two main goals.
  2. The **consolidated one-file sweep report** — one `sweep.md` per day
     instead of a memo plus separate coverage output. Directly serves
     slimming the system down.
  3. The **journal-before-council ordering rule** — the branch hit a real
     bug where council wrote a report with an empty reconciliation section.
     The live system has the same latent weakness.
- Full notes in `archive/agents-from-excel-branch/README.md`. Port these
  deliberately, one at a time — do not bulk-restore.

### P3 — PayPal routing (the fee is now known; the route isn't)
- **Status:** open
- **Confirmed 2026-08-03:** PayPal's conversion spread is 3-4%. Planning
  figure is **4%** (your instruction: assume worst case).
- **What it costs:** ~575 SEK to convert the current 1,177.49 USD + 266.88 EUR
  through PayPal. And it recurs — you receive ~750-1,000 EUR every ~2 months,
  so this is a permanent leak, not a one-off.
- **Still to decide:** the cheapest path out. Options worth pricing: transfer
  out in native currency to a multi-currency account (Revolut already exists
  and does FX far cheaper than PayPal) and convert there, versus converting in
  PayPal and accepting the 4%.
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
- **ETH still has no thesis** after 10+ sweeps. The blocker is genuinely you,
  not data: the system can price it but cannot invent why you hold it. One
  sentence is enough — "diversification, hold 3+ years, sell if X" is complete
  and testable.
- **INVE-A.ST keeps a separate open blocker:** its thesis is plausible but not
  properly *testable*, because the metric that matters for a holding company
  is NAV discount/premium and it has never been obtained. See S6.

### P6 — Build the medium tier (~26,400 SEK available)
- **Status:** decided — pending execution confirmation and post-purchase review
- **EXECUTED 2026-08-03/04** (user-reported): bought Volvo B (13sh @ 367.50),
  Atlas Copco B (27sh @ 181.25), AstraZeneca (4sh @ 1507), Alfa Laval
  (9sh @ 574.40), ABB (4sh @ 946.96) — 24,656.69 SEK of the 26,400.30 SEK
  cash, leaving ~1,743.61 SEK (computed, not broker-confirmed, courtage not
  accounted for). Recorded in `data/portfolio.json` holdings.
- **Not run through `swedish-equity-review` before buying** — 5 of the 10
  candidates were picked without a documented comparison, and AstraZeneca,
  Alfa Laval, and ABB have no `data/company_profiles/` entry at all (Volvo
  and Atlas Copco A do, from the 2026-07-28 pre-purchase screen — note Atlas
  Copco's existing profile is for the A share, this purchase is the B share).
- **Next step:** run `swedish-equity-review` on the 5 new positions
  retroactively — not to second-guess the trade, but so there's a real
  baseline (score, coverage, insider activity) to test the thesis against
  at the next check-in, same as exists for SHB-A.ST/INVE-A.ST/VOLV-B.ST.
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

### S1 — Verified SEK crypto-certificate tickers in `universe.json`
- **Status:** open — now directly blocking P4
- Nordic crypto ETP tickers (Virtune, Valour, XBT Provider, Coinshares) change
  and must be confirmed on Avanza rather than guessed. Until they're in
  `universe.json`, the cheaper-certificate search can't be screened
  automatically. This used to be a nice-to-have; P4 makes it load-bearing.

### S2 — Extract Form 4 buy/sell *direction*, not just filing counts
- **Status:** open
- Filing counts alone are weak signal — a CFO selling to cover taxes and a
  genuine cluster buy look identical. Requires parsing Form 4 XML from EDGAR.
- **Note:** this is US-only. Your actual insider signal comes from
  Finansinspektionen for Swedish names, which already works and already gives
  direction and amount. Lower value than it looks.

### S3 — Optional Alpha Vantage / FMP key for the earnings calendar
- **Status:** blocked (on user creating a free API key)
- Yahoo earnings dates are unreliable for Nordic tickers, and the earnings
  fetch failed outright on 2026-08-03. A free-tier key would make earnings
  timing trustworthy. Worth doing only if you care about avoiding trades
  landing next to earnings prints.

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

### S7 — Per-position performance tracking is thin
- **Status:** open — partially addressed 2026-08-03
- `scripts/position_report.py` was added 2026-08-03 to show per-position
  movement each sweep. It works, but it can only show what the data supports:
  positions with `cost_basis_per_unit` and `date_acquired` filled in get a real
  return figure, and the rest get "no data". Currently missing for the funds
  (Auto 3, Avanza Global have totals but no per-unit basis or acquisition date)
  and for ETH (see P1).
- Not worth a big fix — it improves automatically as the gaps in P1 close.

---

## Closed

Resolutions kept short; full history in `data/portfolio_history_archive.md`
and `reports/SESSION_LOG.md`.

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
