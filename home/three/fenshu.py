#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 分数运算

from fractions import Fraction
a = Fraction(5, 4)
print(a)
b = Fraction(7, 16)
print(b)
print(a + b)
print(a * b)
c = a * b
# 分子
tmp = c.numerator
print(tmp)
# 分母
tmp = c.denominator
print(tmp)

tmp = float(c)
print(tmp)
print(c)
print(c.limit_denominator(8))
print(a.limit_denominator(4))
print("--------------------")
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
