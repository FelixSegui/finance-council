# Council memo — 2026-08-17 (live session, memo 2 of 2)

**This memo supersedes `reports/2026-08-17-council-memo.md`.** That one was an
automated scheduled sweep that fired this morning against snapshot
`20260817T061032.json`, before you sat down. This is the live version: a fresh
snapshot (`data/cache/snapshots/20260817T111313.json`, 11:13 UTC), a fresh Excel
import, five analyst agents plus `scout`, the first real `backtest` this system
has ever run, the retroactive `swedish-equity-review` on the three P6 industrials
— and four of your own decisions taken since. Four of the morning memo's five
headline calls are overtaken by events; the reconciliation is in section 2.

*Structured synthesis of this system's own agents' analysis. Not advice from a
licensed advisor. Every number traces to the snapshot above,
`data/portfolio.json`, `data/cache/definitions.json`,
`data/cache/excel_import/latest-summary.json` (fresh, 11:11 UTC),
`data/cache/backtests/20260817T1117*.json`, or `data/cache/calendar/`, all read
this sweep.*

`journal` ran in session-start mode at the top of this session. Per `OPEN_ITEMS.md`
P2 item 3, the journal-before-council ordering rule does not transplant as a hard
stop in this architecture — reconciliation is a separate end-of-sweep artifact in
`SESSION_LOG.md`, not a section of this memo. Not treated as a blocker.

**Blocking-question check.** No open item holds blocking status. Per CLAUDE.md's
2026-08-03 phase shift, this memo leads with how the positions are behaving and
what should change.

---

## 1. Position report

Snapshot `20260817T111313.json` · previous `20260817T061032.json` (this morning)

> **Provenance note, stated because it matters.** This Council run had no shell
> access, so the table below was reconstructed from the snapshot and
> `portfolio.json` using `position_report.py`'s own conventions rather than by
> executing the script. It is not an estimate: every figure is arithmetic on
> fetched values, and the totals reconcile **exactly** to the portfolio agent's
> independently-computed figures (Avanza ISK 184,352.65 SEK; full portfolio
> ~218,826 SEK; crypto 4.13%; equity 67.55%; cash 20.93%). That agreement between
> two independent computations is the cross-check. Re-run the script next sweep.

| Position | Price | Δ vs this morning | Δ vs cost | 52w percentile | Value (SEK) | Source |
|---|---|---|---|---|---|---|
| Handelsbanken A (1 sh) | 148.30 | +0.5% | **+14.7%** | **95.7%** | 148.30 | fetched |
| Investor A (5 sh) | 406.70 | -0.1% | **+40.1%** | 91.4% | 2,033.50 | fetched |
| Volvo B (13 sh) | 340.20 | +0.0% | **-7.4%** | 73.5% | 4,422.60 | fetched |
| Atlas Copco B (27 sh) | 181.15 | -0.7% | -0.1% | 92.6% | 4,891.05 | fetched |
| **AstraZeneca (5 sh)** | **1,480.00** | **-2.2%** | **-2.0%** | **20.5%** | 7,400.00 | fetched |
| Alfa Laval (9 sh) | 557.20 | -1.0% | -3.0% | 79.6% | 5,014.80 | fetched |
| ABB (4 sh) | 971.60 | -1.0% | +2.6% | 80.2% | 3,886.40 | fetched |
| Avanza Auto 3 (fund) | no data | — | +65.2% | — | 16,191.00 | book value |
| Avanza Global (fund) | no data | — | +0.0% | — | 119,999.00 | book value |
| **COIN-XBT.ST** | **SOLD 2026-08-17** | — | **+27.0% realized** | — | **0** | user-reported, 6 × 2,561 |
| ETH (0.50185, self-custody) | 17,992.33/unit | +0.3% | no data (P1) | — | 9,029.46 | fetched (CoinGecko × sek_per_eur 10.9523) |
| Avanza ISK cash | — | — | — | — | **20,366** (only 15,366 traced — see flag) | Excel delta |
| HB tax reserve + checking | — | — | — | — | 11,363.76 | confirmed |
| PayPal (1,177.49 USD + 266.88 EUR) | — | — | — | — | 14,079.79 | confirmed |

**Full portfolio 218,826 SEK** (full-portfolio convention, per
`data/cache/definitions.json`, D3 decided by you today). Equity 67.55% · crypto
4.13% · cash 20.93%. Crypto spot: BTC 54,838 EUR (-49.1% off ATH; 24h +1.1%, 7d
-2.1%, 30d -0.5%), ETH 1,642.79 EUR (-61.2% off ATH). Fear & Greed 31 ("Fear").

**Reading it.** The equity book barely moved in five hours — nothing exceeds
2.2% — so the movement that matters this week is entirely structural, not
price-driven: **you sold the whole Bitcoin certificate.** That single action
realized 3,265.98 SEK tax-free, cut annual fee drag by 68% (from ~567 to 183.14
SEK/yr, 0.084% of the portfolio), and flipped crypto from 11.43% *over*-target to
4.13% — 5.9pp *under* it. It also parked 15,366 SEK in cash, which is why the
allocation scorecard now reads ACT on two lines that read WATCH this morning. The
index funds (Avanza Global 54.84% of the portfolio, Auto 3) are deliberately
buy-and-hold, both INTACT, nothing to do.

**Does anything contradict a thesis?** One thing, and it contradicts it in the
*helpful* direction. **AstraZeneca fell from the ~32nd to the 20.5th percentile
of its 52-week range today, intraday, and is now below its 1,509.70 cost basis** —
while its fundamentals are unchanged (revenue +6.4%, fourth consecutive rising
year, margins 23.5%, PEG 1.34, beta 0.211). Thesis-review keeps it **INTACT** and
calls it "the textbook case the method exists to catch: price down, thesis intact
— a better entry than the position was bought at, not a worse one." I agree, and
it is the basis of Call 3.

Against that, **Handelsbanken A at 95.7% of its range is the mirror image**:
effectively at its 52-week high on unimproved fundamentals (revenue -3.8% YoY, PEG
20.4, analyst "underperform"). Valuation's word is "cheap for a reason, not
mispriced." It is one share, 148.30 SEK, 0.07% of the portfolio — it cannot affect
returns and costs a line of attention every sweep. Close it out or build it at the
next natural rebalancing; do not keep carrying it as a token.

---

## 2. What should change

### 2a. Reconciling the morning memo

