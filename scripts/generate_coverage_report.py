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
  - the latest data/snapshots/*.json  (this sweep's holdings-relevant fetch)
  - data/portfolio.json               (what SHOULD have been fetched)
  - the latest data/rankings/*.json, if present (candidate/universe coverage)
  - data/universe.json                (structural: which categories even
                                        HAVE a free fundamentals source)

Writes:
  - reports/YYYY-MM-DD-data-coverage.md   (readable holdings-focused report)
  - data/coverage_reports/TIMESTAMP-universe-coverage.csv (full per-ticker
    universe table, for Excel-style filtering — too large for markdown)
  - data/coverage_reports/_streak_state.json (internal: consecutive
    missing/error counts per holding ticker, carried sweep to sweep)

Usage:
  python scripts/generate_coverage_report.py
"""
import csv
import glob
import json
import os
import sys
from datetime import datetime, timezone

SNAPSHOTS_GLOB = "data/snapshots/*.json"
RANKINGS_GLOB = "data/rankings/2*-ranking.json"
PORTFOLIO_PATH = "data/portfolio.json"
UNIVERSE_PATH = "data/universe.json"
COVERAGE_DIR = "data/coverage_reports"
STREAK_STATE_PATH = f"{COVERAGE_DIR}/_streak_state.json"
REPORTS_DIR = "reports"

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
    """Return (status, detail, fields_present) for one portfolio.json holding."""
    ticker = h.get("ticker")
    itype = h.get("instrument_type")

    if itype == "cash" or ticker in ("CASH_SEK", "CASH_USD", "CASH_EUR"):
        return "N/A", "cash — not a market instrument", []

    if ticker == "TBD":
        permanent_reason = h.get("no_ticker_reason")
        if permanent_reason:
            return "N/A (permanent)", permanent_reason, []
        return "N/A", "no resolved ticker/ISIN on file yet — cannot be fetched until named", []

    if itype == "spot_crypto" or ticker == "ethereum":
        rec = snapshot_crypto.get(ticker or "ethereum")
        if rec is None:
            return "MISSING", "not included in this sweep's --crypto fetch list", []
        if "error" in rec:
            return "ERROR", rec["error"], []
        present = [k for k in ("price_eur", "change_24h_pct", "change_7d_pct") if rec.get(k) is not None]
        return "OK", f"CoinGecko, {len(present)} fields", present

    # equity / certificate / fund-with-ticker
    rec = snapshot_equities.get(ticker)
    if rec is None:
        return "MISSING", "not included in this sweep's --tickers fetch list", []
    if "error" in rec:
        return "ERROR", rec["error"], []
    fund_present = [k for k in FUNDAMENTAL_FIELDS if rec.get(k) is not None]
    has_price = rec.get("price") is not None
    if not has_price:
        return "ERROR", "fetched but price field is null", []
    if fund_present:
        return "OK", f"price + {len(fund_present)} fundamentals fields", fund_present
    reason = rec.get("_fundamentals_unavailable_reason")
    return "OK (price only)", reason or "price fetched; fundamentals fields all null", []


def build_holdings_table(portfolio, snapshot):
    equities = snapshot.get("equities", {}) if snapshot else {}
    crypto = snapshot.get("crypto", {}) if snapshot else {}
    if isinstance(equities, dict) and "error" in equities and len(equities) == 1:
        equities = {}  # top-level fetch failure (e.g. import error) — treat as "nothing fetched"

    streaks = load_streak_state()
    rows = []
    for h in portfolio.get("holdings", []):
        status, detail, fields = classify_holding(h, equities, crypto)
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


def write_markdown_report(snapshot_path, snapshot, holdings_rows, universe_summary):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    os.makedirs(REPORTS_DIR, exist_ok=True)
    fname = f"{REPORTS_DIR}/{today}-data-coverage.md"

    lines = []
    lines.append(f"# Data Coverage Report — {today}")
    lines.append("")
    lines.append("Diagnostic report: what was actually fetched this sweep, what wasn't, "
                  "and why. Not a portfolio-vs-market performance tracker — see "
                  "`scripts/performance.py` + `data/valuations.csv` for that.")
    lines.append("")
    if snapshot:
        lines.append(f"**Snapshot used:** `{snapshot_path}` (fetched {snapshot.get('fetched_at_utc')})")
    else:
        lines.append("**No snapshot found** — run `python scripts/fetch_market_data.py` first.")
    lines.append("")

    lines.append("## Holdings — what was fetched this sweep")
    lines.append("")
    lines.append("| Ticker | Name | Account | Status | Detail | Consecutive sweeps missing |")
    lines.append("|---|---|---|---|---|---|")
    n_ok, n_partial, n_missing, n_na = 0, 0, 0, 0
    for r in holdings_rows:
        if r["status"] == "OK":
            n_ok += 1
        elif r["status"].startswith("OK"):
            n_partial += 1
        elif r["status"] == "N/A":
            n_na += 1
        else:
            n_missing += 1
        lines.append(f"| {r['ticker']} | {r['name']} | {r['account']} | **{r['status']}** | "
                      f"{r['detail']} | {r['consecutive_sweeps_missing']} |")
    lines.append("")
    lines.append(f"**Summary: {n_ok} fully OK, {n_partial} price-only (no free fundamentals source), "
                  f"{n_missing} missing/error, {n_na} not applicable (cash / no ticker on file).**")
    lines.append("")
    stuck = [r for r in holdings_rows if isinstance(r["consecutive_sweeps_missing"], int)
             and r["consecutive_sweeps_missing"] >= 2]
    if stuck:
        lines.append("**Flagged — failing for 2+ consecutive sweeps (a real gap, not a blip):**")
        for r in stuck:
            lines.append(f"- {r['ticker']} ({r['name']}): {r['consecutive_sweeps_missing']} "
                          f"sweeps — {r['detail']}")
        lines.append("")

    if universe_summary:
        lines.append("## Screening universe / funnel — structural + empirical coverage")
        lines.append("")
        lines.append("Structural = does a free fundamentals source even exist for this category "
                      "(SEC EDGAR is US-filer-only, so only `sp500` ever has one). "
                      "Empirical = from the last funnel ranking run.")
        lines.append("")
        lines.append("| Category | Tickers | Have a free fundamentals source |")
        lines.append("|---|---:|---:|")
        for s in universe_summary["structural"]:
            lines.append(f"| {s['category']} | {s['count']} | {s['with_free_fundamentals_source']} |")
        lines.append("")
        emp = universe_summary["empirical"]
        if emp:
            cov = emp["coverage"]
            lines.append(f"**Last funnel run** ({emp['ranking_file']}, generated "
                          f"{emp['generated_utc']}, categories: {emp['universe_categories']}): "
                          f"{cov.get('ranked', 0)} full-factor ranked, "
                          f"{cov.get('momentum_only', 0)} momentum-only (no fundamentals), "
                          f"{cov.get('partial_data', 0)} set aside (no data at all).")
            lines.append("")
            lines.append("Full per-ticker universe coverage is in the accompanying CSV "
                          "(too large for this table).")
        else:
            lines.append("_No funnel ranking run found yet — run "
                          "`python scripts/rank_candidates.py --stack` to populate this section._")
        lines.append("")

    with open(fname, "w") as f:
        f.write("\n".join(lines))
    return fname


def main():
    snapshot_path = latest(SNAPSHOTS_GLOB)
    snapshot = load_json(snapshot_path) if snapshot_path else None
    portfolio = load_json(PORTFOLIO_PATH)

    holdings_rows = build_holdings_table(portfolio, snapshot)
    universe_summary, ticker_rows = build_universe_summary()

    md_path = write_markdown_report(snapshot_path, snapshot, holdings_rows, universe_summary)
    csv_path = write_universe_csv(ticker_rows) if ticker_rows else None

    print(f"Wrote {md_path}")
    if csv_path:
        print(f"Wrote {csv_path} ({len(ticker_rows)} tickers)")
    print()
    for r in holdings_rows:
        print(f"  {r['status']:16s} {r['ticker']:14s} {r['detail']}")


if __name__ == "__main__":
    main()
