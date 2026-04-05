#!/usr/bin/env python3
"""
Generate professional charts for equity research presentations.

Usage:
    python3 generate_charts.py <TICKER> <DATA_JSON_PATH> <OUTPUT_DIR>

Reads a structured JSON data file and generates publication-quality charts:
  1. Revenue growth trajectory (bar + line combo)
  2. Revenue segment breakdown (grouped bars + growth rates)
  3. Profitability margin expansion (multi-line)
  4. Valuation comps (horizontal bar)
  5. DCF sensitivity heatmap
  6. Rule of 40 (stacked bar)

DATA_JSON_PATH should contain:
{
  "ticker": "PLTR",
  "revenue_chart": {
    "years": ["2020", "2021", ...],
    "revenue": [1.09, 1.54, ...],
    "growth": [47.1, 41.1, ...]
  },
  "segment_chart": {
    "segments": ["U.S. Commercial", "U.S. Government", "International"],
    "prior_year": [0.701, 1.197, 0.968],
    "current_year": [1.465, 1.855, 1.155],
    "growth_rates": [109, 55, 19]
  },
  "profitability_chart": {
    "years": ["2021", "2022", ...],
    "gross_margin": [...], "adj_op_margin": [...],
    "fcf_margin": [...], "net_margin": [...]
  },
  "comps_chart": {
    "companies": ["Palantir", "CrowdStrike", ...],
    "ev_revenue": [68.4, 22.7, ...]
  },
  "dcf_sensitivity": {
    "wacc_range": [10.0, 11.0, ...],
    "tgr_range": [2.0, 3.0, ...],
    "proj_fcf": [...],
    "net_cash": 7177,
    "shares": 2573,
    "current_price": 155
  },
  "rule_of_40": {
    "years": ["2021", "2022", ...],
    "rev_growth": [...],
    "adj_margin": [...]
  }
}
"""

import sys
import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Professional color palette
NAVY = '#1F4E79'
BLUE = '#2E75B6'
GREEN = '#548235'
GOLD = '#BF8F00'
RED = '#C00000'
LIGHT_BLUE = '#D6E4F0'

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.titlesize': 16,
    'axes.labelsize': 13,
    'figure.facecolor': 'white',
    'axes.facecolor': '#F8F9FA',
    'grid.alpha': 0.3,
})

