# Portfolio history archive

Full historical detail moved out of `data/portfolio.json` on 2026-07-28 to
cut the token cost of reading that file every sweep — every agent was
reading 17+ resolved questions and several paragraph-length notes on every
single invocation, even though almost none of it affects a forward
decision. `portfolio.json` now keeps short current-state summaries with
pointers here; this file is read only during `journal` reconciliation or
when someone needs the full "how did we get here" detail.

Nothing here is deleted — verbatim text moved, not rewritten.

---

## Resolved structural questions (full text)

- RESOLVED 2026-07-07: Handelsbanken wrapper is FONDKONTO (AF), confirmed by user. Was question 1 / the blocking question since 2026-07-03. Consequence: exit plan hb-af-exit.
- RESOLVED 2026-07-07: Handelsbanken fund fees - Auto 50 Criteria 0.66%/yr total cost, Auto 75 Criteria 0.67%/yr total cost (user-confirmed).
- RESOLVED 2026-07-12: HB fund sale EXECUTED - actual proceeds 133,657.41 SEK (gain 28,186.20, tax 8,455.86), plus 2,954.42 SEK pre-existing cash, total 136,611.83 SEK now sitting as cash in hb-main awaiting ISK transfer. See exit_plans.hb-af-exit.actual_execution.
- RESOLVED 2026-07-12: SEB transaction column semantics clarified (Datum, Kontotext, Insattning, Uttag, Saldo) - confirmed sold proceeds 13,558.12 SEK, self-consistent against the running Saldo balance.
- RESOLVED 2026-07-13: SEB fully sold and settled, final figure 17,382.43 SEK (user-confirmed) - close to the original ~18,000 SEK estimate, not the ~46k SEK a column misread had implied.
- RESOLVED 2026-07-13: Avanza ISK holdings fully itemized from a live user snapshot - 2 stocks, 2 funds, 1 crypto certificate, plus 565 SEK cash, exact total 36,120 SEK. Prior 15%-single-position-cap concern (18.7% if it were one holding) is moot - no individual holding breaches the cap.
- RESOLVED 2026-07-20: SEB fund realized gain and tax CONFIRMED from user-supplied 2026 tax-year figures (7 fund lots sold 2026-07-08 to 2026-07-10) - total kapitalvinst 10,124.74 SEK, tax at 30% = 3,037.42 SEK. Materially higher than the earlier ~1,200 SEK placeholder. See seb-fund.confirmed_tax_owed_sek and tax_breakdown_by_fund for the full detail. Consequence: the 9,000 SEK hb-main tax reserve is confirmed short by 2,493.28 SEK against the combined 11,493.28 SEK HB+SEB tax owed - see open question 10.
- RESOLVED 2026-07-22: SEB per-fund cost basis and sale proceeds obtained (not just the gain figures) - see seb-fund.tax_breakdown_by_fund for full detail, useful for K4 filing.
- RESOLVED 2026-07-22: Annual fee percentages confirmed from factsheets for all three previously-unknown holdings - Avanza Auto 3 0.39% (0.35% mgmt + ~0.04% transaction), Tundra Sustainable Frontier 2.6% (2.5% mgmt + ~0.1% transaction), COIN-XBT.ST certificate 2.5% (mgmt only, plus a 2% issuer-redemption exit fee that does not apply to ordinary exchange sales). Fee-drag scorecard row is now gradable. Was open question 8.
- RESOLVED 2026-07-22 (partially): a thesis now exists for COIN-XBT.ST (user's cycle-position view on BTC generally) - the standing trim-default question (former open question 7) is superseded by a broader certificate-vs-self-custody decision, see open question 13.
- RESOLVED 2026-07-22: Risk-tier framework REVISED to 60/30/10 (from 70/20/10) at user's direction - see investor_profile.json risk_tier_framework_proposed.
- RESOLVED 2026-07-22: Open question 14 (Tundra Sustainable Frontier) - user decided to SELL in full (2.6% fee unjustifiable). Tax-free inside ISK. Proceeds recycle to secure tier. See the Tundra holding thesis. Awaiting execution.
- RESOLVED 2026-07-22: Open question 15 (equity/fixed-income split) - user directed near-zero fixed income and explicitly accepts total equity >70% ('the push of equity above 70% is fine'). The 50/40 equity/FI glidepath target is superseded by the tier framework; any ballast should be a very small short-duration/money-market sleeve, not traditional bonds. See investor_profile.json risk_tier_framework_proposed.fixed_income_stance. NOTE: this spawned new open question 16 (how to fill the 30% medium tier).
- RESOLVED 2026-07-22: Medium-tier fill (open Q16) - user chose PHASE-IN (option b): park the intended ~59,050 SEK in the Avanza Global secure core now, migrate into individual stocks one vetted position at a time (tax-free in ISK). 30% target stands; timing phased. Q16 reworded to track the migration.
- RESOLVED 2026-07-22: Crypto cap - user chose to TRIM COIN-XBT.ST now (not soft-cap), ~8,628 SEK / 3 of 6 units, tax-free in ISK, proceeds to secure tier per profit-recycling rule, bringing crypto to ~10%. Chose cap discipline over the active BTC thesis. See COIN-XBT.ST holding. Certificate-vs-self-custody (open Q13) remains separate and open.
- CORRECTED 2026-07-27: The 2026-07-22 entry immediately above was inaccurate. User clarified 2026-07-27 that the actual decision was to HOLD the full 6-unit COIN-XBT.ST position and let crypto's percentage weight decline naturally as the portfolio grows, not to sell. See COIN-XBT.ST holding thesis for the corrected record. PROCESS FAILURE, logged for the meta agent: a decision given by the user was mis-recorded in portfolio.json and then treated as ground truth by all four analysis lenses and the Council memo in the 2026-07-27 sweep (reports/2026-07-27-council-memo.md), which recommended executing a trim that the user says was never the actual decision. Same-day, a second instance of the same failure pattern surfaced: the user states they provided Swedbank fund's cost basis previously, but it was never written to this file (open question 3 remains unanswered as of 2026-07-27).
- ADOPTED 2026-07-27: Council's proposed target allocation (85% equity / 5% cash-ballast / ~0% fixed income / 10% crypto, from the 2026-07-27 memo) approved by the user. See investor_profile.json reference_targets. Supersedes the prior null exposure-class targets; the 60/30/10 risk-tier framework's secure/medium split (~55pp/~30pp) still describes composition inside the 85% equity figure.
- RESOLVED / CLOSED 2026-07-27: Former open question 3 ('Swedbank fund cost basis') is now moot - user confirmed there never was a Swedbank account. The 'swedbank-fund' account (10,000 SEK, AF) was a mislabeled duplicate of seb-fund, created before SEB's details were itemized, and was never reconciled away once seb-fund was fully detailed. Removed from accounts/holdings and from total_estimate_sek (was ~227,703, now ~217,703). The user's SEB cost-basis figures given 2026-07-27 match the existing seb-fund.tax_breakdown_by_fund exactly for 7 of 8 funds, confirming that data was captured correctly under the right institution the first time - the error was purely the phantom duplicate entry, not lost cost-basis data. One genuinely new item surfaced: SEB Ostoeuropafond, cost basis 0.25 SEK, added to tax_breakdown_by_fund (immaterial size, sale details unconfirmed). PROCESS FAILURE, for the meta agent: a childhood-fund narrative got recorded twice under two different institution names early on (2026-07-04 era) and nothing in four sweeps' worth of portfolio/wrapper-efficiency analysis caught that 'Swedbank fund, 10,000 SEK, AF' and 'seb-fund, fully detailed, AF' told the same childhood-fund story - worth a standing cross-check for near-duplicate account narratives, not just per-account data completeness.
- UPDATED 2026-07-28: Full live Avanza statement obtained (total 180,949.35 SEK, per-ticker prices for all 5 securities, confirms the Tundra sale is still PENDING not executed - reverts a premature 2026-07-27 note). hb-main tax reserve confirmed at 10,752.76 SEK (the 1,750 SEK pending inflow landed). User placed a 120,000 SEK Avanza Global buy order today, larger than the ~90,240 SEK calculated secure-tier gap, and is redirecting the remaining 24,864.30 SEK toward medium tier (~18-20k: Swedbank Robur Technology A, Spiltan Aktiefond Investmentbolag, open to alternatives) and high-risk tier (~4-7k, TBD) - see open question 16 and avanza-isk.pending_orders.

---

## Account/holding note history (full text, pre-trim)

### hb-main

"USER DECISION 2026-07-22: user will cover the remaining shortfall from other incoming money rather than a dedicated top-up. Combined available toward the 11,493.28 SEK confirmed HB+SEB tax bill: 9,017 SEK here + 611 SEK at hb-checking + 1,750 SEK pending inflow = 11,378 SEK, a residual gap of only ~115.28 SEK, judged sufficient for now ('enough for now') with further top-up expected from future income before the 2027 deklaration. Not a closed item - revisit sizing once actual deklaration prep begins, but no near-term action needed. Prior history: this account held the Auto 50/Auto 75 Handelsbanken funds, sold 2026-07-12 (total confirmed tax 8,455.86 SEK), repurposed 2026-07-20 as a pure tax-reserve sparkonto after 127,611.83 SEK was transferred to Avanza ISK. See exit_plans.hb-af-exit for the full history."

Then updated 2026-07-28: "CONFIRMED 2026-07-28 (user-reported): balance now 10,752.76 SEK - the 1,750 SEK inflow flagged as pending on 2026-07-22 has landed (close to but not exactly 1,750, actual increase 1,735.76 SEK). Combined available toward the 11,493.28 SEK confirmed HB+SEB tax bill: 10,752.76 SEK here + 611 SEK at hb-checking = 11,363.76 SEK, a residual gap of ~129.52 SEK - essentially unchanged from the ~115.28 SEK gap estimated 2026-07-22, not a closed item but low priority, monitor at deklaration prep."

### avanza-isk

"Confirmed ISK. CONFIRMED LIVE FIGURES 2026-07-22 (user-reported, from Avanza directly): total account value 181,254 SEK, of which 144,864 SEK is available for purchase (uninvested cash). This SUPERSEDES the 2026-07-20 computed estimate (181,114.26 SEK total / 145,559.26 SEK cash) - the ~140 SEK total variance and ~695 SEK cash-vs-computed variance likely reflect price movement on the 5 non-cash holdings (SHB-A.ST, INVE-A.ST, Avanza Auto 3, Tundra, COIN-XBT.ST) since their last fetched prices (2026-07-13) - equities fetch has been blocked by an org egress policy every sweep since 2026-07-20, so no fresh per-ticker breakdown is available; implied aggregate non-cash value is 181,254 - 144,864 = 36,390 SEK (up 835 SEK from the stale 35,555 SEK itemized total, unattributed to specific tickers pending a working equities fetch). Historical context (2026-07-13 itemization, now stale): YTD -10.32%, 1y -23.62%, 3y +48.27%, since-inception -33.88%; Sharpe -1.19, standard deviation 22.55%, CAGR -4.52% (securities only, pre-transfer)."

Then updated 2026-07-28 with the full live statement (see current portfolio.json note for the live figures; this paragraph is retained for the historical variance-tracking detail above, which is no longer needed day to day).

### seb-fund

"FULLY TRANSFERRED to Avanza ISK 2026-07-20 (user-reported, same-session) - full 17,382.43 SEK sent, no separate tax reserve carved out here. Tax liability CONFIRMED 2026-07-20 from user-supplied 2026 tax-year figures (per-fund kapitalvinst, see tax_breakdown_by_fund): total realized gain 10,124.74 SEK across 7 fund lots sold 2026-07-08 to 2026-07-10, tax at 30% = 3,037.42 SEK. This SUPERSEDES and is materially higher than the earlier ~1,200 SEK placeholder (2026-07-07) - open question 4 is now RESOLVED with real numbers. Combined with HB's confirmed 8,455.86 SEK tax, total owed is 11,493.28 SEK against the 9,000 SEK reserve at hb-main - a 2,493.28 SEK SHORTFALL, confirmed (not estimated). History: fully sold and settled 2026-07-13, final figure 17,382.43 SEK, all legs landed. CORRECTION 2026-07-27: this account was previously duplicated in this file under a separate, erroneous 'swedbank-fund' account (10,000 SEK, institution 'Swedbank') - user confirmed 2026-07-27 they never held a Swedbank account; that was a mislabeling of this same SEB fund. The phantom account and its holding have been removed."

### tundra

"SELL DECISION 2026-07-22 (user-directed): user will sell this holding in full. Reason: 2.6% total annual fee (6.7x Avanza Auto 3's 0.39%) is unjustifiable fee drag on a ~1,563 SEK position - lever #2. Sale is inside the ISK so NO capital-gains tax event (the +56.27% gain is tax-free here); only broker fees apply. Proceeds (~1,563 SEK, stale 2026-07-13 price) recycle into the deployment plan (secure tier). Was open question 14, now resolved. History: CONFIRMED from factsheet 2026-07-22 as an actively managed frontier/EM equity fund, >=80% frontier/EM, ESG exclusions, recommended holding period 5 years."

Then a 2026-07-27 session note prematurely marked this SOLD/quantity 0 based on the user saying proceeds "will land" at ~1,528 SEK - corrected 2026-07-28 once the live Avanza statement showed the order was still "Skickad" (submitted), not settled.

### coin-xbt

"TRIM DECISION 2026-07-22 (user-directed): trim to bring total crypto (ETH 12,500 + COIN 16,503.12 = 29,003, currently 14.2% of the 203,754 SEK investable base) down to the 10% high-risk cap (~20,375 SEK). Target trim ~8,628 SEK; practical execution = SELL 3 of 6 units (~8,251.56 SEK at the live 2,750.52/unit price), leaving 3 units and total crypto ~20,752 SEK (~10.2%). Tax-free (ISK, ordinary exchange sale - no issuer redemption fee). Proceeds recycle to the SECURE tier per the profit-recycling rule. Trimming COIN rather than ETH is deliberate: ETH is self-custody (a sale is a 30% K4 event, cost basis unknown), COIN inside the ISK is tax-clean. NOTE the tension: this cuts against the user's own active bullish BTC thesis - user chose cap discipline over the thesis 2026-07-22."

This entire decision was CORRECTED 2026-07-27 - the user clarified the actual decision was to HOLD the full 6 units, not trim. See the resolved_structural_questions CORRECTED entry above for the full process-failure writeup.

---

## thesis_narrative full text, archived 2026-08-17

`portfolio.json` holdings carry structured thesis fields since the V2
Roadmap Phase 1 schema (`why_owned`/`expected_driver`/`valuation_reason`/
`key_risks`/`break_conditions`/`thesis_status`) — the older free-text
`thesis_narrative` field on each holding had kept growing in parallel and
become redundant with those fields (up to 1.7KB per holding). Trimmed to a
one-line pointer per holding; full prior text below, verbatim.

### SHB-A.ST
RECORDED 2026-08-03 (user's own words, closes the long-standing gap): bought because Handelsbanken has 'shown good track record' and is a 'secure', 'stable' pick that 'still shows good upside'. PROVENANCE, stated candidly by the user and kept because it matters: 'I actually bought them without considering a lot of other different options, it was rather that I had some money left and just wanted it to be active on the market.' So this is a PARKING decision, not a conviction pick - the user has explicitly NOT compared it against alternatives. Two consequences agents must respect: (1) it is legitimately testable on 'stable with upside' - if stability or the track record breaks, the thesis breaks; (2) because no comparison was ever made, this position is a FAIR ROTATION CANDIDATE when the medium-tier build (OPEN_ITEMS.md P6) surfaces a better-vetted name. Do not treat it as a high-conviction holding the user is attached to. TENSION TO WATCH: the 'stable/good track record' premise is the part current data argues with - revenue declined 3.8% YoY, PEG ~20, analyst consensus 'underperform'. That does not break the thesis yet (a low-beta 5.5% dividend payer is still defensible as 'stable'), but 'good upside' is the limb under most pressure. swedish-equity-review 2026-07-28 (full real data, see data/company_profiles/SHB-A.ST.json): Score 58/100, Coverage 80% (5/6, only Business Quality missing). REAL TENSION: fundamentals say caution (revenue declined FY2025, PEG ~19.8, analyst 'underperform') but Chairman Par Boman + board member Fredrik Lundberg both bought very heavily (>750M SEK combined) within 48 hours, 2026-07-20/21 - the two signals disagree, not averaged away. Live price 144.25-144.85/share (2026-07-28).

### INVE-A.ST
RECORDED 2026-08-03 (user's own words, same rationale as SHB-A.ST - both were bought together): 'good track record', 'secure'/'stable' pick that 'still shows good upside', bought 'without considering a lot of other different options... had some money left and just wanted it to be active on the market'. Same two consequences as SHB-A.ST: testable on the stability/upside claim, and a fair rotation candidate rather than a conviction holding, since no comparison was ever made. NOTE - this thesis fits Investor A better than it fits Handelsbanken: a diversified Swedish holding company IS structurally a 'stable with upside' vehicle, and current data does not argue with it (ROE 27.3%, positive FCF, up 39.2% vs cost basis). The honest caveat is unchanged: the metric that would actually test it for a holding company is NAV discount/premium, which has never been obtained (see OPEN_ITEMS.md S6) - the 4.71x P/E is an accounting artifact and must not be read as 'cheap'. So the thesis is plausible but still not properly testable. swedish-equity-review 2026-07-28 (see data/company_profiles/INVE-A.ST.json): NO SCORE reportable (corrected same day) - only 2 of 6 dimensions have real data (Dividend Quality, Insider Activity); Holding Company Valuation requires an actual NAV discount, not obtained (would need Investor's own IR page or a quarterly report PDF), so it's marked Not Available per the NAV fallback hierarchy, not filled in with a P/E stand-in. Insider activity: sustained modest CEO/board buying over 6 months. Live price 397.00-400.80/share (2026-07-28).

### ATCO-B.ST
BOUGHT 2026-08-03 or 2026-08-04, part of the OPEN_ITEMS.md P6 medium-tier build. swedish-equity-review RUN 2026-08-17 (full 6-dimension scored review, fresh Yahoo quoteSummary fundamentals + FI insider fetch same day - see data/company_profiles/ATCO-B.ST.json review_history): Score 62/100, Coverage 100% (6/6). Genuinely high-quality business (BQ 8.5/10: global #1/#2 in compressors/vacuum, 42% gross margin, ROE 25.7%, ROIC ~40% est., low leverage D/E 33.7) bought at a rich valuation (Val 3.5/10: trailing P/E 33.2x, PEG 2.38, price at 98.5% of its 52-week range) with a thin insider signal (5.5/10: mostly routine option-exercise pairs, one real board-member buy 2026-06-09 at 161.57 SEK, since up ~13%) and a choppy growth picture (FY2025 revenue -4.8% vs FY2024, but ttm +9.1% recovering). This upgrades, not replaces, the 2026-08-12 user-stated thesis below - the 'no differentiated case, just track record' framing is now backed by real numbers pointing the same direction: strong company, expensive entry.

### AZN.ST
BOUGHT 2026-08-03/04 (4sh, part of the OPEN_ITEMS.md P6 medium-tier build) + 2026-08-06 (1sh, executing the Council's call D). Dual-listed (UK primary, Nasdaq Stockholm cross-listing per data/universe.json's category_notes). REAL THESIS RECORDED 2026-08-06 (user's own reasoning, closes Council call A for this ticker): historically resilient, defensive quality company - healthcare is lower-beta than high-valuation tech/growth; reasonable dividend history; diversifies the portfolio away from its industrials/technology concentration; expected to hold up better than high-valuation growth assets if those correct. Break conditions: revenue growth or margins deteriorate structurally (thesis rests on defensive resilience, not growth); the dividend is cut (removes the income-resilience leg); or it re-rates to trade at a premium indistinguishable from the growth assets it's meant to diversify against. Horizon: 3-5 years, per the user's own framing.

### ALFA.ST
BOUGHT 2026-08-03 or 2026-08-04, part of the OPEN_ITEMS.md P6 medium-tier build. swedish-equity-review RUN 2026-08-17 (full 6-dimension scored review, fresh Yahoo quoteSummary fundamentals + FI insider fetch same day - see data/company_profiles/ALFA.ST.json review_history): Score 63/100, Coverage 100% (6/6) - the HIGHEST of the three P6 industrials reviewed this session. Solid business (BQ 7.5/10: leading heat-transfer/separation/fluid-handling player, diversified marine/energy/food-water exposure) with a genuinely consistent 4-year revenue growth trend (2022-2025: +22%, +5.3%, +4.1%, ttm +7.7% - no down year, unlike ATCO-B.ST) and the STRONGEST insider signal of the three: 10 of 10 FI-recorded transactions since 2023 are real open-market Acquisitions (zero disposals), across 7 distinct insiders. Still expensive on an absolute basis (Val 4.0/10: trailing P/E 28.1x, PEG 2.86 - actually worse growth-adjusted value than ATCO-B.ST despite the lower headline P/E). Best fundamentals+insider combination of the three but not a Buy at this price.

### ABB.ST
BOUGHT 2026-08-03 or 2026-08-04, part of the OPEN_ITEMS.md P6 medium-tier build. Dual-listed (Switzerland primary, USD reporting; Nasdaq Stockholm cross-listing is what this portfolio holds). swedish-equity-review RUN 2026-08-17 (full 6-dimension scored review, fresh Yahoo quoteSummary fundamentals + FI insider fetch same day - see data/company_profiles/ABB.ST.json review_history): Score 51/100, Coverage 100% (6/6) - the WEAKEST of the three P6 industrials reviewed this session and the clearest rotation candidate. Real business quality (BQ 8.0/10: ROE 32.6%, 40% gross margin, direct electrification/automation tailwind exposure) undercut by: (1) the richest valuation of the three (trailing P/E 37.3x, forward P/E 36.9x - essentially FLAT, meaning the market is not pricing further EPS growth despite 14.2% ttm revenue growth, a margin-compression flag); (2) the thinnest FCF conversion (FCF margin ~4.4% vs ATCO-B.ST's ~15.3%/ALFA.ST's ~6.9%, heaviest capex load); (3) a DATA QUALITY FINDING - Yahoo's raw P/S (49.3x) and P/B (110.9x) are implausible, traced to a USD/SEK unit mismatch (market cap correctly in SEK, revenue/book-value still in ABB's USD reporting currency, undivided by the ~9.475 SEK/USD rate); FX-corrected estimates are ~5.2x and ~11.7x respectively, used for scoring instead of the raw figures - see company_profiles/ABB.ST.json currency_note; (4) a recent, sizeable insider-selling cluster - senior executive Peter Terwiesch made three separate open-market disposals within 2 weeks of this review (~48,800 shares / ~CHF 3.85M, 2026-07-31 to 2026-08-14), plus a board-member disposal - the most bearish insider pattern of the three names.

### COIN-XBT.ST full sale_record/thesis_narrative/price_tracking_note, pre-trim (also archived here, not just under the earlier coin-xbt heading, since this is the 2026-08-17 close-out trim)
Sale record: USER-REPORTED 2026-08-17: full 6-unit position sold at 2,561 SEK/unit (exact intra-day execution time not given). Gross proceeds 6 x 2,561 = 15,366 SEK (courtage not stated, not subtracted). Realized gain 6 x (2,561 - 2,016.67) = 3,265.98 SEK, tax-free inside the ISK. This was NOT the 1-unit trim the 2026-08-17 Council memo recommended (Call 1) - the user sold the full position instead. Proceeds credited to the avanza-isk CASH_SEK holding, ultimately funding the Valour Bitcoin Zero purchase after BITC was evaluated and rejected.
Price tracking note (historical, no longer relevant post-sale): NO USABLE TICKER (confirmed by user 2026-08-03). The 'COIN-XBT.ST' symbol 404s on Yahoo and has no chart fallback. AGREED PROXY (user's suggestion, adopted): track spot BITCOIN via CoinGecko as a directional indicator, NOT an exact price. Calibration anchor set 2026-08-03: BTC 54,786 EUR x 11.0432 SEK/EUR = ~605,013 SEK/BTC, vs. certificate 2,540 SEK/unit -> ratio ~0.004198 BTC per unit.
Avanza-isk cash reconciliation (2026-08-17, in full): the previously-flagged unexplained +5,000 SEK gap (20,366 vs. the 15,366 SEK that traced cleanly to the COIN-XBT.ST sale) was resolved same day - user confirmed they transferred their externally-available 5,000 SEK into this account (the same 5,000 SEK the 2026-08-17 memo had earmarked for a possible AZN.ST buy). So 20,366 = 15,366 (XBT sale gross proceeds) + 5,000 (external transfer). From that 20,366, the user spent 9,183 SEK on 150 units of the Valour Bitcoin Zero SEK certificate. Remaining cash: 11,183 SEK.

---

## P4 deliberation history (full text, archived 2026-08-17 - item is CLOSED)

- 2026-08-03: decided NOT to move to self-custody, stay in the ISK wrapper and cut the fee instead. Target: COIN-XBT.ST cost 2.5%/yr on ~15,240 SEK. What's needed: verified tickers/fees for alternatives (see S1).
- 2026-08-17 (morning): situation changed from "trim and find something cheaper" to "already sold, what now" - user sold the full 6-unit COIN-XBT.ST position at 2,561 SEK/unit (not the 1-unit trim the same-day Council memo recommended). Live question: rebuy via BITWISE TRND BITCN TRSR STRGY ETF (ARCX:BITC)?
- 2026-08-17 (Council Candidate Evaluation, `reports/2026-08-17-council-memo-2.md`): REJECT BITC, High conviction. The ticker's full name reads as a bitcoin-treasury-strategy product, not a confirmed spot-BTC tracker; also flagged (not load-bearing) that US-listed ETFs are generally unavailable to EU retail under MiFID II/PRIIPs. Council's Call 2: deploy the 15,366 SEK sale proceeds as 2,513 to Avanza Global now and 12,853 earmarked for a verified BTC ETP, 2026-09-03 auto-convert fallback. Also rejected the portfolio agent's "more self-custody ETH" fallback (P1 being open makes that worse, not neutral).
- 2026-08-17 (later, user's own find): bought 150 units of a Valour Bitcoin Zero SEK certificate (ISIN CH0585378661) at 61.22 SEK/unit = 9,183 SEK directly.
- 2026-08-17 (final): user confirmed 0%/yr fee, genuinely BTC-backed - both verification questions closed by direct statement. P4 CLOSED. Only remaining loose end: a tradeable ticker for live pricing (S1).

---

## S12 full deliberation history (archived 2026-08-17 - D3 closed, D4 still open but consolidated)

- **Why this recurred (2026-08-11):** the crypto trip-wire check produced three different "investable capital" denominators for the identical 24,115.89 SEK of crypto: the 2026-08-10 pinned definition (204,611.94 SEK -> 11.79%, does not fire), the portfolio agent's proposed "Convention A" (201,895.91 SEK -> 11.94%, does not fire), and "Convention C" (190,532.15 SEK -> 12.66%, already breached). Same failure class as S11 (two agents computing "% of 52-week range" two different ways) recurring one level up, at the denominator.
- **2026-08-12:** Council's Call 2 proposed Convention B (investable-only: Avanza ISK + ETH wallet, 188,918.15 SEK) for D3, pending user confirmation. Same sweep, D4 surfaced as a third instance of the same failure class (gross-proceeds vs. realized-gain-only reading of profit_recycling_rule) and was folded into S12 rather than opened separately.
- **2026-08-17 (morning):** D3 became decision-relevant, not cosmetic - Convention B read 12.97% (fires the trip-wire) vs. full-portfolio 11.43% (does not fire) on the identical 24,492.89 SEK of crypto. Council sized that sweep's trim (1 unit) to be correct under both readings as a workaround, not a substitute for the user's actual confirmation.
- **2026-08-17 (later, live session):** user confirmed the full-portfolio convention for D3 (Council's non-recommended option) - pinned in `data/cache/definitions.json`. D4 was initially mis-noted as "practically overtaken" by the COIN-XBT.ST full sale; Council's second memo caught that this was backwards - a full sale makes the gross-vs-gain gap its largest ever (15,366 SEK vs. 3,265.98 SEK), which is exactly when the ambiguity is MOST decision-relevant, not least. D4 reopened.
- **2026-08-17 (same day):** a narrower instance surfaced - the real S5 backtest used the investable-only base (188,839 SEK) while D3 (pinned hours earlier) is the full-portfolio convention (218,826 SEK). Defensible on its own terms (a backtest can't simulate a tax reserve or PayPal balance sitting outside the market), but `definitions.json`'s wording reads broader than intended. Flagged for `meta` to add a `risk_simulation_base` distinct from `investable_capital_convention` rather than force one convention to cover both purposes - not yet applied.

---

## V2 Roadmap Phase 7, original 2026-08-17 draft (superseded 2026-08-18 by the user's detailed 5-item spec, archived verbatim)

**Phase 7 (proposed 2026-08-17, not started) — true per-persona isolation for the Stock Selection Council.** Currently `council`'s six analyst personas are role-played sequentially by one subagent invocation, sharing one context window — real independence (Step 1 says "draft all six in isolation") is enforced by instruction, not by the architecture. The alternative: the orchestrating session spawns six separate `Agent` tool calls (a shared, parameterized "council-analyst" agent definition, one persona name passed per call) in parallel, each reading only its own relevant data slice, genuinely unable to see any other persona's output — then a seventh `Agent` call ("council-chairman") reads all six results plus the raw data and writes the memo. This also opens the door to what the user asked for directly: each persona could target a *different* part of the Excel workbook / a different subset of fetched data if that turns out to matter, and each becomes individually promptable/tunable without touching the others.

Deliberately not implemented same-day as this proposal — the tradeoff is real, not just execution risk: true isolation likely increases total token cost (each of 7 invocations loads its own copy of the shared context - snapshot, digest, portfolio state - instead of one subagent reading it once), which cuts against the same session's token-cost fix (the digest CSV, Step 0 triage). It buys independence and per-persona control, not cheapness. Worth building once the digest-based version has run a few real sweeps and the marginal value of stricter isolation (vs. the current instruction-enforced version) is actually evidenced, not assumed. Revisit if a sweep produces visible evidence of one persona's write anchoring another's (the failure mode this would fix) — 2026-08-18 note: the first real production sweep under the digest-based version ran this session and produced genuine, substantive disagreement across the six voices (see the memo's "Where the agents disagreed" section) with no visible sign of one persona's conclusions anchoring another's — one data point against urgency, not proof the failure mode can't occur, but no evidence yet that it has.

---

## OPEN_ITEMS.md closed log, archived verbatim 2026-08-24

Moved out of `OPEN_ITEMS.md` during the discovery-funnel refactor so the live review surface holds what is outstanding, not what is finished. Nothing was deleted; the full text of every closed item is below, and `OPEN_ITEMS.md` keeps a one-line index pointing here.

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

