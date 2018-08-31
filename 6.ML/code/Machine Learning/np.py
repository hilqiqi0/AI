# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# 原始样本
A = np.mat('3 2000; 2 3000; 4 5000; 5 8000; 1 2000',
           dtype=float)
print('A =', A, sep='\n')
# 均值为0，极差为1
mu = A.mean(axis=0)
s = A.max(axis=0) - A.min(axis=0)
X = (A - mu) / s
print('X =', X, sep='\n')
# 协方差矩阵
SIGMA = X.T * X
print('SIGMA =', SIGMA, sep='\n')
# 奇异值分解
U, S, V = np.linalg.svd(SIGMA)
print('U =', U, sep='\n')
# 主成分特征矩阵
U_reduce = U[:, 0]
print('U_reduce =', U_reduce, sep='\n')
# 降维样本
Z = X * U_reduce
print('Z =', Z, sep='\n')
# 恢复到均值极差转换之前
X_approx = Z * U_reduce.T
print('X_approx =', X_approx, sep='\n')
# 恢复到原始样本
A_approx = np.multiply(X_approx, s) + mu
print('A_approx =', A_approx, sep='\n')
