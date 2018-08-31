# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
n_bubbles = 100
bubbles = np.zeros(n_bubbles, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4)])
bubbles['position'] = np.random.uniform(
    0, 1, (n_bubbles, 2))
bubbles['size'] = np.random.uniform(
    50, 750, n_bubbles)
bubbles['growth'] = np.random.uniform(
    30, 150, n_bubbles)
bubbles['color'] = np.random.uniform(
    0, 1, (n_bubbles, 4))
mp.figure('Bubbles', facecolor='lightgray')
mp.title('Bubbles', fontsize=20)
mp.xticks(())
mp.yticks(())
sc = mp.scatter(bubbles['position'][:, 0],
                bubbles['position'][:, 1],
                s=bubbles['size'],
                c=bubbles['color'])


def update(number):
    bubbles['size'] += bubbles['growth']
    burst = number % n_bubbles
    bubbles['position'][burst] = \
        np.random.uniform(0, 1, 2)
    bubbles['size'][burst] = 0
    bubbles['growth'][burst] = \
        np.random.uniform(30, 150)
    bubbles['color'][burst] = \
        np.random.uniform(0, 1, 4)
    sc.set_offsets(bubbles['position'])
    sc.set_sizes(bubbles['size'])
    sc.set_facecolor(bubbles['color'])
anim = ma.FuncAnimation(
    mp.gcf(), update, interval=10)
mp.show()
