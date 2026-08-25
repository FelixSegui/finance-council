# Finance Council

A personal investment advisory system that runs in Claude Code. It answers
one question every sweep: **what are the best investments available to me
right now?** — then, separately, whether they fit the portfolio you already
have.

No brokerage integration. It analyses and flags; you place every trade.
`CLAUDE.md` holds the design rules every agent must follow.

## The funnel in one picture

```
data/universe.json         ~624 names (S&P 500 + user-verified Nordic/Europe)
        |                  build_universe.py, refreshed ~monthly
        v
scripts/scout.py           deterministic — five lens rankings, no LLM
        |                  quality / value / growth / defensive / contrarian
        |                  max 3 slots per sector per lens; share classes merged;
        |                  scores shrunk toward neutral in proportion to coverage
        v
data/screens/*-candidates.csv    ~60-75 candidates, each tagged
        |                        holding | watchlist | new
        |                        ~20 marked focus=Y for full analysis
        v
council agent              seven analyst voices -> Chairman
        |
        v
portfolio agent            fit: concentration, currency, cash, sizing
        |
        v
reports/YYYY-MM-DD-council-memo.md    BUY / HOLD-WATCH / SELL / NO ACTION
```

Hundreds of stocks are narrowed by **code**. Only the survivors cost
reasoning. Five separate lenses instead of one blended score, so a
high-growth name isn't killed by a static trailing-P/E rule and a deep-value
name isn't killed by a growth rule.

## Running a sweep

```bash
pip install -r requirements.txt

python scripts/build_universe.py                  # periodic discovery refresh
python scripts/fetch_market_data.py --tickers SHB-A.ST,INVE-A.ST \
       --crypto ethereum,bitcoin --insiders
python scripts/scout.py                           # the funnel + SCOUT HEALTH
python scripts/position_report.py                 # how positions are behaving
```

Then open Claude Code here and run the agents in order:

`journal` → `market-data` → `scout` → (`valuation`, `macro-regime`,
`portfolio`, `thesis-review`) → `council` → `journal` → `meta`

## SCOUT HEALTH

Every scout run ends with a block like this:

```
SCOUT HEALTH

  Universe:   624
  Fetched:    624   (cache 0, new 624, failed 0)
  Ranked:     614   (names that earned >=1 lens score)
  Candidates: 72    (holdings 8, watchlist 30, new 34)
  Focus:      22    (full Council analysis; the rest stay as context)
  Screened:   72
  Passed:     35
  Missing:    19
  Failed:     18

  Status: VALID
```

`Status` is the point. `VALID` means the pipeline was healthy, so a thin
result is a real conclusion. `DEGRADED` names what to distrust.
`INVESTIGATE_ZERO_PASS` fires whenever nothing passes and runs a diagnostic —
was the universe loaded? did fetching fail? is the missing-data rate
abnormal? is one threshold alone rejecting everything? are the units right? —
because a broken filter and a quiet market produce identical-looking empty
screens. "We found nothing", "we didn't look" and "the search broke" are
never allowed to blur together.

## The seven Council voices

| Voice | Question |
|---|---|
| Fundamental / Quality | Is this an excellent business? |
| Valuation | Is this price attractive relative to the business? |
| Growth / Opportunity | Is the market underestimating future growth? |
| Defensive / Risk | What can go wrong, and what should we own if it does? |
| Contrarian / Risk Taker | Where is the market potentially wrong? |
| Macro / Regime | Does the environment change this opportunity's attractiveness? |
| Copycat / Smart Money | What are informed insiders actually doing? |

The Chairman weighs the **quality of the arguments**, never a vote count, and
never averages a disagreement away. Diversification is deliberately not a
voice — it is the `portfolio` agent's job, applied once, afterwards.

## Missing data must not buy a shortlist slot

Averaging fewer inputs makes a score *noisier*, not more cautious — the mean
of k z-scores has standard deviation 1/√k, so a half-covered name lands
further out in the tails, and a top-N shortlist is a cut on exactly those
tails. Measured before the fix: growth scores built on partial data averaged
|1.048| against |0.396| for full-coverage names, and Swedish names (whose PEG
and forward-P/E coverage runs ~28 points below US names') took 6 of 10 slots
on two lenses against an expected 1.7.

Lens scores are now scaled by √(coverage), which puts a partial score back on
the full-coverage scale. Nothing is imputed and no name is excluded — a thin
score simply cannot claim more conviction than its inputs support, and the
`thin_lenses` column tells the Council which rankings rest on partial
evidence.

## Maintaining the lists

```bash
python scripts/watchlist.py list
python scripts/watchlist.py add EVO.ST --name "Evolution AB" --category nordic
python scripts/watchlist.py remove EVO.ST --reason "thesis broken"
python scripts/watchlist.py universe-add NIBE-B.ST --region Nordic
python scripts/watchlist.py universe-import my_tickers.csv --dry-run
python scripts/watchlist.py history          # rank over time
python scripts/scout.py --promote            # scout adds its best new finds
```

Every write path verifies the ticker against Yahoo first, and **verifies the
company name too** — "the ticker resolves" is not the same as "the ticker is
the company you meant". `VITR.ST` resolves perfectly, to Vitrolife, not to
Sobi; screening the wrong company on a real price feed produces confident,
wrong analysis with nothing anywhere to flag it.

`universe-import` takes a CSV of `ticker,company name` and sorts every row
into one bucket:

| Bucket | What happened |
|---|---|
| added / already | verified; stored under Yahoo's own name |
| symbol corrected | the CSV's ticker was wrong, but the company was found by name on the expected exchange and re-verified |
| name mismatch | the ticker is real but is a **different company**. Never written |
| no longer trading | delisted, acquired or taken private. Correctly excluded |
| unresolved | no listing found by symbol or by name. Never written |

On a real 120-row Swedish list, 31 rows were wrong: 16 had recoverable
symbols, 5 named a different company, 3 were delisted, 7 did not exist.

## Where the truth lives

| Path | What it is |
|---|---|
| `data/portfolio.json` | Source of truth: accounts, holdings, theses, targets |
| `data/investor_profile.json` | Risk tolerance, horizon, constraints |
| `data/universe.json` | Broad discovery universe |
| `data/watchlist.json` | Curated, persistent watchlist |
| `data/candidate_history.csv` | Candidate rank over time |
| `data/cache/snapshots/` | Timestamped market data — every number traces here |
| `data/screens/` | Scout output |
| `OPEN_ITEMS.md` | Single list of everything outstanding (P = portfolio, S = system) |
| `data/decisions.csv` | Decision ledger — every pick, with the evidence it was made on |
| `reports/system-scorecard.md` | Six-pillar answer to "is this getting better?" |
| `reports/SESSION_LOG.md` | Append-only memory across sessions |

Your Excel workbook is an **input**, not a database: it supplies manual data,
Nordic fundamentals and watchlist edits via
`scripts/import_excel_holdings.py`, which is strictly read-only and *merges*
into the watchlist rather than replacing it.

`archive/` is historical reference only. Nothing active depends on it.

## Two things this system refuses to do

1. **Invent a number.** Every figure traces to a fetched file or is labelled
   user-relayed. A missing price reads "no data", never a stale or estimated
   one.
2. **Act.** It analyses and flags. You place every trade.

## Tests

```bash
python3 -m unittest discover -s tests -v
```
