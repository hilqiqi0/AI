# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np


def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = date.weekday()  # 用0-6表示周一到周日
    return wday

wdays, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    converters={1: dmy2wday})
ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    '''
    ave_closing_prices[wday] = \
        closing_prices[wdays == wday].mean()
    ave_closing_prices[wday] = \
        closing_prices[np.where(wdays == wday)].mean()
    '''
    ave_closing_prices[wday] = \
        np.take(closing_prices,
                np.where(wdays == wday)).mean()
for wday, ave_closing_price in zip(
        ['MON', 'TUE', 'WED', 'THU', 'FRI'],
        ave_closing_prices):
    print(wday, np.round(ave_closing_price, 2))
