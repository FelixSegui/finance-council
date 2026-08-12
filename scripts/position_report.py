#!/usr/bin/env python3
"""
Per-position movement report — "how are my positions actually behaving?"

Reads data/portfolio.json plus the two most recent snapshots in
data/cache/snapshots/ and prints one row per holding: current price, move since
the previous snapshot, move since cost basis, and where the price sits in
its 52-week range.

Design rule, same as every other script here: this file NEVER invents a
number. A position with no fetched price and no user-relayed value shows
"no data" — it does not fall back to a stale figure silently. Where a
figure is user-relayed rather than fetched, the row says so, because those
two things have very different reliability and the memo must not blur them.

Usage:
    python scripts/position_report.py                 # latest 2 snapshots
    python scripts/position_report.py --out FILE      # also write markdown
"""

import argparse
import json
import os
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP_DIR = os.path.join(ROOT, "data", "cache", "snapshots")


def load_json(path):
    with open(path) as fh:
        return json.load(fh)


def latest_snapshots(n=2):
    """Return the n most recent snapshots, newest first."""
    files = sorted(f for f in os.listdir(SNAP_DIR) if f.endswith(".json"))
    return [(f, load_json(os.path.join(SNAP_DIR, f))) for f in files[-n:][::-1]]


def pct(new, old):
    if new is None or old in (None, 0):
        return None
    return (new - old) / old * 100.0


def fmt_pct(v, signed=True):
    if v is None:
        return "no data"
    return f"{v:+.1f}%" if signed else f"{v:.1f}%"


def fmt_num(v):
    if v is None:
        return "no data"
    return f"{v:,.2f}"


def range_position(price, low, high):
    """Where in the 52-week range the price sits, 0% = at low, 100% = at high."""
    if None in (price, low, high) or high == low:
        return None
    return (price - low) / (high - low) * 100.0


def equity_row(h, cur_snap, prev_snap):
    """Build a row for a holding that has a real, fetchable ticker."""
    t = h["ticker"]
    cur = (cur_snap.get("equities") or {}).get(t, {})
    prev = (prev_snap or {}).get("equities", {}).get(t, {}) if prev_snap else {}

    if "error" in cur or not cur.get("price"):
        return {
            "name": h.get("name", t),
            "ticker": t,
            "price": None,
            "since_prev": None,
            "since_cost": None,
            "range_pos": None,
            "value": h.get("market_value_sek"),
            "source": "FETCH FAILED" if "error" in cur else "no price",
            "note": cur.get("error", "")[:80] if "error" in cur else "",
        }

    price = cur.get("price")
    qty = h.get("quantity")
    cost = h.get("cost_basis_per_unit")

    return {
        "name": h.get("name", t),
        "ticker": t,
        "price": price,
        "since_prev": pct(price, prev.get("price")) if prev.get("price") else None,
        "since_cost": pct(price, cost),
        "range_pos": range_position(price, cur.get("52w_low"), cur.get("52w_high")),
        "value": price * qty if (qty is not None) else h.get("market_value_sek"),
        "source": "fetched",
        "note": "",
    }


def spot_crypto_row(h, cur_snap, prev_snap):
    """Row for a self-custody crypto holding (e.g. the ETH wallet) - priced
    from the snapshot's crypto block, not from a stale book value. Mirrors
    equity_row's shape/fields so the table renders identically either way."""
    coin_id = h["ticker"]  # e.g. "ethereum" - a CoinGecko id, not a ticker symbol
    cur_c = (cur_snap.get("crypto") or {}).get(coin_id)
    prev_c = ((prev_snap or {}).get("crypto") or {}).get(coin_id) if prev_snap else None
    sek_per_eur = (cur_snap.get("macro") or {}).get("sek_per_eur", {}).get("value")

    if not cur_c or cur_c.get("price_eur") is None or sek_per_eur is None:
        return {
            "name": h.get("name", coin_id),
            "ticker": coin_id,
            "price": None,
            "since_prev": None,
            "since_cost": None,
            "range_pos": None,
            "value": h.get("market_value_sek"),
            "source": "no crypto price in snapshot",
            "note": "run market-data with --crypto to include this coin",
        }

    qty = h.get("quantity")
    price_sek = cur_c["price_eur"] * sek_per_eur
    cost = h.get("cost_basis_per_unit")

    prev_price_sek = None
    if prev_c and prev_c.get("price_eur") is not None:
        prev_sek_per_eur = (prev_snap.get("macro") or {}).get("sek_per_eur", {}).get("value")
        if prev_sek_per_eur is not None:
            prev_price_sek = prev_c["price_eur"] * prev_sek_per_eur

    return {
        "name": h.get("name", coin_id),
        "ticker": coin_id,
        "price": price_sek,
        "since_prev": pct(price_sek, prev_price_sek),
        "since_cost": pct(price_sek, cost),
        "range_pos": None,  # no 52-week high/low tracked for spot crypto in this snapshot
        "value": price_sek * qty if qty is not None else h.get("market_value_sek"),
        "source": "fetched (CoinGecko, converted via sek_per_eur)",
        "note": "",
    }


