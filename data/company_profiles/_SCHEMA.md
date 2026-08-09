# Company profile cache — schema and purpose

One file per ticker: `data/company_profiles/<TICKER>.json`. This is a cache
of information that does NOT change monthly — the `swedish-equity-review`
skill checks here FIRST and only asks the user (or re-fetches) for fields
that are missing or past their stated validity window. Purpose: stop
re-asking for a quarterly report's numbers every month, and stop re-reading
long PDF-extracted content when a short structured cache already has it.

## Per-field structured values (added 2026-08-09)

Every entry in `fundamentals_cache.figures` is an object, not a bare
number:
```json
"roic_pct": {
  "value": 0.206,
  "source": "computed (derived_metrics.roic)",
  "source_tier": 3,
  "as_of": "2026-08-09",
  "age_days": 0,
  "quality_state": "ESTIMATED",
  "calculation_method": "ebit*(1-tax_rate)/invested_capital, tax_rate=0.147 (assumed statutory rate for Switzerland, NOT a real effective rate)"
}
```
This replaced a flat `{"roic_pct": null, ...}` convention that had drifted
in practice — different writers (the Excel importer vs. the direct-fetch
path) were populating different, inconsistently-named key sets in the same
file, and the schema's own canonical fields sat null in every real profile
because nothing computed them. See `scripts/migrate_company_profile_schema.py`
for the one-time conversion of pre-2026-08-09 files.

**`quality_state`** (one of):
- `OK` — a real, current, trustworthy value.
- `STALE` — real but past its useful age (see `age_days`).
- `MISSING` — genuinely not available from any wired-up source; `value` is
  `null`. Never leave a field silently absent instead of present-with-MISSING
  — the state itself is the signal something needs a better source.
- `SUSPECT` — present but implausible (e.g. Atlas Copco's Excel-sourced P/E
  of 2.05 against a real ~33.7x) — kept, not dropped, so the contradiction
  stays visible, but never used for a decision without flagging it.
- `CONFLICTING` — two sources disagree and neither is clearly authoritative
  by source tier.
- `ESTIMATED` — a real calculation, but built on an assumption a genuine
  source would replace (e.g. `roic_pct` above, built on an assumed
  statutory tax rate because no effective rate exists in any fetched
  source). Distinct from `SUSPECT`: an ESTIMATED value is honestly labeled
  as an approximation by design, not a probably-wrong number.

**`source_tier`** (1 = highest confidence):
1. Company filings / official investor relations.
2. A reliable structured market-data provider (e.g. a real-time API).
3. Excel's Stocks data type (Microsoft 365/LSEG) or this pipeline's own
   Yahoo `quoteSummary` fetch.
4. Secondary financial websites.
5. User-provided/user-relayed data (accepted for reconciliation, always
   marked as such — never silently promoted to a higher tier).

A lower tier is not "don't use it" — it's "know how much confidence this
number earns." The Council and thesis-review agents should weight a Tier 1
figure over a Tier 4 one when the two disagree, not average them.

## Shape

```json
{
  "ticker": "SHB-A.ST",
  "name": "Handelsbanken A",
  "profile_last_updated": "2026-07-28",

  "static_profile": {
    "business_description": "One paragraph, stable for years - what the company does.",
    "sector": "Financials",
    "competitive_moat_notes": "Durable, slow-changing observations - brand, scale, switching costs.",
    "management_notes": "Slow-changing - tenure, capital allocation track record.",
    "last_reviewed": "2026-07-28"
  },

  "fundamentals_cache": {
    "source": "Q2 2026 kvartalsrapport (user-provided PDF) | Avanza Nyckeltal page | Yahoo quoteSummary | ...",
    "as_of_period": "Q2 2026",
    "extracted_date": "2026-07-28",
    "next_report_expected": "~2026-10-20 (Q3 2026, per company's usual reporting calendar - estimate, confirm each cycle)",
    "figures": {
      "_comment": "Every value below is the per-field structured object described above, not a bare number.",
      "ebitda": { "value": null, "source": null, "source_tier": null, "as_of": null, "age_days": null, "quality_state": "MISSING", "calculation_method": "direct from source, not computed" },
      "total_cash": { "value": null, "quality_state": "MISSING", "...": "same shape" },
      "total_debt": { "value": null, "quality_state": "MISSING", "...": "same shape" },
      "operating_cashflow": { "value": null, "quality_state": "MISSING", "...": "same shape" },
      "capex": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.capex_from_ocf_fcf" },
      "ebit": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.ebit_from_margin - only when a real EBIT line isn't available" },
      "interest_expense": { "value": null, "quality_state": "MISSING", "calculation_method": "no wired source yet - needs a filing or PDF extract" },
      "equity_book": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.equity_from_book_value" },
      "invested_capital": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.invested_capital" },
      "roic_pct": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.roic - requires ebit, a tax rate, and invested_capital" },
      "fcf_margin_pct": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.fcf_margin" },
      "operating_margin_pct": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.operating_margin, or direct from source if a real one exists" },
      "net_debt_to_ebitda": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.net_debt_to_ebitda" },
      "interest_coverage": { "value": null, "quality_state": "MISSING", "calculation_method": "derived_metrics.interest_coverage - blocked until interest_expense has a real source" },
      "revenue_growth_pct": { "value": null, "quality_state": "MISSING" },
      "roe_pct": { "value": null, "quality_state": "MISSING" },
      "payout_ratio_pct": { "value": null, "quality_state": "MISSING" }
    }
  },

  "insider_activity_cache": {
    "source": "Finansinspektionen Insynsregister | user-relayed",
    "as_of_date": "2026-07-28",
    "notes": "Recent transactions, size, number of distinct insiders - see skill method for weighting."
  },

  "review_history": [
    { "date": "2026-07-28", "composite_score": null, "dimensions_scored": 0, "action": "not yet reviewed" }
  ]
}
```

## Rules for the skill when using this cache

- **Check before asking.** If `fundamentals_cache.next_report_expected` is
  in the future relative to today, reuse the cached figures - do not ask
  the user to re-supply them, do not re-parse a PDF already extracted.
- **Only refresh what's actually stale.** Price/momentum (fetched fresh
  each run) and insider activity (checked each run) are NOT the same
  refresh cadence as fundamentals (quarterly) or the static profile
  (rarely). Do not force a full re-ask just because it's a new month.
- **Keep `review_history` short** - one line per review (date, composite,
  dimensions scored, action). Do not let this become a prose log; that
  duplicates `reports/SESSION_LOG.md` and re-introduces the token cost
  this cache exists to avoid. Full reasoning for a given review lives in
  that review's own output/report, not duplicated here.
- **This file is a cache, not ground truth for holdings or targets** -
  `data/portfolio.json` remains the source of truth for what's actually
  held, quantities, and cost basis. This file only holds company-level
  research that doesn't depend on your specific position.
- **Never use a `SUSPECT` or `MISSING` value in a headline call without
  saying so.** A `quality_state` other than `OK` is not a reason to drop
  the field - it's the reason to flag it, exactly like the Atlas Copco
  P/E case. Silently filtering out anything non-OK would just recreate
  the false-precision problem this schema exists to prevent.
