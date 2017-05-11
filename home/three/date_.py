#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
"""
Topic: 时间处理
Desc :
"""
from datetime import timedelta
a = timedelta(days=2, hours=6)
print(a)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.total_seconds() / 3600)
print(c.seconds / 3600)
from datetime import datetime
a = datetime(2017, 3, 30)
print(a + timedelta(days=10))

b = datetime(2017, 6, 10)
c = b - a
print(c)

print(c.days)

now = datetime.today()
print(now)
# datetime 会自动处理闰年

a = datetime(2016, 3, 1)
b = datetime(2016, 2, 28)
print((a - b).days)


a = datetime(2017, 3, 1)
b = datetime(2017, 2, 28)
print((a - b).days)

from dateutil.relativedelta import relativedelta

a = datetime(2016, 3, 1)
tmp = a + relativedelta(months=+1)
print(tmp)

b = datetime(2016, 4, 21)
d = b - a
print(d)

d = relativedelta(b, a)
print(d)

print(d.months)
print(d.days)
