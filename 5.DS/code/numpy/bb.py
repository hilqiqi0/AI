# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd
dates, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
N = 5
medios = np.convolve(closing_prices,
                     np.ones(N) / N, 'valid')
stds = np.zeros(medios.size)
for i in range(stds.size):
    stds[i] = np.std(closing_prices[i:i + N])
lowers = medios - 2 * stds
uppers = medios + 2 * stds
mp.figure('Bollinger Bands', facecolor='lightgray')
mp.title('Bollinger Bands', fontsize=20)
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
mp.plot(dates, closing_prices, c='lightgray',
        label='Closing Price')
mp.plot(dates[N - 1:], medios, c='dodgerblue',
        label='Medio')
mp.plot(dates[N - 1:], lowers, c='limegreen',
        label='Lower')
mp.plot(dates[N - 1:], uppers, c='orangered',
        label='Upper')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
