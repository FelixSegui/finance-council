# System scorecard

Generated 2026-09-28 06:40 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 75 (9 held / 30 watchlist / 36 new), focus 23, status VALID
  Runs recorded: 6
  Candidate turnover vs previous run: 4% new to the set
  New candidates per run (last 6): 33, 33, 35, 34, 35, 36

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 4/625 (0.6%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            92%         100%
    fwd_pe                        69%         100%
    peg                           85%          95%
    roic_pct                      96%         100%
    de_ratio                      88%          92%
    rev_growth_pct                96%         100%
    fcf_yield_pct                 81%          95%
    div_yield_pct                 96%          75%
    beta                         100%          98%
    pct_52w_range                100%         100%
  ** fwd_pe: 31pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** div_yield_pct: 21pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 10/75

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=46   median    -5.6%   beat baseline 33%
    defensive                          n=69   median    +0.4%   beat baseline 57%
    growth                             n=62   median    -0.5%   beat baseline 44%
    quality                            n=108  median    +0.1%   beat baseline 53%
    value                              n=70   median    -6.5%   beat baseline 10%

    top-half ranks median -2.8% vs bottom-half -0.3% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=10, need 20) — provisional median +0.0%
    contrarian                         insufficient evidence (n=16, need 20) — provisional median -3.9%
    copycat                            insufficient evidence (n=13, need 20) — provisional median +0.0%
    defensive                          insufficient evidence (n=18, need 20) — provisional median +0.0%
    fundamental                        n=21   median    +0.0%   beat baseline 43%
    growth                             n=20   median    +0.0%   beat baseline 35%
    macro                              insufficient evidence (n=15, need 20) — provisional median +0.0%
    valuation                          n=22   median    +0.0%   beat baseline 32%

    Chairman vs voices: insufficient evidence (chairman n=10, voices n=125, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 24
  Open BUY calls: 9, median age 14 days, oldest 28 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           28d  entry      25.77  now      23.27     -9.7%
    AZN.ST         21d  entry     1570.5  now     1630.0     +3.8%
    VICI           21d  entry      25.65  now      23.27     -9.3%
    VICI           14d  entry      24.73  now      23.27     -5.9%
    AZN.ST         14d  entry     1541.0  now     1630.0     +5.8%
    AZN.ST          7d  entry     1626.5  now     1630.0     +0.2%
    VICI            7d  entry      24.11  now      23.27     -3.5%
    AZN.ST          0d  entry     1630.0  now     1630.0     +0.0%
    VICI            0d  entry      23.27  now      23.27     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=9, need 20) — provisional median +0.0%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +3.9%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-09-21 (16 observations)
  Money in:             192,500 SEK
  Actual:               225,675 SEK  (+17.2%)
  Same money in VWCE.DE:   199,215 SEK  (+3.5%)
  Difference:           +26,460 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 23 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  6  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0, INDU-C.ST)
    div_yield_pct        missing on  5  (BTC0E.AS, DE000A0S9GB0, APP, SNDK, CHTR)
    rev_cagr3y_pct       missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, MU)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    de_ratio             missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, MO)
    net_debt_to_ebitda   missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

