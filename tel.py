#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tablib

# 号码段组合尾数


def addzero(num, tel):
    tmp = str(num)
    while len(tmp) < 4:
        tmp = '0'+tmp
    tel = tel+tmp
    return tel


# print(telhead)

# 一个号码段生成1W号码并写入文件


def maketel(tel, head):
    phone = []
    for z in range(0, 10000):
        phone.append((addzero(z, tel), '1'))
    phone = tablib.Dataset(*phone, headers=head)
    with open(str(x)+'.xlsx', 'wb') as f:
        f.write(phone.export('xlsx'))
# 打开文件读取号码段
# telhead = []
# with open('test.txt') as f:
#     for x in range(1, 500):
#         q = f.readline(7)
#         if q != '':
#             telhead.append(q)
# print(telhead)
#
# 读取号码的另一种写法
from functools import partial
telhead = []
with open('test.txt') as f:
    for tel in iter(partial(f.read, 7), ''):
        telhead.append(tel)

# head = ('tel', 'check')
# for x in telhead:
#     maketel(x, head)

# print(l)
# l = [('151'), ('165')]


# print(tel[:2])
# l = tablib.Dataset(*l, headers=head)
# print(l['tel'])
