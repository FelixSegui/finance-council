#!/usr/bin/env python3
"""
Screen a candidate universe against hard numeric filters. This is the data
layer for the scout agent: it NARROWS a universe, it does not pick winners.

Reads data/universe.json (user-maintained), fetches current fundamentals
via yfinance, applies only the filters passed on the command line, and
writes the survivors + near-misses to data/screens/.

A candidate with a missing value for a filtered field is never silently
passed OR failed — it lands in "missing_data" so the scout agent can say
what it doesn't know.

Usage:
  python screen_candidates.py --categories us_mega_cap,nordic_large_cap \
      --max-pe 25 --min-revenue-growth 0.05 --max-debt-to-equity 150
  python screen_candidates.py --tickers AAPL,EVO.ST --max-pe 20
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_market_data import fetch_equities  # noqa: E402

UNIVERSE_PATH = "data/universe.json"

# (cli_name, snapshot_field, direction) — direction "max" means value must
# be <= threshold to pass, "min" means >=.
FILTERS = [
    ("max_pe", "trailing_pe", "max"),
    ("max_forward_pe", "forward_pe", "max"),
    ("max_peg", "peg_ratio", "max"),
    ("min_revenue_growth", "revenue_growth", "min"),
    ("min_profit_margin", "profit_margins", "min"),
    ("max_debt_to_equity", "debt_to_equity", "max"),
    ("min_dividend_yield", "dividend_yield", "min"),
    ("min_market_cap", "market_cap", "min"),
    ("max_beta", "beta", "max"),
]


def load_universe(categories):
    with open(UNIVERSE_PATH) as f:
        universe = json.load(f)
    cats = universe.get("categories", {})
    if categories == ["all"]:
        selected = cats.keys()
    else:
        unknown = [c for c in categories if c not in cats]
        if unknown:
            sys.exit(f"Unknown categories {unknown}. Available: {sorted(cats)}")
        selected = categories
    tickers = []
    for c in selected:
        tickers.extend(cats[c])
    return sorted(set(tickers))


def apply_filters(data, active_filters):
    passed, failed, missing = {}, {}, {}
    for ticker, fields in data.items():
        if "error" in fields:
            missing[ticker] = {"reason": fields["error"]}
            continue
        fail_reasons, missing_fields = [], []
        for cli_name, field, direction, threshold in active_filters:
            value = fields.get(field)
            if value is None:
                missing_fields.append(field)
                continue
            if direction == "max" and value > threshold:
                fail_reasons.append(f"{field}={value} > {threshold}")
            elif direction == "min" and value < threshold:
                fail_reasons.append(f"{field}={value} < {threshold}")
        if fail_reasons:
            failed[ticker] = {"reasons": fail_reasons}
        elif missing_fields:
            missing[ticker] = {"missing_fields": missing_fields, "data": fields}
        else:
            passed[ticker] = fields
    return passed, failed, missing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--categories", default="all",
                        help="Comma-separated category names from universe.json, or 'all'")
    parser.add_argument("--tickers", default="",
                        help="Screen these tickers instead of the universe file")
    for cli_name, _field, _direction in FILTERS:
        parser.add_argument(f"--{cli_name.replace('_', '-')}", type=float, default=None)
    args = parser.parse_args()

    if args.tickers:
        tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]
    else:
        tickers = load_universe([c.strip() for c in args.categories.split(",")])

    active = []
    for cli_name, field, direction in FILTERS:
        threshold = getattr(args, cli_name)
        if threshold is not None:
            active.append((cli_name, field, direction, threshold))
    if not active:
        sys.exit("No filters given — refusing to run an unfiltered screen. "
                 "Pass at least one, e.g. --max-pe 25")

    print(f"Fetching {len(tickers)} tickers...", file=sys.stderr)
    data = fetch_equities(tickers)
    if "error" in data and len(data) == 1:
        sys.exit(data["error"])

    passed, failed, missing = apply_filters(data, active)

    result = {
        "screened_at_utc": datetime.now(timezone.utc).isoformat(),
        "filters": [f"{c} {d} {t}" for c, _f, d, t in active],
        "universe_size": len(tickers),
        "passed": passed,
        "missing_data": missing,
        "failed": failed,
    }
    os.makedirs("data/screens", exist_ok=True)
    fname = f"data/screens/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-screen.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {fname}")
    print(f"Passed: {sorted(passed)}")
    print(f"Missing data (not failed, not passed): {sorted(missing)}")
    print(f"Failed: {len(failed)} tickers")


if __name__ == "__main__":
    main()
