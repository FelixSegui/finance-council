# System scorecard

Generated 2026-10-19 06:48 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 74 (9 held / 30 watchlist / 35 new), focus 24, status VALID
  Runs recorded: 9
  Candidate turnover vs previous run: 7% new to the set
  New candidates per run (last 8): 33, 35, 34, 35, 36, 35, 33, 35

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            93%         100%
    fwd_pe                        70%         100%
    peg                           81%          95%
    roic_pct                      96%         100%
    de_ratio                      89%          95%
    rev_growth_pct                93%         100%
    fcf_yield_pct                 78%          95%
    div_yield_pct                100%         100%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 30pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** fcf_yield_pct: 17pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 8/74

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=75   median    -1.1%   beat baseline 45%
    defensive                          n=108  median    +0.7%   beat baseline 53%
    growth                             n=102  median    -1.0%   beat baseline 46%
    quality                            n=174  median    +0.4%   beat baseline 52%
    value                              n=111  median    -0.8%   beat baseline 48%

    top-half ranks median -2.2% vs bottom-half +1.4% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=17, need 20) — provisional median +2.8%
    contrarian                         n=26   median    -0.5%   beat baseline 31%
    copycat                            n=22   median    +1.7%   beat baseline 68%
    defensive                          n=30   median    +3.2%   beat baseline 63%
    fundamental                        n=38   median    +0.0%   beat baseline 42%
    growth                             n=36   median    -0.8%   beat baseline 25%
    macro                              n=24   median    +5.2%   beat baseline 75%
    valuation                          n=33   median    -0.8%   beat baseline 36%

    Chairman vs voices: insufficient evidence (chairman n=17, voices n=209, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 39
  Open BUY calls: 16, median age 21 days, oldest 49 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           49d  entry      25.77  now      23.46     -9.0%
    AZN.ST         42d  entry     1570.5  now     1675.5     +6.7%
    VICI           42d  entry      25.65  now      23.46     -8.5%
    VICI           35d  entry      24.73  now      23.46     -5.1%
    AZN.ST         35d  entry     1541.0  now     1675.5     +8.7%
    AZN.ST         28d  entry     1626.5  now     1675.5     +3.0%
    VICI           28d  entry      24.11  now      23.46     -2.7%
    AZN.ST         21d  entry     1630.0  now     1675.5     +2.8%
    VICI           21d  entry      23.27  now      23.46     +0.8%
    AZN.ST         14d  entry     1599.0  now     1675.5     +4.8%
    VICI           14d  entry      22.73  now      23.46     +3.2%
    AZN.ST          7d  entry     1574.5  now     1675.5     +6.4%
    VICI            7d  entry      22.79  now      23.46     +2.9%
    AZN.ST          0d  entry     1675.5  now     1675.5     +0.0%
    VICI            0d  entry      23.46  now      23.46     +0.0%
    NVDA            0d  entry     217.23  now     217.23     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=16, need 20) — provisional median +1.8%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +6.2%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-10-19 (20 observations)
  Money in:             192,500 SEK
  Actual:               225,352 SEK  (+17.1%)
  Same money in VWCE.DE:   196,735 SEK  (+2.2%)
  Difference:           +28,616 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 24 focus names (these are the names the Council actually reasons over):
    peg                  missing on  5  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI, AZA.ST)
    fwd_pe               missing on  5  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0)
    fcf_yield_pct        missing on  5  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, DIOS.ST, AZA.ST)
    net_debt_to_ebitda   missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, AZA.ST)
    rev_cagr3y_pct       missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    de_ratio             missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

