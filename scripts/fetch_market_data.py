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

Writes one timestamped JSON snapshot to data/snapshots/.
Every downstream agent reads this file — it is the single source of
numerical truth for the session. If a fetch fails, the field is written
as null with an "error" note, never silently omitted or guessed.

Usage:
  python fetch_market_data.py --tickers AAPL,VWCE.DE,SPY --crypto bitcoin,ethereum
  python fetch_market_data.py --tickers AAPL,MSFT --insiders
"""
import argparse
import json
import sys
import urllib.request
import urllib.error
import csv
import io
from datetime import datetime, timezone, timedelta

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
    quoteSummary (fundamentals) endpoint requires one. Used as a fallback
    when yfinance's own crumb negotiation fails (e.g. an egress policy
    blocks fc.yahoo.com and guce.yahoo.com, the two hosts yfinance uses to
    mint a crumb, while leaving the plain data hosts reachable). Returns
    price fields only - fundamentals genuinely need the crumb and are not
    obtainable this way."""
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


def fetch_equities(tickers):
    try:
        import yfinance as yf
    except ImportError:
        return {"error": "yfinance not installed. pip install yfinance"}

    out = {}
    for t in tickers:
        try:
            tk = yf.Ticker(t)
            info = tk.fast_info
            fundamentals = tk.info if hasattr(tk, "info") else {}
            out[t] = {
                "price": getattr(info, "last_price", None),
                "prev_close": getattr(info, "previous_close", None),
                "52w_high": getattr(info, "year_high", None),
                "52w_low": getattr(info, "year_low", None),
                "market_cap": fundamentals.get("marketCap"),
                "trailing_pe": fundamentals.get("trailingPE"),
                "forward_pe": fundamentals.get("forwardPE"),
                "peg_ratio": fundamentals.get("pegRatio"),
                "dividend_yield": fundamentals.get("dividendYield"),
                "beta": fundamentals.get("beta"),
                "revenue_growth": fundamentals.get("revenueGrowth"),
                "profit_margins": fundamentals.get("profitMargins"),
                "debt_to_equity": fundamentals.get("debtToEquity"),
                "recommendation": fundamentals.get("recommendationKey"),
                # sector/country feed the portfolio agent's balance scorecard
                "sector": fundamentals.get("sector"),
                "industry": fundamentals.get("industry"),
                "country": fundamentals.get("country"),
                "currency": fundamentals.get("currency"),
            }
        except Exception as e:
            # yfinance's crumb negotiation failed (commonly a blocked
            # fc.yahoo.com/guce.yahoo.com egress policy, not a data problem).
            # Fall back to the crumb-free chart endpoint for price only;
            # fundamentals genuinely require a crumb and are marked as such,
            # never silently guessed.
            try:
                chart = _fetch_chart_direct(t)
                chart["fundamentals_error"] = (
                    f"fundamentals (P/E, dividend yield, sector, etc.) need a Yahoo "
                    f"crumb, unavailable this session: {e}"
                )
                out[t] = chart
            except Exception as e2:
                out[t] = {"error": f"{e}; chart fallback also failed: {e2}"}
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
    args = parser.parse_args()

    tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]
    coins = [c.strip() for c in args.crypto.split(",") if c.strip()]

    snapshot = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "equities": fetch_equities(tickers) if tickers else {},
        "crypto": fetch_crypto(coins),
        "macro": fetch_macro(),
        "sentiment": {"crypto_fear_greed": fetch_crypto_fear_greed()},
    }
    if args.insiders and tickers:
        snapshot["insider_activity"] = fetch_insider_activity(tickers)

    import os
    import glob
    os.makedirs("data/snapshots", exist_ok=True)
    today_prefix = datetime.now(timezone.utc).strftime("%Y%m%d")
    existing_today = glob.glob(f"data/snapshots/{today_prefix}T*.json")
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
    fname = f"data/snapshots/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"Wrote {fname}")
    return fname


if __name__ == "__main__":
    main()
