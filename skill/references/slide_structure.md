# Investment Memo Slide Deck Structure

Standard 10-12 slide structure for equity research investment memos.

## Slide Outline

| # | Slide Title | Content | Chart/Visual |
|---|------------|---------|-------------|
| 1 | Cover | Company name, ticker, recommendation, target price, date, analyst | Cover image (generate with AI) |
| 2 | Executive Summary | Thesis in 1 paragraph + 5-6 key metrics table | None |
| 3 | Business Model | Platform/product ecosystem, moat, strategy | Optional: business model diagram |
| 4 | Revenue Acceleration | Revenue trajectory, growth drivers, guidance | Revenue growth bar+line chart |
| 5 | Revenue Mix | Segment breakdown, fastest-growing areas, deal metrics | Segment comparison grouped bars |
| 6 | Profitability | Margin expansion story, SBC normalization | Multi-line margin chart |
| 7 | Rule of 40 / Quality | Software quality benchmark, peer comparison | Stacked bar chart |
| 8 | Valuation Reality | Peer comps, multiple premium/discount analysis | Horizontal bar comps chart |
| 9 | DCF Valuation | Model assumptions, key outputs, implied price | Metrics table layout |
| 10 | Sensitivity | Scenario analysis across WACC/growth assumptions | Heatmap or scenario boxes |
| 11 | Bull vs Bear | Side-by-side bull/bear arguments with price targets | Two-column layout |
| 12 | Recommendation | Final verdict, action plan, catalysts to monitor | Banner + two-column layout |

## Slide Design Guidelines

- Use dark background (#121212) with light text (#F8F9FA) for a professional terminal aesthetic
- Accent colors: teal (#20C997) for positive/highlights, cyan (#00E5FF) for headers, red (#FF4B4B/#C00000) for warnings
- Font: Space Grotesk for headings, Inter for body text
- Each slide should have a thin accent line at the top left
- Charts should use Chart.js or be pre-generated as PNG images
- Keep text concise: max 3-4 key points per slide
- Use horizontal layouts (side-by-side columns) not vertical stacking

## Chart Data Preparation

Before generating slides, prepare a JSON file with chart data for the `generate_charts.py` script.
Charts are saved as PNG and referenced via absolute paths in slide HTML.
