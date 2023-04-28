import pandas as pd
import numpy as np
import requests
import json
import PortfolioConfig
# from pypfopt import EfficientFrontier, risk_return_analysis
# from pypfopt.expected_returns import mean_historical_return

API_KEY = PortfolioConfig.ALPHA_KEY

# Get the list of symbols
symbols = ['QQQ', 'VTI', 'AMD', 'KNSL', 'AXON', 'NVDA', 'MELI']

# Create a list to store the data
# data = []
# # Loop over the symbols
# for symbol in symbols:
#     # Get the data for the symbol
#     response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + symbol + '&outputsize=full&apikey=' + API_KEY)
#     # Check the response status code
#     if response.status_code == 200:
#         # Parse the JSON response
#         data_json = json.loads(response.content)

#         # Add the data to the list
#         data.append(data_json)
#     else:
#         # Print an error message
#         print('Error: ' + response.status_code)

# # Save the data to a file
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)

# # Print a message
# print('Data downloaded successfully.')

# Load the JSON data
with open('../data.json', 'r') as f:
    data = json.load(f)


symbols_json = []
for i in range(0, 6):
    symbols_json.append(data[i]['Meta Data']['2. Symbol'])

# print(data[0]['Meta Data']['2. Symbol'])
print(symbols_json)
# Create a Pandas dataframe


# df = pd.DataFrame(data)
# print(df.head(10))




# class StockPerformanceChecker:

#     def __init__(self, api_key):
#         self.api_key = api_key

#     def get_symbols(self):
#         # Get the list of available symbols
#         symbols = requests.get('https://api.iexcloud.io/v1/symbols', headers={'Authorization': 'Bearer ' + self.api_key}).json()

#         # Filter the symbols to only include stocks and bonds
#         symbols = [symbol for symbol in symbols if symbol['assetType'] in ['stock', 'bond']]

#         return symbols

#     def get_historical_prices(self, symbols, start_date, end_date):
#         # Get the historical prices for the symbols
#         prices = requests.get('https://api.iexcloud.io/v1/stock/prices?symbols=' + ','.join(symbols) + '&start=' + start_date + '&end=' + end_date, headers={'Authorization': 'Bearer ' + self.api_key}).json()

#         return prices

#     def compute_returns_and_covariance_matrix(self, prices):
#         # Compute the returns and covariance matrix
#         returns = pd.DataFrame(prices['prices']).pct_change()
#         cov_matrix = returns.cov()

#         return returns, cov_matrix

#     def find_optimal_weights(self, returns, cov_matrix, risk_free_rate):
#         # Create an efficient frontier object
#         ef = EfficientFrontier(returns, cov_matrix)

#         # Set the risk-free rate
#         ef.set_risk_free_rate(risk_free_rate)

#         # Find the optimal weights
#         weights = ef.min_var_portfolio()

#         return weights

#     def backtest_portfolio(self, returns, weights, risk_free_rate):
#         # Backtest the portfolio
#         returns_backtest = ef.backtest(returns, risk_free_rate)

#         return returns_backtest

#     def compare_portfolio_to_benchmark(self, returns, weights, benchmark, risk_free_rate):
#         # Compare the portfolio to a benchmark
#         benchmark_returns = df[benchmark]['returns']

#         # Compute the Sharpe ratio of the portfolio and the benchmark
#         sharpe_ratio_portfolio = risk_return_analysis.sharpe_ratio(returns_backtest, risk_free_rate)
#         sharpe_ratio_benchmark = risk_return_analysis.sharpe_ratio(benchmark_returns, risk_free_rate)

#         return sharpe_ratio_portfolio, sharpe_ratio_benchmark

#     def get_top_10_performing_stocks(self, returns, industry):
#         # Get the top 10 performing stocks of the day
#         top_10 = returns[returns['industry'] == industry].nlargest(10, 'returns')

#         return top_10

#     def check_top_10_performing_stocks_daily(self, start_date, end_date):
#         # Get the list of symbols
#         symbols = self.get_symbols()

#         # Get the historical prices for the symbols
#         prices = self.get_historical_prices(symbols, start_date, end_date)

#         # Compute the returns and covariance matrix
#         returns, cov_matrix = self.compute_returns_and_covariance_matrix(prices)

#         # Find the optimal weights
#         weights = self.find_optimal_weights(returns, cov_matrix, 0.01)

#         # Backtest the portfolio
#         returns_backtest = self.backtest_portfolio(returns, weights, 0.01)

#         # Compare the portfolio to a benchmark
#         sharpe_ratio_portfolio, sharpe_ratio_benchmark = self.compare_portfolio_to_benchmark(returns, weights, 'SPY', 0.01)

#         # Print the results
#         print('Portfolio weights:', weights)
#         print('Portfolio returns:', returns)
#         # print('Portfolio Sharpe ratio:', sharpe)
