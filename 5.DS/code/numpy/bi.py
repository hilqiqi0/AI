# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
outcomes = np.random.binomial(9, 0.5, 10000)
chips = [1000]
for outcome in outcomes:
    if outcome >= 5:
        chips.append(chips[-1] + 1)
    else:
        chips.append(chips[-1] - 1)
chips = np.array(chips)
mp.figure('Binomial', facecolor='lightgray')
mp.title('Binomial', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Chip', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
if chips[-1] < chips[0]:
    color = 'limegreen'
elif chips[-1] > chips[0]:
    color = 'orangered'
else:
    color = 'dodgerblue'
mp.plot(chips, c=color, label='Chip')
mp.legend()
mp.show()