| Morning call | Status now | What actually happened |
|---|---|---|
| **Call 1** — trim 1 unit COIN-XBT.ST | **SUPERSEDED** | You sold all 6 units at 2,561 SEK. Over-delivered on the fee half (drag -68%, P4's fee problem is gone); overshot the sizing half (crypto 11.43% → 4.13%, from marginally over to 5.9pp under target) |
| **Call 2** — hold the five, run `swedish-equity-review` by 2026-09-03 | **EXECUTED same day** | ALFA 63 / ATCO-B 62 / ABB 51. The call's load-bearing premise — "no vetted alternative exists, because the review has never run" — is now dead. See Call 4 |
| **Call 3** — adopt neither target, run S5 first | **RESOLVED, and reversed** | S5 ran for real. Both allocations *clear* the -30% tolerance (-14.6% current, -19.95% target), the opposite of the morning's illustrative -42.3%/-45.75%. See Call 5 |
| **Call 4** — PayPal: measure, dated fallback | **SUPERSEDED** | You declined the Revolut test and chose Option A outright. P3 is decided, pending execution |
| **D3 recommendation** — Convention B | **SUPERSEDED** | You chose the full-portfolio convention. Pinned in `definitions.json`; every figure in this memo uses it |

Four of five morning calls overtaken within hours. That is not a criticism of the
automated sweep — it refreshed the data this session ran on — but it is worth
recording plainly for `meta`: **the scheduled pre-session sweep's decisions have a
short shelf life against a live session, and should be read as a data refresh
plus a provisional agenda, not as standing calls.**

### 2b. What to change now

**Five things. Three are executable this week.**

1. **Do not buy BITC.** Full Candidate Evaluation below. Two independent
   disqualifiers, either one sufficient. This is the answer to P4's live question.
2. **Deploy the confirmed 15,366 SEK of ISK cash** — 12,853 SEK earmarked to
   restore crypto to its 10% target *once a vehicle is verified*, with a hard
   2026-09-03 default into Avanza Global if it isn't; 2,513 SEK into Avanza Global
   now. Call 2.
3. **Put the external 5,000 SEK into AstraZeneca — 3 shares at ~1,480 SEK.** It is
   the one name all four lenses agree on, it just dipped below your cost basis on
   unchanged fundamentals, and it is the only add that *reduces* the ACT-rated
   industrials concentration instead of worsening it. Call 3.
4. **Verify the unexplained +5,000 SEK in the ISK cash line against a live Avanza
   statement before treating it as deployable.** Open action, not a call — but it
   is the same class of error that produced a wrong recommendation on 2026-08-11.
5. **Keep the 85/10/5/0 target. S5 is answered.** Do not re-open the allocation on
   the morning memo's superseded estimate. Call 5.

### 2c. Buy list for the 5,000 SEK you actually have

You asked for concrete ideas for the 5,000 SEK sitting in a separate external
account. Ranked, and kept strictly separate from the watchlist section below.

| # | Buy | SEK | Why this, now |
|---|---|---|---|
| **1** | **AZN.ST — 3 shares @ ~1,480** | **~4,440** | Only name with no dissent across valuation (Cheap/Fair, PEG 1.34), thesis-review (INTACT, "strongest mispricing-not-deterioration case in the book"), macro (beta 0.211, defensive, right side of the regime) and portfolio (healthcare *reduces* the 65.5% industrials sleeve). Now **below your own cost basis** on unchanged fundamentals. Earnings already reported 2026-07-27 — no collision |
| 2 | Avanza Global — remainder | ~560 | 0.10%/yr, closes the -17.5pp equity gap directly, zero single-name risk. This is where the change goes |
| — | *Alternative if you want zero single-name risk* | 5,000 | Whole amount into Avanza Global. Slightly worse expected outcome, materially simpler, and still correct — the equity underweight is the single biggest deviation on the scorecard |

**Explicitly not on this list, and why:** **VOLV-B.ST**, despite being -7.4% below
cost and cheap-looking (forward P/E 13.7, PEG 1.42, analyst "buy"). Two reasons:
its status is TOO_EARLY at ~2 weeks held against its own 3-month break condition,
and buying more would deepen the industrials concentration that is already
ACT-rated. **ATCO-B / ALFA / ABB**: all PEG > 2, all 79-93% of range, all
WEAKENING — the P6 review's own recommendation is "do not add to any of the three
at current valuations," and I am not overriding it.

### 2d. Watchlist expansion — to add, not to buy

`scout` offered five discretionary names (explicitly not on the 67-entry
watchlist, no fundamentals fetched, not screened). Add them to the Excel Watchlist
tab so they get screened next sweep. **None of these is a buy recommendation —
this system has fetched exactly zero fundamentals on any of them.**

The Council-level read `scout` couldn't give: your portfolio's actual named gap is
*non-industrial, non-cyclical* exposure (industrials 65.5% of the stock sleeve,
ACT). Sorted by whether they fill that gap or worsen it:

- **Fills the gap:** **MSCI** (index provider, ~70% operating margins, subscription
  revenue — a quality compounder uncorrelated with the capex cycle), **SNPS**
  (Synopsys, EDA software, structural moat), **ARM** (chip-IP licensing).
- **Worsens the gap:** **SCCO** (Southern Copper) and **STL** (Stellantis) are both
  levered to the same global industrial cycle Volvo/Atlas Copco/Alfa Laval/ABB
  already sell into. STL's 7-8% dividend yield is a classic value-trap profile in a
  cyclical trough. Add to the watchlist for coverage; do not treat the yield as a
  reason to buy.

**One caution on `scout`'s 32 screen survivors** (AAPL, GOOGL, MSFT, META, NVDA,
V, JNJ, KO, PG, SAP, TSM, TMO…): most of these are top-20 constituents of Avanza
Global, which is 54.84% of your portfolio. Buying them individually does not
diversify — it concentrates. The non-overlapping ideas in that list are the Nordic
names (NOVO-B.CO, LIFCO-B.ST, HEXA-B.ST, TEL2-B.ST, EQNR, VWS.CO), and NOVO-B.CO
is the one that also fills the healthcare/defensive slot AZN.ST occupies. Nothing
to act on this week.

---

## 3. Portfolio health scorecard

Carried over from the portfolio agent verbatim, with the drawdown row updated from
this sweep's real backtest.

| Dimension | Grade | Detail |
|---|---|---|
| Asset allocation vs targets | **ACT** | Equity **67.55%** vs 85% target — **-17.5pp / ~38,206 SEK short**. Cash **20.93%** vs 5% — **+15.9pp / ~34,868 SEK excess**. Both driven by today's full COIN-XBT.ST sale |
| Crypto allocation | **WATCH** | 4.13% vs 10% target, -5.9pp. Flipped from overweight to *under*weight via the sale. Nowhere near the 12% trip-wire (which is an upper bound only) |
| Equity sector concentration | **ACT** | Industrials **65.5%** of the individual-stock sleeve |
| Geography | **OK** | — |
| Currency exposure | **UNKNOWN** | No revenue-by-currency data for any holding |
| Single-position concentration | **WATCH** | Avanza Global **54.84%** of the portfolio — a literal breach of the 15% cap, but it is a diversified index fund, not single-company risk. Flagged, not urgent |
| Institution concentration | **ACT** | Avanza **84.25%**, breaches the 80% cap — mostly the byproduct of correct ISK consolidation, not idiosyncratic risk. No action proposed |
| Fee drag | **OK** | **183.14 SEK/yr = 0.084%**, down from ~567 SEK/yr pre-sale (**-68%**). The sale closed the fee-drag lever entirely |
| Wrapper efficiency | **OK** | 184,352.65 SEK in the ISK vs the 300,000 SEK allowance (confirmed by you today, P7) — 115,647 SEK headroom |
| Drawdown-tolerance fit | **OK (provisional)** | **Was UNKNOWN — now answered.** Real backtest, 86 months: current mix max DD **-14.6%**, adopted target **-19.95%**, both inside the stated -30%. Provisional because it is one 7.2-year path — see Call 5 for what it does not cover |

**This scorecard is provisional on three unanswered `investor_profile.json`
questions, named rather than smoothed over:**

- **Where is the emergency buffer?** "3-6 months" is stated; which account holds it
  is not recorded. This is load-bearing — it decides whether the 11,363.76 SEK of
  HB cash is buffer or investable capital, and therefore whether cash is really
  20.93% or materially less.
- **`horizon.primary_goal` is explicitly uncertain and the liability currency with
  it.** If the Mediterranean-apartment option firms up, the future liability is EUR,
  not SEK — which reverses the rationale for the Nordic tilt entirely
  (`horizon.currency_note`).
- **Currency exposure stays UNKNOWN** because no source gives revenue-by-currency.
  ABB's own review this sweep found a USD/SEK unit error in Yahoo's raw P/S and P/B
  — a live reminder that this gap is not cosmetic.

**Structure (levers 1-2): nothing broke, and one item closed.** All capital is in
the ISK. Fee drag fell to 0.084%. **P4's fee problem no longer exists** — the 2.5%
certificate is gone. What remains of P4 is only "replace it with what," which is
Call 1 and Call 2.

---

## Headline calls

Five calls. Each ran the six-voice Investment Council method; the voices are
compressed to their load-bearing sentence, the Chairman's decision is the content.

### Call 1 — BITC: do not buy it. (Candidate Evaluation, full method)

BITC is not a current holding, so this runs the **Candidate Evaluation** method —
five voices formed independently, then the Chairman — not the existing-holding
format.

**The single most important fact, stated first and not softened:** the ticker's
own name, *BITWISE TRND BITCN TRSR STRGY ETF*, does not describe a spot-bitcoin
fund. It reads as a **trend / bitcoin / treasury strategy** product. That naming
pattern belongs to funds that rotate between bitcoin exposure and US Treasuries on
a momentum signal, or that hold equities of bitcoin-treasury companies — not to a
fund holding physical BTC in custody. Your characterization ("fully BTC-backed")
may still turn out to be right; the point is that **nothing in this sweep's data
confirms it, and the entire case for the trade depends on it being true.**

There is a second, weaker piece of evidence pointing the same way. BITC trades at
**35.475 USD, just 2.8% above its 52-week low of 35.09, and -27.6% below its
52-week high of 48.985** — while BTC is roughly flat over the last 30 days (-0.5%)
and 7 days (-2.1%). A physically-backed 1:1 tracker should be checkable against its
underlying in one step. This snapshot doesn't carry BTC's own 52-week range, so I
cannot convert that into a definitive tracking-error claim — **but the fact that
the check can't be closed is itself the finding.** For a genuine spot ETP, it would
be trivial.

