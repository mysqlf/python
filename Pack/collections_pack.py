#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# from collections import namedtuple
# # 二维坐标集示例
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# print(p.y)
# # 三维坐标
# Point = namedtuple('Point', ['x', 'y', 'z'])
# p = Point(1, 2, 3)
# print(p.x)
# print(p.y)
# print(p.z)
# print(isinstance(p, Point))
# print(isinstance(p, tuple))
# # 1
# # 2
# # 1
# # 2
# # 3
# # True
# # True
# from collections import deque
# # deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# q = deque(['a', 'b', 'c'])
# q.append('x')  # 尾部压入
# q.appendleft('y')  # 头部压入
# print(q)
# x = q.pop()  # 尾部弹出
# print(x)
# y = q.popleft()  # 头部弹出
# print(y)
#
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')  # 设置默认值
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# from collections import OrderedDict
# # 默认的dict是无序 的
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# #{'c': 3, 'a': 1, 'b': 2}
# print(d)
# # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# #OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# # print(od)
# # print(od.keys())
# # print(od['a'])
# # print(od['b'])
# 按照插入顺序排序 根据这个可以设计FIFO 先进先出
# from collections import OrderedDict


# class LastUpdateOrderDict(OrderedDict):

#     def __init__(self, capacity):
#         super(LastUpdateOrderDict, self).__init__()
#         self._capacity = capacity

#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add', (key, value))
#         OrderedDict.__setitem__(self, key, value)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# lasts = LastUpdateOrderDict(4)  # 初始化长度
# print(od['a'])
# # 测试添加值
# lasts.__setitem__('a', 1)
# lasts.__setitem__('b', 1)
# lasts.__setitem__('c', 1)
# lasts.__setitem__('d', 1)
# lasts.__setitem__('f', 1)
# add ('a', 1)
# add ('b', 1)
# add ('c', 1)
# add ('d', 1)
# remove ('a', 1)
# add ('f', 1)
# print(last._capacity)
#
# # 统计字符出现次数
# from collections import Counter
# c = Counter()
# for ch in 'asdfghzxcasdfgzxc':
#     c[ch] = c[ch] + 1
# print(c)
# #Counter({'g': 2, 'a': 2, 'd': 2, 'f': 2, 'x': 2, 'c': 2, 's': 2, 'z': 2, 'h': 1})
