# System scorecard

Generated 2026-09-07 07:03 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 74 (9 held / 30 watchlist / 35 new), focus 23, status VALID
  Runs recorded: 3
  Candidate turnover vs previous run: 7% new to the set
  New candidates per run (last 3): 33, 33, 35

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 1/625 (0.2%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            93%         100%
    fwd_pe                        67%         100%
    peg                           81%          95%
    roic_pct                      96%         100%
    de_ratio                      89%          95%
    rev_growth_pct                96%         100%
    fcf_yield_pct                 85%          97%
    div_yield_pct                 89%          76%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 33pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 11/74

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         insufficient evidence (n=17, need 20) — provisional median +0.4%
    defensive                          n=29   median    +1.5%   beat baseline 69%
    growth                             n=23   median    -1.0%   beat baseline 48%
    quality                            n=44   median    -0.4%   beat baseline 43%
    value                              n=27   median    +0.9%   beat baseline 85%

    top-half ranks median +0.7% vs bottom-half +0.4% — ranking adds signal

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=4, need 20) — provisional median -0.7%
    contrarian                         insufficient evidence (n=6, need 20) — provisional median +0.2%
    copycat                            insufficient evidence (n=5, need 20) — provisional median -1.0%
    defensive                          insufficient evidence (n=6, need 20) — provisional median -0.2%
    fundamental                        insufficient evidence (n=7, need 20) — provisional median +0.0%
    growth                             insufficient evidence (n=7, need 20) — provisional median +0.0%
    macro                              insufficient evidence (n=6, need 20) — provisional median +0.0%
    valuation                          insufficient evidence (n=8, need 20) — provisional median +0.0%

    Chairman vs voices: insufficient evidence (chairman n=4, voices n=45, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: expired 1, open 10
  Open BUY calls: 3, median age 0 days, oldest 7 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI            7d  entry      25.77  now      25.65     -0.5%
    AZN.ST          0d  entry     1570.5  now     1555.5     -1.0%
    VICI            0d  entry      25.65  now      25.65     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=3, need 20) — provisional median -0.5%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median -1.0%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-09-07 (14 observations)
  Money in:             192,500 SEK
  Actual:               224,067 SEK  (+16.4%)
  Same money in VWCE.DE:   194,144 SEK  (+0.9%)
  Difference:           +29,923 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 23 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  6  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0, INDU-C.ST)
    net_debt_to_ebitda   missing on  5  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, EG, APO)
    div_yield_pct        missing on  5  (BTC0E.AS, DE000A0S9GB0, APP, SNDK, SMCI)
    rev_cagr3y_pct       missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, MU)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    fcf_yield_pct        missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, APO)

