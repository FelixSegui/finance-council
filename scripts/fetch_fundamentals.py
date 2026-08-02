#!/usr/bin/env python3
"""
Fundamentals + price/momentum for the coarse ranker, sourced to survive the
Yahoo fundamentals blackout.

Two independent sources, each chosen because it is reachable through the agent
proxy where Yahoo's quoteSummary (fundamentals) endpoint is NOT:

  - FUNDAMENTALS: SEC EDGAR XBRL companyfacts (US filers only). Authoritative,
    free, no key. Gives revenue, net income, equity, liabilities, shares from
    annual 10-K filings — enough for margin, revenue growth, debt/equity, ROE,
    and (with a price) earnings yield / P/E. Non-US tickers (no CIK) return a
    skip, not a guess.
  - PRICE / MOMENTUM: Yahoo's v8 `chart` endpoint. This one IS reachable
    (only the crumb-gated quoteSummary endpoint is blocked), and it covers
    Nordic (.ST) listings too, so momentum works even where SEC fundamentals
    don't.

Every value traces to a fetched response. A field that cannot be computed is
returned as None with the reason recorded — never imputed, never guessed.

Not a CLI entry point for normal use — imported by rank_candidates.py. Run
directly with tickers/ciks only for spot-checking:
  python scripts/fetch_fundamentals.py AAPL:0000320193 MSFT:0000789019
"""
import json
import math
import os
import statistics
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone

SEC_UA = {"User-Agent": "finance-council personal research (seguifelix@gmail.com)"}

# Revenue is reported under several XBRL concepts depending on the filer/era —
# try them in order of preference.
REVENUE_CONCEPTS = [
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "Revenues",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "SalesRevenueNet",
]
SHARE_CONCEPTS_DEI = ["EntityCommonStockSharesOutstanding"]
SHARE_CONCEPTS_GAAP = ["CommonStockSharesOutstanding", "CommonStockSharesIssued"]


