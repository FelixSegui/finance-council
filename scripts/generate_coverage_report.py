#!/usr/bin/env python3
"""
Data-coverage report: exactly what was fetched this sweep, what wasn't, and
why — for both your actual holdings and the screening universe/funnel.

This is diagnostic, not a portfolio-vs-market performance tracker (that's
scripts/performance.py + data/valuations.csv). It answers a narrower,
recurring question that used to be buried in prose notes across
portfolio.json and SESSION_LOG.md: for THIS sweep, which numbers are real
and fresh, which are stale, which are missing, and — for holdings
specifically — how many consecutive sweeps has a given ticker been failing.

Reads (never fetches — run fetch_market_data.py first):
  - the latest data/cache/snapshots/*.json  (this sweep's holdings-relevant fetch)
  - data/sync/portfolio.json           (what SHOULD have been fetched — synced
                                        from master.xlsx's Portfolio sheet by
                                        `python run.py sync`, run this first)
  - the latest data/cache/rankings/*.json, if present (candidate/universe coverage)
  - data/cache/universe.json           (structural: which categories even
                                        HAVE a free fundamentals source)

Writes (machine-owned JSON/CSV only — the narrative "Missing data" section of
the sweep report is written by whoever assembles reports/YYYY-MM-DD-sweep.md,
sourced from this file, per the one-report-per-sweep rule):
  - data/cache/coverage_reports/TIMESTAMP-summary.json (holdings coverage +
    universe summary, structured)
  - data/cache/coverage_reports/TIMESTAMP-universe-coverage.csv (full per-ticker
    universe table, for Excel-style filtering)
  - data/cache/coverage_reports/_streak_state.json (internal: consecutive
    missing/error counts per holding ticker, carried sweep to sweep)

Usage:
  python run.py sync   # first, so data/sync/portfolio.json is current
  python scripts/generate_coverage_report.py
  # or: python run.py coverage
"""
import csv
import glob
import json
import os
import sys
from datetime import datetime, timezone

SNAPSHOTS_GLOB = "data/cache/snapshots/*.json"
RANKINGS_GLOB = "data/cache/rankings/2*-ranking.json"
PORTFOLIO_PATH = "data/sync/portfolio.json"
UNIVERSE_PATH = "data/cache/universe.json"
COVERAGE_DIR = "data/cache/coverage_reports"
STREAK_STATE_PATH = f"{COVERAGE_DIR}/_streak_state.json"

# Fields that, if present and non-null, mean "fundamentals actually landed"
# for an equity record — used to tell OK-with-fundamentals apart from
# OK-price-only (the fallback path's honest partial result).
FUNDAMENTAL_FIELDS = ["trailing_pe", "profit_margins", "revenue_growth", "market_cap"]


def latest(pattern):
    files = sorted(glob.glob(pattern))
    return files[-1] if files else None


def load_json(path):
    with open(path) as f:
        return json.load(f)


def load_streak_state():
    if os.path.exists(STREAK_STATE_PATH):
        return load_json(STREAK_STATE_PATH)
    return {}


