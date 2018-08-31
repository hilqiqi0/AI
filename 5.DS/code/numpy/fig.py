# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
mp.figure('Figure Object 1', figsize=(6, 4), dpi=120,
          facecolor='lightgray')
mp.title('Figure Object 1', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.figure('Figure Object 2', figsize=(6, 4), dpi=120,
          facecolor='lightgray')
mp.title('Figure Object 2', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.figure('Figure Object 1')
mp.plot(x, cos_y, label=r'$y=\frac{1}{2}cos(x)$')
mp.legend()
mp.figure('Figure Object 2')
mp.plot(x, sin_y, label=r'$y=sin(x)$')
mp.legend()
mp.show()
