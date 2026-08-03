#!/usr/bin/env python3
"""
Generate master.xlsx from portfolio.json + the latest snapshot.

WHY THIS EXISTS, AND WHY IT ONLY WRITES
---------------------------------------
The Excel-backed branch made master.xlsx the *source of truth*: the user
edited the workbook and a sync layer read it back. That inverts the burden
onto the person, and the user's explicit requirement is the opposite -
"I want to minimize the strain on me, I do not want a lot to update and feed."

So the direction is reversed here. portfolio.json stays the source of truth
(agents maintain it), and this script renders it into a workbook you only
ever *look at*. Nothing reads the workbook back. You can delete master.xlsx
at any time and regenerate it; you can never break the system by editing it.

That also gives the cross-check the user asked for: if the totals here don't
match the broker, the system's model of the portfolio is wrong.

The one exception is the "Manual Data" sheet: if it already exists it is
carried over untouched, so hand-entered figures (e.g. a P/E pasted from
Avanza, or values converted from Excel's Stocks data type) survive a rebuild.

Usage:
    python scripts/build_workbook.py
    python scripts/build_workbook.py --out master.xlsx
"""

import argparse
import glob
import json
import os
from datetime import datetime, timezone

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP_DIR = os.path.join(ROOT, "data", "cache", "snapshots")

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(bold=True, color="FFFFFF")
TITLE_FONT = Font(bold=True, size=14)
WARN_FILL = PatternFill("solid", fgColor="FFF2CC")
BAD_FILL = PatternFill("solid", fgColor="FCE4EC")
OK_FILL = PatternFill("solid", fgColor="E8F5E9")


def load_json(path):
    with open(path) as fh:
        return json.load(fh)


def latest_snapshot():
    files = sorted(glob.glob(os.path.join(SNAP_DIR, "*.json")))
    if not files:
        return None, None
    return os.path.basename(files[-1]), load_json(files[-1])


def write_header(ws, headers, row=1):
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=c, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center")


def autosize(ws, max_width=52):
    for col in ws.columns:
        letter = get_column_letter(col[0].column)
        width = max((len(str(c.value)) for c in col if c.value is not None), default=8)
        ws.column_dimensions[letter].width = min(max(width + 2, 10), max_width)


def fx_rate(snap, key):
    """SEK per unit of foreign currency, from the snapshot's macro block only."""
    node = ((snap or {}).get("macro") or {}).get(key) or {}
    try:
        return float(node.get("value"))
    except (TypeError, ValueError):
        return None


def holding_value(h, snap):
    """Live value where possible, else the recorded value. Never invents one."""
    eq = (snap or {}).get("equities", {})
    t = h.get("ticker")
    qty = h.get("quantity")

    # Cash is held as a quantity in its own currency; convert non-SEK at the
    # snapshot's rate. Without a fetched rate we report no data rather than
    # guessing - a wrong FX rate silently distorts every allocation figure.
    if h.get("instrument_type") == "cash" and qty is not None:
        if t == "CASH_SEK" or h.get("currency") == "SEK":
            return qty, "book"
        rate = fx_rate(snap, "sek_per_usd" if h.get("currency") == "USD" else "sek_per_eur")
        return (qty * rate, "live FX") if rate else (None, "no data")

    if t in eq and not eq[t].get("error") and eq[t].get("price") and qty is not None:
        return eq[t]["price"] * qty, "live"
    if h.get("market_value_sek") is not None:
        return h["market_value_sek"], "user-relayed" if h.get("market_value_source") else "book"
    return None, "no data"


def build_overview(wb, pf, snap, snap_name, rows):
    ws = wb.create_sheet("Overview", 0)
    ws["A1"] = "Portfolio overview"
    ws["A1"].font = TITLE_FONT
    ws["A2"] = f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from portfolio.json"
    ws["A3"] = f"Prices from snapshot: {snap_name or 'none'}"
    ws["A4"] = "READ-ONLY VIEW — edit portfolio.json, not this file. Rebuild: python scripts/build_workbook.py"
    ws["A4"].font = Font(italic=True)

    # Exposure-class totals, excluding operating cash by design.
    by_class = {}
    for h in pf.get("holdings", []):
        if h.get("exposure_class") == "excluded_operating_cash":
            continue
        val, _ = holding_value(h, snap)
        if val is None:
            continue
        by_class[h.get("exposure_class", "unknown")] = by_class.get(h.get("exposure_class", "unknown"), 0) + val
    total = sum(by_class.values())

    targets = pf.get("targets", {})
    tmap = {
        "equity": targets.get("equity_pct"),
        "crypto": targets.get("crypto_pct"),
        "cash": targets.get("cash_pct"),
        "fixed_income": targets.get("fixed_income_pct"),
    }

    r = 6
    ws.cell(row=r, column=1, value="Allocation vs target").font = Font(bold=True)
    r += 1
    write_header(ws, ["Exposure class", "Value (SEK)", "% of total", "Target %", "Drift (pp)"], row=r)
    r += 1
    for cls in sorted(by_class, key=lambda k: -by_class[k]):
        val = by_class[cls]
        share = val / total * 100 if total else None
        tgt = tmap.get(cls)
        drift = (share - tgt) if (share is not None and tgt is not None) else None
        ws.cell(row=r, column=1, value=cls)
        ws.cell(row=r, column=2, value=round(val, 2)).number_format = "#,##0.00"
        ws.cell(row=r, column=3, value=round(share, 2) if share is not None else "n/a")
        ws.cell(row=r, column=4, value=tgt if tgt is not None else "n/a")
        dc = ws.cell(row=r, column=5, value=round(drift, 2) if drift is not None else "n/a")
        if drift is not None:
            dc.fill = BAD_FILL if abs(drift) >= 10 else (WARN_FILL if abs(drift) >= 3 else OK_FILL)
        r += 1
    ws.cell(row=r, column=1, value="TOTAL").font = Font(bold=True)
    tc = ws.cell(row=r, column=2, value=round(total, 2))
    tc.font = Font(bold=True)
    tc.number_format = "#,##0.00"

    r += 2
    ws.cell(row=r, column=1, value="Cross-check").font = Font(bold=True)
    r += 1
    ws.cell(row=r, column=1, value="If this total does not match your broker, the system's model is wrong — "
                                   "that mismatch is the point of this sheet.")
    r += 1
    excluded = [h.get("name") for h in pf.get("holdings", [])
                if h.get("exposure_class") == "excluded_operating_cash"]
    if excluded:
        ws.cell(row=r, column=1, value="Deliberately excluded (operating cash, not capital): " + "; ".join(excluded))
    autosize(ws)


