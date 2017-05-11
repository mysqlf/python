#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 以指定宽度格式化字符串
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
import os
print(textwrap.fill(s, 50))
print(textwrap.fill(s, os.get_terminal_size().columns, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))
#
# tmp = os.get_terminal_size().columns #获取终端的宽度
# print(tmp)
# 这段在编辑器直接运行会报错
