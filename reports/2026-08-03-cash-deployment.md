# Deploying the 26,399 SEK Avanza ISK cash — 2026-08-03

Structured analysis of this session's fetched data, not advice from a
licensed adviser. Nothing here is executed — you place every order.

**Mandate (your direction, 2026-08-03):** start building the medium tier with
individual stocks. All of it goes to equity — none to crypto, which is still
above target at 11.3% vs 10%.

Data: `data/cache/snapshots/20260803T150647.json` (fundamentals, 12 tickers)
and `20260803T150805.json` (Finansinspektionen insider transactions).

## Sizing frame

- Medium tier now: **0.98%** of portfolio (~2,165 SEK) against a **30%** target
  (~64,400 SEK). Deploying 26,399 SEK takes it to ~12.6% — real progress, no
  risk of overshooting.
- Single-position cap is 15% (~32,200 SEK). Three positions of ~8,500 SEK are
  ~4% each, comfortably inside it.
- Individual stocks carry **no ongoing fee**, so this also improves the
  portfolio's fee profile relative to holding the same money in funds.

## Ruled out, with reasons

| Candidate | Why not |
|---|---|
| Industrivärden, Latour, Lundbergs, Kinnevik | All holding companies — overlap the Investor A position you already hold, and none can be honestly valued without a NAV discount figure this system has never obtained. Industrivärden also sits at 95% of its 52-week range on an "underperform" rating. |
| Swedbank | Doubles up on Handelsbanken A (both Swedish banks). At 97% of its 52-week range, PEG 7.4. |
| Saab | Forward P/E **61.7 against trailing 46.7** — consensus expects earnings to fall. Most expensive name in the set despite strong 28.6% revenue growth. |
| Atlas Copco | Genuine quality (ROE 25.7%) but P/E 37 at 89% of its 52-week range. Buying the high. |
| Volvo B | Forward P/E 14.9 looks cheap, but debt/equity **147.3** is the highest here and it sits at 94% of range. |
| Hexagon B | Trailing P/E 11.1 looks like the bargain of the list — but forward P/E is **18.0**, implying roughly a 38% EPS decline, on a "hold" rating. Insider buying exists but totals ~8,500 SEK, which is noise. This is the same "cheap for a reason" pattern already flagged on Handelsbanken. |

## The three that survive

| | Alfa Laval | ABB | AstraZeneca |
|---|---|---|---|
| Price | 563.60 | 934.80 | 1,627.50 |
| Trailing / forward P/E | 28.6 / 25.8 | 36.3 / 35.8 | 23.2 / n/a |
| PEG | 2.9 | 2.6 | **1.5** |
| Revenue growth | +7.7% | **+14.2%** | +6.4% |
| ROE | 19.1% | **32.6%** | 22.0% |
| Debt/equity | 45.8 | 55.8 | 64.2 |
| 52-week range position | 84% | 72% | **47%** |
| Analyst view | buy | none | buy |
| Insider activity (FI register) | **9 buys, 0 sells, ~954k SEK** incl. a board member at ~300k in April | 8 buys ~220k, 2 trivial sells | Mixed/uninformative |
| Sector | Industrials | Industrials | **Healthcare** |

**Alfa Laval** has the cleanest insider signal in the whole set — nine
acquisitions, zero disposals, and a board member putting ~300,000 SEK in.
Forward P/E below trailing means earnings are expected to grow. The knock is
valuation: PEG 2.9 and 84% of its 52-week range.

**ABB** is the highest-quality business on the numbers — 32.6% ROE with 14.2%
revenue growth is the best combination here — with net insider buying. Two
caveats: P/E 36 is rich, and see the withholding-tax flag below.

**AstraZeneca** is the only name that adds a sector you don't own at all, at
the most reasonable growth-adjusted valuation (PEG 1.5) and the least
stretched price (47% of range). Its insider data is uninformative rather than
negative — it's UK-domiciled, so the Swedish register only sees part of the
picture. Treat that row as "no signal", not "bad signal".

