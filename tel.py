#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tablib


def addzero(num, tel):
    tmp = str(num)
    while len(tmp) < 4:
        tmp = '0'+tmp
    tel = tel+tmp
    return tel
telhead = []
with open('test.txt') as f:
    for x in range(1, 500):
        q = f.readline(7)
        if q != '':
            telhead.append(q)
# for x in range(0, 10000):
#     tel.append((addzero(x, '1511263'), '1'))


def maketel(tel, head):
    phone = []
    for z in range(0, 10000):
        phone.append((addzero(z, tel), '1'))
    phone = tablib.Dataset(*phone, headers=head)
    with open(str(x)+'.xlsx', 'wb') as f:
        f.write(phone.export('xlsx'))
head = ('tel', 'check')
for x in telhead:
    maketel(x, head)

    # print(l)
    # l = [('151'), ('165')]


# print(tel[:2])
# l = tablib.Dataset(*l, headers=head)
# print(l['tel'])
