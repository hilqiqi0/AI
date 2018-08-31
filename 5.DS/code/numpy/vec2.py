# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def fun(a, b):
    return a + b, a - b, a * b
A = np.array([10, 20, 30])
B = np.array([100, 200, 300])
C = np.vectorize(fun)(A, B)
print(C)
C = np.frompyfunc(fun, 2, 3)(A, B)
print(C)


def foo(a):
    def bar(b):
        return a + b, a - b, a * b
    return np.frompyfunc(bar, 1, 3)
C = foo(100)(A)
print(C)
C = foo(B)(A)
print(C)
