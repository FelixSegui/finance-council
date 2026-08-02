#!/usr/bin/env python3
"""
Entry point for the deterministic (machine-owned) steps of a sweep.

This does NOT do any reasoning — no valuation calls, no thesis judgment, no
council synthesis. That happens in a live Claude Code session reading the
.claude/agents/lens-*.md / core-*.md files, exactly as before this migration.
run.py's job is everything that doesn't need an LLM: sync Excel, fetch market
data, compute coverage, track controller metrics.

A typical session:
  python run.py sync              # master.xlsx -> data/sync/*.json
  python run.py fetch              # fresh market data for current holdings -> _MarketCache
  python run.py coverage           # data coverage report for this sweep
  <open Claude Code, run the reasoning agents in order>
  python run.py sync               # if you edited master.xlsx during the session

Or the shorthand for the deterministic prep in one call:
  python run.py prep               # sync -> fetch -> coverage, in order
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(REPO_ROOT, "data", "sync"))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))

CONTROLLER_STATE_PATH = "data/cache/controller_state.json"


def _load_controller_state():
    if os.path.exists(CONTROLLER_STATE_PATH):
        with open(CONTROLLER_STATE_PATH) as f:
            return json.load(f)
    return {"module_runs": [], "recommendations": []}


def _save_controller_state(state):
    os.makedirs(os.path.dirname(CONTROLLER_STATE_PATH), exist_ok=True)
    with open(CONTROLLER_STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def _run_tracked(module_name, argv):
    """Run a step as a subprocess, timed, with success/failure recorded into
    controller_state.json — this is the Controller's "track module execution"
    responsibility (Task 6/7), applied uniformly to every deterministic step."""
    state = _load_controller_state()
    t0 = time.time()
    result = subprocess.run([sys.executable] + argv, cwd=REPO_ROOT)
    duration = round(time.time() - t0, 2)
    state["module_runs"].append({
        "module": module_name,
        "utc": datetime.now(timezone.utc).isoformat(),
        "duration_sec": duration,
        "success": result.returncode == 0,
        "argv": argv,
    })
    state["module_runs"] = state["module_runs"][-200:]  # cap history, avoid unbounded growth
    _save_controller_state(state)
    if result.returncode != 0:
        sys.exit(f"{module_name} failed (exit {result.returncode}) after {duration}s")
    print(f"[{module_name}] done in {duration}s")


def cmd_sync(args):
    _run_tracked("sync", ["data/sync/sync.py", "read", "--xlsx", args.xlsx])


FETCH_MODULES = {
    "prices": ["scripts/fetch_prices.py", "--tickers"],           # + equities (comma list)
    "fundamentals": ["scripts/fetch_fundamentals_us.py", "--tickers"],  # + equities
    "crypto": ["scripts/fetch_crypto_prices.py", "--coins"],      # + crypto (comma list)
    "macro": ["scripts/fetch_macro.py"],
    "sentiment": ["scripts/fetch_sentiment.py"],
    "insiders_us": ["scripts/fetch_insiders_us.py", "--tickers"],  # + equities (non-US tickers skipped internally)
    # "insiders_se" is handled separately in cmd_fetch — it's issuer-name-based
    # (Finansinspektionen has no ticker search), one call per .ST stock holding.
}


def _fx_rate(snapshot, currency):
    """SEK-per-1-unit-of-currency multiplier, sourced from THIS sweep's macro
    snapshot (fetch_macro.py's sek_per_usd / sek_per_eur, FRED-derived).
    Returns 1.0 for SEK, None if the currency needs conversion and the rate
    isn't available — callers must treat None as missing, never assume 1:1
    (that would silently misstate the SEK total, the exact bug this fixes)."""
    if not currency or currency.upper() == "SEK":
        return 1.0
    key = {"USD": "sek_per_usd", "EUR": "sek_per_eur"}.get(currency.upper())
    if not key:
        return None
    try:
        return float(snapshot.get("macro", {}).get(key, {}).get("value"))
    except (TypeError, ValueError):
        return None


def _latest_file(dir_path):
    if not os.path.exists(dir_path):
        return None
    files = sorted(os.listdir(dir_path))
    return os.path.join(dir_path, files[-1]) if files else None


def _guess_se_issuer_name(portfolio_name):
    """Best-effort company name for Finansinspektionen's free-text issuer
    search, derived from the Portfolio sheet's human-entered name (e.g.
    'Handelsbanken A (stock)' -> 'Handelsbanken'). This is a SEARCH TERM, not
    fetched data — if Finansinspektionen returns zero rows for it, that's
    surfaced as an empty/error result downstream, never silently read as
    'confirmed no insider activity'."""
    if not portfolio_name:
        return ""
    n = re.sub(r"\(.*?\)", "", portfolio_name)  # drop "(stock)" etc.
    n = re.sub(r"\s+[A-Z]$", "", n.strip())      # drop trailing share-class letter " A"/" B"
    return n.strip()


def _fetch_insiders(rows, snapshot):
    """Insider activity for every STOCK holding (funds/certificates/cash
    have no board to trade on), fetched as its own tracked step per source —
    US via SEC Form 4 filing counts, Swedish/Nordic via Finansinspektionen's
    Insynsregistret — and merged into the SAME per-ticker equities record the
    snapshot already carries price/fundamentals in. One standardized place
    every lens reads (`equities[ticker]["insider_activity_us"/"_se"]`),
    not a side file only one agent knows to check."""
    equities = snapshot.setdefault("equities", {})
    stock_rows = [r for r in rows if r.get("instrument_type") == "stock" and r.get("ticker")]
    if not stock_rows:
        return

    us_tickers = [r["ticker"] for r in stock_rows if "." not in r["ticker"]]
    if us_tickers:
        _run_tracked("fetch_insiders_us", ["scripts/fetch_insiders_us.py", "--tickers", ",".join(us_tickers)])
        latest = _latest_file("data/cache/insiders_us")
        if latest:
            with open(latest) as f:
                us_result = json.load(f).get("insiders", {})
            for t, rec in us_result.items():
                equities.setdefault(t, {})["insider_activity_us"] = rec

    for r in stock_rows:
        t = r["ticker"]
        if not t.endswith(".ST"):
            continue
        issuer = _guess_se_issuer_name(r.get("name") or "")
        if not issuer:
            equities.setdefault(t, {})["insider_activity_se"] = {
                "error": "no usable company name in the Portfolio sheet to search Finansinspektionen with"}
            continue
        _run_tracked(f"fetch_insiders_se[{t}]",
                     ["scripts/fetch_insiders_se.py", "--issuer", issuer, "--days", "90"])
        latest = _latest_file("data/cache/insiders_se")
        if not latest:
            continue
        with open(latest) as f:
            data = json.load(f)
        transactions = data.get("transactions")
        equities.setdefault(t, {})["insider_activity_se"] = {
            "issuer_search_term": issuer,
            "date_from": data.get("date_from"), "date_to": data.get("date_to"),
            "transactions": transactions if isinstance(transactions, list) else None,
            "error": transactions.get("error") if isinstance(transactions, dict) else None,
        }


def cmd_fetch(args):
    """Fetch fresh market data for every Portfolio-sheet holding that has a
    real ticker, then write it into _MarketCache. Reads data/sync/portfolio.json
    (the synced output) — never portfolio.json directly, and never master.xlsx
    directly (only sync.py touches the workbook).

    Each data KIND (prices, fundamentals, crypto, macro, sentiment, US/SE
    insider activity) runs as its own tracked step — pass --only <kind> to
    run just one when debugging a specific source instead of the whole
    fetch. Insider activity is merged into the same per-ticker equities
    record as price/fundamentals in the snapshot, not a separate file, so
    every lens reads it from the same standardized place."""
    portfolio_path = "data/sync/portfolio.json"
    if not os.path.exists(portfolio_path):
        sys.exit("data/sync/portfolio.json missing — run 'python run.py sync' first.")
    with open(portfolio_path) as f:
        rows = json.load(f)["rows"]

    equities = [r["ticker"] for r in rows if r.get("ticker") and r["ticker"] not in
                ("TBD", "CASH_SEK", "CASH_USD", "CASH_EUR", "ethereum")]
    crypto = [r["ticker"] for r in rows if r.get("ticker") == "ethereum"]

    only = getattr(args, "only", None)  # cmd_prep's args namespace has no --only
    if only:
        # Debug path: run exactly ONE data kind, standalone, tracked on its
        # own — for when a specific source is broken and you don't want to
        # re-fetch everything else to test the fix. Does NOT touch
        # _MarketCache/Dashboard (that needs all kinds together); re-run
        # `python run.py fetch` without --only afterward to update it.
        if only == "insiders_se":
            stock_rows = [r for r in rows if r.get("instrument_type") == "stock"
                          and (r.get("ticker") or "").endswith(".ST")]
            if not stock_rows:
                sys.exit("No Nasdaq Stockholm (.ST) stock holdings in the Portfolio sheet to fetch.")
            for r in stock_rows:
                issuer = _guess_se_issuer_name(r.get("name") or "")
                if not issuer:
                    print(f"  skip {r['ticker']}: no usable company name to search with")
                    continue
                _run_tracked(f"fetch_insiders_se[{r['ticker']}]",
                             ["scripts/fetch_insiders_se.py", "--issuer", issuer, "--days", "90"])
            print("\nRan only 'insiders_se'. Run 'python run.py fetch' (no --only) "
                  "to update the combined snapshot and _MarketCache/Dashboard.")
            return
        script, *flag = FETCH_MODULES[only]
        argv = [script]
        if flag == ["--tickers"]:
            if not equities:
                sys.exit("No equity tickers in the Portfolio sheet to fetch.")
            argv += ["--tickers", ",".join(equities)]
        elif flag == ["--coins"]:
            if not crypto:
                sys.exit("No crypto tickers in the Portfolio sheet to fetch.")
            argv += ["--coins", ",".join(crypto)]
        _run_tracked(f"fetch_{only}", argv)
        print(f"\nRan only '{only}'. Run 'python run.py fetch' (no --only) "
              f"to update the combined snapshot and _MarketCache/Dashboard.")
        return

    # Default sweep path: ONE fetch via the orchestrator (which internally
    # calls the same separated modules/functions) — avoids fetching every
    # source twice. Tracked as one step; use --only above to isolate one
    # source when debugging.
    _run_tracked("fetch_market_data",
                 ["scripts/fetch_market_data.py",
                  "--tickers", ",".join(equities),
                  "--crypto", ",".join(crypto)])

    snap_dir = "data/cache/snapshots"
    latest = sorted(os.listdir(snap_dir))[-1] if os.path.exists(snap_dir) and os.listdir(snap_dir) else None
    if not latest:
        sys.exit("No snapshot produced — fetch_market_data.py may have failed.")
    snap_path = os.path.join(snap_dir, latest)
    with open(snap_path) as f:
        snapshot = json.load(f)

    _fetch_insiders(rows, snapshot)
    applied = _apply_manual_overrides(snapshot)

    with open(snap_path, "w") as f:
        json.dump(snapshot, f, indent=2)
    if applied:
        print(f"Applied {len(applied)} manual override(s) from the Manual Data sheet: "
              f"{', '.join(applied)}")

    records = {}
    for r in rows:
        t = r.get("ticker")
        if not t:
            continue
        if t in ("CASH_SEK", "CASH_USD", "CASH_EUR"):
            cur = t.replace("CASH_", "")
            fx = _fx_rate(snapshot, cur)
            records[t] = {"last_price": 1, "currency": cur,
                          "price_as_of": snapshot.get("fetched_at_utc"),
                          "market_value_sek": fx,
                          "fetch_status": "N/A" if fx is not None else "N/A (FX MISSING)",
                          "data_source": "cash"}
        elif t == "TBD":
            records[f"TBD-{r.get('name')}"] = {"last_price": None, "currency": r.get("currency"),
                          "price_as_of": None, "market_value_sek": r.get("cost_basis_total_sek"),
                          "fetch_status": "N/A (permanent)" if r.get("no_ticker_reason") else "N/A",
                          "data_source": "unlisted_fund"}
        elif t == "ethereum":
            c = snapshot.get("crypto", {}).get("ethereum", {})
            price_eur = c.get("price_eur")
            fx = _fx_rate(snapshot, "EUR")
            mv = round(price_eur * fx, 4) if (price_eur is not None and fx is not None) else None
            status = "OK" if c else "MISSING"
            if c and mv is None:
                status = "OK (FX MISSING)"
            records[t] = {"last_price": price_eur, "currency": "EUR",
                          "price_as_of": snapshot.get("fetched_at_utc"),
                          "market_value_sek": mv, "fetch_status": status,
                          "data_source": "coingecko"}
        else:
            eq = snapshot.get("equities", {}).get(t, {})
            has_price = eq.get("price") is not None
            has_fund = eq.get("trailing_pe") is not None or eq.get("market_cap") is not None
            status = "OK" if has_fund else ("OK (price only)" if has_price else
                     ("ERROR" if "error" in eq else "MISSING"))
            fx = _fx_rate(snapshot, eq.get("currency")) if has_price else None
            mv = round(eq["price"] * fx, 4) if (has_price and fx is not None) else None
            if has_price and fx is None:
                status += " (FX MISSING)"
            records[t] = {"last_price": eq.get("price"), "currency": eq.get("currency"),
                          "price_as_of": snapshot.get("fetched_at_utc"),
                          "market_value_sek": mv, "fetch_status": status,
                          "data_source": eq.get("_source", "yfinance")}

    os.makedirs("data/sync", exist_ok=True)
    with open("data/sync/market_cache.json", "w") as f:
        json.dump(records, f, indent=2)
    _run_tracked("write_market_cache", ["data/sync/sync.py", "write-cache", "--xlsx", args.xlsx])


def _apply_manual_overrides(snapshot):
    """Fill genuinely-missing equity fields (fundamentals the automated fetch
    couldn't get — e.g. no free source for a non-US ticker) from the Manual
    Data sheet, WITHOUT ever overwriting a value the fetch actually got. Every
    filled field is tagged in `_manual_overrides` so it's always visible which
    numbers came from the user, not a live source — never silently blended.
    Mutates the snapshot dict in place; the caller persists it. Returns the
    list of "ticker.field" strings actually filled, for the caller to log."""
    manual_path = "data/sync/manual_data.json"
    if not os.path.exists(manual_path):
        return []
    with open(manual_path) as f:
        manual_rows = json.load(f).get("rows", [])
    if not manual_rows:
        return []

    equities = snapshot.setdefault("equities", {})
    applied = []
    for row in manual_rows:
        ticker, field, value = row.get("ticker"), row.get("field"), row.get("value")
        if not ticker or not field or value is None:
            continue
        rec = equities.setdefault(ticker, {})
        if rec.get(field) is not None:
            continue  # a real fetched value already exists — manual data never overrides it
        rec[field] = value
        rec.setdefault("_manual_overrides", {})[field] = {
            "source": row.get("source"), "as_of": row.get("as_of"), "notes": row.get("notes"),
        }
        applied.append(f"{ticker}.{field}")
    return applied


def cmd_coverage(args):
    _run_tracked("coverage_report", ["scripts/generate_coverage_report.py"])


def cmd_prep(args):
    cmd_sync(args)
    cmd_fetch(args)
    cmd_coverage(args)
    print("\nDeterministic prep complete. Open a Claude Code session and run "
          "the sweep's reasoning agents (journal -> ... -> council).")


def cmd_controller(args):
    """Surface the Controller's own metrics summary — module health over the
    last N runs, without any LLM call. The narrative recommendations (the
    parts that need judgment) are written by the core-controller.md agent
    during a session; this just reports the raw numbers."""
    state = _load_controller_state()
    runs = state["module_runs"]
    if not runs:
        print("No tracked runs yet — run 'python run.py prep' first.")
        return
    by_module = {}
    for r in runs:
        by_module.setdefault(r["module"], []).append(r)
    print(f"Controller state: {len(runs)} tracked runs across {len(by_module)} modules\n")
    for mod, mruns in by_module.items():
        n = len(mruns)
        fails = sum(1 for r in mruns if not r["success"])
        avg_dur = round(sum(r["duration_sec"] for r in mruns) / n, 2)
        last = mruns[-1]
        flag = "  <- repeated failures" if fails >= 2 else ""
        print(f"  {mod:<22s} runs={n:>3d}  failures={fails:>2d}  avg={avg_dur:>6.2f}s  "
              f"last={'OK' if last['success'] else 'FAIL'}{flag}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--xlsx", default="master.xlsx")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("sync").set_defaults(func=cmd_sync)
    fetch_p = sub.add_parser("fetch")
    fetch_p.add_argument("--only", choices=list(FETCH_MODULES) + ["insiders_se"],
                         help="run just one data kind, standalone, for debugging a specific source")
    fetch_p.set_defaults(func=cmd_fetch)
    sub.add_parser("coverage").set_defaults(func=cmd_coverage)
    sub.add_parser("prep").set_defaults(func=cmd_prep)
    sub.add_parser("controller").set_defaults(func=cmd_controller)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
