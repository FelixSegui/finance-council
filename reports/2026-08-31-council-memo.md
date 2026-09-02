# Council memo — 2026-08-31

*Structured synthesis of this system's own analyst agents. Not advice from a
licensed advisor. Every number below traces to a file fetched or maintained in
this repo this session; nothing is estimated from memory. Where a voice reasons
qualitatively (moat, management, why a price fell), it says so.*

Snapshot: `data/cache/snapshots/20260831T060914.json` · Candidates:
`data/screens/20260831T061021-candidates.csv` · Scout:
`data/screens/20260831T061021-scout.json` · Calendar:
`data/cache/calendar/20260831-events.json` · Backtest:
`data/cache/backtests/20260831T061737.json`

**Two stale premises in the scheduled prompt that launched this sweep, not
followed** (same handling as the 2026-08-17 precedent): (1) it asked the memo to
open with the Handelsbanken wrapper question — resolved 2026-07-07, all capital
in the ISK since 2026-08-03, no open P-item; (2) it asserted
`reference_targets` are null — they hold an adopted 85/10/5/0 written
2026-08-03. Normal memo structure follows. A third premise in the same prompt is
also wrong and is dealt with in §4: it said this sweep's backtest was the first
ever run, but the repo's own closed log and the 2026-08-24 memo record one on
2026-08-17.

