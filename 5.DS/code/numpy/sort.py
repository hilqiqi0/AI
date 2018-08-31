# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
names = np.array(['zhangsan', 'lisi', 'wangwu',
                  'zhaoliu', 'chenqi'])
scores = np.array([90, 70, 50, 80, 60])
ages = np.array([20, 30, 30, 20, 40])
# 按照年龄的升序打印姓名，
# 年龄相同的按成绩的升序
print(names[np.lexsort((scores, ages))])
c = ages + scores * 1j
print(c)
d = np.sort_complex(c)
print(d)