**Step 1 — five independent views.**

**The Contrarian.** ACTION: **Reject.** CONVICTION: **High.** MAIN REASONING: The
entire trade is a fee arbitrage — 2.5%/yr → 0.15%/yr, about 330 SEK/yr on 15,366
SEK. That arbitrage only exists if the exposure is like-for-like. If BITC is a
strategy product, you have not saved a fee; you have silently swapped the asset,
and 330 SEK/yr is a rounding error next to that. KEY RISKS: I could be wrong and it
really is spot-backed at a genuinely great price near its low. WHAT WOULD CHANGE MY
MIND: the prospectus or holdings page showing physical BTC in custody, plus a
tracking-difference series against spot.

**First Principles.** ACTION: **Reject.** CONVICTION: **High.** MAIN REASONING:
Strip the framing. The real question is not "is BITC good" — it is "what is the
cheapest legally-available wrapper for BTC exposure inside a Swedish ISK." BITC is
a **US-domiciled, US-listed ETF**. Under MiFID II/PRIIPs, EU retail investors
generally cannot buy US-domiciled ETFs at all, because those funds don't publish a
KID (Key Information Document) in an EU language. This is why you can buy Apple
shares at Avanza but not VOO. That disqualifies the vehicle *before* any analysis
of what it holds. KEY RISKS: Avanza may offer it under some classification, or
there may be an EU-domiciled sibling with the same strategy. WHAT WOULD CHANGE MY
MIND: an Avanza order page showing it tradeable in a retail ISK.

**The Expansionist.** ACTION: **Reject BITC / Buy a verified physical BTC ETP.**
CONVICTION: **Medium.** MAIN REASONING: Ignore the SEK constraint. The
maximum-upside version of "cheap BTC exposure inside the ISK" is a
**physically-backed, EU/Nordic-domiciled ETP** at 0.15-0.5%/yr — several exist,
they capture essentially the same fee saving, they are actually purchasable, and
they carry no structure ambiguity. The maximum version therefore points *away from*
BITC, not toward it. That is unusual and worth noticing: normally the maximal and
modest versions of a call diverge. KEY RISKS: physical ETPs still carry issuer /
custody / counterparty risk, which self-custody would not. WHAT WOULD CHANGE MY
MIND: nothing about BITC — I need a verified Nordic ticker and fee (S1).

**The Outsider.** ACTION: **Reject.** CONVICTION: **High.** MAIN REASONING:
Described cold: "I sold my bitcoin fund this morning and want to put the money into
a US fund whose name I've read but whose holdings I haven't checked, inside a
Swedish tax account I haven't confirmed can hold it, three days before a central
bank decision." Each of those four clauses would independently give a careful
person pause. KEY RISKS: doing nothing also costs something — cash earns nothing.
WHAT WOULD CHANGE MY MIND: a one-page fact sheet showing what it actually holds.

**The Executor.** ACTION: **Watch (pending a 60-second check).** CONVICTION:
**Medium.** MAIN REASONING: This is not a research project. Monday morning: log
into Avanza, search "BITC". If it isn't tradeable, the question is closed in one
minute. If it is, open the faktablad/KID and read the first line — it will say
whether it holds bitcoin or a strategy. Meanwhile put the 2,513 SEK into Avanza
Global so the cash isn't wholly idle while this resolves. KEY RISKS: the check gets
postponed and the cash sits, which this system has watched happen twice. WHAT WOULD
CHANGE MY MIND: the check itself.

**Step 2 — the Chairman.**

The disagreement that matters is not Reject-vs-Watch (four to one). It is **which
disqualifier binds first**, and the answer changes what you do next.

First Principles has the faster disqualifier: if a US-domiciled ETF simply isn't
purchasable in a Swedish retail ISK, the structure question never arises. That is
almost certainly the operative fact — and the Executor is right that it costs sixty
seconds to confirm. But I will not rest the call on it, for two reasons: it is
regulatory knowledge rather than something this sweep fetched, and if it were the
only objection, a confirmation that Avanza *does* offer it would flip the call
straight to Buy. It shouldn't.

**So the binding reason is the Contrarian's, and it is the one I weight.** The
whole justification for this trade is a fee saving of roughly 330 SEK/yr. That
number is only meaningful if you are buying the same asset in a cheaper wrapper. A
"Trend / Bitcoin / Treasury Strategy" product is, by its own name, something else —
a rotational or partly-Treasury-backed strategy whose returns can diverge from
bitcoin's by far more than 2.35 percentage points a year, in either direction. **You
would be optimizing the small number while unknowingly changing the big one.** That
is a category error, and it is exactly the failure this system exists to catch.

The Outsider's timing point is real but secondary — I address it in Timing
collisions rather than letting it carry the call.

I am also rejecting, on the record, the fallback the portfolio agent named for this
capital: **"if BITC turns out unbuyable, default to more ETH (self-custody)."** No.
P1 (ETH cost basis) is still open, which means you cannot compute the tax on any
future disposal, and adding units changes an average cost basis you do not have —
making a solvable record-keeping problem permanently harder. Every ETH disposal is
a 30% K4 event outside any wrapper, including token swaps. Adding to self-custody
ETH is the worst of the three available options, not the fallback.

```
FINAL ACTION: Reject
CONVICTION: High
WHY: The trade's entire justification is a ~330 SEK/yr fee saving that only
     exists if the exposure is like-for-like BTC. The ticker's own name
     ("TRND BITCN TRSR STRGY") describes a strategy product, not a spot
     holder, and this sweep has zero holdings/structure data to confirm
     otherwise — weighting the Contrarian, whose objection survives even if
     the wrapper question resolves in BITC's favour. First Principles'
     MiFID II/PRIIPs point (US-domiciled ETFs are generally unavailable to
     EU retail, which is why you can buy US *stocks* at Avanza but not US
     *ETFs*) is likely the faster disqualifier and is checkable in one
     minute, but the call does not depend on it. The Expansionist matters
     too: the maximum-upside version of this idea is a physically-backed
     EU/Nordic ETP, which points away from BITC rather than toward it —
     when the ambitious and the modest versions of a call agree, that is
     usually the tell.
KEY RISKS / BREAK CONDITION: This flips to a fresh Buy evaluation if BOTH
     (a) the prospectus/holdings page confirms physical BTC in custody with
     a stated tracking mechanism, AND (b) Avanza shows it tradeable inside
     a retail ISK. Either alone is insufficient. The 0.15%/yr fee is
     user-reported, not fetched — verify it in the same pass.
HORIZON: Medium (6mo-3y). This is a valuation-and-vehicle entry call, the
     bucket `valuation`/`thesis-review` own — not a tactical trade, and not
     a structural multi-year compounding case.
```

**Execution note:** capital is not the constraint here. 15,366 SEK is confirmed
free in the ISK this sweep (verified against this sweep's own portfolio-agent
output, not carried from a prior memo). The constraint is that no verified vehicle
exists — which is **S1**, open for weeks and now the single thing blocking a
5.9pp allocation gap.

### Call 2 — Deploy the 15,366 SEK: 12,853 earmarked for crypto with a dated default, 2,513 to equity now

**Contrarian:** Route the whole 15,366 to Avanza Global and be done. Crypto is
5.9pp under target only because you *chose* to sell it this morning; re-buying
within days is a round trip with a gap, and macro says the regime is actively
hostile to crypto. Also — `profit_recycling_rule` says high-risk-tier realizations
default to the secure tier. On the gross-proceeds reading you already agreed to,
the rule says all of it goes to equity.

**First Principles:** Two rules are colliding and nobody has noticed. The adopted
target says hold 10% crypto. The recycling rule says crypto proceeds go to the
secure tier. Applied to a *full* sale, the recycling rule mechanically guarantees
you can never hold the target again. One of them has to yield, and the honest
reading is: **the target governs sizing; the recycling rule governs what happens to
surplus above target.** Restoring 4.13% → 10% is target compliance, not compounding
within the risky tier.

**Expansionist:** Ignore the constraint. The maximal version is to close the
*whole* 38,206 SEK equity gap and the whole 12,853 SEK crypto gap at once — you
have 45,810 SEK of cash across accounts. You can't, because 11,364 is owed to
Skatteverket and 14,080 is stuck in PayPal at 4%. Which is a reminder that P3's
execution is worth more than this entire debate.

