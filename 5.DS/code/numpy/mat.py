# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]])
print(a, type(a))
b = np.matrix(a, copy=False)
print(b, type(b))
c = np.mat(a)
print(c, type(c))
a *= 10
print(a, b, c, sep='\n')
d = np.mat('1 2; 3 4')
print(d)
e = np.mat('5 6; 7 8')
f = np.bmat('d e')
print(f)
g = np.bmat('d; e')
print(g)
h = d.I
print(h)
print(h * d)
i = f.I
print(i)  # 广义逆矩阵
j = np.array([
    [5, 6],
    [7, 8]])
k = a * j
print(a, j, k, sep='\n')
a = np.mat(a)
j = np.mat(j)
k = a * j
print(a, j, k, sep='\n')