**POST-SWEEP CORRECTION, added 2026-09-02 — do not act on this memo's AZN.ST
sizing or ISK-cash figure as written.** The user reported directly on
2026-09-02 that two purchases had already been made on 2026-08-25, six days
before this sweep ran, but never entered into `data/portfolio.json`: 3 more
AZN.ST shares (4,753.35 SEK) and 4 units of Xetra-Gold ETC (5,689.22 SEK,
closing OPEN_ITEMS.md P7). This sweep's Council therefore reasoned from a
stale 5-share AZN.ST position and an 11,288 SEK ISK-cash figure that was
actually already down to ~845 SEK by the time this memo was written. Below:
AZN.ST holds 5 shares and the ISK cash figure is 11,288 SEK — both numbers
are superseded. Current state (8 AZN.ST shares, ISK cash ~845 SEK, gold
position added, targets updated to 80/10/5/0/5) is in `data/portfolio.json`
and `OPEN_ITEMS.md`'s P7 entry. The AZN.ST BUY thesis itself is not
contradicted by this — if anything the 2026-09-02 price (1,555.50, down from
this memo's 1,571.50) is marginally cheaper — but any further sizing decision
needs the real cash figure, not this memo's.

---

## 1. Position report

## 2026-08-31 sweep
Snapshot: `20260831T060914.json` · previous: `20260824T060950.json`

| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (stock) | 147.20 | +0.8% | +13.9% | 92% | 147.20 | fetched |
| Investor A (stock) | 408.90 | +0.9% | +40.9% | 93% | 2,044.50 | fetched |
| Volvo B | 346.40 | +1.9% | -5.7% | 78% | 4,503.20 | fetched |
| Atlas Copco B | 181.35 | +3.3% | +0.1% | 93% | 4,896.45 | fetched |
| AstraZeneca | 1,571.50 | +0.7% | +4.1% | 37% | 7,857.50 | fetched |
| Alfa Laval | 576.60 | +5.1% | +0.4% | 91% | 5,189.40 | fetched |
| ABB | 938.40 | -0.6% | -0.9% | 73% | 3,753.60 | fetched |
| Avanza Auto 3 (fund) | no data | no data | +65.2% | - | 16,191.00 | book value |
| Avanza Global (fund) | no data | no data | +0.0% | - | 119,999.00 | book value |
| Valour Bitcoin Zero SEK (certificate) | 47.29 EUR (KNOWN BAD — Yahoo feed doesn't reconcile, S1) | +0.0% | -22.9% | - | 7,093.80 (snapshot calc; portfolio-lens instead used broker-confirmed 11,031 SEK — use the broker figure, not the snapshot figure, per the standing S1 note) | fetched |
| ETH (self-custody wallet) | 23,231.88 | +0.7% | no data | - | 11,658.92 | fetched |

Crypto context: ethereum 2,101.14 EUR, 7d -0.1%, 30d +30.4%, vs ATH -50.3%.
Crypto Fear&Greed flipped from 29 ("Fear", 2026-08-11 sweep) to 62 ("Greed")
this snapshot — material regime shift.

**Reading it.** A broad up-week for the Swedish sleeve — Alfa Laval +5.1%, Atlas
Copco +3.3%, Volvo +1.9% — which pushes ATCO-B and ALFA to 93% and 91% of their
52-week ranges while both remain `WEAKENING` on PEG 2.38 and 2.96. That is the
week's most uncomfortable fact: the two names the system says are expensive got
more expensive, and nothing about the businesses changed. ABB was the only
decliner (-0.6%), which marginally improves the economics of the standing sell.
**No move contradicts a thesis.** AstraZeneca (+0.7%, still at 37% of range) is
the one holding whose price position still matches its thesis's own claim, and
the delay on last sweep's BUY cost 33 SEK on three shares this week — small
weekly, but this is the fourth consecutive sweep it has been the top call.
Index funds: no NAV feed, buy-and-hold by design, no action. The Valour
certificate's snapshot price remains known-bad (S1) — the broker figure of
11,031 SEK is the one used everywhere in this memo.

---

## 2. Scout health

```
Universe:                624
From cache:                0
Newly fetched:           624
Fetch failed:              0
Fetched:                 624
Ranked:                  614
Candidates:               71   (holdings 8, watchlist 30, new 33)
Focus:                    22
Share classes collapsed:   6
Screened:                 71
Passed:                   38
Missing:                  16
Failed:                   17
Suspect values:            9
Status:                VALID
```

**Reading it.** Status VALID, zero fetch failures, zero diagnostics. The funnel
is working and it is genuinely discovering: **33 of 71 candidates are `new`** —
neither held nor previously watchlisted — and 11 of those sit in the 22-name
focus set. Three names entered the candidate set for the first time this run
(**MU** at rank 4, **UHS** 31, **ZTS** 42) and three left it (PLTR, MEKO.ST,
TEL2-B.ST). This is not a sweep that only looked at what is already owned.

Two health caveats to carry into §3 rather than bury:

- **MU's arrival at rank 4 is unexplained by the files.** It is absent from the
  2026-08-25 run entirely, and `fetch_failed` is 0 on both runs, so I cannot
  tell from the data whether it was previously missing from the universe or
  silently unfetched. Flagged for `meta`, not resolved here.
- **Nine suspect values were withheld from lens scoring and shown flagged**
  (working as designed, S24): SHB-A `peg=20.28`, INDU-C `revenue_growth=1198%`,
  **SNDK `revenue_growth=372%`**, **MU `revenue_growth=346%`**, ABB
  `price_to_book=108`, ASML `price_to_book=1423` *and* `roic=4.02`, KINV-B
  `price_to_sales=-2.21`, CMCSA `peg=142.98`, FANG `peg=20.69`. Two of those
  belong to the funnel's #2 and #4 ranked names. That matters and §3 #5 deals
  with it directly.

---

## 3. Top opportunities

Seven independent voices ran over the full 71-name candidate set — holdings,
watchlist and new alike — before any of them saw another's conclusions. The
Chairman's synthesis follows. Portfolio fit is applied *after* merit, never
before.

### Chairman's Top 5

```
#1 OPPORTUNITY: AZN.ST — AstraZeneca
CATEGORY: holding (5 sh, 7,857.50 SEK, 3.51% of total)
RANK HISTORY: rank 60 this run, 59 on 2026-08-25 (mechanical rank tracking
        began 2026-08-25 — only two observations exist). Council-level: this is
        the 4th consecutive sweep it has been the top call.
VOICES IN FAVOR: Defensive (8: beta 0.211 is the lowest number in the entire
        candidate set and this book has no other ballast); Copycat (7: CEO
        Soriot and CFO Sarin both still accumulating, latest 19/08/2026, no
        disposals of substance — two officers independently, repeatedly, which
        is the higher-quality pattern); Macro (7: the only held name on the
        right side of DXY 118 — a USD/EUR-revenue business held in SEK gets a
        translation tailwind from the exact thing hurting everything else)
VOICES AGAINST / CAUTIOUS: Growth (6.4% ttm revenue growth is near the bottom
        of anything picked this sweep — this is not a compounder);
        Valuation calls it Cheap but on PEG 1.41, which is 2.2x NVDA's 0.63
        and 1.5x VICI's forward earnings yield
STRONGEST CASE FOR: Defensive — every other equity in the book sits at 73-93%
        of its 52-week range; AZN sits at 37%. A portfolio whose scorecard reads
        ACT on sector, ACT on geography and 100% large-cap does not need another
        way to win in an up-tape. It needs something that holds in a down-tape,
        and there is exactly one candidate for that job inside the book.
STRONGEST CASE AGAINST: Growth — you are buying the fourth-cheapest name on
        PEG in a set that contains NVDA at 0.63 and META at 0.85. That is
        paying for safety, and it should be a conscious purchase, not a default.
KEY DISAGREEMENT: Defensive vs Growth on whether low beta is an asset or a
        cost. Not reconciled: both are right about different questions. The
        Chairman sides with Defensive because portfolio's own scorecard rates
        three concentration dimensions ACT and none of them get better by
        buying growth.
DATA GAPS: no `forward_pe` for AZN.ST — status MISSING on exactly that field,
        for the fourth sweep running, so the single cheapest cross-check used
        everywhere else in this memo (forward vs trailing multiple) cannot be
        run on the name being bought. Discount confidence one notch, no more:
        PEG 1.41, four straight rising fiscal-year revenues (44.4 → 45.8 →
        54.1 → 58.7B), 23.5% operating margin and the insider record all point
        one way. This is also a live instance of S21's Nordic coverage
        asymmetry.
CHAIRMAN CONVICTION: 8
WHAT WOULD CHANGE THIS: a fetched forward P/E above ~28, or the first insider
        disposal by Soriot or Sarin.
PORTFOLIO FIT: portfolio rates Healthcare 27.7% of the stock sleeve against
        Industrials 64.6% (ACT) and Sweden 59.1% (ACT); AZN is UK-domiciled,
        so this add moves both ACT rows the right way. Capital verified against
        *this sweep's* portfolio output §7: ISK idle cash 11,288 SEK,
        broker-confirmed 2026-08-23 — not carried from a prior memo. 3 shares
        at 1,571.50 = 4,714.50 SEK leaves 6,573.50. Zero tax event (ISK).
        Post-trade AZN is 12,572 SEK = 5.61% of total — inside the 15% cap and
        inside the 3-8% "normal" band.
FINAL CALL: BUY — 3 shares at ~1,571.50 = ~4,714.50 SEK from ISK cash
HORIZON: Long
```

```
#2 OPPORTUNITY: ABB.ST — ABB
CATEGORY: holding (4 sh, 3,753.60 SEK, 1.68% of total)
RANK HISTORY: rank 64 this run, 64 on 2026-08-25. Screen status FAIL both runs
        (forward_pe 35.95 > 30.0). Second consecutive sweep as a SELL call.
VOICES IN FAVOR (of holding): Fundamental (ROE 32.6, ROIC 20.6, 14.2% ttm
        revenue growth — this is a good business, not a distressed one, and
        selling it to fix a concentration number has a real cost)
VOICES AGAINST / CAUTIOUS: Valuation (7: trailing P/E 36.97 with forward P/E
        35.95 — the market itself is not pricing a re-rating despite 14.2%
        growth; PEG 2.63, the richest of the three held industrials); Copycat
        (5: the only holding with a net insider-*selling* record — Terwiesch's
        13/08/2026 disposal of 20,000 sh @ CHF 83.46 on top of the earlier
        cluster, against ALFA's 10/10 buys and AZN's continuing accumulation);
        Macro (5: a Nordic-listed industrial into a +1.55% real SEK policy
        rate); Defensive (5: beta 1.011 and 14.1% net margin, thickening an
        ACT-rated industrials cluster)
STRONGEST CASE FOR (holding): Fundamental — 32.6% ROE is top-decile in this
        71-name set. "Expensive good company" is not the same as "bad holding,"
        and this sale is a relative-merit rotation, not a rescue.
STRONGEST CASE AGAINST: Valuation — a forward multiple that has now sat flat
        against trailing for four consecutive sweeps while revenue grows 14.2%
        is the market pricing margin compression. Combined with the thinnest
        FCF conversion of the three P6 industrials (4.4% FCF margin) that is
        one coherent story, not two separate complaints.
KEY DISAGREEMENT: Fundamental vs Valuation on whether business quality can
        outrun a flat forward multiple. Named, not averaged: Fundamental is
        correct that ABB is the better *company* than Volvo or Alfa Laval;
        Valuation is correct that it is the worse *investment* at this price.
        The Chairman takes Valuation because the break condition was written
        against exactly this and has now been satisfiable for four sweeps.
DATA GAPS: ABB's raw P/B 108.13 is a confirmed USD/SEK currency artifact
        (suspect-flagged this run; FX-corrected ~11.7x per
        `data/company_profiles/ABB.ST.json`, which is dated 2026-08-17 and
        stale). No EV/EBITDA exists anywhere in this system — the leverage read
        is approximated from net-debt/EBITDA 0.46, which is genuinely low and
        is the strongest single number in ABB's defence.
CHAIRMAN CONVICTION: 7
WHAT WOULD CHANGE THIS: ABB's 2026-10-20 report converting the 14.2% revenue
        growth into earnings. If it does, the flat forward P/E was an estimate
        error and this sale is wrong.
PORTFOLIO FIT: portfolio rates Industrials 64.6% of the measurable stock sleeve
        (ACT, over the 45% line) and Switzerland 13.2%. Computed from
        portfolio's own per-name values plus this memo's trades: post-trade
        Industrials falls to ~44.4% of the sleeve — under the ACT line for the
        first time — and Sweden falls 59.1% → ~50.6% (still ACT, but moving).
        Wrapper: ISK, no capital-gains event. Position is -0.9% vs cost, so
        there is **no realized gain** and `profit_recycling_rule` (gains from
        medium/high tiers flow to the secure tier) does not bite — redeploying
        into another medium-tier equity is compliant, not an override.
FINAL CALL: SELL — all 4 shares, ~3,753.60 SEK proceeds
HORIZON: Medium
```

```
#3 OPPORTUNITY: VICI — Vici Properties
CATEGORY: new candidate (discovered by the funnel; not held, not previously
        watchlisted)
RANK HISTORY: rank 8 this run, 8 on 2026-08-25 — two of two runs in the top
        ten, best `z_contrarian` in the entire set both times (1.925 / 1.857)
VOICES IN FAVOR: Valuation (8: forward P/E 8.65, 6.98% dividend yield, 70.2%
        operating margin, and it sits at 0.0% of its 52-week range — the
        literal bottom); Contrarian (7: the operating numbers show no
        deterioration at all — 5.7% ttm revenue growth, 15.5% 3y CAGR, 67.5%
        net margin — so the de-rating is about the discount rate, not the
        tenant); Defensive (7: beta 0.687 on contracted triple-net rent, and
        it is one of only two names in the focus set that would add anything
        to the downside book)
VOICES AGAINST / CAUTIOUS: Macro (an explicit downgrade, stated plainly rather
        than buried: a levered REIT into a Fed that is barely restrictive
        (real rate +0.09%) and not yet easing is the profile this regime
        punishes, and buying a USD asset with kronor at DXY 118.06 is an
        unpaid currency bet — the same objection this voice raised against
        GOOGL on 2026-08-18 and META on 2026-08-24, applied consistently);
        Fundamental (ROIC 4.8 and ROE 9.8 are weak in absolute terms — this is
        a spread business, not a compounder, and the quality lens will not
        rank it); Copycat (no data — see DATA GAPS)
STRONGEST CASE FOR: Contrarian — a 6.98% yield and a forward P/E of 8.65 on a
        business with 70% operating margins and no revenue deterioration is a
        rate-driven de-rating, and the position at the exact bottom of the
        52-week range means you are being paid the full width of that
        pessimism. This is the specific "why the pessimism looks wrong" the
        voice is required to produce, not "it's cheap and unpopular."
STRONGEST CASE AGAINST: Macro — net-debt/EBITDA 4.82 means the thing that
        de-rated it can keep de-rating it, and this system fetches no credit
        spreads and no commodity data, so the input that would tell you
        whether refinancing risk is widening does not exist here at all.
KEY DISAGREEMENT: Valuation and Defensive read leverage of 4.82x as normal and
        already priced for a triple-net REIT; Macro reads it as the mechanism
        by which the downside becomes non-linear if rates stay put. Unresolved.
        The Chairman sizes for that: a starter tranche, not a full position.
DATA GAPS: three, and they compound. (1) **No EV/EBITDA or EV/EBIT anywhere in
        this system** — for a REIT that is the metric that matters most, and
        net-debt/EBITDA is a crude substitute; I am approximating and saying
        so. (2) **No FFO/AFFO** — REIT earnings are conventionally measured on
        funds from operations, and the P/E used above is the wrong denominator
        by construction. (3) **Zero insider data**: SEC EDGAR `--insiders` ran
        against the 8 holding tickers only, all non-US, so it returned nothing,
        and no US candidate was submitted at all. The Copycat voice has no read
        on this name. Institutional/13F is not fetched by any script (S20).
        Together these are worth a full conviction notch.
CHAIRMAN CONVICTION: 6
WHAT WOULD CHANGE THIS: an FFO figure and an EV/EBITDA. With those two numbers
        this is either a clear buy or a clear pass; without them it is a
        defensible starter position and nothing more.
PORTFOLIO FIT: portfolio's own candidate line reads "Diversifies (0% Real
        Estate currently, anywhere)", diversifies country (0% US in the stock
        sleeve), diversifies currency (sleeve is all-SEK), does not diversify
        market cap. It is the only Top-5 buy that hits three of four fit
        dimensions. **Tax friction the portfolio lens did not price, and it is
        material:** US dividend withholding is deducted at source, and because
        the ISK sits below the 300,000 SEK allowance (headroom 113,099 SEK),
        there is no Swedish ISK tax to credit it against — so on this account a
        6.98% gross yield is closer to ~5.9% net and the withholding is not
        recoverable. Verify with Skatteverket/Avanza before acting; per
        portfolio's standing tax caveat this memo is not tax advice. Capital:
        funded entirely by #2's ABB proceeds (3,753.60) plus #5's SHB-A share
        (147.20) = 3,900.80 SEK, of which ~3,657.90 buys 15 shares at 25.77 USD
        (sek_per_usd 9.4632, snapshot 2026-08-21). No new money required.
        Post-trade 1.63% of total — a starter, deliberately below the 3-8%
        band.
FINAL CALL: BUY — 15 shares at ~25.77 USD ≈ 3,658 SEK, funded by the ABB and
        SHB-A sales. Starter tranche; do not size up before an FFO figure
        exists.
HORIZON: Medium
```

```
#4 OPPORTUNITY: APP — AppLovin
CATEGORY: new candidate (discovered by the funnel) — the funnel's #1 name
RANK HISTORY: rank 1 this run, rank 1 on 2026-08-25. Highest `z_quality` in the
        set (2.560) on both runs. Screen status PASS.
VOICES IN FAVOR: Fundamental (7: 77.7% operating margin, 64.6% net margin,
        ROIC 65.5, ROE 203.7 — and the D/E of 111 that looks alarming is a
        book-equity artifact, because net-debt/EBITDA is 0.09, i.e. essentially
        no net leverage); Contrarian (7: the price sits at 3% of its 52-week
        range while the *forward* multiple, 14.86, is well below trailing
        24.44 — consensus earnings estimates are still rising while the price
        is at the floor, and price and estimates disagreeing that violently is
        the entire brief of this voice); Growth (7: 52.8% ttm revenue growth on
        a 24.8% three-year CAGR — accelerating, not decaying); Valuation (6:
        PEG 0.88)
VOICES AGAINST / CAUTIOUS: Defensive (**this is the memo's strongest single
        objection**: beta 2.529 is the highest in the entire 71-name set, and
        it is at that beta *at the moment its price is telling you something is
        wrong*. A name at 3% of range with a 2.5 beta does not have a
        symmetric distribution); Macro (2.5-beta USD growth asset at DXY 118);
        Copycat (no data — non-US insider fetch never ran for this ticker)
STRONGEST CASE FOR: Contrarian — this business is not deteriorating on any
        fetched number. Every operating metric is elite and the forward
        multiple is falling. That combination at the bottom of a 52-week range
        appears exactly once in this candidate set.
STRONGEST CASE AGAINST: Defensive, and it is decisive — **a stock with 77.7%
        operating margins and 52.8% revenue growth does not trade at the bottom
        of its 52-week range for no reason.** The market is pricing a
        discontinuity. This system fetches no news, no regulatory filings, no
        short interest and no litigation data. The single most decision-relevant
        fact about this name is the one thing it cannot see.
KEY DISAGREEMENT: Contrarian says the fundamentals disprove the pessimism;
        Defensive says the pessimism is information the fundamentals have not
        caught up to yet. **This is not resolvable with the data in this repo,
        and pretending otherwise would be exactly the confident-structure-on-
        thin-evidence failure this system exists to prevent.** No averaging: the
        Council's #1-ranked mechanical name does not become a buy because it
        ranked first.
DATA GAPS: no news/regulatory/short-interest feed of any kind; no insider data
        (US EDGAR not run for candidates); no institutional ownership (S20). On
        a name whose whole case turns on *why* the price fell, that is
        disqualifying for a buy but not for a watch.
CHAIRMAN CONVICTION: 5 (on the watch, not on a purchase)
WHAT WOULD CHANGE THIS: one of two things, and either is enough — the next
        reported quarter showing revenue growth and margins intact (which would
        confirm the de-rating is multiple compression, not deterioration), or
        the user relaying what the market actually reacted to. Absent both,
        this stays a watch however well it ranks.
PORTFOLIO FIT: not reached — the opportunity does not clear its own merit bar,
        so portfolio fit is moot. For the record, portfolio's line reads
        Communication Services / US / large-cap: diversifies sector, country
        and currency, does not diversify market cap.
FINAL CALL: HOLD-WATCH
HORIZON: Medium
```

```
#5 OPPORTUNITY: MU — Micron Technology (covering SNDK — Sandisk)
CATEGORY: new candidates (both discovered by the funnel; MU appears for the
        first time this run)
RANK HISTORY: MU rank 4 this run, absent from the 2026-08-25 candidate set
        entirely. SNDK rank 2 this run, rank 2 on 2026-08-25.
VOICES IN FAVOR: Fundamental notes both carry elite headline quality — MU ROIC
        53.5 / operating margin 80.4 / net margin 55.9; SNDK ROIC 80.1 /
        operating margin 78.5 / net margin 56.5 — and both PASS the screen;
        Valuation reads both as Cheap on forward multiples (MU 6.02, SNDK 5.61
        against trailing 21.10 and 20.12)
VOICES AGAINST / CAUTIOUS: Growth **declines both explicitly**, and this is the
        finding of the sweep: their headline revenue growth figures (MU 345.7%,
        SNDK 371.6%) are `suspect`-flagged and were **withheld from lens
        scoring by scout itself**. The growth case for the funnel's #2 and #4
        names rests on a number the system refuses to use. Defensive adds that
        **SNDK has no beta value at all** — the field is empty — yet it scored
        `z_defensive` 1.258, a defensive rank computed without the primary
        defensive input; and MU's beta is 2.213. Fundamental adds the second
        half: 78-80% operating margins in memory semiconductors are what the
        *peak* of a memory cycle looks like, not a durable moat — this is
        qualitative reasoning, not a fetched figure, and it is stated as such.
STRONGEST CASE FOR: Valuation — a forward P/E of 6.02 (MU) against trailing
        21.10 means the market expects earnings to more than triple, and in a
        genuine memory upcycle that has happened before.
STRONGEST CASE AGAINST: Growth — a forward multiple that low on a cyclical is
        not "cheap," it is the market pricing peak earnings. The ratio you
        would use to tell those two readings apart is PEG, and MU's PEG of
        0.14 is computed off the same suspect growth figure. **There is no
        uncontaminated way to test the bull case with this system's data.**
KEY DISAGREEMENT: Valuation vs Growth, and it is genuinely unresolved — but it
        is unresolved *because of a data defect*, not because the analysis is
        incomplete. That is a different and more honest conclusion than
        "mixed signals."
DATA GAPS: (1) the suspect growth figures above; (2) portfolio flags MU's
        market cap (~1,054B USD) as anomalous relative to Micron's real-world
        scale — it is internally consistent with price × implied share count,
        so it is not obviously wrong, but it is unverified and the market-cap
        tier call rests on it; (3) no multi-year FCF series exists for any
        name (Yahoo's legacy module exposes `netIncome` only), so mid-cycle
        normalisation cannot be attempted; (4) no insider data (US EDGAR not
        run on candidates); (5) MU's unexplained absence from the previous run.
CHAIRMAN CONVICTION: 3
WHAT WOULD CHANGE THIS: a clean revenue figure. That is all. A single verified
        trailing-twelve-month revenue number for each would either make these
        two the most interesting names in the set or dismiss them, and this is
        exactly what S24's proposed `entity_type` work and a plausibility
        repair would deliver.
PORTFOLIO FIT: not reached. For the record both diversify sector, country and
        currency and neither diversifies market cap.
FINAL CALL: NO ACTION — and this is the correct output, not a failure to
        decide. The two highest-quality-scoring discoveries in the sweep are
        refused because their headline evidence is flagged bad by the system's
        own checks.
HORIZON: n/a
```

### Other SELL recommendations on current holdings

The direct answer to "should I sell anything," every sweep.

- **SHB-A.ST — SELL the single share, alongside the ABB order.** Growth's flag:
  revenue -3.8% YoY and **forward P/E 12.99 above trailing 12.46** — consensus
  expects earnings to fall — with the price at 92% of its 52-week range and
  consensus "underperform." *And the strongest counter-argument in the entire
  sweep sits on the other side of it:* **Copycat rates SHB-A a BUY at conviction
  7** on Chairman Pär Boman's 10 Finansinspektionen filings dated 26/08/2026,
  ~1,850,000 shares at ~146 SEK ≈ 270M SEK — the single largest insider
  transaction anywhere in the fetched record, at the current market price, in a
  name the market rates underperform. **Why the Chairman still says sell, and
  the caveat that decides it:** FI filings cover the notifying person *and
  closely-associated legal persons*, and Boman also chairs Industrivärden —
  Handelsbanken's largest owner, and itself candidate rank 9 in this very set.
  The fetched data does not distinguish a personal open-market purchase from a
  related-party transaction, and those are completely different signals. A 147.20
  SEK position — 0.07% of the portfolio — cannot express an insider thesis in
  either direction. If you want to act on Boman, the honest expression is a real
  position, and that requires knowing which kind of filing this is first.
  Selling one share alongside an order you are placing anyway costs ~1 SEK in
  courtage and removes a rounding error. **Action: sell with the ABB order.**
- **VOLV-B.ST — SELL flagged by two voices, overruled on process.** Fundamental
  (7.6% net margin, ROIC 9.7 — the weakest composite quality in the held book)
  and Defensive (D/E 147.3 and net-debt/EBITDA 3.8, the highest leverage of any
  operating company in the set, on the thinnest margin). Against that:
  thesis-review has it `TOO_EARLY` at ~4 weeks into a written 3-month test
  window, ttm revenue growth turned positive (+2.7%) against the -13%/2yr decline
  cited at purchase, forward P/E 13.99 vs trailing 19.87, and it is the only
  holding that PASSES the screen. **HOLD.** Abandoning a thesis one third of the
  way through its own stated window on no new company data is the exact
  undisciplined behaviour a written break condition exists to prevent. Test
  window runs to ~2026-11-03; the 2026-10-23 report is the real test.
- **INVE-A.ST — HOLD, and for the third consecutive sweep the reason is missing
  data, not confidence.** Contrarian flagged it again: 93% of its 52-week range,
  the "upside" cited at purchase captured, and a trailing P/E of 4.86 that is a
  holding-company accounting artifact rather than a cheapness signal. Copycat
  reads it mildly positive (acquisitions only, zero disposals all year). It stays
  a hold only because NAV discount/premium — the one metric that would settle it
  — has never been obtained (S6). **This is open decision D-b and it is now
  costing a voice's attention every single sweep.**
- **ATCO-B.ST, ALFA.ST — HOLD, no adds.** Both `WEAKENING`, both got *more*
  expensive this week (+3.3% and +5.1%, now at 93% and 91% of range), PEG 2.38
  and 2.96. Contrarian and Valuation both flagged ATCO-B as sell-worthy;
  neither argued it ahead of ABB. ALFA keeps the strongest single positive leg
  in the book — 10/10 insider buys, zero disposals, unbroken this pull — though
  the latest filing is still 24/04/2026 and is now four months stale, which is
  why Copycat rates it 6 and not 8.
- **BTC0E.AS and ETH — HOLD, explicit no-add, no trim.** Crypto is 10.13% vs a
  10.0% target: +0.13pp is not a trigger in either direction. Macro's read is
  binding on the add question: Fear&Greed 29 → 62 alongside a +30.4% 30-day ETH
  move against a dollar index at 118.06 is froth, not confirmation, and a Greed
  reading is not a contrarian entry. Adding to the ETH wallet remains separately
  blocked by **P1** (no cost basis; every disposal including a token swap is a
  K4 event). No BTC price at all this snapshot — the crypto block carries
  ethereum only — so no cross-check on the Valour certificate exists this sweep.

### Names pulled back in from outside the focus set, and what happened to them

Focus narrows where depth goes; it excludes nothing. Four names were argued
explicitly:

- **ZTS (Zoetis, rank 42, screen FAIL)** — Contrarian's best find, conviction 6.
  The machine failed it on `debt_to_equity=293.996`, but net-debt/EBITDA is 1.86,
  which is modest: the D/E is a buyback-shrunken-book-equity artifact, the same
  one that inflates APP (111) and MA (440). At 5% of its 52-week range, P/E
  12.62 falling to 11.84 forward, ROE 64.9, 40.7% operating margin and beta
  0.73, **this is a case where the screen's penalty is not deserved.** Not a
  Top-5 slot because no second voice independently reached it and no insider or
  ownership data exists — but it is the name most likely to be next sweep's
  argument, and it is recorded as a Contrarian BUY.
- **META (rank 50)** — Growth's third pick, conviction 6. 28.0% revenue growth,
  forward P/E 16.53 below trailing 21.79, PEG 0.85, at 19% of its 52-week range.
  The case is intact and the price rose 3.9% since 2026-08-25. It is not in the
  Top 5 because the capital it was earmarked for (ABB proceeds, per the
  2026-08-24 memo) has a better-fitting use this sweep in VICI, which
  diversifies a sector sitting at 0% rather than a sector already represented.
  **Naming the pattern honestly: the destination for these proceeds has now been
  GOOGL (08-18) → META (08-24) → VICI (08-31). That churn is a finding about
  unexecuted decisions, not evidence about any of the three names** — see D-a.
- **NOVO-B.CO (rank 39)** — Defensive's third pick, conviction 6. Beta 0.349,
  ROE 59.8, ROIC 35.6, P/E 11.27, 38% of range, PASS. Blocked for a third sweep
  by the same gap: **no SEK/DKK rate is fetched anywhere**, so the position
  cannot be sized or weighted in base currency. That is a two-line fetcher fix,
  not a research problem.
- **MO (rank 23)** — Macro's third pick, conviction 5: beta 0.495, 6.47%
  dividend, 61.5% operating margin, US domestic earner — precisely the profile a
  positive-real-rate, strong-dollar regime rewards. It is also the concrete case
  for why **D-c (exclusions) matters**: if tobacco is excluded, say so once and
  this voice stops surfacing it. `investor_profile.json.constraints.exclusions`
  is an empty list with "None stated yet."
- **EVO.ST — retired as a contrarian candidate.** Last sweep's most interesting
  find now sits at 97% of its 52-week range. The price answered the question.

---

## 4. Portfolio health scorecard

Carried verbatim from this sweep's `portfolio` lens.

| Dimension | Grade | Number | Reason |
|---|---|---|---|
| Asset allocation vs targets | **ACT** | Equity 70.6% vs 85% target (−14.4pp); Cash 16.4% vs 5% (+11.4pp); Crypto 10.1% vs 10% (on target) | Equity underweight and cash overweight are both >10pp. Good news: the entire cash excess is explained by *deployable* idle cash (ISK cash + PayPal), not by touching the tax reserve. |
| Equity sector concentration | **ACT** | Industrials = 64.6% of the measurable stock sleeve (28,391.85 SEK) | Well over the 45% ACT line. Driven by VOLV-B, ATCO-B, ALFA.ST, ABB.ST together. |
| Geography (home bias) | **ACT** | Sweden = 59.1% of the same measurable slice | Over the 45% ACT line. Portfolio-wide picture is unverifiable. |
| Currency exposure | **UNKNOWN** | — | Snapshot gives quote currency, not underlying revenue currency. Real data gap. |
| Single-position concentration | **ACT** | Avanza Global = 119,999 SEK = 53.6% of total (cap 15%) | Mechanically breaches the cap. Qualifier: a globally diversified index fund, not a single-name bet. |
| Institution concentration | **ACT** | Avanza = 186,900.85 SEK = 83.4% of total (cap 80%) | Marginally over, by design (ISK consolidation). |
| Fee drag | **OK** | 183.14 SEK/yr = 0.082% of total (cap 0.4%) | No holding above 0.5%. |
| Wrapper efficiency | **OK** | ISK headroom 113,099 SEK vs the 300k threshold | No capital left in AF/depa. |
| Drawdown-tolerance fit | **See backtest, below** | Profile states −30% max drawdown | Addressed in full below. |

**Is it provisional?** Partly, and the same two soft fields as last sweep:
`horizon.primary_goal` is "nature UNCERTAIN," `years_until_needed` is "3-7
(SOFT — goal not committed)," and `constraints.exclusions` is an empty list with
"None stated yet" — which is why the ESG row can only ever read UNKNOWN
(**no ESG field exists anywhere in this snapshot or candidate CSV, for any
holding or candidate**). The glidepath re-anchor trigger has **not** fired.
The 85/10/5/0 target stands unchanged and was not re-derived.

### S5 — the drawdown backtest, and what it does and does not close

**First, a correction to the launching prompt.** It stated this was the first
backtest ever run against the target. The repo says otherwise: OPEN_ITEMS.md's
closed index carries "2026-08-17 — S5 resolved: the `backtest` agent ran for
real (its first execution ever) and both the current mix and the adopted
85/10/5/0 target cleared," and the 2026-08-24 memo scored the row "OK
(provisional)" at −19.95%. **This sweep's run is the second, and the two agree
within 0.7pp.** Separately, `portfolio.json.targets.notes` and
`investor_profile.json.reference_targets.ADOPTED_2026-07-27` both still carry
the text "no backtest has ever confirmed" — those two strings are stale and are
the likely source of the prompt's premise. Worth fixing at the file, or the same
wrong premise will keep regenerating.

**This sweep's result** (`data/cache/backtests/20260831T061737.json`): a 90%
VWCE.DE / 10% BTC-USD proxy over 2019-06 to 2026-08 (86 months) produced max
drawdown **−20.62%**, annual vol 14.45%, CAGR 16.33%, Sharpe(rf=0) 1.13, against
the VWCE.DE benchmark's −19.14% / 13.41% / 12.70% / 0.96. On today's
**224,017 SEK** that trough is **~177,825 SEK**, against a −30% tolerance line
at ~156,812 SEK — inside tolerance with about 9.4pp of headroom.

**Does this close S5? Partially, and the honest label is "partially answered,"
not "closed."** Three specific limits:

1. **The window contains no shock of the size the tolerance was written for.**
   The deepest equity drawdown in 86 months of data is −19.14%. A −30% tolerance
   exists to describe behaviour in a −40% to −50% market. The backtest cannot
   speak to a scenario it does not contain, and saying "−20.62% clears −30%" from
   a window whose worst case is −19% is close to circular.
2. **The 10% BTC sleeve barely registered** (−20.62% vs −19.14% for pure
   equity) because monthly rebalancing dilutes crypto's path. The real portfolio
   is not rebalanced monthly — crypto has been allowed to sit at 9.4-10.1% and
   drift. The backtest therefore does **not** test the case the crypto position
   actually poses: allowed to run to 15%+ and then crashing.
3. **The proxy is 90/10; the adopted target is 85/10/5.** The 5% cash line makes
   the real target marginally *less* drawdown-prone, so the proxy is conservative
   on that one axis. No fees, taxes, FX drift or ISK schablonskatt modelled, per
   the file's own caveats.

**What would actually close it:** a fixed-window run across a −40%+ equity
shock. The V2 roadmap's Phase 6 entry says `backtest.py` supports only a rolling
N-year lookback with no `--start`/`--end` — this run's fixed-looking dates may
mean that has changed and should be verified — and VWCE.DE did not exist in
2008, so a longer-history proxy would be needed regardless. Recommend S5 is
re-labelled **partially answered**, with the remaining scope narrowed to exactly
that. Scorecard row this sweep: **OK (provisional, window-limited)**.

---

## 5. Headline calls

1. **BUY 3 shares AZN.ST (~4,715 SEK) from the 11,288 SEK broker-confirmed ISK
   cash.** Fourth consecutive sweep as the top call; the delay has cost 33 SEK
   this week and the position is now +4.1% above blended cost. Confidence:
   **High.** Horizon: **Long.**
2. **SELL all 4 shares ABB.ST (~3,754 SEK) and the single SHB-A.ST share
   (~147 SEK) in one order session.** Rotation on relative merit; no realized
   gain, no tax event, ISK. Confidence: **Medium.** Horizon: **Medium.**
3. **BUY ~15 shares VICI (~3,658 SEK) with those proceeds** — first new
   individual name from the discovery funnel, first Real Estate exposure, first
   non-SEK-listed stock in the sleeve. Starter size, not a full position, and
   **verify the US dividend-withholding treatment inside your ISK before you
   place it.** Confidence: **Medium.** Horizon: **Medium.**
4. **Route the residual ~6,574 SEK of ISK cash into Avanza Global** rather than
   leaving it idle — see §6. Confidence: **High.** Horizon: **Long.**
5. **Execute P3 (the PayPal conversion), unexecuted for a fourth sweep.**
   ~14,094 SEK at a confirmed worst-case 4% spread ≈ 564 SEK friction, ~13,530
   SEK net into the ISK. Confidence: **High.** Horizon: **Long.**

Everything else this sweep is a no: no crypto action, no adds to ATCO-B or ALFA,
no purchase of the funnel's #1, #2 or #4 ranked names.

### Cost of being wrong

| Call | If wrong, realistic downside (SEK) | Recoverable? |
|---|---|---|
| BUY 3 AZN.ST (4,715) | A 25% drawdown on the added shares ≈ 1,179 SEK. Worst realistic case (pipeline failure or dividend cut) ≈ 50% ≈ 2,357 SEK. | Yes — 0.5-1.1% of the portfolio, and the position stays inside the 3-8% band at 5.6%. |
| SELL 4 ABB.ST (3,754) | Opportunity cost, not loss. If ABB re-rates +30% over the horizon you forgo ≈ 1,126 SEK. No tax (ISK); courtage only. | Yes — fully. You can buy it back. |
| SELL 1 SHB-A.ST (147) | If Boman's purchase is a genuine personal signal and SHB re-rates +30%, you forgo ≈ 44 SEK. | Yes — trivially. The real cost is that you cannot express an insider view at this size either way. |
| BUY 15 VICI (3,658) | A 30% REIT de-rating ≈ 1,097 SEK; a genuine rate shock or tenant event at −50% ≈ 1,829 SEK. Add unrecoverable US withholding ≈ 38 SEK/yr on the dividend, and ±5-10% adverse FX ≈ 183-366 SEK if the krona strengthens from DXY 118. | Yes — 0.8% of the portfolio at the −50% case. The FX leg is the least controllable part. |
| Route 6,574 to Avanza Global | A market drawdown on the deployed amount: −20.62% (this sweep's backtested worst case) ≈ 1,356 SEK. Being wrong here really means "cash would have been better," which the profile's own +1.55% real SEK rate caps at a few hundred SEK/yr. | Yes. This is the lowest-regret action in the memo. |
| Execute P3 (~13,530 net) | The 4% spread (≈564 SEK) is a certain, known cost. Wrong only if the money were better left in USD/EUR — bounded by FX drift, a few hundred SEK either way. | Yes. |
| HOLD VOLV-B.ST | Defensive's scenario (leverage bites, recovery stalls): −40% on 4,503.20 ≈ 1,801 SEK. | Yes, but this is the least recoverable call in the memo — 3.8x net-debt/EBITDA makes the downside non-linear rather than proportional. |
| NO ACTION on APP / MU / SNDK | If APP's fundamentals are clean and it re-rates back to mid-range, the forgone gain on a ~4,000 SEK position could be 2,000-4,000 SEK. That is the real, stated price of refusing to buy what you cannot explain. | Yes — a missed gain is always recoverable; a bought discontinuity is not. |

---

## 6. Non-stock structural decisions

Levers 1-2 are structurally closed and are reported only because one item is
live. Wrapper: OK, ISK headroom 113,099 SEK. Fee drag: 0.082% of total. Nothing
broke.

### G1 — Deploy the residual ISK cash

```
ACTION: BUY (route residual idle cash into the secure-tier core)
POSITION: Avanza ISK idle cash 11,288 SEK (broker-confirmed 2026-08-23,
        re-verified against this sweep's portfolio lens §7), of which 4,714.50
        is assigned to AZN.ST above, leaving ~6,573.50
TARGET: ~0 SEK idle ISK cash; ~6,574 SEK into Avanza Global (0.10%/yr, the
        cheapest holding in the portfolio)
REASON: portfolio grades asset allocation ACT at equity 70.6% vs an 85% target
        and cash 16.4% vs 5%. Idle cash inside the wrapper is the single thing
        the scorecard says most clearly not to do, it costs nothing to fix, and
        it carries no tax event. Combined with the AZN buy and the ABB/SHB →
        VICI rotation, equity moves from 158,105.45 to ~169,151 SEK ≈ 75.5% of
        total (computed from portfolio's own figures plus this memo's trades).
THESIS STATUS: INTACT (Avanza Global, `thesis_status: INTACT`, cheapest holding)
WHAT CHANGED: nothing about the merits. What changed is that the Council found
        only two individual names it will actually underwrite this sweep, so
        the residual has to go somewhere and cash is the worst of the available
        somewheres.
BREAK CONDITION: this deliberately does **not** fix the medium-tier underfill
        (individual stocks are 28,392 SEK ≈ 12.7% of total against a 30% tier
        target) and it worsens the already-ACT single-position row (Avanza
        Global 53.6% → ~56.6%). Both are accepted knowingly. If the next two
        sweeps produce underwritable individual names, contributions should go
        there instead, not here.
CONFIDENCE: High
HORIZON: Long
```

### G2 — P3, fourth consecutive sweep

Decided 2026-08-17 (user selected Option A: convert inside PayPal at the
confirmed worst-case 4%), unexecuted since. 1,177.49 USD + 266.88 EUR ≈
**14,093.69 SEK** at this snapshot's `sek_per_usd` 9.4632 / `sek_per_eur`
11.0568; ~564 SEK friction; ~13,530 SEK net into the ISK. Nothing about the
merits has changed and the inflow (~750-1,000 EUR every ~2 months) means the
problem recurs indefinitely. **Break condition unchanged: if PayPal's quoted
spread at execution exceeds ~6%, stop and reopen the routing question.**
Confidence: High. Horizon: Long.

**Capital-availability check, verified against this sweep's `portfolio` output
and not carried from any prior memo:** ISK idle cash **11,288.00 SEK**, PayPal
**14,093.69 SEK** (unconverted, so not yet spendable), genuinely deployable
total **25,381.69 SEK**. Deliberately excluded: the 10,752.76 SEK hb-main tax
reserve and the 611 SEK hb-checking balance — both are earmarked, and treating
them as investable would be a real mistake dressed up as rebalancing precision.
This memo commits 4,714.50 SEK of new capital plus 3,900.80 SEK of rotation
proceeds plus 6,573.50 SEK to the index fund, and requires no PayPal dependency.

---

## 7. Open actions vs open decisions

### Open actions — things to go do

| ID | Action | Amount / detail | By when |
|---|---|---|---|
| **New** | Place this memo's orders: BUY 3 AZN.ST, SELL 4 ABB.ST + 1 SHB-A.ST, BUY ~15 VICI, route residual ISK cash to Avanza Global | ~4,715 buy / ~3,901 sell / ~3,658 buy / ~6,574 fund | Your call on timing; one FOMC caveat in §8 |
| **P3** | Convert both PayPal balances inside PayPal at ~4%, withdraw, transfer to Avanza ISK | 1,177.49 USD + 266.88 EUR → ~13,530 SEK net | Fourth sweep pending; the inflow recurs |
| **P9** | Delete the phantom AZN OPENING row in the Excel Transactions tab | The workbook's own README names this exact fix | Before the next Excel import |
| **P10** | Confirm: was there one 5,000 SEK deposit or two? | `data/transactions.csv` carries rows dated 2026-08-17 and 2026-08-22 | Reply with the correct date |
| **New** | Verify US dividend-withholding treatment on a US REIT inside your ISK, with Avanza or Skatteverket | Decides whether VICI's 6.98% headline yield is ~5.9% net or worse | Before the VICI order |
| **New (file fix)** | Two stale strings say "no backtest has ever confirmed" the target: `portfolio.json.targets.notes` and `investor_profile.json.reference_targets.ADOPTED_2026-07-27` | Both contradicted by the 2026-08-17 and 2026-08-31 backtests | Next time either file is touched |

### Open decisions — forks where the data does not pick one answer

**D-a — What funds what, now that the destination has changed twice.**
- *Option 1 (this memo's call): ABB + SHB proceeds → VICI.* Adds a sector at 0%,
  a country at 0%, a currency at 0%, and takes Industrials under the ACT line.
  Trade-off: an unverified US withholding cost on the yield, plus Macro's FX
  objection at DXY 118.
- *Option 2: ABB proceeds → more AZN.ST.* Highest conviction in the memo, no new
  FX or tax question, deepens the only ballast in the book. Trade-off: pushes
  AZN to ~7.3% of total and does nothing for sector or market-cap diversity.
- *Option 3: ABB proceeds → META*, per the 2026-08-24 call. Trade-off: the case
  is intact (PEG 0.85, forward below trailing, 28% growth) but it diversifies a
  cell VICI diversifies better, and re-confirming it would be the third
  destination in three sweeps.

**D-b — P5/S6: Investor A still cannot be measured.** Third consecutive sweep a
voice has wanted to act and could not.
- *Option 1: get the NAV per share off Investor's monthly IR report* (already
  written as Excel request H). ~10 minutes, closes S6 permanently, and also
  unblocks INDU-C.ST at rank 9.
- *Option 2: sell the 2,044.50 SEK position on the "unmeasurable, and at 93% of
  range" argument alone.* Trade-off: selling a reasonable business on absence of
  evidence rather than evidence of absence.
- *Option 3: keep holding and stop re-flagging it.* Trade-off: it costs a voice's
  attention every sweep, indefinitely.

**D-c — Do you have any exclusions?** `constraints.exclusions` is `[]` with
"None stated yet."
- *Option 1: state none, explicitly.* The ESG scorecard row becomes N/A instead
  of permanently UNKNOWN.
- *Option 2: name specific exclusions.* Live right now: **MO (Altria)** is
  Macro's third pick this sweep and **BETS-B.ST / EVO.ST** (gambling) keep
  surfacing. Under some common exclusion lines all three vanish from the funnel
  and nobody spends time on them again.

**Still open, unchanged, no new evidence this sweep:** P1 (ETH cost basis,
blocked on you), P7 (gold — reviewed, cleared, deferred by you 2026-08-23; not
reopened), S1 (Valour ticker resolves but Yahoo's price is ~7x off — do **not**
wire it as a live feed), S9(a)(b), S20, S21, S22, S23, S24.

---

## 8. Timing collisions

`calendar` ran this sweep (45-day window). **No earnings for any current holding
fall inside the window** — SHB-A 2026-10-21, ABB 2026-10-20, ATCO-B 2026-10-22,
VOLV-B 2026-10-23, ALFA 2026-10-27, AZN 2026-10-30, all beyond it. **INVE-A.ST:
no data returned** — that is "no data," not "no earnings scheduled," and should
not be read as the latter.

Macro events inside the window: **FOMC 2026-09-15/16** (day 2 carries the
Summary of Economic Projections), **Riksbank Business Survey 2026-09-16**,
**Riksbank rate decision + MPR 2026-09-24**, **Riksbank minutes 2026-09-30**.

**One genuine collision, flagged not resolved:** the VICI purchase is a levered
triple-net REIT and the FOMC with an SEP lands two weeks out. This system has no
rate-forecast edge and says so, so this is **not** a reason to delay — but if
you would be uncomfortable holding a rate-sensitive position through that print,
buying after 2026-09-16 rather than before costs nothing but the chance that the
de-rating reverses first. The ABB sale is a Swedish-listed name into a Riksbank
decision on 09-24; it is a rotation, not a rate bet, and the merit case does not
depend on the outcome.

---

## 9. Data gaps for `meta`

What the voices most wanted and did not have, ranked by how often it changed a
conclusion this sweep. Surfaced, not fixed.

1. **US insider data was never fetched for any candidate.** `--insiders` ran
   against the 8 holding tickers, all non-US, so SEC EDGAR returned "skipped"
   eight times and nothing else. The 11 US names in the focus set — APP, VICI,
   NVDA, MU, SNDK, V, MA, TPL, SMCI, APO, EG — were never submitted, and EDGAR
   covers all of them. **The Copycat voice therefore had zero read on the entire
   discovery half of the candidate set**, which is a fetch-scope gap, not a
   source gap, and looks fixable in one argument list. Highest-value item here.
2. **No EV/EBITDA, no EV/EBIT, and for REITs no FFO/AFFO.** Named in
   `council.md` as a standing gap; it bit hard this sweep because three of the
   focus names (VICI, CATE.ST, and by extension BALD-B.ST) are real estate, where
   P/E is the wrong denominator by construction.
3. **Suspect values are withheld from scoring but not from ranking.** SNDK and
   MU rank #2 and #4 overall while their `thin_lenses` fields read "growth 1/4"
   and "growth 2/4" — i.e. they are top-ranked on partial evidence. Worth
   considering whether `thin_lenses` should cap a name's overall rank rather
   than only annotate it.
4. **SNDK has no `beta` value at all and still scored `z_defensive` 1.258** — a
   defensive rank computed without the primary defensive input. Same class of
   problem as #3.
5. **Ratio fields computed across two currencies are still contaminated.** TSM's
   `fcf_yield_pct` of 33.75% implies ~731B USD of free cash flow against a
   2,165B market cap, and its `roic_pct` of 183.7 is not credible either. S17
   was closed on the grounds that the CSV now carries `currency` — but carrying
   the currency does not fix a ratio whose numerator and denominator are in
   different ones. Recommend reopening or a successor item.
6. **No SEK/DKK rate anywhere.** Third consecutive sweep this has blocked
   NOVO-B.CO, which has the best quality metrics of any Nordic name in the set.
   A two-line fetcher addition.
7. **No news, regulatory, litigation or short-interest data of any kind.** This
   is what turned the funnel's #1-ranked name (APP, at 3% of its 52-week range)
   from a decision into a watch. Not necessarily worth building — but it should
   be recorded as the reason a top-ranked name was refused, so the JUDGEMENT
   pillar can eventually tell "correct refusal" from "missed winner."
8. **No multi-year FCF series** (Yahoo's legacy module exposes `netIncome`
   only), which is what prevented any mid-cycle normalisation of MU/SNDK.
9. **MU's unexplained first appearance** at rank 4 with `fetch_failed: 0` on
   both runs — worth a one-line explanation in scout's health block when a
   name's presence changes between runs.
10. **No institutional ownership / 13F** (S20) and **no NAV discount for holding
    companies** (S6) — both already tracked, both bit again this sweep.

---

## 10. Learning notes

- **A low P/E on a holding company is not cheapness, it is an accounting
  artifact.** Investor A shows 4.86x and Industrivärden 3.75x. Both hold
  portfolios of other companies, and the gains on those portfolios flow through
  the income statement as "earnings." When markets rise, reported earnings rise
  with them and the P/E collapses — with no relationship to what the underlying
  assets are worth. Industrivärden's 1,198% "revenue growth" flag is the same
  effect showing up in a different field, which is why scout withheld it. The
  right metric is NAV discount or premium: what the shares cost versus what the
  portfolio inside them is worth. Nobody in this system has that number yet
  (S6), which is why a voice keeps wanting to act on Investor A and keeps being
  unable to.
- **A high debt-to-equity ratio and high leverage are not the same thing.**
  AppLovin shows D/E 111, Zoetis 294, Mastercard 440 — and the screen failed two
  of the three on that basis. But debt-to-equity has *book* equity in the
  denominator, and years of buybacks shrink book equity toward zero regardless of
  how much debt exists. Net-debt-to-EBITDA compares actual net borrowings to
  actual cash generation, and on that measure AppLovin is 0.09 (essentially
  unlevered) and Zoetis 1.86 (modest). Two ratios, same underlying company, very
  different stories — and one of them is measuring the wrong thing.
- **A 6.98% dividend yield is not 6.98% to you.** The US deducts withholding tax
  on dividends at source. Inside an ISK you would normally credit that against
  the ISK's own flat tax — but this ISK sits below the 300,000 SEK allowance, so
  there is no Swedish tax to credit it against and the withholding is simply
  lost. The stated yield is the gross number; what lands in the account is
  meaningfully less. This does not kill the VICI case, but it means a
  high-dividend US name is a worse fit for *this specific wrapper at this
  specific size* than the headline suggests — which is exactly why portfolio fit
  is a separate stage from picking the stock.
- **A backtest can only tell you about the shocks it contains.** This sweep's
  run says the target allocation would have drawn down 20.6% at worst. But the
  worst equity drawdown anywhere in those 86 months is 19.1%. Concluding "20.6%
  clears a −30% tolerance" from a window whose deepest hole is 19% is very close
  to arguing in a circle: the tolerance exists to describe behaviour in the kind
  of crash the data does not contain. The number is real and it is reassuring as
  far as it goes; it just does not go as far as "validated."

---

**`journal` must run before this session ends.** An unlogged memo is invisible
to the next sweep and can never be reconciled — and the calls in it (four
sweeps of AZN, two of ABB, four of P3) are precisely the ones whose repetition
only shows up in the log.
