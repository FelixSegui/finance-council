#!/usr/bin/env python3
"""
Macro indicators only — FRED (US), Riksbank SWEA (Swedish policy rate), SCB
PxWeb (Swedish CPI), ECB Data Portal (euro area deposit rate). Separated so a
macro-source outage (any one of these four independent APIs) doesn't get
tangled up with equity/crypto fetch problems.

Usage:
  python scripts/fetch_macro.py
"""
import csv
import io
import json
import os
import urllib.request
from datetime import datetime, timezone, timedelta

FRED_SERIES = {
    "fed_funds_rate": "FEDFUNDS",
    "us_10y_yield": "DGS10",
    "us_2y_yield": "DGS2",
    "dollar_index": "DTWEXBGS",
    "sek_per_usd": "DEXSDUS",
    "usd_per_eur": "DEXUSEU",
    "vix": "VIXCLS",
}


def _get_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def fetch_fred_series(series_id, last_n=1):
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
    obs = fetch_fred_series("CPIAUCSL", last_n=13)
    if isinstance(obs, dict):
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
    url = "https://api.scb.se/OV0104/v1/doris/en/ssd/START/PR/PR0101/PR0101A/KPItotM"
    query = {
        "query": [{"code": "Tid", "selection": {"filter": "top", "values": ["13"]}}],
        "response": {"format": "json"},
    }
    try:
        req = urllib.request.Request(
            url, data=json.dumps(query).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8-sig"))
        pts = data.get("data", [])
        if len(pts) < 13:
            return {"error": "insufficient history returned"}
        first, last = float(pts[0]["values"][0]), float(pts[-1]["values"][0])
        return {"period": pts[-1]["key"][0], "value": round((last / first - 1) * 100, 2)}
    except Exception as e:
        return {"error": str(e)}


def fetch_macro():
    out = {}
    for label, series_id in FRED_SERIES.items():
        obs = fetch_fred_series(series_id)
        out[label] = obs[-1] if isinstance(obs, list) else obs
    out["us_cpi_yoy"] = fetch_us_cpi_yoy()
    out["riksbank_policy_rate"] = fetch_riksbank_policy_rate()
    out["ecb_deposit_rate"] = fetch_ecb_deposit_rate()
    out["se_cpi_yoy"] = fetch_se_cpi_yoy()
    try:
        y10, y2 = float(out["us_10y_yield"]["value"]), float(out["us_2y_yield"]["value"])
        out["10y_2y_spread"] = round(y10 - y2, 3)
    except (KeyError, TypeError, ValueError):
        out["10y_2y_spread"] = None
    try:
        sek_usd, usd_eur = float(out["sek_per_usd"]["value"]), float(out["usd_per_eur"]["value"])
        out["sek_per_eur"] = {"date": out["sek_per_usd"]["date"], "value": round(sek_usd * usd_eur, 4),
                              "derived_from": "sek_per_usd (DEXSDUS) x usd_per_eur (DEXUSEU)"}
    except (KeyError, TypeError, ValueError):
        out["sek_per_eur"] = {"error": "could not derive: sek_per_usd or usd_per_eur missing/invalid"}
    return out


def main():
    data = fetch_macro()
    os.makedirs("data/cache/macro", exist_ok=True)
    fname = f"data/cache/macro/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(), "macro": data}, f, indent=2)

    print(f"Wrote {fname}")
    for k, v in data.items():
        status = "ERROR" if isinstance(v, dict) and "error" in v else "OK"
        print(f"  {status:<6s} {k:<20s} {v}")
    return fname


if __name__ == "__main__":
    main()
