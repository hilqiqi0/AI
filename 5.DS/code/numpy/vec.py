# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def fun(a, b):
    return a + b, a - b, a * b
A = np.array([10, 20, 30])
B = np.array([100, 200, 300])
C = np.vectorize(fun)(A, B)
print(C)
