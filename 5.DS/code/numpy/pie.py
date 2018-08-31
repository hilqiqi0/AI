# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)
mp.pie(
    [26, 17, 21, 29, 11],
    [0.05, 0.01, 0.01, 0.01, 0.01],
    ['Python', 'JavaScript', 'C++', 'C', 'PHP'],
    ['dodgerblue', 'orangered', 'limegreen',
     'violet', 'gold'],
    '%d%%', shadow=True, startangle=90)
mp.axis('equal')
mp.show()
