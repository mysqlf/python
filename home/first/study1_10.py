#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在一个序列上面保持元素顺序的同时消除重复的值


# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
# return seen


# 消除重复元素


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [3, 1, 2, 4, 1, 2, 4, 5, 6, 7]
b = list(dedupe(a))
print(b)
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
b = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
print(b)
b = list(dedupe(a, key=lambda d: (d['x'])))
print(b)

# 读取文件去掉重复行
with open('../../otherfile/test.txt', 'r') as f:
    k = []
    for line in dedupe(f):
        k.append(line.strip('\n'))
print(k)
