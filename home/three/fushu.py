#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 复数运算
a = complex(2, 4)
print(a)
b = 3 - 5j
print(b)
# 复数取实部
print(a.real)
# 复数取虚部
print(a.imag)
# 取共轭复数
print(a.conjugate())
print("-------------------")

# 复数运算
tmp = a + b
print(tmp)
tmp = a * b
print(tmp)
tmp = a / b
print(tmp)
tmp = abs(a)
print(tmp)
print("-------------------")
# 正弦余弦运算
import cmath
tmp = cmath.sin(a)
print(tmp)
tmp = cmath.cos(a)
print(tmp)
# 平方根
tmp = cmath.exp(a)
print(tmp)
print(cmath.sqrt(1))
print(cmath.sqrt(-1))
# (1+0j)
# 1j

print("-------------------")
# python 标准函数中不会产生复数,所以在标准函数中不会出现复数返回值
# 需要复数返回值必须显示调用cmath模块
import numpy as np
a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a)
print(a + 2)
print(np.sin(a))
