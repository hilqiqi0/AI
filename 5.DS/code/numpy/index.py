# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)
print(a[0])
print(a[0][0])
print(a[0][0][0])
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i][j][k], a[i, j, k])
b = np.array([1, 2, 3], dtype=int)  # int->np.int32
print(b.dtype)
c = b.astype(float)  # float->np.float64
print(c.dtype)
d = c.astype(str)  # str->np.str_
print(d.dtype)
