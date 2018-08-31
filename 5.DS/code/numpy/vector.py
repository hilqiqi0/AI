# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
n = 100000
start = dt.datetime.now()
A, B = [], []
for i in range(n):
    A.append(i ** 2)
    B.append(i ** 3)
C = []
for a, b in zip(A, B):
    C.append(a + b)
print((dt.datetime.now() - start).microseconds)
start = dt.datetime.now()
C = np.arange(n) ** 2 + np.arange(n) ** 3
print((dt.datetime.now() - start).microseconds)
