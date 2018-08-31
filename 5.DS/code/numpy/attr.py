# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([
    [1 + 1j, 2 + 4j, 3 + 7j],
    [4 + 2j, 5 + 5j, 6 + 8j],
    [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.dtype, a.dtype.str, a.dtype.char)
print(a.shape)
print(a.ndim)
print(a.size, len(a))
print(a.itemsize)
print(a.nbytes)
print(a.T)
print(a.real, a.imag, sep='\n')
for elem in a.flat:
    print(elem)
print(a.flat[[1, 3, 5]])
a.flat[[2, 4, 6]] = 0
print(a)


def fun(a, b):
    a.append(b)
    return a


x = np.array([10, 20, 30])
y = 40
x = np.array(fun(x.tolist(), y))
print(x)
x = np.append(x, 50)
print(x)
