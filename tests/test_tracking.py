"""
Tests for the measurement layer: the decision ledger (scripts/decisions.py)
and the six-pillar scorecard (scripts/scorecard.py).

The point of these tests is not that the arithmetic runs. It is that the
system cannot flatter itself: that a number computed on too little evidence is
withheld rather than printed, that a pick is measured against a baseline
rather than in isolation, and that an agent cannot type a price into the
ledger.

Run with: python3 -m unittest discover -s tests -v
"""
import csv
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)

import decisions as dec  # noqa: E402
import scorecard as sc  # noqa: E402


CANDIDATE_ROW = {
    "ticker": "AZN.ST", "source": "holding", "focus": "Y", "rank": "3",
    "best_lens": "value", "screen_status": "PASS", "name": "AstraZeneca",
    "sector": "Healthcare", "country": "Sweden", "currency": "SEK",
    "price": "1560.5", "pe": "24.9", "fwd_pe": "", "peg": "1.44",
    "margin_pct": "17.0", "op_margin_pct": "20.1", "roe_pct": "22.0",
    "roic_pct": "13.1", "de_ratio": "64.2", "net_debt_to_ebitda": "1.38",
    "rev_growth_pct": "6.4", "rev_cagr3y_pct": "5.5", "fcf_yield_pct": "0.2",
    "div_yield_pct": "1.91", "mcap_b": "2400", "beta": "0.21",
    "pct_52w_range": "36", "z_quality": "0.4", "z_value": "0.9",
    "z_growth": "0.1", "z_defensive": "0.5", "z_contrarian": "0.2",
    "thin_lenses": "", "suspect": "", "note": "",
}


class LedgerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.screens = os.path.join(self.tmp, "screens")
        os.makedirs(self.screens)
        self.candidates = os.path.join(self.screens, "20260825T000000-candidates.csv")
        with open(self.candidates, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(CANDIDATE_ROW))
            w.writeheader()
            w.writerow(CANDIDATE_ROW)
            other = dict(CANDIDATE_ROW, ticker="EVO.ST", source="watchlist",
                         price="820.0", rank="9", focus="")
            w.writerow(other)
        self.ledger = os.path.join(self.tmp, "decisions.csv")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _picks(self, rows):
        path = os.path.join(self.tmp, "picks.csv")
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=dec.PICKS_COLUMNS)
            w.writeheader()
            for r in rows:
                w.writerow({c: r.get(c, "") for c in dec.PICKS_COLUMNS})
        return path