**Outsider:** You have 15,366 kronor sitting in an account earning nothing, after
selling something this morning. The obvious thing is to put it back to work in
something you've already decided you want to own. The only reason not to is that
you haven't found the right container yet.

**Executor:** Monday: buy 2,513 SEK of Avanza Global. Leave 12,853 in ISK cash with
a note. Spend twenty minutes on Avanza finding a physically-backed BTC ETP —
Virtune, Valour, XBT Provider, CoinShares, Bitwise all list Nordic products — write
down ticker and TER. If nothing is confirmed by 2026-09-03, buy Avanza Global with
it.

**Chairman.** The Contrarian's recycling-rule objection is the strongest argument
here and it deserves a real answer, not a dismissal. **First Principles' resolution
is the one I take:** on a full sale, the gross-proceeds reading of
`profit_recycling_rule` would permanently prevent you from ever holding your own
adopted 10% crypto target — an outcome you never decided and would not endorse if
stated plainly. That is a genuine internal contradiction between two of your own
written instructions, and it goes to Open decisions as **D4, reopened.**
`OPEN_ITEMS.md` currently calls D4 "practically overtaken" by the full sale. The
opposite is true: the full sale makes the gross-vs-realized-gain difference 15,366
SEK vs 3,266 SEK, the largest it has ever been.

On the market-timing objection, I take **macro-regime at its own word**, which
pre-empted this exactly: *"If the user is doing a like-for-like swap — certificate
proceeds → cheaper vehicle, same BTC exposure, no size increase — the regime is
irrelevant to that decision. If any part of it is sizing UP crypto exposure on a
'good entry' read, that's the piece this agent flags as unsupported."* Restoring to
a written target is the first case, not the second. I am not claiming Fear & Greed
31 is an entry signal — macro is explicit that it is moderate fear, not
capitulation, and this system has no short-term timing edge.

The dated default exists because idle ISK cash going stale is a **documented**
failure mode here, not a hypothetical — twice (2026-08-10, 2026-08-11).

```
ACTION: ADD (equity 2,513 SEK now) + WATCH-with-hard-default (12,853 SEK earmark)
POSITION: Avanza ISK cash 20,366 SEK carried, of which only 15,366 SEK is
          traceable (see Open actions). Crypto 9,029.46 SEK = 4.13% of the
          218,826 SEK full portfolio; equity 147,795.65 SEK = 67.55%
TARGET: Crypto back to 10% (~21,883 SEK, a 12,853 SEK gap) via a verified
        physically-backed BTC ETP purchasable in the ISK. Equity toward 85%
        (~186,002 SEK, a 38,206 SEK gap) with everything else
REASON: (1) Cash at 20.93% vs a 5% target is now the largest single deviation
        on the scorecard, and cash drag is certain while the crypto
        underweight costs nothing measurable; (2) the 10% crypto target is
        adopted and written into portfolio.json — restoring it is compliance,
        not a market call, and macro's own framing exempts a like-for-like
        restore from its regime warning; (3) no purchasable crypto vehicle
        exists this week (BITC rejected, ETH frozen on P1, S1 unresolved), so
        the earmark cannot be spent even if it should be.
THESIS STATUS: n/a — allocation, not a holding. The crypto *conviction* sits
        in ETH (INTACT, 3y+, your own stated view) and is untouched.
        Flagged: OPEN_ITEMS.md P5 still says "ETH has no thesis after 12+
        sweeps," but portfolio.json carries a full structured thesis dated
        2026-08-12 in your own words. Those two files disagree; portfolio.json
        is authoritative and P5's text is stale. The no-adds freeze on ETH
        still holds — on P1 (cost basis), not on thesis grounds.
WHAT CHANGED: The full sale (not the recommended 1-unit trim) converted a fee
        problem into an allocation hole, and converted a like-for-like swap
        into a genuine re-entry decision.
BREAK CONDITION: If no verified physically-backed BTC ETP is confirmed
        purchasable on Avanza inside the ISK by the 2026-09-03 sweep, the
        12,853 SEK earmark converts to Avanza Global automatically and the
        crypto target is formally revisited rather than left silently unmet.
CONFIDENCE: High on deploying the cash / Medium on the crypto split (rests on
        D4's unresolved reading, which I have taken a position on rather than
        deferred)
HORIZON: Long (allocation — lever 3, `portfolio`'s own bucket)
```

**Capital-availability check.** Verified against **this sweep's** portfolio-agent
output, not a carried figure: Avanza ISK cash is 20,366 SEK, of which **15,366 SEK
traces cleanly** to the 6 × 2,561 SEK sale from a confirmed-zero prior balance. The
call is sized to the traceable 15,366 only. The extra 5,000 is excluded until
verified — see Open actions.

### Call 3 — Buy 3 shares of AstraZeneca with the external 5,000 SEK

**Contrarian:** AZN just fell 2.2% today and is at a 52-week-range low for a
reason — the market is repricing something you can't see from a P/E screen. "Price
down, thesis intact" is what every value trap looks like from the inside, and you
already own 5 shares; adding is doubling down on a position that has gone against
you.

**First Principles:** The question is not "is AZN cheap." It is "given 5,000 SEK
of genuinely free money, what single purchase most improves this portfolio." The
portfolio's named defects are: too much cash, too much industrial cycle, no
verified crypto vehicle. AZN fixes two of the three in one order.

**Expansionist:** Ignore the constraint and the maximum version is a materially
larger healthcare/defensive sleeve — AZN plus NOVO-B.CO, taking the defensive
block from 3.4% to something that actually counterweights 65.5% industrials. Same
direction as the modest version, just more of it. That is a contribution-plan
question, not a this-week question.

**Outsider:** A company whose revenue has risen four years running, whose margins
are unchanged, is now cheaper than when you bought it, and it is the only one of
your seven stocks that isn't near its yearly high. You have 5,000 kronor. This is
not a hard question.

**Executor:** 3 shares at ~1,480 = ~4,440 SEK. Move the 5,000 to the ISK, place a
limit order, put the ~560 change into Avanza Global. Earnings already reported
2026-07-27, so no print to trip over.

**Chairman.** The Contrarian's objection is the only one worth time, and it is
answerable rather than dismissible. "Price down, thesis intact" *is* what a value
trap looks like from the inside — the distinguishing test is whether the
fundamentals moved with the price. Here they did not, and this system has the
receipts: revenue **+6.4%**, four consecutive rising fiscal years (44.4 → 45.8 →
54.1 → 58.7 bn), operating margin 23.5%, PEG 1.34, dividend payout 47.4%. A -2.2%
intraday move against that record is price, not information. If the fundamentals
turn, the holding's own recorded break conditions fire and this becomes a different
conversation — that is what break conditions are for.

The decisive point is the First Principles one, and it is a *portfolio* argument
rather than a stock argument: this is the only available purchase that improves two
ACT-rated dimensions at once. Every alternative worsens at least one.

```
ACTION: ADD
POSITION: AZN.ST 5 shares, 7,400 SEK = 3.38% of the 218,826 SEK portfolio.
          Largest true single-company position in the book
TARGET: 8 shares, ~11,840 SEK = ~5.4% — inside the 15% single-position cap and
        inside the "normal" 3-8% band
REASON: (1) Only holding with no dissent across valuation (Cheap/Fair, PEG
        1.34), thesis-review (INTACT, "strongest mispricing-not-deterioration
        case in the book"), macro (beta 0.211, defensive, right side of the
        regime) and portfolio (reduces the ACT-rated industrials sleeve);
        (2) now trading below your own 1,509.70 cost basis at the 20.5th
        percentile of its 52-week range on unchanged fundamentals — a better
        entry than the one already taken; (3) the money is external and fresh,
        so `profit_recycling_rule` does not govern it and no tax event or
        wrapper question arises.
THESIS STATUS: INTACT. portfolio.json and thesis-review agree — checked
        directly, no silent pick required.
WHAT CHANGED: AZN dropped from ~32% to 20.5% of its 52-week range today,
        intraday, moving below cost basis while every fundamental input held.
        The morning memo said "if a contribution lands before next sweep,
        AZN.ST is where the medium-tier krona goes." One landed.
BREAK CONDITION: The holding's own recorded conditions — revenue growth or
        margins deteriorate structurally; the dividend is cut; or it re-rates
        to a premium indistinguishable from the growth assets it is meant to
        diversify against. None triggered.
CONFIDENCE: High
HORIZON: Medium (6mo-3y) for the entry; the holding's own stated horizon is
        3-5 years
```

