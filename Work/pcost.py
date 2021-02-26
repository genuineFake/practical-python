# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                total_cost += float(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", shares)
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost ', cost)
