# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import functools


def f1(x, y):
    print('f1:', x, y)
    return x + y


a = [1, 2, 3]
print(a)
b = sum(a)
print(b)
#c = functools.reduce(f1, a)
c = functools.reduce(lambda x, y: x + y, a)
print(c)
