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
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCHLIST_PATH = os.path.join(ROOT, "data", "watchlist.json")
UNIVERSE_PATH = os.path.join(ROOT, "data", "universe.json")
HISTORY_PATH = os.path.join(ROOT, "data", "candidate_history.csv")

# `price` and `currency` are what make this file measurable rather than merely
# descriptive: without a price recorded AT the moment of the ranking, no
# forward return can ever be attributed to a lens, and "does the mechanical
# screen actually rank anything real?" stays unanswerable forever.
HISTORY_COLUMNS = ["run_utc", "ticker", "source", "rank", "best_lens",
                   "lens_score", "screen_status", "price", "currency",
                   "z_quality", "z_value", "z_growth", "z_defensive",
                   "z_contrarian"]

WATCHLIST_NOTE = (
    "CURATED WATCHLIST — persistent between sweeps, deliberately much smaller "
    "than data/universe.json. Maintained by scripts/watchlist.py, the Excel "
    "import, and scout promotions. Presence here means 'worth monitoring', "
    "not 'buy'."
)


def _today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# Corporate-form noise that carries no identifying information. Stripped from
# both sides before a name is compared, so "AB Volvo (publ)" and "Volvo Group"
# are recognised as the same company.
_NAME_NOISE = {
    "ab", "publ", "plc", "asa", "a/s", "as", "oyj", "abp", "se", "nv", "sa",
    "inc", "corp", "corporation", "co", "company", "group", "holding",
    "holdings", "the", "limited", "ltd", "aktiebolag", "industrier",
}


def _normalise_name(name):
    """Lowercase, drop punctuation and corporate-form words, return tokens."""
    if not name:
        return set(), ""
    cleaned = "".join(c if c.isalnum() or c.isspace() else " " for c in name.lower())
    tokens = {t for t in cleaned.split() if t and t not in _NAME_NOISE}
    return tokens, " ".join(sorted(tokens))


def name_matches(claimed, actual):
    """Does `claimed` plausibly name the same company as `actual`?

    This exists because "the ticker resolves" is NOT the same as "the ticker is
    the company you meant", and the difference is dangerous rather than
    cosmetic: VITR.ST resolves perfectly — to Vitrolife, not to Sobi. Screening
    the wrong company on a real price feed produces confident, wrong analysis
    with nothing anywhere to flag it.

    Returns one of "match" / "near" / "mismatch"."""
    import difflib
    a_tokens, a_str = _normalise_name(claimed)
    b_tokens, b_str = _normalise_name(actual)
    if not a_tokens or not b_tokens:
        return "mismatch"
    if a_tokens & b_tokens:
        return "match"
    # No shared token, but a typo ("Bonavia" vs "Bonava") should not read the
    # same as a genuinely different company ("Sobi" vs "Vitrolife").
    if difflib.SequenceMatcher(None, a_str, b_str).ratio() >= 0.80:
        return "near"
    return "mismatch"


def verify_ticker(ticker, claimed_name=None):
    """Confirm a hand-typed ticker resolves AND is the company it claims to be.

    Nordic/European suffixes (.ST/.CO/.OL/.HE/.DE/.AS) are exactly where a
    plausible-looking wrong symbol slips in, and a wrong ticker is worse than
    an honest gap. Returns (status, info) where status is one of:
      "ok"            — resolves; name matches (or no name was claimed)
      "name_mismatch" — resolves, but to a different company than claimed
      "unresolved"    — no such listing
    `info` always carries Yahoo's own long_name, exchange, quote_type and
    currency when the ticker resolved, so the CALLER writes the authoritative
    name rather than the hand-typed one."""
    import time as _time
    from fetch_market_data import _yahoo_session
    # Yahoo rate-limits; a single transient 429 must not decide whether a real
    # company enters the universe. Observed live: the same ticker resolved on
    # one run and 404'd on the next.
    r, last_error = None, None
    for attempt in range(3):
        try:
            r = _yahoo_session.fetch_quote_summary(ticker, modules="quoteType,price")
            break
        except Exception as e:
            last_error = e
            if "404" in str(e):
                break            # a genuine "no such symbol" — do not retry
            _time.sleep(0.8 * (attempt + 1))
    if r is None:
        return "unresolved", {"error": str(last_error)}
    q = r.get("quoteType") or {}
    pr = r.get("price") or {}
    info = {
        # Some Stockholm lines carry a name only in the price module
        # (COIC.ST returns quoteType.longName = null but is very much listed).
        "long_name": (q.get("longName") or q.get("shortName")
                      or pr.get("longName") or pr.get("shortName")),
        "exchange": q.get("exchange"),
        "quote_type": q.get("quoteType"),
        "currency": pr.get("currency"),
        "price": (pr.get("regularMarketPrice") or {}).get("raw")
                 if isinstance(pr.get("regularMarketPrice"), dict)
                 else pr.get("regularMarketPrice"),
    }
    if info["price"] is None and not info["long_name"]:
        # Yahoo knows the symbol but serves nothing for it — the signature of a
        # delisted or acquired company, which is a different problem from a
        # symbol that never existed and needs a different fix from the user.
        return "unresolved", {"error": "no longer trading (delisted, acquired, "
                                       "or taken private)"}
    if claimed_name:
        verdict = name_matches(claimed_name, info["long_name"] or "")
        info["name_check"] = verdict
        if verdict == "mismatch":
            return "name_mismatch", info
    return "ok", info