# ---------------------------------------------------------------------------
# The ledger must join evidence, not accept it
# ---------------------------------------------------------------------------
class TestRecording(LedgerTest):
    def test_metrics_are_joined_from_the_sweep_not_the_picks_file(self):
        """An agent typing a price into the ledger is a transcription-error
        surface, and a wrong entry price corrupts every performance figure
        derived from it forever."""
        picks = self._picks([{"voice": "valuation", "ticker": "AZN.ST",
                              "action": "BUY", "conviction": "8",
                              "thesis": "cheap on fundamentals"}])
        rows = dec.record(picks, self.candidates, self.ledger)
        self.assertEqual(rows[0]["entry_price"], "1560.5")
        self.assertEqual(rows[0]["pe"], "24.9")
        self.assertEqual(rows[0]["screen_status"], "PASS")
        self.assertEqual(rows[0]["source"], "holding")

    def test_a_pick_outside_the_candidate_set_is_refused(self):
        """A name the funnel never surfaced cannot be evidenced — that is the
        LLM stock-picking this system exists to prevent."""
        picks = self._picks([{"voice": "growth", "ticker": "TSLA",
                              "action": "BUY", "conviction": "9"}])
        with self.assertRaises(SystemExit) as cm:
            dec.record(picks, self.candidates, self.ledger)
        self.assertIn("not in", str(cm.exception))

    def test_an_unknown_voice_is_refused(self):
        picks = self._picks([{"voice": "vibes", "ticker": "AZN.ST", "action": "BUY"}])
        with self.assertRaises(SystemExit):
            dec.record(picks, self.candidates, self.ledger)

    def test_an_unknown_action_is_refused(self):
        picks = self._picks([{"voice": "macro", "ticker": "AZN.ST", "action": "MAYBE"}])
        with self.assertRaises(SystemExit):
            dec.record(picks, self.candidates, self.ledger)

    def test_nothing_is_written_when_any_row_is_bad(self):
        """Partial writes would leave a ledger that looks complete."""
        picks = self._picks([
            {"voice": "valuation", "ticker": "AZN.ST", "action": "BUY"},
            {"voice": "growth", "ticker": "NOTREAL", "action": "BUY"},
        ])
        with self.assertRaises(SystemExit):
            dec.record(picks, self.candidates, self.ledger)
        self.assertFalse(os.path.exists(self.ledger))

    def test_every_voice_and_the_chairman_are_recorded_separately(self):
        """Chairman vs voices is the comparison that would ever justify
        weighting the Council — it needs both sides stored."""
        picks = self._picks([
            {"voice": "valuation", "ticker": "AZN.ST", "action": "BUY", "conviction": "8"},
            {"voice": "contrarian", "ticker": "EVO.ST", "action": "BUY", "conviction": "6"},
            {"voice": "chairman", "ticker": "AZN.ST", "action": "BUY",
             "conviction": "8", "confidence": "High", "horizon": "Long"},
        ])
        rows = dec.record(picks, self.candidates, self.ledger)
        self.assertEqual({r["voice"] for r in rows},
                         {"valuation", "contrarian", "chairman"})

    def test_status_marks_only_the_newest_open_call(self):
        picks = self._picks([{"voice": "chairman", "ticker": "AZN.ST",
                              "action": "BUY", "conviction": "8"}])
        dec.record(picks, self.candidates, self.ledger)
        dec.record(picks, self.candidates, self.ledger)     # a later sweep repeats it
        dec.set_status("AZN.ST", "executed", "bought 3", ledger_path=self.ledger)
        rows = dec.load_ledger(self.ledger)
        self.assertEqual([r["status"] for r in rows], ["open", "executed"])

    def test_status_on_a_ticker_with_no_open_call_fails_loudly(self):
        with self.assertRaises(SystemExit):
            dec.set_status("AZN.ST", "executed", ledger_path=self.ledger)


class TestBasisReport(LedgerTest):
    def test_before_council_runs_it_shows_the_focus_set_with_metrics(self):
        text = dec.basis(self.candidates, self.ledger)
        self.assertIn("AZN.ST", text)
        self.assertIn("no council picks recorded", text)
        self.assertIn("24.9", text)          # the P/E the sweep actually produced

    def test_after_council_runs_it_shows_who_picked_what(self):
        picks = self._picks([
            {"voice": "valuation", "ticker": "AZN.ST", "action": "BUY", "conviction": "8"},
            {"voice": "defensive", "ticker": "AZN.ST", "action": "BUY", "conviction": "6"},
        ])
        dec.record(picks, self.candidates, self.ledger)
        text = dec.basis(self.candidates, self.ledger)
        self.assertIn("valuation(B8)", text)
        self.assertIn("defensive(B6)", text)

    def test_it_names_where_the_evidence_was_thin(self):
        """fwd_pe is blank on the fixture — the report must say so rather than
        leaving a silent gap."""
        text = dec.basis(self.candidates, self.ledger)
        self.assertIn("Where the evidence was thin", text)
        self.assertIn("fwdP/E", text)


# ---------------------------------------------------------------------------
# The scorecard must refuse to flatter
# ---------------------------------------------------------------------------
class TestAntiFlattery(unittest.TestCase):
    def test_a_thin_bucket_withholds_its_number(self):
        line = sc.evidence([0.1] * 5, "growth")
        self.assertIn("insufficient evidence", line)
        self.assertIn("n=5", line)
        self.assertNotIn("beat baseline", line)

    def test_a_full_bucket_reports_median_and_hit_rate(self):
        line = sc.evidence([0.02] * sc.MIN_OBSERVATIONS, "growth")
        self.assertIn("beat baseline", line)
        self.assertIn(f"n={sc.MIN_OBSERVATIONS}", line)

    def test_an_empty_bucket_says_so(self):
        self.assertIn("no observations", sc.evidence([], "copycat"))

    def test_the_threshold_is_not_trivially_low(self):
        """Lowering MIN_OBSERVATIONS to make the report look fuller is the
        exact self-deception this guard exists to prevent."""
        self.assertGreaterEqual(sc.MIN_OBSERVATIONS, 20)


