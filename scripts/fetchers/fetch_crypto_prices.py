#!/usr/bin/env python3
"""
Crypto PRICE data only (CoinGecko) — separated so a CoinGecko outage is
isolated from equity/macro fetch problems.

Usage:
  python scripts/fetch_crypto_prices.py --coins bitcoin,ethereum
"""
import argparse
import json
import os
import urllib.request
from datetime import datetime, timezone


def fetch_crypto(coin_ids):
    if not coin_ids:
        return {}
    ids = ",".join(coin_ids)
    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        f"?vs_currency=eur&ids={ids}&order=market_cap_desc"
        "&price_change_percentage=24h,7d,30d"
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        out = {}
        for coin in data:
            out[coin["id"]] = {
                "price_eur": coin.get("current_price"),
                "market_cap": coin.get("market_cap"),
                "market_cap_rank": coin.get("market_cap_rank"),
                "change_24h_pct": coin.get("price_change_percentage_24h_in_currency"),
                "change_7d_pct": coin.get("price_change_percentage_7d_in_currency"),
                "change_30d_pct": coin.get("price_change_percentage_30d_in_currency"),
                "ath": coin.get("ath"),
                "ath_change_pct": coin.get("ath_change_percentage"),
            }
        return out
    except Exception as e:
        return {"error": str(e)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--coins", required=True, help="Comma-separated CoinGecko coin ids")
    args = p.parse_args()
    coins = [c.strip() for c in args.coins.split(",") if c.strip()]

    data = fetch_crypto(coins)
    os.makedirs("data/cache/crypto", exist_ok=True)
    fname = f"data/cache/crypto/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(), "crypto": data}, f, indent=2)

    print(f"Wrote {fname}")
    if "error" in data:
        print(f"  ERROR  {data['error']}")
    else:
        for cid, rec in data.items():
            print(f"  OK     {cid:<14s} {rec.get('price_eur')} EUR  30d={rec.get('change_30d_pct')}%")
    return fname


if __name__ == "__main__":
    main()
