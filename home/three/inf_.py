#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
a = float('inf')
print(a)
b = float('-inf')
print(b)
c = float('nan')
print(c)
import math
tmp = math.isinf(a)
print(tmp)
tmp = math.isnan(c)
print(tmp)
# 无穷大数在执行数学计算的时候会传播
a = float('inf')
print(a + 34)
# inf
print(10 / a)
# 0.0
print(a / a)
# nan
print(a + b)
# nan
# NaN值会在所有操作中传播，而不会产生异常。
c = float('nan')
print(c + 23)
# nan
print(c / 2)
# nan
print(c * 2)
# nan
# NaN值的一个特别的地方时它们之间的比较操作总是返回False。
d = float('nan')
print(c == d)
# False
