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
import sys
from datetime import datetime

VALUATIONS_PATH = "data/valuations.csv"


def load_valuations():
    rows = []
    try:
        with open(VALUATIONS_PATH) as f:
            for row in csv.DictReader(f):
                rows.append({
                    "date": datetime.strptime(row["date"], "%Y-%m-%d"),
                    "value": float(row["total_value_sek"]),
                    "contribution": float(row["net_contribution_since_last_sek"] or 0),
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
    import yfinance as yf
    period_days = (datetime.now() - start).days + 30
    years = max(1, period_days // 365 + 1)
    data = yf.download([benchmark, "EURSEK=X"], period=f"{years}y",
                       interval="1d", auto_adjust=True, progress=False)["Close"]
    data = data.dropna()
    return data[benchmark] * data["EURSEK=X"]


def nearest_price(prices, when):
    eligible = prices[prices.index <= when.strftime("%Y-%m-%d")]
    if eligible.empty:
        return None
    return float(eligible.iloc[-1])


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

    latest_px = float(prices.iloc[-1])
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
