#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 求两个字典中的交集
a = {'x': 1, 'y': 2, 'z': 3}
b = {'x': 10, 'y': 2, 'w': 3}
# 键的交集
x = a.keys() & b.keys()
print(x)
# 键的差集
x = a.keys() - b.keys()
print(x)
# 交集
# 字典的 items() 方法返回一个包含(键，值)对的元素视图对象
x = a.items() & b.items()
print(x)
# 过滤字典元素
c = {key: a[key] for key in a.keys()-{'z', 'w'}}
print(c)