**Capital-availability check.** You stated this session that 5,000 SEK is available
right now in a separate external account. That is a direct user statement, which
outranks any file. **One caveat that matters:** it is coincidentally the same amount
as the unexplained +5,000 SEK now sitting in the ISK cash line. If those turn out to
be the same money, this call is funded and Call 2's earmark shrinks to 12,853 SEK
from a 15,366 base rather than 20,366 — which is exactly how Call 2 is already
sized. Either way this call stands; verify before assuming you have both.

### Call 4 — The P6 review is done. Hold all three, no adds, ABB is first in line to be sold.

**Contrarian:** ABB scored 51/100 with a live insider-selling cluster and the
richest multiple in the book. You now have a vetted alternative for the first time.
Sell it and buy AZN. Waiting for confirmation is how you watch a signal play out
from inside the position.

**First Principles:** A "rotation candidate" only means something if there is
something to rotate *into* and capital that needs a home. This week capital does
need a home. But the holding's own recorded break condition — written this morning,
from real data — sets the bar at the insider pattern *continuing into the next FI
pull*. This is the first pull. Overriding a break condition on its first data point
is the failure the condition exists to prevent.

**Expansionist:** The maximum version isn't selling 3,886 SEK of ABB. It is
noticing that all three of these plus Volvo are one bet — the global capex cycle —
sized at 65.5% of your stock sleeve, and that the fix is a *contribution policy*
(everything new goes non-industrial until the sleeve is under 45%), not a 1.8%
trade.

**Outsider:** You bought this two weeks ago. You then studied it and found it was
the weakest of the three you bought. Selling it immediately would be admitting the
study should have come first — which it should have. But churning a two-week-old
position on one executive's share sales is its own kind of mistake.

**Executor:** No trades. Direct every new krona away from industrials. Re-pull the
FI insider register on ABB before the 2026-09-03 sweep.

**Chairman.** **HOLD all three, no adds, and arm the reduce trigger with a date.**

The Contrarian is right that the morning memo's premise ("no vetted alternative
exists") is dead — the review ran, AZN is demonstrably better on every lens (PEG
1.34 vs 2.71, 20.5th vs 80.2nd percentile, INTACT vs WEAKENING, beta 0.211 vs
1.011, and it reduces rather than adds to the concentration). That is genuinely new
and I am not going to bury it.

What stops it becoming a sale this week is **First Principles' point, which is a
discipline point rather than a view about ABB**: `ABB.ST`'s own `break_conditions`,
written this morning from the actual FI data, say the insider pattern hardens from
"rotation candidate" to "active reduce signal" *if it continues or grows into the
next FI data pull.* This is that pull. Firing on the first observation of a
condition explicitly written to require a second is precisely the kind of drift
this system's structured-thesis schema exists to prevent — and I would rather be
consistent about that than right about one 3,886 SEK position.

Two things I will not soften. **ABB is first in line.** The moment capital needs a
home from any source other than new money, ABB is where it comes from — not
ATCO-B (62/100), not ALFA (63/100, 10-of-10 insider buys, zero disposals). And
**the Expansionist's reframe is the real finding**: this is one bet placed four
times at 65.5% of the sleeve, and it is fixed with contribution policy, not with a
1.8% trade.

```
ACTION: HOLD (ATCO-B.ST, ALFA.ST, ABB.ST) — no adds, no trims
POSITION: ATCO-B 4,891.05 (2.23%), ALFA 5,014.80 (2.29%), ABB 3,886.40 (1.78%)
          of the 218,826 SEK portfolio. Industrials 65.5% of the stock sleeve
TARGET: Industrials below 45% of the stock sleeve, reached by growing the
        sleeve elsewhere (AZN.ST, Avanza Global) rather than by selling these
REASON: (1) All three are quality businesses at expensive prices (PEG 2.38 /
        2.86 / 2.71) — the P6 review's own conclusion is "do not add at
        current valuations," which I adopt unchanged; (2) ABB's recorded
        break condition requires the insider-selling pattern to continue into
        the *next* FI pull, and this is the first — firing early would
        override a condition written from real data hours ago; (3) the
        binding constraint is concentration, which is a fact about the
        portfolio and is correctable with new money rather than sales.
THESIS STATUS: WEAKENING on all three. portfolio.json (updated today by the
        review) and thesis-review agree exactly — no disagreement to report.
WHAT CHANGED: The review that had been overdue for seven sweeps actually ran,
        with fresh Yahoo fundamentals and a same-day Finansinspektionen
        insider pull. It resolved the ranking (ALFA 63 > ATCO-B 62 > ABB 51)
        and surfaced two genuinely new facts: a currency-unit error in
        Yahoo's raw P/S and P/B for ABB, and an insider-selling cluster from
        a senior ABB executive (~48,800 shares / ~CHF 3.85M across three
        disposals, 07-31 to 08-14).
BREAK CONDITION: Each holding's own recorded condition, restated: a materially
        better-positioned Nordic-industrial alternative surfacing; the
        industrials concentration needing correction; ATCO-B's ttm revenue
        recovery (+9.1%) failing to appear next fiscal quarter; ALFA's
        10-of-10 insider-buy pattern breaking with a disposal; ABB's
        insider-selling cluster continuing or growing into the next FI pull —
        that last one hardens ABB to an active REDUCE.
CONFIDENCE: High
HORIZON: Medium (6mo-3y)
```

**On VOLV-B.ST, kept separate because its status differs:** TOO_EARLY, 340.20 vs a
367.50 cost basis (-7.4%) and below the board member's ~360 SEK insider buy. Its
own break condition is "3+ months with no sign of the expected earnings recovery";
it is at ~2 weeks. Revenue growth has flipped positive (+2.7% vs the -13% cited at
purchase), forward P/E 13.7, PEG 1.42, analyst "buy." No action, and no pretending
two weeks is evidence.

### Call 5 — The backtest cleared the target. Keep 85/10/5/0 — and read the result honestly.

**Contrarian:** A 7.2-year window starting 2019-06 that produces a **15.0% CAGR** is
telling you about the window, not the allocation. That is roughly double a
realistic long-run global equity return. The 2022 bear was shallow and fast; 2008
was -50%+ over eighteen months and is structurally excluded because VWCE.DE didn't
exist. "Clears -30%" on the kindest decade in modern market history is not
validation.

**First Principles:** Two facts, and they should not merge. (1) The estimate that
said the target breached was a sum-of-worst-cases with implicit perfect
correlation — a method engineered to breach any threshold. (2) A real
correlation-aware backtest now says -19.95%. The second supersedes the first as
evidence. Neither tells you what a 2008 does to this book.

**Expansionist:** Ignore the constraint. If the target genuinely draws down only
-20% in the worst tested year, the honest question flips: is 85/10/5/0 *too
conservative* for a soft 3-7 year horizon with rising income? That is a real
conversation, and it is the one the number actually opens.

**Outsider:** You wrote down a limit, built a portfolio, and finally checked. It
passed. The sensible response is to keep the plan and note what the test didn't
cover.

**Executor:** Nothing to trade. Mark S5 resolved. Keep 85/10/5/0. Note that a
2008-shaped window remains untested and needs fixed `--start`/`--end` support.

**Chairman.** **NO ACTION — keep the adopted 85/10/5/0 target.** S5 is answered and
should close.

I am giving the Contrarian more weight than the verdict implies, and it changes the
*label* rather than the decision. The scorecard row moves UNKNOWN → **OK
(provisional)**, not UNKNOWN → validated, on three specific grounds. First, the
window: 2019-06 to 2026-08 is bounded by VWCE.DE's inception and excludes 2008
entirely; a 15.0% CAGR is the tell that the period was unusually generous. Second,
no fees, taxes or FX are modelled. Third — the detail most likely to be skipped —
**the target's max drawdown (-19.95%) equals its worst rolling 12 months, meaning
the entire drawdown occurred inside a single year.** A fast, sharp shock is
behaviourally the hardest kind to sit through, and it is a thinner margin against
-30% than the headline number suggests.

The Expansionist's inversion is the genuinely interesting output and I am flagging
it rather than acting on it: this result opens a real question about whether -30%
is a live constraint or a number written down once. That is your call, not the
system's, and it goes to Open decisions.