def generate_revenue_chart(data, ticker, output_dir):
    """Revenue growth trajectory: bar + line combo chart."""
    rd = data.get('revenue_chart', {})
    years = rd.get('years', [])
    revenue = rd.get('revenue', [])
    growth = rd.get('growth', [])
    if not years:
        return
    fig, ax1 = plt.subplots(figsize=(12, 6))
    n_hist = len(years) - len([y for y in years if 'E' in str(y)])
    colors = [BLUE]*n_hist + [LIGHT_BLUE]*(len(years)-n_hist)
    bars = ax1.bar(years, revenue, color=colors, edgecolor=NAVY, linewidth=0.5, width=0.6, zorder=3)
    for bar, val in zip(bars, revenue):
        ax1.text(bar.get_x()+bar.get_width()/2., bar.get_height()+0.15,
                 f'${val:.1f}B', ha='center', va='bottom', fontweight='bold', fontsize=10, color=NAVY)
    ax2 = ax1.twinx()
    ax2.plot(years, growth, color=RED, marker='o', linewidth=2.5, markersize=8, zorder=4)
    for x, y in zip(years, growth):
        ax2.annotate(f'{y:.0f}%', (x, y), textcoords="offset points", xytext=(0, 12),
                    ha='center', fontsize=9, color=RED, fontweight='bold')
    ax1.set_ylabel('Revenue ($ Billions)', color=NAVY, fontweight='bold')
    ax2.set_ylabel('YoY Growth (%)', color=RED, fontweight='bold')
    ax1.set_title(f'{ticker} Revenue Growth Trajectory', fontweight='bold', color=NAVY, pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'revenue_growth.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved revenue_growth.png")

def generate_comps_chart(data, ticker, output_dir):
    """Valuation comparison horizontal bar chart."""
    cd = data.get('comps_chart', {})
    companies = cd.get('companies', [])
    ev_rev = cd.get('ev_revenue', [])
    if not companies:
        return
    fig, ax = plt.subplots(figsize=(12, 6))
    colors_v = [RED] + [BLUE]*(len(companies)-1)
    bars = ax.barh(companies, ev_rev, color=colors_v, edgecolor=NAVY, linewidth=0.5, height=0.5)
    for bar, val in zip(bars, ev_rev):
        ax.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2.,
                f'{val:.1f}x', va='center', fontweight='bold', fontsize=11)
    ax.set_xlabel('EV / Revenue Multiple', fontweight='bold')
    ax.set_title('Valuation Comparison: EV/Revenue', fontweight='bold', color=NAVY, pad=15)
    ax.invert_yaxis()
    median_val = np.median(ev_rev[1:]) if len(ev_rev) > 1 else ev_rev[0]
    ax.axvline(x=median_val, color=GOLD, linestyle='--', linewidth=2, alpha=0.8)
    ax.text(median_val+1, len(companies)-0.8, f'Peer Median: {median_val:.1f}x',
            color=GOLD, fontweight='bold', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'valuation_comps.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved valuation_comps.png")

def generate_dcf_sensitivity(data, ticker, output_dir):
    """DCF sensitivity heatmap."""
    sd = data.get('dcf_sensitivity', {})
    wacc_range = sd.get('wacc_range', [])
    tgr_range = sd.get('tgr_range', [])
    proj_fcf = sd.get('proj_fcf', [])
    net_cash = sd.get('net_cash', 0)
    shares = sd.get('shares', 1)
    current_price = sd.get('current_price', 0)
    if not wacc_range or not proj_fcf:
        return
    grid = []
    for w in wacc_range:
        row = []
        for tgr in tgr_range:
            w_d, tgr_d = w/100, tgr/100
            dfs = [1/(1+w_d)**i for i in range(1, len(proj_fcf)+1)]
            pv = sum(f*d for f, d in zip(proj_fcf, dfs))
            tv = proj_fcf[-1]*(1+tgr_d)/(w_d-tgr_d) if w_d > tgr_d else 0
            pv_tv = tv * dfs[-1]
            price = (pv + pv_tv + net_cash) / shares
            row.append(price)
        grid.append(row)
    fig, ax = plt.subplots(figsize=(10, 7))
    im = ax.imshow(np.array(grid), cmap='RdYlGn', aspect='auto')
    ax.set_xticks(range(len(tgr_range)))
    ax.set_xticklabels([f'{t:.1f}%' for t in tgr_range])
    ax.set_yticks(range(len(wacc_range)))
    ax.set_yticklabels([f'{w:.1f}%' for w in wacc_range])
    ax.set_xlabel('Terminal Growth Rate', fontweight='bold')
    ax.set_ylabel('WACC', fontweight='bold')
    ax.set_title(f'{ticker} DCF Sensitivity: Implied Share Price ($)', fontweight='bold', color=NAVY, pad=15)
    for i in range(len(wacc_range)):
        for j in range(len(tgr_range)):
            val = grid[i][j]
            color = 'white' if val < 30 or val > 80 else 'black'
            ax.text(j, i, f'${val:.0f}', ha='center', va='center', fontweight='bold', fontsize=10, color=color)
    if current_price:
        fig.text(0.5, 0.01, f'Current Market Price: ${current_price}',
                 ha='center', fontsize=11, style='italic', color=RED, fontweight='bold')
    plt.colorbar(im, ax=ax, label='Implied Price ($)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dcf_sensitivity.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved dcf_sensitivity.png")

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 generate_charts.py <TICKER> <DATA_JSON_PATH> <OUTPUT_DIR>")
        sys.exit(1)
    ticker = sys.argv[1].upper()
    data_path = sys.argv[2]
    output_dir = sys.argv[3]
    os.makedirs(output_dir, exist_ok=True)
    with open(data_path) as f:
        data = json.load(f)
    generate_revenue_chart(data, ticker, output_dir)
    generate_comps_chart(data, ticker, output_dir)
    generate_dcf_sensitivity(data, ticker, output_dir)
    print("\nAll charts generated.")

if __name__ == '__main__':
    main()
