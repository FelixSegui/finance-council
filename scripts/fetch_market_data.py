#!/usr/bin/env python3
"""
Fetch market data from free sources only. No API keys required.

Sources:
  - Equities/ETFs: yfinance (Yahoo Finance)
  - Crypto: CoinGecko public API
  - US Macro: FRED public CSV download (no key needed for this endpoint)
  - Swedish macro: Riksbank SWEA API (policy rate), SCB PxWeb (CPI)
  - Euro area: ECB Data Portal (deposit facility rate)
  - Sentiment: alternative.me crypto Fear & Greed index
  - Insider activity: SEC EDGAR (US tickers only, --insiders flag)

Writes one timestamped JSON snapshot to data/cache/snapshots/.
Every downstream agent reads this file — it is the single source of
numerical truth for the session. If a fetch fails, the field is written
as null with an "error" note, never silently omitted or guessed.

Usage:
  python fetch_market_data.py --tickers AAPL,VWCE.DE,SPY --crypto bitcoin,ethereum
  python fetch_market_data.py --tickers AAPL,MSFT --insiders
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
import csv
import io
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import derived_metrics  # noqa: E402
from config.settings import (  # noqa: E402
    DEFAULT_CORPORATE_TAX_RATE_ASSUMPTION, DEFAULT_CORPORATE_TAX_RATE_FALLBACK,
)

FRED_SERIES = {
    "fed_funds_rate": "FEDFUNDS",
    "us_10y_yield": "DGS10",
    "us_2y_yield": "DGS2",
    "dollar_index": "DTWEXBGS",
    "sek_per_usd": "DEXSDUS",
    "usd_per_eur": "DEXUSEU",  # used to derive sek_per_eur (no direct FRED SEK/EUR series)
    "vix": "VIXCLS",
}

# SEC requires a User-Agent identifying the requester
SEC_UA = {"User-Agent": "finance-council personal research (seguifelix@gmail.com)"}


def _get_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


CHART_UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


def _fetch_chart_direct(ticker, timeout=15):
    """Yahoo's v8 chart endpoint needs no crumb/cookie - only the
    quoteSummary (fundamentals) endpoint requires one. Used as a last-resort
    fallback (price only) if the crumb-based fetch below fails for any
    reason (network hiccup, ticker not covered, etc)."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=5d&interval=1d"
    req = urllib.request.Request(url, headers=CHART_UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode())
    result = (data.get("chart") or {}).get("result")
    if not result:
        err = (data.get("chart") or {}).get("error")
        raise ValueError(f"no chart result (error: {err})")
    meta = result[0].get("meta", {})
    return {
        "price": meta.get("regularMarketPrice"),
        "prev_close": meta.get("chartPreviousClose"),
        "52w_high": meta.get("fiftyTwoWeekHigh"),
        "52w_low": meta.get("fiftyTwoWeekLow"),
        "currency": meta.get("currency"),
    }


class _YahooCrumbSession:
    """Yahoo's fundamentals endpoint (quoteSummary) requires a 'crumb' token
    minted from a cookie obtained at fc.yahoo.com. yfinance's own client
    (curl_cffi, browser-TLS-fingerprint impersonation) gets connection-reset
    by Yahoo's anti-bot layer even once the network path is open - plain
    urllib with a cookie jar does not trigger that and works reliably.
    One cookie+crumb per script run, reused across all tickers."""

    def __init__(self, timeout=15):
        self.timeout = timeout
        self._cookie_jar = None
        self._crumb = None
        self._init_error = None
        self._initialized = False

    def _ensure_init(self):
        if self._initialized:
            return
        self._initialized = True
        try:
            import http.cookiejar
            self._cookie_jar = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(self._cookie_jar))
            req = urllib.request.Request("https://fc.yahoo.com", headers=CHART_UA)
            try:
                opener.open(req, timeout=self.timeout)  # sets cookies; a 404 status is expected and fine
            except urllib.error.HTTPError:
                pass  # cookies are set by the CookieProcessor before the error is raised
            req = urllib.request.Request(
                "https://query1.finance.yahoo.com/v1/test/getcrumb", headers=CHART_UA)
            with opener.open(req, timeout=self.timeout) as resp:
                self._crumb = resp.read().decode().strip()
            self._opener = opener
            if not self._crumb or "<html" in self._crumb.lower():
                raise ValueError(f"no usable crumb returned: {self._crumb!r}")
        except Exception as e:
            self._init_error = str(e)

    def fetch_quote_summary(self, ticker):
        self._ensure_init()
        if self._init_error:
            raise RuntimeError(f"crumb session init failed: {self._init_error}")
        modules = "summaryDetail,defaultKeyStatistics,financialData,assetProfile,incomeStatementHistory"
        url = (f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}"
               f"?modules={modules}&crumb={self._crumb}")
        req = urllib.request.Request(url, headers=CHART_UA)
        with self._opener.open(req, timeout=self.timeout) as resp:
            data = json.loads(resp.read().decode())
        result = (data.get("quoteSummary") or {}).get("result")
        if not result:
            err = (data.get("quoteSummary") or {}).get("error")
            raise ValueError(f"no quoteSummary result (error: {err})")
        return result[0]


