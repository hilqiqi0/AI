# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def pingfang(x):
    print('pingfang:', x)
    return x * x
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
Y = np.apply_along_axis(pingfang, 1, X)
print(Y)