def save_streak_state(state):
    os.makedirs(COVERAGE_DIR, exist_ok=True)
    with open(STREAK_STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def classify_holding(h, snapshot_equities, snapshot_crypto):
    """Return (status, detail, fields_present, fields_missing, manual_fields)
    for one holding. fields_missing is what makes this actionable — the exact
    field names to go fill in on the Manual Data sheet, not just a status
    word."""
    ticker = h.get("ticker")
    itype = h.get("instrument_type")

    if itype == "cash" or ticker in ("CASH_SEK", "CASH_USD", "CASH_EUR"):
        return "N/A", "cash — not a market instrument", [], [], []

    if ticker == "TBD":
        permanent_reason = h.get("no_ticker_reason")
        if permanent_reason:
            return "N/A (permanent)", permanent_reason, [], [], []
        return "N/A", "no resolved ticker/ISIN on file yet — cannot be fetched until named", [], [], []

    if itype == "spot_crypto" or ticker == "ethereum":
        rec = snapshot_crypto.get(ticker or "ethereum")
        if rec is None:
            return "MISSING", "not included in this sweep's --crypto fetch list", [], [], []
        if "error" in rec:
            return "ERROR", rec["error"], [], [], []
        wanted = ("price_eur", "change_24h_pct", "change_7d_pct")
        present = [k for k in wanted if rec.get(k) is not None]
        missing = [k for k in wanted if rec.get(k) is None]
        return "OK", f"CoinGecko, {len(present)} fields", present, missing, []

    # equity / certificate / fund-with-ticker
    rec = snapshot_equities.get(ticker)
    if rec is None:
        return "MISSING", "not included in this sweep's --tickers fetch list", [], FUNDAMENTAL_FIELDS, []
    if "error" in rec:
        return "ERROR", rec["error"], [], FUNDAMENTAL_FIELDS, []
    manual = list((rec.get("_manual_overrides") or {}).keys())
    fund_present = [k for k in FUNDAMENTAL_FIELDS if rec.get(k) is not None]
    fund_missing = [k for k in FUNDAMENTAL_FIELDS if rec.get(k) is None]
    has_price = rec.get("price") is not None
    if not has_price:
        return "ERROR", "fetched but price field is null", [], fund_missing, manual
    if fund_present and manual:
        return "OK (incl. manual)", f"price + {len(fund_present)} fields ({len(manual)} manually supplied)", \
            fund_present, fund_missing, manual
    if fund_present:
        return "OK", f"price + {len(fund_present)} fundamentals fields", fund_present, fund_missing, manual
    reason = rec.get("_fundamentals_unavailable_reason")
    detail = reason or "price fetched; fundamentals fields all null"
    if fund_missing:
        detail += f" — missing: {', '.join(fund_missing)} (fillable via the Manual Data sheet)"
    return "OK (price only)", detail, [], fund_missing, manual


def build_holdings_table(portfolio, snapshot):
    equities = snapshot.get("equities", {}) if snapshot else {}
    crypto = snapshot.get("crypto", {}) if snapshot else {}
    if isinstance(equities, dict) and "error" in equities and len(equities) == 1:
        equities = {}  # top-level fetch failure (e.g. import error) — treat as "nothing fetched"

    streaks = load_streak_state()
    rows = []
    # portfolio is the synced output of sync.py: {"rows": [...]}, one dict per
    # Portfolio-sheet row, column names from data/sync/schema.py
    for h in portfolio.get("rows", []):
        status, detail, present, missing, manual = classify_holding(h, equities, crypto)
        key = f"{h.get('ticker')}|{h.get('account_id')}"
        if status in ("MISSING", "ERROR"):
            streaks[key] = streaks.get(key, 0) + 1
        elif status.startswith("OK"):
            streaks[key] = 0
        streak = streaks.get(key, 0)
        rows.append({
            "ticker": h.get("ticker"),
            "name": h.get("name"),
            "account": h.get("account_id"),
            "status": status,
            "detail": detail,
            "fields_missing": missing,
            "fields_manual": manual,
            "consecutive_sweeps_missing": streak if status in ("MISSING", "ERROR") else "",
        })
    save_streak_state(streaks)
    return rows


def build_universe_summary():
    """Structural (does a free fundamentals source even exist) + empirical
    (what the last funnel run actually got) coverage, by universe category."""
    if not os.path.exists(UNIVERSE_PATH):
        return None, None
    universe = load_json(UNIVERSE_PATH)
    cats = universe.get("categories", {})
    meta = universe.get("metadata", {})
    structural = []
    for c, tickers in cats.items():
        with_cik = sum(1 for t in tickers if (meta.get(t) or {}).get("cik"))
        structural.append({
            "category": c, "count": len(tickers), "with_free_fundamentals_source": with_cik,
        })

    ranking_path = latest(RANKINGS_GLOB)
    empirical = None
    ticker_rows = []
    if ranking_path:
        d = load_json(ranking_path)
        empirical = {
            "ranking_file": ranking_path,
            "generated_utc": d.get("generated_utc"),
            "universe_categories": d.get("universe_categories"),
            "coverage": d.get("coverage"),
        }
        for r in d.get("ranking", []):
            ticker_rows.append({
                "ticker": r["ticker"], "name": r.get("name") or "", "bucket": "full-factor",
                "composite": r.get("composite"), "data_risk_score": r.get("data_risk_score"),
                "sector_or_source": r.get("sector") or r.get("thesis_source") or "",
            })
        for r in d.get("momentum_only_ranking", []):
            ticker_rows.append({
                "ticker": r["ticker"], "name": r.get("name") or "", "bucket": "momentum-only",
                "composite": "", "data_risk_score": r.get("data_risk_score"),
                "sector_or_source": r.get("currency") or r.get("thesis_source") or "",
            })
        for r in d.get("partial_data", []):
            ticker_rows.append({
                "ticker": r["ticker"], "name": r.get("name") or "", "bucket": "no-data",
                "composite": "", "data_risk_score": "",
                "sector_or_source": r.get("reason", ""),
            })
    return {"structural": structural, "empirical": empirical}, ticker_rows


def write_universe_csv(ticker_rows):
    os.makedirs(COVERAGE_DIR, exist_ok=True)
    fname = f"{COVERAGE_DIR}/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-universe-coverage.csv"
    with open(fname, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ticker", "name", "bucket", "composite",
                                           "data_risk_score", "sector_or_source"])
        w.writeheader()
        for r in sorted(ticker_rows, key=lambda r: (r["bucket"], r["ticker"])):
            w.writerow(r)
    return fname


