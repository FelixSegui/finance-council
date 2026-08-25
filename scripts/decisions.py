#!/usr/bin/env python3
"""
THE DECISION LEDGER — every recommendation the system makes, recorded at the
moment it is made, with the evidence it was made on.

Why this file exists: without it the system cannot answer "is it any good?"
Memos are prose, they scroll away, and a memo written after the fact will
always sound more coherent than the decision felt. The ledger is the opposite:
a flat, boring row per pick, written before the outcome is known.

    data/decisions.csv     one row per (sweep, voice, ticker, action)

**The metrics are JOINED, never typed.** `record` takes a small picks file
from `council` — voice, ticker, action, conviction, one-line thesis — and
joins price, currency, screen status, lens scores and rank from that sweep's
own `data/screens/<ts>-candidates.csv`. An LLM re-typing numbers into a
ledger is a transcription-error surface, and a ledger with a wrong entry price
silently corrupts every performance number computed from it forever.

`voice` is one of the seven Council voices, or `chairman` for the final call.
Both are recorded: the point is to find out whether the Chairman's synthesis
beats its own inputs, which is the only honest basis for ever weighting the
Council.

Usage:
  python scripts/decisions.py record --picks data/picks/2026-08-25-picks.csv
  python scripts/decisions.py status AZN.ST --set executed --note "bought 3 @ 1560"
  python scripts/decisions.py open            # what is still awaiting action
  python scripts/decisions.py template        # print the picks-file header
"""
import argparse
import csv
import glob
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER_PATH = os.path.join(ROOT, "data", "decisions.csv")
SCREENS_DIR = os.path.join(ROOT, "data", "screens")

VOICES = ["fundamental", "valuation", "growth", "defensive", "contrarian",
          "macro", "copycat", "chairman"]
ACTIONS = ["BUY", "SELL", "HOLD-WATCH", "NO_ACTION"]
STATUSES = ["open", "executed", "declined", "expired"]

# What council writes. Deliberately tiny — everything else is joined.
PICKS_COLUMNS = ["voice", "ticker", "action", "conviction", "confidence",
                 "horizon", "thesis"]

LEDGER_COLUMNS = [
    "decided_utc", "sweep_csv", "voice", "ticker", "action", "conviction",
    "confidence", "horizon",
    # --- joined from the mechanical sweep, never typed by an agent ---
    "source", "screen_status", "best_lens", "rank", "entry_price", "currency",
    "sector", "country", "pe", "fwd_pe", "peg", "roic_pct", "margin_pct",
    "de_ratio", "rev_growth_pct", "fcf_yield_pct", "div_yield_pct", "beta",
    "pct_52w_range", "thin_lenses",
    # --- the human's side ---
    "thesis", "status", "status_date", "status_note",
]

# Metric columns copied verbatim from the candidates CSV.
JOINED_METRICS = ["source", "screen_status", "best_lens", "rank", "sector",
                  "country", "currency", "pe", "fwd_pe", "peg", "roic_pct",
                  "margin_pct", "de_ratio", "rev_growth_pct", "fcf_yield_pct",
                  "div_yield_pct", "beta", "pct_52w_range", "thin_lenses"]


def latest_candidates_csv(screens_dir=None):
    files = sorted(glob.glob(os.path.join(screens_dir or SCREENS_DIR,
                                          "*-candidates.csv")))
    return files[-1] if files else None


def load_candidates(path):
    with open(path, newline="") as f:
        return {r["ticker"]: r for r in csv.DictReader(f)}


def load_ledger(path=None):
    path = path or LEDGER_PATH
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def save_ledger(rows, path=None):
    path = path or LEDGER_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=LEDGER_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in LEDGER_COLUMNS})
    return path


