# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
mp.figure('Explained Variance Ratio', facecolor='black')
mp.subplots_adjust(left=0.04, bottom=0, right=0.98,
                   top=0.96, wspace=0, hspace=0)
rows, cols = 11, 40
for row in range(rows):
    if row > 0:
        ncp = 140 - (row - 1) * 15
        model = dc.PCA(n_components=ncp)
        model.fit(x)
    for col in range(cols):
        mp.subplot(rows, cols, row * cols + col + 1)
        mp.title(str(col), fontsize=8,
                 color='limegreen')
        if col == 0:
            mp.ylabel(str(ncp) if row > 0 else 'orig',
                      fontsize=8, color='limegreen')
        mp.xticks(())
        mp.yticks(())
        if row > 0:
            pca_x = model.transform([x[y == col][0]])
            ipca_x = model.inverse_transform(pca_x)
            image = ipca_x.reshape(64, 64)
        else:
            image = x[y == col][0].reshape(64, 64)
        mp.imshow(image, cmap='gray')
mp.show()
