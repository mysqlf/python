#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字典中的键映射多个值
from collections import defaultdict
# d = defaultdict(list)

# d['a'].append(1)
# d['b'].append(2)
# d['c'].append(3)
# print(d)
# d = defaultdict(set)
# d['a'].add(1)
# d['b'].add(2)
# d['c'].add(3)
# print(d)
# pairs = [('a', 2), ('b', 2), ('c', 2), ('d', 2), ('a', 2), ('b', 2)]
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)
# print(d)
d = defaultdict(list)
with open('../otherfile/test.txt') as f:
    for line in f.readlines():
        for key in line.split(' '):
            print(key)
