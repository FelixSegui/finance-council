#!/usr/bin/env python3
"""
One-time migration: add the structured thesis schema (spec section 18 of
docs/v2-upgrade-spec.md) to every ACTIVE holding in data/portfolio.json.
The existing free-text `thesis` field is preserved verbatim as
`thesis_narrative` - nothing is deleted.

New fields per holding: thesis_status, why_owned, expected_driver,
valuation_reason, key_risks, break_conditions, last_reviewed.

Status values: INTACT / WEAKENING / BROKEN / UNTESTED / TOO_EARLY.

WHY THIS IS HARDCODED, NOT AUTO-PARSED: the existing `thesis` strings are
free prose, and turning them into honest structured fields (especially
`thesis_status`) requires actually knowing what this session's real
Council/thesis-review runs concluded - guessing via regex on the prose
would produce plausible-looking garbage, exactly the failure mode this
whole system exists to avoid. The mapping below is transcribed from the
2026-08-06 sweep's actual thesis-review and Council outputs
(reports/2026-08-06-council-memo.md), not invented.

Holdings NOT touched (skip list, and why):
  - CASH_* / CASH_EUR / CASH_USD entries: not investments, no thesis applies.
  - Tundra Sustainable Frontier Fund A SEK: quantity 0 (sold 2026-07-28),
    not an active position.
  - SEB Osteuropafond: frozen/unsellable, not an active decision.

Usage:
  python scripts/migrate_thesis_schema.py --dry-run
  python scripts/migrate_thesis_schema.py
"""
import argparse
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_PATH = os.path.join(ROOT, "data", "portfolio.json")
REVIEWED = "2026-08-06"