Translate it into money, which is the only form that matters: **-20% on today's
investable capital is about 193k becoming about 155k — and not selling.** If that
sentence is uncomfortable, the target is wrong regardless of what the backtest says.

```
ACTION: NO ACTION (target unchanged at equity 85 / crypto 10 / cash 5 / FI 0)
POSITION: Current mix max drawdown -14.6%, worst 12m -12.45%, vol 11.8%.
          Adopted target -19.95% max DD, worst 12m -19.95%, vol 13.9%.
          Alternative 82/6/12/0: -16.14%. Benchmark VWCE.DE alone: -19.14%.
          Stated tolerance -30% (~58,015 SEK on 193,382 SEK investable)
TARGET: Unchanged. Neither of the morning memo's two proposed alternatives
        adopted — both were answers to a question that has now been answered
        differently.
REASON: (1) The first real backtest in this system's history clears the
        stated tolerance on both the current mix and the target, and
        supersedes the illustrative sum-of-worst-cases that said otherwise;
        (2) the morning memo's Option 1 contradicted your explicit 2026-07-22
        instruction and Option 2 breached the same tolerance it was meant to
        fix — both are moot; (3) changing an adopted target on evidence that
        has just been reversed would be motion, not progress.
THESIS STATUS: n/a — allocation governance
WHAT CHANGED: `backtest` ran for the first time ever, over 86 months, after a
        real bug fix (its yfinance client failed on this network with the
        same curl_cffi TLS-fingerprint issue as fetch_market_data.py;
        rewritten against Yahoo's v8 chart endpoint via urllib and validated
        against the script's own known-good example before any new result was
        trusted). Result: -14.6% / -19.95% vs the morning's -42.3% / -45.75%.
BREAK CONDITION: A crisis-window backtest covering 2008 (needs fixed
        --start/--end support, V2 Roadmap Phase 6) returning worse than -30%
        — at which point the target and the tolerance genuinely conflict and
        one must change deliberately, with your input.
CONFIDENCE: Medium. High that the target should not change today; Medium on
        the drawdown number itself, capped by a single 7.2-year path over an
        unusually generous window with no 2008 in it.
HORIZON: Long
```

---

## Where the agents disagreed

**1. Portfolio says the crypto fallback is "more ETH." I reject that outright.**
The portfolio agent's rebalancing recommendation states that if BITC turns out
unbuyable, the earmarked cash "defaults to more ETH (self-custody) or stays in cash
pending a different certificate/ETF candidate." Those two options are not
equivalent and should not have been listed side by side. Adding to self-custody ETH
while **P1 (cost basis) is open** makes an already-unsolvable tax position worse:
you cannot compute the gain on any future disposal, and each new purchase changes
an average cost basis you do not possess. Swedish crypto tax treats every
disposal — including token swaps — as a 30% K4 event outside any wrapper.
**Resolution: cash, not ETH.** Confidence: High. This is the clearest agent error
this sweep and it would have been expensive.

**2. `OPEN_ITEMS.md` and `portfolio.json` disagree about whether ETH has a
thesis.** P5 says "ETH still has no thesis after 12+ sweeps" and imposes a
no-adds freeze "until either a thesis is written or P1 closes."
`portfolio.json` carries a full structured thesis for `ethereum` dated 2026-08-12
in your own words, status INTACT. **portfolio.json is authoritative and P5's text
is stale** — but the practical answer is unchanged, because the freeze survives on
the P1 (cost basis) limb regardless. Flagged so P5 gets corrected rather than
quietly relied on.

**3. Valuation and macro-regime agree on BITC's *conclusion* but for
non-overlapping reasons, and neither reason is sufficient alone.** Valuation says
the structure is unconfirmed and it may not be a spot tracker. Macro says the
regime is a headwind but explicitly exempts a like-for-like swap from that
warning — *"the regime is irrelevant to that decision."* Read together they do
**not** produce "wait for a better crypto entry." They produce something more
precise: **the vehicle is the problem, not the timing.** That distinction is what
makes Call 2's earmark (restore the target, once a vehicle exists) different from
"stay out of crypto for now," and it is the kind of thing that gets averaged away
if you only read the verdicts.

**4. The backtest's base is 188,839 SEK (investable-only), but D3 pinned the
full-portfolio convention (218,826 SEK) hours earlier.** This is the S12 failure
class recurring on the same day it was supposedly closed. It is *defensible* — you
cannot backtest a tax reserve or a PayPal balance — but `definitions.json`'s wording
says the convention governs "any other 'percent of investable capital' figure,"
which reads broader than intended. **Do not compare the backtest's SEK figures
against the scorecard's percentages without noticing they use different bases.** The
fix is a one-line clarification in `definitions.json` distinguishing *allocation
percentages* (full portfolio) from *risk-simulation base* (investable only). Flagged
for `meta`; not Council's file to edit.

**5. The Excel import wrote a +5,000 SEK cash delta that no one asked for, and it
did not appear in `flags`.** `portfolio_deltas` reads `CASH_SEK (avanza-isk):
quantity 15366 -> 20366 (from Excel)`. The 15,366 is user-confirmed from today's
sale; the extra 5,000 has no documented source. This is the **second confirmed
instance of S9(c)** — an Excel figure conflicting with a direct user statement,
applied as a delta, and invisible to `claude_excel_prompt.txt` because it never
became a flag. The first instance funded a wrong recommendation on 2026-08-11.
Treated here as unverified: every call in this memo is sized against 15,366, not
20,366.

**Where they agree, stated because it is uncommon.** **AstraZeneca has no dissent
across four lenses** — valuation (Cheap/Fair, "the strongest mispricing-not-
deterioration case in the book"), thesis-review (INTACT, only clean status among the
recent buys), macro-regime (beta 0.211, defensive, right side of the regime),
portfolio (reduces the ACT-rated industrials concentration). Four lenses, zero
tension, and the price fell today. That combination is why Call 3 is the only High
confidence buy in this memo.

---

## Broken theses requiring a decision

**None broken.** From thesis-review, unsoftened:

- **WEAKENING (5):** SHB-A.ST, INVE-A.ST, ATCO-B.ST, ALFA.ST, ABB.ST. No status
  changed versus stored data this sweep — the P6 review *confirmed* the existing
  reads with fresher numbers rather than moving any of them.
- **INTACT (4):** AZN.ST, Avanza Auto 3, Avanza Global, ethereum.
- **TOO_EARLY (1):** VOLV-B.ST — ~2 weeks held against a 3-month break condition.
- **CLOSED (1):** COIN-XBT.ST — sold in full, recorded, +27.0% realized, tax-free.
- **Status agreement check:** `portfolio.json` and thesis-review agree on **every**
  holding this sweep, including the three whose thesis fields were rewritten hours
  earlier by the P6 review. No silent picking required anywhere in this memo.
- **The standing cross-holding pattern, carried unsoftened:** five of seven equity
  holdings still share the identical thin "Swedish track record" non-differentiated
  rationale, and four of those five sit at 79.6-95.7% of their 52-week range
  simultaneously. That is one bet placed five times, and it remains a
  portfolio-level construction problem rather than five independent stories.

---

## Rebalancing actions

From the portfolio agent, with my amendments marked.

| # | Action | SEK | Tax | Status |
|---|---|---|---|---|
| 1 | **Buy Avanza Global** with part of the traceable sale proceeds | **2,513** | Tax-free (ISK) | **Execute this week** |
| 2 | **Hold 12,853 SEK as an earmarked ISK cash reserve** for a verified physically-backed BTC ETP — auto-converts to Avanza Global on **2026-09-03** if no ticker is confirmed | **12,853** | n/a | **Blocked on S1** — the earmark is the mechanism, not the delay |
| 3 | **Move the external 5,000 SEK into the ISK; buy 3 shares AZN.ST (~4,440), remainder to Avanza Global** | **5,000** | No tax event on the transfer | **Execute this week** |
| 4 | Execute the P3 PayPal conversion (Option A, decided today) and route the SEK into the ISK | 14,079.79 gross / ~13,517 net at the 4% worst case | No tax event | **Decided — pending your execution** |
| 5 | Buy BITC with the proceeds | 15,366 | — | **Not recommended — Call 1** |
| 6 | Default the crypto earmark to more self-custody ETH | 12,853 | Uncomputable (30% K4, no cost basis) | **Do not execute — P1 blocks the tax math.** Portfolio agent listed this; I reject it |
| 7 | Treat the +5,000 SEK Excel cash delta as deployable | 5,000 | — | **Not until verified against a live Avanza statement** |

