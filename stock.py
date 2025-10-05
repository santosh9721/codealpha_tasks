 
stock_prices = {
    'AAPL': 180,
    'GOOGL': 138.21,
    'MSFT': 324.90,
    'TSLA': 250,
    'AMZN': 129.54
}

stock_holdings = {
    'AAPL': 10,
    'GOOGL': 5,
    'MSFT': 8,
    'TSLA': 3,
    'AMZN': 6
}

total_investment = 0
print("📈 Your Stock Portfolio:\n")

for symbol, shares in stock_holdings.items():
    price = stock_prices.get(symbol, 0)
