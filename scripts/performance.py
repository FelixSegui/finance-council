#!/usr/bin/env python3
"""
Track whether the whole system beats "just buy the index".

Reads data/valuations.csv — a manually maintained log of portfolio value
observations (the journal agent reminds you to append one per sweep):

    date,total_value_sek,net_contribution_since_last_sek,note

Builds a shadow portfolio: every net contribution buys benchmark units
(converted to SEK via EURSEK) on its observation date. Compares actual
value today vs what the same money in the benchmark would be worth.

This is honest only if valuations.csv is honest — garbage in, garbage out.

Usage:
  python performance.py --benchmark VWCE.DE
"""
import argparse
import csv
import os
import sys
from datetime import datetime, timezone

VALUATIONS_PATH = "data/valuations.csv"


def _num(raw, field, date):
    """Parse a numeric CSV cell that a human may have annotated (this file is
    hand-appended, and a real row reads `0 (no confirmed contribution
    logged)`). Take the leading number and keep the annotation out of the
    math; refuse rows with no number at all rather than assuming zero."""
    if raw is None or str(raw).strip() == "":
        return 0.0
    head = str(raw).strip().split()[0].replace(",", "")
    try:
        return float(head)
    except ValueError:
        sys.exit(f"{VALUATIONS_PATH}: row {date} has an unparseable "
                 f"{field}: {raw!r}. Fix the row; do not guess it.")


def load_valuations():
    rows = []
    try:
        with open(VALUATIONS_PATH) as f:
            for row in csv.DictReader(f):
                rows.append({
                    "date": datetime.strptime(row["date"], "%Y-%m-%d"),
                    "value": _num(row["total_value_sek"], "total_value_sek", row["date"]),
                    "contribution": _num(row["net_contribution_since_last_sek"],
                                         "net_contribution_since_last_sek", row["date"]),
                    "note": row.get("note", ""),
                })
    except FileNotFoundError:
        sys.exit(f"{VALUATIONS_PATH} not found. Create it with header: "
                 "date,total_value_sek,net_contribution_since_last_sek,note")
    if len(rows) < 2:
        sys.exit("Need at least 2 valuation rows to measure anything. "
                 f"Currently {len(rows)}. Keep logging; come back next sweep.")
    return sorted(rows, key=lambda r: r["date"])


def benchmark_prices_sek(benchmark, start):
    """{(year, month): benchmark price in SEK}, fetched through the same
    direct Yahoo v8 chart path scripts/backtest.py uses. yfinance's own client
    does not work on this network (see CLAUDE.md's Yahoo note), and this
    script used to depend on it — a benchmark comparison that silently could
    not run is worse than none.

    A month is only usable when BOTH the benchmark and the FX rate have a
    bar; a month with one and not the other is dropped, never carried."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from backtest import _fetch_monthly_series
    period1 = int(start.replace(tzinfo=timezone.utc).timestamp()) - 60 * 86400
    period2 = int(datetime.now(timezone.utc).timestamp())
    bench = _fetch_monthly_series(benchmark, period1, period2)
    fx = _fetch_monthly_series("EURSEK=X", period1, period2)
    if not bench:
        raise RuntimeError(f"no price history returned for {benchmark}")
    if not fx:
        raise RuntimeError("no EURSEK history returned — refusing to assume a rate")
    return {k: bench[k] * fx[k] for k in sorted(set(bench) & set(fx))}


def nearest_price(prices, when):
    """Most recent monthly bar at or before `when`. None if there is none —
    never the closest bar in either direction, which would use a future price."""
    key = (when.year, when.month)
    eligible = [k for k in prices if k <= key]
    return float(prices[max(eligible)]) if eligible else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", default="VWCE.DE",
                        help="EUR-denominated benchmark ticker (converted via EURSEK)")
    args = parser.parse_args()

    rows = load_valuations()
    try:
        prices = benchmark_prices_sek(args.benchmark, rows[0]["date"])
    except Exception as e:
        sys.exit(f"Benchmark fetch failed: {e}")

    # First row's full value counts as the opening contribution
    shadow_units = 0.0
    contributions = []
    for i, row in enumerate(rows):
        amount = row["value"] if i == 0 else row["contribution"]
        if amount == 0:
            continue
        px = nearest_price(prices, row["date"])
        if px is None:
            sys.exit(f"No benchmark price on/before {row['date'].date()}")
        shadow_units += amount / px
        contributions.append(amount)

    latest_px = float(prices[max(prices)])
    shadow_value = shadow_units * latest_px
    actual_value = rows[-1]["value"]
    total_in = sum(contributions)

    print(f"Period: {rows[0]['date'].date()} -> {rows[-1]['date'].date()} "
          f"({len(rows)} observations)")
    print(f"Total money in:                {total_in:>12,.0f} SEK")
    print(f"Actual portfolio value:        {actual_value:>12,.0f} SEK "
          f"({(actual_value/total_in - 1)*100:+.1f}%)")
    print(f"Same money in {args.benchmark}:  {shadow_value:>12,.0f} SEK "
          f"({(shadow_value/total_in - 1)*100:+.1f}%)")
    diff = actual_value - shadow_value
    print(f"Difference vs benchmark:       {diff:>+12,.0f} SEK")
    if diff < 0:
        print("The benchmark is winning. Before changing strategy, check "
              "whether the gap is explained by fees or wrapper drag — "
              "those are fixable without a view on markets.")


if __name__ == "__main__":
    main()
