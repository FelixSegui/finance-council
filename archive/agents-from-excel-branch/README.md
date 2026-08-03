# Agent definitions from the Excel-backed branch

These are the agent definitions from `claude/project-status-briefing-0528tx`,
merged into `main` on 2026-08-03. They are **archived, not deleted, and not
live** — nothing runs them.

## Why they're here and not in `.claude/agents/`

The branch was a parallel rearchitecture of this system. Its agents are in
several respects **more developed** than the live ones — in particular
`core-council.md`, which absorbed the old standalone `controller` agent and
runs a 5-persona system-health debate, and the consolidated one-file sweep
report format.

But they are written against **the branch's runtime**, not the live one:

- they call `python run.py <module>`, which orchestrates fetches differently
- they read `data/cache/coverage_reports/*-summary.json` and
  `data/cache/controller_state.json`
- they treat `master.xlsx` as the source of truth, and expect `journal` to
  write reconciliation rows into the workbook's Notes sheet
- they expect the consolidated `reports/YYYY-MM-DD-sweep.md` format instead of
  the current separate council memo

Dropping them into the live system would produce agents that reference
infrastructure that isn't wired up — which fails confusingly rather than
loudly. That is worse than not having them.

## What to do with them

Port improvements **deliberately, one at a time**, each with its dependency
either satisfied or removed. Do not bulk-copy them back.

The three most valuable things in here, in order:

1. **`core-council.md`'s system-health half** — the standing 5-persona debate
   over module health and coverage trends. This is real capability the live
   `meta` agent covers only thinly.
2. **The consolidated single-report format** — one `sweep.md` per day instead
   of a memo plus separate coverage/controller output. Directly serves the
   "slim it down" goal.
3. **`core-journal.md`'s reconciliation ordering rule** — journal must
   reconcile *before* council runs, or council writes a report with an empty
   reconciliation section. That was a real bug found on the branch's own first
   sweep, and the live system has the same latent ordering weakness.

Tracked as an open item in `/OPEN_ITEMS.md`.