**Net effect if lines 1 and 3 execute** (the realistic case this week): equity rises
by ~7,513 SEK to ~155,309 SEK; the equity gap narrows from -17.5pp to about
-13.6pp; investable cash falls from 20,366 to 12,853 SEK, all of it earmarked with
a date attached. Crypto stays at 4.13% until a vehicle exists — deliberately, and
visibly, rather than by neglect.

---

## Confidence and horizon per call

| Call | Confidence | Horizon | What caps it |
|---|---|---|---|
| 1 — Reject BITC | **High** | Medium | Nothing caps the reject: the fee case requires like-for-like exposure that is unconfirmed, and the wrapper is likely unavailable to EU retail. What *is* uncertain is whether a verified alternative exists — that's S1, not this call |
| 2 — Deploy 15,366: 2,513 equity now, 12,853 earmarked | **High** on deploying / **Medium** on the split | Long | The split rests on my reading of D4 (target governs sizing, recycling rule governs surplus) — a position I've taken rather than deferred, and one you can overrule |
| 3 — Buy 3 shares AZN.ST | **High** | Medium | Four-lens agreement is the strongest evidence base in this memo. Capped only by the possibility that today's -2.2% reflects information not yet in the fundamentals |
| 4 — Hold all three P6 industrials, ABB first in line | **High** | Medium | The review is fresh and complete (6/6 coverage on all three). Capped by S4: Swedish CPI is 8 months stale, so macro cannot regime-grade Swedish industrials — a reason for caution, not for action |
| 5 — Keep 85/10/5/0 | **Medium** | Long | One 7.2-year path, no 2008, no fees/taxes/FX, and a 15.0% CAGR that flags the window as generous. Enough to keep the target; not enough to call it validated |

No Short-horizon calls this sweep, so the 10% tactical cap and the never-High-
confidence rule are not engaged.

---

## Cost of being wrong

| Call | If wrong, realistic downside in SEK | Recoverable? |
|---|---|---|
| 1 — Reject BITC | If BITC really is spot-backed *and* ISK-purchasable: ~330 SEK/yr of forgone fee saving versus whatever alternative you end up using, plus a few weeks of crypto underexposure on 12,853 SEK. If BTC rose 30% during the delay, ~3,856 SEK of forgone gain | **Yes, fully.** The reject costs a delay, not a position. The mirror error — buying a strategy product believing it is spot BTC — is unbounded in the sense that you would not know what you owned |
| 2 — Deploy 15,366 as split | If crypto is restored and BTC falls 30%: **-3,856 SEK** on the 12,853 earmark. If the earmark instead defaults to equity and BTC doubles: ~12,853 SEK of forgone upside | **Yes.** The earmark sits inside the 10% high-risk tier you have explicitly said you can afford to lose more of. Worst case is a documented, dated, visible decision rather than drift |
| 3 — Buy 3 shares AZN.ST | AZN falls another 20% from here: **-888 SEK** on the new 4,440, or -1,480 SEK across the enlarged 8-share position | **Yes, trivially.** 0.4% of the portfolio. The larger risk is opportunity cost, and the alternative (Avanza Global) has a near-identical risk profile |
| 4 — Hold all three, don't sell ABB | ABB corrects 30% before the next FI pull: **-1,166 SEK**. All three industrials plus Volvo correct 30%: **-5,464 SEK**, 2.5% of the portfolio | **Yes**, over a 3-7y horizon. The mirror risk — selling three quality compounders near highs and watching them run — is similar in size, which is why the answer is hold-and-arm rather than sell |
| 5 — Keep 85/10/5/0 | If the backtest window flatters and a 2008-shaped event lands: **-30%+ on ~193,382 SEK = worse than -58,015 SEK**, beyond the stated tolerance | **Financially yes**, over a long horizon. **Behaviourally, this is the one that may not be** — exceeding a stated tolerance risks capitulating at the bottom. Cost of running the crisis-window test instead: zero once fixed dates are supported |

---

## Timing collisions

`calendar` ran this sweep. **One flag, and it touches exactly one recommendation.**

- **Riksbank rate decision + Monetary Policy Update: 2026-08-20 — three days away.**
  Flagged as a collision for any near-term crypto redeployment (BTC is
  policy-sensitive, and the certificate/ETP would be SEK-denominated against a
  USD-priced asset, so both the numerator and the SEK denominator move).
  **Assessment: this resolves itself.** Call 2's crypto earmark is blocked on
  finding a vehicle (S1), which will not happen before Friday, so the redeployment
  lands after the decision by construction rather than by choice. **No reason to
  hurry it before 08-20, and no reason to formally wait either** — the two effects
  are partially offsetting and ambiguous in sign, which is precisely why this
  system does not trade around central bank meetings.
- **AZN.ST (Call 3): no collision.** Already reported 2026-07-27. Its next print is
  well outside the window. Beta 0.211 means a Riksbank surprise is close to
  irrelevant to it.
- **Held-ticker earnings all 34-41 days out:** ABB 10-20, SHB-A 10-21, ATCO-B
  10-22, VOLV-B 10-23, ALFA 10-27. No holding under discussion this sweep has a
  print inside the window. FOMC 2026-09-15/16, outside every action.
- **Gap:** no forward earnings date exists for INVE-A.ST. Nothing is exposed —
  it carries no action this sweep.

---

## Open actions

Things you can just go do. Pulled from `/OPEN_ITEMS.md` by ID.

| ID | Action | Amount / detail | By when |
|---|---|---|---|
| **P4** | **Verify the +5,000 SEK ISK cash discrepancy against a live Avanza statement.** Only 15,366 SEK of the carried 20,366 traces to today's sale. It is coincidentally the same figure as your external 5,000 — confirm whether these are the same money before spending both | 5,000 SEK | **Before executing anything below** |
| **P4** | Buy 2,513 SEK of Avanza Global from the traceable proceeds | 2,513 SEK | This week |
| **P4 / S1** | **Find one physically-backed, EU/Nordic-domiciled BTC ETP purchasable on Avanza inside the ISK.** Write down ticker + TER + whether Avanza actually lists it. Virtune, Valour, XBT Provider, CoinShares and Bitwise all have Nordic-listed products; tickers must be read off Avanza, not guessed | — | **2026-09-03** — after that the 12,853 SEK earmark auto-converts to Avanza Global |
| **P4** | *Optional, 60 seconds:* search "BITC" on Avanza to confirm or kill the availability question outright | — | Whenever |
| — | Move the external 5,000 SEK into the ISK; buy 3 shares AZN.ST (~4,440), remainder to Avanza Global | 5,000 SEK | This week |
| **P3** | **Execute the decided PayPal conversion (Option A) and route the SEK to the ISK.** Decided today; nothing further to deliberate | 14,079.79 gross / ~563 SEK cost | Soon — it recurs every ~2 months at ~1,970-2,630 SEK/yr |
| **P1** | Dig up the ETH cost basis. It now blocks more than tax math — it is why "add more ETH" is off the table as a crypto fallback | — | Not urgent unless selling, but it is the cheapest open item to close |
| **P5** | Correct the stale P5 text: ETH's thesis was written 2026-08-12 and is in `portfolio.json`. The freeze stands on P1, not on the missing thesis | — | Bookkeeping |
| — | Fix the Excel items below | — | Before next sweep |

