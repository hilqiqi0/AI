# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('2 1; 3 4')
print(A)
a = np.linalg.det(A)
print(a)
B = np.mat('3 2 1; 4 9 8; 5 6 7')
print(B)
b = np.linalg.det(B)
print(b)