# Keyed by (ticker, name) - some tickers (TBD) repeat across distinct funds,
# so ticker alone isn't a safe key (see import_excel_holdings.py's
# _match_key, same problem, same fix).
THESIS_UPDATES = {
    ("SHB-A.ST", "Handelsbanken A (stock)"): {
        "thesis_status": "WEAKENING",
        "why_owned": "Bought without comparing alternatives - user's own stated rationale: "
                     "'good track record', 'secure/stable' pick with 'good upside'.",
        "expected_driver": "Continued stability as a low-beta Nordic bank with a ~5.4% dividend.",
        "valuation_reason": "Trailing P/E ~12x looked reasonable for a bank at purchase.",
        "key_risks": "Revenue declining (-3.8% YoY), analyst consensus 'underperform', PEG ~20x; "
                     "heavy insider buying (Chairman + board member, >750M SEK) contradicts the "
                     "fundamentals read - unresolved tension, not averaged away.",
        "break_conditions": "Revenue decline continues another quarter with no fundamentals offset "
                            "-> treat as a rotation candidate, not a conviction add.",
    },
    ("INVE-A.ST", "Investor A (stock)"): {
        "thesis_status": "WEAKENING",
        "why_owned": "Bought without comparing alternatives - same rationale as SHB-A.ST: "
                     "'good track record', 'stable with upside'.",
        "expected_driver": "Diversified holding-company exposure with steady NAV growth.",
        "valuation_reason": "P/E ~5-7x is a holding-company accounting artifact, NOT a cheap signal - "
                            "never properly testable on valuation since NAV discount/premium has never "
                            "been obtained (OPEN_ITEMS.md S6).",
        "key_risks": "Price now within 0.5% of its 52-week high - the 'good upside' the user cited "
                     "has already been captured. No NAV discount data to confirm it's still attractive.",
        "break_conditions": "No further re-rating expected without a resolved NAV discount/premium "
                            "figure -> rotation candidate rather than an add.",
    },
    ("VOLV-B.ST", "Volvo B"): {
        "thesis_status": "TOO_EARLY",
        "why_owned": "Part of the 2026-08-03 medium-tier build; bought explicitly into an unresolved "
                     "tension (2yr revenue decline -13%, D/E 147) vs. a large single-insider purchase "
                     "(board member ~1.3M shares at ~360 SEK).",
        "expected_driver": "A cyclical/earnings recovery consistent with the insider's large purchase; "
                           "forward P/E 14.6/PEG 1.49 already prices some of this in.",
        "valuation_reason": "Forward multiple attractive if the recovery shows up; trailing multiple "
                            "(20.6x) still reflects the decline.",
        "key_risks": "Revenue decline continuing, leverage remaining elevated, no recovery materializing.",
        "break_conditions": "3+ months with no sign of the expected earnings recovery -> re-test; a "
                            "further leg down in revenue -> weakening.",
    },
    ("ATCO-B.ST", "Atlas Copco B"): {
        "thesis_status": "UNTESTED",
        "why_owned": None, "expected_driver": None, "valuation_reason": None, "key_risks": None,
        "break_conditions": "No thesis on record - per the 2026-08-06 Council call A, write one before "
                            "the next sweep or this becomes a rotation candidate.",
    },
    ("ALFA.ST", "Alfa Laval"): {
        "thesis_status": "UNTESTED",
        "why_owned": None, "expected_driver": None, "valuation_reason": None, "key_risks": None,
        "break_conditions": "No thesis on record - per the 2026-08-06 Council call A, write one before "
                            "the next sweep or this becomes a rotation candidate.",
    },
    ("ABB.ST", "ABB"): {
        "thesis_status": "UNTESTED",
        "why_owned": None, "expected_driver": None, "valuation_reason": None, "key_risks": None,
        "break_conditions": "No thesis on record - per the 2026-08-06 Council call A, write one before "
                            "the next sweep or this becomes a rotation candidate.",
    },
    ("AZN.ST", "AstraZeneca"): {
        "thesis_status": "INTACT",
        "why_owned": "Historically resilient, defensive quality company; healthcare is lower-beta than "
                     "high-valuation tech/growth; reasonable dividend history; diversifies away from "
                     "the portfolio's industrials/technology concentration.",
        "expected_driver": "Continued defensive resilience and dividend income over a 3-5 year horizon, "
                           "especially if high-valuation growth assets correct.",
        "valuation_reason": "PEG 1.33 (2026-08-06) is attractive for a large-cap pharma; priced ~20% "
                            "off its 52-week high despite intact margins and 4 straight years of rising "
                            "revenue.",
        "key_risks": "Revenue growth or margins deteriorate structurally; the dividend is cut; or it "
                     "re-rates to trade at a premium indistinguishable from the growth assets it's meant "
                     "to diversify against.",
        "break_conditions": "Any of the three key_risks above -> re-test the thesis.",
    },
    ("TBD", "Avanza Auto 3 (fund)"): {
        "thesis_status": "INTACT",
        "why_owned": "Diversified core multi-asset fund (~60% equity, 40-70% range), fits the 'secure' "
                     "risk tier.",
        "expected_driver": "Broad, low-fee diversified growth in line with the fund's stated allocation band.",
        "valuation_reason": "Not applicable - evaluated on cost (0.39%/yr) and diversification, not P/E.",
        "key_risks": "Fee (0.39%/yr) is higher than Avanza Global's 0.10%/yr but still under the 0.4% cap.",
        "break_conditions": "A structurally cheaper equivalent core holding becomes available with the "
                            "same diversification profile.",
    },
    ("COIN-XBT.ST", "CoinShares XBT Provider Bitcoin Tracker One (certificate)"): {
        "thesis_status": "WEAKENING",
        "why_owned": "User's original thesis: BTC 'pretty low valued', 2028 halving ahead, "
                     "'positive buy-in signals now'.",
        "expected_driver": "BTC cycle appreciation ahead of the 2028 halving.",
        "valuation_reason": "BTC still -48.2% off its ATH (2026-08-06) - the 'cheap vs history' leg "
                            "still holds directionally.",
        "key_risks": "Position already +26-29% vs cost basis; crypto Fear&Greed at 25 ('Extreme Fear') "
                     "makes the original 'positive buy-in signal' framing harder to sustain than at "
                     "purchase; 2.5%/yr fee (P4, pending a cheaper certificate).",
        "break_conditions": "Still above 12% of investable capital at the 2026-09-03 sweep -> trim "
                            "(per the 2026-08-06 Council trip-wire), replacing 'let it dilute'.",
    },
    ("TBD", "Avanza Global (fund)"): {
        "thesis_status": "INTACT",
        "why_owned": "Broad, cheap (0.10%/yr) global index exposure - the structural core-equity holding.",
        "expected_driver": "Market-return equity growth, broadly diversified.",
        "valuation_reason": "Not applicable - evaluated on cost and diversification, not P/E. Cheapest "
                            "holding in the portfolio.",
        "key_risks": "None specific to this holding beyond broad market risk.",
        "break_conditions": "None identified - this is the core structural holding, not a tactical position.",
    },
    ("ethereum", "ETH (self-custody wallet)"): {
        "thesis_status": "UNTESTED",
        "why_owned": None, "expected_driver": None, "valuation_reason": None, "key_risks": None,
        "break_conditions": "No thesis after 10+ sweeps (OPEN_ITEMS.md P5) - the blocker is genuinely "
                            "the user, not data. One sentence is enough: 'diversification, hold 3+ "
                            "years, sell if X.'",
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(PORTFOLIO_PATH) as f:
        pf = json.load(f)

    touched = []
    for h in pf.get("holdings", []):
        key = (h.get("ticker"), h.get("name"))
        if key not in THESIS_UPDATES:
            continue
        if "thesis_narrative" in h:
            continue  # already migrated
        h["thesis_narrative"] = h.pop("thesis", None)
        h["last_reviewed"] = REVIEWED
        h.update(THESIS_UPDATES[key])
        touched.append(key)

    print(f"{'[dry-run] ' if args.dry_run else ''}{len(touched)} holding(s) migrated:")
    for t in touched:
        print(f"  {t[0]:<14s} {t[1]}")

    if not args.dry_run and touched:
        with open(PORTFOLIO_PATH, "w") as f:
            json.dump(pf, f, indent=2)
            f.write("\n")
    elif args.dry_run:
        print("\n--dry-run: nothing written.")


if __name__ == "__main__":
    main()
