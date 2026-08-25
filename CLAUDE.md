# Finance Council — Investment Analytics System

Personal investment advisory system, run locally through Claude Code. No
brokerage integration — you are the human-in-the-loop for every action. This
system produces analysis and flags. It never executes a trade.

## What this system is for

**Stock selection.** It exists to keep answering one question:

> *What are the best investments available to me right now?*

That is **not** the same question as *"what should I do with the stocks I
already own?"* Both matter, but they are separate stages and the order is
fixed: find the best opportunities first, then decide what fits the
portfolio. A sweep that only reviews current holdings is a system failure.

## The canonical flow

```
DATA                     fetch_market_data.py -> data/cache/snapshots/
  |
BROAD UNIVERSE           data/universe.json      (~500-2,000 names)
  |
MECHANICAL SCOUT         scripts/scout.py        (code, not an LLM)
  |                      five lens rankings -> ~50-75 plausible names
WATCHLIST + CANDIDATES   data/watchlist.json + newly discovered names
  |                      -> data/screens/<ts>-candidates.csv
  |                      ~20 marked focus=Y (holdings + top ranked)
SPECIALIST COUNCIL       seven independent analyst voices
  |
CHAIRMAN                 weighs argument quality, not vote counts
  |
PORTFOLIO FIT            portfolio agent's diversification/capital read
  |
FINAL ACTION             BUY / HOLD-WATCH / SELL / NO ACTION
```

The wide part of the funnel is **deterministic code**. Hundreds of stocks
never reach an LLM. Judgement is spent on ~10–20 names that survived.

## The four words, defined exactly

| Term | What it means | What it is NOT |
|---|---|---|
| **UNIVERSE** (`data/universe.json`) | The broad pool the system is allowed to discover from. Hundreds to low thousands of names. Membership implies nothing about quality. | Not holdings. Not the watchlist. Not a recommendation list. |
| **WATCHLIST** (`data/watchlist.json`) | Small, curated, persistent set worth monitoring. Survives between sweeps. Names arrive by hand, from Excel, or by scout promotion. | Not the discovery universe. Not rebuilt from scratch each sweep. |
| **SCOUT** (`scripts/scout.py`) | The mechanism that reduces the universe to a candidate set. Deterministic screening and ranking, capped at 3 slots per sector per lens, with share classes of one company merged. Runs **every** stock-selection sweep. | Not deep analysis. Not a stock picker. "Scout was not invoked" is not a valid outcome. |
| **COUNCIL** (`.claude/agents/council.md`) | Deep investment reasoning over a manageable candidate set. Compares holdings, watchlist names and new discoveries side by side. | Not a portfolio audit. Not a place to re-derive concentration math. |
| **PORTFOLIO** (`.claude/agents/portfolio.md`) | What fits *this* portfolio, applied **after** opportunity selection. The single diversification authority. | Not a stock-picking voice. Never defines the discovery universe. |

## The three outcomes that must never be conflated

1. **"We searched and found nothing"** — the funnel ran, the health block is
   `VALID`, and no name cleared the bar. A legitimate conclusion.
2. **"We did not search"** — scout didn't run. Never acceptable on a normal
   sweep; the memo must say so outright.
3. **"The search failed"** — the funnel ran and broke. Status
   `INVESTIGATE_ZERO_PASS` or `DEGRADED`: universe empty, fetches failing,
   missing-data rate abnormal, one threshold killing everything, a unit/scale
   mistake. `scripts/scout.py` runs this diagnostic automatically whenever
   zero names pass, because a broken filter and a quiet market produce an
   identical-looking empty screen.

## Why this exists (read before extending)

The biggest risk in an LLM-based investment system is **confident structure
built on stale or hallucinated numbers.** Every numerical claim in every
agent's output must trace to a file under `data/` written in the same
session. No agent invents a price, ratio or macro figure. If data wasn't
fetched, the agent says "no data" — it does not estimate from training
knowledge, which is stale by definition.

The second-biggest risk is **process for its own sake.** Extra agents, extra
reports and elaborate structure are worthless unless they improve stock
selection or decision quality. When in doubt, delete a step.

## Running a sweep

```bash
python scripts/build_universe.py            # periodic — discovery refresh (~30d)
python scripts/watchlist.py universe-import <csv>   # add hand-collected tickers, verified
python scripts/fetch_market_data.py --tickers ... --crypto ethereum,bitcoin \
       --insiders --fi-issuers "Handelsbanken,Investor"
python scripts/scout.py                     # every sweep — the funnel
python scripts/position_report.py           # how the positions are behaving
```

Then, in the Claude Code session:

