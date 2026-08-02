#!/usr/bin/env python3
"""
Orchestrator: calls the separated fetch modules and assembles one combined
snapshot, for single-call convenience and backward compatibility with the
lens agents' "read the latest snapshot" instructions.

Each data KIND is its own independently runnable, independently debuggable
module — if one breaks, target it directly instead of digging through a
monolith:
  scripts/fetch_prices.py            equity/ETF prices
  scripts/fetch_fundamentals_us.py   equity fundamentals (US-listed only)
  scripts/fetch_crypto_prices.py     crypto prices (CoinGecko)
  scripts/fetch_macro.py             FRED / Riksbank / SCB / ECB
  scripts/fetch_sentiment.py         crypto Fear & Greed
  scripts/fetch_insiders_us.py       SEC Form 4 filing counts
  scripts/fetch_insiders_se.py       Finansinspektionen Insynsregistret (issuer-name-based)

Insider activity is NOT fetched by this orchestrator — `run.py fetch`'s
`_fetch_insiders()` calls those two modules directly and merges the result
into `equities[ticker]["insider_activity_us"/"_se"]` of the SAME snapshot
file this script writes, keyed per-ticker exactly like price/fundamentals.
That's the one standardized place every lens reads it from. (An earlier
version of this script had its own separate `--insiders` flag writing a
differently-shaped `insider_activity` block — removed, since two schemas
for the same fact is exactly the duplicated-state problem this project's
architecture exists to avoid. Use `python run.py fetch --only insiders_us`
/ `--only insiders_se` to fetch just insider data standalone.)

Writes one timestamped JSON snapshot to data/cache/snapshots/.
Every downstream lens reads this file — it is the single source of
numerical truth for the session. If a fetch fails, the field is written
as null with an "error" note, never silently omitted or guessed.

Usage:
  python fetch_market_data.py --tickers AAPL,VWCE.DE,SPY --crypto bitcoin,ethereum
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_prices import fetch_prices  # noqa: E402
from fetch_fundamentals_us import fetch_fundamentals  # noqa: E402
from fetch_crypto_prices import fetch_crypto  # noqa: E402
from fetch_macro import fetch_macro  # noqa: E402
from fetch_sentiment import fetch_crypto_fear_greed  # noqa: E402


def fetch_equities(tickers):
    """Combine separated price + fundamentals fetches into the schema lenses
    already expect (one record per ticker with both price and fundamentals
    fields). Kept for backward compatibility — new code should prefer calling
    fetch_prices.py / fetch_fundamentals_us.py directly when only one kind of
    data is needed."""
    prices = fetch_prices(tickers)
    fundamentals = fetch_fundamentals(tickers)
    out = {}
    for t in tickers:
        px, fd = prices.get(t, {}), fundamentals.get(t, {})
        if px.get("error") and fd.get("error"):
            out[t] = {"error": px["error"]}
            continue
        out[t] = {
            "price": px.get("price"), "prev_close": px.get("prev_close"),
            "52w_high": px.get("52w_high"), "52w_low": px.get("52w_low"),
            "currency": px.get("currency") or fd.get("currency"),
            "market_cap": fd.get("market_cap"), "trailing_pe": fd.get("trailing_pe"),
            "forward_pe": fd.get("forward_pe"), "peg_ratio": fd.get("peg_ratio"),
            "dividend_yield": fd.get("dividend_yield"), "beta": fd.get("beta"),
            "revenue_growth": fd.get("revenue_growth"), "profit_margins": fd.get("profit_margins"),
            "debt_to_equity": fd.get("debt_to_equity"), "recommendation": fd.get("recommendation"),
            "sector": fd.get("sector"), "industry": fd.get("industry"), "country": fd.get("country"),
            "_source": fd.get("_source") if not fd.get("error") else None,
            "_fundamentals_unavailable_reason": fd.get("error"),
        }
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", default="", help="Comma-separated equity/ETF tickers")
    parser.add_argument("--crypto", default="", help="Comma-separated CoinGecko coin ids")
    args = parser.parse_args()

    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]
    coins = [c.strip() for c in args.crypto.split(",") if c.strip()]

    snapshot = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "equities": fetch_equities(tickers) if tickers else {},
        "crypto": fetch_crypto(coins),
        "macro": fetch_macro(),
        "sentiment": {"crypto_fear_greed": fetch_crypto_fear_greed()},
    }

    os.makedirs("data/cache/snapshots", exist_ok=True)
    fname = f"data/cache/snapshots/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"Wrote {fname}")
    return fname


if __name__ == "__main__":
    main()
