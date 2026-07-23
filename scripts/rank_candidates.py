#!/usr/bin/env python3
"""
Coarse factor ranker — stage 1 of the two-stage selection funnel.

The funnel:
  stage 1  rank_candidates.py   ~500 names -> ranked shortlist (~30)   [THIS FILE]
  stage 2  screen_candidates.py  shortlist -> hard pass/fail survivors
  stage 3  valuation + thesis-review  survivors -> the 1-2 you act on

What it does: for a universe (default the auto-built S&P 500), it pulls
fundamentals (SEC EDGAR) and price/momentum (Yahoo chart) via
fetch_fundamentals.py, computes CROSS-SECTIONAL z-scores per factor (each name
scored relative to its peers, which is what "find the best relative value /
quality / momentum" actually means), and combines them into one composite
score. It RANKS; it does not pick — the top names are candidates for the hard
screen and human valuation, nothing more.

Honesty rules carried over from the rest of the system:
  - Every number traces to a fetched response. Missing factors are reported as
    missing and EXCLUDED from that name's composite — never imputed to zero,
    never guessed. Coverage is reported so you can see what the rank rests on.
  - A rank is a relative ordering, NOT a buy signal and NOT a predicted return.
    Selection is lever #4 (smallest edge); this widens and disciplines the
    field, it does not manufacture alpha.
  - Names without fundamentals (no CIK — non-US, ETFs) can't be value/quality
    ranked; they are set aside in `partial_data`, not force-ranked on momentum.

Caching: fetched factor data is cached to data/universe_cache/ for --cache-days
(default 7) so a rank run is fast and doesn't re-hit 500 endpoints each session.
Use --refresh to force a re-fetch.

Usage:
  python scripts/rank_candidates.py                         # rank the sp500
  python scripts/rank_candidates.py --categories sp500 --top 30
  python scripts/rank_candidates.py --limit 25 --refresh    # quick fresh run
  python scripts/rank_candidates.py --weights 2,1,1,1       # tilt toward value
"""
import argparse
import json
import os
import statistics
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_fundamentals import fetch_one  # noqa: E402

UNIVERSE_PATH = "data/universe.json"
CACHE_PATH = "data/universe_cache/factors.json"

# factor -> (record field, direction). "high" = bigger is better.
FACTOR_FIELDS = {
    "value":    [("earnings_yield", "high")],
    "quality":  [("profit_margin", "high"), ("roe", "high"), ("debt_to_equity", "low")],
    "growth":   [("revenue_growth", "high")],
    "momentum": [("momentum_12m", "high"), ("pct_of_52w_high", "high")],
}
# A name needs at least these categories present to earn a composite rank.
REQUIRED_CATEGORIES = {"value", "quality"}


def load_universe(categories):
    with open(UNIVERSE_PATH) as f:
        uni = json.load(f)
    cats = uni.get("categories", {})
    meta = uni.get("metadata", {})
    if categories == ["all"]:
        selected = list(cats)
    else:
        unknown = [c for c in categories if c not in cats]
        if unknown:
            sys.exit(f"Unknown categories {unknown}. Available: {sorted(cats)}")
        selected = categories
    tickers = []
    for c in selected:
        tickers.extend(cats[c])
    return sorted(set(tickers)), meta


def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH) as f:
            return json.load(f)
    return {}


def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)


def gather(tickers, meta, cache, cache_days, refresh):
    """Return {ticker: record}, using cache where fresh."""
    now = datetime.now(timezone.utc)
    records = {}
    for i, t in enumerate(tickers, 1):
        entry = cache.get(t)
        fresh = False
        if entry and not refresh:
            try:
                age = (now - datetime.fromisoformat(entry["fetched_utc"])).days
                fresh = age < cache_days
            except (KeyError, ValueError):
                fresh = False
        if fresh:
            records[t] = entry["record"]
            continue
        cik = (meta.get(t) or {}).get("cik")
        print(f"  [{i}/{len(tickers)}] fetching {t}...", file=sys.stderr)
        rec = fetch_one(t, cik)
        cache[t] = {"fetched_utc": now.isoformat(), "record": rec}
        records[t] = rec
    return records