0. **`journal`** (session-start mode) — where the last sweep left off, pending
   decisions, open items, and `meta`'s recommended emphasis. No analysis
   before this runs.
1. **`market-data`** — one snapshot; everything else reads it.
1a. *(optional)* the user's Excel workbook, if a fresh copy is available:
   download via the Google Drive connector, then
   `python scripts/import_excel_holdings.py --xlsx <path>`. Read-only. It
   supplies Nordic fundamentals no free headless source reaches, and **merges**
   into `data/watchlist.json` — it never overwrites it. Skip it if there's no
   fresh copy; nothing downstream blocks.
2. **`scout`** — runs the funnel, reports SCOUT HEALTH, hands over the
   candidate CSV. Every sweep.
3. **`valuation`, `macro-regime`, `portfolio`, `thesis-review`** — the lenses,
   over holdings *and* candidates. Optional: `calendar` (event collisions),
   `backtest` (risk profile of a proposed allocation).
4. **`council`** — last. Seven voices → Chairman → portfolio fit → one memo in
   `reports/`.
5. **`journal`** (sweep-end) — reconcile last sweep's calls against today's
   data, append the entry. An unlogged sweep is invisible to the next session.
6. **`meta`** — did the system get better at deciding? Maintains S-items.
7. `python scripts/check_unmerged_work.py`, then push. Not optional — on
   2026-08-03 the repo was found forked in two for 12 days with ~25 commits
   invisible on each side.

Separately, roughly monthly: the `monthly-contribution` skill (how much new
money to deploy) and `swedish-equity-review` (deep dive on the Swedish sleeve).

## Data ownership — one canonical owner per concept

| Path | Owns |
|---|---|
| `data/portfolio.json` | Portfolio truth: accounts, holdings, theses, targets |
| `data/investor_profile.json` | Client profile: risk tolerance, horizon, buffer, constraints |
| `data/universe.json` | Broad investable universe |
| `data/watchlist.json` | Curated persistent watchlist |
| `data/candidate_history.csv` | Candidate rank over time |
| `data/cache/snapshots/` | Market-data snapshots (every number traces here) |
| `data/screens/` | Scout outputs (candidates CSV + full JSON) |
| `data/company_profiles/` | Per-company research that doesn't change monthly |
| `data/definitions.json` | Pinned definitions of ambiguous shared terms |
| `reports/` | Human-readable memos + `SESSION_LOG.md` |
| `OPEN_ITEMS.md` | The single list of everything outstanding |

Do not create a competing "truth" file. If one appears, migrate its content
and delete it.

**Excel stays an input, never a database.** `portfolio.json` is authoritative.
The user's workbook supplies manual data, Nordic fundamentals and watchlist
edits; `import_excel_holdings.py` reads it and never writes back.

**`archive/` is history only.** No active code, prompt, workflow, doc or
import may depend on anything under it. Port an idea deliberately if it is
worth having; leave the archived version unused.

## Data sources (all free, no keys)

Yahoo Finance quoteSummary (price + full fundamentals), CoinGecko, FRED,
Riksbank SWEA, SCB PxWeb, ECB Data Portal, alternative.me Fear & Greed, SEC
EDGAR Form 4 counts (`--insiders`), Finansinspektionen Insynsregister
(`--fi-issuers`), and the S&P 500 / NASDAQ / NYSE constituent CSVs used to
build the universe.

**Yahoo fundamentals note.** Yahoo's fundamentals endpoint needs a "crumb"
token from fc.yahoo.com. yfinance's own client fails on this network (its
curl_cffi browser-TLS impersonation gets connection-reset by Yahoo's anti-bot
layer). `scripts/fetch_market_data.py` bypasses yfinance entirely and talks to
the quoteSummary API via plain `urllib` + a cookie jar, which works reliably
for both US and Nordic tickers. One real gap remains: Yahoo's legacy
multi-year cash-flow module exposes only `netIncome` per year, so free cash
flow is trailing-only, not a multi-year series. For a real FCF trend, use a
company's own cash-flow statement (PDF via the `pdf` skill).

**Never write an unverified ticker.** Every path that adds a ticker
(`watchlist.py add`, `universe-add`, `universe-import`) checks with Yahoo that
the symbol resolves *and* that its name is the company claimed. A resolving
ticker is not a correct ticker: `VITR.ST` is Vitrolife, not Sobi. When a
symbol fails, the company is looked up by name on the expected exchange and
re-verified — a lookup against Yahoo's index, never a guessed suffix. Nasdaq
Stockholm names share classes "Elekta AB ser. B", so the search tries that
form too; a plain name search returns Frankfurt and Pink Sheet lines and
misses the home listing entirely.

