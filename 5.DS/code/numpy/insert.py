# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([1, 2, 4, 5, 6, 8, 9])
b = np.array([7, 3])
c = np.searchsorted(a, b)
print(c)
d = np.insert(a, c, b)
print(d)
