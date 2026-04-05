---
name: equity-research-analyst
description: Automate the full equity research analyst workflow for any publicly traded company. Produces an investment memo (slides), financial model (Excel), and research report (Markdown + PDF) with a Buy/Hold/Sell recommendation. Use for equity research, stock analysis, investment memos, due diligence, valuation modeling, or comparable company analysis.
---

# Equity Research Analyst

Automate the end-to-end workflow of an equity research analyst: collect financial data, analyze fundamentals, build valuation models, and produce professional deliverables for any publicly traded company.

## Input

The user provides a **ticker symbol** (e.g., `PLTR`, `SNOW`, `CRM`). The company must be publicly traded on a U.S. exchange with SEC filings available.

## Output

Three deliverables:

1. **Investment Memo Slide Deck** — 10-12 slides via Manus slides tool
2. **Financial Model** — Excel workbook with DCF, comps, income statement, balance sheet
3. **Research Report** — Markdown document (+ PDF) with full analysis and sources

## Workflow

The process has 8 sequential phases. Complete each before moving to the next.

### Phase 1: Project Setup

```
mkdir -p /home/ubuntu/{ticker}-equity-research/{data,charts,output}
```

### Phase 2: Automated Data Collection

Run the fetch script to pull Yahoo Finance data:

```
python3 /home/ubuntu/skills/equity-research-analyst/scripts/fetch_financials.py <TICKER> /home/ubuntu/{ticker}-equity-research/data
```

### Phase 3: Manual Research & Extraction

Browse these sources and save findings to `data/` as Markdown files:

1. **SEC EDGAR** — Latest 10-K/10-Q and earnings release. Extract: revenue by segment, income statement, balance sheet, cash flow, guidance, SBC.
2. **Macrotrends** — Historical revenue, margins, ratios (5+ years).
3. **Financial news** — Recent earnings commentary, analyst upgrades/downgrades, insider activity.
4. **Industry context** — TAM/SAM estimates, competitive landscape, macro trends.

Save extracted data to:
- `data/{ticker}_financials_extracted.md` — Financial statements and metrics
- `data/{ticker}_business_competitive.md` — Business model, competitors, moat, risks
- `data/{ticker}_historical.md` — Historical data and market context

See `references/data_sources.md` for the full data collection checklist.

### Phase 4: Financial Model (Excel)

Build the Excel workbook with these sheets:

1. **Income Statement** — 5 years historical + 5 years projected. Highlight projection columns in yellow.
2. **Balance Sheet** — 3 years with key ratios (current ratio, debt-to-equity).
3. **DCF Valuation** — Assumptions section (WACC, terminal growth, beta, risk-free rate, ERP) + 10-year FCF projections + implied price per share.
4. **Comparable Company Analysis** — 5-7 peers with EV/Revenue, EV/EBITDA, P/E, revenue growth.
5. **Key Metrics** — Rule of 40, FCF yield, SBC as % of revenue, net retention if available.

Use `scripts/build_financial_model.py` as a starting point, or build directly with openpyxl. Key DCF formula:

```
Enterprise Value = PV(projected FCFs) + PV(terminal value)
Terminal Value = Final Year FCF × (1 + g) / (WACC - g)
Equity Value = Enterprise Value + Net Cash
Price/Share = Equity Value / Shares Outstanding
```

Save to `output/{TICKER}_Financial_Model.xlsx`.

### Phase 5: Chart Generation

Prepare a chart data JSON file and run:

```
python3 /home/ubuntu/skills/equity-research-analyst/scripts/generate_charts.py <TICKER> <DATA_JSON> /home/ubuntu/{ticker}-equity-research/charts
```

Or generate charts directly with matplotlib. Required charts:
- Revenue growth trajectory (bar + line)
- Valuation comps (horizontal bar)
- DCF sensitivity heatmap

Optional: segment breakdown, profitability margins, Rule of 40.

### Phase 6: Research Report (Markdown)

Write the full investment memo using `templates/investment_memo_template.md` as the structure. Include:
- All financial data with sources cited
- DCF results and sensitivity ranges
- Bull/bear case with price targets
- Clear Buy/Hold/Sell recommendation with rationale

Save to `output/{TICKER}_Investment_Memo.md`.

### Phase 7: Investment Memo Slides

Create a 10-12 slide deck using the Manus slides tool. See `references/slide_structure.md` for the standard outline and design guidelines.

Key design principles:
- Dark background (#121212), light text (#F8F9FA)
- Accent: teal (#20C997) for highlights, cyan (#00E5FF) for headers
- Fonts: Space Grotesk (headings), Inter (body)
- Horizontal layouts, max 3-4 points per slide
- Reference chart PNGs from `charts/` directory via absolute paths

Generate a cover image using the AI image generator with a professional financial/tech aesthetic.

### Phase 8: Final Assembly & Delivery

1. Convert Markdown report to PDF: `manus-md-to-pdf output/{TICKER}_Investment_Memo.md output/{TICKER}_Investment_Memo.pdf`
2. Present slides via `slide_present`
3. Deliver all files to user: slides, Excel, Markdown, PDF

## DCF Calibration Notes

- **WACC**: Use CAPM. Typical range 10-16% for high-growth tech. Risk-free rate ~4.3%, ERP ~5.5%.
- **Beta**: Use Yahoo Finance reported beta. If >2.0, consider capping at 2.0 with justification.
- **Terminal growth**: 2-5% depending on industry. 3-4% is standard for tech.
- **FCF projections**: Base on historical FCF margins, guided revenue growth, and gradual margin expansion.
- **Sanity check**: Reverse-engineer the market-implied WACC from the current stock price. If implied WACC < risk-free rate, the stock is likely overvalued by DCF.
- **Sensitivity**: Always present optimistic / base / bear scenarios.

## Key Principles

- Use only real, verifiable data. Never fabricate financial figures.
- Cite all data sources in the report.
- Let the analysis drive the recommendation — approach neutrally.
- The DCF is one input, not the sole determinant. Weight qualitative factors (moat, management, catalysts).
- For high-growth companies, DCF often undervalues. Acknowledge this and use comps as a cross-check.
