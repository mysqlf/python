#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将数据按某一列分组
# 实现类似 数据库的group by 功能
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby
# 先排序后分组
# groupby只检查连续的元素
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('', i)
# 将日期分组作为下标
from collections import defaultdict
row_by_date = defaultdict(list)
for row in rows:
    row_by_date[row['date']].append(row)
print(row_by_date)
