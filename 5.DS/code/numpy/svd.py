# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
M = np.mat('4 11 14; 8 7 -2')
print(M)
U, s, V = np.linalg.svd(M, full_matrices=False)
S = np.diag(s)
print(U, S, V, sep='\n')
print(U * U.T, V * V.T, sep='\n')
print(U * S * V)
