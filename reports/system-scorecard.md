# System scorecard

Generated 2026-11-02 06:35 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 73 (9 held / 30 watchlist / 34 new), focus 24, status VALID
  Runs recorded: 11
  Candidate turnover vs previous run: 3% new to the set
  New candidates per run (last 8): 34, 35, 36, 35, 33, 35, 34, 34

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            89%         100%
    fwd_pe                        70%         100%
    peg                           81%          95%
    roic_pct                      96%         100%
    de_ratio                      89%          95%
    rev_growth_pct                93%         100%
    fcf_yield_pct                 81%          95%
    div_yield_pct                100%         100%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 30pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 9/73

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=101  median    +3.1%   beat baseline 69%
    defensive                          n=135  median    +2.8%   beat baseline 68%
    growth                             n=122  median    -3.6%   beat baseline 46%
    quality                            n=219  median    -1.9%   beat baseline 45%
    value                              n=136  median    +2.4%   beat baseline 63%

    top-half ranks median -0.5% vs bottom-half +2.8% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           n=21   median    +5.4%   beat baseline 71%
    contrarian                         n=32   median    +1.3%   beat baseline 53%
    copycat                            n=29   median    +4.3%   beat baseline 69%
    defensive                          n=36   median    +8.9%   beat baseline 94%
    fundamental                        n=47   median    -4.2%   beat baseline 40%
    growth                             n=44   median    -7.0%   beat baseline 16%
    macro                              n=28   median   +10.3%   beat baseline 82%
    valuation                          n=41   median    +1.4%   beat baseline 54%

    Chairman median +5.4% vs voices' median +1.8% — synthesis adds value

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 49
  Open BUY calls: 20, median age 28 days, oldest 63 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           63d  entry      25.77  now      24.46     -5.1%
    AZN.ST         56d  entry     1570.5  now     1800.0    +14.6%
    VICI           56d  entry      25.65  now      24.46     -4.6%
    VICI           49d  entry      24.73  now      24.46     -1.1%
    AZN.ST         49d  entry     1541.0  now     1800.0    +16.8%
    AZN.ST         42d  entry     1626.5  now     1800.0    +10.7%
    VICI           42d  entry      24.11  now      24.46     +1.5%
    AZN.ST         35d  entry     1630.0  now     1800.0    +10.4%
    VICI           35d  entry      23.27  now      24.46     +5.1%
    AZN.ST         28d  entry     1599.0  now     1800.0    +12.6%
    VICI           28d  entry      22.73  now      24.46     +7.6%
    AZN.ST         21d  entry     1574.5  now     1800.0    +14.3%
    VICI           21d  entry      22.79  now      24.46     +7.3%
    AZN.ST         14d  entry     1675.5  now     1800.0     +7.4%
    VICI           14d  entry      23.46  now      24.46     +4.3%
    NVDA           14d  entry     217.23  now     204.64     -5.8%
    SHB-A.ST        7d  entry      147.7  now     155.65     +5.4%
    NVDA            7d  entry     212.21  now     204.64     -3.6%
    VICI            7d  entry      24.02  now      24.46     +1.8%
    NVDA            0d  entry     213.66  now     204.64     -4.2%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       n=20   median    +5.2%   beat baseline 70%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +15.1%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-10-26 (21 observations)
  Money in:             192,500 SEK
  Actual:               223,644 SEK  (+16.2%)
  Same money in VWCE.DE:   192,084 SEK  (-0.2%)
  Difference:           +31,560 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 24 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  5  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0)
    rev_cagr3y_pct       missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    peg                  missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    net_debt_to_ebitda   missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)
    fcf_yield_pct        missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)
    de_ratio             missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

