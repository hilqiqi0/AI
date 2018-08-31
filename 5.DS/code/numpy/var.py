# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6), unpack=True)
mean = np.mean(closing_prices)
devs = closing_prices - mean
pvar = (devs ** 2).mean()
pstd = np.sqrt(pvar)
print(pstd)
pstd = np.std(closing_prices)
print(pstd)
svar = (devs ** 2).sum() / (devs.size - 1)
sstd = np.sqrt(svar)
print(sstd)
sstd = np.std(closing_prices, ddof=1)
print(sstd)
