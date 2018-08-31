# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('3 -2; 1 0')
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
print(A * eigvecs[:, 0])
print(eigvals[0] * eigvecs[:, 0])
print(A * eigvecs[:, 1])
print(eigvals[1] * eigvecs[:, 1])
eigvals = np.linalg.eigvals(A)
print(eigvals)
