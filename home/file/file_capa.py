#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 读取固定长度的字符
# rb 读取二进制
# rt 读取文本
# 后面那个 b/t指的是读取什么

from functools import partial
RECORD_SIZE=32
with open('byte.bin','rb') as f:
    records=iter(partial(f.read,RECORD_SIZE),b'')
    for r in records:
        print(r)
