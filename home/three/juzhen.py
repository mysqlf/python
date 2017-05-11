#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, -8, 9]])
print(m)
# [[ 1 -2  3]
#  [ 0  4  5]
#  [ 7 -8  9]]

# 矩阵转换
tmp = m.T
print(tmp)
# [[ 1  0  7]
#  [-2  4 -8]
#  [ 3  5  9]]

tmp = m.I
print(tmp)
# [[-0.97435897  0.07692308  0.28205128]
#  [-0.44871795  0.15384615  0.06410256]
#  [0.35897436  0.07692308 - 0.05128205]]

v = np.matrix([[2, 3], [3, 4], [4, 5]])
print(v)

# 矩阵相乘
print(m * v)
# [[ 8 10]
#  [32 41]
#  [26 34]]


# a = 1234567890
# b = 1234567890
# print(a is b)

# a = 257
# b = 257
# print(a is b)

# a = 123
# b = 123
# print(a is b)

# a = -5
# b = -5
# print(a is b)


# a = -6
# b = -6
# print(a is b)
# is和==的区别
# is是要两个对象完全一样,内存空间都要一致才是一样
# 而==只需要内存空间内存的数值是相等就是相等

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, -8, 9]])
import numpy.linalg
tmp = numpy.linalg.det(m)
print(m)
tmp = numpy.linalg.eigvals(m)
print(tmp)
