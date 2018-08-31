# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('1 2 3; 8 9 4; 7 6 5')
#A = np.mat('1 2 3; 8 9 4')
print(A)
B = np.linalg.inv(A)
print(B)
C = A * B
print(C)
