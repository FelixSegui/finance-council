#!/usr/bin/env python3
"""
The synchronization layer — the ONLY module besides workbook.py that opens
master.xlsx. Every other script in this project reads plain JSON that this
module produces; none of them import openpyxl or know a spreadsheet exists.

Two directions:
  read  — master.xlsx Zone-1 sheets -> data/sync/*.json (what scripts consume)
  write — fresh market data -> the hidden _MarketCache sheet (what Dashboard
          formulas read). Zone-1 sheets are NEVER written by this direction —
          only a human (or Claude, acting on the human's instruction during a
          session) edits Portfolio/Transactions/Watchlist/etc.

A third direction exists for agents that need to RECORD something during a
session (a new thesis nomination, a resolved note, a pending order) without
every agent needing its own openpyxl knowledge:
  append — one JSON row -> appended to a named Zone-1 sheet in master.xlsx.
           This is the ONLY way anything outside this file writes to the
           workbook; the openpyxl logic stays here, callable, not duplicated.

Usage:
  python data/sync/sync.py read                  # xlsx -> JSON
  python data/sync/sync.py write-cache            # fresh snapshot -> _MarketCache
  python data/sync/sync.py append --sheet Watchlist --row '{"ticker": "V", ...}'
  python data/sync/sync.py read --xlsx other.xlsx --out-dir /tmp/x
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import SHEETS, ZONE1_SHEETS  # noqa: E402

from openpyxl import load_workbook

DEFAULT_XLSX = "master.xlsx"
DEFAULT_OUT_DIR = "data/sync"
UNIVERSE_CACHE_PATH = "data/cache/universe.json"  # machine-owned; sp500 auto-built here
THESIS_CACHE_PATH = "data/cache/thesis_candidates.json"  # regenerated from Watchlist+Thesis each sync

# sheet name -> output JSON filename (snake_case, matches what scripts expect)
SHEET_TO_FILE = {
    "Portfolio": "portfolio.json",
    "Transactions": "transactions.json",
    "Watchlist": "watchlist.json",
    "Universe": "universe_manual.json",
    "Investment Thesis": "thesis.json",
    "Pending Orders": "pending_orders.json",
    "Settings": "settings.json",
    "Notes": "notes.json",
    "Manual Data": "manual_data.json",
}


def _sheet_rows(ws, columns):
    """Yield dict rows from row 2 onward; skip fully-blank rows."""
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row is None or all(v is None or v == "" for v in row):
            continue
        rec = {}
        for i, col in enumerate(columns):
            val = row[i] if i < len(row) else None
            rec[col] = val
        yield rec


def read_workbook(xlsx_path, out_dir):
    """Zone 1: master.xlsx -> JSON files every other module consumes."""
    if not os.path.exists(xlsx_path):
        sys.exit(f"{xlsx_path} not found. Run data/sync/workbook.py first, "
                 f"then scripts/migrate_from_json.py to populate it.")
    wb = load_workbook(xlsx_path, data_only=False)
    os.makedirs(out_dir, exist_ok=True)

    written = {}
    for sheet_name in ZONE1_SHEETS:
        if sheet_name not in wb.sheetnames:
            sys.exit(f"Expected sheet '{sheet_name}' missing from {xlsx_path} — "
                     f"workbook is out of date, rebuild with data/sync/workbook.py")
        rows = list(_sheet_rows(wb[sheet_name], SHEETS[sheet_name]))
        out_file = os.path.join(out_dir, SHEET_TO_FILE[sheet_name])
        with open(out_file, "w") as f:
            json.dump({
                "synced_utc": datetime.now(timezone.utc).isoformat(),
                "source_sheet": sheet_name,
                "row_count": len(rows),
                "rows": rows,
            }, f, indent=2, default=str)
        written[sheet_name] = (out_file, len(rows))

    print(f"Synced {xlsx_path} -> {out_dir}/")
    for sheet, (path, n) in written.items():
        print(f"  {sheet:<20s} {n:>4d} rows -> {path}")

    _merge_universe_manual(written.get("Universe"))
    _rebuild_thesis_cache(written.get("Watchlist"), written.get("Investment Thesis"))
    return written


def _rebuild_thesis_cache(watchlist_written, thesis_written):
    """rank_candidates.py reads a candidates cache in the same shape the old
    thesis_candidates.json used — regenerate it from the synced Watchlist
    (which tickers are being tracked) + Investment Thesis (the prose/risk_tag
    for each) sheets every sync, so it never drifts from what's in Excel."""
    if not watchlist_written or not thesis_written:
        return
    with open(watchlist_written[0]) as f:
        watchlist = json.load(f)["rows"]
    with open(thesis_written[0]) as f:
        thesis_by_ticker = {t["ticker"]: t for t in json.load(f)["rows"] if t.get("ticker")}

    candidates = []
    for w in watchlist:
        t = thesis_by_ticker.get(w.get("ticker"), {})
        candidates.append({
            "ticker": w.get("ticker"), "name": w.get("name"), "source": w.get("source"),
            "date": w.get("date_added"), "risk_tag": t.get("risk_tag"),
            "thesis": t.get("thesis"), "policy_tailwind": t.get("policy_tailwind"),
        })
    out = {"note": "Regenerated from the Watchlist + Investment Thesis sheets each sync — not hand-edited.",
           "candidates": candidates}
    os.makedirs(os.path.dirname(THESIS_CACHE_PATH), exist_ok=True)
    with open(THESIS_CACHE_PATH, "w") as f:
        json.dump(out, f, indent=2)
    print(f"  rebuilt thesis cache -> {THESIS_CACHE_PATH} ({len(candidates)} candidates)")


