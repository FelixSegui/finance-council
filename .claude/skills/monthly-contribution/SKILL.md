---
name: monthly-contribution
description: On-demand monthly check-in to decide how much new money can be allocated to the market this month. Invoke roughly once a month, not every weekly sweep - separate cadence from the Council sweep and from swedish-equity-review. Reads investor_profile.json for the buffer requirement and the 1000-3000 SEK planned range, but the actual income/expense numbers must come from the user each time - this system has no bank-account visibility and must not estimate them.
---

# Monthly contribution check-in

## Role

You help the user answer one question, once a month: **how much of this
month's money is safe to move from "available" to "invested"?** This is
deliberately a small, repeatable checklist, not a financial-planning
engine — "not too fancy" per the user's own framing when this skill was
requested (2026-08-04). Keep the whole exchange short.

## Why this is separate from the weekly sweep

The Council sweep answers "how is the portfolio doing." This skill answers
a different, narrower question on a different cadence: "how much NEW money
should join it this month." Conflating them either buries this question in
a weekly memo it doesn't belong in, or turns every sweep into a budgeting
exercise. Keep them apart.

## What this skill does NOT have

No bank API, no income visibility, no expense tracking. Every number this
skill uses either comes from `investor_profile.json`/`portfolio.json`
(already-recorded facts) or must be asked of the user fresh, this session —
never estimated from a prior month, never assumed unchanged. If the user
doesn't have a number to hand, say "no data" for that step and work with
what's actually known, exactly like every other agent in this system.

## Method

1. **Read the standing facts first** — don't ask for what's already on
   file:
   - `investor_profile.json.buffer` — the emergency-fund target
     (3-6 months of expenses, per the current file).
   - `investor_profile.json.horizon.planned_monthly_contribution_sek` —
     the existing planned range (1000-3000 SEK as of 2026-08-03), which
     this check-in either confirms or revises, not replaces blindly.
   - `data/portfolio.json` — current buffer-account balances (hb-main,
     hb-checking per the current structure) and any known tax-reserve
     shortfall that competes with this month's contribution for the same
     cash.

2. **Ask the user, this session, for:**
   - Income received (or expected) this month, if it varies month to
     month — skip this if income is stable and already reflected in the
     planned range.
   - Any one-off expense this month that competes with the buffer or the
     contribution (skip if none).
   - Current buffer-account balance, if it might have moved since the
     file was last updated (skip if unchanged).
   Keep this to the minimum needed — don't interrogate a stable month.

3. **Check the buffer first, always.** If the buffer is below the
   3-6 month target after accounting for anything raised in step 2, that
   takes priority over a market contribution — say so plainly and
   recommend topping up the buffer instead (or splitting the amount), per
   this system's standing rule that the risk budget is genuine investable
   money, not partly an emergency fund (see `investor_profile.json.buffer`
   notes).

4. **Recommend an amount.** Default to the existing planned range
   (currently 1000-3000 SEK) unless step 2 gives a concrete reason to go
   above or below it this month — state the reason either way, don't
   silently pick a number. If nothing this month argues for a change, say
   so and use the range's usual point (or ask the user which end, if it's
   genuinely close).

5. **Recommend routing**, using the CURRENT operating targets in
   `data/portfolio.json.targets` and whatever's actually under-target
   right now (same logic the `portfolio` agent already uses for drift) —
   don't re-derive a separate routing rule here, just apply the existing
   one to this month's amount.

6. **Record the decision.** Once the user confirms an amount:
   - Append one line to `data/portfolio_history_archive.md` (or, if a
     dedicated running log for these check-ins doesn't exist yet, create
     `data/contribution_log.md` with a one-line header and append there
     instead, then use it going forward) — date, amount, routing, and the
     one-line reason.
   - If the amount or routing genuinely changes the standing plan (not
     just this month's instance of it), update
     `investor_profile.json.horizon.planned_monthly_contribution_sek`
     directly and say so explicitly — don't leave the file describing a
     range the user has already moved past.
   - This is a DECISION, not an executed trade — recording it here does
     not mean the money has moved. If the user confirms it's already been
     transferred/invested, treat it like any other trade: record it in
     `data/portfolio.json` (new/updated holding or cash line) the same way
     the main session does for any other purchase.

## Rules

- Never invent income, expenses, or a buffer balance — ask, or say "no
  data" and work around the gap.
- The buffer target always wins over the contribution when they compete
  for the same cash.
- Keep the whole exchange short — this is a monthly five-minute check-in,
  not a full financial plan. If the user wants the deeper conversation
  (revisiting the buffer target, the contribution range itself, goals),
  say so and treat it as a separate, longer conversation rather than
  expanding this one.
