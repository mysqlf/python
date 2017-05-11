#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 时间模块
import calendar
cal = calendar.month(2016, 9)
# print(cal)
#    September 2016
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30
#
# calendar(year,w=2,l=1,c=6)
year = calendar.calendar(2016)
# print(year)
# 判断是否为闰年
x = calendar.isleap(2014)
# print(x)
#
# 统计一个时间段内闰年总数
y = calendar.leapdays(1900, 2016)
print(y)

m = calendar.monthcalendar(2016, 9)
print(m)

# [[0, 0, 0, 1, 2, 3, 4],
#  [5, 6, 7, 8, 9, 10, 11],
#  [12, 13, 14, 15, 16, 17, 18],
#  [19, 20, 21, 22, 23, 24, 25],
#  [26, 27, 28, 29, 30, 0, 0]]

m = calendar.monthrange(2016, 9)
print(m)