**Swedish insider data.** Finansinspektionen's register is real and free, and
`fetch_market_data.py --fi-issuers` reads it — but search is by **issuer name**
with exact Swedish spelling (å/ä/ö). ASCII transliteration returns zero rows,
which is indistinguishable from "no insider activity". Börsdata needs a key.
Placera / Dagens Industri / Affärsvärlden are editorial, not APIs — treat
anything from them as user-relayed.

## Scope

**In:** equities, ETFs/index funds, crypto, and gold as a single named
commodity (crash-hedge diversifier, user-directed 2026-08-22 —
`fetch_market_data.py` handles `GC=F` and listed physical-gold ETCs like
`SGOL` through the same pipeline). Macro (rates, curve, inflation, dollar) is
regime context, not a tradeable class.

**Out until a paid feed exists:** individual bonds, options, other
alternatives. Free data for these is non-existent or too thin to trust. Do
not let any agent generate options or alternatives recommendations from
scraped data — that is false confidence, not analysis. Say so and stop.

Which specific ISK-eligible gold ETC the user actually buys is a real-ticker
choice that must be verified, never guessed. `GC=F`/`SGOL` are directional
price proxies for sizing discussion only.

## Currencies

Base currency is SEK. Equity data may arrive in USD/EUR/DKK — convert using
`sek_per_usd` / `sek_per_eur` from the macro snapshot before computing
weights. A missing FX rate is a missing weight, never an assumed 1:1. Crypto
certificates trade on Nasdaq Stockholm in SEK — fetch them as `.ST` tickers,
not via CoinGecko.

## Priority order (Swedish retail, ~200–250k SEK)

1. **Account wrapper efficiency** (ISK vs taxed AF) — **DONE 2026-08-03.** All
   capital is in the ISK.
2. **Fee drag** — **SUBSTANTIALLY DONE.** One item left: the 2.5% BTC
   certificate (P4).
3. **Allocation / drift** — live, mechanical, owned by `portfolio`.
4. **Selection** — **the main active work**, because 1–3 are closed. This is
   why the system is built as a discovery funnel rather than a portfolio audit.

The old rule "never lead with a stock pick while a wrapper inefficiency sits
unaddressed" still holds but is no longer binding — there is no such
inefficiency left. Re-flagging settled structural facts every week is noise,
not diligence.

## Time horizons

Every Council call carries a horizon tag. The system's edge shrinks as the
horizon shortens.

- **Long (3y+)** — allocation, wrapper, fees. Structural, highest edge.
- **Medium (6mo–3y)** — valuation entry/exit, thesis health, regime
  positioning. Where selection work lands.
- **Short (<6mo)** — tactical overlay only: capped at 10% of portfolio, never
  High confidence, always flagged as tactical. LLMs on free data have no
  demonstrated short-term edge, and the system says so rather than pretending.

## Open items

`OPEN_ITEMS.md` is the single review surface. **P-items** are the user's
portfolio questions — only the user closes those, and `meta` must never edit
them. **S-items** are system improvements — `meta` proposes, nothing
self-applies, the user approves with "apply S3". Closed items move to the
bottom log with a one-line resolution; never delete an item silently.

If an open item makes a conclusion untrustworthy, the memo leads with it
rather than burying it.

## Session continuity

`reports/SESSION_LOG.md` is the memory across sessions — append-only, one
entry per sweep, written by `journal`, which also reconciles previous calls
against current data. That reconciliation is the only calibration mechanism
this system has. `data/valuations.csv` accumulates portfolio-value
observations for `scripts/performance.py` ("are we beating just buying the
index?"). A session that did meaningful work without a log entry is a process
failure — fix it before ending.

**Token hygiene.** `data/portfolio.json` keeps short current-state summaries
only; superseded narratives live in `data/portfolio_history_archive.md`, read
during reconciliation or deep audits, not every sweep. Per-company research
that doesn't change monthly lives in `data/company_profiles/<TICKER>.json`
(schema: `_SCHEMA.md`). Don't let notes and thesis fields regrow into essays.

## Model tiering

`council` runs on `opus` — the single highest-stakes synthesis point and the
only output the user acts on directly. `market-data`, `scout` and `calendar`
run on `haiku` — script execution, mechanical screening, event fetching.
Everything else inherits the default.

## Branching rule

Branches for testing are fine and encouraged. Leaving one unmerged and
unannounced is not. Any branch holding commits `main` doesn't have at the end
of a session must be merged or explicitly reported to the user by name, with
what's on it. Never let work go quiet on a branch.
