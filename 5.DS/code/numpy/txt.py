# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10).reshape(3, 3)
print(a)
np.savetxt('../../data/test.csv', a, delimiter=',',
           fmt='%d')
b = np.loadtxt('../../data/test.csv', delimiter=',',
               dtype='i4')
print(b)
c = np.loadtxt('../../data/test.csv', delimiter=',',
               usecols=(0, 2), dtype='i4')
print(c)
d, e = np.loadtxt('../../data/test.csv', delimiter=',',
                  usecols=(0, 2), unpack=True,
                  dtype='i4, f8')
print(d, e)
