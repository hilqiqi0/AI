# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 6)
print('a:', a)
b = np.arange(6, 9)
print('b:', b)
c = np.convolve(a, b, 'full')
print('c ( full):', c)
c = np.convolve(a, b, 'same')
print('c ( same):', c)
c = np.convolve(a, b, 'valid')
print('c (valid):', c)
