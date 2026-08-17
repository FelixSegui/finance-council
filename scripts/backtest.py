#!/usr/bin/env python3
"""
Replay a proposed allocation over historical data. This is NOT prediction —
past returns don't repeat. Its one honest use: showing the volatility and
drawdown you would have had to sit through, so an allocation isn't chosen
on return alone.

Monthly rebalancing to target weights. Uses Yahoo adjusted closes in
each ticker's native currency — FX drift between USD/EUR/SEK legs is NOT
modeled; the report says so.

Usage:
  python backtest.py --allocation "VWCE.DE:0.7,BTC-USD:0.1,EUNL.DE:0.2" \
      --years 8 --benchmark VWCE.DE

DATA FETCH NOTE (added 2026-08-17, see CLAUDE.md's yfinance data-availability
note): yfinance's own Python client fails on this environment's network — its
curl_cffi-based browser-TLS-fingerprint impersonation gets connection-reset by
Yahoo's anti-bot layer, the same failure mode CLAUDE.md documents for
scripts/fetch_market_data.py. This script uses the identical fix: plain
urllib straight to Yahoo's v8 chart endpoint (no crumb/cookie needed for
price history, unlike the quoteSummary fundamentals endpoint), not
yfinance's yf.download(). This is a data-fetch mechanism change only — the
methodology (monthly adjusted closes, monthly rebalancing, dropna-based
overlap window) is unchanged from the original yfinance-backed version.
"""
import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone


CHART_UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


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


def _fetch_monthly_series(ticker, period1, period2, timeout=20, retries=3):
    """Direct Yahoo v8 chart endpoint fetch, monthly adjusted close.
    No crumb/cookie required for price history (only quoteSummary
    fundamentals need that). Returns a dict of {date: adj_close} or {}
    if the ticker has no usable data (caller treats it as missing)."""
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?period1={period1}&period2={period2}&interval=1mo")
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=CHART_UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode())
            result = (data.get("chart") or {}).get("result")
            if not result:
                return {}
            r = result[0]
            ts = r.get("timestamp") or []
            indicators = r.get("indicators", {})
            adj = (indicators.get("adjclose") or [{}])[0].get("adjclose")
            if not adj:
                adj = (indicators.get("quote") or [{}])[0].get("close")
            if not ts or not adj:
                return {}
            out = {}
            for t, v in zip(ts, adj):
                if v is None:
                    continue
                dt = datetime.fromtimestamp(t, tz=timezone.utc)
                # Bucket by (year, month) so tickers whose monthly bar lands
                # on a different day-of-month still align for rebalancing.
                key = (dt.year, dt.month)
                out[key] = v  # last value wins if duplicate bucket
            return out
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
                json.JSONDecodeError) as e:
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    print(f"  warning: failed to fetch {ticker} after {retries} attempts "
          f"({last_err}) — treated as missing", file=sys.stderr)
    return {}


def monthly_prices(tickers, years):
    """Returns a dict-of-dicts {ticker: {(year, month): price}} plus the
    sorted list of (year, month) keys actually observed for any ticker.
    Deliberately not a pandas DataFrame — avoids adding a hard pandas
    dependency just for this script; the arithmetic below is plain Python."""
    end = datetime.now(tz=timezone.utc)
    start = end - timedelta(days=int(years * 365.25))
    period1, period2 = int(start.timestamp()), int(end.timestamp())

    series = {}
    for i, t in enumerate(tickers):
        if i > 0:
            time.sleep(0.4)  # be polite to Yahoo's endpoint; avoid 429s
        s = _fetch_monthly_series(t, period1, period2)
        if s:
            series[t] = s
    return series


def simulate(series, alloc):
    """Monthly-rebalanced portfolio, value series starting at 1.0.
    Only months where every leg has data are used."""
    cols = [t for t in alloc if t in series]
    missing = [t for t in alloc if t not in series]
    if not cols:
        sys.exit(f"No usable price data for any of {list(alloc)}.")

    common_months = set(series[cols[0]].keys())
    for c in cols[1:]:
        common_months &= set(series[c].keys())
    months = sorted(common_months)

    if len(months) < 24:
        sys.exit(f"Fewer than 24 overlapping months of data for {cols} "
                 f"(missing entirely: {missing}). Backtest would be noise.")

    # returns[i] = return from months[i-1] to months[i], per ticker
    returns_by_month = []
    for i in range(1, len(months)):
        prev_m, cur_m = months[i - 1], months[i]
        port_ret = 0.0
        for t, w in alloc.items():
            if t not in series:
                continue
            p_prev = series[t][prev_m]
            p_cur = series[t][cur_m]
            if p_prev in (0, None) or p_cur is None:
                continue
            port_ret += w * (p_cur / p_prev - 1)
        returns_by_month.append(port_ret)

    value = [1.0]
    for r in returns_by_month:
        value.append(value[-1] * (1 + r))
    value = value[1:]  # align with returns_by_month (drop the seed 1.0)

    start_date = datetime(months[0][0], months[0][1], 1)
    end_date = datetime(months[-1][0], months[-1][1], 1)
    return value, returns_by_month, missing, start_date, end_date


def _mean(xs):
    return sum(xs) / len(xs)


def _std(xs):
    m = _mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) if len(xs) > 1 else 0.0


def metrics(value, returns):
    n_months = len(returns)
    years = n_months / 12
    cagr = value[-1] ** (1 / years) - 1
    vol = _std(returns) * math.sqrt(12)

    running_max = []
    m = float("-inf")
    for v in value:
        m = max(m, v)
        running_max.append(m)
    drawdowns = [v / rm - 1 for v, rm in zip(value, running_max)]
    max_drawdown = min(drawdowns)

    worst_12m = None
    if n_months > 12:
        rolling = [value[i] / value[i - 12] - 1 for i in range(12, n_months)]
        if rolling:
            worst_12m = min(rolling)

    mean_ret = _mean(returns)
    std_ret = _std(returns)
    sharpe = (mean_ret * 12) / (std_ret * math.sqrt(12)) if std_ret > 0 else None

    return {
        "months": n_months,
        "cagr_pct": round(cagr * 100, 2),
        "annual_vol_pct": round(vol * 100, 2),
        "max_drawdown_pct": round(max_drawdown * 100, 2),
        "worst_rolling_12m_pct": round(worst_12m * 100, 2) if worst_12m is not None else None,
        "sharpe_rf0": round(sharpe, 2) if sharpe is not None else None,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocation", required=True,
                        help='e.g. "VWCE.DE:0.7,BTC-USD:0.1,EUNL.DE:0.2"')
    parser.add_argument("--years", type=int, default=10)
    parser.add_argument("--benchmark", default="VWCE.DE")
    args = parser.parse_args()

    alloc = parse_allocation(args.allocation)
    tickers = sorted(set(list(alloc) + [args.benchmark]))
    series = monthly_prices(tickers, args.years)

    value, returns, missing, start, end = simulate(series, alloc)
    bench_value, bench_returns, _, _, _ = simulate(
        series, {args.benchmark: 1.0})

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
            "Data fetched via direct Yahoo v8 chart endpoint (urllib), not yfinance's client — "
            "see the module docstring; same underlying Yahoo data, different transport.",
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
