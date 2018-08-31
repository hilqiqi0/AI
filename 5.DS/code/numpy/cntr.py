# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * \
    np.exp(-x ** 2 - y ** 2)
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(x, y, z, 8, cmap='jet')
cntr = mp.contour(x, y, z, 8, colors='black',
                  linewidths=0.5)
mp.clabel(cntr, inline_spacing=1,
          fmt='%.1f', fontsize=10)
mp.show()
