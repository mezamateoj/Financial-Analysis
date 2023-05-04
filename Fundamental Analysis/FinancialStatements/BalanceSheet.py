
accounts_receivable = 1298
accounts_payable = 500
short_term_loans = 3357
long_term_loans = 8000
inventory = 5420
long_term_investments = 7892
property_plant_equipment = 9840

# Add up total current assets
total_current_assets = inventory + accounts_receivable

# Add up total non-current assets
total_non_current_assets = long_term_investments + property_plant_equipment

# Add up total current liabilities
total_current_liab = short_term_loans + accounts_payable

# Add up total non-current liabilities
total_non_current_liab = long_term_loans

assets = total_current_assets + total_non_current_assets
liabilities = total_current_liab + total_non_current_liab
equity = assets - liabilities

# Liquidity Ratios

# financial ratios. Measures the company's ability to pay off its short-term liabilities with its current assets
# a ratio of 1 or higher is considered good for short-term conditions.
current_ratio = total_current_assets / total_current_liab

# Leveraging Ratios

# debt to equity ratio. measure of the degree to which a company is financing its operations with debt
# https://www.investopedia.com/terms/d/debtequityratio.asp
# D/E varies by industry, but if it is too high, it could signal that a company is in financial trouble
debt_to_equity_ratio = liabilities / equity

# Equity Multiplier. Measures the portion of a company’s assets that is financed by shareholders' equity 
# A high equity multiplier indicates that a company is using a high amount of debt to finance its assets. 
# A low equity multiplier means that the company has less reliance on debt
equity_multiplier = assets / equity
# print("Equity Multiplier: " + str(equity_multiplier))

# Solvency Ratios

# Debt to Assets Ratio. Total amount of debt a company has relative to its assets
# compare one company's leverage with that of other companies in the same industry
# Ex: a ratio of 0.4, means its assets are financed by creditors, and 60% are financed by equity.
debt_to_assets_ratio = liabilities / assets
print("Debt to Assets Ratio: " + str(debt_to_assets_ratio))
