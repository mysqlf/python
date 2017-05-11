#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
# 不会执行数组内的数值计算,而是将两个数组合并
tmp = x * 2
print(tmp)
# 数组合并
tmp = x + y
print(tmp)
# 基本的列表不能直接加一个int数,会报错


import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
tmp = ax * 2
print(tmp)
#[2 4 6 8]

tmp = ax + 10
print(tmp)
#[11 12 13 14]

tmp = ax + ay
print(tmp)
#[ 6  8 10 12]
tmp = ax * ay
print(tmp)
# 对整个数组中所有元素同时执行数学运算可以
# 使得作用在整个数组上的函数运算简单而又快速。
# 比如，如果你想计算多项式的值，可以这样做：


def f(x):
    return 3 * x**2 - 2 * x + 7
tmp = f(ax)
print(tmp)
#[ 8 15 28 47]
tmp = np.sqrt(ax)
print(tmp)


#grid = np.zeros(shape=(10000, 10000), dtype=float)
# print(grid)
#grid += 10
# print(grid)

# print(np.sin(grid))
# 有一点需要特别的主意，那就是它扩展Python列表的索引功能
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[:1])
#[[1 2 3 4]]

print(a[1, 1])
# 6
print(a[0, 0])
# 1
print(a[0][0])
# 1
# a[0][0]==a[0,0]
print(a[0:1, 2:])
#[ 7 11]
print(a[0:3, 2:3] + 10)

#[[16 17 18]]
