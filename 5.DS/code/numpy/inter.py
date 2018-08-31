# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp
min_x, max_x = -2.5, 2.5
con_x = np.linspace(min_x, max_x, 1001)
con_y = np.sinc(con_x)
dis_x = np.linspace(min_x, max_x, 11)
dis_y = np.sinc(dis_x)
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 51)
lin_y = linear(lin_x)
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 51)
cub_y = cubic(cub_x)
mp.figure('Interpolation', facecolor='lightgray')
mp.subplot(221)
mp.title('Continuous', fontsize=16)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(con_x, con_y, c='hotpink',
        label='Continuous')
mp.legend()
mp.subplot(222)
mp.title('Discrete', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(dis_x, dis_y, c='orangered',
           label='Discrete')
mp.legend()
mp.subplot(223)
mp.title('Linear', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(lin_x, lin_y, 'o-', c='limegreen',
        label='Linear')
mp.scatter(dis_x, dis_y, c='orangered', zorder=3)
mp.legend()
mp.subplot(224)
mp.title('Cubic', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(cub_x, cub_y, 'o-', c='dodgerblue',
        label='Cubic')
mp.scatter(dis_x, dis_y, c='orangered', zorder=3)
mp.legend()
mp.tight_layout()
mp.show()
