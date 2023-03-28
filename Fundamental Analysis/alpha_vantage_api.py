import requests
import pandas as pd
import config

# API key for Alpha Vantage API
API_KEY = config.ALPHA_KEY

# Company symbol for which financials are needed
symbol = input('Pleas provide a stock symbol: ')

# URL for getting balance sheet data
bs_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}'

# URL for getting income statement data
is_url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'

# URL for getting cash flow statement data
cf_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}'

# Fetch balance sheet data
bs_data = requests.get(bs_url).json()

# Fetch income statement data
is_data = requests.get(is_url).json()

# Fetch cash flow statement data
cf_data = requests.get(cf_url).json()

# Convert balance sheet data to Pandas dataframe
bs_df = pd.DataFrame(bs_data['annualReports']).T

# Convert income statement data to Pandas dataframe
is_df = pd.DataFrame(is_data['annualReports']).T

# Convert cash flow statement data to Pandas dataframe
cf_df = pd.DataFrame(cf_data['annualReports']).T

# Output the data to CSV files
bs_df.to_csv('balance_sheet.csv')
is_df.to_csv('income_statement.csv')
cf_df.to_csv('cash_flow.csv')
