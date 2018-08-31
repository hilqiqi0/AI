# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# 1 1 2 3 5 8 13 21...
# fn = fn-1 + fn-2, n > 2, f1 = f2 = 1
n = 35


def fibo(n):
    return 1 if n < 3 else \
        fibo(n - 1) + fibo(n - 2)
print(fibo(n))
f1, f2 = 0, 1
for i in range(n):
    fn = f1 + f2
    f1, f2 = fn, f1
print(fn)
print(int((np.mat(
    '1. 1.; 1. 0.') ** (n - 1))[0, 0]))
r = np.sqrt(5)
print(int((((1 + r) / 2) ** n -
           ((1 - r) / 2) ** n) / r))
