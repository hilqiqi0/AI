# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
x, y = sd.make_circles(n_samples=500, factor=0.2,
                       noise=0.04)
model = dc.KernelPCA(kernel='rbf',
                     fit_inverse_transform=True,
                     gamma=10)
kpca_x = model.fit_transform(x)
mp.figure('Original', facecolor='lightgray')
mp.title('Original', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x[:, 0], x[:, 1], s=60, c=y, cmap='brg',
           alpha=0.5)
mp.figure('KPCA', facecolor='lightgray')
mp.title('KPCA', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(kpca_x[:, 0], kpca_x[:, 1], s=60, c=y,
           cmap='brg', alpha=0.5)
mp.show()
