# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10).reshape(3, 3)
print(a)
b = a.clip(min=3, max=7)
print(b)
c = a.compress(3 < a.ravel()).reshape(-1, 3)
print(c)
d = a.compress(a.ravel() < 7).reshape(-1, 3)
print(d)
e = a.compress((3 < a.ravel()) & (a.ravel() < 7))
print(e)
f = a.prod()
print(f)
g = 1
for elem in a.flat:
    g *= elem
print(g)
h = a.cumprod()
print(h)
i = [1]
for elem in a.flat:
    i.append(i[-1] * elem)
i = np.array(i[1:])
print(i)


def jiecheng(n):
    if n == 1:
        return 1
    return n * jiecheng(n - 1)
print(jiecheng(9))
print(np.arange(1, 10).prod())
