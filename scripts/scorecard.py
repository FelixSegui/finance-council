#!/usr/bin/env python3
"""
SYSTEM SCORECARD — is this system actually getting better at deciding?

Six pillars, each answering a question that can be wrong in a way the memos
would never reveal:

  1. DISCOVERY    Is the funnel still finding things it has not seen before?
  2. DATA         Is the evidence sound, and is it EVEN across markets?
  3. MECHANICAL   Do the lens rankings predict anything?
  4. JUDGEMENT    Do the seven voices beat the mechanics they were handed?
  5. DECISION     Does stated conviction mean anything, and does the human act?
  6. OUTCOME      Is the real portfolio beating just buying the index?

THE ANTI-FLATTERY RULE, enforced in code, not by good intentions
-----------------------------------------------------------------
Every skill number is reported as EXCESS versus a stated baseline, never as a
raw return — a raw return mostly measures the market, and in a rising market
every pillar would look brilliant while proving nothing.

And below MIN_OBSERVATIONS in a bucket, this script prints "insufficient
evidence (n=k)" and NO number at all. This is the whole point. At roughly one
sweep a week with a handful of picks, a hit rate computed on six observations
is noise that reads like skill, and a system that quotes it will be trusted
for the wrong reason. The refusal is the feature; do not lower the threshold
to make the report look fuller.

Benchmark returns are monthly-granularity (see backtest.py's fetcher), so a
pick held under ~30 days has a coarse comparison. Reported, not hidden.

Usage:
  python scripts/scorecard.py                    # print the scorecard
  python scripts/scorecard.py --write            # also write reports/system-scorecard.md
  python scripts/scorecard.py --pillar judgement
"""
import argparse
import csv
import glob
import json
import os
import statistics
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENS_DIR = os.path.join(ROOT, "data", "screens")
HISTORY_PATH = os.path.join(ROOT, "data", "candidate_history.csv")
LEDGER_PATH = os.path.join(ROOT, "data", "decisions.csv")
VALUATIONS_PATH = os.path.join(ROOT, "data", "valuations.csv")
PORTFOLIO_PATH = os.path.join(ROOT, "data", "portfolio.json")
OUT_PATH = os.path.join(ROOT, "reports", "system-scorecard.md")

# Below this many observations in a bucket, report the count and refuse the
# number. Raising the report's apparent richness by lowering this is the exact
# self-deception this file exists to prevent.
MIN_OBSERVATIONS = 20
# A market-coverage gap wider than this on a field two lenses rank on is a
# structural tilt, not noise (this is how the forward-P/E asymmetry was found).
COVERAGE_GAP_ALERT_PP = 15


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _f(x):
    try:
        v = float(x)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def _read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def _latest(pattern):
    files = sorted(glob.glob(os.path.join(SCREENS_DIR, pattern)))
    return files[-1] if files else None


def _pct(x, nd=1):
    return f"{x * 100:+.{nd}f}%" if x is not None else "n/a"


def evidence(values, label, unit="%"):
    """One line per bucket. Below MIN_OBSERVATIONS, the number is withheld."""
    n = len(values)
    if n == 0:
        return f"{label:<34} no observations yet"
    if n < MIN_OBSERVATIONS:
        return (f"{label:<34} insufficient evidence (n={n}, need {MIN_OBSERVATIONS}) "
                f"— provisional median {_pct(statistics.median(values))}")
    med = statistics.median(values)
    hit = sum(1 for v in values if v > 0) / n
    return f"{label:<34} n={n:<4} median {_pct(med):>8}   beat baseline {hit:.0%}"


# ---------------------------------------------------------------------------
# price fetching (current prices + benchmark series)
# ---------------------------------------------------------------------------

def current_prices(tickers, workers=8):
    from fetch_market_data import fetch_equities
    out = {}
    recs = fetch_equities(sorted(set(tickers)), workers=workers)
    for t, r in recs.items():
        out[t] = _f(r.get("price"))
    return out


def benchmark_series(ticker="VWCE.DE", years_back=3):
    """{(year, month): price} for the benchmark, via the same direct Yahoo
    chart path backtest.py uses. Returns {} if unavailable — every caller
    treats that as "no baseline", never as zero."""
    from backtest import _fetch_monthly_series
    now = datetime.now(timezone.utc)
    p2 = int(now.timestamp())
    p1 = p2 - years_back * 365 * 86400
    try:
        return _fetch_monthly_series(ticker, p1, p2)
    except Exception:
        return {}


