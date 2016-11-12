#!/usr/bin/env python
# -*- coding: utf-8 -*-
items = [0, 1, 2, 3, 4, 5, 6]
# 内置切片函数
a = slice(2, 4)
print(items[a])
items[a] = [8, 9]
print(items)
del items[a]
print(items)
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 6, 2)  # 开始：结束：步长
print(items[a])
