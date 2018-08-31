# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.decomposition as dc
# 原始样本
A = np.mat('3 2000; 2 3000; 4 5000; 5 8000; 1 2000',
           dtype=float)
print('A =', A, sep='\n')
# PCA模型
model = pl.Pipeline([
    ('MinMaxScaler', sp.MinMaxScaler()),
    ('PCA', dc.PCA(n_components=1))])
# 降维样本
Z = model.fit_transform(A)
print('Z =', Z, sep='\n')
# 恢复原始样本
A_approx = model.inverse_transform(Z)
print('A_approx =', A_approx, sep='\n')
