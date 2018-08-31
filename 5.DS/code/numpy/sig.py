# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
ax = mp.gca()
ax.set_ylim(-3, 3)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
pl = mp.plot([], [], c='orangered')[0]
pl.set_data([], [])


def update(data):
    t, v = data
    x, y = pl.get_data()
    x.append(t)
    y.append(v)
    x_min, x_max = ax.get_xlim()
    if t >= x_max:
        ax.set_xlim(t - (x_max - x_min), t)
        ax.figure.canvas.draw()
    pl.set_data(x, y)


def generator():
    t = 0
    while True:
        v = np.sin(2 * np.pi * t) * np.exp(
            np.sin(0.2 * np.pi * t))
        yield t, v
        t += 0.05
anim = ma.FuncAnimation(mp.gcf(), update,
                        generator, interval=5)
mp.show()