**Closed or closing this sweep:** P7 (ISK allowance confirmed at 300,000 SEK by
you), D3 (full-portfolio convention chosen by you, pinned in `definitions.json`),
P6 (`swedish-equity-review` run on all three, seven sweeps overdue, now done), P3
(decided — pending execution only), **S5** (real backtest run; `meta`'s call to move
it to closed, not Council's file to edit), and **P4's fee half** (the 2.5%
certificate is gone; only "replace with what" remains).

## Open decisions

Forks where the data does not pick a single answer. Each gets concrete options.

**D4, reopened — does `profit_recycling_rule` apply to gross proceeds or the
realized gain only?** `OPEN_ITEMS.md` says the full sale made this moot. The
opposite is true: the full sale makes the difference **15,366 SEK vs 3,265.98 SEK**,
the largest it has ever been, and it decides whether you ever hold your own 10%
crypto target again.
1. **Target governs sizing; the recycling rule governs surplus above target.**
   Restoring crypto from 4.13% to 10% is compliance, not compounding within the
   risky tier. Trade-off: requires reading the rule as narrower than its literal
   words. **Council's recommendation, and what Call 2 assumes.**
2. **Gross proceeds — all 15,366 SEK to the secure tier.** Trade-off: the literal
   reading, simplest to execute, one order — but it mechanically means crypto never
   returns to 10% after any full sale, which is an allocation decision made by a
   bookkeeping rule rather than by you.
3. **Realized gain only — 3,265.98 SEK to Avanza Global, 12,100 SEK free.**
   Trade-off: also literal ("money I *make*"), lands within ~750 SEK of Call 2's
   split anyway, but leaves the general question unresolved for the next trim.

**Is -30% still your real drawdown tolerance?** The backtest cleared it, which
paradoxically makes this *more* worth asking, not less. You have already explicitly
overridden the conservative allocation -30% implies ("The push of equity above 70%
is fine. I don't mind," 2026-07-22).
1. **Keep -30% and keep 85/10/5/0.** Trade-off: consistent, tested on one window,
   and the target sits comfortably inside it at -19.95%. **Recommended — this is
   Call 5.**
2. **Revise the tolerance upward deliberately** (e.g. -35%) to reflect the soft
   horizon and rising income. Trade-off: honest about your stated appetite, but it
   removes the only guardrail on the allocation, and no crisis-window test exists to
   tell you what the real tail looks like.
3. **Keep -30% but require a 2008-window test before the next target change.**
   Trade-off: strictly better information, but it is blocked on fixed
   `--start`/`--end` support in `scripts/backtest.py` (V2 Roadmap Phase 6).

**What happens to the crypto sleeve if no vehicle is found?** Call 2 attaches an
automatic default, but the underlying question is yours.
1. **Auto-convert the 12,853 SEK earmark to Avanza Global on 2026-09-03** and
   formally revise the crypto target downward to match reality. Trade-off: honest
   and prevents indefinite idle cash — but it is a permanent 6pp risk reduction
   arrived at by deadline rather than by decision. **This is what Call 2 does absent
   other instruction.**
2. **Keep the earmark open past 2026-09-03.** Trade-off: preserves the 10% target,
   at the documented cost that idle ISK cash in this portfolio has gone stale twice.
3. **Accept a Nordic BTC certificate at ~1%/yr rather than holding out for
   ~0.15%.** Trade-off: about 110 SEK/yr worse than the ideal on 12,853 SEK, but it
   is executable now and still cuts 1.5pp off the 2.5% you just exited.

---

## Excel data gaps

Sourced verbatim from `data/cache/excel_import/latest-summary.json` (generated
11:11 UTC this sweep), plus one conflict the script did not flag.

1. **`ATCO-B.ST`: P/E 2.05 is outside the 3-80 sanity range — treat as suspect,
   verify in Excel before using it.** *Not used anywhere in this memo* — valuation
   and the P6 review both ran on Yahoo's 33.3x. Same bad cell first caught
   2026-08-06; the sanity check is working, the underlying cell is still wrong.
   Refresh that cell's Stocks data type.
2. **`ALFA.ST` / `ATCO-B.ST` / `SHB-A.ST` / `VOLV-B.ST`: no 52-week range in
   Excel.** Confirmed data-provider gap for some Nordic-primary tickers, not a
   formula bug. No action available — the 52-week figures in the position report
   come from Yahoo. Do not chase these.
3. **Not in `flags`, and it should have been: the +5,000 SEK ISK cash delta.**
   `portfolio_deltas` reads `CASH_SEK (avanza-isk): quantity 15366 -> 20366 (from
   Excel)`. Only 15,366 traces to today's confirmed sale. Because this never became
   a flag, it also never reached `claude_excel_prompt.txt` — the exact gap S9(c)
   describes, now on its **second** confirmed instance. **Set the Avanza ISK cash
   cell to the figure on your live Avanza statement**, and treat the extra 5,000 as
   unverified until then.
4. **Twelve Watchlist tickers still carry a space instead of an exchange suffix**
   (e.g. `SEB A` → `SEB-A.ST`, `NOVO B` → `NOVO-B.CO`). Still unfetchable, still
   silently capping `scout`'s effective universe. Worth fixing now that you have
   asked for candidate ideas — it is the difference between screening 67 entries
   and screening 55.
5. **Add the five new watchlist names** from section 2d (MSCI, SNPS, ARM, SCCO,
   STL) to the Watchlist tab so they get screened next sweep rather than staying
   discretionary.

---

## Learning notes

- **"Fully BTC-backed" is a claim about a fund's *structure*, and structure is the
  one thing a price feed can never tell you.** Three different products can carry
  bitcoin in the name and behave completely differently: a **physically-backed ETP**
  holds actual BTC in custody and tracks spot almost exactly; a **futures/strategy
  fund** holds derivatives and can bleed value through roll costs or trend-following
  whipsaw even when spot goes sideways; and a **treasury-company fund** holds shares
  in businesses that own bitcoin, which adds equity risk, management decisions and
  leverage on top. BITC's name — "TRND BITCN TRSR STRGY" — reads as the second or
  third kind, not the first. The reason this mattered more than the fee arithmetic:
  the whole trade was justified by saving 2.35 percentage points a year, which is
  only a saving if you end up owning the same asset. **Optimizing the small number
  while unknowingly changing the big one is the most common way a "cost-cutting"
  trade destroys value.**
- **Why you can buy Apple at Avanza but generally can't buy a US-listed ETF.**
  Under EU rules (MiFID II / PRIIPs, in force since 2018), a fund sold to EU retail
  investors must publish a short standardised **KID** — Key Information Document —
  in a local language. US-domiciled ETFs publish a US prospectus instead and mostly
  haven't bothered producing KIDs, so European brokers block them for retail
  clients. Individual *shares* aren't caught by the rule, which is why the
  restriction feels arbitrary until you know the mechanism. The practical takeaway
  for your ISK: when a US ticker looks attractive, check whether it is a **company**
  or a **fund** first — it changes whether the question is even askable.
- **A backtest's window is part of its answer, and a suspiciously good CAGR is the
  tell.** This sweep's real backtest says the 85/10/5/0 target's worst drawdown was
  -19.95% — comfortably inside your -30% tolerance, and the opposite of the crude
  estimate it replaced. But it also reports a **15.0% annual return** over 7.2
  years, roughly double a realistic long-run global equity return. That is not good
  news about the allocation; it is information about the period, which began in
  2019 and excludes 2008 entirely. One more detail worth internalising: the target's
  **max drawdown equalled its worst rolling 12 months**, meaning the entire fall
  happened inside a single year. A slow -20% and a fast -20% are the same number and
  very different experiences — the fast one is what makes people sell. This is why
  the scorecard row moved to "OK (provisional)" rather than "validated."
- **Rebalancing back to a target is not the same thing as timing the market, and
  the distinction decides whether macro gets a vote.** Macro-regime flagged a real
  headwind for crypto — strong dollar, US policy rate well above the ECB's,
  sentiment at "Fear." It then drew the line itself: that warning applies to *sizing
  up* on a "good entry" read, and is *irrelevant* to restoring an allocation you
  already decided to hold. Restoring crypto from 4.13% to its written 10% is
  mechanical compliance with a target you adopted; deciding that now is a great
  moment to own more bitcoin would be a forecast, which this system doesn't make.
  Same trade, two different justifications, and only one of them is defensible on
  free data.
- **When two of your own written rules collide, the collision is the finding.**
  Your `profit_recycling_rule` says gains from the risky tier flow to the safe tier.
  Your target says hold 10% crypto. Applied to a *partial* trim those never touch —
  but applied to today's *full* sale, the recycling rule would mechanically prevent
  you from ever holding 10% crypto again. Nobody decided that; it would just happen.
  The general lesson is that rules written for one situation quietly acquire
  consequences in another, and the moment to notice is when a rule starts producing
  an outcome you would not have chosen if someone asked you directly.

---

*Portfolio valued this sweep at **218,826 SEK** (full-portfolio convention, per
`data/cache/definitions.json`) / **193,382 SEK** investable (Avanza ISK 184,352.65 +
ETH 9,029.46). Append a row to `data/valuations.csv` before closing the session —
note in it that this is the second memo of 2026-08-17 and supersedes the first.*
