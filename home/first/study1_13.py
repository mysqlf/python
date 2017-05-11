#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
# 后面的会影响前面的数据下标顺序
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

rows_by_fname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_fname)
#  ↑
#  ||
#  ↓
rows_by_fname = sorted(rows, key=lambda r: r['lname'])
# itemgetter 适用于max等函数
x = max(rows, key=itemgetter('uid'))
print(x)
