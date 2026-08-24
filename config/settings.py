"""
Tunable constants for the Finance Council system, in one place.

Machine config (how the system behaves), not financial config (what the user
decided about their own money — that lives in `data/investor_profile.json`).

Import with: from config.settings import ...
"""

HTTP_USER_AGENT = "finance-council personal research (seguifelix@gmail.com)"

# ---------------------------------------------------------------------------
# Discovery funnel — scripts/build_universe.py + scripts/scout.py
# ---------------------------------------------------------------------------

# How old data/universe.json may get before scout flags it as stale. The broad
# universe is refreshed periodically (constituent changes are slow); the
# watchlist and holdings are re-read every sweep regardless.
UNIVERSE_REFRESH_INTERVAL_DAYS = 30

# Fundamentals cache for the universe stage. Screening 600 names against a live
# fetch every sweep is both slow and pointless — fundamentals move quarterly.
# Holdings and watchlist names are always refetched (they drive live decisions).
UNIVERSE_CACHE_DAYS = 7
UNIVERSE_FETCH_WORKERS = 8

# Funnel shape. universe -> (lens ranking) -> candidate pool -> Council.
# Each of the five lenses contributes its own top slice, so a name that fails
# one lens's view of the world can still reach the Council through another.
LENS_TOP_N = 10                 # names each lens promotes
CANDIDATE_POOL_SOFT_CAP = 80    # warn above this; Council reasoning gets expensive
# Limited scout refinement: the pool stays broad, but the top slice is marked
# `focus` so the Council knows where to spend depth. Every current holding is
# always in focus (each has a live hold/sell decision), and nothing outside
# focus is excluded — a voice can always pull a non-focus name back in.
FOCUS_TOP_N = 15
FACTOR_WINSOR_PCT = 0.02        # clip to [2nd, 98th] pct before z-scoring
LENS_MIN_FIELDS = 2             # a lens score needs this many non-null inputs

# Scout health thresholds. A screen that looks empty must be distinguishable
# from a screen that broke — see scout.py's diagnose_zero_pass().
MISSING_DATA_RATE_ALERT = 0.35  # >35% of screened names missing a filtered field
FETCH_FAILURE_RATE_ALERT = 0.20
SINGLE_FILTER_KILL_RATE = 0.90  # one filter alone rejecting >=90% of names

# Unit guards (S19). These snapshot fields are on a percentage-POINT scale
# (Yahoo reports debt_to_equity as 45.6, not 0.456). A threshold below the
# guard is almost certainly a decimal-scale mistake, and silently produces an
# empty screen that looks exactly like "the market has nothing good in it".
# field -> (minimum plausible threshold, human explanation)
PERCENT_POINT_SCALE_FIELDS = {
    "debt_to_equity": (5.0, "Yahoo reports debt/equity in percentage points "
                            "(45.6 = 0.46x). A ceiling of 2.0 rejects everything; "
                            "use 150-200."),
}

# Default screen thresholds. Triage only — a FAIL is context for the Council,
# never an automatic exclusion.
DEFAULT_SCREEN = {
    "max_pe": 40.0,
    "max_forward_pe": 30.0,
    "min_profit_margin": 0.0,
    "max_debt_to_equity": 250.0,
    "min_market_cap": 5e8,
}

# ---------------------------------------------------------------------------
# scripts/import_excel_holdings.py — sanity bounds (flag, never block)
# ---------------------------------------------------------------------------
EXCEL_STALE_AFTER_DAYS = 10
EXCEL_PE_SANITY_RANGE = (3, 80)
# Lower bound deliberately not 0: an implausibly LOW P/E on a normally-profitable
# large cap is exactly the failure mode observed (a wrong/mismatched field), and
# a pure upper-bound check misses it entirely.

# ---------------------------------------------------------------------------
# derived_metrics.py / fetch_market_data.py — ROIC tax-rate assumption
# ---------------------------------------------------------------------------
# No source in this pipeline provides a real effective tax rate. ROIC needs
# SOME rate, so this is an explicit, labelled ASSUMPTION (statutory rate by
# listing country); any ROIC computed with it is tagged quality_state
# "ESTIMATED", never "OK".
DEFAULT_CORPORATE_TAX_RATE_ASSUMPTION = {
    "Sweden": 0.206, "United Kingdom": 0.25, "United States": 0.21,
    "Switzerland": 0.147, "Germany": 0.298, "Denmark": 0.22, "Norway": 0.22,
}
DEFAULT_CORPORATE_TAX_RATE_FALLBACK = 0.25

# ---------------------------------------------------------------------------
# performance.py / backtest.py
# ---------------------------------------------------------------------------
DEFAULT_BENCHMARK_TICKER = "VWCE.DE"
