# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(10)
print(a)
b = np.arange(1, 10)
print(b)
c = np.arange(1, 10, 2)
print(c)
d = np.array([])
print(d)
e = np.array([10, 20, 30, 40, 50])
print(e)
f = np.array([
    [1, 2, 3],
    [4, 5, 6]])
print(f)
print(type(f))
print(type(f[0][0]))
print(f.dtype)
g = np.array(['1', '2', '3'], dtype=np.int32)
print(type(g[0]))
print(g.dtype)
h = g.astype(np.str_)
print(type(h[0]))
print(h.dtype)
print(e.shape)
print(f.shape)
i = np.array([
    [np.arange(1, 5), np.arange(5, 9), np.arange(9, 13)],
    [np.arange(13, 17), np.arange(17, 21), np.arange(21, 25)]])
print(i.shape)
print(i)