_yahoo_session = _YahooCrumbSession()


def _raw(field):
    """Yahoo wraps numeric fields as {'raw': ..., 'fmt': ...}; pass through
    plain numbers/None unchanged."""
    if isinstance(field, dict):
        return field.get("raw")
    return field


def _fetch_fundamentals_direct(ticker):
    r = _yahoo_session.fetch_quote_summary(ticker)
    summary = r.get("summaryDetail", {})
    stats = r.get("defaultKeyStatistics", {})
    fin = r.get("financialData", {})
    profile = r.get("assetProfile", {})
    income_stmts = r.get("incomeStatementHistory", {}).get("incomeStatementHistory", [])
    revenue_history = [
        {"fiscal_year_end": _raw(s.get("endDate")) and s["endDate"].get("fmt"),
         "total_revenue": _raw(s.get("totalRevenue"))}
        for s in income_stmts
    ]

    # --- Layer A additions (2026-08-09): raw figures confirmed genuinely
    # present in the financialData module (verified live against ABB.ST/
    # AZN.ST before writing this) - ebit/interestExpense in
    # incomeStatementHistory are NOT usable, Yahoo returns 0/None for both
    # on every ticker checked (a known degradation of that legacy module,
    # not a bug in this fetcher). Layer B derivations built on top, via the
    # one shared formula module so nothing computes a ratio two ways.
    ebitda = _raw(fin.get("ebitda"))
    total_cash = _raw(fin.get("totalCash"))
    total_debt = _raw(fin.get("totalDebt"))
    operating_cashflow = _raw(fin.get("operatingCashflow"))
    free_cashflow = _raw(fin.get("freeCashflow"))
    total_revenue = _raw(fin.get("totalRevenue"))
    operating_margins = _raw(fin.get("operatingMargins"))
    book_value_per_share = _raw(stats.get("bookValue"))
    shares_outstanding = _raw(stats.get("sharesOutstanding"))
    country = profile.get("country")

    capex = derived_metrics.capex_from_ocf_fcf(operating_cashflow, free_cashflow)
    ebit_estimated = derived_metrics.ebit_from_margin(operating_margins, total_revenue)
    equity_book = derived_metrics.equity_from_book_value(book_value_per_share, shares_outstanding)
    invested_capital = derived_metrics.invested_capital(total_debt, equity_book)
    tax_rate_assumed = (DEFAULT_CORPORATE_TAX_RATE_ASSUMPTION.get(country)
                        or DEFAULT_CORPORATE_TAX_RATE_FALLBACK)
    roic_estimated = derived_metrics.roic(ebit_estimated, tax_rate_assumed, invested_capital)

    layer_a_b = {
        "ebitda": ebitda,
        "total_cash": total_cash,
        "total_debt": total_debt,
        "operating_cashflow": operating_cashflow,
        "capex": {"value": capex, "quality_state": "ESTIMATED" if capex is not None else "MISSING",
                  "calculation_method": "operating_cashflow - free_cashflow"},
        "ebit": {"value": ebit_estimated, "quality_state": "ESTIMATED" if ebit_estimated is not None else "MISSING",
                 "calculation_method": "operating_margins * total_revenue - Yahoo's own EBIT line "
                                        "(incomeStatementHistory) is broken/zero for this source, confirmed "
                                        "empirically, not fetched"},
        "interest_expense": {"value": None, "quality_state": "MISSING",
                             "calculation_method": "not available from Yahoo quoteSummary for any ticker "
                                                    "checked - needs a filing or PDF extract (source tier 1)"},
        "equity_book": {"value": equity_book, "quality_state": "OK" if equity_book is not None else "MISSING",
                        "calculation_method": "book_value_per_share * shares_outstanding"},
        "invested_capital": {"value": invested_capital,
                             "quality_state": "OK" if invested_capital is not None else "MISSING",
                             "calculation_method": "total_debt + equity_book (cash not netted out)"},
        "roic_pct": {"value": roic_estimated,
                    "quality_state": "ESTIMATED" if roic_estimated is not None else "MISSING",
                    "calculation_method": f"ebit*(1-tax_rate)/invested_capital, tax_rate={tax_rate_assumed} "
                                          f"(assumed statutory rate for {country or 'unknown country'}, "
                                          f"NOT a real effective rate - no source provides one)"},
    }
    out = {
        "price": _raw(summary.get("regularMarketPreviousClose")) or _raw(fin.get("currentPrice")),
        "prev_close": _raw(summary.get("previousClose")),
        "52w_high": _raw(summary.get("fiftyTwoWeekHigh")),
        "52w_low": _raw(summary.get("fiftyTwoWeekLow")),
        "market_cap": _raw(summary.get("marketCap")),
        "trailing_pe": _raw(summary.get("trailingPE")),
        "forward_pe": _raw(summary.get("forwardPE")),
        "price_to_sales": _raw(summary.get("priceToSalesTrailing12Months")),
        "price_to_book": _raw(stats.get("priceToBook")),
        "peg_ratio": _raw(stats.get("pegRatio")),
        "dividend_yield": _raw(summary.get("dividendYield")),
        "payout_ratio": _raw(summary.get("payoutRatio")),
        "beta": _raw(summary.get("beta")),
        "revenue_growth": _raw(fin.get("revenueGrowth")),
        "total_revenue": _raw(fin.get("totalRevenue")),
        "free_cashflow": _raw(fin.get("freeCashflow")),
        "revenue_history_last_n_fiscal_years": revenue_history,
        "gross_margins": _raw(fin.get("grossMargins")),
        "operating_margins": _raw(fin.get("operatingMargins")),
        "ebitda_margins": _raw(fin.get("ebitdaMargins")),
        "profit_margins": _raw(fin.get("profitMargins")),
        "return_on_equity": _raw(fin.get("returnOnEquity")),
        "return_on_assets": _raw(fin.get("returnOnAssets")),
        "debt_to_equity": _raw(fin.get("debtToEquity")),
        "recommendation": fin.get("recommendationKey"),
        # sector/country feed the portfolio agent's balance scorecard
        "sector": profile.get("sector"),
        "industry": profile.get("industry"),
        "country": profile.get("country"),
        "currency": summary.get("currency"),
        "fundamentals_source": "Yahoo quoteSummary via direct crumb fetch (fc.yahoo.com + getcrumb) - "
                                "yfinance's own client fails on this network (curl_cffi TLS fingerprint "
                                "gets connection-reset by Yahoo's anti-bot layer), plain urllib does not.",
        "note": "Multi-year revenue is real (Yahoo's own reported fiscal-year figures). Free cash flow, "
                "capex, EBIT, ROIC, and invested capital are TRAILING-ONLY snapshots (single current "
                "figures, not multi-year series) - Yahoo's legacy cashflowStatementHistory/"
                "incomeStatementHistory modules don't expose real multi-year capex/EBIT lines. capex, ebit, "
                "and roic_pct below are DERIVED (see each field's calculation_method), not filed figures - "
                "for a real FCF/EBIT trend, use a company's own cash flow statement (PDF via the pdf skill).",
    }
    out.update(layer_a_b)
    return out


