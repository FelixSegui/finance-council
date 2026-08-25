# System scorecard

Generated 2026-08-25 08:42 UTC · benchmark VWCE.DE

Every skill figure below is **excess return versus the benchmark**, not a raw return — a raw return mostly measures the market. Any bucket with fewer than 20 observations reports its count and withholds the number, because a hit rate computed on a handful of picks is noise that reads like skill.

## 1. DISCOVERY — is the funnel finding things it has not seen?

  Latest run: universe 624, candidates 71 (8 held / 30 watchlist / 33 new), focus 22, status VALID
  Runs recorded: 1
  New candidates per run (last 1): 33

## 2. DATA — is the evidence sound, and even across markets?

  Fetch failures: 0/624 (0.0%)

  Coverage by market (a gap here tilts whole lenses invisibly):
    field                       Sweden  United State
    pe                            93%         100%
    fwd_pe                        70%         100%
    peg                           81%          94%
    roic_pct                      96%          97%
    de_ratio                      89%          94%
    rev_growth_pct               100%         100%
    fcf_yield_pct                 85%          94%
    div_yield_pct                 89%          72%
    beta                         100%          97%
    pct_52w_range                100%         100%
  ** fwd_pe: 30pp spread across markets — any lens ranking on it compares names on unequal evidence.
  ** div_yield_pct: 17pp spread across markets — any lens ranking on it compares names on unequal evidence.
  Candidates with a thin lens score: 9/71

## 3. MECHANICAL — do the lens rankings predict anything?

  Only 1 run recorded. This pillar needs history: a rank is only testable once time has passed since it was assigned. Come back after several sweeps.

## 4. JUDGEMENT — do the voices beat the mechanics they were handed?

  Decision ledger is empty. `council` records picks with
  `python scripts/decisions.py record --picks <file>`.
  Until then this pillar cannot be measured at all — and
  'we don't know' is the correct answer, not an estimate.

## 5. DECISION — does conviction mean anything, and does the human act?

  Decision ledger is empty.

## 6. OUTCOME — is the real portfolio beating just buying the index?

  Period 2026-07-13 -> 2026-08-24 (12 observations)
  Money in:             192,500 SEK
  Actual:               221,588 SEK  (+15.1%)
  Same money in VWCE.DE:   193,236 SEK  (+0.4%)
  Difference:           +28,352 SEK

## GAPS — what would most improve the next decision

  Missing metrics across the 22 focus names (these are the names the Council actually reasons over):
    fwd_pe               missing on  5  (INVE-A.ST, ATCO-B.ST, AZN.ST, BTC0E.AS, INDU-C.ST)
    div_yield_pct        missing on  5  (BTC0E.AS, APP, SNDK, SMCI, CHTR)
    net_debt_to_ebitda   missing on  4  (SHB-A.ST, BTC0E.AS, EG, APO)
    peg                  missing on  3  (BTC0E.AS, SNDK, VICI)
    fcf_yield_pct        missing on  3  (SHB-A.ST, BTC0E.AS, APO)
    rev_cagr3y_pct       missing on  2  (BTC0E.AS, SNDK)

  ** The decision ledger is empty, so pillars 4 and 5 cannot be
     measured at all. That is the single largest gap: until
     `council` records its picks, 'do the voices add value?'
     has no answer and the Council cannot be weighted.

