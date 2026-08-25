"""
Tests for the discovery funnel: universe -> mechanical ranking -> candidate
set -> screen -> health. Standard-library unittest, no pytest dependency.

These are deliberately offline: every test builds its own fixture records
rather than hitting Yahoo, so the suite is deterministic and runs anywhere.

Run with: python3 -m unittest discover -s tests -v
"""
import json
import os
import shutil
import statistics
import sys
import tempfile
import unittest
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)

import scout  # noqa: E402
import watchlist as wl  # noqa: E402
import build_universe as bu  # noqa: E402


def record(pe=15.0, fpe=13.0, roe=0.20, margin=0.12, op_margin=0.15,
           de=60.0, growth=0.08, mcap=5e10, beta=1.0, price=100.0,
           hi=120.0, lo=80.0, fcf=2e9, ebitda=1e10, debt=2e10, cash=5e9,
           pb=3.0, ps=2.0, peg=1.5, div=0.02, roic=0.11, **extra):
    """A complete, plausible fundamentals record shaped exactly like
    fetch_market_data.py's output (including the derived-metric wrapper)."""
    rec = {
        "price": price, "52w_high": hi, "52w_low": lo, "market_cap": mcap,
        "trailing_pe": pe, "forward_pe": fpe, "price_to_book": pb,
        "price_to_sales": ps, "peg_ratio": peg, "dividend_yield": div,
        "beta": beta, "revenue_growth": growth, "free_cashflow": fcf,
        "profit_margins": margin, "operating_margins": op_margin,
        "return_on_equity": roe, "debt_to_equity": de, "ebitda": ebitda,
        "total_debt": debt, "total_cash": cash,
        "roic_pct": {"value": roic, "quality_state": "ESTIMATED"},
        "sector": "Industrials", "country": "United States", "currency": "USD",
        "revenue_history_last_n_fiscal_years": [
            {"fiscal_year_end": "2025-12-31", "total_revenue": 1200},
            {"fiscal_year_end": "2024-12-31", "total_revenue": 1100},
            {"fiscal_year_end": "2023-12-31", "total_revenue": 1000},
        ],
    }
    rec.update(extra)
    return rec


def universe_records(n=40):
    """A spread-out synthetic universe so z-scores actually discriminate."""
    out = {}
    for i in range(n):
        t = f"T{i:03d}" if n > 99 else f"T{i:02d}"
        out[t] = record(pe=8 + i, fpe=7 + i, roe=0.05 + i * 0.01,
                        margin=0.02 + i * 0.005, op_margin=0.04 + i * 0.005,
                        de=20 + i * 5, growth=-0.05 + i * 0.01,
                        mcap=1e9 * (i + 1), beta=0.6 + i * 0.03,
                        price=50 + i, roic=0.03 + i * 0.004)
    return out


class Args:
    """Stand-in for argparse's namespace in run()."""
    def __init__(self, **kw):
        self.cache_days = 7
        self.refresh = False
        self.workers = 1
        self.lens_top_n = 5
        self.focus_top_n = 6
        self.max_per_sector = 99      # fixtures are all one sector by design
        self.limit = None
        self.promote = False
        self.promote_top = 5
        self.quiet = True
        for cli, _f, _d in scout.FILTERS:
            setattr(self, cli, None)
        for k, v in kw.items():
            setattr(self, k, v)


