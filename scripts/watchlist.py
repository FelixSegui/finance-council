#!/usr/bin/env python3
"""
The curated WATCHLIST and the candidate ranking history — plain deterministic
bookkeeping, no agent required.

WATCHLIST (`data/watchlist.json`)
  A small, persistent, curated set of companies worth monitoring. Stronger
  evidence behind them than the broad universe, survives between sweeps, and
  is NOT rebuilt from scratch each week. Names arrive three ways:
    - by hand            (`watchlist.py add TICKER --name ... --note ...`)
    - from the user's Excel Watchlist/Universe tab (import_excel_holdings.py)
    - promoted by scout  (`scout.py --promote`, when a discovery keeps ranking)
  It is not the discovery universe (that is `data/universe.json`) and it is
  not the portfolio (that is `data/portfolio.json`).

HISTORY (`data/candidate_history.csv`)
  One row per candidate per scout run: date, ticker, source, rank, lens.
  Lets the Council see persistent / improving / deteriorating candidates.
  Persistence is evidence, never an automatic BUY.

Usage:
  python scripts/watchlist.py list
  python scripts/watchlist.py add EVO.ST --name "Evolution AB" --category nordic --note "..."
  python scripts/watchlist.py remove EVO.ST --reason "thesis broken"
  python scripts/watchlist.py universe-add NIBE-B.ST --name "NIBE B" --region Nordic
  python scripts/watchlist.py history            # rank-over-time table
"""
import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCHLIST_PATH = os.path.join(ROOT, "data", "watchlist.json")
UNIVERSE_PATH = os.path.join(ROOT, "data", "universe.json")
HISTORY_PATH = os.path.join(ROOT, "data", "candidate_history.csv")

HISTORY_COLUMNS = ["run_utc", "ticker", "source", "rank", "best_lens",
                   "lens_score", "screen_status"]

WATCHLIST_NOTE = (
    "CURATED WATCHLIST — persistent between sweeps, deliberately much smaller "
    "than data/universe.json. Maintained by scripts/watchlist.py, the Excel "
    "import, and scout promotions. Presence here means 'worth monitoring', "
    "not 'buy'."
)


def _today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def verify_ticker(ticker):
    """Confirm a hand-typed ticker actually resolves to real price data before
    it is written anywhere. Nordic/European suffixes (.ST/.CO/.OL/.HE/.DE/.AS)
    are exactly where a plausible-looking wrong symbol slips in, and a wrong
    ticker is worse than an honest gap: it silently screens the wrong company.
    Returns (ok, detail)."""
    from fetch_market_data import _fetch_chart_direct
    try:
        rec = _fetch_chart_direct(ticker)
    except Exception as e:
        return False, str(e)
    if rec.get("price") is None:
        return False, "resolved but returned no price"
    return True, f"price {rec['price']} {rec.get('currency') or ''}".strip()


# --------------------------------------------------------------------------
# watchlist
# --------------------------------------------------------------------------

def load(path=None):
    path = path or WATCHLIST_PATH
    if not os.path.exists(path):
        return {"note": WATCHLIST_NOTE, "updated_utc": None, "entries": {}}
    with open(path) as f:
        data = json.load(f)
    data.setdefault("entries", {})
    return data


def save(data, path=None):
    path = path or WATCHLIST_PATH
    data["note"] = WATCHLIST_NOTE
    data["updated_utc"] = datetime.now(timezone.utc).isoformat()
    data["entries"] = dict(sorted(data["entries"].items()))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path


def tickers(data=None, path=None):
    return sorted((data or load(path))["entries"])


def add(ticker, name=None, category=None, source="manual", note=None,
        data=None, path=None, persist=True):
    """Add or update one watchlist entry. Returns True if the ticker is new.

    Updating never clobbers an existing curated field with None — an Excel
    import or a scout promotion should enrich an entry, not erase the note
    somebody wrote by hand."""
    path = path or WATCHLIST_PATH
    data = data if data is not None else load(path)
    entries = data["entries"]
    is_new = ticker not in entries
    rec = entries.get(ticker, {"added": _today(), "source": source})
    if name:
        rec["name"] = name
    if category:
        rec["category"] = category
    if note:
        rec["note"] = note
    rec.setdefault("name", None)
    rec.setdefault("category", None)
    rec.setdefault("source", source)
    rec["last_seen"] = _today()
    entries[ticker] = rec
    if persist:
        save(data, path)
    return is_new


def remove(ticker, reason=None, data=None, path=None, persist=True):
    path = path or WATCHLIST_PATH
    data = data if data is not None else load(path)
    existed = data["entries"].pop(ticker, None) is not None
    if existed:
        log = data.setdefault("removed", [])
        log.append({"ticker": ticker, "removed": _today(), "reason": reason})
        data["removed"] = log[-100:]
    if persist:
        save(data, path)
    return existed


def universe_add(ticker, name=None, sector=None, region=None,
                 asset_class="equity", path=None):
    """Add a hand-verified ticker to the broad universe's manual block. Manual
    entries survive every `build_universe.py` refresh — this is the only
    supported way to get a non-US listing into the discovery pool, since no
    free constituent feed for those is reachable from this network."""
    path = path or UNIVERSE_PATH
    with open(path) as f:
        uni = json.load(f)
    is_new = ticker not in uni["tickers"]
    rec = uni["tickers"].get(ticker, {})
    rec.update({"name": name or rec.get("name"), "sector": sector or rec.get("sector"),
                "region": region or rec.get("region"), "cik": rec.get("cik"),
                "asset_class": asset_class, "source": "manual"})
    uni["tickers"][ticker] = rec
    uni["tickers"] = dict(sorted(uni["tickers"].items()))
    manual = sum(1 for r in uni["tickers"].values() if r.get("source") == "manual")
    uni["counts"] = {"total": len(uni["tickers"]), "manual": manual,
                     "auto": len(uni["tickers"]) - manual}
    with open(path, "w") as f:
        json.dump(uni, f, indent=2)
    return is_new


