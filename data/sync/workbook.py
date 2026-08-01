#!/usr/bin/env python3
"""
Builds a fresh master.xlsx with all sheets, headers, and the Dashboard's
formulas. Run standalone to create an EMPTY workbook (headers only) — the
normal path is to run scripts/migrate_from_json.py afterward to populate it
from the current JSON state.

This is the ONLY module besides sync.py that constructs sheet layout — schema.py
is the shared column definition both import from.

Usage:
  python data/sync/workbook.py                    # writes master.xlsx (headers only)
  python data/sync/workbook.py --out other.xlsx    # write elsewhere (for tests)
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema import SHEETS, ZONE1_SHEETS, ZONE2_SHEETS  # noqa: E402

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HEADER_FILL = PatternFill(start_color="1F6E63", end_color="1F6E63", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")
DASHBOARD_LABEL_FONT = Font(bold=True, size=12)
DASHBOARD_SECTION_FONT = Font(bold=True, size=14, color="1F6E63")


def _style_header_row(ws, ncols):
    for col in range(1, ncols + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="left")
    ws.freeze_panes = "A2"


def build_workbook(out_path):
    wb = Workbook()
    wb.remove(wb.active)  # drop the default sheet, we add our own in order

    # --- Zone 1: human-owned input sheets ---
    for name in ["Portfolio", "Transactions", "Watchlist", "Universe",
                 "Investment Thesis", "Pending Orders", "Settings", "Notes"]:
        cols = SHEETS[name]
        ws = wb.create_sheet(name)
        for i, col in enumerate(cols, 1):
            ws.cell(row=1, column=i, value=col)
            ws.column_dimensions[get_column_letter(i)].width = max(14, len(col) + 2)
        _style_header_row(ws, len(cols))

    # --- Zone 2: machine-write cache, hidden ---
    for name in ZONE2_SHEETS:
        cols = SHEETS[name]
        ws = wb.create_sheet(name)
        for i, col in enumerate(cols, 1):
            ws.cell(row=1, column=i, value=col)
            ws.column_dimensions[get_column_letter(i)].width = max(14, len(col) + 2)
        _style_header_row(ws, len(cols))
        ws.sheet_state = "hidden"

    # --- Dashboard: pure view, formulas only, reads Portfolio + _MarketCache ---
    dash = wb.create_sheet("Dashboard", 0)  # index 0 = first tab
    dash.sheet_view.showGridLines = False
    dash.column_dimensions["A"].width = 32
    dash.column_dimensions["B"].width = 18
    dash.column_dimensions["C"].width = 40

    dash["A1"] = "Finance Council — Dashboard"
    dash["A1"].font = Font(bold=True, size=18, color="1F6E63")
    dash["A2"] = "Computed from Portfolio + _MarketCache. Never edit this sheet by hand."
    dash["A2"].font = Font(italic=True, size=9, color="5C6669")

    dash["A4"] = "PORTFOLIO TOTAL"
    dash["A4"].font = DASHBOARD_SECTION_FONT
    dash["A5"] = "Total value (SEK)"
    dash["B5"] = "=SUMPRODUCT((Portfolio!J2:J1000)*IFERROR(VLOOKUP(Portfolio!A2:A1000,_MarketCache!A:E,5,0),0))"
    dash["A5"].font = DASHBOARD_LABEL_FONT
    dash["C5"] = "Sum of each holding's quantity x current price, from _MarketCache"
    dash["C5"].font = Font(italic=True, size=9, color="5C6669")

    dash["A7"] = "RISK TIER BREAKDOWN"
    dash["A7"].font = DASHBOARD_SECTION_FONT
    tiers = [("Secure", "secure", 60), ("Medium", "medium", 30), ("High-risk", "high", 10)]
    row = 8
    dash.cell(row=row, column=1, value="Tier")
    dash.cell(row=row, column=2, value="Value (SEK)")
    dash.cell(row=row, column=3, value="Target %")
    for c in range(1, 4):
        dash.cell(row=row, column=c).font = Font(bold=True)
    for label, key, target in tiers:
        row += 1
        dash.cell(row=row, column=1, value=label)
        dash.cell(row=row, column=2,
                  value=(f'=SUMPRODUCT((Portfolio!H2:H1000="{key}")*Portfolio!J2:J1000*'
                         f'IFERROR(VLOOKUP(Portfolio!A2:A1000,_MarketCache!A:E,5,0),0))'
                         f'/SUMPRODUCT((Portfolio!J2:J1000)*IFERROR(VLOOKUP(Portfolio!A2:A1000,_MarketCache!A:E,5,0),1))'))
        dash.cell(row=row, column=3, value=f"{target}%")

    dash["A13"] = "FEE DRAG"
    dash["A13"].font = DASHBOARD_SECTION_FONT
    dash["A14"] = "Total annual fees (SEK/yr)"
    dash["A14"].font = DASHBOARD_LABEL_FONT
    dash["B14"] = ("=SUMPRODUCT(Portfolio!M2:M1000/100*Portfolio!J2:J1000*"
                   "IFERROR(VLOOKUP(Portfolio!A2:A1000,_MarketCache!A:E,5,0),0))")
    dash["C14"] = "Sum of annual_fee_pct x market value per holding"
    dash["C14"].font = Font(italic=True, size=9, color="5C6669")

    dash["A16"] = "DATA FRESHNESS"
    dash["A16"].font = DASHBOARD_SECTION_FONT
    dash["A17"] = "Last sync"
    dash["A17"].font = DASHBOARD_LABEL_FONT
    dash["B17"] = "(set by run.py sync)"

    dash["A19"] = "Add new KPIs below this line — this sheet is designed to grow."
    dash["A19"].font = Font(italic=True, size=9, color="8FA09D")

    wb.save(out_path)
    print(f"Wrote {out_path}")
    print(f"  Zone 1 (human-owned): {', '.join(ZONE1_SHEETS)}")
    print(f"  Zone 2 (machine cache, hidden): {', '.join(ZONE2_SHEETS)}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="master.xlsx")
    args = p.parse_args()
    build_workbook(args.out)
