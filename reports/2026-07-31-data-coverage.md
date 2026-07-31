# Data Coverage Report — 2026-07-31

Diagnostic report: what was actually fetched this sweep, what wasn't, and why. Not a portfolio-vs-market performance tracker — see `scripts/performance.py` + `data/valuations.csv` for that.

**Snapshot used:** `data/snapshots/20260731T093145.json` (fetched 2026-07-31T09:31:28.488551+00:00)

## Holdings — what was fetched this sweep

| Ticker | Name | Account | Status | Detail | Consecutive sweeps missing |
|---|---|---|---|---|---|
| CASH_SEK | Tax-reserve sparkonto (2027 deklaration - confirmed HB + SEB capital-gains tax) | hb-main | **N/A** | cash — not a market instrument |  |
| CASH_SEK | Handelsbanken normal/checking account | hb-checking | **N/A** | cash — not a market instrument |  |
| SHB-A.ST | Handelsbanken A (stock) | avanza-isk | **OK (price only)** | Yahoo's fundamentals endpoint (quoteSummary) is blocked in this environment; no free fundamentals source exists for non-US tickers (SEC EDGAR is US-listed-filer only). Price/momentum are real and fresh; market_cap/PE/margins/etc. are null, not estimated. |  |
| INVE-A.ST | Investor A (stock) | avanza-isk | **OK (price only)** | Yahoo's fundamentals endpoint (quoteSummary) is blocked in this environment; no free fundamentals source exists for non-US tickers (SEC EDGAR is US-listed-filer only). Price/momentum are real and fresh; market_cap/PE/margins/etc. are null, not estimated. |  |
| TBD | Avanza Auto 3 (fund) | avanza-isk | **N/A (permanent)** | UNLISTED FUND (user-confirmed 2026-07-31) - Avanza Auto 3 exists only on Avanza's own fund platform, not on a public exchange. No ticker/ISIN will ever resolve for it via Yahoo/SEC or any exchange-based fetch. This is PERMANENT, not a data gap awaiting a fix - do not keep re-flagging it as an open item each sweep. |  |
| TBD | Tundra Sustainable Frontier Fund A SEK | avanza-isk | **N/A** | no resolved ticker/ISIN on file yet — cannot be fetched until named |  |
| COIN-XBT.ST | CoinShares XBT Provider Bitcoin Tracker One (certificate) | avanza-isk | **ERROR** | yahoo chart unreachable: HTTP Error 404: Not Found (fallback path also failed) | 2 |
| TBD | Avanza Global (fund) | avanza-isk | **N/A (permanent)** | UNLISTED FUND (user-confirmed 2026-07-31) - Avanza Global exists only on Avanza's own fund platform, not on a public exchange. No ticker/ISIN will ever resolve for it via Yahoo/SEC or any exchange-based fetch. This is PERMANENT, not a data gap awaiting a fix - do not keep re-flagging it as an open item each sweep. |  |
| CASH_SEK | Avanza ISK available cash | avanza-isk | **N/A** | cash — not a market instrument |  |
| TBD | Swedbank fund | swedbank-fund | **N/A (permanent)** | LIKELY UNLISTED FUND (inferred 2026-07-31, NOT explicitly confirmed by user - flag if this differs): probably a Swedbank Robur-style fund on Swedbank's own platform, same structural situation as Avanza Auto 3/Avanza Global. Treated as probably-permanent pending user confirmation, not re-flagged as an urgent open item each sweep. |  |
| CASH_SEK | SEB fund proceeds - fully transferred to Avanza ISK 2026-07-20 | seb-fund | **N/A** | cash — not a market instrument |  |
| ethereum | ETH (self-custody wallet) | eth-wallet | **OK** | CoinGecko, 3 fields |  |
| CASH_USD | PayPal USD balance | paypal | **N/A** | cash — not a market instrument |  |
| CASH_EUR | PayPal EUR balance | paypal | **N/A** | cash — not a market instrument |  |

**Summary: 1 fully OK, 2 price-only (no free fundamentals source), 4 missing/error, 7 not applicable (cash / no ticker on file).**

**Flagged — failing for 2+ consecutive sweeps (a real gap, not a blip):**
- COIN-XBT.ST (CoinShares XBT Provider Bitcoin Tracker One (certificate)): 2 sweeps — yahoo chart unreachable: HTTP Error 404: Not Found (fallback path also failed)

## Screening universe / funnel — structural + empirical coverage

Structural = does a free fundamentals source even exist for this category (SEC EDGAR is US-filer-only, so only `sp500` ever has one). Empirical = from the last funnel ranking run.

| Category | Tickers | Have a free fundamentals source |
|---|---:|---:|
| us_mega_cap | 6 | 6 |
| us_quality_dividend | 6 | 6 |
| semis_and_ai_infra | 4 | 2 |
| nordic_large_cap | 10 | 0 |
| broad_index_etfs | 5 | 0 |
| crypto_usd_proxies | 2 | 0 |
| sp500 | 503 | 503 |
| europe_large_cap | 27 | 0 |
| thesis_candidates | 6 | 0 |

**Last funnel run** (data/rankings/20260729T150852-ranking.json, generated 2026-07-29T15:08:52.153526+00:00, categories: sp500,europe_large_cap,thesis_candidates): 449 full-factor ranked, 61 momentum-only (no fundamentals), 0 set aside (no data at all).

Full per-ticker universe coverage is in the accompanying CSV (too large for this table).
