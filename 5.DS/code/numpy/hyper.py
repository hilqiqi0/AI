# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
outcomes = np.random.hypergeometric(25, 1, 3, 100)
scores = [0]
for outcome in outcomes:
    if outcome == 3:
        scores.append(scores[-1] + 1)
    else:
        scores.append(scores[-1] - 6)
scores = np.array(scores)
mp.figure('Hypergeometric',
          facecolor='lightgray')
mp.title('Hypergeometric', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
if scores[-1] < scores[0]:
    color = 'limegreen'
elif scores[-1] > scores[0]:
    color = 'orangered'
else:
    color = 'dodgerblue'
mp.plot(scores, c=color, label='Score')
mp.legend()
mp.show()
