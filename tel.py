#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tablib
l = []
with open('test.txt') as f:
    for x in range(1, 500):
        k = f.readline(7)
        if k != '':
            l.append(k)
print(l)
#l = [('151'), ('165')]
head = ('tel')

l = tablib.Dataset(*l)
print(l[:2])
