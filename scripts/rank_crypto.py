#!/usr/bin/env python3
"""
Crypto CONTEXT for the high-risk tier — deliberately NOT a buy-ranker.

Stocks get factor-ranked because they have fundamentals (earnings, margins,
growth). Crypto has none of that, so "value" and "quality" are undefined and
any composite score pretending otherwise would be false confidence — exactly
what this system forbids. What crypto DOES have is measurable cycle context:
momentum, distance from all-time high, market-cap rank, and market-wide
sentiment. This tool surfaces that context so the user can manage the
actively-traded high-risk tier on an informed discretionary basis. It orders by
momentum for readability; that ordering is NOT a recommendation and NOT a
signal to buy a new coin.

Sources (free, no key): CoinGecko markets + alternative.me Fear & Greed —
both already used by fetch_market_data.py and reachable through the proxy.

CoinGecko IDs must be exact (bitcoin, ethereum, solana...) — a wrong id is
silently dropped by the API, so verify ids, never guess. Defaults cover the
user's holdings (BTC, ETH) plus major-cap context.

Usage:
  python scripts/rank_crypto.py
  python scripts/rank_crypto.py --coins bitcoin,ethereum,solana
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_market_data import fetch_crypto, fetch_crypto_fear_greed  # noqa: E402

# Held by the user (BTC via ISK certificate, ETH self-custody) + major-cap
# context. IDs are CoinGecko ids, not tickers — verified against the API.
DEFAULT_COINS = [
    "bitcoin", "ethereum", "solana", "binancecoin",
    "ripple", "cardano", "avalanche-2", "chainlink",
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--coins", default=",".join(DEFAULT_COINS),
                   help="CoinGecko coin ids (verify — wrong ids are dropped)")
    args = p.parse_args()
    coins = [c.strip() for c in args.coins.split(",") if c.strip()]

    data = fetch_crypto(coins)
    if "error" in data:
        sys.exit(f"CoinGecko fetch failed: {data['error']}")
    fng = fetch_crypto_fear_greed()

    rows = []
    for cid in coins:
        d = data.get(cid)
        if not d:
            rows.append({"coin": cid, "error": "not returned by CoinGecko (check id)"})
            continue
        rows.append({
            "coin": cid,
            "price_eur": d.get("price_eur"),
            "market_cap_rank": d.get("market_cap_rank"),
            "change_7d_pct": d.get("change_7d_pct"),
            "change_30d_pct": d.get("change_30d_pct"),
            "pct_below_ath": d.get("ath_change_pct"),  # negative = below ATH
        })
    # order by 30d momentum for readability only (NOT a ranking of quality)
    rows.sort(key=lambda r: (r.get("change_30d_pct") is None, -(r.get("change_30d_pct") or 0)))

    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "disclaimer": ("CONTEXT ONLY for discretionary high-risk-tier management. "
                       "Ordered by 30d momentum for readability. NOT a buy-ranker, "
                       "NOT a signal to acquire new coins, NOT a return forecast. "
                       "Crypto has no fundamentals to standardise on."),
        "market_sentiment": {"crypto_fear_greed": fng},
        "context": rows,
    }
    os.makedirs("data/cache/rankings", exist_ok=True)
    fname = f"data/cache/rankings/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-crypto.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {fname}")
    fg = fng.get("value")
    print(f"Market Fear & Greed: {fg} ({fng.get('classification','?')})  "
          "— context for timing, not a trigger\n")
    print(f"{'COIN':<14}{'RANK':>5}{'PRICE_EUR':>12}{'7d%':>8}{'30d%':>8}{'vs ATH%':>9}")
    for r in rows:
        if r.get("error"):
            print(f"{r['coin']:<14}  {r['error']}")
            continue
        def f(x, d=1): return f"{x:>7.{d}f}" if x is not None else "      ."
        print(f"{r['coin']:<14}{(r['market_cap_rank'] or '.'):>5}"
              f"{(r['price_eur'] or 0):>12.2f}{f(r['change_7d_pct'])}"
              f"{f(r['change_30d_pct'])}{f(r['pct_below_ath']):>9}")
    print("\nReminder: high-risk tier is capped at 10% and managed on your thesis, "
          "not this table. Trim proceeds default to the secure tier.")


if __name__ == "__main__":
    main()
