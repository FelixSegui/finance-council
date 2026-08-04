# Finance Council

Personal investment advisory system. No brokerage integration — you are the
human-in-the-loop for every action. This produces analysis and flags; it
never executes trades. See `CLAUDE.md` for the design philosophy and the
rules every agent must follow.

## Where the truth lives

**`data/portfolio.json` is the source of truth.** Agents maintain it. You
should rarely need to open it.

**`master.xlsx` is a generated view.** The `Overview` and `Holdings` sheets
are rebuilt from the JSON every time and never read back by anything — look,
don't maintain; any edit there is overwritten on the next rebuild. As of
2026-08-04, `Overview`'s totals/allocation/drift are **live Excel formulas**
(`SUMIF`/`SUMPRODUCT`) over the raw facts on `Holdings`, not Python-computed
static numbers — open it, click a cell, see exactly what it's summing.

Two sheets are the exception and survive every rebuild verbatim:
- **`Manual Data`** — hand-entered figures, `ticker, field, value, currency,
  as_of, source, notes`.
- **`Fundamentals`** — pre-seeded with a row per tradeable holding
  (ticker + name only). This is where **Excel's own "Stocks" data type**
  comes in: this pipeline has no live path to it (needs a real, internet-
  connected Microsoft 365 Excel session — confirmed empirically, see
  `OPEN_ITEMS.md`'s closed items), but if YOU have it, use it directly in
  this sheet — convert a ticker cell to the Stocks data type, pull whatever
  fields you want (P/E, sector, market cap, dividend yield, 52-week range,
  beta...) into that row, save. `python scripts/import_fundamentals_tab.py`
  then folds whatever's filled in into `data/company_profiles/<TICKER>.json`
  — the cache `swedish-equity-review` reads — tagged with source and date.
  **Limitation, stated plainly:** this is a periodic manual refresh, not a
  live feed. openpyxl can't read or preserve a live Stocks link, only the
  last value Excel cached — redo the lookup in your own Excel and save again
  whenever you want fresher numbers.

This direction is deliberate. An earlier design made the workbook the source
of truth and had the user keep it current; that puts the maintenance burden
on the person, which is backwards. The Fundamentals tab doesn't reverse that
— it's still optional, still just data you feed in when you have it.

## Running a sweep

```
pip install yfinance openpyxl

python scripts/fetch_market_data.py --tickers SHB-A.ST,INVE-A.ST --crypto ethereum,bitcoin
python scripts/fetch_calendar.py    --tickers SHB-A.ST,INVE-A.ST --days 45
python scripts/position_report.py          # how the positions are behaving
python scripts/build_workbook.py           # refresh master.xlsx
```

Then open a Claude Code session in this directory and run the agents in
order: `journal` → the four lenses (`valuation`, `macro-regime`,
`portfolio`, `thesis-review`) → `council` → `journal` again. `CLAUDE.md`
documents the full flow and why the order matters.

## The files that matter

| Path | What it is |
|---|---|
| `data/portfolio.json` | Source of truth: accounts, holdings, theses, targets |
| `data/investor_profile.json` | Risk tolerance, horizon, constraints |
| `OPEN_ITEMS.md` | **Single list of everything outstanding** (P = portfolio, S = system) |
| `master.xlsx` | Generated read-only view (`Overview`/`Holdings`, formula-based) + two sheets that survive rebuilds: `Manual Data`, `Fundamentals` |
| `reports/SESSION_LOG.md` | Append-only memory across sessions |
| `data/cache/snapshots/` | Timestamped market data — every number traces here |

## Two things this system refuses to do

1. **Invent a number.** Every figure traces to a file in `data/cache/`
   fetched in the same session, or is explicitly labelled user-relayed. A
   missing price reads "no data", never a stale or estimated one.
2. **Act.** It analyses and flags. You place every trade.

## Parked capability

`run.py`, `data/sync/`, `scripts/fetchers/` and `scripts/funnel/` came from
a parallel Excel-backed branch merged on 2026-08-03. They are **not wired
into the live flow** — they belong to that branch's runtime. Their agent
definitions are preserved in `archive/agents-from-excel-branch/` with notes
on what is worth porting. Tracked in `OPEN_ITEMS.md`.