class TempRepo(unittest.TestCase):
    """Each test runs against its own temp data dir, so nothing touches the
    real portfolio/universe/watchlist files."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.universe_path = os.path.join(self.tmp, "universe.json")
        self.watchlist_path = os.path.join(self.tmp, "watchlist.json")
        self.history_path = os.path.join(self.tmp, "candidate_history.csv")
        self.portfolio_path = os.path.join(self.tmp, "portfolio.json")
        self.screens_dir = os.path.join(self.tmp, "screens")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_universe(self, tickers, generated=None, extra=None):
        data = {
            "generated_utc": generated or datetime.now(timezone.utc).isoformat(),
            "refresh_interval_days": 30,
            "counts": {"total": len(tickers)},
            "sources": [],
            "tickers": {t: {"name": t, "sector": None, "region": "US",
                            "cik": None, "source": "sp500"} for t in tickers},
        }
        if extra:
            data["tickers"].update(extra)
        with open(self.universe_path, "w") as f:
            json.dump(data, f)
        return data

    def write_portfolio(self, held):
        holdings = [{"ticker": t, "name": t, "quantity": 1,
                     "exposure_class": "equity"} for t in held]
        holdings += [
            {"ticker": "CASH_SEK", "name": "cash", "exposure_class": "cash"},
            {"ticker": "TBD", "name": "Some unlisted fund", "exposure_class": "equity"},
            {"ticker": "OLD.ST", "name": "Something (FROZEN - unsellable)",
             "exposure_class": "equity"},
        ]
        with open(self.portfolio_path, "w") as f:
            json.dump({"holdings": holdings}, f)


# ---------------------------------------------------------------------------
# 1. Universe loads correctly
# ---------------------------------------------------------------------------
class TestUniverseLoads(TempRepo):
    def test_loads_tickers_and_metadata(self):
        self.write_universe([f"T{i:02d}" for i in range(200)])
        tickers, warnings = scout.load_universe(self.universe_path)
        self.assertEqual(len(tickers), 200)
        self.assertEqual(tickers["T00"]["source"], "sp500")
        self.assertEqual(warnings, [])

    def test_missing_file_warns_instead_of_silently_empty(self):
        tickers, warnings = scout.load_universe(os.path.join(self.tmp, "nope.json"))
        self.assertEqual(tickers, {})
        self.assertTrue(any("does not exist" in w for w in warnings))

    def test_watchlist_sized_universe_is_flagged_not_accepted(self):
        self.write_universe([f"T{i:02d}" for i in range(30)])
        _tickers, warnings = scout.load_universe(self.universe_path)
        self.assertTrue(any("that is a watchlist" in w for w in warnings))

    def test_stale_universe_is_flagged(self):
        old = (datetime.now(timezone.utc) - timedelta(days=90)).isoformat()
        self.write_universe([f"T{i:02d}" for i in range(200)], generated=old)
        _tickers, warnings = scout.load_universe(self.universe_path)
        self.assertTrue(any("days old" in w for w in warnings))

    def test_build_preserves_manual_entries(self):
        """A universe refresh must never drop hand-verified non-US tickers —
        no free constituent feed can put them back."""
        existing = {"tickers": {
            "EVO.ST": {"name": "Evolution", "source": "manual", "region": "Nordic"},
            "AAPL": {"name": "stale", "source": "sp500"},
        }}
        self.assertEqual(set(bu.manual_entries(existing)), {"EVO.ST"})


# ---------------------------------------------------------------------------
# 2. Mechanical ranking works
# ---------------------------------------------------------------------------
class TestRanking(unittest.TestCase):
    def test_lens_scores_are_produced_per_lens(self):
        met = {t: scout.metrics(r) for t, r in universe_records(40).items()}
        scores, coverage, _fcov = scout.rank_lenses(met)
        for lens in scout.LENSES:
            self.assertGreater(coverage[lens], 30, f"{lens} coverage collapsed")
            self.assertIsNotNone(scores["T00"][lens])
        self.assertEqual(set(scores["T00"]), set(scout.LENSES))

    def test_lenses_disagree(self):
        """The whole point of five lenses is that they don't produce one
        ranking wearing five hats."""
        met = {t: scout.metrics(r) for t, r in universe_records(40).items()}
        scores, _c, _f = scout.rank_lenses(met)
        shortlists = scout.lens_shortlists(scores, top_n=5)
        self.assertNotEqual(set(shortlists["value"]), set(shortlists["quality"]))

    def test_expensive_high_growth_name_survives_via_the_growth_lens(self):
        """The specific failure this design exists to prevent: a static
        trailing-P/E rule deleting a genuine compounder."""
        recs = universe_records(40)
        recs["GROWTH"] = record(pe=90.0, fpe=45.0, peg=0.8, growth=0.55,
                                roe=0.30, margin=0.25, op_margin=0.30,
                                de=15.0, roic=0.25,
                                revenue_history_last_n_fiscal_years=[
                                    {"fiscal_year_end": "2025-12-31", "total_revenue": 3000},
                                    {"fiscal_year_end": "2024-12-31", "total_revenue": 1800},
                                    {"fiscal_year_end": "2023-12-31", "total_revenue": 1000}])
        met = {t: scout.metrics(r) for t, r in recs.items()}
        scores, _c, _f = scout.rank_lenses(met)
        shortlists = scout.lens_shortlists(scores, top_n=5)
        self.assertIn("GROWTH", shortlists["growth"])
        self.assertNotIn("GROWTH", shortlists["value"])

    def test_zscores_are_winsorized_against_one_bad_outlier(self):
        vals = {f"T{i}": float(i) for i in range(50)}
        vals["JUNK"] = 1e12  # a multi-class share-count artefact
        z = scout.zscores(vals)
        spread = max(v for k, v in z.items() if k != "JUNK") - min(z.values())
        self.assertGreater(spread, 1.0, "one outlier collapsed the whole factor")

    def test_metrics_never_impute(self):
        m = scout.metrics({"price": 10})
        self.assertIsNone(m["earnings_yield"])
        self.assertIsNone(m["roe"])
        self.assertIsNone(m["net_debt_to_ebitda"])
        self.assertIsNone(m["revenue_cagr_3y"])

    def test_lens_needs_minimum_field_coverage(self):
        """A 'quality score' derived from one number is not a quality score."""
        met = {t: scout.metrics(r) for t, r in universe_records(10).items()}
        met["THIN"] = scout.metrics({"price": 10, "return_on_equity": 0.3})
        scores, _c, _f = scout.rank_lenses(met)
        self.assertIsNone(scores["THIN"]["quality"])


# ---------------------------------------------------------------------------
# 3. Scout health reports all counts
# ---------------------------------------------------------------------------
class TestScoutHealth(TempRepo):
    UNIVERSE_SIZE = 200   # above scout's "that is a watchlist" floor

    def _run(self, **kw):
        self.write_universe([f"T{i:03d}" for i in range(self.UNIVERSE_SIZE)])
        self.write_portfolio(["T000"])
        recs = universe_records(self.UNIVERSE_SIZE)
        recs["T000"] = record()
        self._patch(recs)
        return scout.run(Args(**kw))

    def _patch(self, recs):
        """Swap every path and the network fetch for the fixture."""
        self._orig = (scout.UNIVERSE_PATH, scout.PORTFOLIO_PATH, scout.SCREENS_DIR,
                      scout.FUND_CACHE_PATH, wl.WATCHLIST_PATH, wl.HISTORY_PATH,
                      scout.fetch_equities)
        scout.UNIVERSE_PATH = self.universe_path
        scout.PORTFOLIO_PATH = self.portfolio_path
        scout.SCREENS_DIR = self.screens_dir
        scout.FUND_CACHE_PATH = os.path.join(self.tmp, "fund_cache.json")
        wl.WATCHLIST_PATH = self.watchlist_path
        wl.HISTORY_PATH = self.history_path
        scout.fetch_equities = lambda tickers, workers=1, progress=None: {
            t: recs.get(t, {"error": "not covered"}) for t in tickers}
        self.addCleanup(self._restore)

    def _restore(self):
        (scout.UNIVERSE_PATH, scout.PORTFOLIO_PATH, scout.SCREENS_DIR,
         scout.FUND_CACHE_PATH, wl.WATCHLIST_PATH, wl.HISTORY_PATH,
         scout.fetch_equities) = self._orig

    def test_health_block_carries_every_required_count(self):
        result = self._run()
        h = result["health"]
        for key in ("universe", "fetched", "ranked", "candidates", "screened",
                    "passed", "missing", "failed", "status",
                    "holdings", "watchlist", "new", "fetch_failed"):
            self.assertIn(key, h)
        self.assertEqual(h["universe"], self.UNIVERSE_SIZE)
        self.assertEqual(h["screened"], h["passed"] + h["missing"] + h["failed"])
        text = scout.format_health(h)
        for label in ("Universe:", "Fetched:", "Screened:", "Passed:",
                      "Missing:", "Failed:", "Status:"):
            self.assertIn(label, text)

    def test_valid_status_on_a_healthy_run(self):
        self.assertEqual(self._run()["health"]["status"], "VALID")

    def test_screened_equals_candidate_set(self):
        result = self._run()
        self.assertEqual(result["health"]["screened"], result["health"]["candidates"])


# ---------------------------------------------------------------------------
# 4. Missing data is handled correctly
# ---------------------------------------------------------------------------
class TestMissingData(unittest.TestCase):
    def test_missing_is_not_pass_and_not_fail(self):
        active = [("max_pe", "trailing_pe", "max", 20.0)]
        status, detail = scout.apply_filters(
            {"HAS": {"trailing_pe": 15.0}, "LACKS": {"price": 3.0},
             "OVER": {"trailing_pe": 40.0}}, active)
        self.assertEqual(status["HAS"], "PASS")
        self.assertEqual(status["LACKS"], "MISSING")
        self.assertEqual(status["OVER"], "FAIL")
        self.assertEqual(detail["LACKS"]["missing_fields"], ["trailing_pe"])

    def test_fetch_error_becomes_missing_with_a_reason(self):
        status, detail = scout.apply_filters(
            {"BROKEN": {"error": "404"}}, [("max_pe", "trailing_pe", "max", 20.0)])
        self.assertEqual(status["BROKEN"], "MISSING")
        self.assertEqual(detail["BROKEN"]["reason"], "404")

    def test_a_real_failure_beats_a_missing_field(self):
        """A name that fails one filter and lacks another is FAIL — we know
        something disqualifying about it, which is not the same as unknown."""
        active = [("max_pe", "trailing_pe", "max", 20.0),
                  ("min_profit_margin", "profit_margins", "min", 0.1)]
        status, _ = scout.apply_filters({"X": {"trailing_pe": 50.0}}, active)
        self.assertEqual(status["X"], "FAIL")

    def test_nothing_is_dropped_by_the_screen(self):
        recs = {"A": {"trailing_pe": 5.0}, "B": {"trailing_pe": 500.0}, "C": {}}
        status, _ = scout.apply_filters(recs, [("max_pe", "trailing_pe", "max", 20.0)])
        self.assertEqual(set(status), set(recs))


# ---------------------------------------------------------------------------
# 5. Zero-pass triggers investigation, never a false "no opportunities"
# ---------------------------------------------------------------------------
class TestZeroPass(TestScoutHealth):
    def test_zero_pass_sets_investigate_status_and_diagnostics(self):
        result = self._run(max_pe=0.001)          # nothing can clear this
        self.assertEqual(result["health"]["passed"], 0)
        self.assertEqual(result["health"]["status"], "INVESTIGATE_ZERO_PASS")
        self.assertTrue(result["diagnostics"])

    def test_diagnostic_names_the_single_filter_doing_the_killing(self):
        result = self._run(max_pe=0.001)
        self.assertTrue(any("max-pe" in d and "alone rejects" in d
                            for d in result["diagnostics"]),
                        result["diagnostics"])

    def test_decimal_scale_threshold_is_refused_at_parse_time(self):
        """S19: --max-debt-to-equity 2.0 against a percentage-point field
        silently rejected every candidate and looked like a quiet market."""
        problems = scout.validate_thresholds(
            [("max_debt_to_equity", "debt_to_equity", "max", 2.0)])
        self.assertTrue(problems)
        self.assertIn("percentage points", problems[0])
        self.assertFalse(scout.validate_thresholds(
            [("max_debt_to_equity", "debt_to_equity", "max", 150.0)]))

    def test_healthy_zero_pass_says_so_explicitly(self):
        """A zero-pass on a healthy pipeline is a real conclusion, and the
        diagnostic must say that rather than inventing a fault."""
        health = {"screened": 50, "missing": 2, "fetched": 50, "fetch_failed": 0}
        findings = scout.diagnose_zero_pass(
            health, {"A": {"trailing_pe": 15.0}},
            [("min_dividend_yield", "dividend_yield", "min", 0.99)], [], {})
        self.assertTrue(any("pipeline looks healthy" in f for f in findings))

    def test_broken_fetch_is_diagnosed_separately_from_a_thin_market(self):
        health = {"screened": 10, "missing": 10, "fetched": 2, "fetch_failed": 8}
        findings = scout.diagnose_zero_pass(health, {}, [], [], {"A": "boom"})
        self.assertTrue(any("fetches failed" in f for f in findings))
        self.assertTrue(any("missing a" in f for f in findings))


# ---------------------------------------------------------------------------
# 6. A newly discovered stock can enter the pool without being held/watchlisted
# ---------------------------------------------------------------------------
class TestNewCandidates(TestScoutHealth):
    def test_new_candidates_appear_and_are_labelled(self):
        result = self._run()
        new = [t for t, c in result["candidates"].items() if c["source"] == "new"]
        self.assertTrue(new, "the funnel discovered nothing — that is the failure mode")
        for t in new:
            self.assertNotIn(t, ("T000",))
            self.assertEqual(result["candidates"][t]["source"], "new")
            self.assertTrue(result["candidates"][t]["in_lens_shortlists"])

    def test_holdings_always_reach_the_candidate_set(self):
        result = self._run()
        self.assertEqual(result["candidates"]["T000"]["source"], "holding")

    def test_cash_frozen_and_unlisted_holdings_are_excluded(self):
        self.write_portfolio(["T000"])
        held = scout.load_holdings(self.portfolio_path)
        self.assertEqual(set(held), {"T000"})

    def test_promotion_moves_a_new_name_onto_the_watchlist(self):
        result = self._run(promote=True, promote_top=3)
        promoted = set(wl.load(self.watchlist_path)["entries"])
        new = {t for t, c in result["candidates"].items() if c["source"] == "new"}
        self.assertTrue(promoted & new)


# ---------------------------------------------------------------------------
# 7. Watchlist persistence
# ---------------------------------------------------------------------------
class TestWatchlistPersistence(TempRepo):
    def test_add_persists_and_reloads(self):
        self.assertTrue(wl.add("EVO.ST", name="Evolution", category="nordic",
                               path=self.watchlist_path))
        again = wl.load(self.watchlist_path)
        self.assertEqual(again["entries"]["EVO.ST"]["name"], "Evolution")
        self.assertFalse(wl.add("EVO.ST", path=self.watchlist_path))

    def test_update_never_erases_a_curated_field(self):
        wl.add("EVO.ST", name="Evolution", note="watch the regulator",
               path=self.watchlist_path)
        wl.add("EVO.ST", category="nordic", source="excel", path=self.watchlist_path)
        rec = wl.load(self.watchlist_path)["entries"]["EVO.ST"]
        self.assertEqual(rec["name"], "Evolution")
        self.assertEqual(rec["note"], "watch the regulator")
        self.assertEqual(rec["category"], "nordic")

    def test_remove_logs_a_reason(self):
        wl.add("EVO.ST", path=self.watchlist_path)
        self.assertTrue(wl.remove("EVO.ST", reason="thesis broken",
                                  path=self.watchlist_path))
        data = wl.load(self.watchlist_path)
        self.assertNotIn("EVO.ST", data["entries"])
        self.assertEqual(data["removed"][-1]["reason"], "thesis broken")

    def test_watchlist_survives_a_sweep_that_discovers_nothing(self):
        wl.add("EVO.ST", name="Evolution", path=self.watchlist_path)
        wl.add("SAND.ST", name="Sandvik", path=self.watchlist_path)
        before = set(wl.tickers(path=self.watchlist_path))
        # a later sweep touching an unrelated name must not rebuild the file
        wl.add("NEW.ST", source="scout", path=self.watchlist_path)
        self.assertTrue(before.issubset(set(wl.tickers(path=self.watchlist_path))))

    def test_universe_add_writes_a_manual_entry(self):
        self.write_universe(["AAPL"])
        self.assertTrue(wl.universe_add("EVO.ST", name="Evolution",
                                        region="Nordic", path=self.universe_path))
        with open(self.universe_path) as f:
            uni = json.load(f)
        self.assertEqual(uni["tickers"]["EVO.ST"]["source"], "manual")
        self.assertEqual(uni["counts"]["manual"], 1)


# ---------------------------------------------------------------------------
# 8. Candidate ranking history
# ---------------------------------------------------------------------------
class TestHistory(TempRepo):
    def test_history_tracks_rank_over_runs(self):
        wl.append_history([{"ticker": "AAA", "source": "new", "rank": 3,
                            "best_lens": "value", "lens_score": 1.1,
                            "screen_status": "PASS"},
                           {"ticker": "BBB", "source": "watchlist", "rank": 8,
                            "best_lens": "quality", "lens_score": 0.4,
                            "screen_status": "FAIL"}],
                          path=self.history_path, run_utc="2026-08-01T00:00:00+00:00")
        wl.append_history([{"ticker": "AAA", "source": "new", "rank": 1,
                            "best_lens": "value", "lens_score": 1.9,
                            "screen_status": "PASS"},
                           {"ticker": "BBB", "source": "watchlist", "rank": 20,
                            "best_lens": "quality", "lens_score": 0.1,
                            "screen_status": "FAIL"}],
                          path=self.history_path, run_utc="2026-08-08T00:00:00+00:00")
        table = {r["ticker"]: r for r in wl.history_table(path=self.history_path)}
        self.assertEqual(table["AAA"]["current_rank"], 1)
        self.assertEqual(table["AAA"]["previous_rank"], 3)     # improving
        self.assertEqual(table["AAA"]["times_top_n"], 2)
        self.assertEqual(table["BBB"]["current_rank"], 20)
        self.assertEqual(table["BBB"]["previous_rank"], 8)     # deteriorating
        self.assertEqual(table["BBB"]["times_top_n"], 1)
        self.assertEqual(table["BBB"]["runs_seen"], 2)

    def test_two_runs_the_same_day_are_two_runs(self):
        for stamp, rank in (("2026-08-01T09:00:00+00:00", 5),
                            ("2026-08-01T17:00:00+00:00", 2)):
            wl.append_history([{"ticker": "AAA", "source": "new", "rank": rank,
                                "best_lens": "value", "lens_score": 1.0,
                                "screen_status": "PASS"}],
                              path=self.history_path, run_utc=stamp)
        row = wl.history_table(path=self.history_path)[0]
        self.assertEqual((row["current_rank"], row["previous_rank"]), (2, 5))

    def test_empty_history_is_not_an_error(self):
        self.assertEqual(wl.history_table(path=self.history_path), [])


# ---------------------------------------------------------------------------
# 9. Council receives holdings + watchlist + new scout candidates
# ---------------------------------------------------------------------------
class TestCouncilInput(TestScoutHealth):
    def test_candidate_csv_carries_all_three_categories(self):
        wl.add("T199", name="Watched", category="test", path=self.watchlist_path)
        result = self._run()
        csvs = [f for f in os.listdir(self.screens_dir) if f.endswith("-candidates.csv")]
        self.assertEqual(len(csvs), 1)
        import csv as _csv
        with open(os.path.join(self.screens_dir, csvs[0])) as f:
            rows = list(_csv.DictReader(f))
        sources = {r["source"] for r in rows}
        self.assertEqual(sources, {"holding", "watchlist", "new"})
        self.assertEqual(len(rows), result["health"]["candidates"])

    def test_csv_exposes_the_columns_the_voices_triage_on(self):
        self._run()
        csvs = [f for f in os.listdir(self.screens_dir) if f.endswith("-candidates.csv")]
        import csv as _csv
        with open(os.path.join(self.screens_dir, csvs[0])) as f:
            cols = set(_csv.DictReader(f).fieldnames)
        for needed in ("source", "screen_status", "rank", "best_lens", "currency",
                       "roic_pct", "pe", "fwd_pe", "peg", "de_ratio",
                       "net_debt_to_ebitda", "beta", "pct_52w_range",
                       "rev_growth_pct", "fcf_yield_pct",
                       "z_quality", "z_value", "z_growth", "z_defensive",
                       "z_contrarian"):
            self.assertIn(needed, cols)

    def test_focus_marks_a_manageable_slice_without_excluding_anything(self):
        """Limited refinement: the pool stays broad, focus says where depth
        goes. Every holding is in focus; nothing is dropped from the file."""
        result = self._run()
        cands = result["candidates"]
        focus = {t for t, c in cands.items() if c["focus"]}
        self.assertTrue(focus)
        self.assertLess(len(focus), len(cands), "focus must be a slice, not everything")
        self.assertIn("T000", focus, "a holding must always get full analysis")
        self.assertEqual(result["health"]["focus"], len(focus))
        # non-focus names are still present, still screened, still readable
        non_focus = set(cands) - focus
        self.assertTrue(non_focus)
        for t in non_focus:
            self.assertIn("screen_status", cands[t])

    def test_focus_column_is_in_the_csv(self):
        self._run()
        import csv as _csv
        csvs = [f for f in os.listdir(self.screens_dir) if f.endswith("-candidates.csv")]
        with open(os.path.join(self.screens_dir, csvs[0])) as f:
            rows = list(_csv.DictReader(f))
        self.assertIn("focus", rows[0])
        self.assertTrue(any(r["focus"] == "Y" for r in rows))
        self.assertTrue(any(r["focus"] == "" for r in rows))

    def test_failed_and_missing_names_still_reach_the_council(self):
        """Screening is triage. A FAIL label travels with the candidate; it
        does not delete it."""
        result = self._run(max_pe=12.0)
        statuses = {c["screen_status"] for c in result["candidates"].values()}
        self.assertIn("FAIL", statuses)
        self.assertEqual(len(result["candidates"]), result["health"]["screened"])


# ---------------------------------------------------------------------------
# 10. No active code reads from archive/
# ---------------------------------------------------------------------------
class TestNoArchiveDependency(unittest.TestCase):
    """The active system must behave as though archive/ does not exist.

    Scope is deliberately "code and prompts": scripts, config, agent
    definitions, and the two docs a new person reads. OPEN_ITEMS.md's closed
    log is excluded on purpose — recording that something WAS deleted is
    history, not a dependency. This test file is excluded because it has to
    name the dead things in order to check for them.
    """
    ACTIVE_DIRS = ("scripts", "config", ".claude")
    ACTIVE_FILES = ("CLAUDE.md", "README.md", "requirements.txt")
    DEAD = ["scripts/funnel", "scripts/fetchers", "data/sync/",
            "build_workbook", "generate_coverage_report", "controller_state",
            "screen_candidates", "rank_candidates", "add_manual_tickers",
            "import_fundamentals_tab", "migrate_from_json",
            "data/cache/watchlist.json", "data/cache/universe.json",
            "data/cache/screens"]

    def _active_paths(self):
        for d in self.ACTIVE_DIRS:
            for dirpath, _dirs, files in os.walk(os.path.join(ROOT, d)):
                if "__pycache__" in dirpath:
                    continue
                for f in files:
                    if f.endswith((".py", ".md", ".json", ".sh", ".txt")):
                        yield os.path.join(dirpath, f)
        for f in self.ACTIVE_FILES:
            yield os.path.join(ROOT, f)

    def test_no_active_file_references_archive(self):
        offenders = []
        for path in self._active_paths():
            with open(path, errors="replace") as f:
                for i, line in enumerate(f, 1):
                    if "archive/" not in line or "portfolio_history_archive" in line:
                        continue
                    if "history only" in line or "historical reference only" in line:
                        continue          # stating the rule is not a dependency
                    offenders.append(f"{os.path.relpath(path, ROOT)}:{i}")
        self.assertEqual(offenders, [], f"active files referencing archive/: {offenders}")

    def test_no_active_file_references_deleted_architecture(self):
        offenders = []
        for path in self._active_paths():
            with open(path, errors="replace") as f:
                text = f.read()
            for token in self.DEAD:
                if token in text:
                    offenders.append(f"{os.path.relpath(path, ROOT)} -> {token}")
        self.assertEqual(offenders, [], f"references to deleted architecture: {offenders}")

    def test_deleted_paths_are_actually_gone(self):
        for p in ("run.py", "master.xlsx", "data/sync", "scripts/fetchers",
                  "scripts/funnel", "data/cache/controller_state.json"):
            self.assertFalse(os.path.exists(os.path.join(ROOT, p)),
                             f"{p} still exists")

    def test_every_live_script_imports_cleanly(self):
        import importlib
        for mod in ("scout", "watchlist", "build_universe", "fetch_market_data",
                    "derived_metrics", "position_report", "performance",
                    "backtest", "fetch_calendar", "import_excel_holdings"):
            importlib.import_module(mod)


if __name__ == "__main__":
    unittest.main()


# ---------------------------------------------------------------------------
# 11. Universe hygiene: verified tickers, no share-class duplicates, no
#     single-sector lens shortlists. All three were live defects found by the
#     2026-08-24 Swedish-CSV import test run.
# ---------------------------------------------------------------------------
class TestNameVerification(unittest.TestCase):
    def test_same_company_different_wording_matches(self):
        for claimed, actual in [
            ("Volvo Group", "AB Volvo (publ)"),
            ("Atlas Copco AB (A)", "Atlas Copco AB (publ)"),
            ("Investor AB", "Investor AB (publ)"),
            ("Kindred Group plc", "Kindred Group Plc"),
        ]:
            self.assertEqual(wl.name_matches(claimed, actual), "match", (claimed, actual))

    def test_a_different_company_is_rejected(self):
        """The dangerous case: VITR.ST resolves perfectly — to Vitrolife, not
        to Sobi. A resolving ticker is not a correct ticker."""
        for claimed, actual in [
            ("Swedish Orphan Biovitrum AB (Sobi)", "Vitrolife AB (publ)"),
            ("Catena AB", "Catella AB (publ)"),           # 0.6 similar, different company
            ("Betsson AB", "Better Collective A/S"),
            ("MediOver AB", "Malmbergs Elektriska AB (publ)"),
            ("Alifrost AB", "AddLife AB (publ)"),
        ]:
            self.assertEqual(wl.name_matches(claimed, actual), "mismatch", (claimed, actual))

    def test_a_typo_is_near_not_a_match_and_not_a_mismatch(self):
        self.assertEqual(wl.name_matches("Bonavia AB", "Bonava AB (publ)"), "near")

    def test_corporate_form_words_carry_no_identity(self):
        self.assertEqual(wl.name_matches("AB", "Holding Group AB"), "mismatch")

    def test_stockholm_share_class_queries_are_tried(self):
        """Yahoo's index matches 'Elekta AB ser. B', not 'Elekta AB' — without
        this the Stockholm listing is never found."""
        qs = list(wl._search_queries("ELEK-B.ST", "Elekta AB"))
        self.assertIn("Elekta AB ser. B", qs)
        self.assertEqual(qs[0], "Elekta AB")


class TestShareClassCollapse(unittest.TestCase):
    NAMES = {
        "ATCO-A.ST": "Atlas Copco AB (publ)", "ATCO-B.ST": "Atlas Copco AB (publ)",
        "INVE-A.ST": "Investor AB (publ)", "INVE-B.ST": "Investor AB (publ)",
        "EVO.ST": "Evolution AB (publ)",
        "CAT-B.ST": "Catella AB (publ)", "CATE.ST": "Catena AB (publ)",
    }

    def test_a_holding_always_survives_its_own_share_class(self):
        """Collapsing a held line into one the user does not own would
        silently drop that position's hold/sell decision."""
        dropped = scout.collapse_share_classes(
            set(self.NAMES), self.NAMES,
            holdings={"ATCO-B.ST"}, watch_tickers={"ATCO-A.ST"},
            market_caps={"ATCO-A.ST": 9e11, "ATCO-B.ST": 1e9})
        self.assertEqual(dropped.get("ATCO-A.ST"), "ATCO-B.ST")
        self.assertNotIn("ATCO-B.ST", dropped)

    def test_larger_market_cap_wins_when_neither_is_held(self):
        dropped = scout.collapse_share_classes(
            set(self.NAMES), self.NAMES, holdings=set(), watch_tickers=set(),
            market_caps={"INVE-A.ST": 1e9, "INVE-B.ST": 5e9})
        self.assertEqual(dropped.get("INVE-A.ST"), "INVE-B.ST")

    def test_different_companies_never_merge(self):
        """CAT-B.ST is Catella and CATE.ST is Catena — similar tickers, not
        the same issuer."""
        dropped = scout.collapse_share_classes(
            set(self.NAMES), self.NAMES, holdings=set(), watch_tickers=set(),
            market_caps={})
        self.assertNotIn("CATE.ST", dropped)
        self.assertNotIn("CAT-B.ST", dropped)

    def test_a_single_class_ticker_is_untouched(self):
        dropped = scout.collapse_share_classes(
            {"EVO.ST"}, self.NAMES, set(), set(), {})
        self.assertEqual(dropped, {})


