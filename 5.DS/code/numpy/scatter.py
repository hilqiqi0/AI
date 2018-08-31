# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
d = np.sqrt(x ** 2 + y ** 2)
mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c=d, cmap='jet_r', alpha=0.5,
           marker='o')
mp.show()