def build_holdings(wb, rows):
    ws = wb.create_sheet("Holdings")
    write_header(ws, ["Position", "Ticker", "Account", "Class", "Qty",
                      "Value (SEK)", "Δ vs cost", "Fee %/yr", "Price source"])
    for i, r in enumerate(rows, start=2):
        ws.cell(row=i, column=1, value=r["name"])
        ws.cell(row=i, column=2, value=r["ticker"])
        ws.cell(row=i, column=3, value=r["account"])
        ws.cell(row=i, column=4, value=r["cls"])
        ws.cell(row=i, column=5, value=r["qty"])
        vc = ws.cell(row=i, column=6, value=r["value"])
        vc.number_format = "#,##0.00"
        gc = ws.cell(row=i, column=7, value=r["gain"])
        if isinstance(r["gain"], (int, float)):
            gc.number_format = "+0.0%;-0.0%"
            gc.fill = OK_FILL if r["gain"] >= 0 else BAD_FILL
        ws.cell(row=i, column=8, value=r["fee"])
        sc = ws.cell(row=i, column=9, value=r["source"])
        if r["source"] == "no data":
            sc.fill = BAD_FILL
        elif r["source"] != "live":
            sc.fill = WARN_FILL
    autosize(ws)


def build_history(wb):
    path = os.path.join(ROOT, "data", "valuations.csv")
    if not os.path.exists(path):
        return
    import csv
    ws = wb.create_sheet("Value history")
    with open(path) as fh:
        for i, row in enumerate(csv.reader(fh), start=1):
            for j, v in enumerate(row, start=1):
                cell = ws.cell(row=i, column=j, value=v)
                if i == 1:
                    cell.fill = HEADER_FILL
                    cell.font = HEADER_FONT
    ws.column_dimensions["D"].width = 60
    for c in "ABC":
        ws.column_dimensions[c].width = 18
    autosize(ws, max_width=60)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "master.xlsx"))
    args = ap.parse_args()

    pf = load_json(os.path.join(ROOT, "data", "portfolio.json"))
    snap_name, snap = latest_snapshot()

    rows = []
    for h in pf.get("holdings", []):
        if h.get("quantity") == 0:
            continue
        val, source = holding_value(h, snap)
        cost = h.get("cost_basis_total_sek")
        if cost is None and h.get("cost_basis_per_unit") is not None and h.get("quantity") is not None:
            cost = h["cost_basis_per_unit"] * h["quantity"]
        gain = ((val - cost) / cost) if (val is not None and cost) else "no data"
        rows.append({
            "name": h.get("name"),
            "ticker": h.get("ticker"),
            "account": h.get("account_id"),
            "cls": h.get("exposure_class"),
            "qty": h.get("quantity") if h.get("quantity") is not None else "n/a",
            "value": val if val is not None else "no data",
            "gain": gain,
            "fee": h.get("annual_fee_pct") if h.get("annual_fee_pct") is not None else "n/a",
            "source": source,
        })

    # Preserve a hand-maintained Manual Data sheet across rebuilds.
    preserved = None
    if os.path.exists(args.out):
        try:
            old = load_workbook(args.out)
            if "Manual Data" in old.sheetnames:
                preserved = [[c.value for c in row] for row in old["Manual Data"].iter_rows()]
        except Exception as exc:  # a corrupt/locked file must not block a rebuild
            print(f"note: could not read existing workbook ({exc}) — rebuilding fresh")

    wb = Workbook()
    wb.remove(wb.active)
    build_overview(wb, pf, snap, snap_name, rows)
    build_holdings(wb, rows)
    build_history(wb)

    ws = wb.create_sheet("Manual Data")
    if preserved:
        for row in preserved:
            ws.append(row)
        print(f"preserved {len(preserved) - 1} manual row(s)")
    else:
        write_header(ws, ["ticker", "field", "value", "currency", "as_of", "source", "notes"])
        ws.cell(row=2, column=7, value="Hand-entered figures go here; this sheet survives rebuilds.")
    autosize(ws)

    wb.save(args.out)
    # Match the Overview total: operating cash is excluded from portfolio value.
    counted = [r for r in rows
               if isinstance(r["value"], (int, float)) and r["cls"] != "excluded_operating_cash"]
    total = sum(r["value"] for r in counted)
    print(f"Wrote {args.out}  ({len(counted)} positions counted, total {total:,.2f} SEK)")


if __name__ == "__main__":
    main()
