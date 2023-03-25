import pandas as pd
import yfinance as yf
import requests
import config


# income statement function call
def income_statement(stock):
    r = requests.get(url=f"https://financialmodelingprep.com/api/v3/income-statement/{stock}?limit=120&apikey={config.KEY}")
    income = r.json()
    df = pd.DataFrame.from_dict(income)
    return df

def balance_sheet(stock):
    r = requests.get(url=f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?limit=120&apikey={config.KEY}")
    income = r.json()
    df = pd.DataFrame.from_dict(income)
    return df

def cash_flow(stock):
    r = requests.get(url=f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{stock}?limit=120&apikey={config.KEY}")
    income = r.json()
    df = pd.DataFrame.from_dict(income)
    return df

# Trailing 12 Months ratios
def ttm_ratios(stock):
    r = requests.get(url=f"https://financialmodelingprep.com/api/v3/ratios-ttm/{stock}?apikey={config.KEY}")
    ratios = r.json()
    df = pd.DataFrame.from_dict(ratios)
    return df


print(cash_flow('TSLA'))
# # Define the ticker symbol for the company you want to analyze
# ticker_symbol = 'AAPL'

# # Download the company's financial data using Yahoo Finance API
# company_data = yf.Ticker(ticker_symbol)

# # Extract the relevant financial statements
# income_statement = company_data.financials.loc[['Total Revenue', 'Net Income']]
# balance_sheet = company_data.balance_sheet.loc[['Total Current Assets', 'Total Current Liabilities']]
# cash_flow_statement = company_data.cashflow.loc[['Operating Cash Flow', 'Capital Expenditures']]

# # Calculate the financial ratios
# revenue = income_statement.loc['Total Revenue'][0]
# net_income = income_statement.loc['Net Income'][0]
# gross_profit_margin = (revenue - income_statement.loc['Cost of Revenue'][0]) / revenue
# net_profit_margin = net_income / revenue
# current_ratio = balance_sheet.loc['Total Current Assets'][0] / balance_sheet.loc['Total Current Liabilities'][0]
# operating_cash_flow = cash_flow_statement.loc['Operating Cash Flow'][0]
# capital_expenditures = cash_flow_statement.loc['Capital Expenditures'][0]
# free_cash_flow = operating_cash_flow - capital_expenditures

# # Print the financial ratios
# print('Gross Profit Margin:', gross_profit_margin)
# print('Net Profit Margin:', net_profit_margin)
# print('Current Ratio:', current_ratio)
# print('Free Cash Flow:', free_cash_flow)
