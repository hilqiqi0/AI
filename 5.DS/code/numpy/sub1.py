# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
mp.figure(facecolor='lightgray')
for i in range(2):
    for j in range(3):
        k = i * 3 + j + 1
        mp.subplot(2, 3, k)
        mp.xticks(())
        mp.yticks(())
        mp.text(0.5, 0.5, str(k), ha='center', va='center',
                size=36, alpha=0.5)
mp.tight_layout()
mp.show()