def fetch_equities(tickers):
    out = {}
    for t in tickers:
        try:
            out[t] = _fetch_fundamentals_direct(t)
        except Exception as e:
            # Fundamentals fetch failed (network hiccup, ticker not covered,
            # crumb session couldn't init). Fall back to the crumb-free
            # chart endpoint for price only - never silently guess
            # fundamentals.
            try:
                chart = _fetch_chart_direct(t)
                chart["fundamentals_error"] = f"fundamentals fetch failed: {e}"
                out[t] = chart
            except Exception as e2:
                out[t] = {"error": f"{e}; chart fallback also failed: {e2}"}
    return out


def fetch_insider_activity_fi(issuer_names, max_rows=15, timeout=15):
    """Finansinspektionen's PDMR/Insynsregister - real, free, public insider
    transaction data for Swedish-listed companies. Search is by issuer NAME
    (not ticker). Returns the most recent transactions per issuer; the
    register itself is unreviewed/self-reported by the notifying party -
    FI states it cannot guarantee completeness or correctness."""
    out = {}
    for name in issuer_names:
        try:
            from bs4 import BeautifulSoup
            params = urllib.parse.urlencode({
                "SearchFunctionType": "Insyn",
                "Utgivare": name,
                "PageNumber": 1,
            })
            url = f"https://marknadssok.fi.se/Publiceringsklient/en-GB/Search/Search?{params}"
            req = urllib.request.Request(url, headers=CHART_UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                html = resp.read().decode()
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("table")
            if table is None:
                out[name] = {"transactions": [], "note": "no results table found - issuer name may not match FI's registry spelling"}
                continue
            rows = table.find_all("tr")
            headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])] if rows else []
            transactions = []
            for row in rows[1:1 + max_rows]:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                if len(cells) == len(headers):
                    transactions.append(dict(zip(headers, cells)))
            out[name] = {
                "transactions": transactions,
                "source": "Finansinspektionen Insynsregister (marknadssok.fi.se), free public data, "
                          "attribution required. FI does not review notifications before publication - "
                          "cannot guarantee completeness/correctness.",
                "note": f"showing up to {max_rows} most recent transactions, may not be the full set",
            }
        except Exception as e:
            out[name] = {"error": str(e)}
    return out


