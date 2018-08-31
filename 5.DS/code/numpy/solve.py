# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('1 -2 1; 0 2 -8; -4 5 9')
B = np.mat('0; 8; -9')
X = np.linalg.solve(A, B)
print(X)
