# System scorecard

Generated 2026-09-21 07:10 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 74 (9 held / 30 watchlist / 35 new), focus 23, status VALID
  Runs recorded: 5
  Candidate turnover vs previous run: 5% new to the set
  New candidates per run (last 5): 33, 33, 35, 34, 35

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 3/625 (0.5%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            92%         100%
    fwd_pe                        69%         100%
    peg                           85%          95%
    roic_pct                      96%         100%
    de_ratio                      88%          95%
    rev_growth_pct                96%         100%
    fcf_yield_pct                 85%          97%
    div_yield_pct                 92%          77%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 31pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** div_yield_pct: 15pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 10/74

## 3. MECHANICAL — do the lens rankings predict anything?

  Excess return vs benchmark, by the lens that ranked the name best:
    contrarian                         n=37   median    -2.7%   beat baseline 19%
    defensive                          n=56   median    +0.6%   beat baseline 61%
    growth                             n=48   median    -1.7%   beat baseline 38%
    quality                            n=87   median    -0.6%   beat baseline 48%
    value                              n=55   median    -3.7%   beat baseline 20%

    top-half ranks median -2.1% vs bottom-half -0.9% — RANKING IS NOT ADDING SIGNAL

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Excess return vs benchmark on BUY calls, per voice:
    chairman                           insufficient evidence (n=8, need 20) — provisional median +0.4%
    contrarian                         insufficient evidence (n=13, need 20) — provisional median -2.5%
    copycat                            insufficient evidence (n=10, need 20) — provisional median +0.2%
    defensive                          insufficient evidence (n=14, need 20) — provisional median +0.0%
    fundamental                        insufficient evidence (n=16, need 20) — provisional median +0.0%
    growth                             insufficient evidence (n=15, need 20) — provisional median +0.0%
    macro                              insufficient evidence (n=12, need 20) — provisional median +2.4%
    valuation                          insufficient evidence (n=17, need 20) — provisional median +0.0%

    Chairman vs voices: insufficient evidence (chairman n=8, voices n=97, need 20 each). This is the number that would justify ever weighting the Council — do not weight it before this line reads.

## 5. DECISION — does conviction mean anything, and does the human act?

  Chairman calls by status: declined 1, expired 1, open 19
  Open BUY calls: 7, median age 7 days, oldest 21 days
  Price drift while unexecuted (what the delay has cost so far):
    VICI           21d  entry      25.77  now      24.11     -6.4%
    AZN.ST         14d  entry     1570.5  now     1638.5     +4.3%
    VICI           14d  entry      25.65  now      24.11     -6.0%
    VICI            7d  entry      24.73  now      24.11     -2.5%
    AZN.ST          7d  entry     1541.0  now     1638.5     +6.3%
    AZN.ST          0d  entry     1626.5  now     1638.5     +0.7%
    VICI            0d  entry      24.11  now      24.11     +0.0%

  Calibration — a conviction score that does not sort outcomes is noise:
    low (1-4)                          no observations yet
    medium (5-7)                       insufficient evidence (n=7, need 20) — provisional median +0.0%
    high (8-10)                        insufficient evidence (n=1, need 20) — provisional median +4.3%

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-09-21 (16 observations)
  Money in:             192,500 SEK
  Actual:               225,675 SEK  (+17.2%)
  Same money in VWCE.DE:   195,738 SEK  (+1.7%)
  Difference:           +29,937 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 23 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  6  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, DE000A0S9GB0, INDU-C.ST)
    div_yield_pct        missing on  5  (BTC0E.AS, DE000A0S9GB0, APP, SNDK, CHTR)
    rev_cagr3y_pct       missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, MU)
    peg                  missing on  4  (BTC0E.AS, DE000A0S9GB0, SNDK, VICI)
    de_ratio             missing on  4  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0, MO)
    net_debt_to_ebitda   missing on  3  (SHB-A.ST, BTC0E.AS, DE000A0S9GB0)

