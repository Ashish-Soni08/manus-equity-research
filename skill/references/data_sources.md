# Data Sources & Collection Guide

## Automated Sources (via scripts/fetch_financials.py)

Run `python3 scripts/fetch_financials.py <TICKER> <OUTPUT_DIR>` to pull:

| Endpoint | Data Retrieved | Use Case |
|----------|---------------|----------|
| `get_stock_profile` | Business description, sector, employees, website | Company overview |
| `get_stock_financial_data` | Market cap, P/E, EV, margins, price targets | Valuation metrics |
| `get_stock_what_analyst_recommend` | Buy/hold/sell ratings by month | Sentiment analysis |
| `get_stock_holders` | Top institutional holders, insider transactions | Ownership analysis |
| `get_stock_insights` | Technical indicators, analyst trend scores | Trading signals |
| `get_stock_sec_filing` | Recent SEC filing links (10-K, 10-Q, 8-K) | Financial statements |
| `get_stock_chart` | 5-year monthly price history | Price chart, returns |

## Manual Research (via web browser)

These require browsing and extraction:

| Source | URL Pattern | Data |
|--------|------------|------|
| SEC EDGAR | `sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<TICKER>` | 10-K, 10-Q, earnings releases |
| Macrotrends | `macrotrends.net/stocks/charts/<TICKER>/...` | Historical financials, ratios |
| OpenInsider | `openinsider.com/screener?s=<TICKER>` | Insider transaction details |
| Earnings Transcripts | Search `<COMPANY> earnings call transcript` | Management commentary |
| Industry Reports | Search `<INDUSTRY> market size TAM` | TAM/SAM/SOM data |

## Data Extraction Checklist

For each company, collect and save to `data/` directory:

- [ ] Annual revenue (5+ years historical)
- [ ] Quarterly revenue (last 8 quarters)
- [ ] Income statement line items (COGS, OpEx breakdown, Net Income)
- [ ] Balance sheet (cash, debt, total assets/liabilities)
- [ ] Cash flow statement (operating CF, CapEx, FCF)
- [ ] Revenue segmentation (by product, geography, customer type)
- [ ] Guidance / forward estimates
- [ ] Analyst consensus ratings and price targets
- [ ] Insider transactions (last 90 days)
- [ ] Comparable company multiples (5-7 peers)
- [ ] Industry TAM and growth rates
- [ ] Key risks and upcoming catalysts
