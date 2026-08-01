"""
Centralized tunable constants for the Finance Council system.

Before this file existed, these values were hardcoded across multiple scripts
and agent .md files — changing the AI Council's SEK trigger, for example, meant
finding and editing prose inside council.md. This file is the one place to tune
system behavior. It is machine-owned config (how the system behaves), not
financial config (what the user decided about their own money — that lives in
the Settings sheet of master.xlsx).

Import with: from config.settings import ...
"""

# --- AI Council deep-dive mode triggers (council.md / meta.md) ---
AI_COUNCIL_SEK_THRESHOLD = 20_000
AI_COUNCIL_PORTFOLIO_PCT_THRESHOLD = 0.10  # whichever of the two is smaller

# --- rank_candidates.py: hybrid risk score weights (must sum to 1.0) ---
RISK_SCORE_WEIGHTS = {
    "volatility": 0.40,
    "max_drawdown": 0.35,
    "leverage": 0.15,
    "size": 0.10,
}
RISK_SCORE_VOLATILITY_BAND = (0.15, 0.60)     # (low, high) annualized vol -> 0-100
RISK_SCORE_DRAWDOWN_BAND = (0.10, 0.60)       # (low, high) abs 1y max drawdown -> 0-100
RISK_SCORE_LEVERAGE_BAND = (0.3, 3.0)         # (low, high) debt/equity -> 0-100
RISK_SCORE_SIZE_BANDS = [                      # (market_cap_threshold, score)
    (200e9, 5), (50e9, 20), (10e9, 40), (2e9, 65),
]  # below the smallest threshold: 85 (micro/small cap)

# --- rank_candidates.py: factor z-score winsorization ---
FACTOR_WINSOR_PCT = 0.02  # clip to [2nd, 98th] percentile before z-scoring

# --- fetch_fundamentals.py: multi-class share-count staleness guard ---
SHARES_MAX_AGE_DAYS = 400  # a share-count row older than this is treated as missing, not current

# --- fetch_fundamentals.py: retry policy for throttled Yahoo chart requests ---
YAHOO_CHART_RETRY_TRIES = 3
YAHOO_CHART_RETRY_BACKOFF_SEC = 0.6  # multiplied by attempt number

# --- rank_candidates.py: universe cache freshness ---
UNIVERSE_CACHE_DAYS = 7

# --- generate_coverage_report.py: consecutive-sweeps-missing flag threshold ---
COVERAGE_STREAK_FLAG_THRESHOLD = 2

# --- performance.py / backtest.py: default benchmark ---
DEFAULT_BENCHMARK_TICKER = "VWCE.DE"

# --- SEC EDGAR requests require an identifying User-Agent ---
SEC_USER_AGENT = "finance-council personal research (seguifelix@gmail.com)"

# --- Insynsregistret (Finansinspektionen Swedish insider register) ---
INSYNSREGISTRET_BASE_URL = "https://marknadssok.fi.se/Publiceringsklient/sv-SE/Search/Search"