class TestSectorCap(unittest.TestCase):
    def test_no_lens_shortlist_is_dominated_by_one_sector(self):
        """Measured live before this cap existed: growth 8/10 Technology,
        contrarian 5/10 Real Estate. Five lenses that each pick one sector are
        not five perspectives."""
        scores = {f"T{i:02d}": {lens: 10 - i * 0.1 for lens in scout.LENSES}
                  for i in range(30)}
        sectors = {f"T{i:02d}": ("Technology" if i < 20 else "Healthcare")
                   for i in range(30)}
        lists = scout.lens_shortlists(scores, top_n=6, sectors=sectors, max_per_sector=3)
        for lens, names in lists.items():
            tech = sum(1 for n in names if sectors[n] == "Technology")
            self.assertLessEqual(tech, 3, f"{lens} took {tech} Technology slots")
            self.assertEqual(len(names), 6, "the cap must not shorten the shortlist")

    def test_yahoo_sector_aliases_are_folded_together(self):
        self.assertEqual(scout.normalise_sector("Financials"),
                         scout.normalise_sector("Financial Services"))
        self.assertEqual(scout.normalise_sector("Information Technology"), "Technology")
        self.assertIsNone(scout.normalise_sector(None))

    def test_unknown_sector_is_never_capped_away(self):
        scores = {f"T{i:02d}": {lens: 10 - i for lens in scout.LENSES} for i in range(8)}
        lists = scout.lens_shortlists(scores, top_n=5, sectors={}, max_per_sector=1)
        self.assertEqual(len(lists["value"]), 5)

    def test_backfill_keeps_the_shortlist_full_when_the_cap_bites(self):
        scores = {f"T{i:02d}": {lens: 10 - i for lens in scout.LENSES} for i in range(10)}
        sectors = {t: "Technology" for t in scores}
        lists = scout.lens_shortlists(scores, top_n=8, sectors=sectors, max_per_sector=2)
        self.assertEqual(len(lists["quality"]), 8)


