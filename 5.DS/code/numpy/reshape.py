# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 9)
print(a)
b = a.reshape(2, 4)
print(b)
c = b.reshape(2, 2, 2)
print(c)
d = c.ravel()
print(d)
e = c.flatten()
print(e)
f = b.reshape(2, 2, 2).copy()
print(f)
a += 10
print(a, b, c, d, e, f, sep='\n')
a.shape = (2, 2, 2)
print(a)
a.resize(2, 4)
print(a)
#g = a.transpose()
#g = a.reshape(4, 2)
g = a.T
print(g)
# print(np.array([e]).T)
print(e.reshape(-1, 1))
