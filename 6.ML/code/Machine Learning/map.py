# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def f1(x):
    return x + 3


x = 1
y = f1(x)
print(y)

X = [1, 2, 3]
#Y = list(map(f1, X))
Y = list(map(lambda x: x + 3, X))
print(Y)
