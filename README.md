# Finance Council

Personal investment advisory system. No brokerage integration — you are the
human-in-the-loop for every action. This produces analysis and flags; it
never executes trades. See `CLAUDE.md` for the design philosophy and the
rules every agent must follow.

## Where the truth lives

**`data/portfolio.json` is the source of truth.** Agents maintain it. You
should rarely need to open it.

**`master.xlsx` is a generated view.** It is rebuilt from the JSON and is
never read back by anything. Look at it, don't maintain it — you cannot
break the system by editing it, and any edit is overwritten on the next
rebuild. The one exception is its `Manual Data` sheet, which survives
rebuilds so hand-entered figures aren't lost.

This direction is deliberate. An earlier design made the workbook the source
of truth and had the user keep it current; that puts the maintenance burden
on the person, which is backwards.

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
| `master.xlsx` | Generated read-only view of holdings and allocation |
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