# --------------------------------------------------------------------------
# candidate ranking history
# --------------------------------------------------------------------------

def append_history(rows, path=None, run_utc=None):
    """Append this run's ranked candidates. One row per candidate per run.

    Run identity is a full UTC timestamp, not a date: two scout runs on the
    same day are two runs, and collapsing them would make "previous rank"
    compare a run against itself."""
    path = path or HISTORY_PATH
    run_utc = run_utc or datetime.now(timezone.utc).isoformat(timespec="seconds")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    is_new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_COLUMNS)
        if is_new:
            w.writeheader()
        for r in rows:
            w.writerow({"run_utc": run_utc, "ticker": r["ticker"],
                        "source": r.get("source"), "rank": r.get("rank"),
                        "best_lens": r.get("best_lens"),
                        "lens_score": r.get("lens_score"),
                        "screen_status": r.get("screen_status")})
    return path


def read_history(path=None):
    path = path or HISTORY_PATH
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def history_table(path=None, top_n=10):
    """Candidate | Current Rank | Previous Rank | Times Top N | Runs seen.

    Deliberately dumb: it reports what the mechanical ranking did over time so
    the Council can weigh persistence as evidence. It draws no conclusion."""
    rows = read_history(path)
    if not rows:
        return []
    runs = sorted({r["run_utc"] for r in rows})
    current, previous = runs[-1], (runs[-2] if len(runs) > 1 else None)

    def rank_of(row):
        try:
            return int(row["rank"])
        except (TypeError, ValueError):
            return None

    cur = {r["ticker"]: rank_of(r) for r in rows if r["run_utc"] == current}
    prev = {r["ticker"]: rank_of(r) for r in rows if r["run_utc"] == previous} if previous else {}
    times_top = {}
    seen = {}
    for r in rows:
        rk = rank_of(r)
        seen[r["ticker"]] = seen.get(r["ticker"], 0) + 1
        if rk is not None and rk <= top_n:
            times_top[r["ticker"]] = times_top.get(r["ticker"], 0) + 1
    out = []
    for t, rk in sorted(cur.items(), key=lambda kv: (kv[1] is None, kv[1])):
        out.append({"ticker": t, "current_rank": rk, "previous_rank": prev.get(t),
                    "times_top_n": times_top.get(t, 0), "runs_seen": seen.get(t, 0)})
    return out


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")

    a = sub.add_parser("add")
    a.add_argument("ticker")
    a.add_argument("--name")
    a.add_argument("--category")
    a.add_argument("--note")
    a.add_argument("--source", default="manual")
    a.add_argument("--no-verify", action="store_true",
                   help="skip the live ticker-resolves check (offline use only)")

    r = sub.add_parser("remove")
    r.add_argument("ticker")
    r.add_argument("--reason")

    u = sub.add_parser("universe-add")
    u.add_argument("ticker")
    u.add_argument("--name")
    u.add_argument("--sector")
    u.add_argument("--region")
    u.add_argument("--asset-class", default="equity")
    u.add_argument("--no-verify", action="store_true",
                   help="skip the live ticker-resolves check (offline use only)")

    h = sub.add_parser("history")
    h.add_argument("--top-n", type=int, default=10)

    args = p.parse_args()

    if args.cmd == "list":
        data = load()
        print(f"Watchlist: {len(data['entries'])} entries (updated {data.get('updated_utc')})")
        for t, rec in data["entries"].items():
            print(f"  {t:<12} {(rec.get('category') or '-'):<18} "
                  f"{(rec.get('name') or '')[:34]:<34} src={rec.get('source')}")
    elif args.cmd == "add":
        if not args.no_verify:
            ok, detail = verify_ticker(args.ticker)
            if not ok:
                sys.exit(f"{args.ticker} does not resolve to real price data ({detail}) — "
                         f"not written. Verify the exchange suffix; do not guess it.")
            print(f"verified {args.ticker}: {detail}")
        new = add(args.ticker, args.name, args.category, args.source, args.note)
        print(f"{'Added' if new else 'Updated'} {args.ticker} in {WATCHLIST_PATH}")
    elif args.cmd == "remove":
        print(f"{'Removed' if remove(args.ticker, args.reason) else 'Not present:'} {args.ticker}")
    elif args.cmd == "universe-add":
        if not args.no_verify:
            ok, detail = verify_ticker(args.ticker)
            if not ok:
                sys.exit(f"{args.ticker} does not resolve to real price data ({detail}) — "
                         f"not written. Verify the exchange suffix; do not guess it.")
            print(f"verified {args.ticker}: {detail}")
        new = universe_add(args.ticker, args.name, args.sector, args.region, args.asset_class)
        print(f"{'Added' if new else 'Updated'} {args.ticker} in {UNIVERSE_PATH} (manual block)")
    elif args.cmd == "history":
        table = history_table(top_n=args.top_n)
        if not table:
            print(f"No history yet — {HISTORY_PATH} is written by scout.py.")
            return
        print(f"{'TICKER':<12}{'RANK':>6}{'PREV':>6}{'TOP'+str(args.top_n):>7}{'RUNS':>6}")
        for row in table:
            print(f"{row['ticker']:<12}{str(row['current_rank']):>6}"
                  f"{str(row['previous_rank']):>6}{row['times_top_n']:>7}{row['runs_seen']:>6}")


if __name__ == "__main__":
    main()
