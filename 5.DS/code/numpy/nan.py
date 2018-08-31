# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([1, 2, np.nan, 3, 4])
print(np.max(a), np.min(a))
print(np.argmax(a), np.argmin(a))
print(np.nanmax(a), np.nanmin(a))
print(np.nanargmax(a), np.nanargmin(a))