def fetch_crypto(coin_ids):
    if not coin_ids:
        return {}
    ids = ",".join(coin_ids)
    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        f"?vs_currency=eur&ids={ids}&order=market_cap_desc"
        "&price_change_percentage=24h,7d,30d"
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        out = {}
        for coin in data:
            out[coin["id"]] = {
                "price_eur": coin.get("current_price"),
                "market_cap": coin.get("market_cap"),
                "market_cap_rank": coin.get("market_cap_rank"),
                "change_24h_pct": coin.get("price_change_percentage_24h_in_currency"),
                "change_7d_pct": coin.get("price_change_percentage_7d_in_currency"),
                "change_30d_pct": coin.get("price_change_percentage_30d_in_currency"),
                "ath": coin.get("ath"),
                "ath_change_pct": coin.get("ath_change_percentage"),
            }
        return out
    except Exception as e:
        return {"error": str(e)}


def fetch_fred_series(series_id, last_n=1):
    """Return the last_n observations of a FRED series as a list of
    {date, value} dicts (oldest first), or {"error": ...}."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            text = resp.read().decode()
        reader = csv.reader(io.StringIO(text))
        rows = [r for r in list(reader)[1:] if len(r) == 2 and r[1] not in ("", ".")]
        if not rows:
            return {"error": "no data returned"}
        return [{"date": d, "value": v} for d, v in rows[-last_n:]]
    except Exception as e:
        return {"error": str(e)}


def fetch_us_cpi_yoy():
    """CPIAUCSL is an index level, not a rate — compute YoY from 13 months."""
    obs = fetch_fred_series("CPIAUCSL", last_n=13)
    if isinstance(obs, dict):  # error
        return obs
    if len(obs) < 13:
        return {"error": "insufficient CPI history"}
    try:
        first, last = float(obs[0]["value"]), float(obs[-1]["value"])
        return {"date": obs[-1]["date"], "value": round((last / first - 1) * 100, 2)}
    except ValueError as e:
        return {"error": str(e)}


def fetch_riksbank_policy_rate():
    frm = (datetime.now(timezone.utc) - timedelta(days=120)).strftime("%Y-%m-%d")
    url = f"https://api.riksbank.se/swea/v1/Observations/SECBREPOEFF/{frm}"
    try:
        data = _get_json(url)
        if not data:
            return {"error": "no observations returned"}
        last = data[-1]
        return {"date": last.get("date"), "value": last.get("value")}
    except Exception as e:
        return {"error": str(e)}


def fetch_ecb_deposit_rate():
    url = (
        "https://data-api.ecb.europa.eu/service/data/FM/"
        "D.U2.EUR.4F.KR.DFR.LEV?lastNObservations=1&format=csvdata"
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            text = resp.read().decode()
        rows = list(csv.DictReader(io.StringIO(text)))
        if not rows:
            return {"error": "no data returned"}
        r = rows[-1]
        return {"date": r.get("TIME_PERIOD"), "value": r.get("OBS_VALUE")}
    except Exception as e:
        return {"error": str(e)}


def fetch_se_cpi_yoy():
    """Swedish CPI YoY from SCB PxWeb (13 months of the KPI total index)."""
    url = "https://api.scb.se/OV0104/v1/doris/en/ssd/START/PR/PR0101/PR0101A/KPItotM"
    query = {
        "query": [{"code": "Tid", "selection": {"filter": "top", "values": ["13"]}}],
        "response": {"format": "json"},
    }
    try:
        req = urllib.request.Request(
            url, data=json.dumps(query).encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8-sig"))
        pts = data.get("data", [])
        if len(pts) < 13:
            return {"error": "insufficient history returned"}
        first = float(pts[0]["values"][0])
        last = float(pts[-1]["values"][0])
        return {"period": pts[-1]["key"][0], "value": round((last / first - 1) * 100, 2)}
    except Exception as e:
        return {"error": str(e)}


def fetch_crypto_fear_greed():
    try:
        data = _get_json("https://api.alternative.me/fng/?limit=1")
        d = data["data"][0]
        return {"value": int(d["value"]), "classification": d["value_classification"]}
    except Exception as e:
        return {"error": str(e)}


def fetch_insider_activity(tickers):
    """Form 4 filing counts from SEC EDGAR for US-listed tickers.
    Count only — buy/sell direction requires reading individual filings."""
    out = {}
    us = [t for t in tickers if "." not in t]
    for t in tickers:
        if t not in us:
            out[t] = {"skipped": "non-US ticker, not covered by SEC EDGAR"}
    if not us:
        return out
    try:
        mapping = _get_json("https://www.sec.gov/files/company_tickers.json", headers=SEC_UA)
        by_ticker = {v["ticker"].upper(): str(v["cik_str"]).zfill(10) for v in mapping.values()}
    except Exception as e:
        out["error"] = f"CIK mapping fetch failed: {e}"
        return out
    cutoff = (datetime.now(timezone.utc) - timedelta(days=90)).strftime("%Y-%m-%d")
    for t in us:
        cik = by_ticker.get(t.upper())
        if not cik:
            out[t] = {"error": "ticker not found in SEC CIK mapping"}
            continue
        try:
            subs = _get_json(f"https://data.sec.gov/submissions/CIK{cik}.json", headers=SEC_UA)
            recent = subs["filings"]["recent"]
            form4_dates = [
                d for f, d in zip(recent["form"], recent["filingDate"])
                if f == "4" and d >= cutoff
            ]
            out[t] = {
                "form4_filings_90d": len(form4_dates),
                "latest_form4_date": max(form4_dates) if form4_dates else None,
                "note": "filing count only; direction (buy vs sell) not extracted",
            }
        except Exception as e:
            out[t] = {"error": str(e)}
    return out


def fetch_macro():
    out = {}
    for label, series_id in FRED_SERIES.items():
        obs = fetch_fred_series(series_id)
        out[label] = obs[-1] if isinstance(obs, list) else obs
    out["us_cpi_yoy"] = fetch_us_cpi_yoy()
    out["riksbank_policy_rate"] = fetch_riksbank_policy_rate()
    out["ecb_deposit_rate"] = fetch_ecb_deposit_rate()
    out["se_cpi_yoy"] = fetch_se_cpi_yoy()
    # yield curve spread is the single most-watched recession signal —
    # compute it directly rather than making the macro-regime agent do math
    try:
        y10 = float(out["us_10y_yield"]["value"])
        y2 = float(out["us_2y_yield"]["value"])
        out["10y_2y_spread"] = round(y10 - y2, 3)
    except (KeyError, TypeError, ValueError):
        out["10y_2y_spread"] = None
    # No FRED series quotes SEK/EUR directly; derive it from sek_per_usd x
    # usd_per_eur (both DEXSDUS and DEXUSEU are noon buying rates from the
    # same source, same day) rather than leaving it unfetched.
    try:
        sek_usd = float(out["sek_per_usd"]["value"])
        usd_eur = float(out["usd_per_eur"]["value"])
        out["sek_per_eur"] = {
            "date": out["sek_per_usd"]["date"],
            "value": round(sek_usd * usd_eur, 4),
            "derived_from": "sek_per_usd (DEXSDUS) x usd_per_eur (DEXUSEU)",
        }
    except (KeyError, TypeError, ValueError):
        out["sek_per_eur"] = {"error": "could not derive: sek_per_usd or usd_per_eur missing/invalid"}
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", default="", help="Comma-separated equity/ETF tickers")
    parser.add_argument("--crypto", default="", help="Comma-separated CoinGecko coin ids")
    parser.add_argument("--insiders", action="store_true",
                        help="Also fetch SEC EDGAR Form 4 counts for US tickers")
    parser.add_argument("--fi-issuers", default="",
                        help="Comma-separated Swedish issuer names (not tickers) to fetch "
                             "PDMR insider transactions for, from Finansinspektionen's "
                             "Insynsregister, e.g. 'Atlas Copco,Volvo,Handelsbanken'")
    args = parser.parse_args()

    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]
    coins = [c.strip() for c in args.crypto.split(",") if c.strip()]
    fi_issuers = [n.strip() for n in args.fi_issuers.split(",") if n.strip()]

    snapshot = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "equities": fetch_equities(tickers) if tickers else {},
        "crypto": fetch_crypto(coins),
        "macro": fetch_macro(),
        "sentiment": {"crypto_fear_greed": fetch_crypto_fear_greed()},
    }
    if args.insiders and tickers:
        snapshot["insider_activity"] = fetch_insider_activity(tickers)
    if fi_issuers:
        snapshot["insider_activity_fi"] = fetch_insider_activity_fi(fi_issuers)

    import os
    import glob
    os.makedirs("data/cache/snapshots", exist_ok=True)
    today_prefix = datetime.now(timezone.utc).strftime("%Y%m%d")
    existing_today = glob.glob(f"data/cache/snapshots/{today_prefix}T*.json")
    if existing_today:
        # Not a hard block - a same-day re-fetch can be legitimate (intraday
        # price move, testing a fix). But macro series (FRED, Riksbank, ECB)
        # update at most daily/monthly, so re-fetching them repeatedly in one
        # day is pure waste - flag it so a human notices the pattern rather
        # than silently accumulating near-duplicate snapshots.
        print(f"Note: {len(existing_today)} snapshot(s) already exist for "
              f"today ({', '.join(os.path.basename(f) for f in existing_today)}) "
              f"- macro data won't have changed since the last one today; "
              f"only re-fetch if you specifically need fresher equity/crypto prices.")
    fname = f"data/cache/snapshots/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"Wrote {fname}")
    return fname


if __name__ == "__main__":
    main()
