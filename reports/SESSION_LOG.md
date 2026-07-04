# Session Log

Append-only. The journal agent writes one entry per sweep; every new
session starts by reading the last two entries. Newest entry at the top.

Entry format:

```
## YYYY-MM-DD — <one-line summary>
- **Snapshot:** data/snapshots/<file>
- **Memo:** reports/<file> (or "no memo — reason")
- **Headline calls:** call → confidence (H/M/L) → horizon (S/M/L)
- **User decisions:** what you actually decided/did (or "none yet")
- **Reconciliation:** how last sweep's calls look against today's data
- **Open items carried forward:** ...
```

---

## 2026-07-04 — System build-out, no market sweep run
- **Snapshot:** none this session
- **Memo:** none — this session extended the system, it did not analyze markets
- **Headline calls:** n/a
- **User decisions:** approved adding scout/calendar/journal/backtest/meta agents, new data sources (Riksbank, ECB, SCB CPI, VIX, crypto Fear & Greed, SEC EDGAR insiders), and session-continuity logging. Later same day: provided Riksbank H2-2026 dates (calendar updated, IMPROVEMENTS #1 done); filled investor profile (max drawdown -30%, goal = house deposit 3-7y, contributions 1-3k SEK/mo, buffer 3-6mo — note the drawdown/deadline tension recorded in the profile); approved weekly automated sweep.
- **Reconciliation:** n/a — first entry
- **Infrastructure:** project moved to ~/Desktop/finance-council, now a git repo pushed to private GitHub FelixSegui/finance-council. Cloud routine "Finance Council weekly sweep" (trig_01XGYZrSEh1fETQDAPjrkYv5) runs Mondays 06:00 UTC and pushes results to main — PULL BEFORE LOCAL WORK, PUSH AFTER, or local and cloud will diverge.
- **Open items carried forward:**
  - All 5 `open_structural_questions` in portfolio.json remain open; #1 (Handelsbanken wrapper) still blocks and must lead every memo
  - portfolio.json holdings still have TBD tickers/quantities — itemize before portfolio agent output is meaningful; this is also why the first automated sweeps will be thin
  - investor_profile.json reference_targets still null — next Council sweep must PROPOSE a target allocation (glidepath for the 3-7y deposit deadline)
  - FOMC dates in macro_calendar.json need one-time verification (IMPROVEMENTS #2)
  - data/universe.json: verify Nordic crypto certificate tickers before adding them
  - data/valuations.csv is empty — log first valuation row at next sweep