def zscores(values, winsor=0.02):
    """Map ticker->raw to ticker->z (clipped to +/-3), over non-null values.

    Values are WINSORIZED to the [winsor, 1-winsor] percentile range before the
    mean/stdev are computed and before each point is standardized. Without this,
    a single bad-data extreme — e.g. BRK.B's garbage earnings yield from a
    multi-class share-count mismatch — inflates the stdev so much that every
    other name collapses to ~0, and the factor stops discriminating. Winsorizing
    makes the ranker robust to those outliers instead of hostage to them."""
    pts = {t: v for t, v in values.items() if v is not None}
    if len(pts) < 2:
        return {t: None for t in values}
    sv = sorted(pts.values())
    n = len(sv)
    lo = sv[max(0, int(winsor * n))]
    hi = sv[min(n - 1, int((1 - winsor) * n))]

    def clamp(v):
        return min(hi, max(lo, v))

    clamped = [clamp(v) for v in pts.values()]
    mean = statistics.fmean(clamped)
    sd = statistics.pstdev(clamped)
    out = {}
    for t in values:
        v = values[t]
        if v is None or sd == 0:
            out[t] = None
        else:
            z = (clamp(v) - mean) / sd
            out[t] = max(-3.0, min(3.0, z))
    return out


def category_scores(records):
    """ticker -> {category: z or None}, z-scored cross-sectionally per sub-factor."""
    # z-score every sub-factor across the universe first
    subz = {}
    for cat, fields in FACTOR_FIELDS.items():
        for field, direction in fields:
            raw = {t: (records[t].get(field)) for t in records}
            z = zscores(raw)
            if direction == "low":  # invert so "better" is always positive
                z = {t: (-v if v is not None else None) for t, v in z.items()}
            subz[(cat, field)] = z
    # average sub-factor z-scores within each category (over what's present)
    cat_scores = {}
    for t in records:
        cat_scores[t] = {}
        for cat, fields in FACTOR_FIELDS.items():
            zs = [subz[(cat, f)][t] for f, _ in fields if subz[(cat, f)][t] is not None]
            cat_scores[t][cat] = statistics.fmean(zs) if zs else None
    return cat_scores


