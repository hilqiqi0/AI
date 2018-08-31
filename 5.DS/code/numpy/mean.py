# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6), unpack=True)
mean = 0
for closing_price in closing_prices:
    mean += closing_price
mean /= closing_prices.size
print(mean)
mean = np.mean(closing_prices)
print(mean)