def excess_return(entry_price, current_price, decided_date, bench, bench_now):
    """Return of a pick MINUS the benchmark over the same window.

    A raw return would mostly measure the market. Returns None when either
    leg is unavailable — never a zero, which would silently read as
    'performed exactly in line' and pollute every median computed from it."""
    entry, cur = _f(entry_price), _f(current_price)
    if not entry or not cur or entry <= 0:
        return None
    pick = cur / entry - 1.0
    if not bench or bench_now is None:
        return None
    key = (decided_date.year, decided_date.month)
    eligible = [k for k in bench if k <= key]
    if not eligible:
        return None
    b_entry = bench[max(eligible)]
    if not b_entry:
        return None
    return pick - (bench_now / b_entry - 1.0)


# ---------------------------------------------------------------------------
# pillars
# ---------------------------------------------------------------------------

def pillar_discovery():
    out = ["## 1. DISCOVERY — is the funnel finding things it has not seen?", ""]
    scout_json = _latest("*-scout.json")
    if not scout_json:
        return out + ["  No scout run found. Run `python scripts/scout.py`.", ""]
    with open(scout_json) as f:
        res = json.load(f)
    h = res["health"]
    out.append(f"  Latest run: universe {h['universe']}, candidates {h['candidates']} "
               f"({h['holdings']} held / {h['watchlist']} watchlist / {h['new']} new), "
               f"focus {h.get('focus', '?')}, status {h['status']}")

    hist = _read_csv(HISTORY_PATH)
    runs = sorted({r["run_utc"] for r in hist})
    out.append(f"  Runs recorded: {len(runs)}")
    if len(runs) >= 2:
        prev = {r["ticker"] for r in hist if r["run_utc"] == runs[-2]}
        cur = {r["ticker"] for r in hist if r["run_utc"] == runs[-1]}
        churn = len(cur - prev) / max(1, len(cur))
        out.append(f"  Candidate turnover vs previous run: {churn:.0%} new to the set")
    new_counts = []
    for run in runs[-8:]:
        new_counts.append(sum(1 for r in hist if r["run_utc"] == run and r["source"] == "new"))
    if new_counts:
        out.append(f"  New candidates per run (last {len(new_counts)}): "
                   f"{', '.join(str(c) for c in new_counts)}")
        if new_counts[-1] == 0:
            out.append("  ** ZERO new candidates — check scout health before "
                       "believing the market is quiet.")
    return out + [""]


def pillar_data():
    out = ["## 2. DATA — is the evidence sound, and even across markets?", ""]
    cand_csv = _latest("*-candidates.csv")
    scout_json = _latest("*-scout.json")
    if not cand_csv:
        return out + ["  No candidates CSV found.", ""]
    rows = _read_csv(cand_csv)
    if scout_json:
        with open(scout_json) as f:
            res = json.load(f)
        h = res["health"]
        fetched = h["fetched"] + h["fetch_failed"]
        rate = h["fetch_failed"] / fetched if fetched else 0
        out.append(f"  Fetch failures: {h['fetch_failed']}/{fetched} ({rate:.1%})")
        if res.get("universe_warnings"):
            for w in res["universe_warnings"]:
                out.append(f"  ** {w}")

    fields = ["pe", "fwd_pe", "peg", "roic_pct", "de_ratio", "rev_growth_pct",
              "fcf_yield_pct", "div_yield_pct", "beta", "pct_52w_range"]
    markets = {}
    for r in rows:
        markets.setdefault(r.get("country") or "?", []).append(r)
    big = {k: v for k, v in markets.items() if len(v) >= 8}
    out.append("")
    out.append("  Coverage by market (a gap here tilts whole lenses invisibly):")
    header = "    " + "field".ljust(20) + "".join(f"{m[:12]:>14}" for m in big)
    out.append(header)
    worst = []
    for fld in fields:
        cells, rates = [], []
        for m, sub in big.items():
            have = sum(1 for r in sub if r.get(fld)) / len(sub)
            rates.append(have)
            cells.append(f"{have:>13.0%}")
        out.append("    " + fld.ljust(20) + "".join(cells))
        if len(rates) >= 2:
            gap = (max(rates) - min(rates)) * 100
            if gap >= COVERAGE_GAP_ALERT_PP:
                worst.append((gap, fld))
    for gap, fld in sorted(worst, reverse=True):
        out.append(f"  ** {fld}: {gap:.0f}pp spread across markets — any lens ranking "
                   f"on it compares names on unequal evidence.")

    thin = [r for r in rows if r.get("thin_lenses")]
    out.append(f"  Candidates with a thin lens score: {len(thin)}/{len(rows)}")
    return out + [""]