class TestVerifyOrExit(unittest.TestCase):
    """The single-ticker write paths must REFUSE, not warn. verify_ticker
    returns a status string; an earlier version tested it for truthiness,
    which silently accepted every bad ticker."""

    def _patched(self, status, info):
        orig = wl.verify_ticker
        wl.verify_ticker = lambda t, n=None: (status, info)
        self.addCleanup(lambda: setattr(wl, "verify_ticker", orig))

    def test_unresolved_ticker_exits(self):
        self._patched("unresolved", {"error": "HTTP Error 404: Not Found"})
        with self.assertRaises(SystemExit) as cm:
            wl._verify_or_exit("ZZQQ.ST", "Not Real AB")
        self.assertIn("does not resolve", str(cm.exception))

    def test_wrong_company_exits(self):
        self._patched("name_mismatch", {"long_name": "Vitrolife AB (publ)"})
        with self.assertRaises(SystemExit) as cm:
            wl._verify_or_exit("VITR.ST", "Swedish Orphan Biovitrum AB")
        self.assertIn("Vitrolife", str(cm.exception))

    def test_a_good_ticker_returns_yahoos_name_not_the_typed_one(self):
        self._patched("ok", {"long_name": "Meko AB (publ)", "exchange": "STO",
                             "price": 72.6, "currency": "SEK"})
        self.assertEqual(wl._verify_or_exit("MEKO.ST", "Mekonomen AB"),
                         "Meko AB (publ)")


