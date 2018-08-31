# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([0, 1, -2, 3, 4])
b = np.array([-5, 6, 7, 8, -9])
#c = a ^ b
#c = a.__xor__(b)
c = np.bitwise_xor(a, b)
print(a, b, c)
print(np.where(c < 0)[0])
d = np.arange(1, 21)
print(d)
e = d & (d - 1)
print(e)
print(d[e == 0])
print(d[d & (d - 1) == 0])