def pillar_mechanical(prices, bench, bench_now):
    out = ["## 3. MECHANICAL — do the lens rankings predict anything?", ""]
    hist = _read_csv(HISTORY_PATH)
    if not hist:
        return out + ["  No candidate history yet.", ""]
    runs = sorted({r["run_utc"] for r in hist})
    if len(runs) < 2:
        return out + [f"  Only {len(runs)} run recorded. This pillar needs history: "
                      "a rank is only testable once time has passed since it was "
                      "assigned. Come back after several sweeps.", ""]

    by_lens = {}
    for r in hist:
        if r["run_utc"] == runs[-1]:
            continue                     # no elapsed time to measure
        lens = r.get("best_lens")
        if not lens:
            continue
        decided = datetime.fromisoformat(r["run_utc"])
        ex = excess_return(r.get("price"), prices.get(r["ticker"]), decided,
                           bench, bench_now)
        if ex is None:
            continue
        rank = _f(r.get("rank"))
        by_lens.setdefault(lens, []).append((rank, ex))

    if not by_lens:
        return out + ["  No measurable observations yet (needs a prior run with "
                      "recorded prices).", ""]
    out.append("  Excess return vs benchmark, by the lens that ranked the name best:")
    for lens in sorted(by_lens):
        vals = [ex for _rank, ex in by_lens[lens]]
        out.append("    " + evidence(vals, lens))
    # Does a better rank actually mean a better outcome?
    allpts = [(rk, ex) for pts in by_lens.values() for rk, ex in pts if rk is not None]
    if len(allpts) >= MIN_OBSERVATIONS:
        allpts.sort(key=lambda p: p[0])
        half = len(allpts) // 2
        top = statistics.median([e for _r, e in allpts[:half]])
        bot = statistics.median([e for _r, e in allpts[half:]])
        out.append("")
        out.append(f"    top-half ranks median {_pct(top)} vs bottom-half {_pct(bot)} "
                   f"— {'ranking adds signal' if top > bot else 'RANKING IS NOT ADDING SIGNAL'}")
    else:
        out.append("")
        out.append(f"    rank-vs-outcome: insufficient evidence (n={len(allpts)}, "
                   f"need {MIN_OBSERVATIONS})")
    return out + [""]


def pillar_judgement(prices, bench, bench_now):
    out = ["## 4. JUDGEMENT — do the voices beat the mechanics they were handed?", ""]
    ledger = _read_csv(LEDGER_PATH)
    if not ledger:
        return out + ["  Decision ledger is empty. `council` records picks with",
                      "  `python scripts/decisions.py record --picks <file>`.",
                      "  Until then this pillar cannot be measured at all — and",
                      "  'we don't know' is the correct answer, not an estimate.", ""]

    buys = [r for r in ledger if r["action"] == "BUY"]
    per_voice = {}
    for r in buys:
        decided = datetime.fromisoformat(r["decided_utc"])
        ex = excess_return(r.get("entry_price"), prices.get(r["ticker"]), decided,
                           bench, bench_now)
        if ex is not None:
            per_voice.setdefault(r["voice"], []).append(ex)

    out.append("  Excess return vs benchmark on BUY calls, per voice:")
    for voice in sorted(per_voice):
        out.append("    " + evidence(per_voice[voice], voice))
    if not per_voice:
        out.append("    no BUY calls with a measurable window yet")

    # The question that decides whether the LLM layer earns its cost.
    chairman = per_voice.get("chairman", [])
    others = [v for k, vals in per_voice.items() if k != "chairman" for v in vals]
    out.append("")
    if len(chairman) >= MIN_OBSERVATIONS and len(others) >= MIN_OBSERVATIONS:
        out.append(f"    Chairman median {_pct(statistics.median(chairman))} vs "
                   f"voices' median {_pct(statistics.median(others))} — "
                   f"{'synthesis adds value' if statistics.median(chairman) > statistics.median(others) else 'SYNTHESIS IS NOT ADDING VALUE over its own inputs'}")
    else:
        out.append(f"    Chairman vs voices: insufficient evidence "
                   f"(chairman n={len(chairman)}, voices n={len(others)}, "
                   f"need {MIN_OBSERVATIONS} each). This is the number that would "
                   f"justify ever weighting the Council — do not weight it before "
                   f"this line reads.")
    return out + [""]


