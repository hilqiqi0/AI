# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.random.randint(10, 100, 9).reshape(3, 3)
print(a)
print(np.max(a), a.max())
print(np.min(a), a.min())
print(np.argmax(a), a.argmax())
print(np.argmin(a), a.argmin())
b = np.random.randint(10, 100, 9).reshape(3, 3)
print(b)
print(np.maximum(a, b))
print(np.minimum(a, b))
