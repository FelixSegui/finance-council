# Excel workbook upgrade — paste-ready prompt

Hand the block below to your Claude-for-Excel session. It describes what
`master-6.xlsx` should carry so the analysis system can make better decisions.

**Read this first, before the prompt.** Excel is an *input*, never a second
portfolio database — `data/portfolio.json` stays authoritative and
`scripts/import_excel_holdings.py` is strictly read-only. Every ask below is a
field that **no free automated source reaches**, and each one names what its
absence currently costs. Nothing here asks you to duplicate something the
pipeline already fetches; that would create two versions of one number, which
is worse than having one.

Three asks are worth far more than the rest. If you only do part of this, do
**A1 (entity type)**, **A2 (NAV discount)** and **A3 (forward P/E for Nordic
names)** — between them they unblock two Council voices and remove the largest
measured bias in the funnel.

---

## THE PROMPT

You're working inside my personal finance workbook (`master-6.xlsx`). A script
reads this file and expects the existing sheet and column layout, so: **add new
columns to the right of existing ones, never reorder or restructure a sheet,
never merge cells, and keep one row per ticker.** Use ISO dates (`YYYY-MM-DD`).
Leave a cell genuinely blank when you don't have the value — never type 0, "n/a"
or a guess, because blank is read as "unknown" and a zero is read as data.

### A. New columns on the `Universe` sheet (highest value)

**A1 — `entity_type`.** One of: `operating` · `holding_company` · `bank` ·
`insurer` · `reit` · `fund_or_etp` · `commodity` · `crypto`.
*Why:* the system currently ranks every name with the same metrics, and that is
wrong for several of my holdings. Industrivärden shows **1198% "revenue
growth"** because the data provider counts investment gains as revenue;
Handelsbanken and SEB show **no debt-to-equity at all**, which is normal for a
bank but currently reads as missing data. With this column the screen can apply
the right metrics per entity type instead of flagging healthy companies as
data gaps. This is the single cheapest high-value field in this list.

**A2 — `nav_per_share` and `nav_as_of`.** For `holding_company` rows only
(Investor, Industrivärden, Latour, Lundbergs, Kinnevik, Bure).
*Why:* holding companies cannot be valued on P/E — the real metric is the
discount or premium to net asset value, and **no free source anywhere provides
it.** Two separate analyst voices have now wanted this and been unable to act.
Investor A is one of my largest positions and the system currently has no
honest way to say whether it is cheap. Quarterly refresh is plenty; it does not
change weekly.

**A3 — `forward_pe`.** Every row where Excel's Stocks data type can supply it.
*Why, with the measurement:* forward P/E is available for **100% of US names
and 68% of Swedish names** in my universe. Two of the five screening lenses
rank partly on forward multiples, so a Swedish company can lose a shortlist
slot for *having no estimate* rather than for being less attractive. The system
now corrects for this statistically, but the correction lowers confidence — it
cannot conjure the number. Filling this closes a 32-percentage-point evidence
gap between the two markets I actually invest in.

**A4 — `enterprise_value` (or `net_debt` if EV isn't available).**
*Why:* the Valuation voice has no EV/EBIT or EV/EBITDA and says so on every
memo. It currently approximates and labels the approximation. EV is the single
field that turns that into a real multiple.

**A5 — `effective_tax_rate`.**
*Why:* return on invested capital is computed with an *assumed* statutory tax
rate by country, and every ROIC figure the system produces is therefore tagged
`ESTIMATED` rather than `OK`. One real number per company promotes it to a
figure worth arguing over.

**A6 — `dividend_years_unbroken` and `dividend_per_share_5y_ago`.**
*Why:* dividend *quality* — consistency and growth — is not fetchable, only the
current yield is. For the Swedish sleeve in particular, a 4% yield that has
grown for fifteen years is a completely different asset from a 4% yield that
was cut two years ago, and the system currently cannot tell them apart.

### B. New columns for the Copycat / Smart Money voice

**B1 — `institutional_ownership_pct` and `institutional_change_pct` (quarter on
quarter).**
**B2 — `largest_shareholders`** — top three, as free text, with their stakes.
**B3 — `activist_position`** — blank, or a one-line note.
*Why:* a seventh analyst voice was added whose job is "what are informed
insiders and sophisticated investors actually doing?" Insider transactions it
can already fetch (SEC Form 4 for US names, Finansinspektionen for Swedish
ones). Institutional ownership, 13F changes and activist stakes are fetched by
**nothing in the system**, so that voice runs at roughly half strength on every
name and is instructed to write `MISSING` rather than guess. Quarterly refresh
is fine.

### C. Ticker hygiene on `Universe` — a correctness issue, not a nicety

**C1.** Any ticker containing a space (`SEB A`, `HM B`, `INVE B`, `NOVO B`, …)
is Excel's display name, not a symbol. Replace each with the real
exchange-suffixed symbol (`SEB-A.ST`, `HM-B.ST`, `INVE-B.ST`, `NOVO-B.CO`).
**Verify the exchange per name — do not assume `.ST` for all of them.** Novo
Nordisk is Copenhagen-listed. These rows fail every fetch until corrected.

**C2.** Make sure the share class in the sheet matches what I actually hold.
The workbook has carried `INVE-B.ST` and `ATCO-A.ST` while I hold `INVE-A.ST`
and `ATCO-B.ST`. The A and B lines are different prices and different voting
rights; tracking the wrong one produces analysis of something I don't own.

**C3.** A ticker that resolves is not a ticker that is *correct*. `VITR.ST`
returns a perfectly good live price — for **Vitrolife**, not for Sobi, whose
symbol is `SOBI.ST`. When you add or change a symbol, confirm the company name
that comes back matches the company you meant.

### D. `Transactions` sheet — one column

**D1 — `decision_ref`.** When a buy or sell follows a recommendation from my
memos, put the memo date here (`2026-08-24`). Blank otherwise.
*Why:* the system logs what it recommended and when. This closes the loop, and
lets it measure the one thing it currently cannot: **the cost of the delay
between a call and the trade.** Two recommendations have now sat unexecuted for
three consecutive weeks and the system can only estimate what that cost.

### E. Sheet-level

**E1.** Every fundamentals row needs an `as_of` date. A stale figure that looks
current is worse than a blank one — the import flags anything older than ten
days, but only if the date is there.

**E2.** Add a `currency` column wherever a money figure appears and it isn't
already explicit. Mixed SEK/USD/EUR/DKK columns without a currency make totals
silently wrong, and the system will not assume 1:1.

**E3.** Don't restructure a sheet to fix a row, and leave existing cell
formatting and Stocks data-type links in place — refresh them where asked, but
don't convert them to static values.

---

## What NOT to add

- Prices, market caps, betas, 52-week ranges for US names — already fetched
  automatically and reliably. Duplicating them creates two versions of one
  number and a reconciliation problem.
- Any computed ratio you can derive from two columns already present. Give the
  system the inputs and let it compute, so the formula is visible and testable
  in one place.
- Opinions, target prices, or ratings. The workbook is an evidence source; the
  judgement layer is deliberately elsewhere.
