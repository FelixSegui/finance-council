#!/usr/bin/env python3
"""
Equity/ETF PRICE data only — separated from fundamentals so a price-fetch
failure and a fundamentals-fetch failure are two different, independently
debuggable problems, not one entangled one.

Source: Yahoo's chart endpoint (`fetch_fundamentals.py:fetch_price_momentum`)
— the endpoint proven reachable in this environment even when Yahoo's
fundamentals endpoint (quoteSummary) is crumb-blocked. No yfinance dependency
for price at all; price/momentum has been reliable via this path all session.

Usage:
  python scripts/fetch_prices.py --tickers SHB-A.ST,INVE-A.ST,AAPL
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_fundamentals import fetch_price_momentum  # noqa: E402


def fetch_prices(tickers):
    out = {}
    for t in tickers:
        out[t] = fetch_price_momentum(t)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--tickers", required=True, help="Comma-separated equity/ETF tickers")
    args = p.parse_args()
    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]

    data = fetch_prices(tickers)
    os.makedirs("data/cache/prices", exist_ok=True)
    fname = f"data/cache/prices/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(), "prices": data}, f, indent=2)

    print(f"Wrote {fname}")
    for t, rec in data.items():
        if rec.get("error"):
            print(f"  ERROR  {t:<14s} {rec['error']}")
        else:
            print(f"  OK     {t:<14s} {rec.get('price')} {rec.get('currency')}")
    return fname


if __name__ == "__main__":
    main()
