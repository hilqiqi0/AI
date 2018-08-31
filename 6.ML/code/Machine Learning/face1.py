# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
mp.figure('Olivetti Faces', facecolor='black')
mp.subplots_adjust(left=0.04, bottom=0, right=0.98,
                   top=0.96, wspace=0, hspace=0)
rows, cols = 10, 40
for row in range(rows):
    for col in range(cols):
        mp.subplot(rows, cols, row * cols + col + 1)
        mp.title(str(col), fontsize=8,
                 color='limegreen')
        if col == 0:
            mp.ylabel(str(row), fontsize=8,
                      color='limegreen')
        mp.xticks(())
        mp.yticks(())
        image = x[y == col][row].reshape(64, 64)
        mp.imshow(image, cmap='gray')
mp.show()
