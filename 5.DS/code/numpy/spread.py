# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
highest_prices, lowest_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(4, 5), unpack=True)
max_highest_price, min_highest_price, \
    max_lowest_price, min_lowest_price = \
    highest_prices[0], highest_prices[0], \
    lowest_prices[0], lowest_prices[0]
for highest_price, lowest_price in zip(
        highest_prices, lowest_prices):
    if highest_price > max_highest_price:
        max_highest_price = highest_price
    if highest_price < min_highest_price:
        min_highest_price = highest_price
    if lowest_price > max_lowest_price:
        max_lowest_price = lowest_price
    if lowest_price < min_lowest_price:
        min_lowest_price = lowest_price
high_spread = max_highest_price - min_highest_price
low_spread = max_lowest_price - min_lowest_price
print(high_spread, low_spread)
high_spread = np.ptp(highest_prices)
low_spread = np.ptp(lowest_prices)
print(high_spread, low_spread)
