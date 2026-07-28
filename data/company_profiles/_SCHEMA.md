# Company profile cache — schema and purpose

One file per ticker: `data/company_profiles/<TICKER>.json`. This is a cache
of information that does NOT change monthly — the `swedish-equity-review`
skill checks here FIRST and only asks the user (or re-fetches) for fields
that are missing or past their stated validity window. Purpose: stop
re-asking for a quarterly report's numbers every month, and stop re-reading
long PDF-extracted content when a short structured cache already has it.

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
    "source": "Q2 2026 kvartalsrapport (user-provided PDF) | Avanza Nyckeltal page | ...",
    "as_of_period": "Q2 2026",
    "extracted_date": "2026-07-28",
    "next_report_expected": "~2026-10-20 (Q3 2026, per company's usual reporting calendar - estimate, confirm each cycle)",
    "figures": {
      "ebit_margin_pct": null,
      "roic_pct": null,
      "roe_pct": null,
      "revenue_growth_pct": null,
      "fcf_sek": null,
      "net_debt_to_ebitda": null,
      "payout_ratio_pct": null
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
