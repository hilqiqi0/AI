# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import functools


def f1(a):
    return map(lambda x: x + 3, a)


def f2(a):
    return map(lambda x: x * 6, a)


def f3(a):
    return map(lambda x: x - 9, a)


def function_composer(*fs):
    return functools.reduce(
        lambda fa, fb: lambda x: fa(fb(x)), fs)


a = [1, 2, 3]
print(a)

# (a+3)x6-9
b = list(f3(f2(f1(a))))
print(b)

c = list(functools.reduce(
    lambda fa, fb: lambda x: fa(fb(x)), [f3, f2, f1])(a))
print(c)

d = list(function_composer(f3, f2, f1)(a))
print(d)