# Ticker suffix -> the exchange code Yahoo reports for that listing. Used to
# keep a symbol search on the market the user actually trades in: "Sweco"
# matches four Frankfurt and Munich lines before the Stockholm one.
_SUFFIX_EXCHANGE = {
    ".ST": {"STO"}, ".CO": {"CPH"}, ".OL": {"OSL"}, ".HE": {"HEL"},
    ".DE": {"GER", "FRA", "MUN"}, ".AS": {"AMS"}, ".PA": {"PAR"}, ".MI": {"MIL"},
}
_US_EXCHANGES = {"NMS", "NYQ", "NGM", "PCX", "ASE", "BTS"}


def _expected_exchanges(ticker):
    for suffix, exchanges in _SUFFIX_EXCHANGE.items():
        if ticker.upper().endswith(suffix):
            return exchanges
    return _US_EXCHANGES


def search_symbol(company_name, expected_exchanges, limit=20):
    """Ask Yahoo's own symbol index which listing carries this company name,
    restricted to the expected exchange.

    This is a LOOKUP, not a guess: the candidate it returns still has to pass
    the same verify_ticker() name check as any hand-typed symbol before
    anything is written. It exists because the alternative is silently losing
    a real company from the universe — 'Sweco AB' with the wrong symbol should
    become SWEC-B.ST, not disappear.

    `limit` is deliberately generous: Yahoo ranks foreign secondary listings
    (Frankfurt, Munich, Pink Sheets) above the home listing for several
    Swedish names, so a short result list drops the one line that matters."""
    import urllib.parse
    from fetch_market_data import CHART_UA
    url = ("https://query1.finance.yahoo.com/v1/finance/search?"
           + urllib.parse.urlencode({"q": company_name, "quotesCount": limit,
                                     "newsCount": 0}))
    try:
        req = urllib.request.Request(url, headers=CHART_UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode())
    except Exception:
        return []
    hits = []
    for q in data.get("quotes", []):
        sym, exch = q.get("symbol"), q.get("exchange")
        if not sym or exch not in expected_exchanges:
            continue
        if q.get("quoteType") not in (None, "EQUITY"):
            continue
        hits.append((sym, q.get("shortname") or q.get("longname") or ""))
    return hits


def _search_queries(ticker, claimed_name):
    """Query variants to try, in order. Nasdaq Stockholm names its share
    classes "Elekta AB ser. B", and Yahoo's index matches on that string —
    a plain "Elekta AB" search returns Frankfurt and Pink Sheet lines and no
    Stockholm one at all. Confirmed live, and it is the difference between
    finding EKTA-B.ST and dropping Elekta from the universe."""
    yield claimed_name
    upper = ticker.upper()
    for cls in ("A", "B", "C"):
        if f"-{cls}." in upper or upper.endswith(f"-{cls}"):
            yield f"{claimed_name} ser. {cls}"
            return
    # No class in the claimed symbol: try both common Stockholm lines anyway.
    if upper.endswith(".ST"):
        yield f"{claimed_name} ser. B"
        yield f"{claimed_name} ser. A"


def resolve_by_name(ticker, claimed_name, max_candidates=6):
    """Last resort for a row whose symbol does not check out: find the real
    listing by company name, then verify it properly. Returns
    (symbol, info) or (None, None) — never an unverified suggestion."""
    if not claimed_name:
        return None, None
    exchanges = _expected_exchanges(ticker)
    tried = set()
    for query in _search_queries(ticker, claimed_name):
        for sym, _hit_name in search_symbol(query, exchanges)[:max_candidates]:
            if sym in tried:
                continue
            tried.add(sym)
            status, info = verify_ticker(sym, claimed_name)
            if status == "ok":
                return sym, info
    return None, None


