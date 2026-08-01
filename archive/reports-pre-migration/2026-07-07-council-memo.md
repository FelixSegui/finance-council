# Council memo — 2026-07-07 — HB exit redeployment

*Structured synthesis of this system's own agents' outputs. Not investment
advice from a licensed advisor.*

Snapshot: `data/snapshots/20260707T153216.json`. The HB exit decision is
made (user, 2026-07-07) and is not re-litigated here. This memo answers
one question: **how to deploy the ~126,067 SEK net proceeds.**

---

## The answer (execute within days)

**Adopt reference_targets v1 AS AMENDED: equity start 45%, not 50%.**
Portfolio's own stress estimate of its 50/5 start is ≈ -30% — exactly the
stated tolerance, zero slack — and its glidepath anchor (T-5) is a guess,
because the deposit date is a range (3–7y), not a date. A hard-deadline
goal with a guessed anchor and an equity entry that valuation certifies as
unknowable does not start at full tolerance. The 50% column becomes
available the day the user confirms the deposit is ≥5 years out.

**Deployment of 126,067 SEK into Avanza ISK:**

| Sleeve | SEK | Constraint |
|---|---|---|
| Global equity index fund (unhedged) | 33,650 | broad global index, fee ≤0.20% |
| Nordic/European index fund (or SEK-hedged global) | 8,405 | fee ≤0.25% (≤0.30% if hedged class) |
| Short-duration SEK fixed income (kort räntefond) | 78,055 | fee ≤0.20% — at ~2% expected return, higher fees eat it |
| Cash in ISK (staging) | 5,957 | — |
| **Total** | **126,067** | |

Tax earmark **8,826.91 SEK → separate sparkonto OUTSIDE the ISK** (per
portfolio agent: near-1.75% sparkonto beats 0% ISK cash; never invest
money owed to Skatteverket; if it transits the ISK, withdraw same week).

Post-move whole portfolio (184,567 ex-earmark): equity 83,055 (45.0%),
FI 78,055 + 5,000 Swedbank-implied = 45.0%, cash 5,957 (3.2%), crypto
12,500 (6.8% — deliberately over the 5% target; dilute via contributions,
do not trigger a K4 sale with unknown basis).

Execution window: **both legs done by ~2026-07-21** or reinvestment lands
within 5 trading days of FOMC (07-28/29). Calendar's verdict stands:
event timing is noise for a structural move; the only real risk is gap
risk while uninvested. Sell, transfer, reinvest — days, not weeks.

