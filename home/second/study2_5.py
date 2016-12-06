#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串搜索和替换
text = 'yeah, but no, but yeah, but no, but yeah'
tmp = text.replace('yeah', 'yep')
print(tmp)

import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
tmp = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(tmp)
# Today is 2012-11-27. PyCon starts 2013-3-13.
# sub() 函数中的第一个参数是被匹配的模式，
# 第二个参数是替换模式。
# 反斜杠数字比如 \3 指向前面模式的捕获组号。

from calendar import month_abbr

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

tmp = datepat.sub(change_date, text)
print(tmp)
