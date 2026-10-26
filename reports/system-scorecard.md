# System scorecard

Generated 2026-10-26 06:39 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 73 (9 held / 30 watchlist / 34 new), focus 24, status VALID
  Runs recorded: 10
  Candidate turnover vs previous run: 4% new to the set
  New candidates per run (last 8): 35, 34, 35, 36, 35, 33, 35, 34

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            89%         100%
    fwd_pe                        71%         100%
    peg                           82%          94%
    roic_pct                      96%         100%
    de_ratio                      89%          94%
    rev_growth_pct                93%         100%
    fcf_yield_pct                 82%          97%
    div_yield_pct                100%         100%
    beta                          96%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 29pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** fcf_yield_pct: 15pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 9/73

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=87   median    +1.1%   beat baseline 55%
    defensive                          n=121  median    -0.1%   beat baseline 49%
    growth                             n=113  median    -4.0%   beat baseline 35%
    quality                            n=197  median    -2.8%   beat baseline 42%
    value                              n=124  median    +0.8%   beat baseline 55%

    top-half ranks median -2.7% vs bottom-half +0.6% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           n=20   median    +2.8%   beat baseline 60%
    contrarian                         n=29   median    +0.0%   beat baseline 45%
    copycat                            n=25   median    +0.0%   beat baseline 48%
    defensive                          n=33   median    +6.5%   beat baseline 79%
    fundamental                        n=42   median    -2.6%   beat baseline 36%
    growth                             n=40   median    -5.4%   beat baseline 18%
    macro                              n=26   median    +9.0%   beat baseline 77%
    valuation                          n=38   median    +0.0%   beat baseline 42%

    Chairman median +2.8% vs voices' median +0.0% — synthesis adds value

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 44
  Open BUY calls: 19, median age 21 days, oldest 56 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           56d  entry      25.77  now      24.02     -6.8%
    AZN.ST         49d  entry     1570.5  now     1713.5     +9.1%
    VICI           49d  entry      25.65  now      24.02     -6.4%
    VICI           42d  entry      24.73  now      24.02     -2.9%
    AZN.ST         42d  entry     1541.0  now     1713.5    +11.2%
    AZN.ST         35d  entry     1626.5  now     1713.5     +5.3%
    VICI           35d  entry      24.11  now      24.02     -0.4%
    AZN.ST         28d  entry     1630.0  now     1713.5     +5.1%
    VICI           28d  entry      23.27  now      24.02     +3.2%
    AZN.ST         21d  entry     1599.0  now     1713.5     +7.2%
    VICI           21d  entry      22.73  now      24.02     +5.7%
    AZN.ST         14d  entry     1574.5  now     1713.5     +8.8%
    VICI           14d  entry      22.79  now      24.02     +5.4%
    AZN.ST          7d  entry     1675.5  now     1713.5     +2.3%
    VICI            7d  entry      23.46  now      24.02     +2.4%
    NVDA            7d  entry     217.23  now     212.21     -2.3%
    SHB-A.ST        0d  entry      147.7  now      147.7     +0.0%
    NVDA            0d  entry     212.21  now     212.21     +0.0%
    VICI            0d  entry      24.02  now      24.02     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=19, need 20) — provisional median +2.4%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +9.3%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-10-19 (20 observations)
  Money in:             192,500 SEK
  Actual:               225,352 SEK  (+17.1%)
  Same money in VWCE.DE:   195,587 SEK  (+1.6%)
  Difference:           +29,765 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 24 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  5  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    beta                 missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, DIOS.ST)
    rev_cagr3y_pct       missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    net_debt_to_ebitda   missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)
    fcf_yield_pct        missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

