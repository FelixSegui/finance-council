"""
Column schemas for master.xlsx — the single definition every other module
(the workbook builder, the sync reader, the migration script) imports from.
Changing a sheet's columns means editing this file once, not three places.

Sheet names starting with "_" are Zone 2 (machine-write cache, hidden by
default) — everything else is Zone 1 (human-owned, scripts only ever read it).
"""

SHEETS = {
    "Dashboard": [],  # formula-only sheet, built directly by workbook.py, no data rows

    "Portfolio": [
        "ticker", "name", "account_id", "institution", "wrapper",
        "instrument_type", "exposure_class", "risk_tier", "currency",
        "quantity", "cost_basis_per_unit", "cost_basis_total_sek",
        "annual_fee_pct", "date_acquired", "no_ticker_reason", "notes",
    ],

    "Transactions": [
        "date", "ticker", "account_id", "action", "quantity",
        "price_per_unit", "currency", "proceeds_or_cost_sek", "tax_sek",
        "tax_free_wrapper", "notes",
    ],

    "Watchlist": [
        "ticker", "name", "date_added", "source", "notes",
    ],

    "Universe": [
        "ticker", "category", "name", "currency", "date_added", "source",
    ],

    "Investment Thesis": [
        "ticker", "date", "status", "risk_tag", "policy_tailwind", "thesis",
    ],

    "Pending Orders": [
        "ticker", "name", "account_id", "committed_amount_sek",
        "committed_date", "status", "tier", "rationale",
    ],

    "Settings": [
        "key", "value", "notes",
    ],

    "Notes": [
        "id", "date", "status", "text", "resolved_date", "resolution",
    ],

    "Manual Data": [
        "ticker", "field", "value", "currency", "as_of", "source", "notes",
    ],

    "_MarketCache": [
        "ticker", "last_price", "currency", "price_as_of",
        "market_value_sek", "fetch_status", "data_source",
    ],
}

# Zone 1 = human-owned input sheets. Zone 2 = machine-write cache.
ZONE1_SHEETS = [s for s in SHEETS if not s.startswith("_") and s != "Dashboard"]
ZONE2_SHEETS = [s for s in SHEETS if s.startswith("_")]
