# Finance Council

Personal investment advisory system. No brokerage integration — you're the
human-in-the-loop for every action. This produces analysis and flags; it
never executes trades. See `SYSTEM.md` for the architecture and design
philosophy behind everything below.

## First time here

```
pip install openpyxl
python data/sync/workbook.py            # builds an empty master.xlsx
python scripts/migrate_from_json.py     # only if migrating from a pre-Excel version
```

If `master.xlsx` already exists (it does if you cloned this repo), skip both
— just open it.

## Running a sweep

1. **Edit `master.xlsx`** if anything changed since last time — new
   holdings, a trade you placed, an updated thesis, a resolved question.
   Portfolio, Transactions, Watchlist, Universe, Investment Thesis, Pending
   Orders, Settings, and Notes are all plain sheets — edit them like any
   spreadsheet.

2. **Run the deterministic prep:**
   ```
   python run.py prep
   ```
   This syncs the workbook, fetches fresh market data, and computes a
   coverage summary — no LLM calls, just data plumbing. Takes under a
   minute for a typical holdings list.

3. **Open a Claude Code session in this directory** and run the sweep:
   ```
   journal          # where did we leave off
   market-data      # (if you skipped step 2) fetch + sync + coverage
   valuation
   macro-regime
   portfolio
   thesis-review
   council          # writes reports/YYYY-MM-DD-sweep.md
   journal          # reconcile, log
   ```
   Optional, when relevant: `scout` (find new candidates), `calendar`
   (event collisions), `backtest` (stress-test a proposed allocation),
   `controller` (system health check).

4. **Read `reports/YYYY-MM-DD-sweep.md`.** That's the one file with
   everything: portfolio summary, new candidates, council's conclusions,
   open actions/decisions, missing data, and system health. You decide.
   Nothing here executes anything.

## Filling data gaps by hand

Some fields have no free automated source (non-US equity fundamentals, mainly —
SEC EDGAR only covers US filers). Run `python run.py coverage` and check the
report's `fields_missing` per ticker, then add rows to the **Manual Data**
sheet in `master.xlsx`: `ticker, field, value, currency, as_of, source, notes`.
The next `python run.py fetch` fills those fields ONLY where the automated
fetch came back empty — it never overwrites a real fetched number — and tags
every filled field so agents cite it as user-supplied, not live data.

## Debugging one data source

Each data kind fetches independently, so a broken source doesn't block the
rest:
```
python run.py fetch --only prices          # equity/ETF prices
python run.py fetch --only fundamentals    # US equity fundamentals
python run.py fetch --only crypto          # crypto prices
python run.py fetch --only macro           # FRED / Riksbank / SCB / ECB
python run.py fetch --only sentiment       # crypto Fear & Greed
python run.py fetch --only insiders_us     # SEC Form 4 filing counts, US stock holdings
python run.py fetch --only insiders_se     # Finansinspektionen Insynsregistret, .ST stock holdings
```
`--only` runs just that one module and prints its raw output — it does not
update the Dashboard (that needs the full combined snapshot). Once the
source is fixed, re-run `python run.py fetch` without `--only`.

Insider activity (both `insiders_us` and `insiders_se`) is part of every
default `python run.py fetch` sweep, not an opt-in extra — it's fetched
automatically for each stock holding and merged into the same per-ticker
snapshot record as price/fundamentals, so every lens reads it from one
standardized place. `insiders_se` guesses each Swedish issuer's search name
from the Portfolio sheet's `name` column (e.g. "Handelsbanken A (stock)" →
"Handelsbanken") — if that guess misses, run
`python scripts/fetch_insiders_se.py --issuer "<exact name>" --days 90`
directly with the right name.

## The Dashboard

Open `master.xlsx` and look at the **Dashboard** tab — total value, risk-tier
breakdown vs. target, fee drag, all computed by formula from the Portfolio
sheet and the (hidden) `_MarketCache` sheet that `run.py fetch` refreshes.
Add your own charts/KPIs below the existing rows; it's designed to grow.

## Finding candidates

```
python scripts/build_universe.py                       # refresh the S&P 500 base (run occasionally, not every sweep)
python scripts/rank_candidates.py --stack --top 30      # coarse factor rank across the whole universe
python scripts/screen_candidates.py --tickers ... --max-pe 25 ...   # hard pass/fail on the shortlist
```
Or just invoke the `scout` agent in a session — it drives this whole funnel
and hands the survivors to `valuation`/`thesis-review`.

## Recording something new mid-session

`master.xlsx` is Zone-1/human-owned — only `data/sync/sync.py` touches it.
To record a thesis nomination, a resolved note, or anything else without
opening the spreadsheet by hand:
```
python data/sync/sync.py append --sheet Watchlist --row '{"ticker": "V", "name": "Visa Inc.", "date_added": "2026-08-01", "source": "user"}'
python data/sync/sync.py read     # flow it into data/sync/*.json
```

## Checking system health

```
python run.py controller
```
Module run counts, failure counts, average duration per step — the raw
numbers behind the `controller` agent's narrative recommendations.

## Where things live

See `SYSTEM.md`'s "The project structure" section, or just: **human edits go
in `master.xlsx`, machine output lives in `data/cache/`, AI output lives in
`reports/`.** If you're ever unsure where a piece of information belongs,
that's the rule.
