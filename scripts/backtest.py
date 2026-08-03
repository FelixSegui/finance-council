#!/usr/bin/env python3
"""
Replay a proposed allocation over historical data. This is NOT prediction —
past returns don't repeat. Its one honest use: showing the volatility and
drawdown you would have had to sit through, so an allocation isn't chosen
on return alone.

Monthly rebalancing to target weights. Uses yfinance adjusted closes in
each ticker's native currency — FX drift between USD/EUR/SEK legs is NOT
modeled; the report says so.

Usage:
  python backtest.py --allocation "VWCE.DE:0.7,BTC-USD:0.1,EUNL.DE:0.2" \
      --years 8 --benchmark VWCE.DE
"""
import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone


def parse_allocation(spec):
    alloc = {}
    for part in spec.split(","):
        ticker, _, weight = part.strip().partition(":")
        if not ticker or not weight:
            sys.exit(f"Bad allocation entry: '{part}'. Use TICKER:WEIGHT")
        alloc[ticker] = float(weight)
    total = sum(alloc.values())
    if abs(total - 1.0) > 0.001:
        sys.exit(f"Weights sum to {total}, must sum to 1.0")
    return alloc


def monthly_prices(tickers, years):
    import yfinance as yf
    data = yf.download(tickers, period=f"{years}y", interval="1mo",
                       auto_adjust=True, progress=False)["Close"]
    if len(tickers) == 1:
        data = data.to_frame(name=tickers[0])
    return data.dropna(how="all")


def simulate(prices, alloc):
    """Monthly-rebalanced portfolio, value series starting at 1.0.
    Only months where every leg has data are used."""
    cols = [t for t in alloc if t in prices.columns]
    missing = [t for t in alloc if t not in prices.columns]
    frame = prices[cols].dropna()
    if len(frame) < 24:
        sys.exit(f"Fewer than 24 overlapping months of data for {cols} "
                 f"(missing entirely: {missing}). Backtest would be noise.")
    returns = frame.pct_change().dropna()
    port_returns = sum(returns[t] * w for t, w in alloc.items() if t in cols)
    value = (1 + port_returns).cumprod()
    return value, port_returns, missing, frame.index[0], frame.index[-1]


def metrics(value, returns):
    n_months = len(returns)
    years = n_months / 12
    cagr = value.iloc[-1] ** (1 / years) - 1
    vol = returns.std() * math.sqrt(12)
    running_max = value.cummax()
    drawdown = value / running_max - 1
    worst_12m = (value.pct_change(12)).min() if n_months > 12 else None
    return {
        "months": n_months,
        "cagr_pct": round(cagr * 100, 2),
        "annual_vol_pct": round(vol * 100, 2),
        "max_drawdown_pct": round(drawdown.min() * 100, 2),
        "worst_rolling_12m_pct": round(worst_12m * 100, 2) if worst_12m is not None else None,
        "sharpe_rf0": round((returns.mean() * 12) / (returns.std() * math.sqrt(12)), 2),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocation", required=True,
                        help='e.g. "VWCE.DE:0.7,BTC-USD:0.1,EUNL.DE:0.2"')
    parser.add_argument("--years", type=int, default=10)
    parser.add_argument("--benchmark", default="VWCE.DE")
    args = parser.parse_args()

    try:
        import yfinance  # noqa: F401
    except ImportError:
        sys.exit("yfinance not installed. pip install yfinance")

    alloc = parse_allocation(args.allocation)
    tickers = sorted(set(list(alloc) + [args.benchmark]))
    prices = monthly_prices(tickers, args.years)

    value, returns, missing, start, end = simulate(prices, alloc)
    bench_value, bench_returns, _, _, _ = simulate(
        prices, {args.benchmark: 1.0})

    result = {
        "run_at_utc": datetime.now(timezone.utc).isoformat(),
        "allocation": alloc,
        "period": {"start": str(start.date()), "end": str(end.date())},
        "tickers_missing_data": missing,
        "caveats": [
            "Past performance is not predictive. Use for risk tolerance, not return expectation.",
            "FX drift between currency legs not modeled — each leg in native currency.",
            "No fees, taxes, or spreads modeled. ISK schablonskatt and fund fees reduce these numbers.",
            f"Only {round(len(returns)/12, 1)} years of overlapping data — short histories (esp. crypto) overweight recent regimes.",
        ],
        "portfolio": metrics(value, returns),
        "benchmark": {args.benchmark: metrics(bench_value, bench_returns)},
    }

    os.makedirs("data/cache/backtests", exist_ok=True)
    fname = f"data/cache/backtests/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {fname}")
    print(json.dumps({"portfolio": result["portfolio"],
                      "benchmark": result["benchmark"]}, indent=2))


if __name__ == "__main__":
    main()
