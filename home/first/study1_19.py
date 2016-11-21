#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
files = os.listdir('D:/Git/python/home')
if any(name.endswith('.py') for name in files):
    print('There be python')
else:
    print('Sorry , no python ')

nums = [1, 2, 3, 4, 5, 6]
s = sum(x * x for x in nums)  # 平方和

print(s)

s = ('AC', 50, 123.45)
print(','.join(str(x) for x in s))
