#!/usr/bin/env python3
"""
Fetch financial data for a given ticker from Yahoo Finance APIs.

Usage:
    python3 fetch_financials.py <TICKER> <OUTPUT_DIR>

Example:
    python3 fetch_financials.py PLTR /home/ubuntu/equity-research/data
"""

import sys
import json
import os

sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_financials.py <TICKER> <OUTPUT_DIR>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    output_dir = sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)

    client = ApiClient()
    prefix = symbol.lower()

    endpoints = [
        ('YahooFinance/get_stock_insights', {'symbol': symbol}),
        ('YahooFinance/get_stock_sec_filing', {'symbol': symbol}),
        ('YahooFinance/get_stock_chart', {'symbol': symbol, 'interval': '1mo', 'range': '5y'}),
        ('YahooFinance/get_stock_holders', {'symbol': symbol}),
        ('YahooFinance/get_stock_profile', {'symbol': symbol}),
        ('YahooFinance/get_stock_what_analyst_recommend', {'symbol': symbol}),
        ('YahooFinance/get_stock_financial_data', {'symbol': symbol}),
    ]

    for endpoint, params in endpoints:
        name = endpoint.split('/')[-1].replace('get_stock_', '')
        print(f"Fetching {name}...")
        try:
            data = client.call_api(endpoint, query=params)
            filepath = os.path.join(output_dir, f"{prefix}_{name}.json")
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"  -> Saved {prefix}_{name}.json")
        except Exception as e:
            print(f"  -> Error: {e}")

    print(f"\nDone fetching all data for {symbol}.")

if __name__ == '__main__':
    main()
