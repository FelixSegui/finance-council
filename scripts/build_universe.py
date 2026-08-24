#!/usr/bin/env python3
"""
Build the BROAD INVESTABLE UNIVERSE — the wide mouth of the discovery funnel.

The universe is the pool the system is allowed to discover companies from. It
is deliberately much bigger than anything the user would ever look at by hand
(hundreds to low thousands of names), and it does NOT need to already satisfy
any investment threshold. Narrowing is `scripts/scout.py`'s job.

Three things the universe is NOT:
  - it is not the portfolio (`data/portfolio.json`),
  - it is not the watchlist (`data/watchlist.json` — curated, small, persistent),
  - it is not a recommendation list.

Sources (free, no key, reachable through this environment's proxy):
  - sp500   : datasets/s-and-p-500-companies constituents CSV. Carries name,
              GICS sector and CIK.
  - nasdaq  : datasets/nasdaq-listings symbol file (opt-in, --wide). Noisy —
              ETFs/test issues are dropped, but it is a listing file, not a
              curated index.
  - nyse    : datasets/nyse-other-listings (opt-in, --wide). Same caveat.
  - manual  : every ticker already in data/universe.json tagged source
              "manual" is PRESERVED verbatim. Nordic/European listings have no
              free constituent feed this network can reach, so they stay
              user-maintained. Add them with `scripts/watchlist.py universe-add`.

Never hand-types a ticker from model memory — that is the hallucination this
system exists to prevent. If a fetch fails, the existing universe.json is left
untouched and the script exits non-zero.

Usage:
  python scripts/build_universe.py                 # sp500 + manual (~560 names)
  python scripts/build_universe.py --wide          # + NASDAQ/NYSE common stock
  python scripts/build_universe.py --dry-run
"""
import argparse
import csv
import io
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from config.settings import UNIVERSE_REFRESH_INTERVAL_DAYS, HTTP_USER_AGENT  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNIVERSE_PATH = os.path.join(ROOT, "data", "universe.json")

SOURCES = {
    "sp500": "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv",
    "nasdaq": "https://raw.githubusercontent.com/datasets/nasdaq-listings/main/data/nasdaq-listed-symbols.csv",
    "nyse": "https://raw.githubusercontent.com/datasets/nyse-other-listings/master/data/nyse-listed.csv",
}

# Suffixes/markers that mean "not an ordinary share" in the raw listing files:
# warrants, units, rights, preferreds, notes. Screening these is meaningless.
NON_COMMON_MARKERS = (
    " warrant", " right", " unit", " preferred", " depositary", " note",
    " debenture", "%", " trust preferred",
)


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": HTTP_USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode()


def fetch_sp500():
    rows = list(csv.DictReader(io.StringIO(_get(SOURCES["sp500"]))))
    if len(rows) < 400:
        raise RuntimeError(f"sp500 CSV returned only {len(rows)} rows — refusing to trust it")
    out = {}
    for r in rows:
        sym = (r.get("Symbol") or "").strip()
        if not sym:
            continue
        cik = (r.get("CIK") or "").strip()
        out[sym] = {
            "name": (r.get("Security") or "").strip() or None,
            "sector": (r.get("GICS Sector") or "").strip() or None,
            "region": "US",
            "cik": cik.zfill(10) if cik.isdigit() else None,
            "source": "sp500",
        }
    return out


def _listing_rows(url, symbol_key, name_key):
    out = {}
    for r in csv.DictReader(io.StringIO(_get(url))):
        sym = (r.get(symbol_key) or "").strip()
        name = (r.get(name_key) or "").strip()
        if not sym or not name:
            continue
        if (r.get("ETF") or "").strip().upper() == "Y":
            continue
        if (r.get("Test Issue") or "").strip().upper() == "Y":
            continue
        low = name.lower()
        if any(m in low for m in NON_COMMON_MARKERS):
            continue
        if any(ch in sym for ch in ".$^"):  # class/unit/warrant share lines
            continue
        out[sym] = {"name": name, "sector": None, "region": "US", "cik": None,
                    "source": "listing"}
    return out


def fetch_wide():
    wide = {}
    wide.update(_listing_rows(SOURCES["nasdaq"], "Symbol", "Company Name"))
    wide.update(_listing_rows(SOURCES["nyse"], "ACT Symbol", "Company Name"))
    if len(wide) < 1000:
        raise RuntimeError(f"listing files returned only {len(wide)} usable rows — refusing to trust them")
    return wide


def load_existing():
    if os.path.exists(UNIVERSE_PATH):
        with open(UNIVERSE_PATH) as f:
            return json.load(f)
    return {}


def manual_entries(existing):
    """Every ticker the user (or a scout promotion) put here by hand. These are
    preserved verbatim on every refresh — they come from sources this network
    cannot fetch (Nordic/European listings), so losing them silently would
    quietly shrink the discoverable universe back to US-only."""
    return {t: rec for t, rec in (existing.get("tickers") or {}).items()
            if (rec or {}).get("source") == "manual"}


def build(wide=False, existing=None):
    existing = existing if existing is not None else load_existing()
    manual = manual_entries(existing)
    sources = []

    auto = fetch_sp500()
    sources.append({"id": "sp500", "url": SOURCES["sp500"], "count": len(auto),
                    "fetched_utc": datetime.now(timezone.utc).isoformat()})
    if wide:
        listing = fetch_wide()
        # sp500 metadata (sector, CIK) is better — never let a listing row
        # overwrite it.
        for sym, rec in listing.items():
            auto.setdefault(sym, rec)
        sources.append({"id": "listings", "url": f"{SOURCES['nasdaq']} + {SOURCES['nyse']}",
                        "count": len(listing),
                        "fetched_utc": datetime.now(timezone.utc).isoformat()})

    tickers = dict(auto)
    tickers.update(manual)  # manual always wins — it is the curated metadata
    return {
        "note": ("BROAD INVESTABLE UNIVERSE — the discovery pool, not a watchlist and not "
                 "holdings. Auto-generated blocks are refreshed by scripts/build_universe.py; "
                 "entries with source 'manual' are user-maintained and preserved verbatim "
                 "(add via `python scripts/watchlist.py universe-add`). Membership implies "
                 "nothing about quality — narrowing is scripts/scout.py's job."),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "refresh_interval_days": UNIVERSE_REFRESH_INTERVAL_DAYS,
        "counts": {"total": len(tickers), "manual": len(manual),
                   "auto": len(tickers) - len(manual)},
        "sources": sources,
        "tickers": dict(sorted(tickers.items())),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--wide", action="store_true",
                   help="also pull NASDAQ/NYSE common-stock listings (~2-4k more names)")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    existing = load_existing()
    try:
        result = build(wide=args.wide, existing=existing)
    except Exception as e:
        sys.exit(f"universe fetch failed ({e}); {UNIVERSE_PATH} left unchanged.")

    old = set((existing.get("tickers") or {}))
    new = set(result["tickers"])
    print(f"Universe: {len(new)} tickers "
          f"({result['counts']['auto']} auto, {result['counts']['manual']} manual) "
          f"(+{len(new - old)} / -{len(old - new)} vs previous)")
    if args.dry_run:
        print("dry-run — not writing.")
        return
    with open(UNIVERSE_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote {UNIVERSE_PATH}")


if __name__ == "__main__":
    main()
