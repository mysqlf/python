#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# #无限迭代器
import itertools
natu = itertools.count(1)  # 无限计算加1
# for n in natu:
#     print(n)

cs = itertools.cycle('ABC')  # 无限循环读取字符串
# for c in cs:
#     print(c)

# 根本停不下来
ns = itertools.repeat('A', 3)  # 可以设置循环次数
for x in ns:
    print(x)
# A
# A
# A

natu = itertools.count(1)  # 无限计算加1
ns = itertools.takewhile(lambda x: x <= 10, natu)
print(list(ns))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
