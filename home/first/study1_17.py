#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 从字典中提取子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 100}
tach_name = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tach_name}
print(p2)
print(p1)
p2 = {key: prices[key] for key in prices.keys() & tach_name}
print(p2)

# 映射名称到序列元素
# 类似C语言中的结构体
from collections import namedtuple
Subscr = namedtuple('Subscr', ['addr', 'joined'])
sub = Subscr('zl@qq.com', '2016-11-14')
print(sub)
print(sub.addr)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('Z', 100, 123.45)
print(s)
print(type(s))
# 元组不可变,改变要使用函数,而且它并不是在原来的数据上改变
# 它会创建一个全新的命名元组并将对应的字段用新的值取代。
s = s._replace(shares=76)
print(s)

Stock = namedtuple('Stock', ['name', 'age', 'sex', 'height'])

# 设置默认值


def dict_to_stock(s):
    ks = Stock('', None, 0, 178)
    return ks._replace(**s)
a = {'name': 'Zl', 'age': 24, 'sex': 1}
tmp = dict_to_stock(a)
print(tmp)
