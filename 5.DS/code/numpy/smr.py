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
dates, bhp_closing_prices = np.loadtxt(
    '../../data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
_, vale_closing_prices = np.loadtxt(
    '../../data/vale.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
bhp_returns = np.diff(
    bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(
    vale_closing_prices) / vale_closing_prices[:-1]
N = 8
weights = np.hanning(N)  # 汉宁窗
weights /= weights.sum()
bhp_smooth_returns = np.convolve(
    bhp_returns, weights, 'valid')
vale_smooth_returns = np.convolve(
    vale_returns, weights, 'valid')
days = dates[N - 1:-1].astype(int)
degree = 3
bhp_p = np.polyfit(days, bhp_smooth_returns,
                   degree)
bhp_fitted_returns = np.polyval(bhp_p, days)
vale_p = np.polyfit(days, vale_smooth_returns,
                    degree)
vale_fitted_returns = np.polyval(vale_p, days)
sub_p = np.polysub(bhp_p, vale_p)
roots = np.roots(sub_p)
reals = roots[np.isreal(roots)].real
inters = []
for real in reals:
    if days[0] <= real <= days[-1]:
        inters.append(
            [real, np.polyval(bhp_p, real)])
inters.sort()
inters = np.array(inters)
mp.figure('Smoothing Returns',
          facecolor='lightgray')
mp.title('Smoothing Returns', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Returns', fontsize=14)
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
mp.plot(dates[:-1], bhp_returns, c='orangered',
        alpha=0.25, label='BHP')
mp.plot(dates[:-1], vale_returns, c='dodgerblue',
        alpha=0.25, label='VALE')
mp.plot(dates[N - 1:-1], bhp_smooth_returns,
        c='orangered', alpha=0.75,
        label='Smooth BHP')
mp.plot(dates[N - 1:-1], vale_smooth_returns,
        c='dodgerblue', alpha=0.75,
        label='Smooth VALE')
mp.plot(dates[N - 1:-1], bhp_fitted_returns,
        c='orangered', linewidth=3,
        label='Fitted BHP')
mp.plot(dates[N - 1:-1], vale_fitted_returns,
        c='dodgerblue', linewidth=3,
        label='Fitted VALE')
dates, returns = np.hsplit(inters, 2)
dates = dates.astype(int).astype(
    'M8[D]').astype(md.datetime.datetime)
mp.scatter(dates, returns, marker='x',
           c='firebrick', s=100, lw=3, zorder=3)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
