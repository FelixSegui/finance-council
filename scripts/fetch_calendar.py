#!/usr/bin/env python3
"""
Fetch upcoming market events relevant to the portfolio:
  - Earnings dates: yfinance, per ticker
  - Macro events (FOMC, Riksbank, CPI releases): data/macro_calendar.json,
    which is MANUALLY maintained — this script only filters it to the
    lookahead window. It never invents a date.

Writes data/cache/calendar/YYYYMMDD-events.json and prints a summary.

Usage:
  python fetch_calendar.py --tickers AAPL,EVO.ST --days 45
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_market_data import _yahoo_session, _raw  # noqa: E402

MACRO_CALENDAR_PATH = "data/macro_calendar.json"


def fetch_earnings_dates(tickers):
    """Earnings dates via the same direct urllib + crumb/cookie-jar bypass
    fetch_market_data.py already uses for fundamentals (see CLAUDE.md's
    yfinance note - yfinance's own client, and anything routing through it
    like the old yf.Ticker(t).calendar call this replaced, gets connection-
    reset by Yahoo's anti-bot layer on this network). Requests the
    calendarEvents module instead of the default fundamentals modules -
    no new API key, reuses code already proven reliable here (S3)."""
    out = {}
    for t in tickers:
        try:
            r = _yahoo_session.fetch_quote_summary(t, modules="calendarEvents")
            earnings = (r.get("calendarEvents") or {}).get("earnings") or {}
            raw_dates = earnings.get("earningsDate") or []
            dates = [d for d in (_raw(x) for x in raw_dates) if d is not None]
            if dates:
                out[t] = {
                    "next_earnings": [
                        datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
                        for ts in dates
                    ]
                }
            else:
                out[t] = {"next_earnings": None, "note": "no earnings date returned"}
        except Exception as e:
            out[t] = {"error": str(e)}
    return out


def load_macro_events(days):
    if not os.path.exists(MACRO_CALENDAR_PATH):
        return {"error": f"{MACRO_CALENDAR_PATH} not found"}
    with open(MACRO_CALENDAR_PATH) as f:
        cal = json.load(f)
    today = datetime.now(timezone.utc).date()
    horizon = today + timedelta(days=days)
    upcoming = []
    for event in cal.get("events", []):
        try:
            d = datetime.strptime(event["date"], "%Y-%m-%d").date()
        except (KeyError, ValueError):
            continue
        if today <= d <= horizon:
            upcoming.append(event)
    return {
        "upcoming": sorted(upcoming, key=lambda e: e["date"]),
        "calendar_last_verified": cal.get("last_verified"),
        "unverified_sources": cal.get("unverified_sources", []),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", default="", help="Comma-separated tickers")
    parser.add_argument("--days", type=int, default=45, help="Lookahead window in days")
    args = parser.parse_args()

    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]

    result = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "lookahead_days": args.days,
        "earnings": fetch_earnings_dates(tickers) if tickers else {},
        "macro_events": load_macro_events(args.days),
    }

    os.makedirs("data/cache/calendar", exist_ok=True)
    fname = f"data/cache/calendar/{datetime.now(timezone.utc).strftime('%Y%m%d')}-events.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {fname}")
    for ev in result["macro_events"].get("upcoming", []):
        print(f"  {ev['date']}  {ev['name']}")
    for t, info in result["earnings"].items():
        if info.get("next_earnings"):
            print(f"  {t} earnings: {info['next_earnings'][0]}")


if __name__ == "__main__":
    main()
