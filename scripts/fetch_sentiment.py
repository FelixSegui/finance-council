#!/usr/bin/env python3
"""
Crypto Fear & Greed sentiment index only (alternative.me) — separated because
it's a distinct source from CoinGecko's price data, and market-wide sentiment
context is used differently (timing signal) than price (valuation input).

Usage:
  python scripts/fetch_sentiment.py
"""
import json
import os
import urllib.request
from datetime import datetime, timezone


def fetch_crypto_fear_greed():
    try:
        req = urllib.request.Request("https://api.alternative.me/fng/?limit=1")
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        d = data["data"][0]
        return {"value": int(d["value"]), "classification": d["value_classification"]}
    except Exception as e:
        return {"error": str(e)}


def main():
    data = fetch_crypto_fear_greed()
    os.makedirs("data/cache/sentiment", exist_ok=True)
    fname = f"data/cache/sentiment/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(),
                   "crypto_fear_greed": data}, f, indent=2)
    print(f"Wrote {fname}")
    print(f"  {data}")
    return fname


if __name__ == "__main__":
    main()
