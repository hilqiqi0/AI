# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
import mpl_finance as mf
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        '../../data/goog.csv', delimiter=',',
        usecols=(0, 1, 2, 3, 4), unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        skiprows=1)
mp.figure('Candlestick', facecolor='lightgray')
mp.title('Candlestick', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.MonthLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
dates = mf.date2num(dates)
ohlcs = np.column_stack((
    dates, opening_prices, highest_prices,
    lowest_prices, closing_prices))
mf.candlestick_ohlc(mp.gca(), ohlcs, 0.8,
                    'orangered', 'limegreen')
mp.gcf().autofmt_xdate()
mp.show()
