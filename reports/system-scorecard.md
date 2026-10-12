# System scorecard

Generated 2026-10-12 06:43 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 72 (9 held / 30 watchlist / 33 new), focus 23, status VALID
  Runs recorded: 8
  Candidate turnover vs previous run: 4% new to the set
  New candidates per run (last 8): 33, 33, 35, 34, 35, 36, 35, 33

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            92%         100%
    fwd_pe                        72%         100%
    peg                           84%          95%
    roic_pct                      96%         100%
    de_ratio                      88%          95%
    rev_growth_pct                96%         100%
    fcf_yield_pct                 80%          97%
    div_yield_pct                100%         100%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 28pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** fcf_yield_pct: 17pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 8/72

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=65   median    -4.3%   beat baseline 17%
    defensive                          n=96   median    -1.3%   beat baseline 43%
    growth                             n=89   median    +0.8%   beat baseline 56%
    quality                            n=152  median    +0.3%   beat baseline 51%
    value                              n=98   median    -5.7%   beat baseline 16%

    top-half ranks median -2.2% vs bottom-half -1.1% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=14, need 20) — provisional median -1.8%
    contrarian                         n=22   median    -4.4%   beat baseline 18%
    copycat                            insufficient evidence (n=19, need 20) — provisional median -0.7%
    defensive                          n=26   median    +0.0%   beat baseline 42%
    fundamental                        n=33   median    +1.2%   beat baseline 52%
    growth                             n=31   median    +0.0%   beat baseline 39%
    macro                              n=21   median    +0.9%   beat baseline 62%
    valuation                          n=29   median    -0.3%   beat baseline 34%

    Chairman vs voices: insufficient evidence (chairman n=14, voices n=181, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 34
  Open BUY calls: 13, median age 21 days, oldest 42 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           42d  entry      25.77  now      22.79    -11.6%
    AZN.ST         35d  entry     1570.5  now     1574.5     +0.3%
    VICI           35d  entry      25.65  now      22.79    -11.2%
    VICI           28d  entry      24.73  now      22.79     -7.8%
    AZN.ST         28d  entry     1541.0  now     1574.5     +2.2%
    AZN.ST         21d  entry     1626.5  now     1574.5     -3.2%
    VICI           21d  entry      24.11  now      22.79     -5.5%
    AZN.ST         14d  entry     1630.0  now     1574.5     -3.4%
    VICI           14d  entry      23.27  now      22.79     -2.1%
    AZN.ST          7d  entry     1599.0  now     1574.5     -1.5%
    VICI            7d  entry      22.73  now      22.79     +0.3%
    AZN.ST          0d  entry     1574.5  now     1574.5     +0.0%
    VICI            0d  entry      22.79  now      22.79     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=13, need 20) — provisional median -2.1%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median -1.6%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-10-05 (18 observations)
  Money in:             192,500 SEK
  Actual:               226,181 SEK  (+17.5%)
  Same money in VWCE.DE:   200,951 SEK  (+4.4%)
  Difference:           +25,230 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 23 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  5  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    fcf_yield_pct        missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, DIOS.ST)
    rev_cagr3y_pct       missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    net_debt_to_ebitda   missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)
    de_ratio             missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

