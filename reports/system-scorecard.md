# System scorecard

Generated 2026-09-14 06:31 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 73 (9 held / 30 watchlist / 34 new), focus 23, status VALID
  Runs recorded: 4
  Candidate turnover vs previous run: 3% new to the set
  New candidates per run (last 4): 33, 33, 35, 34

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 1/625 (0.2%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            92%         100%
    fwd_pe                        69%         100%
    peg                           85%          95%
    roic_pct                      96%         100%
    de_ratio                      88%          95%
    rev_growth_pct                96%         100%
    fcf_yield_pct                 85%          97%
    div_yield_pct                 92%          76%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 31pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** div_yield_pct: 17pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 10/73

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=27   median    -2.6%   beat baseline 19%
    defensive                          n=43   median    -1.4%   beat baseline 42%
    growth                             n=35   median    -2.1%   beat baseline 37%
    quality                            n=66   median    -1.4%   beat baseline 32%
    value                              n=41   median    -2.5%   beat baseline 22%

    top-half ranks median -2.3% vs bottom-half -1.7% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=6, need 20) — provisional median -1.9%
    contrarian                         insufficient evidence (n=9, need 20) — provisional median +0.0%
    copycat                            insufficient evidence (n=7, need 20) — provisional median -0.3%
    defensive                          insufficient evidence (n=10, need 20) — provisional median -1.9%
    fundamental                        insufficient evidence (n=11, need 20) — provisional median +0.0%
    growth                             insufficient evidence (n=11, need 20) — provisional median +0.0%
    macro                              insufficient evidence (n=9, need 20) — provisional median +0.0%
    valuation                          insufficient evidence (n=12, need 20) — provisional median +0.0%

    Chairman vs voices: insufficient evidence (chairman n=6, voices n=69, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 14
  Open BUY calls: 5, median age 7 days, oldest 14 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           14d  entry      25.77  now      24.73     -4.0%
    AZN.ST          7d  entry     1570.5  now     1541.0     -1.9%
    VICI            7d  entry      25.65  now      24.73     -3.6%
    VICI            0d  entry      24.73  now      24.73     +0.0%
    AZN.ST          0d  entry     1541.0  now     1541.0     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=5, need 20) — provisional median -1.9%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median -1.9%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-09-07 (14 observations)
  Money in:             192,500 SEK
  Actual:               224,067 SEK  (+16.4%)
  Same money in VWCE.DE:   194,885 SEK  (+1.2%)
  Difference:           +29,182 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 23 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  6  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0, INDU-C.ST)
    rev_cagr3y_pct       missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, MU)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    net_debt_to_ebitda   missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, EG)
    div_yield_pct        missing on  4  (BTC0E.AS, DE000A0S9GB0, APP, SNDK)
    de_ratio             missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, MO)

