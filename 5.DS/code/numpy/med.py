# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6), unpack=True)
sorted_prices = np.msort(closing_prices)
l = sorted_prices.size
median = (sorted_prices[int((l - 1) / 2)] +
          sorted_prices[int(l / 2)]) / 2
print(median)
median = np.median(closing_prices)
print(median)