def _get_json(url, timeout=30):
    req = urllib.request.Request(url, headers=SEC_UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _annual_flow(facts_gaap, concepts):
    """Latest and prior full-year value for a flow concept (revenue, income).
    Full-year = a 10-K row spanning ~a year. Returns (latest, prior) vals.

    MERGES across all listed concepts (dedupe by period-end, first-listed concept
    wins ties) rather than returning the first concept that has any data. Filers
    switch XBRL revenue tags over time, so picking one concept can return a stale
    year for revenue while net income comes from the current year — producing an
    impossible margin (e.g. net income > revenue). Merging captures the most
    recent year whichever tag it's under."""
    by_end = {}
    for concept in concepts:
        node = facts_gaap.get(concept)
        if not node:
            continue
        for unit_rows in node.get("units", {}).values():
            for r in unit_rows:
                if r.get("form", "").startswith("10-K") and r.get("start") and r.get("end"):
                    try:
                        d0 = datetime.fromisoformat(r["start"])
                        d1 = datetime.fromisoformat(r["end"])
                    except ValueError:
                        continue
                    if (d1 - d0).days >= 300 and r["end"] not in by_end:
                        by_end[r["end"]] = r["val"]
    if not by_end:
        return None, None
    ordered = [by_end[e] for e in sorted(by_end)]
    latest = ordered[-1]
    prior = ordered[-2] if len(ordered) >= 2 else None
    return latest, prior


def _annual_instant(facts_gaap, concepts):
    """Latest full-year value for an instant concept (equity, liabilities)."""
    for concept in concepts:
        node = facts_gaap.get(concept)
        if not node:
            continue
        rows = []
        for unit_rows in node.get("units", {}).values():
            for r in unit_rows:
                if r.get("form", "").startswith("10-K") and r.get("end"):
                    rows.append((r["end"], r["val"]))
        if rows:
            rows.sort(key=lambda x: x[0])
            return rows[-1][1]
    return None


_SHARES_MAX_AGE_DAYS = 400  # a bit over a year, to tolerate annual-only filers


def _shares(facts):
    """Latest share count, but ONLY if it's recent. Some multi-class filers
    (e.g. Visa) stop reporting the single-figure EntityCommonStockSharesOutstanding
    tag once they switch to per-class reporting the free companyfacts API can't
    cleanly aggregate (dimensioned facts aren't distinguishable in this feed).
    Without a staleness guard, `sorted(...)[-1]` silently returns the LAST time
    that tag was ever reported — years stale — presented as current, which then
    poisons EPS/PE with a false number (this is exactly how Visa's PE showed 8.7
    instead of its real ~30-35). Per this system's own rule: no data beats wrong
    data, so an old count is treated as missing, not returned."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=_SHARES_MAX_AGE_DAYS)).date().isoformat()
    for c in SHARE_CONCEPTS_DEI:
        node = facts.get("dei", {}).get(c)
        if node:
            for unit_rows in node.get("units", {}).values():
                rows = sorted((r["end"], r["val"]) for r in unit_rows if r.get("end"))
                if rows and rows[-1][0] >= cutoff:
                    return rows[-1][1]
    gaap = facts.get("us-gaap", {})
    for concept in SHARE_CONCEPTS_GAAP:
        node = gaap.get(concept)
        if not node:
            continue
        rows = []
        for unit_rows in node.get("units", {}).values():
            for r in unit_rows:
                if r.get("form", "").startswith("10-K") and r.get("end"):
                    rows.append((r["end"], r["val"]))
        if rows:
            rows.sort(key=lambda x: x[0])
            if rows[-1][0] >= cutoff:
                return rows[-1][1]
    return None


UNIVERSE_CIK_CACHE = "data/cache/universe.json"


def resolve_ciks(tickers):
    """ticker -> CIK, preferring the already-fetched S&P 500 metadata cache
    (data/cache/universe.json, populated by build_universe.py) over a live
    www.sec.gov/files/company_tickers.json lookup. This matters: that lookup
    endpoint has been observed 403-blocked at the proxy level (a genuine,
    reportable org-policy denial — see /root/.ccr/README.md's rule not to
    retry 403s) while data.sec.gov's own fundamentals API stays reachable.
    Only tickers NOT already in the cache (non-S&P-500 US names) trigger the
    live lookup; if that also fails, they get "unresolved", not a guess."""
    resolved = {}
    remaining = list(tickers)
    if os.path.exists(UNIVERSE_CIK_CACHE):
        try:
            with open(UNIVERSE_CIK_CACHE) as f:
                meta = json.load(f).get("metadata", {})
            for t in list(remaining):
                cik = (meta.get(t) or {}).get("cik")
                if cik:
                    resolved[t] = cik
                    remaining.remove(t)
        except (json.JSONDecodeError, OSError):
            pass
    if remaining:
        try:
            mapping = _get_json("https://www.sec.gov/files/company_tickers.json")
            by_ticker = {v["ticker"].upper(): str(v["cik_str"]).zfill(10) for v in mapping.values()}
            for t in remaining:
                cik = by_ticker.get(t.upper())
                if cik:
                    resolved[t] = cik
        except Exception as e:
            for t in remaining:
                resolved.setdefault(t, None)
            resolved["_lookup_error"] = str(e)
    return resolved


def fetch_sec_fundamentals(cik):
    """Derived fundamentals for one CIK, or {'error': ...}. Price-independent."""
    if not cik:
        return {"error": "no CIK (non-US or unmapped ticker)"}
    try:
        facts = _get_json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")["facts"]
    except urllib.error.HTTPError as e:
        return {"error": f"SEC companyfacts HTTP {e.code}"}
    except Exception as e:
        return {"error": f"SEC companyfacts fetch failed: {e}"}

    gaap = facts.get("us-gaap", {})
    revenue, revenue_prior = _annual_flow(gaap, REVENUE_CONCEPTS)
    net_income, _ = _annual_flow(gaap, ["NetIncomeLoss"])
    equity = _annual_instant(gaap, ["StockholdersEquity"])
    liabilities = _annual_instant(gaap, ["Liabilities"])
    shares = _shares(facts)

    def ratio(n, d):
        if n is None or d in (None, 0):
            return None
        return n / d

    margin = ratio(net_income, revenue)
    # Plausibility guard: a net margin outside [-100%, +100%] means the revenue
    # figure is wrong for this filer (a bank/REIT with no clean "Revenues" tag, or
    # a mismatched concept). Drop it rather than poison the quality factor with a
    # 446%/2073% margin. Better a null the ranker sets aside than a false number.
    if margin is not None and not (-1.0 <= margin <= 1.0):
        margin = None

    return {
        "revenue": revenue,
        "revenue_prior": revenue_prior,
        "net_income": net_income,
        "equity": equity,
        "liabilities": liabilities,
        "shares": shares,
        "profit_margin": margin,
        "revenue_growth": (ratio(revenue, revenue_prior) - 1) if revenue_prior else None,
        "debt_to_equity": ratio(liabilities, equity),
        "roe": ratio(net_income, equity),
        "_source": "sec_edgar_companyfacts",
    }


# Yahoo exchange suffixes we keep as-is; only US class-share dots (BRK.B) get
# rewritten to dashes (BRK-B). Without this, SAP.DE would become SAP-DE (404).
_EXCH_SUFFIXES = {
    "ST", "DE", "AS", "PA", "CO", "MI", "SW", "MC", "L", "BR", "HE", "OL",
    "VI", "LS", "IR", "F", "BE", "MU", "SG", "TO", "HK", "T", "AX", "NZ",
}


def _yahoo_symbol(ticker):
    if "." in ticker:
        base, suf = ticker.rsplit(".", 1)
        if suf.upper() in _EXCH_SUFFIXES:
            return ticker  # foreign exchange-suffixed symbol — keep the dot
        return ticker.replace(".", "-")  # US class share, e.g. BRK.B -> BRK-B
    return ticker


def _get_json_retry(url, timeout=20, tries=3):
    """Yahoo throttles bursts by returning sporadic 404/429 (not just 429), so
    retry transient HTTP errors with backoff before giving up."""
    last = None
    for i in range(tries):
        try:
            return _get_json(url, timeout=timeout)
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (404, 429, 500, 502, 503) and i < tries - 1:
                time.sleep(0.6 * (i + 1))
                continue
            raise
    raise last


def fetch_price_momentum(ticker):
    """Last price, 52w range position, and momentum from Yahoo's chart endpoint
    (the reachable one). Returns {'error': ...} on failure."""
    sym = _yahoo_symbol(ticker)
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           "?range=1y&interval=1d")
    try:
        data = _get_json_retry(url, timeout=20)
        res = data["chart"]["result"][0]
        closes = [c for c in res["indicators"]["quote"][0]["close"] if c is not None]
        if len(closes) < 30:
            return {"error": "insufficient price history"}
        price = closes[-1]
        prev_close = closes[-2] if len(closes) >= 2 else None
        hi, lo = max(closes), min(closes)
        mom_12m = price / closes[0] - 1
        mom_6m = price / closes[-126] - 1 if len(closes) >= 126 else None
        # Risk metrics from the same series (same formulas as backtest.py:metrics)
        rets = [closes[i] / closes[i - 1] - 1 for i in range(1, len(closes))]
        vol = statistics.pstdev(rets) * math.sqrt(252) if len(rets) > 1 else None
        run_max, max_dd = closes[0], 0.0
        for c in closes:
            run_max = max(run_max, c)
            max_dd = min(max_dd, c / run_max - 1)
        return {
            "price": price,
            "prev_close": prev_close,
            "currency": res["meta"].get("currency"),
            "52w_high": hi,
            "52w_low": lo,
            "pct_of_52w_high": price / hi if hi else None,
            "momentum_6m": mom_6m,
            "momentum_12m": mom_12m,
            "volatility": vol,          # annualized stdev of daily returns
            "max_drawdown": max_dd,     # most negative peak-to-trough over 1y
            "_source": "yahoo_chart_v8",
        }
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        return {"error": f"yahoo chart unreachable: {e}"}
    except (KeyError, IndexError, TypeError) as e:
        return {"error": f"yahoo chart parse failed: {e}"}


def fetch_one(ticker, cik, polite_delay=0.12):
    """Combine both sources for a single name, joining P/E where possible."""
    fund = fetch_sec_fundamentals(cik)
    time.sleep(polite_delay)  # SEC asks for <10 req/s
    px = fetch_price_momentum(ticker)
    rec = {"ticker": ticker, "cik": cik}
    rec.update({k: v for k, v in px.items() if not k.startswith("_")})
    rec["price_error"] = px.get("error")
    rec.update({k: v for k, v in fund.items() if not k.startswith("_")})
    rec["fundamentals_error"] = fund.get("error")
    # earnings yield / PE need both a price and SEC earnings+shares
    price = px.get("price")
    ni, sh = fund.get("net_income"), fund.get("shares")
    if price and ni and sh:
        eps = ni / sh
        rec["eps"] = eps
        rec["pe"] = price / eps if eps > 0 else None
        rec["earnings_yield"] = eps / price
    else:
        rec["eps"] = rec["pe"] = rec["earnings_yield"] = None
    return rec


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        tkr, _, cik = arg.partition(":")
        print(json.dumps(fetch_one(tkr, cik.zfill(10) if cik else None), indent=2))
