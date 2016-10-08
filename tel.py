#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
l = []
with open('test.txt') as f:
    for x in range(1, 500):
        k = f.readline(7)
        if k != '':
            l.append(k)
f.close()