# ---------------------------------------------------------------------------
# 12. Missing data must not buy a shortlist slot.
#     Measured on the live 2026-08-24 universe: growth scores built on partial
#     data averaged |1.048| vs |0.396| for full-coverage names — 2.6x more
#     extreme, and a top-N shortlist is a cut on exactly those tails.
# ---------------------------------------------------------------------------
class TestCoverageShrinkage(unittest.TestCase):
    LENS = {"solo": {"a": "high", "b": "high", "c": "high", "d": "high"}}

    def _rows(self, n=40):
        """A spread of names so z-scores discriminate, plus two names with the
        same average signal but different amounts of evidence behind it."""
        rows = {f"T{i:02d}": {k: (i - n / 2) / 5 for k in "abcd"} for i in range(n)}
        rows["FULL"] = {"a": 3.0, "b": 3.0, "c": 3.0, "d": 3.0}
        rows["THIN"] = {"a": 3.0, "b": 3.0, "c": None, "d": None}
        return rows

    def test_a_thin_score_is_shrunk_toward_neutral(self):
        scores, _cov, fcov = scout.rank_lenses(self._rows(), lenses=self.LENS)
        self.assertEqual(fcov["THIN"]["solo"], (2, 4))
        self.assertEqual(fcov["FULL"]["solo"], (4, 4))
        self.assertLess(scores["THIN"]["solo"], scores["FULL"]["solo"],
                        "half the evidence must not score the same as all of it")

    def test_full_coverage_is_left_alone(self):
        """The correction must not quietly rescale names that have all their
        inputs — sqrt(K/K) is 1."""
        rows = self._rows()
        scores, _c, _f = scout.rank_lenses(rows, lenses=self.LENS)
        raw = statistics.fmean([
            scout.zscores({t: r["a"] for t, r in rows.items()})["FULL"],
            scout.zscores({t: r["b"] for t, r in rows.items()})["FULL"],
            scout.zscores({t: r["c"] for t, r in rows.items()})["FULL"],
            scout.zscores({t: r["d"] for t, r in rows.items()})["FULL"],
        ])
        self.assertAlmostEqual(scores["FULL"]["solo"], round(raw, 3), places=3)

    def test_shrinkage_is_exactly_sqrt_of_coverage(self):
        rows = self._rows()
        scores, _c, _f = scout.rank_lenses(rows, lenses=self.LENS)
        za = scout.zscores({t: r["a"] for t, r in rows.items()})
        zb = scout.zscores({t: r["b"] for t, r in rows.items()})
        expected = statistics.fmean([za["THIN"], zb["THIN"]]) * (2 / 4) ** 0.5
        self.assertAlmostEqual(scores["THIN"]["solo"], round(expected, 3), places=3)

    def test_a_thin_name_is_still_ranked_not_excluded(self):
        """Missing data lowers conviction; it never disqualifies."""
        scores, _c, _f = scout.rank_lenses(self._rows(), lenses=self.LENS)
        self.assertIsNotNone(scores["THIN"]["solo"])

    def test_thin_coverage_is_disclosed_in_the_candidate_csv(self):
        self.assertIn("thin_lenses", scout.DIGEST_COLUMNS)


class TestThinLensDisclosure(TestScoutHealth):
    def test_thin_lenses_column_is_populated_when_data_is_partial(self):
        self.write_universe([f"T{i:03d}" for i in range(self.UNIVERSE_SIZE)])
        self.write_portfolio(["T000"])
        recs = universe_records(self.UNIVERSE_SIZE)
        recs["T000"] = record()
        # a name with no forward-looking data at all — the real Nordic pattern
        recs["T005"] = record(fpe=None, peg=None)
        self._patch(recs)
        result = scout.run(Args())
        thin = result["candidates"].get("T005", {}).get("thin_lenses")
        self.assertTrue(thin, "a name missing forward data must be flagged thin")
        self.assertTrue(any("growth" in t for t in thin), thin)
