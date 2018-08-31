# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np


def dmy2days(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    days = (date - dt.date.min).days
    return days

days, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    converters={1: dmy2days})
twap, tsum = 0, 0
for closing_price, day in zip(
        closing_prices, days):
    twap += closing_price * day
    tsum += day
twap /= tsum
print(twap)
twap = np.average(closing_prices, weights=days)
print(twap)
