# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
ncps = range(10, 410, 10)
evrs = []
for ncp in ncps:
    model = dc.PCA(n_components=ncp)
    model.fit_transform(x)
    evr = model.explained_variance_ratio_.sum()
    evrs.append(evr)
mp.figure('Explained Variance Ratio',
          facecolor='lightgray')
mp.title('Explained Variance Ratio', fontsize=20)
mp.xlabel('n_components', fontsize=14)
mp.ylabel('Explained Variance Ratio', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(ncps, evrs, c='dodgerblue',
        label='Explained Variance Ratio')
mp.legend()
mp.show()
