#!/usr/bin/env python3
"""
One-time migration: convert every data/company_profiles/<TICKER>.json's
fundamentals_cache.figures from the old flat {"key": value_or_null} shape
to the new per-field structured shape documented in
data/company_profiles/_SCHEMA.md (added 2026-08-09).

Idempotent - a field that's already a structured dict (has a "value" key)
is left untouched, so this is safe to re-run.

Usage:
  python scripts/migrate_company_profile_schema.py --dry-run
  python scripts/migrate_company_profile_schema.py
"""
import argparse
import glob
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(ROOT, "data", "company_profiles")


def infer_source_tier(source_str):
    """Best-effort tier from the free-text fundamentals_cache.source field.
    Not a certainty - flagged clearly where the source is ambiguous, rather
    than defaulting to a confidence level the data hasn't earned."""
    if not source_str:
        return 4, "unknown legacy source - no fundamentals_cache.source recorded"
    s = source_str.lower()
    if "excel" in s and "stocks data type" in s:
        return 3, None
    if "yahoo" in s or "quotesummary" in s:
        return 2, None
    if "pdf" in s or "kvartalsrapport" in s or "arsredovisning" in s:
        return 1, None
    if "user" in s:
        return 5, None
    return 4, f"source string not recognized by the migration's tier inference: {source_str!r}"


def migrate_figures(figures, as_of, source_str):
    tier, tier_note = infer_source_tier(source_str)
    changed = 0
    for key, val in list(figures.items()):
        if isinstance(val, dict) and "value" in val:
            continue  # already migrated
        quality_state = "MISSING" if val is None else "OK"
        entry = {
            "value": val,
            "source": source_str or "unknown (pre-2026-08-09 file, no source recorded)",
            "source_tier": tier,
            "as_of": as_of,
            "age_days": None,
            "quality_state": quality_state,
            "calculation_method": "direct from source, not computed",
        }
        if tier_note:
            entry["migration_note"] = tier_note
        figures[key] = entry
        changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total_files, total_fields = 0, 0
    for path in sorted(glob.glob(os.path.join(PROFILES_DIR, "*.json"))):
        with open(path) as f:
            profile = json.load(f)
        fc = profile.get("fundamentals_cache", {})
        figures = fc.get("figures")
        if not figures:
            continue
        as_of = fc.get("extracted_date") or fc.get("as_of_period") or profile.get("profile_last_updated")
        changed = migrate_figures(figures, as_of, fc.get("source"))
        if changed:
            total_files += 1
            total_fields += changed
            print(f"{os.path.basename(path):<20s} {changed} field(s) migrated")
            if not args.dry_run:
                with open(path, "w") as f:
                    json.dump(profile, f, indent=2)
                    f.write("\n")

    print(f"\n{'[dry-run] ' if args.dry_run else ''}{total_files} file(s), {total_fields} field(s) total.")
    if args.dry_run:
        print("--dry-run: nothing written.")


if __name__ == "__main__":
    main()