def composite(cat_score, weights):
    present = {c: s for c, s in cat_score.items() if s is not None}
    if not REQUIRED_CATEGORIES.issubset(present):
        return None, sorted(present)
    wsum = sum(weights[c] for c in present)
    if wsum == 0:
        return None, sorted(present)
    score = sum(weights[c] * present[c] for c in present) / wsum
    return score, sorted(present)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--categories", default="sp500")
    p.add_argument("--limit", type=int, default=None, help="cap universe size (quick runs)")
    p.add_argument("--top", type=int, default=30, help="how many ranked names to write/print")
    p.add_argument("--weights", default="1,1,1,1",
                   help="value,quality,growth,momentum weights")
    p.add_argument("--cache-days", type=int, default=7)
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--exclude-sectors", default="",
                   help="comma-separated GICS sectors to drop (sustainability "
                        "negative screen), e.g. 'Energy,Tobacco'")
    args = p.parse_args()

    try:
        wv = [float(x) for x in args.weights.split(",")]
        weights = dict(zip(["value", "quality", "growth", "momentum"], wv))
    except ValueError:
        sys.exit("--weights must be four numbers, e.g. 1,1,1,1")

    tickers, meta = load_universe([c.strip() for c in args.categories.split(",")])
    excluded_sectors = {s.strip() for s in args.exclude_sectors.split(",") if s.strip()}
    excluded = []
    if excluded_sectors:
        kept = []
        for t in tickers:
            if (meta.get(t) or {}).get("sector") in excluded_sectors:
                excluded.append(t)
            else:
                kept.append(t)
        tickers = kept
        print(f"Excluded {len(excluded)} names in sectors {sorted(excluded_sectors)} "
              "(note: names without GICS sector metadata, e.g. non-US, can't be "
              "sector-excluded)", file=sys.stderr)
    if args.limit:
        tickers = tickers[:args.limit]
    print(f"Universe: {len(tickers)} tickers from [{args.categories}]", file=sys.stderr)

    cache = load_cache()
    records = gather(tickers, meta, cache, args.cache_days, args.refresh)
    save_cache(cache)

    cat_scores = category_scores(records)

    ranked, momentum_only, partial = [], [], []
    for t in records:
        score, present = composite(cat_scores[t], weights)
        row = {
            "ticker": t,
            "name": (meta.get(t) or {}).get("name"),
            "sector": (meta.get(t) or {}).get("sector"),
            "currency": (meta.get(t) or {}).get("currency"),
            "composite": round(score, 3) if score is not None else None,
            "z": {c: (round(v, 2) if v is not None else None)
                  for c, v in cat_scores[t].items()},
            "coverage": present,
            "raw": {k: records[t].get(k) for k in
                    ["pe", "earnings_yield", "profit_margin", "roe", "debt_to_equity",
                     "revenue_growth", "momentum_12m", "pct_of_52w_high", "price"]},
        }
        if score is not None:
            ranked.append(row)
        elif cat_scores[t].get("momentum") is not None:
            # No fundamentals (typically non-US: SEC is US-only, Yahoo fundamentals
            # blocked) but a real price history exists — rank on momentum ALONE,
            # in its own list. Momentum is the weakest single factor, so this is a
            # research watchlist, NOT a factor-vetted shortlist. Never merged into
            # the main composite ranking.
            row["reason"] = "no fundamentals — momentum-only (weak signal, research manually)"
            momentum_only.append(row)
        else:
            row["reason"] = f"insufficient data (have {present or 'nothing'})"
            partial.append(row)
    ranked.sort(key=lambda r: r["composite"], reverse=True)
    momentum_only.sort(key=lambda r: r["z"].get("momentum") or -9, reverse=True)

    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "universe_categories": args.categories,
        "universe_size": len(tickers),
        "weights": weights,
        "method": ("cross-sectional z-scores per factor, clipped +/-3, "
                   "equal-weighted within category, weighted across categories; "
                   "relative ranking only, NOT a return forecast"),
        "excluded_sectors": sorted(excluded_sectors),
        "excluded_tickers": excluded,
        "coverage": {
            "ranked": len(ranked),
            "momentum_only": len(momentum_only),
            "partial_data": len(partial),
        },
        "ranking": ranked[:args.top],
        "momentum_only_ranking": momentum_only[:args.top],
        "partial_data": partial,
    }
    os.makedirs("data/rankings", exist_ok=True)
    fname = f"data/rankings/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-ranking.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nWrote {fname}")
    print(f"Ranked {len(ranked)} (full factors); {len(momentum_only)} momentum-only "
          f"(no fundamentals); {len(partial)} set aside.\n")
    print(f"{'#':>3}  {'TICKER':<8}{'COMPOSITE':>10}  {'VAL':>5}{'QUAL':>6}{'GRW':>6}{'MOM':>6}  SECTOR")
    def f(x): return f"{x:>5.2f}" if x is not None else "    ."
    for i, r in enumerate(ranked[:args.top], 1):
        z = r["z"]
        print(f"{i:>3}  {r['ticker']:<8}{r['composite']:>10.3f}  "
              f"{f(z['value'])}{f(z['quality'])}{f(z['growth'])}{f(z['momentum'])}  {r['sector'] or ''}")
    if momentum_only:
        print(f"\nMomentum-only (no fundamentals — research watchlist, NOT factor-vetted):")
        print(f"{'#':>3}  {'TICKER':<12}{'MOM z':>7}  {'12m%':>8}  CURRENCY")
        for i, r in enumerate(momentum_only[:args.top], 1):
            m12 = r["raw"].get("momentum_12m")
            print(f"{i:>3}  {r['ticker']:<12}{f(r['z'].get('momentum')):>7}  "
                  f"{(m12*100 if m12 is not None else 0):>7.1f}  {r.get('currency') or ''}")


if __name__ == "__main__":
    main()