def verify_many(rows, workers=8):
    """Verify [(ticker, claimed_name), ...] concurrently. Returns
    {ticker: (status, info)}."""
    from concurrent.futures import ThreadPoolExecutor
    from fetch_market_data import _yahoo_session
    _yahoo_session._ensure_init()      # mint the crumb once, not once per worker
    out = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(verify_ticker, t, n): t for t, n in rows}
        for fut, t in futures.items():
            out[t] = fut.result()
    return out


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


def universe_import(csv_path, workers=8, dry_run=False, path=None,
                    ticker_col="ticker", name_col="company name", resolve=True):
    """Bulk-add hand-collected tickers (a CSV of ticker,name) to the universe's
    manual block, verifying every row against Yahoo first.

    Nothing is written unless the ticker both resolves AND is the company the
    CSV says it is. Every row lands in exactly one bucket:
      added         — verified; Yahoo's own name is what gets stored
      already       — verified, already in the universe (metadata refreshed)
      corrected     — the CSV's symbol was wrong, but the company was found by
                      name on the expected exchange and re-verified. Written
                      under the corrected symbol, and always reported.
      name_mismatch — resolves, but to a DIFFERENT company, and no correct
                      listing could be found by name. Never written.
      unresolved    — no such listing, by symbol or by name. Never written.
    Returns that classification so a caller can report it. This is the boundary
    where a hallucinated or stale ticker gets stopped; downstream code assumes
    everything in the universe is real."""
    path = path or UNIVERSE_PATH
    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = {(h or "").strip().lower(): h for h in (reader.fieldnames or [])}
        tcol = headers.get(ticker_col) or (reader.fieldnames or [None])[0]
        ncol = headers.get(name_col)
        for row in reader:
            ticker = (row.get(tcol) or "").strip()
            if not ticker:
                continue
            rows.append((ticker, (row.get(ncol) or "").strip() if ncol else ""))

    seen, deduped = set(), []
    for t, n in rows:
        if t not in seen:
            seen.add(t)
            deduped.append((t, n))

    results = verify_many(deduped, workers=workers)
    with open(path) as f:
        uni = json.load(f)

    report = {"added": [], "already": [], "name_mismatch": [], "unresolved": [],
              "corrected": [],
              "duplicates_in_csv": len(rows) - len(deduped), "total_rows": len(rows)}
    for ticker, claimed in deduped:
        status, info = results[ticker]
        original = ticker
        if status in ("unresolved", "name_mismatch") and resolve:
            # The symbol is wrong; is the COMPANY real and listed? Look it up
            # by name and re-verify. A found symbol still has to pass the same
            # checks — this recovers real companies without ever guessing one.
            found, found_info = resolve_by_name(ticker, claimed)
            if found:
                report["corrected"].append((original, found, found_info.get("long_name"),
                                            status))
                ticker, info, status = found, found_info, "ok"
        if status == "unresolved":
            report["unresolved"].append((ticker, claimed, info.get("error", "")))
            continue
        if status == "name_mismatch":
            report["name_mismatch"].append((ticker, claimed, info.get("long_name")))
            continue
        bucket = "already" if ticker in uni["tickers"] else "added"
        report[bucket].append((ticker, info.get("long_name"), info.get("name_check")))
        rec = uni["tickers"].get(ticker, {})
        rec.update({
            # Yahoo's name, not the CSV's — the CSV is the thing being checked.
            "name": info.get("long_name") or rec.get("name"),
            "sector": rec.get("sector"),
            "region": rec.get("region") or "Nordic",
            "cik": rec.get("cik"),
            "asset_class": rec.get("asset_class", "equity"),
            "source": "manual",
            "verified": {"utc": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                         "exchange": info.get("exchange"),
                         "currency": info.get("currency"),
                         "quote_type": info.get("quote_type")},
        })
        uni["tickers"][ticker] = rec

    if not dry_run:
        uni["tickers"] = dict(sorted(uni["tickers"].items()))
        manual = sum(1 for r in uni["tickers"].values() if r.get("source") == "manual")
        uni["counts"] = {"total": len(uni["tickers"]), "manual": manual,
                         "auto": len(uni["tickers"]) - manual}
        with open(path, "w") as f:
            json.dump(uni, f, indent=2)
    report["universe_total"] = len(uni["tickers"])
    return report


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
            w.writerow({c: r.get(c) for c in HISTORY_COLUMNS if c != "run_utc"}
                       | {"run_utc": run_utc})
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

