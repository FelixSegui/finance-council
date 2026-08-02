#!/usr/bin/env python3
"""
Equity FUNDAMENTALS only (US-listed filers) — separated from price so a
fundamentals-fetch failure is isolated from a price-fetch failure.

Tries yfinance's quoteSummary first (richer fields — beta, recommendation,
sector, industry — when it works), falls back to SEC EDGAR
(`fetch_fundamentals.py:fetch_sec_fundamentals`) when it doesn't. Non-US
tickers correctly return "no free source" — SEC EDGAR is US-filer-only and
there is no free non-US fundamentals API; this is a structural limit, not a
bug to chase (see SYSTEM.md).

Usage:
  python scripts/fetch_fundamentals_us.py --tickers AAPL,MSFT
  python scripts/fetch_fundamentals_us.py --tickers AAPL:0000320193  # explicit CIK, skips lookup
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_fundamentals import fetch_sec_fundamentals, resolve_ciks  # noqa: E402


def fetch_fundamentals(tickers):
    """tickers: list of 'TICKER' or 'TICKER:CIK'. Tries yfinance first (richer
    fields), falls back to SEC EDGAR. Non-US tickers (no CIK resolvable) get
    an explicit 'no free source' — not a guess."""
    plain, explicit_cik = [], {}
    for t in tickers:
        tk, _, cik = t.partition(":")
        plain.append(tk)
        if cik:
            explicit_cik[tk] = cik

    out = {}
    try:
        import yfinance as yf
        yf_available = True
    except ImportError:
        yf_available = False

    need_sec = []
    for t in plain:
        if yf_available:
            try:
                info = yf.Ticker(t).info
                if info and info.get("trailingPE") is not None or info.get("profitMargins") is not None:
                    out[t] = {
                        "trailing_pe": info.get("trailingPE"), "forward_pe": info.get("forwardPE"),
                        "peg_ratio": info.get("pegRatio"), "market_cap": info.get("marketCap"),
                        "dividend_yield": info.get("dividendYield"), "beta": info.get("beta"),
                        "revenue_growth": info.get("revenueGrowth"), "profit_margins": info.get("profitMargins"),
                        "debt_to_equity": info.get("debtToEquity"), "recommendation": info.get("recommendationKey"),
                        "sector": info.get("sector"), "industry": info.get("industry"),
                        "country": info.get("country"), "_source": "yfinance",
                    }
                    continue
            except Exception:
                pass
        need_sec.append(t)

    if need_sec:
        ciks = dict(explicit_cik)
        lookup_needed = [t for t in need_sec if t not in ciks]
        if lookup_needed:
            resolved = resolve_ciks(lookup_needed)
            lookup_err = resolved.pop("_lookup_error", None)
            ciks.update({t: c for t, c in resolved.items() if c})
            if lookup_err:
                for t in lookup_needed:
                    if t not in ciks:
                        out.setdefault(t, {"error": f"CIK lookup failed (and not in the cached "
                                                    f"S&P 500 metadata): {lookup_err}"})
        for t in need_sec:
            if t in out:
                continue
            cik = ciks.get(t)
            if not cik:
                out[t] = {"error": "no free fundamentals source (non-US ticker or unmapped CIK — "
                                   "SEC EDGAR is US-listed-filer only)"}
                continue
            rec = fetch_sec_fundamentals(cik)
            # normalize field names against the yfinance branch above (SEC's
            # own schema uses "profit_margin", singular — a real inconsistency
            # caught while wiring the two paths together; fixed here so every
            # caller sees one consistent key regardless of which path served it)
            if not rec.get("error") and "profit_margin" in rec:
                rec["profit_margins"] = rec.pop("profit_margin")
            rec["_source"] = rec.get("_source", "sec_edgar_companyfacts")
            out[t] = rec
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--tickers", required=True, help="Comma-separated, optionally TICKER:CIK")
    args = p.parse_args()
    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]

    data = fetch_fundamentals(tickers)
    os.makedirs("data/cache/fundamentals", exist_ok=True)
    fname = f"data/cache/fundamentals/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(), "fundamentals": data}, f, indent=2)

    print(f"Wrote {fname}")
    for t, rec in data.items():
        if rec.get("error"):
            print(f"  N/A    {t:<10s} {rec['error']}")
        else:
            print(f"  OK     {t:<10s} PE={rec.get('trailing_pe')} margin={rec.get('profit_margins')} "
                  f"src={rec.get('_source','sec_edgar')}")
    return fname


if __name__ == "__main__":
    main()
