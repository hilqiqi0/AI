# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        '../../data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})
mp.figure('Candlestick', facecolor='lightgray')
mp.title('Candlestick', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
    md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
rise = closing_prices - opening_prices >= 0.01
fall = opening_prices - closing_prices >= 0.01
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[rise], fc[fall] = (1, 1, 1), (0, 0.5, 0)
ec[rise], ec[fall] = (1, 0, 0), (0, 0.5, 0)
mp.bar(dates, highest_prices - lowest_prices, 0,
       lowest_prices, color=fc, edgecolor=ec)
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=fc, edgecolor=ec)
mp.gcf().autofmt_xdate()
mp.show()
