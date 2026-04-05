# Equity Research Analyst — Manus Prompt

> Copy everything below this line and paste it into a new Manus session. Replace `[INSERT TICKER HERE]` with any U.S.-listed ticker symbol.

---

Act as an expert Equity Research Analyst. Your task is to perform an end-to-end fundamental analysis on a specific publicly traded company and produce three professional deliverables: an Investment Memo Slide Deck, a Financial Model (Excel), and a Research Report (PDF/Markdown).

The target company is: **[INSERT TICKER HERE, e.g., PLTR, SNOW, CRM]**

Please execute the following 5-phase workflow sequentially. Do not skip steps.

### Phase 1: Data Collection & Research
1. Create a working directory for the project.
2. Write and execute a Python script to fetch live financial data, analyst ratings, and historical price data for the target ticker using Yahoo Finance APIs (specifically: `get_stock_profile`, `get_stock_financial_data`, `get_stock_what_analyst_recommend`, `get_stock_holders`, `get_stock_insights`, `get_stock_sec_filing`, `get_stock_chart`).
3. Use your browser tools to read the company's most recent 10-K/10-Q and earnings release from SEC EDGAR. Extract segment revenue, margin trends, and management guidance.
4. Research the competitive landscape, TAM/SAM, and key macro tailwinds/headwinds.
5. Save all extracted qualitative and quantitative data into structured Markdown notes in your working directory.

### Phase 1.5: Competitor Selection Checkpoint
Before building the financial model, pause and ask me the following:

> "For the Comparable Company Analysis, I need to select 5-7 peer companies to benchmark against. Comps are important because they help us determine whether the stock is cheap or expensive relative to similar companies — this directly influences the valuation conclusion.
>
> Based on my research, I've identified the following potential peers: [list the companies you found and briefly explain why each was selected].
>
> Do you have specific competitors you'd like me to include or exclude? Or should I proceed with this set?"

Wait for my response before continuing. If I say "proceed" or don't have preferences, use your selected set.

### Phase 2: Financial Modeling
Write and execute a Python script (using `openpyxl`) to build a comprehensive Excel Financial Model (`.xlsx`) with the following sheets:
1. **Income Statement**: 5 years of historical data + 5 years of projections.
2. **Balance Sheet**: 3 years historical + key ratios (current ratio, debt-to-equity).
3. **DCF Valuation**: Calculate WACC (using CAPM), project 10 years of Free Cash Flow, calculate Terminal Value, and derive an implied price per share.
4. **Comparable Company Analysis**: Use the agreed-upon 5-7 peers and compare EV/Revenue, EV/EBITDA, and revenue growth.
5. **Key Metrics**: Calculate the Rule of 40, FCF margin, and stock-based compensation as a % of revenue.

### Phase 3: Data Visualization
Write and execute a Python script (using `matplotlib`) to generate publication-quality PNG charts:
1. Revenue growth trajectory (bar chart with YoY growth line).
2. Valuation comps (horizontal bar chart comparing EV/Revenue multiples).
3. DCF sensitivity heatmap (implied price across various WACC and terminal growth rate scenarios).

### Phase 4: Research Report Generation
Draft a comprehensive Investment Memo in Markdown. The report must include:
- Executive Summary with a clear Buy/Hold/Sell recommendation.
- Business Model & Platform Ecosystem overview.
- Financial Analysis (revenue growth, profitability, cash flow).
- Competitive Landscape & Moat assessment.
- Bull vs. Bear case arguments with respective price targets.
- DCF Valuation summary and peer comps analysis.
- Key risks and upcoming catalysts.
Convert this Markdown file into a PDF using the `manus-md-to-pdf` utility.

### Phase 5: Investment Memo Slide Deck
Use the `slide_initialize` and `slide_edit` tools to create a 10-12 slide presentation summarizing the investment memo.
- **Design Guidelines**: Use a dark theme (#121212 background) with light text (#F8F9FA). Use teal (#20C997) for positive highlights and cyan (#00E5FF) for headers. Use Space Grotesk for headings and Inter for body text.
- **Structure**: Cover, Executive Summary, Business Model, Revenue Acceleration, Profitability, Rule of 40, Valuation Reality, DCF Valuation, Sensitivity, Bull vs. Bear, Recommendation.
- Embed the PNG charts generated in Phase 3 into the relevant slides.
- Ensure no slide exceeds a height of 720px (keep content concise and use horizontal layouts).
- Generate a professional cover image using your image generation tool.

Once all 5 phases are complete, use the `slide_present` tool to finalize the deck and deliver all three outputs (Slides, Excel, PDF) to me in your final message.