def _merge_universe_manual(universe_written):
    """The Universe SHEET is the human-owned source for manually-curated
    tickers (Nordic, Europe, thesis picks); data/cache/universe.json is
    machine-owned (build_universe.py writes its auto-built sp500 list there).
    Rather than have both independently hold manual categories — the exact
    'same information in two places' the architecture forbids — this merges
    the sheet's rows into the cache file's manual categories on every sync,
    leaving sp500 untouched. rank_candidates.py / screen_candidates.py then
    read ONE file and don't need to know Excel exists."""
    if not universe_written:
        return
    path, _n = universe_written
    with open(path) as f:
        manual = json.load(f)["rows"]

    if os.path.exists(UNIVERSE_CACHE_PATH):
        with open(UNIVERSE_CACHE_PATH) as f:
            cache = json.load(f)
    else:
        cache = {"categories": {}, "metadata": {}}

    cats, meta = cache.setdefault("categories", {}), cache.setdefault("metadata", {})
    manual_cat_names = sorted({r["category"] for r in manual if r.get("category")})
    for cat in manual_cat_names:
        cats[cat] = sorted({r["ticker"] for r in manual if r.get("category") == cat and r.get("ticker")})
    for r in manual:
        if r.get("ticker"):
            meta[r["ticker"]] = {"name": r.get("name"), "sector": meta.get(r["ticker"], {}).get("sector"),
                                 "cik": meta.get(r["ticker"], {}).get("cik"),
                                 "currency": r.get("currency"), "source": r.get("source")}
    cache["manual_categories"] = manual_cat_names
    os.makedirs(os.path.dirname(UNIVERSE_CACHE_PATH), exist_ok=True)
    with open(UNIVERSE_CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)
    print(f"  merged {len(manual)} manual universe rows -> {UNIVERSE_CACHE_PATH} "
          f"(categories: {manual_cat_names}; sp500 untouched)")


def write_market_cache(xlsx_path, records):
    """Zone 2: fresh {ticker: {last_price, currency, price_as_of, market_value_sek,
    fetch_status, data_source}} -> the hidden _MarketCache sheet. Overwrites the
    sheet wholesale every call — it is fully disposable, exactly like the JSON
    cache under data/cache/. Never touches any Zone-1 sheet."""
    wb = load_workbook(xlsx_path)
    ws = wb["_MarketCache"]
    ws.delete_rows(2, ws.max_row)  # clear all data rows, keep the header
    cols = SHEETS["_MarketCache"]
    for i, (ticker, rec) in enumerate(records.items(), 2):
        for j, col in enumerate(cols, 1):
            val = ticker if col == "ticker" else rec.get(col)
            ws.cell(row=i, column=j, value=val)
    dash = wb["Dashboard"]
    dash["B17"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    wb.save(xlsx_path)
    print(f"Wrote {len(records)} rows to _MarketCache in {xlsx_path}")


def append_row(xlsx_path, sheet_name, row):
    """Append one row (dict, keys matching schema.py's column list for that
    sheet — unknown keys ignored, missing keys left blank) to a Zone-1 sheet.
    The only way an agent records new information into master.xlsx; keeps the
    openpyxl/file-format knowledge in this one module. Caller should follow up
    with `read` if the appended data needs to flow to the other JSON caches
    (e.g. a new Watchlist row needs `read` to rebuild the thesis cache)."""
    if sheet_name not in ZONE1_SHEETS:
        sys.exit(f"'{sheet_name}' is not a Zone-1 sheet — append only writes "
                 f"human-owned input sheets. Zone-1 sheets: {ZONE1_SHEETS}")
    wb = load_workbook(xlsx_path)
    ws = wb[sheet_name]
    cols = SHEETS[sheet_name]
    next_row = ws.max_row + 1
    for i, col in enumerate(cols, 1):
        ws.cell(row=next_row, column=i, value=row.get(col))
    wb.save(xlsx_path)
    print(f"Appended 1 row to '{sheet_name}' (row {next_row}) in {xlsx_path}")
    print("Run 'python data/sync/sync.py read' to flow this into data/sync/*.json "
          "and any dependent caches (universe/thesis).")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("direction", choices=["read", "write-cache", "append"])
    p.add_argument("--xlsx", default=DEFAULT_XLSX)
    p.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    p.add_argument("--sheet", help="(append) target sheet name")
    p.add_argument("--row", help="(append) JSON object for the new row")
    args = p.parse_args()

    if args.direction == "read":
        read_workbook(args.xlsx, args.out_dir)
    elif args.direction == "append":
        if not args.sheet or not args.row:
            sys.exit("append requires --sheet and --row '<json object>'")
        append_row(args.xlsx, args.sheet, json.loads(args.row))
    else:
        cache_path = os.path.join(args.out_dir, "market_cache.json")
        if not os.path.exists(cache_path):
            sys.exit(f"{cache_path} not found — run.py should write it before "
                     f"calling 'write-cache' (see run.py's fetch step).")
        with open(cache_path) as f:
            records = json.load(f)
        write_market_cache(args.xlsx, records)


if __name__ == "__main__":
    main()
