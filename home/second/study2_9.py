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

# 正则中使用unicode
import re
num = re.compile('\d+')
tmp = num.match('123')
print(tmp)
num = re.compile('\d+')
tmp = num.match('\u0661\u0662\u0663')
print(ascii(tmp))

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
tmp = pat.match(s)
print(ascii(tmp))


# 删除字符串中不需要的字符
s = ' hello world \n'
tmp = s.strip()
print(tmp)
tmp = s.lstrip()
print(tmp)
tmp = s.rstrip()
print(tmp)

t = '------hello =='
tmp = t.lstrip('-')
print(tmp)
tmp = t.strip('-=')
print(tmp)

s = ' hello     world  \n'
tmp = s.strip()
print(tmp)
tmp = s.replace(' ', '')
print(tmp)

tmp = re.sub('\s+', '', s)
print(tmp)

# 因为它不需要预先读取所有数据放到一个临时的列表中去。
# 它仅仅只是创建一个生成器，并且每次返回行之前会先执行 strip 操作。
with open('../../otherfile/test.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
