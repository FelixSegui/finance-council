"""
Layer B: quantitative metrics derived from Layer A (fetched/standardized raw
data). Pure functions only - no I/O, no fetching. This is the ONE place
these formulas live, so the Excel-import path and the direct-fetch path
never compute the same ratio two different, silently-diverging ways.

Every function returns None (never a fabricated number) when a required
input is missing - "prefer UNKNOWN over false precision" is the standing
rule for this whole system (see CLAUDE.md), and this module is where that
rule gets enforced for calculated, not just fetched, figures.
"""
import statistics


def _safe_div(numerator, denominator):
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def capex_from_ocf_fcf(operating_cashflow, free_cashflow):
    """Capex = OCF - FCF. Only meaningful when both come from the same
    source/period - don't mix a trailing FCF with an annual OCF."""
    if operating_cashflow is None or free_cashflow is None:
        return None
    return operating_cashflow - free_cashflow


def ebit_from_margin(operating_margin, revenue):
    """Approximation, not a filed figure - use only when a source's own
    EBIT/operating-income line is broken or absent (e.g. Yahoo's
    incomeStatementHistory module returns 0/None for these fields on many
    tickers, confirmed empirically 2026-08). Callers must tag the result
    ESTIMATED, not OK, since this is margin x revenue, not a reported line."""
    if operating_margin is None or revenue is None:
        return None
    return operating_margin * revenue


def equity_from_book_value(book_value_per_share, shares_outstanding):
    """Book equity, not market value - a real filed-data product, not a
    guess, but distinct from market cap."""
    if book_value_per_share is None or shares_outstanding is None:
        return None
    return book_value_per_share * shares_outstanding


def invested_capital(total_debt, equity, cash=None):
    """total_debt + equity, optionally netting out cash (the 'operating'
    invested-capital convention). Netting cash is opt-in via the `cash`
    argument so callers are explicit about which convention they're using -
    the two are not interchangeable and silently picking one would be
    exactly the kind of unlabeled methodology choice this system avoids."""
    if total_debt is None or equity is None:
        return None
    base = total_debt + equity
    return base - cash if cash is not None else base


def roic(ebit, tax_rate, invested_capital_value):
    """ROIC = EBIT * (1 - tax_rate) / invested_capital. `tax_rate` must be
    passed explicitly by the caller - this function never assumes one. If
    the caller only has an assumed statutory rate (not a real effective
    rate), that's a legitimate ESTIMATED input, but the caller must tag the
    result accordingly, not this function's job to guess a default."""
    if ebit is None or tax_rate is None or not invested_capital_value:
        return None
    return (ebit * (1 - tax_rate)) / invested_capital_value


def fcf_margin(fcf, revenue):
    return _safe_div(fcf, revenue)


def operating_margin(ebit, revenue):
    return _safe_div(ebit, revenue)


def net_debt_to_ebitda(total_debt, cash, ebitda):
    if total_debt is None or cash is None:
        return None
    net_debt = total_debt - cash
    return _safe_div(net_debt, ebitda)


def interest_coverage(ebit, interest_expense):
    if interest_expense == 0:
        return None  # avoid a divide-by-zero reading as "infinite coverage"
    return _safe_div(ebit, interest_expense)


def _cagr(first_value, last_value, years):
    if first_value is None or last_value is None or years is None or years <= 0:
        return None
    if first_value <= 0 or last_value <= 0:
        return None  # CAGR is undefined/misleading across a sign change
    return (last_value / first_value) ** (1 / years) - 1


def revenue_cagr(values_by_year):
    """values_by_year: {fiscal_year_int: value}, at least 2 points needed."""
    return _series_cagr(values_by_year)


def eps_cagr(values_by_year):
    return _series_cagr(values_by_year)


def fcf_cagr(values_by_year):
    return _series_cagr(values_by_year)


def _series_cagr(values_by_year):
    clean = {y: v for y, v in (values_by_year or {}).items() if v is not None}
    if len(clean) < 2:
        return None
    years = sorted(clean)
    span = years[-1] - years[0]
    return _cagr(clean[years[0]], clean[years[-1]], span)


def eps_volatility(values_by_year):
    """Coefficient of variation (stdev/mean) of a multi-year EPS series -
    scale-independent, so it's comparable across companies with very
    different absolute EPS. None if fewer than 2 points or mean is 0."""
    return _coefficient_of_variation(values_by_year)


def margin_stability(values_by_year):
    """Same coefficient-of-variation approach applied to a margin series
    (e.g. operating margin by year) - lower means more stable."""
    return _coefficient_of_variation(values_by_year)


def _coefficient_of_variation(values_by_year):
    clean = [v for v in (values_by_year or {}).values() if v is not None]
    if len(clean) < 2:
        return None
    mean = statistics.fmean(clean)
    if mean == 0:
        return None
    return statistics.pstdev(clean) / abs(mean)
