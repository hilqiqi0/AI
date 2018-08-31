# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)
mp.xlim(x.min() * 1.1, x.max() * 1.1)
mp.ylim(sin_y.min() * 1.1, sin_y.max() * 1.1)
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi * 3 / 4,
           np.pi],
          [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$',
           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$',
           r'$\pi$'])
mp.yticks([-1, -0.5, 0.5, 1])
ax = mp.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
mp.plot(x, cos_y, linestyle='-', linewidth=2,
        color='dodgerblue', label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_y, linestyle='-', linewidth=2,
        color='orangered', label=r'$y=sin(x)$')
mp.plot([xo, xo], [yo_cos, yo_sin], linestyle='--',
        linewidth=1, color='limegreen')
mp.scatter([xo, xo], [yo_cos, yo_sin], s=60,
           edgecolor='limegreen', facecolor='white',
           zorder=3)
mp.annotate(
    r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{4}$',
    xy=(xo, yo_cos), xycoords='data',
    xytext=(-90, -40), textcoords='offset points',
    fontsize=14,
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3, rad=.2'))
mp.annotate(
    r'$sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$',
    xy=(xo, yo_sin), xycoords='data',
    xytext=(20, 20), textcoords='offset points',
    fontsize=14,
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3, rad=.2'))
mp.legend(loc='upper left')
mp.show()
