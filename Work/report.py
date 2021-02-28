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


# Read data files and create the report data

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')


#Calculate total cost of portfolio

portfolio_cost = 0.0
for s in portfolio:
    portfolio_cost += s['shares'] * s['price']
print('Value of the portfolio ', portfolio_cost)


#Calculate current value of the portfolio

portfolio_value = 0.0
for s in portfolio:
    portfolio_value += s['shares']*prices[s['name']]

print('Current value', portfolio_value)
print('Gain', portfolio_value - portfolio_cost)


#Takes a list of stocks and dictionary of prices as input and returns a list of tuples

def make_report(portfolio, prices):
    report = []
    for shares in portfolio:
        current_price = prices[shares['name']]
        change = current_price - shares['price']
        current_portfolio = (shares['name'], shares['shares'], current_price, change)
        report.append(current_portfolio)
    return report

report = make_report(portfolio, prices)


#Prints a nicely formatted table

def print_report(report):
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

print_report(report)
