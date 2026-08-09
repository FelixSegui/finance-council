"""
Tests for scripts/derived_metrics.py. Uses the standard library's unittest -
no pytest dependency exists anywhere else in this repo, so this doesn't add
one. Run with: python3 -m unittest tests.test_derived_metrics -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import derived_metrics as dm  # noqa: E402


class TestBasicDerivations(unittest.TestCase):
    def test_capex_from_ocf_fcf(self):
        self.assertAlmostEqual(dm.capex_from_ocf_fcf(5904999936, 1570499968), 4334499968)

    def test_capex_missing_input(self):
        self.assertIsNone(dm.capex_from_ocf_fcf(None, 100))
        self.assertIsNone(dm.capex_from_ocf_fcf(100, None))

    def test_ebit_from_margin(self):
        self.assertAlmostEqual(dm.ebit_from_margin(0.16908, 35752001536), 6044948419.71, places=1)

    def test_ebit_from_margin_missing(self):
        self.assertIsNone(dm.ebit_from_margin(None, 100))

    def test_equity_from_book_value(self):
        self.assertAlmostEqual(dm.equity_from_book_value(8.76, 1813299480), 15884503444.8, places=1)

    def test_invested_capital_no_cash_netting(self):
        self.assertEqual(dm.invested_capital(total_debt=9146000384, equity=15884503444.8), 25030503828.8)

    def test_invested_capital_with_cash_netting(self):
        self.assertEqual(dm.invested_capital(total_debt=100, equity=200, cash=50), 250)

    def test_invested_capital_missing(self):
        self.assertIsNone(dm.invested_capital(None, 200))


class TestRoic(unittest.TestCase):
    def test_roic_requires_explicit_tax_rate(self):
        # No default tax rate assumption inside the function - caller must supply one.
        self.assertIsNone(dm.roic(ebit=1000, tax_rate=None, invested_capital_value=5000))

    def test_roic_basic(self):
        # EBIT 1000, tax 20%, invested capital 5000 -> (1000*0.8)/5000 = 0.16
        self.assertAlmostEqual(dm.roic(ebit=1000, tax_rate=0.20, invested_capital_value=5000), 0.16)

    def test_roic_zero_invested_capital_is_none(self):
        self.assertIsNone(dm.roic(ebit=1000, tax_rate=0.20, invested_capital_value=0))


class TestMarginsAndCoverage(unittest.TestCase):
    def test_fcf_margin(self):
        self.assertAlmostEqual(dm.fcf_margin(4905375232, 61366001664), 0.07994, places=4)

    def test_fcf_margin_missing(self):
        self.assertIsNone(dm.fcf_margin(None, 100))

    def test_net_debt_to_ebitda(self):
        # total_debt 32349999104, cash 4968000000 -> net_debt 27381999104; /ebitda 19904000000
        result = dm.net_debt_to_ebitda(total_debt=32349999104, cash=4968000000, ebitda=19904000000)
        self.assertAlmostEqual(result, 1.3757, places=4)

    def test_interest_coverage_zero_expense_is_none(self):
        # A real zero interest expense would read as "infinite coverage" - refuse rather than lie.
        self.assertIsNone(dm.interest_coverage(ebit=1000, interest_expense=0))

    def test_interest_coverage_basic(self):
        self.assertAlmostEqual(dm.interest_coverage(ebit=1000, interest_expense=250), 4.0)


class TestCagrAndVolatility(unittest.TestCase):
    def test_revenue_cagr_basic(self):
        # 100 -> 121 over 2 years = 10% CAGR
        result = dm.revenue_cagr({2024: 100, 2025: 110, 2026: 121})
        self.assertAlmostEqual(result, 0.10, places=4)

    def test_cagr_needs_two_points(self):
        self.assertIsNone(dm.revenue_cagr({2026: 100}))
        self.assertIsNone(dm.revenue_cagr({}))

    def test_cagr_negative_value_is_none(self):
        # A sign change makes CAGR undefined/misleading, not computable
        self.assertIsNone(dm.revenue_cagr({2024: -50, 2026: 100}))

    def test_eps_volatility_basic(self):
        # Perfectly stable series -> 0 volatility
        self.assertAlmostEqual(dm.eps_volatility({2024: 10, 2025: 10, 2026: 10}), 0.0)

    def test_eps_volatility_needs_two_points(self):
        self.assertIsNone(dm.eps_volatility({2026: 10}))

    def test_margin_stability_zero_mean_is_none(self):
        self.assertIsNone(dm.margin_stability({2024: -5, 2025: 5}))


if __name__ == "__main__":
    unittest.main()
