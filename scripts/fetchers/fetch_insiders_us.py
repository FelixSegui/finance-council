#!/usr/bin/env python3
"""
US corporate insider activity — SEC EDGAR Form 4 filing counts. Separated
from price/fundamentals fetch: insider signal is a distinct research question
("is management buying or selling") from valuation, and the failure modes
differ (CIK mapping lookups, filing-index parsing).

Count only — buy/sell direction requires parsing individual Form 4 XML, not
yet built (see data/cache/controller_state.json recommendation #5).

Usage:
  python scripts/fetch_insiders_us.py --tickers AAPL,MSFT
"""
import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_fundamentals import resolve_ciks, SEC_UA  # noqa: E402


def _get_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def fetch_insider_activity(tickers):
    out = {}
    us = [t for t in tickers if "." not in t]
    for t in tickers:
        if t not in us:
            out[t] = {"skipped": "non-US ticker, not covered by SEC EDGAR"}
    if not us:
        return out
    # Cache-first CIK resolution (see fetch_fundamentals.resolve_ciks) — the
    # live www.sec.gov ticker-mapping lookup has been observed 403-blocked at
    # the proxy level while data.sec.gov itself stays reachable; prefer the
    # already-fetched S&P 500 metadata cache and only hit the live lookup for
    # names not in it.
    ciks = resolve_ciks(us)
    lookup_err = ciks.pop("_lookup_error", None)
    cutoff = (datetime.now(timezone.utc) - timedelta(days=90)).strftime("%Y-%m-%d")
    for t in us:
        cik = ciks.get(t)
        if not cik:
            reason = "ticker not found in SEC CIK mapping"
            if lookup_err:
                reason += f" (live lookup also failed: {lookup_err})"
            out[t] = {"error": reason}
            continue
        try:
            subs = _get_json(f"https://data.sec.gov/submissions/CIK{cik}.json", headers=SEC_UA)
            recent = subs["filings"]["recent"]
            form4_dates = [d for f, d in zip(recent["form"], recent["filingDate"])
                          if f == "4" and d >= cutoff]
            out[t] = {"form4_filings_90d": len(form4_dates),
                      "latest_form4_date": max(form4_dates) if form4_dates else None,
                      "note": "filing count only; direction (buy vs sell) not extracted"}
        except Exception as e:
            out[t] = {"error": str(e)}
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--tickers", required=True, help="Comma-separated tickers")
    args = p.parse_args()
    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]

    data = fetch_insider_activity(tickers)
    os.makedirs("data/cache/insiders_us", exist_ok=True)
    fname = f"data/cache/insiders_us/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(), "insiders": data}, f, indent=2)

    print(f"Wrote {fname}")
    for t, rec in data.items():
        print(f"  {t:<10s} {rec}")
    return fname


if __name__ == "__main__":
    main()