## Flag worth knowing before you buy ABB

ABB is **Swiss-domiciled** and AstraZeneca **UK-domiciled**, even though both
trade in SEK on Nasdaq Stockholm.

Switzerland withholds tax on dividends at source (commonly 35%), and inside an
ISK that is difficult to reclaim — the ISK's flat schablonskatt structure gives
you no Swedish tax to credit it against. On ABB's 1.2% yield that is roughly
0.4%/yr of quiet drag, which is the size of your entire portfolio fee cap.
The UK generally does not withhold on dividends, so AstraZeneca is unaffected,
and Swedish-domiciled Alfa Laval has no issue in an ISK.

**Verify this with Avanza before buying ABB** — I have not confirmed the
current treaty treatment, and it is the one thing here that could change the
decision rather than just colour it.

## Recommendation

Three positions, roughly equal, ~830 SEK left for courtage:

| Order | Shares | Amount |
|---|---|---|
| **ALFA.ST** (Alfa Laval) | 16 | 9,017.60 |
| **AZN.ST** (AstraZeneca) | 5 | 8,137.50 |
| **ABB.ST** (ABB) | 9 | 8,413.20 |
| | | **25,568.30** |

Alfa Laval and AstraZeneca are the two I hold highest confidence in — the
first on insider conviction plus improving earnings, the second on valuation
plus genuine diversification.

**If the ABB withholding issue bothers you**, the third slot has two
Swedish-domiciled alternatives, both worse on other grounds: Atlas Copco
(42 shares, 8,446 SEK — better business, expensive at 89% of range) or Volvo B
(23 shares, 8,379 SEK — cheaper forward, but 147 debt/equity). A third option
is simply splitting the ~8,400 across Alfa Laval and AstraZeneca and holding
two positions instead of three. That concentrates more but avoids every flag
above.

## Confidence and horizon

| Call | Confidence | Horizon |
|---|---|---|
| Deploy all 26,399 to equity, none to crypto | High — crypto is above target either way | Long |
| Alfa Laval as a core medium-tier holding | Medium — strong insider signal, rich valuation | Medium (6mo–3y) |
| AstraZeneca as the diversifier | Medium — cleanest valuation, weakest insider visibility | Medium |
| ABB as the third | Low-Medium — best business, but rich and carries the withholding flag | Medium |
| Three positions rather than one | High — structural, not a market view | Long |

## Cost of being wrong

| If wrong | Realistic downside | Recoverable? |
|---|---|---|
| All three fall in a broad Swedish drawdown | ~25,600 SEK exposed; a -30% move is ~7,700 SEK, inside your stated tolerance | Yes — liquid, and you hold no forced-seller position |
| Alfa Laval's 84%-of-range entry proves to be the top | Roughly 9,000 SEK at risk of a multi-quarter drawdown; insider buying does not prevent a de-rating | Yes |
| ABB withholding drag is real and unreclaimable | ~0.4%/yr on 8,400 SEK ≈ 34 SEK/yr — small in SEK, but it recurs forever and is invisible unless checked | Yes, by switching once confirmed |
| Deploying now, just before Riksbank (Aug 20) | A hawkish surprise pressures Swedish equities near-term; none of this thesis depends on the rate path | Yes |

## Timing

**Riksbank decision 2026-08-20**, 17 days out. Swedish CPI last read 0.3%,
which leaves room for a cut. This is not a reason to wait — none of the three
theses rest on the rate path, and holding cash to time a central bank is
exactly the short-horizon guessing this system is built to avoid. Noted so
it isn't a surprise if the market moves that week.

FOMC is 2026-09-15/16, outside any relevant window here.

## After you execute

Send me the fills (ticker, shares, price paid, date) and I will record them in
`portfolio.json` — cost basis and acquisition date included, so the position
report can show real returns from day one rather than the "no data" the funds
currently show.
