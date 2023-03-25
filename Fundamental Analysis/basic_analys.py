import pandas as pd
import yfinance as yf

# Define the ticker symbol for the company you want to analyze
ticker_symbol = 'AAPL'

# Download the company's financial data using Yahoo Finance API
company_data = yf.Ticker(ticker_symbol)

# Extract the relevant financial statements
income_statement = company_data.financials.loc[['Total Revenue', 'Net Income']]
balance_sheet = company_data.balance_sheet.loc[['Total Current Assets', 'Total Current Liabilities']]
cash_flow_statement = company_data.cashflow.loc[['Operating Cash Flow', 'Capital Expenditures']]

# Calculate the financial ratios
revenue = income_statement.loc['Total Revenue'][0]
net_income = income_statement.loc['Net Income'][0]
gross_profit_margin = (revenue - income_statement.loc['Cost of Revenue'][0]) / revenue
net_profit_margin = net_income / revenue
current_ratio = balance_sheet.loc['Total Current Assets'][0] / balance_sheet.loc['Total Current Liabilities'][0]
operating_cash_flow = cash_flow_statement.loc['Operating Cash Flow'][0]
capital_expenditures = cash_flow_statement.loc['Capital Expenditures'][0]
free_cash_flow = operating_cash_flow - capital_expenditures

# Print the financial ratios
print('Gross Profit Margin:', gross_profit_margin)
print('Net Profit Margin:', net_profit_margin)
print('Current Ratio:', current_ratio)
print('Free Cash Flow:', free_cash_flow)
