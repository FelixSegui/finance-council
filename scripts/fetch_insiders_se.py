#!/usr/bin/env python3
"""
Swedish corporate insider activity — Finansinspektionen's Insynsregistret
(the Swedish equivalent of SEC Form 4: board/executive trades on Nasdaq
Stockholm and Nordic Growth Market issuers). Verified live and working
through this environment's proxy in-session — real transaction data with
genuine BUY/SELL direction (Förvärv/Avyttring), richer than the US Form 4
count-only feed, since FI's export includes the actual transaction type.

This is a NEW capability this system didn't have before — closes the "no
insider signal at all for Swedish holdings" gap (SEC EDGAR is US-filer-only).

Source: https://marknadssok.fi.se/Publiceringsklient/ — a public CSV export
endpoint, no key needed. Response is UTF-16 encoded.

Usage:
  python scripts/fetch_insiders_se.py --issuer Volvo --days 60
  python scripts/fetch_insiders_se.py --issuer "Investor" --days 60
"""
import argparse
import csv
import io
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta

UA = {"User-Agent": "finance-council personal research (seguifelix@gmail.com)"}
BASE_URL = "https://marknadssok.fi.se/Publiceringsklient/sv-SE/Search/Search"

# Karaktar values worth flagging as genuine conviction vs. routine noise —
# reported here so the reader can judge, not decided for them.
ROUTINE_KARAKTAR = {"Lösen ökning", "Lösen minskning"}  # option exercise, not open-market conviction


def fetch_insynsregistret(issuer, date_from, date_to):
    """issuer: free-text company name (FI's own search, not an exact ticker
    match — e.g. 'Volvo' matches 'AB Volvo'). Returns list of transaction
    dicts, or {'error': ...}."""
    params = {
        "SearchFunctionType": "Insyn",
        "Utgivare": issuer,
        "PersonILedandeStällningNamn": "",
        "Transaktionsdatum.From": date_from,
        "Transaktionsdatum.To": date_to,
        "Publiceringsdatum.From": date_from,
        "Publiceringsdatum.To": date_to,
        "button": "export",
    }
    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read()
        text = raw.decode("utf-16")
        rows = list(csv.DictReader(io.StringIO(text), delimiter=";"))
        out = []
        for r in rows:
            karaktar = r.get("Karaktär")
            out.append({
                "publication_date": r.get("Publiceringsdatum"),
                "issuer": r.get("Emittent"),
                "person": r.get("Person i ledande ställning"),
                "role": r.get("Befattning"),
                "related_party": r.get("Närstående"),
                "transaction_type": karaktar,  # "Förvärv"=buy, "Avyttring"=sell, "Lösen ökning/minskning"=option exercise
                "is_routine_option_exercise": karaktar in ROUTINE_KARAKTAR,
                "instrument": r.get("Instrumentnamn"),
                "isin": r.get("ISIN"),
                "transaction_date": r.get("Transaktionsdatum"),
                "volume": r.get("Volym"),
                "price": r.get("Pris"),
                "currency": r.get("Valuta"),
                "venue": r.get("Handelsplats"),
            })
        return out
    except Exception as e:
        return {"error": str(e)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--issuer", required=True, help="Company name (FI free-text search, e.g. 'Volvo')")
    p.add_argument("--days", type=int, default=60)
    args = p.parse_args()

    date_to = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    date_from = (datetime.now(timezone.utc) - timedelta(days=args.days)).strftime("%Y-%m-%d")

    result = fetch_insynsregistret(args.issuer, date_from, date_to)
    os.makedirs("data/cache/insiders_se", exist_ok=True)
    fname = f"data/cache/insiders_se/{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-{args.issuer.replace(' ', '_')}.json"
    with open(fname, "w") as f:
        json.dump({"fetched_at_utc": datetime.now(timezone.utc).isoformat(),
                   "issuer_query": args.issuer, "date_from": date_from, "date_to": date_to,
                   "transactions": result}, f, indent=2)

    print(f"Wrote {fname}")
    if isinstance(result, dict) and "error" in result:
        print(f"  ERROR  {result['error']}")
        return fname
    print(f"  {len(result)} transactions, {date_from} to {date_to}")
    for r in result[:10]:
        flag = " (routine option exercise)" if r["is_routine_option_exercise"] else ""
        print(f"  {r['transaction_date'][:10]}  {r['person']:<22s} {r['role']:<20s} "
              f"{r['transaction_type']:<12s} {r['volume']:>10} @ {r['price']} {r['currency']}{flag}")
    return fname


if __name__ == "__main__":
    main()
