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
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        '../../data/bhp.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        dtype=np.dtype('M8[D], f8, f8, f8, f8'),
        converters={1: dmy2ymd})


def profit(opening_price, highest_price,
           lowest_price, closing_price):
    buying_price = opening_price * 0.99
    if lowest_price <= buying_price <= highest_price:
        return (closing_price -
                buying_price) * 100 / buying_price
    return np.nan
profits = np.vectorize(profit)(
    opening_prices, highest_prices,
    lowest_prices, closing_prices)
nan = np.isnan(profits)
dates, profits = dates[~nan], profits[~nan]
gain_dates, gain_profits = \
    dates[profits > 0], profits[profits > 0]
loss_dates, loss_profits = \
    dates[profits < 0], profits[profits < 0]
mp.figure('Trading Simulation',
          facecolor='lightgray')
mp.title('Trading Simulation', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Profit', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
    md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
if dates.size > 0:
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, profits, c='gray',
            label='Profit')
    mp.axhline(y=profits.mean(), linestyle='--',
               color='gray')
if gain_dates.size > 0:
    gain_dates = gain_dates.astype(
        md.datetime.datetime)
    mp.plot(gain_dates, gain_profits, 'o',
            c='orangered', label='Gain Profit')
    mp.axhline(y=gain_profits.mean(),
               linestyle='--', color='orangered')
if loss_dates.size > 0:
    loss_dates = loss_dates.astype(
        md.datetime.datetime)
    mp.plot(loss_dates, loss_profits, 'o',
            c='limegreen', label='Loss Profit')
    mp.axhline(y=loss_profits.mean(),
               linestyle='--', color='limegreen')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
