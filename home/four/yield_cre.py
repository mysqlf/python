#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
"""
Topic: 使用生成器创建新的迭代模式
Desc :
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in frange(0, 5, 0.5):
    print(n)
tmp = list(frange(0, 6, 0.6))
print(tmp)


def countdown(n):
    print('Start', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')
c = countdown(4)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print(next(c))
