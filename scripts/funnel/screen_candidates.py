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

BUG FIXED 2026-08-12: this used to import fetch_equities from
scripts/fetchers/fetch_market_data.py (the parked Excel-branch fetcher,
via a sys.path pointed at scripts/fetchers/), which routes through
fetch_fundamentals_us.py's SEC-CIK-lookup-based yfinance path - the same
broken-on-this-network mechanism CLAUDE.md's yfinance note already
documents for fetch_calendar.py (S3). Every ticker failed with a CIK-
lookup 403. Fixed to import from the real scripts/fetch_market_data.py
(direct urllib + crumb/cookie-jar bypass, the one that works) instead -
same function name, same output field names, confirmed compatible with
this file's FILTERS list.

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

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fetch_market_data import fetch_equities  # noqa: E402

WATCHLIST_PATH = "data/cache/watchlist.json"  # built from the Excel Watchlist tab, see
                                               # scripts/import_excel_holdings.py
LEGACY_UNIVERSE_PATH = "data/universe.json"  # pre-Watchlist-tab fallback, see below

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
    # data/universe.json is retired in favor of a Watchlist tab in the user's
    # Excel workbook (import_excel_holdings.py builds WATCHLIST_PATH from it,
    # with a "categories" dict shaped exactly like the old universe.json so
    # this function doesn't need to change). Until that tab exists and has
    # been imported at least once, fall back to the legacy cache so scout
    # doesn't just break in the interim.
    path = WATCHLIST_PATH if os.path.exists(WATCHLIST_PATH) else LEGACY_UNIVERSE_PATH
    with open(path) as f:
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
            failed[ticker] = {"reasons": fail_reasons, "data": fields}
        elif missing_fields:
            missing[ticker] = {"missing_fields": missing_fields, "data": fields}
        else:
            passed[ticker] = fields
    return passed, failed, missing


DIGEST_COLUMNS = [
    "ticker", "status", "sector", "price", "pe", "fwd_pe", "peg",
    "margin_pct", "roe_pct", "roic_pct", "de_ratio", "net_debt_to_ebitda",
    "rev_growth_pct", "fcf_b", "div_yield_pct", "mcap_b", "beta", "note",
]


def write_compact_digest(passed, failed, missing, fname):
    """One row per ticker, key fields only, no nested source/quality_state
    wrappers. This exists because the full JSON this script also writes
    (~60k+ tokens across a ~70-ticker universe, per the 2026-08-17
    Stock-Selection-Council test run) is what a reading agent burns most of
    its budget on before it does any actual reasoning - this file is the
    cheap-to-read version council.md's Stock Selection Council should read
    first, falling back to the full JSON only for a specific ticker that
    needs a field this digest doesn't carry (e.g. the multi-year revenue
    history, or a field's source/quality_state)."""
    import csv
    rows = []

    def _val(x):
        """Unwrap the Layer-B derived-metric shape ({"value":...,
        "quality_state":...}) used for roic_pct/ebit/capex/etc - see
        derived_metrics.py - down to a plain number, or None."""
        if isinstance(x, dict):
            return x.get("value")
        return x

    def row(ticker, fields, status, note=""):
        pe = fields.get("trailing_pe")
        mcap = fields.get("market_cap")
        margin = fields.get("profit_margins")
        roe = fields.get("return_on_equity")
        roic = _val(fields.get("roic_pct"))
        rev_g = fields.get("revenue_growth")
        div_y = fields.get("dividend_yield")
        fcf = fields.get("free_cashflow")
        total_debt, total_cash, ebitda = (fields.get("total_debt"), fields.get("total_cash"),
                                           fields.get("ebitda"))
        net_debt_to_ebitda = None
        if all(isinstance(x, (int, float)) for x in (total_debt, total_cash, ebitda)) and ebitda:
            net_debt_to_ebitda = round((total_debt - total_cash) / ebitda, 2)
        rows.append({
            "ticker": ticker,
            "status": status,
            "sector": fields.get("sector") or "",
            "price": fields.get("price"),
            "pe": pe,
            "fwd_pe": fields.get("forward_pe"),
            "peg": fields.get("peg_ratio"),
            "margin_pct": round(margin * 100, 1) if isinstance(margin, (int, float)) else None,
            "roe_pct": round(roe * 100, 1) if isinstance(roe, (int, float)) else None,
            "roic_pct": round(roic * 100, 1) if isinstance(roic, (int, float)) else None,
            "de_ratio": fields.get("debt_to_equity"),
            "net_debt_to_ebitda": net_debt_to_ebitda,
            "rev_growth_pct": round(rev_g * 100, 1) if isinstance(rev_g, (int, float)) else None,
            "fcf_b": round(fcf / 1e9, 2) if isinstance(fcf, (int, float)) else None,
            "div_yield_pct": round(div_y * 100, 2) if isinstance(div_y, (int, float)) else None,
            "mcap_b": round(mcap / 1e9, 1) if isinstance(mcap, (int, float)) else None,
            "beta": fields.get("beta"),
            "note": note,
        })

    for ticker, fields in passed.items():
        row(ticker, fields, "PASS")
    for ticker, info in failed.items():
        row(ticker, info.get("data", {}), "FAIL", "; ".join(info.get("reasons", []))[:120])
    for ticker, info in missing.items():
        fields = info.get("data", {})
        note = info.get("reason") or ("missing: " + ",".join(info.get("missing_fields", [])))
        row(ticker, fields, "MISSING", note[:120])

    with open(fname, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIGEST_COLUMNS)
        writer.writeheader()
        for r in sorted(rows, key=lambda r: r["ticker"]):
            writer.writerow(r)
    return fname


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
    os.makedirs("data/cache/screens", exist_ok=True)
    fname = f"data/cache/screens/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-screen.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)

    digest_fname = fname.replace("-screen.json", "-digest.csv")
    write_compact_digest(passed, failed, missing, digest_fname)

    print(f"Wrote {fname}")
    print(f"Wrote {digest_fname} (compact - read this first; fall back to the "
          f"full JSON only for a ticker needing a field the digest doesn't carry)")
    print(f"Passed: {sorted(passed)}")
    print(f"Missing data (not failed, not passed): {sorted(missing)}")
    print(f"Failed: {len(failed)} tickers")


if __name__ == "__main__":
    main()
