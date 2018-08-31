# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import scipy.misc as sm
import sklearn.cluster as sc
import matplotlib.pyplot as mp
image = sm.imread('../../data/lily.jpg',
                  True).astype(np.uint8)
x = image.reshape(-1, 1)
model = sc.KMeans(n_clusters=2)
model.fit(x)
y = model.labels_
centers = model.cluster_centers_.squeeze()
z = centers[y]
quant = z.reshape(image.shape)
mp.figure('Original Image', facecolor='lightgray')
mp.title('Original Image', fontsize=20)
mp.axis('off')
mp.imshow(image, cmap='gray')
mp.figure('Quant Image', facecolor='lightgray')
mp.title('Quant Image', fontsize=20)
mp.axis('off')
mp.imshow(quant, cmap='gray')
mp.show()