def manual_row(h):
    """Row for a holding priced by the user or carried at book value."""
    val = h.get("market_value_sek")
    cost_total = h.get("cost_basis_total_sek")
    cost_unit = h.get("cost_basis_per_unit")
    qty = h.get("quantity")

    if cost_total is None and None not in (cost_unit, qty):
        cost_total = cost_unit * qty

    user_priced = bool(h.get("market_value_source"))
    return {
        "name": h.get("name", h.get("ticker", "?")),
        "ticker": h.get("ticker", "-"),
        "price": None,
        "since_prev": None,
        "since_cost": pct(val, cost_total) if val is not None else None,
        "range_pos": None,
        "value": val,
        "source": "user-relayed" if user_priced else "book value",
        "note": "" if user_priced else "no live feed",
    }


def crypto_proxy_note(cur_snap, prev_snap):
    """BTC/ETH moves — context for crypto positions, incl. the certificate proxy."""
    out = []
    cur_c = cur_snap.get("crypto") or {}
    prev_c = (prev_snap or {}).get("crypto", {}) if prev_snap else {}
    for coin in ("bitcoin", "ethereum"):
        c = cur_c.get(coin)
        if not c:
            continue
        out.append({
            "coin": coin,
            "price_eur": c.get("price_eur"),
            "since_prev": pct(c.get("price_eur"), (prev_c.get(coin) or {}).get("price_eur")),
            "d7": c.get("change_7d_pct"),
            "d30": c.get("change_30d_pct"),
            "off_ath": c.get("ath_change_pct"),
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="also write the markdown report to this path")
    args = ap.parse_args()

    pf = load_json(os.path.join(ROOT, "data", "portfolio.json"))
    snaps = latest_snapshots(2)
    if not snaps:
        raise SystemExit("no snapshots found — run fetch_market_data.py first")

    cur_name, cur_snap = snaps[0]
    prev_name, prev_snap = snaps[1] if len(snaps) > 1 else (None, None)

    rows = []
    for h in pf.get("holdings", []):
        # Skip things that are not investments: cash, operating accounts,
        # and the frozen/unsellable SEB fund (nothing to report, no action possible).
        if h.get("instrument_type") == "cash":
            continue
        if h.get("exposure_class") == "excluded_operating_cash":
            continue
        if h.get("quantity") == 0:
            continue  # closed positions
        if "FROZEN" in (h.get("name") or "").upper():
            continue

        ticker = h.get("ticker", "")
        has_real_ticker = ticker not in ("TBD", "", None) and "CASH_" not in ticker
        is_fetchable = has_real_ticker and ticker in (cur_snap.get("equities") or {})

        if h.get("instrument_type") == "spot_crypto":
            rows.append(spot_crypto_row(h, cur_snap, prev_snap))
        elif is_fetchable:
            rows.append(equity_row(h, cur_snap, prev_snap))
        else:
            rows.append(manual_row(h))

    lines = []
    lines.append(f"## Position report — {datetime.utcnow().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"Snapshot: `{cur_name}`" + (f" · previous: `{prev_name}`" if prev_name else ""))
    lines.append("")
    lines.append("| Position | Price | Δ vs prev snapshot | Δ vs cost | 52w range | Value (SEK) | Source |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in rows:
        rng = f"{r['range_pos']:.0f}%" if r["range_pos"] is not None else "-"
        lines.append(
            f"| {r['name']} | {fmt_num(r['price'])} | {fmt_pct(r['since_prev'])} | "
            f"{fmt_pct(r['since_cost'])} | {rng} | {fmt_num(r['value'])} | {r['source']} |"
        )

    lines.append("")
    lines.append("*52w range: 0% = at the 52-week low, 100% = at the 52-week high.*")
    lines.append("")

    proxies = crypto_proxy_note(cur_snap, prev_snap)
    if proxies:
        lines.append("### Crypto context (spot, from CoinGecko)")
        lines.append("")
        lines.append("| Coin | Price (EUR) | Δ vs prev snapshot | 7d | 30d | vs ATH |")
        lines.append("|---|---|---|---|---|---|")
        for p in proxies:
            lines.append(
                f"| {p['coin']} | {fmt_num(p['price_eur'])} | {fmt_pct(p['since_prev'])} | "
                f"{fmt_pct(p['d7'])} | {fmt_pct(p['d30'])} | {fmt_pct(p['off_ath'])} |"
            )
        lines.append("")
        lines.append("*Bitcoin is the agreed directional proxy for the XBT certificate, "
                     "which has no working ticker. It indicates direction, not the "
                     "certificate's actual price — that comes from the user.*")

    report = "\n".join(lines)
    print(report)
    if args.out:
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        with open(args.out, "w") as fh:
            fh.write(report + "\n")
        print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
