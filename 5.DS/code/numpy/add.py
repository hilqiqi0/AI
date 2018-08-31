# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 7)
print(a)
b = np.add.reduce(a)
print(b)
c = np.add.accumulate(a)
print(c)
d = np.add.reduceat(a, [0, 2, 4])
#
#   3   7  11
# 1 2 3 4 5 6
# 0   2   4
#
print(d)
e = np.add.outer([10, 20, 30], a)  # 外和
#  +  1  2  3  4  5  6
# 10 11 12 13 14 15 16
# 20 21 22 23 24 25 26
# 30 31 32 33 34 35 36
print(e)
f = np.outer([10, 20, 30], a)  # 外积
#  x  1  2  3  4  5  6
# 10
# 20
# 30
print(f)
