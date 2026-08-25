#!/usr/bin/env python3
"""
THE DISCOVERY FUNNEL. Turns a broad universe into a candidate set the Council
can actually reason over, using code — not LLM reasoning — for the wide part.

    data/universe.json            ~500-2,000 names
              |  cheap deterministic ranking, five independent lenses
              v
    lens shortlists               ~50-75 plausible candidates
              |  + every current holding, + every watchlist name
              v
    data/screens/<ts>-candidates.csv    the Council's candidate set
              |  hard numeric screen, PASS / MISSING / FAIL labels only
              v
    SCOUT HEALTH block            was this run trustworthy?

Three rules this file exists to enforce:

1. **Screening is triage, never investment judgement.** A FAIL label is
   context for the Council, not a deletion. Nothing is removed from the
   candidate set by a threshold.
2. **No single universal score.** Five lenses (quality / value / growth /
   defensive / contrarian) each promote their own top names, so a company
   that one lens's generic thresholds would reject can still reach the
   Council through another. High-growth names being killed by a static
   trailing-P/E rule is the specific failure this design prevents.
3. **"Found nothing" must be distinguishable from "the search broke".**
   Zero passing names triggers diagnose_zero_pass() and a status of
   INVESTIGATE_ZERO_PASS — never a quiet "no interesting stocks".

Usage:
  python scripts/scout.py                       # normal weekly sweep
  python scripts/scout.py --refresh             # ignore the fundamentals cache
  python scripts/scout.py --promote             # add new top names to the watchlist
  python scripts/scout.py --limit 60            # quick run over part of the universe
  python scripts/scout.py --max-pe 25 --min-profit-margin 0.08
"""
import argparse
import csv
import json
import os
import statistics
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import watchlist as wl  # noqa: E402
from fetch_market_data import fetch_equities  # noqa: E402
from config.settings import (  # noqa: E402
    UNIVERSE_CACHE_DAYS, UNIVERSE_FETCH_WORKERS, UNIVERSE_REFRESH_INTERVAL_DAYS,
    LENS_TOP_N, CANDIDATE_POOL_SOFT_CAP, FACTOR_WINSOR_PCT, LENS_MIN_FIELDS,
    MISSING_DATA_RATE_ALERT, FETCH_FAILURE_RATE_ALERT, SINGLE_FILTER_KILL_RATE,
    PERCENT_POINT_SCALE_FIELDS, DEFAULT_SCREEN, FOCUS_TOP_N, LENS_MAX_PER_SECTOR,
    THIN_LENS_COVERAGE, METRIC_SANITY_RANGES,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNIVERSE_PATH = os.path.join(ROOT, "data", "universe.json")
PORTFOLIO_PATH = os.path.join(ROOT, "data", "portfolio.json")
SCREENS_DIR = os.path.join(ROOT, "data", "screens")
FUND_CACHE_PATH = os.path.join(ROOT, "data", "cache", "universe_fundamentals.json")

# Lens rankings need real fundamentals. ETFs (Yahoo reports no meaningful
# P/E or margin for them), crypto proxies and the gold tracker are carried
# through the funnel when held or watchlisted, but never ranked against
# operating companies — that comparison is meaningless, not merely noisy.
NON_RANKABLE_ASSET_CLASSES = {"etf", "crypto", "commodity"}

# (cli flag, snapshot field, direction) — "max" passes when value <= threshold.
FILTERS = [
    ("max_pe", "trailing_pe", "max"),
    ("max_forward_pe", "forward_pe", "max"),
    ("max_peg", "peg_ratio", "max"),
    ("min_revenue_growth", "revenue_growth", "min"),
    ("min_profit_margin", "profit_margins", "min"),
    ("max_debt_to_equity", "debt_to_equity", "max"),
    ("min_dividend_yield", "dividend_yield", "min"),
    ("min_market_cap", "market_cap", "min"),
    ("max_beta", "beta", "max"),
]

# Each lens: metric -> direction. "low" means smaller is better (inverted
# before averaging), so a lens score is always "higher = more attractive
# through this lens". Weights are deliberately absent: an equal-weighted
# average of z-scores is honest about how little precision free data supports.
LENSES = {
    "quality":    {"roic": "high", "roe": "high", "profit_margin": "high",
                   "operating_margin": "high", "net_debt_to_ebitda": "low"},
    "value":      {"earnings_yield": "high", "forward_earnings_yield": "high",
                   "fcf_yield": "high", "price_to_book": "low", "price_to_sales": "low"},
    "growth":     {"revenue_growth": "high", "revenue_cagr_3y": "high",
                   "peg": "low", "pe_compression": "high"},
    "defensive":  {"beta": "low", "debt_to_equity": "low", "net_debt_to_ebitda": "low",
                   "profit_margin": "high", "dividend_yield": "high"},
    "contrarian": {"pct_of_52w_range": "low", "earnings_yield": "high",
                   "price_to_book": "low", "profit_margin": "high"},
}


# ---------------------------------------------------------------------------
# inputs
# ---------------------------------------------------------------------------

def load_universe(path=None):
    """Returns (tickers_map, warnings). A missing or suspiciously small
    universe is a warning, never a silent empty run."""
    path = path or UNIVERSE_PATH
    warnings = []
    if not os.path.exists(path):
        return {}, [f"universe file {path} does not exist — run "
                    f"`python scripts/build_universe.py`"]
    with open(path) as f:
        uni = json.load(f)
    tickers = uni.get("tickers") or {}
    if not tickers:
        warnings.append(f"universe file {path} has no tickers")
    elif len(tickers) < 100:
        warnings.append(f"universe is only {len(tickers)} names — that is a watchlist, "
                        f"not a discovery universe; re-run scripts/build_universe.py")
    gen = uni.get("generated_utc")
    if gen:
        try:
            age = (datetime.now(timezone.utc) - datetime.fromisoformat(gen)).days
            limit = uni.get("refresh_interval_days", UNIVERSE_REFRESH_INTERVAL_DAYS)
            if age > limit:
                warnings.append(f"universe is {age} days old (refresh interval {limit}) — "
                                f"run `python scripts/build_universe.py` for a discovery refresh")
        except ValueError:
            warnings.append(f"universe generated_utc unparseable: {gen!r}")
    return tickers, warnings


def load_holdings(path=None):
    """Tickers with a live buy/sell decision. Cash, unlisted funds (TBD) and
    frozen/unsellable positions have no decision to make and are excluded."""
    path = path or PORTFOLIO_PATH
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        port = json.load(f)
    out = {}
    for h in port.get("holdings", []):
        t = h.get("ticker")
        if not t or t == "TBD" or t.startswith("CASH_"):
            continue
        name = h.get("name") or ""
        if "FROZEN" in name.upper() or "SOLD" in name.upper():
            continue
        if t == "ethereum":
            continue  # CoinGecko id, priced by fetch_market_data --crypto
        out[t] = {"name": name, "quantity": h.get("quantity"),
                  "exposure_class": h.get("exposure_class")}
    return out


# ---------------------------------------------------------------------------
# fetching (cached, concurrent)
# ---------------------------------------------------------------------------

def load_cache(path=None):
    path = path or FUND_CACHE_PATH
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_cache(cache, path=None):
    path = path or FUND_CACHE_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(cache, f)


def gather(universe_tickers, always_fresh, cache, cache_days, refresh, workers,
           quiet=False):
    """Fetch fundamentals for the whole universe, reusing cached records that
    are younger than cache_days. `always_fresh` (holdings + watchlist) is
    refetched every run — those names drive live decisions.

    Returns (records, stats)."""
    now = datetime.now(timezone.utc)
    to_fetch, from_cache = [], {}
    for t in universe_tickers:
        if refresh or t in always_fresh:
            to_fetch.append(t)
            continue
        entry = cache.get(t)
        if not entry:
            to_fetch.append(t)
            continue
        try:
            age = (now - datetime.fromisoformat(entry["fetched_utc"])).days
        except (KeyError, ValueError):
            to_fetch.append(t)
            continue
        if age < cache_days:
            from_cache[t] = entry["record"]
        else:
            to_fetch.append(t)

    if not quiet:
        print(f"  {len(from_cache)} from cache, fetching {len(to_fetch)}...",
              file=sys.stderr)

    fetched = {}
    if to_fetch:
        def progress(done, total, _t):
            if not quiet and (done % 50 == 0 or done == total):
                print(f"    fetched {done}/{total}", file=sys.stderr)
        fetched = fetch_equities(to_fetch, workers=workers, progress=progress)
        stamp = now.isoformat()
        for t, rec in fetched.items():
            if "error" not in rec:
                cache[t] = {"fetched_utc": stamp, "record": rec}

    records = dict(from_cache)
    records.update(fetched)
    failures = {t: r.get("error") for t, r in records.items() if "error" in r}
    stats = {
        "requested": len(universe_tickers),
        "from_cache": len(from_cache),
        "newly_fetched": len(to_fetch),
        "fetch_failed": len(failures),
        "fetched_ok": len(records) - len(failures),
    }
    return records, stats, failures


# ---------------------------------------------------------------------------
# metrics + mechanical ranking
# ---------------------------------------------------------------------------

def _num(x):
    """Unwrap derived_metrics' {"value":..., "quality_state":...} shape and
    reject anything that isn't a finite number."""
    if isinstance(x, dict):
        x = x.get("value")
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    if x != x or x in (float("inf"), float("-inf")):
        return None
    return float(x)


def metrics(rec):
    """Every quantitative field the lenses rank on, derived from ONE fetched
    record. Anything not derivable is None — never imputed, never zero-filled."""
    g = lambda k: _num(rec.get(k))  # noqa: E731
    pe, fpe = g("trailing_pe"), g("forward_pe")
    mcap, fcf = g("market_cap"), g("free_cashflow")
    debt, cash, ebitda = g("total_debt"), g("total_cash"), g("ebitda")
    hi, lo, px = g("52w_high"), g("52w_low"), g("price")

    # A ratio that divides a statement figure by a market figure is only
    # meaningful when both are in the same currency (see
    # fetch_market_data._fetch_fundamentals_direct). For a cross-listed name
    # they are not, and no FX rate exists here to reconcile them, so the
    # honest value is None — which lowers the name's lens coverage and
    # therefore its conviction, rather than handing a lens a number that is
    # wrong by an exchange rate.
    mixed_ccy = bool(rec.get("currency_mismatch"))

    m = {
        "price": px,
        "market_cap": mcap,
        "earnings_yield": (1.0 / pe) if pe and pe > 0 else None,
        "forward_earnings_yield": (1.0 / fpe) if fpe and fpe > 0 else None,
        "fcf_yield": None if mixed_ccy else ((fcf / mcap) if (fcf is not None and mcap) else None),
        "price_to_book": g("price_to_book"),
        "price_to_sales": g("price_to_sales"),
        "peg": g("peg_ratio"),
        "roe": g("return_on_equity"),
        "roic": None if mixed_ccy else g("roic_pct"),
        "profit_margin": g("profit_margins"),
        "operating_margin": g("operating_margins"),
        "revenue_growth": g("revenue_growth"),
        "debt_to_equity": g("debt_to_equity"),
        "dividend_yield": g("dividend_yield"),
        "beta": g("beta"),
        "net_debt_to_ebitda": ((debt - cash) / ebitda)
                              if (debt is not None and cash is not None and ebitda) else None,
        # A forward multiple below the trailing one means the market expects
        # earnings to grow into the price — the single growth signal this
        # system can compute without analyst-revision data.
        "pe_compression": ((pe - fpe) / pe) if (pe and fpe and pe > 0) else None,
        "pct_of_52w_range": ((px - lo) / (hi - lo))
                            if (px is not None and hi is not None and lo is not None and hi > lo) else None,
    }

    hist = rec.get("revenue_history_last_n_fiscal_years") or []
    revs = [_num(h.get("total_revenue")) for h in hist]
    revs = [r for r in revs if r and r > 0]
    if len(revs) >= 3:
        newest, oldest = revs[0], revs[-1]      # Yahoo returns newest first
        years = len(revs) - 1
        m["revenue_cagr_3y"] = (newest / oldest) ** (1.0 / years) - 1.0
    else:
        m["revenue_cagr_3y"] = None
    return m


def zscores(values, winsor=FACTOR_WINSOR_PCT):
    """ticker -> z, computed only over non-null values and winsorized first.

    Without winsorizing, one bad-data extreme (a multi-class share-count
    mismatch producing an absurd earnings yield) inflates the stdev until
    every other name collapses toward zero and the factor stops
    discriminating at all."""
    pts = {t: v for t, v in values.items() if v is not None}
    if len(pts) < 3:
        return {t: None for t in values}
    sv = sorted(pts.values())
    n = len(sv)
    lo = sv[max(0, int(winsor * n))]
    hi = sv[min(n - 1, int((1 - winsor) * n))]
    clamp = lambda v: min(hi, max(lo, v))  # noqa: E731
    clamped = [clamp(v) for v in pts.values()]
    mean = statistics.fmean(clamped)
    sd = statistics.pstdev(clamped)
    if sd == 0:
        return {t: None for t in values}
    return {t: (max(-3.0, min(3.0, (clamp(v) - mean) / sd)) if v is not None else None)
            for t, v in values.items()}


def rank_lenses(metric_rows, lenses=LENSES, min_fields=LENS_MIN_FIELDS):
    """Cross-sectional z-score per metric, then one score per lens per name.

    Returns (scores, coverage, field_coverage):
      scores[ticker][lens]         float or None
      coverage[lens]               how many names earned a score
      field_coverage[ticker][lens] (fields_present, fields_in_lens)

    A name is scored on a lens only if at least `min_fields` of that lens's
    metrics are present — a "quality score" derived from one number is not a
    quality score.

    **Thin scores are shrunk toward neutral, and this matters more than it
    looks.** Averaging fewer z-scores produces a NOISIER average, not a more
    cautious one: the mean of k independent z-scores has standard deviation
    1/sqrt(k), so a name missing half a lens's inputs lands further out in the
    tails than a fully-covered one — and a top-N shortlist is precisely a cut
    on the tails. Measured on the 2026-08-24 universe before this correction,
    growth scores built on partial data averaged |1.048| against |0.396| for
    full-coverage names, 2.6x more extreme, and Swedish names (whose PEG and
    forward-P/E coverage is ~28 points below US names') took 6 of 10 slots on
    both the defensive and contrarian lenses against an expected 1.7. Missing
    data was buying shortlist slots.

    Multiplying by sqrt(k/K) rescales a k-field mean back onto the full-
    coverage scale, so extremity reflects evidence rather than the absence of
    it. Nothing is imputed and no name is excluded — a thin score is simply
    not allowed to claim more conviction than its inputs support, and the name
    still reaches the Council with its coverage stated. (The fields inside a
    lens are correlated, so 1/sqrt(k) understates the true variance somewhat;
    this is a deliberate under-correction, not an exact one.)"""
    fields = sorted({f for spec in lenses.values() for f in spec})
    z = {f: zscores({t: row.get(f) for t, row in metric_rows.items()}) for f in fields}

    scores, coverage, field_coverage = {}, {lens: 0 for lens in lenses}, {}
    for t in metric_rows:
        scores[t], field_coverage[t] = {}, {}
        for lens, spec in lenses.items():
            vals = []
            for field, direction in spec.items():
                v = z[field].get(t)
                if v is None:
                    continue
                vals.append(-v if direction == "low" else v)
            k, total = len(vals), len(spec)
            field_coverage[t][lens] = (k, total)
            if k >= min_fields:
                shrink = (k / total) ** 0.5
                scores[t][lens] = round(statistics.fmean(vals) * shrink, 3)
                coverage[lens] += 1
            else:
                scores[t][lens] = None
    return scores, coverage, field_coverage


# Yahoo returns both "Financials" and "Financial Services" for the same kind
# of business, and a sector cap that treats them as different sectors leaks.
SECTOR_ALIASES = {"financials": "Financial Services", "financial services": "Financial Services",
                  "information technology": "Technology", "technology": "Technology",
                  "consumer discretionary": "Consumer Cyclical",
                  "consumer staples": "Consumer Defensive",
                  "health care": "Healthcare", "healthcare": "Healthcare"}


def normalise_sector(sector):
    if not sector:
        return None
    return SECTOR_ALIASES.get(sector.strip().lower(), sector.strip())


def lens_shortlists(scores, top_n=LENS_TOP_N, eligible=None, sectors=None,
                    max_per_sector=LENS_MAX_PER_SECTOR):
    """Top `top_n` names per lens, with no sector allowed to fill more than
    `max_per_sector` slots.

    Deliberately NOT one blended score: a deep-value name and a high-quality
    compounder are both allowed through on their own terms, and a name that
    one lens's worldview rejects can still arrive via another.

    The sector cap exists because that promise was not being kept. Each lens
    ranks on metrics that cluster in one sector — growth metrics in tech,
    price/book in real estate, leverage in banks — so an uncapped top-10 was
    routinely 8/10 one sector. The Council then compares "the whole market"
    while actually looking at one industry. Overflow names are not deleted;
    the slot simply goes to the next-best name from an under-represented
    sector, and everything remains in the full JSON.

    Names with no sector data are never capped away — unknown is not a sector.
    """
    sectors = sectors or {}
    out = {}
    for lens in LENSES:
        ranked = [(t, s[lens]) for t, s in scores.items()
                  if s.get(lens) is not None and (eligible is None or t in eligible)]
        ranked.sort(key=lambda kv: kv[1], reverse=True)
        picked, used, overflow = [], {}, []
        for t, _score in ranked:
            if len(picked) >= top_n:
                break
            sec = normalise_sector(sectors.get(t))
            if sec and used.get(sec, 0) >= max_per_sector:
                overflow.append(t)
                continue
            picked.append(t)
            if sec:
                used[sec] = used.get(sec, 0) + 1
        # If the cap left the shortlist short (a thin lens), backfill from the
        # names it displaced rather than returning fewer candidates.
        for t in overflow:
            if len(picked) >= top_n:
                break
            picked.append(t)
        out[lens] = picked
    return out


def collapse_share_classes(tickers, names, holdings, watch_tickers, market_caps):
    """Nasdaq Stockholm lists most large caps twice (INDU-A / INDU-C,
    ATCO-A / ATCO-B, INVE-A / INVE-B). Two lines of the same company are ONE
    investment decision, and letting both through spends scarce lens slots and
    Council attention on a share-class question nobody asked.

    Runs before the lens shortlists, so a duplicate never occupies a slot.

    Collapses only when the ticker stem AND the company name agree — two
    different companies must never merge. Survivor priority is strict:
      1. a current holding   (it has a live hold/sell decision; collapsing it
                              into a line the user does not own would silently
                              drop that decision)
      2. a watchlist name    (already curated)
      3. the larger market cap (the more liquid line, usually the B share)
    Returns {dropped_ticker: surviving_ticker}; the caller records the
    survivors' siblings so the alternative class is never hidden.
    """
    import re
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from watchlist import _normalise_name

    groups = {}
    for t in tickers:
        stem = re.sub(r"-(A|B|C|SDB)(\.[A-Z]+)?$", r"\2", t)
        if stem != t:                       # only tickers that carry a class
            groups.setdefault(stem, []).append(t)

    def priority(t):
        return (0 if t in holdings else 1 if t in watch_tickers else 2,
                -(market_caps.get(t) or 0))

    dropped = {}
    for members in groups.values():
        if len(members) < 2:
            continue
        tokens = {t: _normalise_name(names.get(t) or "")[0] for t in members}
        base = members[0]
        same = [t for t in members
                if t == base or (tokens[t] and tokens[base] and tokens[t] & tokens[base])]
        if len(same) < 2:
            continue
        keep = min(same, key=priority)
        for t in same:
            if t != keep:
                dropped[t] = keep
    return dropped


# ---------------------------------------------------------------------------
# hard screen
# ---------------------------------------------------------------------------

def validate_thresholds(active):
    """S19 guard. Yahoo reports some fields on a percentage-POINT scale; a
    decimal-scale threshold silently rejects everything and looks exactly like
    a quiet market. Hard error, not a warning — an automated run must fail
    loudly rather than produce an empty candidate pool that reads as
    'nothing good out there'."""
    problems = []
    for _cli, field, _direction, threshold in active:
        guard = PERCENT_POINT_SCALE_FIELDS.get(field)
        if guard and threshold < guard[0]:
            problems.append(f"--{_cli.replace('_', '-')} {threshold}: {guard[1]}")
    return problems


def apply_filters(records, active):
    """PASS / MISSING / FAIL per name. Nothing is dropped — the label travels
    with the candidate into the Council's candidate set."""
    status, detail = {}, {}
    for ticker, fields in records.items():
        if "error" in fields:
            status[ticker] = "MISSING"
            detail[ticker] = {"reason": fields["error"]}
            continue
        fail, missing = [], []
        for _cli, field, direction, threshold in active:
            value = _num(fields.get(field))
            if value is None:
                missing.append(field)
            elif direction == "max" and value > threshold:
                fail.append(f"{field}={round(value, 3)} > {threshold}")
            elif direction == "min" and value < threshold:
                fail.append(f"{field}={round(value, 3)} < {threshold}")
        if fail:
            status[ticker] = "FAIL"
            detail[ticker] = {"reasons": fail}
        elif missing:
            status[ticker] = "MISSING"
            detail[ticker] = {"missing_fields": missing}
        else:
            status[ticker] = "PASS"
            detail[ticker] = {}
    return status, detail


def diagnose_zero_pass(health, records, active, universe_warnings, failures):
    """Cheap diagnostic run when nothing passes. A zero-result is only a valid
    investment conclusion once the pipeline itself is shown to be healthy."""
    findings = []
    if universe_warnings:
        findings += [f"universe: {w}" for w in universe_warnings]
    if health["screened"] == 0:
        findings.append("nothing was screened at all — the candidate set was empty "
                        "before any threshold was applied")
    fetched = health["fetched"] + health["fetch_failed"]
    if fetched and health["fetch_failed"] / fetched > FETCH_FAILURE_RATE_ALERT:
        findings.append(f"{health['fetch_failed']}/{fetched} fetches failed "
                        f"(>{int(FETCH_FAILURE_RATE_ALERT*100)}%) — sample error: "
                        f"{next(iter(failures.values()), 'n/a')}")
    if health["screened"] and health["missing"] / health["screened"] > MISSING_DATA_RATE_ALERT:
        findings.append(f"{health['missing']}/{health['screened']} candidates were missing a "
                        f"filtered field — the data path, not the market, may be the problem")

    # Which single filter is doing the killing? A threshold that alone rejects
    # nearly everything is far more likely a units/scale mistake than a market.
    for cli, field, direction, threshold in active:
        rejected = 0
        comparable = 0
        for fields in records.values():
            v = _num(fields.get(field))
            if v is None:
                continue
            comparable += 1
            if (direction == "max" and v > threshold) or (direction == "min" and v < threshold):
                rejected += 1
        if comparable and rejected / comparable >= SINGLE_FILTER_KILL_RATE:
            guard = PERCENT_POINT_SCALE_FIELDS.get(field)
            scale = f" {guard[1]}" if guard else ""
            findings.append(f"--{cli.replace('_', '-')} {threshold} alone rejects "
                            f"{rejected}/{comparable} names with data — check the "
                            f"threshold's units/scale before believing the result.{scale}")
    if not findings:
        findings.append("pipeline looks healthy: the universe loaded, fetching succeeded, "
                        "missing-data rate is normal and no single filter dominates. "
                        "A genuine zero-pass on these thresholds is the honest reading.")
    return findings


# ---------------------------------------------------------------------------
# outputs
# ---------------------------------------------------------------------------

DIGEST_COLUMNS = [
    "ticker", "source", "focus", "rank", "best_lens", "screen_status", "name", "sector",
    "country", "currency", "price", "pe", "fwd_pe", "peg", "margin_pct",
    "op_margin_pct", "roe_pct", "roic_pct", "de_ratio", "net_debt_to_ebitda",
    "rev_growth_pct", "rev_cagr3y_pct", "fcf_yield_pct", "div_yield_pct",
    "mcap_b", "beta", "pct_52w_range",
    "z_quality", "z_value", "z_growth", "z_defensive", "z_contrarian",
    "thin_lenses", "suspect", "note",
]


def _pct(x, nd=1):
    return round(x * 100, nd) if isinstance(x, (int, float)) else None


def sanity_flags(metric_row, ranges=None):
    """Which of a name's metrics fall outside a plausible range for their field.

    Flags, never fixes. A holding company's 1198% "revenue growth" is Yahoo
    counting investment gains as revenue — real data, wrong meaning. Naming it
    lets a voice discount it; deleting it would hide a data problem, and
    correcting it would be inventing a number."""
    ranges = ranges or METRIC_SANITY_RANGES
    out = []
    for field, (lo, hi) in ranges.items():
        v = metric_row.get(field)
        if isinstance(v, (int, float)) and not (lo <= v <= hi):
            out.append(f"{field}={round(v, 4)}")
    return out


def drop_implausible(metric_rows, ranges=None):
    """Return (metrics_for_ranking, flags_by_ticker).

    An implausible value is withheld from the lens z-scores. It is not
    evidence, so it must not earn a name a shortlist slot — and because the
    lens score is already shrunk in proportion to coverage, removing it
    automatically lowers that name's conviction rather than silently
    substituting something."""
    ranges = ranges or METRIC_SANITY_RANGES
    cleaned, flags = {}, {}
    for t, row in metric_rows.items():
        bad = sanity_flags(row, ranges)
        flags[t] = bad
        if not bad:
            cleaned[t] = row
            continue
        bad_fields = {b.split("=")[0] for b in bad}
        cleaned[t] = {k: (None if k in bad_fields else v) for k, v in row.items()}
    return cleaned, flags


def digest_rows(candidates, records, met, scores, status, detail, universe):
    rows = []
    for t, cand in candidates.items():
        rec = records.get(t, {})
        m = met.get(t, {})
        s = scores.get(t, {})
        note = ""
        d = detail.get(t) or {}
        if d.get("reasons"):
            note = "; ".join(d["reasons"])[:140]
        elif d.get("missing_fields"):
            note = "missing: " + ",".join(d["missing_fields"])[:120]
        elif d.get("reason"):
            note = str(d["reason"])[:140]
        rows.append({
            "ticker": t,
            "source": cand["source"],
            "focus": "Y" if cand.get("focus") else "",
            "rank": cand.get("rank"),
            "best_lens": cand.get("best_lens"),
            "screen_status": status.get(t, "MISSING"),
            "name": cand.get("name") or (universe.get(t) or {}).get("name") or "",
            "sector": rec.get("sector") or (universe.get(t) or {}).get("sector") or "",
            "country": rec.get("country") or "",
            "currency": rec.get("currency") or "",
            "price": m.get("price"),
            "pe": _num(rec.get("trailing_pe")),
            "fwd_pe": _num(rec.get("forward_pe")),
            "peg": m.get("peg"),
            "margin_pct": _pct(m.get("profit_margin")),
            "op_margin_pct": _pct(m.get("operating_margin")),
            "roe_pct": _pct(m.get("roe")),
            "roic_pct": _pct(m.get("roic")),
            "de_ratio": m.get("debt_to_equity"),
            "net_debt_to_ebitda": round(m["net_debt_to_ebitda"], 2)
                                  if m.get("net_debt_to_ebitda") is not None else None,
            "rev_growth_pct": _pct(m.get("revenue_growth")),
            "rev_cagr3y_pct": _pct(m.get("revenue_cagr_3y")),
            "fcf_yield_pct": _pct(m.get("fcf_yield"), 2),
            "div_yield_pct": _pct(m.get("dividend_yield"), 2),
            "mcap_b": round(m["market_cap"] / 1e9, 2) if m.get("market_cap") else None,
            "beta": m.get("beta"),
            "pct_52w_range": _pct(m.get("pct_of_52w_range"), 0),
            "z_quality": s.get("quality"),
            "z_value": s.get("value"),
            "z_growth": s.get("growth"),
            "z_defensive": s.get("defensive"),
            "z_contrarian": s.get("contrarian"),
            "thin_lenses": "; ".join(cand.get("thin_lenses") or []),
            "suspect": "; ".join(cand.get("suspect") or []),
            "note": note,
        })
    order = {"holding": 0, "watchlist": 1, "new": 2}
    rows.sort(key=lambda r: (0 if r["focus"] else 1,
                             order.get(r["source"], 3),
                             r["rank"] if r["rank"] is not None else 10**6,
                             r["ticker"]))
    return rows


def write_outputs(rows, result, out_dir=None, stamp=None):
    out_dir = out_dir or SCREENS_DIR
    os.makedirs(out_dir, exist_ok=True)
    stamp = stamp or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    csv_path = os.path.join(out_dir, f"{stamp}-candidates.csv")
    json_path = os.path.join(out_dir, f"{stamp}-scout.json")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=DIGEST_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    with open(json_path, "w") as f:
        json.dump(result, f, indent=2)
    return csv_path, json_path


def format_health(health):
    return "\n".join([
        "SCOUT HEALTH",
        "",
        f"  Universe:   {health['universe']}",
        f"  Fetched:    {health['fetched']}   (cache {health['from_cache']}, "
        f"new {health['newly_fetched']}, failed {health['fetch_failed']})",
        f"  Ranked:     {health['ranked']}    (names that earned >=1 lens score)",
        f"  Candidates: {health['candidates']}  "
        f"(holdings {health['holdings']}, watchlist {health['watchlist']}, new {health['new']})",
        f"  Focus:      {health['focus']}   (full Council analysis; the rest stay "
        f"available as context)",
        f"  Screened:   {health['screened']}",
        f"  Passed:     {health['passed']}",
        f"  Missing:    {health['missing']}",
        f"  Failed:     {health['failed']}",
        "",
        f"  Status: {health['status']}",
    ])


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def run(args):
    universe, universe_warnings = load_universe()
    holdings = load_holdings()
    watch = wl.load()
    watch_tickers = set(watch["entries"])

    for w in universe_warnings:
        if not args.quiet:
            print(f"  ! {w}", file=sys.stderr)

    # --limit takes an alphabetical slice for quick runs. Report the slice
    # actually used as the universe count — a health block saying 539 after a
    # 60-name run would misrepresent how wide the search really was.
    universe_used = sorted(universe)
    if args.limit:
        universe_used = universe_used[:args.limit]
        universe_warnings.append(
            f"--limit {args.limit}: only {len(universe_used)} of {len(universe)} "
            f"universe names were considered (alphabetical slice) — this is a "
            f"quick run, not a full discovery sweep")

    # Holdings and watchlist names are candidates whether or not they are in
    # the universe file — a sweep that cannot see what you own is broken.
    pool = set(universe_used) | set(holdings) | watch_tickers
    always_fresh = set(holdings) | watch_tickers

    if not args.quiet:
        print(f"Universe {len(universe_used)} | holdings {len(holdings)} | "
              f"watchlist {len(watch_tickers)} | to fetch {len(pool)}", file=sys.stderr)

    cache = load_cache()
    records, fetch_stats, failures = gather(
        sorted(pool), always_fresh, cache, args.cache_days, args.refresh,
        args.workers, quiet=args.quiet)
    save_cache(cache)

    met = {t: metrics(r) for t, r in records.items() if "error" not in r}

    # One company, one decision — before anything is ranked, so a duplicate
    # share class never occupies a lens slot or a Council seat.
    ticker_names = {t: ((universe.get(t) or {}).get("name")
                        or (holdings.get(t) or {}).get("name")
                        or ((watch["entries"].get(t) or {}).get("name")))
                    for t in set(records) | set(holdings) | watch_tickers}
    class_dupes = collapse_share_classes(
        set(records) | set(holdings) | watch_tickers, ticker_names,
        set(holdings), watch_tickers,
        {t: (met.get(t) or {}).get("market_cap") for t in met})
    siblings = {}
    for dropped_t, keeper in class_dupes.items():
        siblings.setdefault(keeper, []).append(dropped_t)

    met_for_ranking, suspect_flags = drop_implausible(met)
    rankable = {t for t in met
                if t not in class_dupes
                and (universe.get(t) or {}).get("asset_class", "equity")
                not in NON_RANKABLE_ASSET_CLASSES}
    scores, lens_coverage, field_coverage = rank_lenses(met_for_ranking)
    sectors = {t: (records[t].get("sector") or (universe.get(t) or {}).get("sector"))
               for t in met}
    shortlists = lens_shortlists(scores, args.lens_top_n, eligible=rankable,
                                 sectors=sectors, max_per_sector=args.max_per_sector)

    discovered = sorted({t for names in shortlists.values() for t in names})

    # ---- the candidate set: holdings + watchlist + newly discovered --------
    candidates = {}
    for t in sorted((set(holdings) | watch_tickers | set(discovered)) - set(class_dupes)):
        uni_name = (universe.get(t) or {}).get("name")
        if t in holdings:
            source = "holding"
            name = holdings[t].get("name") or uni_name
        elif t in watch_tickers:
            source = "watchlist"
            # Watchlist entries are often added as a bare ticker. The universe
            # carries Yahoo's verified name — use it rather than handing the
            # Council a blank name column for a third of its candidates.
            name = (watch["entries"][t] or {}).get("name") or uni_name
        else:
            source, name = "new", uni_name
        s = scores.get(t, {})
        best = max(((lens, v) for lens, v in s.items() if v is not None),
                   key=lambda kv: kv[1], default=(None, None))
        thin = [f"{ln} {k}/{n}" for ln, (k, n) in (field_coverage.get(t) or {}).items()
                if n and k and k / n < THIN_LENS_COVERAGE]
        flags = list(suspect_flags.get(t) or [])
        if (records.get(t) or {}).get("currency_mismatch"):
            flags.append(f"reports in {(records.get(t) or {}).get('financial_currency')}, "
                         f"priced in {(records.get(t) or {}).get('currency')} — FCF yield and "
                         f"ROIC not computable")
        candidates[t] = {"source": source, "name": name,
                         "best_lens": best[0], "lens_score": best[1],
                         "thin_lenses": thin,
                         "suspect": flags,
                         "share_class_siblings": sorted(siblings.get(t, [])),
                         "in_lens_shortlists": [ln for ln, names in shortlists.items()
                                                if t in names]}
    # Rank the candidate set by its best lens score (a relative ordering for
    # the history file, NOT a conviction score and NOT a return forecast).
    ordered = sorted([t for t in candidates if candidates[t]["lens_score"] is not None],
                     key=lambda t: candidates[t]["lens_score"], reverse=True)
    for i, t in enumerate(ordered, 1):
        candidates[t]["rank"] = i

    # ---- limited refinement: where should the Council spend its depth? -----
    # The pool stays broad (that is the point of five lenses); `focus` marks
    # the ~10-20 names worth full analysis. Every holding is in focus because
    # every holding has a live hold/sell decision. Nothing outside focus is
    # excluded — a voice can pull any name back in and argue for it.
    focus = set(holdings) | set(ordered[:args.focus_top_n])
    for t, c in candidates.items():
        c["focus"] = t in focus

    active = []
    for cli, field, direction in FILTERS:
        threshold = getattr(args, cli, None)
        if threshold is None:
            threshold = DEFAULT_SCREEN.get(cli)
        if threshold is not None:
            active.append((cli, field, direction, float(threshold)))
    problems = validate_thresholds(active)
    if problems:
        sys.exit("Refusing to run — threshold scale looks wrong:\n  " + "\n  ".join(problems))

    cand_records = {t: records.get(t, {"error": "not fetched"}) for t in candidates}
    status, detail = apply_filters(cand_records, active)

    counts = {"PASS": 0, "MISSING": 0, "FAIL": 0}
    for st in status.values():
        counts[st] += 1
    health = {
        "universe": len(universe_used),
        "from_cache": fetch_stats["from_cache"],
        "newly_fetched": fetch_stats["newly_fetched"],
        "fetch_failed": fetch_stats["fetch_failed"],
        "fetched": fetch_stats["fetched_ok"],
        "ranked": sum(1 for t in scores if any(v is not None for v in scores[t].values())),
        "candidates": len(candidates),
        "holdings": sum(1 for c in candidates.values() if c["source"] == "holding"),
        "watchlist": sum(1 for c in candidates.values() if c["source"] == "watchlist"),
        "new": sum(1 for c in candidates.values() if c["source"] == "new"),
        "focus": sum(1 for c in candidates.values() if c.get("focus")),
        "share_class_collapsed": len(class_dupes),
        "screened": len(status),
        "passed": counts["PASS"],
        "missing": counts["MISSING"],
        "failed": counts["FAIL"],
    }

    diagnostics = []
    if health["passed"] == 0:
        health["status"] = "INVESTIGATE_ZERO_PASS"
        diagnostics = diagnose_zero_pass(health, cand_records, active,
                                         universe_warnings, failures)
    elif universe_warnings or health["fetch_failed"] / max(1, len(pool)) > FETCH_FAILURE_RATE_ALERT:
        health["status"] = "DEGRADED"
        diagnostics = [f"universe: {w}" for w in universe_warnings]
        if health["fetch_failed"] / max(1, len(pool)) > FETCH_FAILURE_RATE_ALERT:
            diagnostics.append(f"{health['fetch_failed']} fetch failures out of {len(pool)}")
    else:
        health["status"] = "VALID"
    if health["candidates"] > CANDIDATE_POOL_SOFT_CAP:
        diagnostics.append(f"candidate set is {health['candidates']} names "
                           f"(soft cap {CANDIDATE_POOL_SOFT_CAP}) — lower --lens-top-n "
                           f"if the Council run gets expensive")

    rows = digest_rows(candidates, records, met, scores, status, detail, universe)
    suspect_rows = [r for r in rows if r["suspect"]]
    health["suspect_values"] = len(suspect_rows)
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "health": health,
        "diagnostics": diagnostics,
        "filters": [f"{c} {d} {t}" for c, _f, d, t in active],
        "lens_definitions": LENSES,
        "lens_coverage": lens_coverage,
        "lens_shortlists": shortlists,
        "share_class_collapsed": {k: v for k, v in class_dupes.items()},
        "universe_warnings": universe_warnings,
        "fetch_failures": failures,
        "candidates": {t: dict(candidates[t], screen_status=status.get(t),
                               screen_detail=detail.get(t)) for t in candidates},
        "method": ("Five independent lens rankings (cross-sectional z-scores, winsorized, "
                   "equal-weighted within a lens). A lens score is a RELATIVE ordering "
                   "within this run's universe — not a valuation, not a forecast, and not "
                   "a buy signal. The hard screen labels candidates PASS/MISSING/FAIL and "
                   "removes nothing."),
    }

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    csv_path, json_path = write_outputs(rows, result, stamp=stamp)

    hist_rows = []
    for t, c in candidates.items():
        z = scores.get(t, {})
        hist_rows.append({
            "ticker": t, "source": c["source"], "rank": c.get("rank"),
            "best_lens": c.get("best_lens"), "lens_score": c.get("lens_score"),
            "screen_status": status.get(t),
            # Price at ranking time — the only thing that makes a past rank
            # measurable against what actually happened afterwards.
            "price": (met.get(t) or {}).get("price"),
            "currency": (records.get(t) or {}).get("currency"),
            "z_quality": z.get("quality"), "z_value": z.get("value"),
            "z_growth": z.get("growth"), "z_defensive": z.get("defensive"),
            "z_contrarian": z.get("contrarian"),
        })
    wl.append_history(hist_rows)

    promoted = []
    if args.promote:
        for t in ordered[:args.promote_top]:
            if candidates[t]["source"] == "new":
                wl.add(t, name=candidates[t].get("name"),
                       category=f"scout:{candidates[t]['best_lens']}", source="scout",
                       note=f"promoted {datetime.now(timezone.utc).strftime('%Y-%m-%d')} — "
                            f"ranked #{candidates[t]['rank']} on the {candidates[t]['best_lens']} lens")
                promoted.append(t)

    # ---- report -----------------------------------------------------------
    if args.quiet:
        print(f"{csv_path}  [{health['status']}] "
              f"{health['candidates']} candidates "
              f"({health['passed']} passed / {health['missing']} missing / "
              f"{health['failed']} failed)")
        return result

    print()
    print(format_health(health))
    if suspect_rows:
        print("\nIMPLAUSIBLE VALUES (flagged, not corrected — a lens may be ranking "
              "on an artefact):")
        for r in suspect_rows:
            print(f"  {r['ticker']:<12} {r['suspect']}")
    if class_dupes:
        print("\nSHARE CLASSES COLLAPSED (one company, one decision): "
              + ", ".join(f"{k}->{v}" for k, v in sorted(class_dupes.items())))
    if diagnostics:
        print("\nDIAGNOSTICS")
        for d in diagnostics:
            print(f"  - {d}")
    print("\nLENS SHORTLISTS (each lens promotes its own top names)")
    for lens, names in shortlists.items():
        print(f"  {lens:<11} scored {lens_coverage[lens]:>4}  ->  {', '.join(names) or '(none)'}")
    focus_names = [t for t in ordered if candidates[t]["focus"]]
    focus_names += [t for t in sorted(candidates)
                    if candidates[t]["focus"] and t not in focus_names]
    print(f"\nFOCUS ({health['focus']} names — full Council analysis): "
          f"{', '.join(focus_names)}")
    print(f"\nNEW CANDIDATES (not held, not previously on the watchlist): "
          f"{', '.join(t for t in ordered if candidates[t]['source'] == 'new') or '(none)'}")
    if promoted:
        print(f"Promoted to the watchlist: {', '.join(promoted)}")
    print(f"\nWrote {csv_path}")
    print(f"Wrote {json_path}  (full detail; read the CSV first)")
    print(f"Appended {len(hist_rows)} rows to {wl.HISTORY_PATH}")

    table = wl.history_table()
    if table:
        print("\nRANK HISTORY (persistence is evidence, never an automatic BUY)")
        print(f"  {'TICKER':<12}{'RANK':>6}{'PREV':>6}{'TOP10':>7}{'RUNS':>6}")
        for row in table[:15]:
            print(f"  {row['ticker']:<12}{str(row['current_rank']):>6}"
                  f"{str(row['previous_rank']):>6}{row['times_top_n']:>7}{row['runs_seen']:>6}")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--cache-days", type=int, default=UNIVERSE_CACHE_DAYS)
    p.add_argument("--refresh", action="store_true", help="ignore the fundamentals cache")
    p.add_argument("--workers", type=int, default=UNIVERSE_FETCH_WORKERS)
    p.add_argument("--lens-top-n", type=int, default=LENS_TOP_N,
                   help="names each lens promotes into the candidate pool")
    p.add_argument("--focus-top-n", type=int, default=FOCUS_TOP_N,
                   help="how many top-ranked candidates to mark for full Council analysis")
    p.add_argument("--max-per-sector", type=int, default=LENS_MAX_PER_SECTOR,
                   help="cap on how many shortlist slots one sector may fill per lens")
    p.add_argument("--limit", type=int, default=None,
                   help="cap the universe slice (quick runs; holdings/watchlist always included)")
    p.add_argument("--promote", action="store_true",
                   help="add the best newly discovered names to the curated watchlist")
    p.add_argument("--promote-top", type=int, default=10)
    p.add_argument("--quiet", action="store_true",
                   help="suppress the report; print one summary line and the output path")
    for cli, _field, _direction in FILTERS:
        p.add_argument(f"--{cli.replace('_', '-')}", type=float, default=None)
    args = p.parse_args()
    run(args)


if __name__ == "__main__":
    main()
