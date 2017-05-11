#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  过滤序列元素
mylist = [1, 4, -5, 10, -7, 2, 3, -1, 0]
x = list(n for n in mylist if n % 2 == 0)  # 除以2余数为0
print(x)
x = list(n for n in mylist if n / 2 == 0)  # 除以2商为0
print(x)

x = (n for n in mylist if n > 0)
print(x)
for k in x:
    print(k)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
isvals = list(filter(is_int, values))
print(isvals)
import math
# sqrt开平方
x = [math.sqrt(n) for n in mylist if n > 0]
print(x)
# python 三目运算
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
x = list(compress(addresses, more5))
print(x)
