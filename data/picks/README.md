# Council picks — the handoff into the decision ledger

`council` writes one file here per sweep: `YYYY-MM-DD-picks.csv`, with exactly
this header and nothing else:

```
voice,ticker,action,conviction,confidence,horizon,thesis
```

Then:

```bash
python scripts/decisions.py record --picks data/picks/YYYY-MM-DD-picks.csv
```

That joins price, screen status, lens scores and every metric from the sweep's
own `data/screens/<ts>-candidates.csv` and appends the result to
**`data/decisions.csv`** — the ledger.

**Seven columns, no numbers.** The metrics are joined, never typed. An agent
copying an entry price into this file is a transcription-error surface, and a
wrong entry price silently corrupts every performance figure derived from it
afterwards, permanently.

A pick for a ticker that was not in that sweep's candidate set is rejected.
A name from outside the funnel cannot be evidenced.
