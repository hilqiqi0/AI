# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([('ABC', [1, 2, 3])], dtype='U3, 3i4')
print(a)
print(a[0]['f0'])
print(a[0]['f1'][0])
print(a[0]['f1'][1])
print(a[0]['f1'][2])
b = np.array([('ABC', [1, 2, 3])], dtype=[
    ('name', np.str_, 3), ('scores', np.int32, 3)])
print(b)
print(b[0]['name'])
print(b[0]['scores'][0])
print(b[0]['scores'][1])
print(b[0]['scores'][2])
c = np.array([('ABC', [1, 2, 3])], dtype={
    'names': ['name', 'scores'],
    'formats': ['U3', '3i4']})
print(c)
print(c[0]['name'])
print(c[0]['scores'][0])
print(c[0]['scores'][1])
print(c[0]['scores'][2])
d = np.array([('ABC', [1, 2, 3])], dtype={
    'name': ('U3', 0), 'scores': ('3i4', 12)})
print(d)
print(d[0]['name'])
print(d[0]['scores'][0])
print(d[0]['scores'][1])
print(d[0]['scores'][2])
e = np.array([0x1234], dtype=(
    '>u2', {'lo': ('u1', 0), 'hi': ('u1', 1)}))
print('{:x}'.format(e[0]))
print('{:x} {:x}'.format(e['lo'][0], e['hi'][0]))