Wrapper (lever #1) and fees (lever #2) are won by the exit itself
(~1,056 → ≤240 SEK/yr, fondskatt to zero, future gains tax-free under the
allowance). Fund selection is lever #4 — a category-compliant fund picked
this week beats a perfect fund picked next month. Do not stall.

---

## Portfolio health scorecard (from portfolio agent, verbatim; now → post-move)

| Dimension | Now | Post-move |
|---|---|---|
| Allocation vs targets | ACT | OK (if v1 adopted) |
| Single position | ACT (Auto 50 = 50.9% vs 15% cap) | WATCH (single global index fund — cap presumably means single securities, not diversified funds; profile needs a one-line clarification) |
| Institution concentration | WATCH (HB 69.8%) | ACT (Avanza 87.8% vs 80% cap) — see Decision 3 |
| Fee drag | ACT (893.94 SEK/yr = 0.46% vs 0.4% cap) | OK (~240 SEK/yr known, ~0.13%) |
| Wrapper efficiency | ACT | OK (residual: Swedbank 10k AF) |
| Drawdown fit | UNKNOWN — no backtest; rule-of-thumb stress on v1 start ≈ -30% = ZERO SLACK | UNKNOWN (improved by the 45% amendment above) |

Scorecard is **provisional** — profile TBDs still open:
1. **Deposit-date anchor** — "3–7y" is a range; the glidepath guessed T-5.
   Pinning the earliest realistic house-purchase year is the single
   highest-value profile answer outstanding.
2. **Position-cap wording** — does the 15% cap apply to diversified funds
   or only single securities? One line settles a standing WATCH.
3. **Exclusions** — "none stated yet"; confirm or fill.

---

## Headline calls

| # | Call | Confidence | Horizon |
|---|---|---|---|
| 1 | Deploy now; do not wait for equity index data next sweep | High | Long |
| 2 | Adopt v1 amended: 45% equity start, step-up to 50% only on confirmed ≥5y deposit | Medium | Long |
| 3 | Equity sleeve gets a 20% Nordic/European (or SEK-hedged) tilt, capped there | Medium | Medium |
| 4 | ETH: hold-and-dilute stands, with a hard deadline — bucket question answered by next sweep or default = deposit corpus → sell-by-T-2 glidepath | Medium | Medium |
| 5 | Institution cap: accept-and-amend 80→90 for diversified-fund-only holdings, revisit at 500k | High | Long |

No tactical (<6mo) calls this memo. The "execute by 07-21" line is
operational sequencing, not a market call. Per system policy, nothing
short-horizon could carry High confidence anyway.

---

## Where the agents disagreed — and who lost

**1. Deploy-now vs equity-entry-blind (valuation vs macro-regime,
thesis-review, calendar).** Valuation says the equity entry is unknowable
from this snapshot (equities block empty) and wants index proxies fetched
first. Macro-regime says do not wait; thesis-review says fees accrue
daily and VIX 15.57 is as good a transfer window as you get; calendar
says gap risk is the real risk. **Valuation loses on delay** — its
objection is true but doesn't support waiting: one more sweep of free
index data still cannot certify cheap-vs-expensive with any confidence,
while the fee drag and gap risk are certain. Valuation's objection is
instead absorbed structurally: only ~33% of proceeds (42,055) goes to
equity at the blind entry, the 78k FI sleeve is a genuinely paid position
(+~1.4pp real), and the 45%-not-50% amendment is partly this. Valuation's
fetch list is mandatory for next sweep. Confidence High, horizon Long.

**2. Currency (macro-regime vs portfolio).** Macro-regime: dollar at
120.69 is elevated; 100% unhedged global equity buys expensive dollars,
and mean-reversion is a SEK-return haircut even if the index rises.
Portfolio's table was plain global with no hedge line. **Split decision,
macro-regime wins a capped 20% of the equity sleeve.** The justification
is structural, not timing: the liability (house deposit) is in SEK, so
home-currency-correlated equity has a standing rationale independent of
the dollar's level; the elevated dollar makes now a reasonable moment to
institute it. Capped at 20% so it never becomes active FX management —
free data has no FX-timing edge and the dollar reading is 5 days stale.
Confidence Medium, horizon Medium.

**3. ETH (valuation vs macro-regime vs thesis-review).** Valuation reads
the cycle as constructive-hold (-64% from ATH, Extreme Fear 20, momentum
turned, rank #2 stable). Macro-regime says the regime is against it and
it already consumes the entire crypto budget this profile can justify.
Thesis-review says the position is UNTESTABLE — no thesis three sweeps
running, no cost basis, value not even verifiable this session (no
sek_per_eur in snapshot). **Nobody wins, and that is the ruling:** the
disagreement is undecidable until basis and bucket are known, so the
tie-break is procedural. Hold-and-dilute (portfolio's tax-aware plan)
stands for now; all agents agree zero NEW money goes to crypto. Hard
deadline attached: if the bucket question (deposit corpus vs ring-fenced
risk capital) is unanswered by next sweep, the default classification is
deposit corpus, which puts ETH on the glidepath's sell-by-T-2 track.
Confidence Medium, horizon Medium.

**4. Zero slack at 50% equity (Council vs portfolio).** Portfolio
defended 50% against 55–60 but not against 45, while its own stress math
showed -30% = exactly full tolerance and its anchor was a guess.
**Portfolio loses the start point, keeps the framework.** The glidepath
table, triggers, and taper logic are adopted intact; only the entry
column is shaved 50→45 until the deposit date is pinned. The cost of
being wrong on this is trivially small (see table below); the cost of
breaching a hard-deadline tolerance is not. Confidence Medium — this is
a judgment between two defensible numbers, and it flips on Decision 5.

**5. Institution cap (portfolio vs the written profile constraint).**
Post-move Avanza = 87.8% vs the 80% cap. No agent argued for the split
option at this size. **Accept-and-amend wins:** fund units are segregated
at the fund company; insättningsgaranti/investerarskydd cover the rest;
the realistic risk is operational (access delay), not credit loss. Amend
the cap to 90% for diversified-fund-only holdings with that written
reason, revisit at 500k. The alternative (second ISK for the 68k FI
sleeve) remains available if the user rejects the amendment — but it must
not delay deployment. Confidence High, horizon Long.

---

## Broken / untestable theses requiring a decision (from thesis-review, unsoftened)

- **ETH: no thesis THREE sweeps running — the oldest unaddressed gap in
  the book.** Status is not intact or broken but UNTESTABLE. Required to
  make it testable: (1) bucket — deposit corpus or ring-fenced risk
  capital (-64% from ATH demonstrates the drawdown profile; if this is
  deposit money on the 3y end, that alone likely decides it); (2) a
  specific mechanism claim with a falsifier and date; (3) a written exit
  condition; (4) cost basis + acquisition dates (K4; crypto losses only
  70% deductible); (5) whether ~6.8% weight is intentional or residual.
- **Swedbank fund:** drifting because an input is missing (cost basis),
  not because a call was made. Get the basis; then the move-to-ISK math
  is mechanical. No urgency, but it stays flagged until the number exists.
- **Avanza ISK existing holdings (~36k, ~19%):** not itemized, no thesis,
  no prices on file. Must be itemized at the same time as the new
  purchases are booked — the account is being opened up anyway.

---

## Rebalancing actions (SEK)

1. Sell both HB Auto funds in full, one order round (gross ~134,894 at
   2026-07-07 statement values; actuals will differ).
2. Transfer full proceeds to Avanza ISK.
3. Move 8,827 to a separate sparkonto outside the ISK (tax earmark).
4. Buy: 33,650 global equity index + 8,405 Nordic/European index +
   78,055 short-duration SEK räntefond; leave 5,957 cash.
5. Route monthly contributions (1–3k) to FI/cash sleeves first — this is
   also the ETH dilution mechanism (6.8% → 5% without K4).
6. No other trades. Swedbank and ETH are data-gathering items, not trades.

---

## Cost of being wrong

| Call | If wrong, realistic downside | Recoverable? |
|---|---|---|
| Deploy now (entry proves expensive) | Equity leg 42,055; a -25% mark ≈ -10,500 SEK | Yes — Medium/Long horizon; FI sleeve (78k, paid in real terms) unaffected. Waiting instead costs ~816 SEK/yr certain + unbounded gap risk. |
| 45% not 50% equity (markets rally) | Foregone ≈ 5pp × ~4%/yr equity premium ≈ 370 SEK/yr | Yes, trivially; asymmetric vs breaching -30% on a hard deadline |
| 20% currency tilt (dollar keeps rising) | 8,405 tilted; a 10% FX move missed ≈ -840 SEK | Yes |
| ETH hold-and-dilute (crypto winter extends) | Further -50% ≈ -6,250 SEK | NOT reliably, if it lands inside the deposit window — hence the bucket deadline |
| Institution cap 90% (Avanza operational failure) | Access delay on ~162k; fund units segregated, investerarskydd applies | Yes — operational, not credit loss |

---

## Timing collisions (from calendar)

- **FOMC 2026-07-28/29** — only event in the 4-week window. No collision
  if execution completes ~07-08 to 07-15. Conditional flag: slip past
  ~2026-07-21 (redemption T+2/T+3 + bank transfer) and reinvestment lands
  within 5 trading days of FOMC. Do not straddle the event deliberately —
  selling before and reinvesting after would be a tactical bet dressed as
  prudence.
- **Riksbank 2026-08-20** — verified no collision.
- **US/Swedish CPI dates: calendar is BLIND** (dates not on file, refused
  to fill from memory). A mid-July print inside the window is plausible
  and unverified. FOMC dates themselves are model-knowledge, unverified
  (IMPROVEMENTS #2).

---

## Data provenance

- **From the 2026-07-07 snapshot:** VIX 15.57, 10y-2y +0.35, fed funds
  3.63%, US CPI 4.27%, Riksbank 1.75%, ETH EUR 1,517.03, Fear & Greed 20.
  Stale within it: sek_per_usd / dollar index 120.69 (2026-07-02, 5d),
  SE CPI 0.3% (2025M12, SCB lag).
- **From the user's 2026-07-07 HB statement:** 134,894.24 gross,
  105,471.21 basis, 29,423.03 gain, 8,826.91 tax, 126,067.33 net.
- **Unverifiable this session:** all equity index levels (equities block
  empty — the equity entry valuation is a stated blind spot), ETH SEK
  value (no sek_per_eur in snapshot — fetch-script gap), Avanza ISK
  contents, Swedbank basis, ETH basis. ISK allowance threshold and
  fondskatt parameters: verify with Skatteverket, direction unchanged.
- **Next sweep must fetch (valuation's list):** global index proxy
  (VWCE.DE / IUSQ.DE), US large-cap proxy, Swedish/Nordic proxy,
  sek_per_eur, ETH certificate .ST ticker; verify FOMC schedule.

---

## Decisions requested (yes / no / amend)

1. **Adopt reference_targets v1 as amended** — 45% equity start,
   glidepath table otherwise as proposed, step-up to 50% only on
   confirmed ≥5y deposit horizon?
2. **Approve the deployment table** — 33,650 global / 8,405
   Nordic-European / 78,055 SEK short FI / 5,957 cash — and execute both
   legs by ~2026-07-21?
3. **Amend max_single_institution_pct 80 → 90** (diversified funds only,
   written reason, revisit at 500k)? If no: second ISK elsewhere for the
   78k FI sleeve — but deployment proceeds either way.
4. **Confirm the 15% single-position cap wording** applies to single
   securities/issuers, not diversified funds.
5. **Pin the earliest realistic house-purchase year** (converts the
   guessed T-5 anchor into a real one; may flip Decision 1's equity
   number in either direction).
6. **Answer the ETH bucket question** — deposit corpus or ring-fenced
   risk capital — and supply cost basis + acquisition dates. Default if
   unanswered by next sweep: deposit corpus → sell-by-T-2 track.
7. **Confirm the tax earmark routing** — 8,827 to a separate sparkonto
   outside the ISK.

## Post-execution bookkeeping (same day as trades)

1. `data/portfolio.json`: zero out hb-main, itemize every new ISK
   holding (one entry, one thesis each), itemize the existing ~36k Avanza
   holdings, mark `exit_plans.hb-af-exit` EXECUTED with actual sale
   prices.
2. `data/investor_profile.json`: write reference_targets v1 (as adopted
   or amended per Decisions 1/3/4), record the institution-cap amendment
   with its written reason.
3. Note the 8,827 earmark location so spring-2027 deklaration finds it.
4. Log actual vs statement sale values (slippage record for journal
   reconciliation).
5. Add sek_per_eur and the valuation fetch list to the fetch script /
   next-sweep checklist (meta/IMPROVEMENTS candidate).

---
---

# Amendment 2026-07-07 (same day)

Two user disclosures arrived after the memo above, and the portfolio
agent filed an amendment contesting two Council calls. This section
supersedes the original where stated; the original body is preserved
unedited for the record.

**New facts:**
1. **SEB fund account, ~18,000 SEK, previously undisclosed** (wrapper
   presumed AF, cost basis unknown), being sold today. Combined
   deployable into Avanza ISK: **142,867 SEK** (= 126,067 HB net +
   18,000 SEB − 1,200 provisional SEB tax reserve; the 1,200 is an
   illustration pending the avräkningsnota, released if the wrapper
   turns out not to be AF).
2. **The goal is softened.** Not a hard-deadline house deposit. User:
   "not completely sure what I am saving for" — most likely an apartment;
   one live idea is a Mediterranean vacation apartment (a EUR liability)
   rented out while renting in Sweden. Profile updated: horizon "3–7y
   (SOFT)", re-anchor trigger is the operative control, currency_note
   added.

## Rulings on the contested calls

**(a) Equity 45% vs 50% — portfolio's reassertion UPHELD. Adopt 50%.
(Supersedes original Call 2 and the "who lost" §4 ruling.)**
The Council's 45 rested on one load-bearing argument: zero slack against
a *hard-deadline* goal, where a -30% drawdown in year 6 is unrecoverable
before the money is needed. The user removed the hard deadline; the
binding constraint reverts to the stated -30% behavioral tolerance, and
portfolio's stress at 50 equity / 6.2 crypto lands AT -30, not beyond.
The Council's own original step-up condition ("50% unlocks on confirmed
≥5y horizon") was a proxy for recoverability — and goal flexibility is
recoverability. Searching for a replacement justification: valuation's
entry-blindness is a one-time entry concern, not a permanent allocation
parameter, and cannot carry a standing 5pp haircut alone. The Council
yields. Two residuals stated, not softened: (i) zero slack is now zero
slack against a *behavioral* limit — the -30% tolerance was stated when
the goal was hard, and a lived -30% may feel different; (ii) the
crystallize-early risk is real, but portfolio is right that the
re-anchor trigger, not a permanent equity discount, is the correct
instrument — a 5pp haircut would not save a portfolio that re-anchors
into an already-incurred drawdown anyway. Control demanded: `backtest`
runs the drawdown profile of the adopted 50/40/5/5 (crypto actual 6.2%)
next sweep — "drawdown fit UNKNOWN" is no longer acceptable on a
scorecard whose stress sits exactly at tolerance. **Confidence Medium,
horizon Long.** Stakes of the dispute: ~10k SEK of placement (59,684 vs
49,615 equity buy) — worth ruling correctly, not worth delaying
execution.

**(b) Currency tilt — DROPPED entirely; portfolio wins in full. No SEK/
Nordic tilt, no EUR tilt. (Supersedes original Call 3.)**
Cross-examined per the coordinator's question: was the SEK liability
doing the load-bearing work, or does macro-regime's elevated-dollar flag
(120.69, unchanged, still 5d stale) alone sustain the tilt at Medium?
The original ruling answered this itself: "the justification is
structural, not timing... the elevated dollar just makes now a
reasonable moment." Liability-matching was load-bearing; the dollar
level was explicitly declined as a basis because free data has no
FX-timing edge. With the liability currency genuinely unknown — SEK
apartment vs EUR Mediterranean point in *opposite* directions — matching
is void both ways, and keeping the tilt on the dollar datum alone would
be exactly the FX-timing call the original memo refused to make. Plain
global market-cap unhedged it is — which natively carries substantial
EUR exposure, so the Mediterranean branch gets partial coverage for
free; FI + cash stay SEK (living costs are SEK). Standing trigger,
written in the profile currency_note: the moment the goal's currency
firms, this ruling is reopened. Macro-regime's flag is thereby answered,
not ignored. **Confidence Medium** (the decision logic is robust, but
macro-regime's elevated-dollar headwind on unhedged SEK returns stands
unrebutted as an outcome risk), **horizon Medium.**

**(c) Institution concentration 88.8% (was 87.8%) vs 80 cap — ruling
UNCHANGED: accept-and-amend 80 → 90** (diversified funds only, written
reason: fund units segregated at fund company, insättningsgaranti/
investerarskydd, risk operational not credit; revisit at 500k). The
extra 1.0pp changes nothing in the reasoning. Post-move ISK ~178,867 —
still under the ~300k allowance (verify with Skatteverket).
**Confidence High, horizon Long.**

**(d) ETH default on the bucket deadline — default stays GOAL CORPUS.
(Original Call 4 stands, wording updated.)** The coordinator asked
whether the softened goal flips the fallback to ring-fenced risk
capital. No. Softening the goal is a fact about the goal, not a thesis
about ETH — thesis-review's finding (untestable, no basis, no owner) is
untouched. Flipping the default to "risk capital" would reward three
sweeps of non-answering by permanently exempting the position from the
glidepath. The conservative default holds: unanswered by next sweep =
goal corpus, on the taper track (whose dates now follow the re-anchor
trigger rather than a fixed calendar T). Zero new money to crypto
remains unanimous; dilution 6.2% → 5% via contributions. **Confidence
Medium, horizon Medium.**

**(e) New open question 5 — endorsed and escalated.** SEB is the second
undisclosed-account surprise. The class, not the instance, is the
problem: every allocation percentage this system computes is wrong if
the denominator is incomplete — today's true total was ~9% larger than
recorded. One-time full inventory (every bank/broker login) is now a
decision item below.

## FINAL deployment table — execute this week (supersedes the original)

Deployment of **142,867 SEK** into Avanza ISK at 50/40/5/5 targets:

| Sleeve | SEK | Constraint |
|---|---|---|
| Global equity index fund (unhedged, no tilt) | 59,684 | broad global index, fee ≤0.20% |
| Short-duration SEK fixed income (kort räntefond) | 75,547 | fee ≤0.20% |
| Cash in ISK (staging) | 7,636 | — |
| **Total** | **142,867** | |

Outside the ISK: **8,827 SEK** HB tax earmark to a separate sparkonto
(unchanged), plus the **1,200 SEK provisional SEB reserve** in the same
sparkonto — adjusted to 30% of the actual SEB gain when the
avräkningsnota arrives, released if no gain or non-AF wrapper.

Post-move whole portfolio (201,367 ex-earmarks): equity 100,684 (50.0%),
FI 80,547 (40.0%), cash 7,636 (3.8%), crypto 12,500 (6.2% vs 5% target,
diluted by contributions). Avanza 178,867 (88.8%).

Execution window unchanged: **both sales, transfer, and reinvestment by
~2026-07-21** (FOMC 07-28/29 buffer). The SEB sale rides the same
schedule.

## Decisions requested — UPDATED (supersedes the original list)

1. **Adopt reference_targets v1 with 50% equity start** (portfolio's
   reassertion upheld; Council's 45 withdrawn with the hard deadline)?
2. **Approve the final deployment table above** — 59,684 / 75,547 /
   7,636 of 142,867, no currency tilt — executed by ~2026-07-21?
3. **Amend max_single_institution_pct 80 → 90** (now covers 88.8%;
   diversified funds only, written reason, revisit at 500k)? Alternative
   unchanged: second ISK for the FI sleeve, without delaying deployment.
4. **Confirm the 15% single-position cap wording** applies to single
   securities, not diversified funds — the global fund is now 59,684 =
   29.6% of the portfolio, so this one line decides a scorecard status.
5. **Goal-firming trigger (replaces "pin the purchase year"):** commit to
   telling the system the moment the goal firms — type, currency, rough
   date. That event re-anchors the glidepath AND reopens currency ruling
   (b). No calendar answer is demanded while the goal is honestly vague.
6. **ETH bucket question** — unchanged; default if unanswered by next
   sweep remains goal corpus → taper track. Supply cost basis +
   acquisition dates.
7. **Tax earmarks:** confirm 8,827 (HB) + 1,200 provisional (SEB) to the
   sparkonto; adjust the SEB reserve to 30% of actual gain per
   avräkningsnota.
8. **NEW — full account inventory:** one-time sweep of every bank/broker
   login to close the undisclosed-account class. SEB was the second
   surprise; the system's percentages are only as good as the
   denominator.

## Post-execution bookkeeping — additions to the original list

6. Record the SEB sale from the avräkningsnota: fund name, wrapper
   confirmation, anskaffningsvärde, realized gain; zero out `seb-fund`
   in `data/portfolio.json`; update open structural question 4.
7. Write the goal-softening consequences into the adopted
   reference_targets note (re-anchor trigger is the operative control;
   currency ruling reopens on goal firming).
8. Queue `backtest` for next sweep: drawdown profile of the adopted
   50/40/5/5 (+6.2 actual crypto) — closes the "drawdown fit UNKNOWN"
   scorecard row.

## Updated data provenance

- **18,000 SEB value: user estimate**, not a statement or snapshot
  figure. SEB wrapper (AF) presumed from the user's description —
  unverified. SEB gain/tax: unknown until the avräkningsnota; the 1,200
  reserve is an illustration, not tax math.
- **142,867 deployable** is therefore user-statement-derived on both
  legs (HB statement + SEB estimate), not snapshot-verified; actual
  buys should use actual settled cash, keeping the 50/40/5/5 ratios.
- Goal softening and the Mediterranean/EUR possibility: user statement
  2026-07-07, recorded in `data/investor_profile.json`.
- Everything in the original provenance section stands, including the
  equity-entry blind spot and the next-sweep fetch list.

---
---

# Amendment 2026-07-12

*Note on this amendment's existence: an earlier attempt to write this
section terminated mid-task on an API connection error before anything
was written to disk — the memo file's timestamp (Jul 7, 17:56) confirmed
no partial or corrupt content was left behind. This is the complete,
successful pass. Full transparency for the record: this was a tool
failure, not a data or reasoning problem.*

A health-check sweep (portfolio + macro-regime) ran 2026-07-12 against a
fresh snapshot. Three new facts, two agent findings to rule on, and one
constraint ranking to fold in.

**New facts:**
1. **PayPal balance disclosed:** 1,177.49 USD + 266.88 EUR = **14,321.03
   SEK** at snapshot rates (sek_per_usd 9.6567, sek_per_eur 11.055 —
   the latter newly derived this session from sek_per_usd × usd_per_eur,
   closing the standing fetch-script gap flagged since 2026-07-07). Both
   rates dated 2026-07-02 (FRED lag). Recurring inflow ~750-1000 EUR
   roughly every 2 months lands here, irregular timing, described by the
   user as not salary.
2. **Risk-tier framework proposed** by the user, separate from and
   unreconciled with the adopted exposure-class glidepath: 70%
   secure/non-volatile, 20% medium risk, 10% high risk (actively traded
   weekly/daily).
3. **Execution status, confirmed 2026-07-12:** the Handelsbanken sale
   IS DONE — proceeds have landed — but the exact settled SEK amount has
   not yet been given to the system; do not treat 134,894.24 as final.
   The SEB sale is NOT done; it settles tomorrow, 2026-07-13. The
   142,867 SEK deployment plan from the 07-07 amendment is therefore
   **not executed — imminent, not final.**

## Rulings

**(A) Risk-tier reconciliation — split ruling: adopt the 10% tactical
tier now; do NOT adopt the 70% "secure" figure; force it back as a
question.**

The 10% high-risk/actively-traded tier is adopted immediately as an
ADDITIONAL lens over the existing exposure-class glidepath, not a
replacement — carved OUT of the crypto+equity sleeve, not added on top:
ETH (5%, already-adopted) + up to 5% of the equity sleeve reserved for
individual-stock tactical positions = the 10% tier. This is not a new
risk decision; it is a formalization of a rule this system already
carries — CLAUDE.md's short-horizon policy is explicit: tactical
overlay only, capped at 10% of portfolio, never High confidence, always
flagged tactical. The user's proposal maps onto that guardrail almost
exactly, so adopting it costs nothing and gains a named container for
future single-stock ideas that would otherwise arrive undisciplined.
**Confidence Medium** (the mapping — which specific holdings sit in
which tier — is being defined today, not tested), **horizon Short**
for the tactical sub-tier itself (per CLAUDE.md: <6mo, capped, never
High confidence), sitting inside the Long-horizon glidepath that
contains it.

The 70% "secure/non-volatile" figure is a different matter and is
**not adopted, silently or otherwise.** It is 25 percentage points more
conservative than the just-ruled 45% FI+cash at "now" (07-07
amendment's own 40 FI + 5 cash), a swing of roughly 55,000-68,000 SEK
out of equity into fixed income/cash on the current portfolio size, if
"secure" is read literally as FI+cash only. Portfolio agent is right to
decline resolving this by inference. Two readings exist with materially
different consequences: (i) "secure" means literally FI+cash+similar —
in which case the user is asking to de-risk substantially beyond what
was agreed five days ago, reopening the 45-vs-50 equity debate this
memo just closed; or (ii) "secure" is being used loosely to include
diversified, low-volatility equity index funds alongside cash/bonds —
in which case the 70/20/10 split may be largely compatible with
50/40/5/5 once index equity is counted as "secure." A provisional lean,
**Low confidence only:** reading (ii) is more consistent with the
user's own actions this week (fighting to keep equity at 50%, not 45%,
five days before proposing this), so guessing (ii) is more likely
correct than guessing (i) — but a 55-68k SEK swing is exactly the kind
of number this system does not estimate its way past. **This is Decision
item 1 below, not a Council assumption.**

**(B) PayPal FX — uncontested, ruling adopted as stated by both agents:
convert promptly via the lowest-spread path available; do not hold
either currency as an implicit FX position.** No dissent to record —
both agents reach the same conclusion for the same reason, which is
itself the interesting part: this is not a currency-timing call in
disguise. The idle balance earns 0% whether held in USD, EUR, or
converted to SEK today; there is no rate differential to wait for
because none of it is interest-bearing. The actual cost is structural
and recurring — PayPal's own conversion spread, unconfirmed but typically
several percent above mid-market, paid again every ~2 months on each
inflow indefinitely. That makes this a lever-#2 fee-drag problem under
CLAUDE.md's own priority order, not a lever-#5-adjacent FX-timing
question, and fee drag does not wait for a better macro read. **Do not
assume a spread number** — confirm PayPal's actual fee schedule before
choosing the routing path (direct low-spread converter vs. bank transfer
before conversion vs. holding foreign currency only if a matching
foreign-currency use exists — none currently does). **Confidence High**
(no regime dependency, no agent disagreement, the underlying logic is
structural not predictive), **horizon Long** (this is a routing/process
fix that recurs every ~2 months for as long as the inflow continues —
same category as wrapper and fee-drag fixes, not a one-time trade).

**(C) What constrains this setup — ranked, from portfolio agent, most to
least binding:**

1. **HB+SEB execution staleness** — now partially resolved: HB sale is
   done (proceeds landed, exact figure pending), SEB settles tomorrow.
   Until both are confirmed with actual figures, no allocation
   percentage in this memo is final — they are all computed against
   statement/estimate values, not settled cash.
2. **Operational sprawl** — 6 accounts/logins, 3 undisclosed-account
   surprises this month (SEB, the HB wrapper type itself, PayPal). Open
   question 5 (one-time full inventory) is now overdue on its own
   evidence: every surprise found so far was found by accident, in
   passing, not by a systematic check.
3. **Missing equity/fund data** — the snapshot's equities block remains
   empty; 4-5 holdings are still ticker TBD. This is why every equity
   entry-price judgment in this memo stays qualified as unknowable.
4. **Unresolved cost bases** — Swedbank, SEB, ETH. Each blocks a
   specific downstream decision (move-to-ISK math, tax earmark size, K4
   exit math respectively) but none blocks execution of the current plan.
5. **FX/multi-currency routing** — real, per ruling (B) above, but the
   smallest absolute SEK amount in this ranking and the most
   procedurally simple to fix once PayPal's fee schedule is confirmed.

This ranking is the direct answer to "what constrains this setup": it
is not a market call anywhere in the top three — it is data hygiene and
execution completion. That is consistent with CLAUDE.md's priority
order (wrapper/fee/allocation before selection); the system's own
constraints right now sit even earlier, at "know what you actually
hold and whether the trades you already decided on have settled."

**Single-position concentration, flagged ACT by the health check** (HB
Auto50 43.65% of total, Auto75 16.13%, both vs the 15% cap, as
diversified funds not single stocks): **noted for the record, not newly
actionable.** The sale is already in motion — the ACT flag is an
artifact of `hb-main` not yet being zeroed out in `data/portfolio.json`
pending exact settlement figures, not a fresh breach requiring a new
decision. It resolves automatically at bookkeeping step 1 once the HB
sale is confirmed and the file is updated. Recording it here so it does
not silently vanish from the audit trail before that update happens.

## Confirmed-executed vs still-pending (state of the world, 2026-07-12)

| Leg | Status | Note |
|---|---|---|
| HB sale | **DONE** | Proceeds landed 2026-07-12; exact settled SEK amount not yet reported — do not assume 134,894.24 is final |
| SEB sale | **PENDING** | Settles 2026-07-13 |
| 142,867 SEK deployment (07-07 amendment) | **NOT EXECUTED** | Imminent, not final — wait for both settled figures before buying; the 50/40/5/5 sleeve *ratios* stand, the absolute SEK amounts will be recomputed against actual settled cash, not the 142,867 estimate |
| PayPal conversion | **NOT STARTED** | Pending Decision 2 below (routing path) and PayPal's actual fee schedule |
| Risk-tier 10% tactical lens | **ADOPTED** (ruling A) | No trades required to adopt; it's a container, not a position, until a specific tactical idea is proposed |
| Risk-tier 70% "secure" figure | **NOT ADOPTED** | Forced back to user, Decision 1 |

## Decisions requested — additions (do not supersede the 07-07 amendment's list; these are new)

1. **Resolve the 70% "secure" question:** does "secure" mean literally
   FI+cash+equivalent (→ reopens the 45-vs-50 equity ruling, ~55-68k SEK
   swing), or does it include diversified low-volatility equity index
   funds alongside cash/bonds (→ likely compatible with the adopted
   50/40/5/5 once mapped)? Answer determines whether risk-tier and
   exposure-class glidepath can be merged or must run as two lenses.
2. **Confirm PayPal's actual conversion fee schedule** before choosing a
   routing path (direct low-spread converter / bank transfer before
   conversion / hold-if-matching-use — none currently applies).
3. **Report the exact settled SEK amounts** for the HB sale (done) and
   the SEB sale (settles 2026-07-13) before the 142,867 deployment plan
   is executed — the ratios stand, the absolute figures need the real
   numbers.
4. **Commit to the one-time full account inventory** (open question 5) —
   three surprises this month is no longer a coincidence worth waiting
   out.
5. **Name which specific holdings, if any, are candidates for the new
   10% tactical tier** — the container is adopted; it is empty until a
   position is proposed against it, capped, and tagged Short-horizon
   per CLAUDE.md.

## Updated data provenance

- **PayPal SEK value (14,321.03):** computed this session from snapshot
  `data/snapshots/20260712T082357.json` (sek_per_usd 9.6567, sek_per_eur
  11.055, both dated 2026-07-02) applied to user-disclosed balances
  (1,177.49 USD + 266.88 EUR, disclosed 2026-07-12). The balances
  themselves are a user statement; the conversion is snapshot-derived.
- **sek_per_eur** is newly present in this snapshot, derived from
  sek_per_usd × usd_per_eur — this closes the fetch-script gap flagged
  in the 07-07 memo's data provenance section and in thesis-review's ETH
  finding (ETH's SEK value can now be computed directly rather than
  estimated).
- **HB settled amount:** NOT YET AVAILABLE. The 134,894.24 figure
  remains a 2026-07-07 statement value, not a settlement confirmation.
  User has stated the figure is coming.
- **SEB settled amount:** NOT YET AVAILABLE — sale has not occurred as
  of this writing (settles 2026-07-13).
- **Risk-tier framework (70/20/10):** user statement 2026-07-12, recorded
  verbatim in `data/investor_profile.json` under
  `risk_tier_framework_proposed`, status PROPOSED not ADOPTED except
  for the 10% tactical sub-tier ruled on above.
- Everything in the original memo's and the 07-07 amendment's provenance
  sections stands.

---
---

# Amendment 2026-07-13 — TIME-SENSITIVE, same-day transfer

*User is executing a ~154k SEK transfer into Avanza ISK today. Ruling
kept compact by design — action items first, reasoning short-form.*

**What changed:** HB and SEB are both now CONFIRMED SOLD AND SETTLED
(136,611.83 SEK and 17,382.43 SEK respectively — actuals, not estimates;
HB tax confirmed 8,455.86, down from the 8,826.91 statement estimate).
Avanza ISK is now fully itemized: 2 stocks, 2 funds, 1 crypto certificate
(CoinShares XBT Provider Bitcoin Tracker One, 15,540 SEK), plus cash.
The certificate was invisible to every prior deployment calculation in
this memo, which assumed the Avanza 36k line was pure equity. Combined
with the ETH wallet (12,500 SEK), total crypto is **28,040 SEK = 12.90%**
of the 217,279.43 SEK investable base (both tax earmarks excluded) —
well above the adopted 5% target.

## Ruling (a): crypto trim — NO forced trim today; deploy as below;
forced thesis deadline set for the BTC certificate.

Dilution-only is ruled out on the numbers alone: reaching 5% by
contribution dilution needs +343,521 SEK of new capital, i.e. 9.5–28.6
years at 1,000–3,000 SEK/mo — outside even the soft 3–7y horizon. That
much is settled and doesn't need more debate.

Whether to trim is a different question, and does not need to be settled
today. Today's transfer adds zero to crypto either way (the 78,571 /
65,768 deployment below touches equity and FI only), so the trim
decision is fully separable from the time-critical action. The BTC
certificate has never had a written thesis — same gap as ETH — and
mechanically resembles it: trimming it "because no thesis" would repeat
the exact shortcut this system already refused to take with ETH.
Deciding it properly, not fast, is available here because — unlike
ETH — waiting costs nothing: the certificate sits inside the ISK, so a
future sale is schablonintäkt-taxed, not a 30%-on-realized-gain K4 event.
There is no tax clock and no fee-drag clock running on indecision here,
unlike the HB/SEB legs that were genuinely time-costly to hold.

**Ruling: no trim today. Default at next sweep, absent a written
thesis, is TRIM — not classify-and-hold.** This is deliberately the
opposite default from ETH's, and the asymmetry is the point: ETH's
default was "classify as goal corpus, don't sell" because an
unreasoned ETH sale is expensive to get wrong (K4, 30% tax, unknown
basis) — the cost of a bad default was high, so the default was
conservative-by-inertia. A BTC-certificate sale is tax-free and
mechanically trivial, so the cost of a bad default is low, and the
conservative default is instead the one that actually fixes the
glidepath breach: if next sweep arrives with still no thesis, sell down
the BTC certificate (not ETH — portfolio agent's own point: any trim
hits the certificate first on tax grounds) to bring crypto to the 5%
target. **Confidence Medium** (single-agent analysis this round under
time pressure — not cross-examined by valuation, macro-regime, or
thesis-review; revisit at next full sweep), **horizon Long**
(allocation-class correction, owned by portfolio per CLAUDE.md).

## Ruling (b): deployment amounts — CONFIRMED, no changes.

| Sleeve | SEK |
|---|---|
| Global equity index fund | 78,571 |
| Short-duration SEK fixed income | 65,768 |
| Cash | 0 |
| Crypto | 0 |
| **Total** | **144,339** |

Uncontested inputs, preserves the adopted 50:40 equity:FI ratio against
the small existing clean-equity base already in the ISK. Zero to cash
is correct — the cash sleeve is already above target from existing ISK
cash. Zero to crypto is correct on every ruling above. Sign-off stands
on the same logic as headline call 1 (deploy now, don't wait for equity
index data) — that ruling was High confidence on *not waiting*, not on
the entry price itself, which remains unverifiable this session; nothing
here changes that.

## Ruling (c): what to do right now

1. Complete today's transfer of the settled HB (136,611.83) + SEB
   (17,382.43) cash into Avanza ISK.
2. Route **8,455.86 SEK** (HB, confirmed) + **~1,200 SEK** (SEB,
   provisional — adjust to 30% of actual gain once the avräkningsnota is
   read) to a sparkonto outside the ISK. Do not deploy this money.
3. Inside the ISK, buy **78,571 SEK** broad global equity index fund and
   **65,768 SEK** short-duration SEK fixed-income fund.
4. Do **not** buy crypto and do **not** trim the BTC certificate today.
   Leave the certificate and the ETH wallet untouched.
5. Post-move Avanza institution share: 83.05% — under the already-amended
   90% cap. No action needed, noted for the record only.

## Additions to decisions requested

9. **Write a thesis for the BTC certificate** (mechanism, falsifier,
   exit condition, cost basis if obtainable) by next sweep. Default if
   silent: trim to the 5% crypto target, hitting the certificate before
   ETH.
10. Get the certificate's, Avanza Auto 3's, and Tundra Sustainable
    Frontier's annual fee percentages from factsheets — feeds the
    fee-drag scorecard row, currently incomplete for three holdings.

## Updated data provenance

- HB and SEB settlement figures (136,611.83 / 17,382.43, tax 8,455.86
  confirmed) are user-confirmed actuals as of 2026-07-12/13, superseding
  all prior statement-based estimates in this memo.
- Avanza ISK itemization (2 stocks, 2 funds, 1 crypto certificate, cash;
  36,120 SEK total) is from a live user-provided account snapshot
  captured 2026-07-13 — not a fetched snapshot, a user statement.
- BTC certificate cost basis (6 units, 2,016.67 SEK/unit, 15,540 SEK
  market value, +28.43% since purchase) is from the same live snapshot.
- The 217,279.43 SEK investable-base and 12.90% crypto-share figures are
  portfolio agent's calculation this session, not independently
  cross-checked against the raw account figures under time pressure —
  flagged, not expected to be materially wrong given the inputs above.