class TestExcessReturn(unittest.TestCase):
    DECIDED = datetime(2026, 6, 15, tzinfo=timezone.utc)
    BENCH = {(2026, 5): 100.0, (2026, 6): 100.0, (2026, 7): 110.0}

    def test_a_pick_is_measured_against_the_benchmark_not_in_isolation(self):
        """A raw return mostly measures the market. +10% while the benchmark
        did +10% is zero skill, and must read as zero."""
        ex = sc.excess_return("100", 110.0, self.DECIDED, self.BENCH, 110.0)
        self.assertAlmostEqual(ex, 0.0, places=6)

    def test_beating_the_benchmark_is_positive(self):
        ex = sc.excess_return("100", 120.0, self.DECIDED, self.BENCH, 110.0)
        self.assertAlmostEqual(ex, 0.10, places=6)

    def test_losing_to_a_rising_benchmark_is_negative(self):
        ex = sc.excess_return("100", 105.0, self.DECIDED, self.BENCH, 110.0)
        self.assertAlmostEqual(ex, -0.05, places=6)

    def test_a_missing_leg_is_none_never_zero(self):
        """Zero would silently read as 'performed exactly in line' and pollute
        every median computed from it."""
        self.assertIsNone(sc.excess_return(None, 110.0, self.DECIDED, self.BENCH, 110.0))
        self.assertIsNone(sc.excess_return("100", None, self.DECIDED, self.BENCH, 110.0))
        self.assertIsNone(sc.excess_return("100", 110.0, self.DECIDED, {}, None))
        self.assertIsNone(sc.excess_return("0", 110.0, self.DECIDED, self.BENCH, 110.0))

    def test_a_decision_older_than_the_benchmark_history_is_none(self):
        old = datetime(2020, 1, 1, tzinfo=timezone.utc)
        self.assertIsNone(sc.excess_return("100", 110.0, old, self.BENCH, 110.0))


class TestScorecardStructure(unittest.TestCase):
    """These must not read the live repo. A test that passes only while
    data/decisions.csv happens to be empty is not a test — it broke the moment
    the first real sweep recorded picks."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self._orig = (sc.LEDGER_PATH, sc.HISTORY_PATH, sc.SCREENS_DIR)
        sc.LEDGER_PATH = os.path.join(self.tmp, "decisions.csv")
        sc.HISTORY_PATH = os.path.join(self.tmp, "candidate_history.csv")
        sc.SCREENS_DIR = os.path.join(self.tmp, "screens")
        os.makedirs(sc.SCREENS_DIR)
        self.addCleanup(self._restore)

    def _restore(self):
        sc.LEDGER_PATH, sc.HISTORY_PATH, sc.SCREENS_DIR = self._orig

    def test_it_builds_offline_without_inventing_numbers(self):
        text = sc.build(["discovery", "data", "gaps"], offline=True)
        for heading in ("1. DISCOVERY", "2. DATA", "GAPS"):
            self.assertIn(heading, text)

    def test_an_empty_ledger_reports_unknown_rather_than_estimating(self):
        text = sc.build(["judgement"], offline=True)
        self.assertIn("cannot be measured", text)
        self.assertNotIn("beat baseline", text)

    def test_a_populated_ledger_still_withholds_below_the_threshold(self):
        """The failure mode this whole layer exists to prevent: having a few
        rows must not start producing numbers."""
        with open(sc.LEDGER_PATH, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=dec.LEDGER_COLUMNS)
            w.writeheader()
            for i in range(3):
                w.writerow({"decided_utc": "2026-08-25T00:00:00+00:00",
                            "voice": "valuation", "ticker": f"T{i}",
                            "action": "BUY", "entry_price": "100",
                            "conviction": "8", "status": "open"})
        text = sc.build(["judgement"], offline=True)
        self.assertIn("insufficient evidence", text)
        self.assertNotIn("beat baseline", text)

    def test_every_pillar_is_reachable(self):
        self.assertEqual(set(sc.PILLARS),
                         {"discovery", "data", "mechanical", "judgement",
                          "decision", "outcome", "gaps"})


if __name__ == "__main__":
    unittest.main()
