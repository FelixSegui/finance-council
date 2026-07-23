#!/usr/bin/env python3
"""
Add tickers to a user-maintained universe category — WITH VALIDATION.

The universe's non-US categories can't be auto-sourced (the constituent lists
live on proxy-blocked sites), so they're maintained by hand. Hand-maintained is
exactly where a wrong or hallucinated ticker slips in — especially for
`.PA`/`.AS`/`.DE`/`.MI`/`.CO` European formats. This script closes that hole:
it fetches each proposed ticker's price history from Yahoo's chart endpoint (the
reachable one) and adds ONLY the ones that return real data. Anything that
doesn't resolve is reported and dropped, never written.

It does NOT invent tickers — you pass the list; it verifies the list.

Usage:
  python scripts/add_manual_tickers.py --category europe_large_cap \
      --tickers ASML.AS,SAP.DE,MC.PA,NOVO-B.CO
"""
import argparse
import json
import sys
import os
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_fundamentals import fetch_price_momentum  # noqa: E402

UNIVERSE_PATH = "data/universe.json"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--category", required=True)
    p.add_argument("--tickers", required=True, help="comma-separated")
    p.add_argument("--source", default="manual_validated")
    args = p.parse_args()

    proposed = [t.strip() for t in args.tickers.split(",") if t.strip()]
    with open(UNIVERSE_PATH) as f:
        uni = json.load(f)

    valid, dropped = [], []
    for t in proposed:
        px = fetch_price_momentum(t)
        time.sleep(0.1)
        if px.get("error") or not px.get("price"):
            dropped.append((t, px.get("error", "no price")))
        else:
            valid.append((t, px.get("currency")))
            print(f"  OK   {t:12s} {px.get('currency')}  {px.get('price'):.2f}")

    for t, reason in dropped:
        print(f"  DROP {t:12s} {reason}", file=sys.stderr)

    if not valid:
        sys.exit("No tickers validated — nothing written.")

    cats = uni.setdefault("categories", {})
    meta = uni.setdefault("metadata", {})
    existing = set(cats.get(args.category, []))
    for t, cur in valid:
        existing.add(t)
        meta[t] = {"name": meta.get(t, {}).get("name"), "sector": None,
                   "cik": None, "currency": cur, "source": args.source}
    cats[args.category] = sorted(existing)

    manual = set(uni.get("manual_categories", []))
    manual.add(args.category)
    uni["manual_categories"] = sorted(manual)
    uni["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with open(UNIVERSE_PATH, "w") as f:
        json.dump(uni, f, indent=2)
    print(f"\nAdded {len(valid)} validated tickers to '{args.category}' "
          f"({len(dropped)} dropped). Wrote {UNIVERSE_PATH}")


if __name__ == "__main__":
    main()