def write_json_summary(snapshot_path, snapshot, holdings_rows, universe_summary):
    """Machine-readable coverage summary — data/cache/, not reports/. This
    script no longer writes its own markdown report: under the consolidated
    reporting rule (one reports/YYYY-MM-DD-sweep.md per sweep), the "Missing
    data" section of that single file is written by whoever assembles the
    sweep report (core-council.md), sourced from this JSON — not a second,
    competing markdown file."""
    n_ok = sum(1 for r in holdings_rows if r["status"] == "OK")
    n_partial = sum(1 for r in holdings_rows if r["status"].startswith("OK") and r["status"] != "OK")
    n_na = sum(1 for r in holdings_rows if r["status"].startswith("N/A"))
    n_missing = len(holdings_rows) - n_ok - n_partial - n_na
    stuck = [r for r in holdings_rows if isinstance(r["consecutive_sweeps_missing"], int)
             and r["consecutive_sweeps_missing"] >= 2]

    summary = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "snapshot_used": snapshot_path,
        "snapshot_fetched_at": snapshot.get("fetched_at_utc") if snapshot else None,
        "holdings": holdings_rows,
        "holdings_summary": {"ok": n_ok, "price_only": n_partial, "missing_or_error": n_missing, "na": n_na},
        "stuck_2plus_sweeps": stuck,
        "universe_summary": universe_summary,
    }
    os.makedirs(COVERAGE_DIR, exist_ok=True)
    fname = f"{COVERAGE_DIR}/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-summary.json"
    with open(fname, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    return fname, summary


def main():
    snapshot_path = latest(SNAPSHOTS_GLOB)
    snapshot = load_json(snapshot_path) if snapshot_path else None
    portfolio = load_json(PORTFOLIO_PATH)

    holdings_rows = build_holdings_table(portfolio, snapshot)
    universe_summary, ticker_rows = build_universe_summary()

    json_path, summary = write_json_summary(snapshot_path, snapshot, holdings_rows, universe_summary)
    csv_path = write_universe_csv(ticker_rows) if ticker_rows else None

    print(f"Wrote {json_path}")
    if csv_path:
        print(f"Wrote {csv_path} ({len(ticker_rows)} tickers)")
    s = summary["holdings_summary"]
    print(f"\nSummary: {s['ok']} OK, {s['price_only']} price-only, "
          f"{s['missing_or_error']} missing/error, {s['na']} N/A")
    if summary["stuck_2plus_sweeps"]:
        print(f"Flagged (2+ consecutive sweeps missing): "
              f"{', '.join(r['ticker'] for r in summary['stuck_2plus_sweeps'])}")
    print()
    for r in holdings_rows:
        print(f"  {r['status']:16s} {r['ticker']:14s} {r['detail']}")


if __name__ == "__main__":
    main()
