#!/usr/bin/env python
# -*- coding: utf-8 -*-
line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
# 多种分割
tmp = re.split(r'[;,\s]\s*', line)
print(tmp)
# 捕获分隔符
tmp = re.split(r'(,|;|\s)\s*', line)
print(tmp)
# 不捕获分隔符
tmp = re.split(r'(?:,|;|\s)\s*', line)
print(tmp)
field = re.split(r'(,|;|\s)\s*', line)
values = field[0::2]  # 切片每两个取一个
print(values)
delim = field[1::2]+['']
print(delim)
# zip 将两个list合并
p = ''.join(v+d for v, d in zip(values, delim))
print(p)
