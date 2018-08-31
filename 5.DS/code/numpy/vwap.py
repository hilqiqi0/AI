# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices, volumes = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6, 7), unpack=True)
vwap, vsum = 0, 0
for closing_price, volume in zip(
        closing_prices, volumes):
    vwap += closing_price * volume
    vsum += volume
vwap /= vsum
print(vwap)
vwap = np.average(closing_prices, weights=volumes)
print(vwap)
