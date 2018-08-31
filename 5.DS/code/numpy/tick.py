# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
mp.figure()
locators = [
    'mp.NullLocator()',
    'mp.MaxNLocator(nbins=3, steps=[1, 3, 5, 7, 9])',
    'mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])',
    'mp.AutoLocator()',
    'mp.IndexLocator(offset=0.5, base=1.5)',
    'mp.MultipleLocator()',
    'mp.LinearLocator(numticks=21)',
    'mp.LogLocator(base=2, subs=[1.0])']
n_locators = len(locators)
for i, locator in enumerate(locators):
    mp.subplot(n_locators, 1, i + 1)
    mp.xlim(0, 10)
    mp.ylim(-1, 1)
    mp.yticks(())
    ax = mp.gca()
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_major_locator(eval(locator))
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
    mp.plot(np.arange(11), np.zeros(11), c='none')
    mp.text(5, 0.3, locator[3:], ha='center', size=12)
mp.tight_layout()
mp.show()