def pillar_decision(prices, bench, bench_now):
    out = ["## 5. DECISION — does conviction mean anything, and does the human act?", ""]
    ledger = _read_csv(LEDGER_PATH)
    if not ledger:
        return out + ["  Decision ledger is empty.", ""]
    chair = [r for r in ledger if r["voice"] == "chairman"]
    by_status = {}
    for r in chair:
        by_status.setdefault(r.get("status") or "open", []).append(r)
    out.append("  Chairman calls by status: "
               + ", ".join(f"{k} {len(v)}" for k, v in sorted(by_status.items())))

    today = datetime.now(timezone.utc).date()
    open_buys = [r for r in chair if r.get("status") == "open" and r["action"] == "BUY"]
    if open_buys:
        ages = [(today - datetime.fromisoformat(r["decided_utc"]).date()).days
                for r in open_buys]
        out.append(f"  Open BUY calls: {len(open_buys)}, median age {statistics.median(ages):.0f} days, "
                   f"oldest {max(ages)} days")
        out.append("  Price drift while unexecuted (what the delay has cost so far):")
        for r in sorted(open_buys, key=lambda r: r["decided_utc"]):
            entry, cur = _f(r.get("entry_price")), prices.get(r["ticker"])
            drift = f"{(cur / entry - 1) * 100:+.1f}%" if (entry and cur) else "n/a"
            age = (today - datetime.fromisoformat(r["decided_utc"]).date()).days
            out.append(f"    {r['ticker']:<12} {age:>4}d  entry {r.get('entry_price') or '?':>10}  "
                       f"now {cur if cur else '?':>10}  {drift:>8}")

    buckets = {"low (1-4)": [], "medium (5-7)": [], "high (8-10)": []}
    for r in chair:
        if r["action"] != "BUY":
            continue
        c = _f(r.get("conviction"))
        decided = datetime.fromisoformat(r["decided_utc"])
        ex = excess_return(r.get("entry_price"), prices.get(r["ticker"]), decided,
                           bench, bench_now)
        if c is None or ex is None:
            continue
        key = "low (1-4)" if c <= 4 else "medium (5-7)" if c <= 7 else "high (8-10)"
        buckets[key].append(ex)
    out.append("")
    out.append("  Calibration — a conviction score that does not sort outcomes is noise:")
    for k, vals in buckets.items():
        out.append("    " + evidence(vals, k))
    return out + [""]


def pillar_outcome(bench_ticker="VWCE.DE"):
    out = ["## 6. OUTCOME — is the real portfolio beating just buying the index?", ""]
    rows = []
    for r in _read_csv(VALUATIONS_PATH):
        try:
            rows.append({
                "date": datetime.strptime(r["date"], "%Y-%m-%d"),
                "value": float(str(r["total_value_sek"]).split()[0].replace(",", "")),
                "contribution": float(str(r["net_contribution_since_last_sek"] or 0)
                                      .split()[0].replace(",", "")),
            })
        except (ValueError, KeyError):
            continue
    if len(rows) < 2:
        return out + [f"  Need at least 2 valuation rows in {VALUATIONS_PATH}; "
                      f"have {len(rows)}.", ""]
    rows.sort(key=lambda r: r["date"])

    from backtest import _fetch_monthly_series
    p2 = int(datetime.now(timezone.utc).timestamp())
    p1 = int(rows[0]["date"].replace(tzinfo=timezone.utc).timestamp()) - 60 * 86400
    bench = _fetch_monthly_series(bench_ticker, p1, p2)
    fx = _fetch_monthly_series("EURSEK=X", p1, p2)
    if not bench or not fx:
        return out + ["  Benchmark or FX history unavailable — refusing to compare "
                      "against an assumed rate.", ""]
    prices = {k: bench[k] * fx[k] for k in set(bench) & set(fx)}
    if not prices:
        return out + ["  No overlapping benchmark/FX months.", ""]

    units, contributed = 0.0, 0.0
    for i, r in enumerate(rows):
        amount = r["value"] if i == 0 else r["contribution"]
        if amount == 0:
            continue
        key = (r["date"].year, r["date"].month)
        eligible = [k for k in prices if k <= key]
        if not eligible:
            continue
        units += amount / prices[max(eligible)]
        contributed += amount
    shadow = units * prices[max(prices)]
    actual = rows[-1]["value"]
    out.append(f"  Period {rows[0]['date'].date()} -> {rows[-1]['date'].date()} "
               f"({len(rows)} observations)")
    out.append(f"  Money in:        {contributed:>12,.0f} SEK")
    out.append(f"  Actual:          {actual:>12,.0f} SEK  ({(actual/contributed-1)*100:+.1f}%)")
    out.append(f"  Same money in {bench_ticker}: {shadow:>9,.0f} SEK  "
               f"({(shadow/contributed-1)*100:+.1f}%)")
    out.append(f"  Difference:      {actual - shadow:>+12,.0f} SEK")
    if len(rows) < 12:
        out.append(f"  ** {len(rows)} observations over "
                   f"{(rows[-1]['date'] - rows[0]['date']).days} days is far too short "
                   f"to read as skill either way.")
    return out + [""]


