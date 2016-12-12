#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将Unicode文本标准化
s1 = 'Script javas\u00f1o'
s2 = 'Script javas\u0303o'

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(ascii(t1))
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(ascii(t1))


t1 = unicodedata.normalize('NFKD', s1)
t2 = unicodedata.normalize('NFKC', s2)
print(ascii(t1))
print(ascii(t2))
# 去掉变音符
t1 = unicodedata.normalize('NFD', s1)
tmp = ''.join(c for c in t1 if not unicodedata.combining(c))
print(tmp)
