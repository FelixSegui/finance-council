# System scorecard

Generated 2026-11-09 06:43 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 76 (9 held / 30 watchlist / 37 new), focus 24, status VALID
  Runs recorded: 12
  Candidate turnover vs previous run: 16% new to the set
  New candidates per run (last 8): 35, 36, 35, 33, 35, 34, 34, 37

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            88%         100%
    fwd_pe                        69%         100%
    peg                           81%          95%
    roic_pct                      96%         100%
    de_ratio                      88%          95%
    rev_growth_pct                92%         100%
    fcf_yield_pct                 81%         100%
    div_yield_pct                100%         100%
    beta                         100%          98%
    pct_52w_range                100%         100%
  ** fwd_pe: 31pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** fcf_yield_pct: 19pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 8/76

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=115  median    +6.7%   beat baseline 88%
    defensive                          n=149  median    +5.0%   beat baseline 79%
    growth                             n=132  median    -9.4%   beat baseline 29%
    quality                            n=239  median    +1.3%   beat baseline 54%
    value                              n=149  median    +8.0%   beat baseline 76%

    top-half ranks median +2.2% vs bottom-half +4.8% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           n=22   median    +9.6%   beat baseline 82%
    contrarian                         n=35   median    +9.5%   beat baseline 77%
    copycat                            n=32   median    +6.1%   beat baseline 69%
    defensive                          n=40   median    +8.6%   beat baseline 82%
    fundamental                        n=52   median    +0.0%   beat baseline 46%
    growth                             n=48   median    -0.3%   beat baseline 42%
    macro                              n=30   median   +12.8%   beat baseline 80%
    valuation                          n=44   median    +4.4%   beat baseline 61%

    Chairman median +9.6% vs voices' median +6.1% — synthesis adds value

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 54
  Open BUY calls: 21, median age 35 days, oldest 70 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           70d  entry      25.77  now      25.21     -2.2%
    AZN.ST         63d  entry     1570.5  now     1860.5    +18.5%
    VICI           63d  entry      25.65  now      25.21     -1.7%
    VICI           56d  entry      24.73  now      25.21     +1.9%
    AZN.ST         56d  entry     1541.0  now     1860.5    +20.7%
    AZN.ST         49d  entry     1626.5  now     1860.5    +14.4%
    VICI           49d  entry      24.11  now      25.21     +4.6%
    AZN.ST         42d  entry     1630.0  now     1860.5    +14.1%
    VICI           42d  entry      23.27  now      25.21     +8.3%
    AZN.ST         35d  entry     1599.0  now     1860.5    +16.4%
    VICI           35d  entry      22.73  now      25.21    +10.9%
    AZN.ST         28d  entry     1574.5  now     1860.5    +18.2%
    VICI           28d  entry      22.79  now      25.21    +10.6%
    AZN.ST         21d  entry     1675.5  now     1860.5    +11.0%
    VICI           21d  entry      23.46  now      25.21     +7.5%
    NVDA           21d  entry     217.23  now      181.6    -16.4%
    SHB-A.ST       14d  entry      147.7  now      161.2     +9.1%
    NVDA           14d  entry     212.21  now      181.6    -14.4%
    VICI           14d  entry      24.02  now      25.21     +5.0%
    NVDA            7d  entry     213.66  now      181.6    -15.0%
    NVDA            0d  entry      181.6  now      181.6     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       n=21   median    +9.1%   beat baseline 81%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +20.7%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-11-09 (23 observations)
  Money in:             192,500 SEK
  Actual:               223,873 SEK  (+16.3%)
  Same money in VWCE.DE:   189,419 SEK  (-1.6%)
  Difference:           +34,454 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 24 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  5  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, AZA.ST)
    net_debt_to_ebitda   missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, AZA.ST)
    fcf_yield_pct        missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, AZA.ST)
    rev_cagr3y_pct       missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    de_ratio             missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

