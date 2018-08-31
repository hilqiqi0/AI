# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
d = np.sqrt(x ** 2 + y ** 2 + z ** 2)
mp.figure('Scatter3D')
ax = mp.gca(projection='3d')
mp.title('Scatter3D', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
ax.scatter(x, y, z, s=60, c=d, cmap='jet_r',
           alpha=0.5, marker='o')
mp.show()
