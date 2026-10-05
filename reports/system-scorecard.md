# System scorecard

Generated 2026-10-05 06:45 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 74 (9 held / 30 watchlist / 35 new), focus 23, status VALID
  Runs recorded: 7
  Candidate turnover vs previous run: 7% new to the set
  New candidates per run (last 7): 33, 33, 35, 34, 35, 36, 35

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            92%         100%
    fwd_pe                        72%         100%
    peg                           84%          95%
    roic_pct                      96%          98%
    de_ratio                      88%          92%
    rev_growth_pct               100%          98%
    fcf_yield_pct                 80%          95%
    div_yield_pct                100%         100%
    beta                         100%          95%
    pct_52w_range                100%         100%
  ** fwd_pe: 28pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 9/74

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=55   median    -5.2%   beat baseline 11%
    defensive                          n=82   median    -1.6%   beat baseline 32%
    growth                             n=76   median    -2.1%   beat baseline 38%
    quality                            n=129  median    -2.0%   beat baseline 40%
    value                              n=86   median    -7.4%   beat baseline 8%

    top-half ranks median -4.7% vs bottom-half -2.0% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=12, need 20) — provisional median -1.8%
    contrarian                         insufficient evidence (n=19, need 20) — provisional median -8.1%
    copycat                            insufficient evidence (n=16, need 20) — provisional median -1.7%
    defensive                          n=22   median    -1.9%   beat baseline 9%
    fundamental                        n=27   median    +0.0%   beat baseline 33%
    growth                             n=25   median    +0.0%   beat baseline 32%
    macro                              insufficient evidence (n=18, need 20) — provisional median -0.3%
    valuation                          n=26   median    -1.5%   beat baseline 31%

    Chairman vs voices: insufficient evidence (chairman n=12, voices n=153, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 29
  Open BUY calls: 11, median age 14 days, oldest 35 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           35d  entry      25.77  now      22.73    -11.8%
    AZN.ST         28d  entry     1570.5  now     1599.0     +1.8%
    VICI           28d  entry      25.65  now      22.73    -11.4%
    VICI           21d  entry      24.73  now      22.73     -8.1%
    AZN.ST         21d  entry     1541.0  now     1599.0     +3.8%
    AZN.ST         14d  entry     1626.5  now     1599.0     -1.7%
    VICI           14d  entry      24.11  now      22.73     -5.7%
    AZN.ST          7d  entry     1630.0  now     1599.0     -1.9%
    VICI            7d  entry      23.27  now      22.73     -2.3%
    AZN.ST          0d  entry     1599.0  now     1599.0     +0.0%
    VICI            0d  entry      22.73  now      22.73     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=11, need 20) — provisional median -1.9%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +0.9%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-09-28 (17 observations)
  Money in:             192,500 SEK
  Actual:               226,008 SEK  (+17.4%)
  Same money in VWCE.DE:   200,203 SEK  (+4.0%)
  Difference:           +25,805 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 23 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  6  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0, INDU-C.ST)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    de_ratio             missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, MO)
    rev_cagr3y_pct       missing on  3  (BTC0E.AS, DE000A0S9GB0, SNDK)
    net_debt_to_ebitda   missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)
    fcf_yield_pct        missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