def _verify_or_exit(ticker, claimed_name):
    """Verify before any single-ticker write, and refuse loudly otherwise.
    Returns the name to store — always Yahoo's, so a stale or mistyped name in
    the command line never becomes the recorded one."""
    status, info = verify_ticker(ticker, claimed_name)
    if status == "unresolved":
        sys.exit(f"{ticker} does not resolve to a real listing "
                 f"({info.get('error')}) — not written. Verify the exchange "
                 f"suffix on Avanza/Nasdaq; do not guess it.")
    if status == "name_mismatch":
        sys.exit(f"{ticker} is a real listing, but it is "
                 f"{info.get('long_name')!r}, not {claimed_name!r} — not written. "
                 f"A resolving ticker is not a correct ticker. Fix one or the "
                 f"other, or pass --no-verify if you are certain.")
    print(f"verified {ticker}: {info.get('long_name')!r} on {info.get('exchange')} "
          f"@ {info.get('price')} {info.get('currency') or ''}".rstrip())
    return info.get("long_name") or claimed_name


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

    ui = sub.add_parser("universe-import",
                        help="bulk-add a CSV of ticker,name to the universe, verified")
    ui.add_argument("csv_path")
    ui.add_argument("--workers", type=int, default=8)
    ui.add_argument("--dry-run", action="store_true")
    ui.add_argument("--no-resolve", action="store_true",
                    help="do not look a failed symbol up by company name")

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
            args.name = _verify_or_exit(args.ticker, args.name)
        new = add(args.ticker, args.name, args.category, args.source, args.note)
        print(f"{'Added' if new else 'Updated'} {args.ticker} in {WATCHLIST_PATH}")
    elif args.cmd == "remove":
        print(f"{'Removed' if remove(args.ticker, args.reason) else 'Not present:'} {args.ticker}")
    elif args.cmd == "universe-add":
        if not args.no_verify:
            args.name = _verify_or_exit(args.ticker, args.name)
        new = universe_add(args.ticker, args.name, args.sector, args.region, args.asset_class)
        print(f"{'Added' if new else 'Updated'} {args.ticker} in {UNIVERSE_PATH} (manual block)")
    elif args.cmd == "universe-import":
        rep = universe_import(args.csv_path, workers=args.workers,
                              dry_run=args.dry_run, resolve=not args.no_resolve)
        print(f"Rows in CSV: {rep['total_rows']} "
              f"({rep['duplicates_in_csv']} duplicate ticker(s) collapsed)\n")
        print(f"  ADDED          {len(rep['added']):>4}")
        print(f"  ...of which symbol-corrected: {len(rep['corrected'])}")
        print(f"  ALREADY PRESENT{len(rep['already']):>4}")
        print(f"  NAME MISMATCH  {len(rep['name_mismatch']):>4}   <- resolves to a DIFFERENT company; not written")
        print(f"  UNRESOLVED     {len(rep['unresolved']):>4}   <- no such listing; not written")
        if rep["corrected"]:
            print("\nSYMBOL CORRECTED — the CSV's ticker was wrong; the company was found "
                  "by name on the expected exchange and re-verified:")
            for old_t, new_t, actual, why in sorted(rep["corrected"]):
                print(f"  {old_t:<16} -> {new_t:<16} {actual!r} ({why})")
        if rep["name_mismatch"]:
            print("\nNAME MISMATCH — the ticker is real but is not this company. "
                  "Fix the ticker or the name at the source; nothing was written.")
            for t, claimed, actual in sorted(rep["name_mismatch"]):
                print(f"  {t:<16} csv says {claimed!r:<42} Yahoo says {actual!r}")
        if rep["unresolved"]:
            gone = [r for r in rep["unresolved"] if "no longer trading" in r[2]]
            unknown = [r for r in rep["unresolved"] if "no longer trading" not in r[2]]
            if gone:
                print("\nNO LONGER TRADING — delisted, acquired or taken private. "
                      "Correctly excluded; nothing to fix.")
                for t, claimed, _e in sorted(gone):
                    print(f"  {t:<16} {claimed!r}")
            if unknown:
                print("\nUNRESOLVED — no listing found by symbol or by company name. "
                      "Verify on Avanza/Nasdaq; do not guess a suffix.")
                for t, claimed, err in sorted(unknown):
                    print(f"  {t:<16} {claimed!r:<42} {err[:44]}")
        near = [r for r in rep["added"] + rep["already"] if r[2] == "near"]
        if near:
            print("\nNAME CORRECTED (close enough to accept, stored under Yahoo's name):")
            for t, actual, _ in sorted(near):
                print(f"  {t:<16} -> {actual!r}")
        print(f"\nUniverse now {rep['universe_total']} tickers"
              f"{' (dry run — nothing written)' if args.dry_run else ''}")

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
