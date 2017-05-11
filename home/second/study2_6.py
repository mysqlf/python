#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串忽略大小写的搜索替换
text = 'UPPER PYTHON, lower python, Mixed Python'
import re

# 使用 re 模块的时候给这些操作提供
#  re.IGNORECASE 标志参数
tmp = re.findall('python', text, flags=re.IGNORECASE)
print(tmp)
tmp = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(tmp)
# UPPER snake, lower snake, Mixed snake
#
# 替换字符串并不会自动跟被匹配字符串的大小写保持一致。


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
tmp = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(tmp)