def pillar_gaps():
    """What is missing — derived from the run, not from anyone's opinion."""
    out = ["## GAPS — what would most improve the next decision", ""]
    cand_csv = _latest("*-candidates.csv")
    if not cand_csv:
        return out + ["  No candidates CSV.", ""]
    rows = _read_csv(cand_csv)
    focus = [r for r in rows if r.get("focus") == "Y"] or rows
    fields = ["pe", "fwd_pe", "peg", "roic_pct", "margin_pct", "de_ratio",
              "net_debt_to_ebitda", "rev_growth_pct", "rev_cagr3y_pct",
              "fcf_yield_pct", "div_yield_pct", "beta", "pct_52w_range"]
    missing = sorted(((sum(1 for r in focus if not r.get(f)), f) for f in fields),
                     reverse=True)
    out.append(f"  Missing metrics across the {len(focus)} focus names "
               f"(these are the names the Council actually reasons over):")
    for n, f in missing[:6]:
        if n:
            who = [r["ticker"] for r in focus if not r.get(f)][:6]
            out.append(f"    {f:<20} missing on {n:>2}  ({', '.join(who)})")
    if not any(n for n, _f in missing):
        out.append("    none — every focus name has every tracked metric")

    ledger = _read_csv(LEDGER_PATH)
    if not ledger:
        out.append("")
        out.append("  ** The decision ledger is empty, so pillars 4 and 5 cannot be")
        out.append("     measured at all. That is the single largest gap: until")
        out.append("     `council` records its picks, 'do the voices add value?'")
        out.append("     has no answer and the Council cannot be weighted.")
    return out + [""]


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

PILLARS = ["discovery", "data", "mechanical", "judgement", "decision", "outcome", "gaps"]


def build(selected=None, benchmark="VWCE.DE", offline=False):
    selected = selected or PILLARS
    needs_prices = any(p in selected for p in ("mechanical", "judgement", "decision"))
    prices, bench, bench_now = {}, {}, None
    if needs_prices and not offline:
        tickers = {r["ticker"] for r in _read_csv(HISTORY_PATH)}
        tickers |= {r["ticker"] for r in _read_csv(LEDGER_PATH)}
        if tickers:
            print(f"  fetching current prices for {len(tickers)} tracked names...",
                  file=sys.stderr)
            prices = current_prices(tickers)
        bench = benchmark_series(benchmark)
        bench_now = bench[max(bench)] if bench else None

    lines = [
        "# System scorecard",
        "",
        f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} "
        f"· benchmark {benchmark}",
        "",
        "Every skill figure below is **excess return versus the benchmark**, not a "
        "raw return — a raw return mostly measures the market. Any bucket with "
        f"fewer than {MIN_OBSERVATIONS} observations reports its count and "
        "withholds the number, because a hit rate computed on a handful of picks "
        "is noise that reads like skill.",
        "",
    ]
    fn = {"discovery": pillar_discovery, "data": pillar_data, "gaps": pillar_gaps}
    for p in PILLARS:
        if p not in selected:
            continue
        if p in fn:
            lines += fn[p]()
        elif p == "mechanical":
            lines += pillar_mechanical(prices, bench, bench_now)
        elif p == "judgement":
            lines += pillar_judgement(prices, bench, bench_now)
        elif p == "decision":
            lines += pillar_decision(prices, bench, bench_now)
        elif p == "outcome":
            lines += pillar_outcome(benchmark) if not offline else []
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pillar", action="append", choices=PILLARS,
                   help="limit to one or more pillars (default: all)")
    p.add_argument("--benchmark", default="VWCE.DE")
    p.add_argument("--write", action="store_true",
                   help=f"also write {os.path.relpath(OUT_PATH, ROOT)}")
    p.add_argument("--offline", action="store_true",
                   help="skip every network call (structure only, no returns)")
    args = p.parse_args()
    text = build(args.pillar, args.benchmark, args.offline)
    print(text)
    if args.write:
        os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
        with open(OUT_PATH, "w") as f:
            f.write(text + "\n")
        print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
