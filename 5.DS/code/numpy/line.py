# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import pandas as pd
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
pred_prices = np.zeros(
    closing_prices.size - 2 * N + 1)
for i in range(pred_prices.size):
    a = np.zeros((N, N))
    for j in range(N):
        a[j, ] = closing_prices[i + j: i + j + N]
    b = closing_prices[i + N: i + N * 2]
    x = np.linalg.lstsq(a, b)[0]
    pred_prices[i] = b.dot(x)
print(pred_prices)
mp.figure('Stock Price Prediction',
          facecolor='lightgray')
mp.title('Stock Price Prediction', fontsize=20)
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
mp.plot(dates, closing_prices, 'o-',
        c='lightgray', label='Closing Price')
dates = np.append(
    dates, dates[-1] + pd.tseries.offsets.BDay())
mp.plot(dates[N * 2:], pred_prices, 'o-',
        c='orangered', label='Predicted Price')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
