#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
files = os.listdir('D:/Git/python/home')
if any(name.endswith('.py') for name in files):
    print('There be python')
else:
    print('Sorry , no python ')


# 按照自己想要的方式切割字典
s = ('AC', 50, 123.45)
print(';'.join(str(x) for x in s))

# 使用一个生成器表达式作为参数会比先创建一个临时列表更加高效和优雅
nums = [1, 2, 3, 4, 5, 6]
s = sum(x * x for x in nums)  # 平方和
print(s)

# 这种会创建一个列表
s = sum([x*x for x in nums])
print(s)


portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_share = min(s['shares'] for s in portfolio)
print(min_share)

min_share = min(portfolio, key=lambda s: s['shares'])
print(min_share)
# 现在有多个字典或者映射，
# 你想将它们从逻辑上合并为一个单一的映射后执行某些操作，
# 比如查找值或者检查某些键是否存在。
a = {'x': 1, 'z': 3, 'y': 9, 't': 2}
b = {'y': 2, 'z': 4, 'x': 0, 's': 2}
# 解决方案就是使用
# collections 模块中的 ChainMap 类。
# 个人见解：
# ChainMap是加上元字典的名字组成一个新的有序字典，然后找要找的键值
# 然而实际是，根本不管原来的字典名，只是将两个字典暴力组合在一起,
# 应该是开辟了一个空间存储了两个字典的地址，字典的实时修改会实时反映
from collections import ChainMap
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(len(c))
print(c.keys())
print(list(c.keys()))
c['x'] = 100
print(a)
# del(c['s'])
# 删除失败因为这个只会操作第一个字典的数据，
# 第一个字典没有这个字段，就会报错
value = ChainMap()
value['x'] = 1
value = value.new_child()
value['x'] = 2
print(value)
value = value.new_child()
value['x'] = 3
print(value)
value = value.parents
print(value)

value = value.new_child()
value['x'] = 3
print(value)
value = value.parents
print(value)


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = {'x': 1, 'z': 1}
mer = dict(b)
# update会将数据整合在一起形成一个全新集合,
# 并且后面写入的会覆盖前面的键值相同的数据
# 页因为是新生成的数组，导致原数组的修改不会同步到这个数组里面来
mer.update(a)
print(mer)
mer.update(c)
print(mer)

c['z'] = 100
print(mer)