def read_picks(picks_path):
    with open(picks_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    missing = [c for c in ("voice", "ticker", "action") if rows and c not in rows[0]]
    if missing:
        raise ValueError(f"picks file is missing required column(s): {missing}. "
                         f"Expected header: {','.join(PICKS_COLUMNS)}")
    return rows


def record(picks_path, candidates_path=None, ledger_path=None, dry_run=False):
    """Append this sweep's picks to the ledger, joining the evidence.

    Refuses a pick for a ticker that was not in the sweep's candidate set —
    that means a voice invented a name outside the funnel, which is exactly
    the LLM stock-picking the system is built to prevent, and it must surface
    as an error rather than a quietly unverifiable ledger row."""
    candidates_path = candidates_path or latest_candidates_csv()
    if not candidates_path:
        raise SystemExit("No candidates CSV found in data/screens/ — run "
                         "`python scripts/scout.py` before recording decisions.")
    candidates = load_candidates(candidates_path)
    picks = read_picks(picks_path)

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    new_rows, problems = [], []
    for p in picks:
        ticker = (p.get("ticker") or "").strip()
        voice = (p.get("voice") or "").strip().lower()
        action = (p.get("action") or "").strip().upper()
        if not ticker:
            continue
        if voice not in VOICES:
            problems.append(f"{ticker}: unknown voice {voice!r} (expected one of {VOICES})")
            continue
        if action not in ACTIONS:
            problems.append(f"{ticker}: unknown action {action!r} (expected one of {ACTIONS})")
            continue
        cand = candidates.get(ticker)
        if cand is None:
            problems.append(f"{ticker}: not in {os.path.basename(candidates_path)} — a pick "
                            f"outside the funnel's candidate set cannot be evidenced")
            continue
        row = {
            "decided_utc": now,
            "sweep_csv": os.path.basename(candidates_path),
            "voice": voice, "ticker": ticker, "action": action,
            "conviction": (p.get("conviction") or "").strip(),
            "confidence": (p.get("confidence") or "").strip(),
            "horizon": (p.get("horizon") or "").strip(),
            "entry_price": cand.get("price", ""),
            "thesis": (p.get("thesis") or "").strip()[:300],
            "status": "open", "status_date": "", "status_note": "",
        }
        for m in JOINED_METRICS:
            row[m] = cand.get(m, "")
        new_rows.append(row)

    if problems:
        raise SystemExit("Refusing to record — fix these first:\n  "
                         + "\n  ".join(problems))
    if dry_run:
        return new_rows
    rows = load_ledger(ledger_path) + new_rows
    save_ledger(rows, ledger_path)
    return new_rows


def set_status(ticker, status, note=None, voice="chairman", ledger_path=None):
    """Mark the Chairman's call on a ticker executed / declined / expired.

    Only the newest open row for that ticker is touched — a later sweep
    re-recommending the same name is a separate decision with its own outcome,
    and collapsing them would hide exactly the repeat-recommendation pattern
    worth seeing."""
    if status not in STATUSES:
        raise SystemExit(f"status must be one of {STATUSES}")
    rows = load_ledger(ledger_path)
    matches = [r for r in rows
               if r["ticker"] == ticker and r["voice"] == voice
               and r.get("status") == "open"]
    if not matches:
        raise SystemExit(f"No open {voice} decision for {ticker}.")
    target = matches[-1]
    target["status"] = status
    target["status_date"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    target["status_note"] = note or ""
    save_ledger(rows, ledger_path)
    return target


def open_decisions(ledger_path=None, action="BUY"):
    rows = load_ledger(ledger_path)
    return [r for r in rows
            if r["voice"] == "chairman" and r.get("status") == "open"
            and (action is None or r["action"] == action)]


BASIS_METRICS = [
    ("pe", "P/E"), ("fwd_pe", "fwdP/E"), ("peg", "PEG"),
    ("roic_pct", "ROIC%"), ("margin_pct", "Marg%"), ("de_ratio", "D/E"),
    ("net_debt_to_ebitda", "ND/EB"), ("rev_growth_pct", "Rev%"),
    ("fcf_yield_pct", "FCF%"), ("div_yield_pct", "Div%"),
    ("beta", "Beta"), ("pct_52w_range", "52w%"),
]


def basis(candidates_path=None, ledger_path=None, sweep_csv=None):
    """"What did the system actually decide on?" — one table, every name the
    Council surfaced, the voices that picked it, and the metrics behind it.

    Two modes, both useful:
      * before council runs — the focus set with its metrics, so the mechanical
        sweep can be checked on its own before any judgement is layered on it
      * after council runs  — the same table with each voice's picks attached,
        so overlap between voices is visible and every pick can be traced to
        the numbers it was made on

    The metrics come from the sweep's candidates CSV, the same file the voices
    read. If a figure looks wrong here, the screen is wrong — not the memo.
    """
    candidates_path = candidates_path or latest_candidates_csv()
    if not candidates_path:
        raise SystemExit("No candidates CSV in data/screens/.")
    candidates = load_candidates(candidates_path)
    sweep_csv = sweep_csv or os.path.basename(candidates_path)

    ledger = [r for r in load_ledger(ledger_path) if r.get("sweep_csv") == sweep_csv]
    picks = {}
    for r in ledger:
        if r["action"] in ("BUY", "SELL"):
            picks.setdefault(r["ticker"], []).append(
                (r["voice"], r["action"], r.get("conviction") or "?"))

    if picks:
        tickers = sorted(picks, key=lambda t: (-len(picks[t]), t))
        title = (f"Picked names for {sweep_csv} — {len(tickers)} names across "
                 f"{len({v for ps in picks.values() for v, _a, _c in ps})} voices")
    else:
        tickers = [t for t, c in candidates.items() if c.get("focus") == "Y"]
        tickers.sort(key=lambda t: int(candidates[t].get("rank") or 10**6))
        title = (f"Focus set for {sweep_csv} — {len(tickers)} names "
                 f"(no council picks recorded for this sweep yet)")

    lines = [f"# Decision basis — {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             "", title, "",
             "Every figure below is copied from the mechanical sweep "
             f"(`data/screens/{sweep_csv}`), not re-derived. A blank cell means the "
             "value was genuinely unavailable — never zero, never estimated.", ""]

    head = (f"| {'Ticker':<12} | {'Src':<9} | {'Scr':<7} | "
            + " | ".join(f"{lbl:>6}" for _f, lbl in BASIS_METRICS) + " | Picked by |")
    lines.append(head)
    lines.append("|" + "|".join(["-" * (len(c) + 2) for c in
                                 ["x" * 12, "x" * 9, "x" * 7]
                                 + ["x" * 6] * len(BASIS_METRICS) + ["x" * 9]]) + "|")
    for t in tickers:
        c = candidates.get(t, {})
        cells = []
        for fld, _lbl in BASIS_METRICS:
            v = c.get(fld) or ""
            cells.append(f"{v[:6]:>6}")
        who = ", ".join(f"{v}({a[0]}{cv})" for v, a, cv in picks.get(t, [])) or "-"
        lines.append(f"| {t:<12} | {(c.get('source') or ''):<9} | "
                     f"{(c.get('screen_status') or ''):<7} | " + " | ".join(cells)
                     + f" | {who} |")

    gaps = []
    for fld, lbl in BASIS_METRICS:
        miss = [t for t in tickers if not candidates.get(t, {}).get(fld)]
        if miss:
            gaps.append(f"- **{lbl}** missing on {len(miss)}/{len(tickers)}: "
                        f"{', '.join(miss[:8])}")
    lines += ["", "## Where the evidence was thin", ""]
    lines += gaps or ["- Nothing missing: every name above carries every tracked metric."]

    thin = [(t, candidates[t]["thin_lenses"]) for t in tickers
            if candidates.get(t, {}).get("thin_lenses")]
    if thin:
        lines += ["", "Lens scores resting on partial inputs (already shrunk toward "
                  "neutral, listed so the discount is visible):", ""]
        lines += [f"- {t}: {v}" for t, v in thin]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("record", help="append a sweep's picks to the ledger")
    r.add_argument("--picks", required=True)
    r.add_argument("--candidates", default=None,
                   help="candidates CSV to join from (default: newest in data/screens/)")
    r.add_argument("--dry-run", action="store_true")

    st = sub.add_parser("status", help="mark a Chairman call executed/declined/expired")
    st.add_argument("ticker")
    st.add_argument("--set", dest="status", required=True, choices=STATUSES)
    st.add_argument("--note")

    o = sub.add_parser("open", help="Chairman calls still awaiting action")
    o.add_argument("--action", default="BUY", choices=ACTIONS + ["ALL"])

    sub.add_parser("template", help="print the picks-file header for council")

    b = sub.add_parser("basis", help="the metrics behind this sweep's picks")
    b.add_argument("--write", action="store_true",
                   help="write reports/<date>-decision-basis.md as well")

    args = p.parse_args()

    if args.cmd == "record":
        rows = record(args.picks, args.candidates, dry_run=args.dry_run)
        by_voice = {}
        for row in rows:
            by_voice.setdefault(row["voice"], []).append(row["ticker"])
        print(f"{'Would record' if args.dry_run else 'Recorded'} {len(rows)} pick(s) "
              f"into {LEDGER_PATH}")
        for v in VOICES:
            if v in by_voice:
                print(f"  {v:<13} {', '.join(by_voice[v])}")
    elif args.cmd == "status":
        row = set_status(args.ticker, args.status, args.note)
        print(f"{args.ticker}: {row['action']} -> {row['status']} "
              f"(recorded {row['decided_utc'][:10]}, entry {row['entry_price']})")
    elif args.cmd == "open":
        rows = open_decisions(action=None if args.action == "ALL" else args.action)
        if not rows:
            print("No open Chairman decisions.")
            return
        print(f"{'TICKER':<12}{'ACTION':<12}{'CONV':>5}{'DECIDED':>13}{'AGE':>6}  THESIS")
        today = datetime.now(timezone.utc).date()
        for r in rows:
            decided = r["decided_utc"][:10]
            age = (today - datetime.strptime(decided, "%Y-%m-%d").date()).days
            print(f"{r['ticker']:<12}{r['action']:<12}{r['conviction']:>5}"
                  f"{decided:>13}{age:>5}d  {r['thesis'][:52]}")
    elif args.cmd == "basis":
        text = basis()
        print(text)
        if args.write:
            out = os.path.join(ROOT, "reports",
                               f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
                               f"-decision-basis.md")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, "w") as f:
                f.write(text + "\n")
            print(f"\nWrote {out}")
    elif args.cmd == "template":
        print(",".join(PICKS_COLUMNS))
        print("valuation,AZN.ST,BUY,8,,Long,one-line reason specific to this sweep")
        print("chairman,AZN.ST,BUY,8,High,Long,the final call")


if __name__ == "__main__":
    main()
