#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
"""
Topic: 星期中某一天最后出现的日期
Desc :
"""
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    print(day_num)

    day_num_target = weekdays.index(dayname)
    print(day_num_target)

    days_ago = (7 + day_num - day_num_target) % 7
    print(days_ago)
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(get_previous_byday('Monday'))
# 先将开始日期和目标日期映射到星期数组的位置上(星期一索引为0)，
# 然后通过模运算计算出目标日期要经过多少天才能到达开始日期。
# 然后用开始日期减去那个时间差即得到结果日期。

#
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d + relativedelta(weekday=FR))
print(d + relativedelta(weekday=FR(-1)))
