# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {headers[0]: row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')


portfolio_cost = 0.0
for s in portfolio:
    portfolio_cost += s['shares'] * s['price']
print('Value of the portfolio ', portfolio_cost)

portfolio_value = 0.0
for s in portfolio:
    portfolio_value += s['shares']*prices[s['name']]

print('Current value', portfolio_value)
print('Gain', portfolio_value - portfolio_cost)
