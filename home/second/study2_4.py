#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 匹配或者搜索特定模式的文本
text = 'yeah, but no, but yeah, but no, but yeah'
tmp = text.find('yeah')
print(tmp)

import re
text = '11/27/2016'
text1 = 'Nov 27,2016'
if re.match(r'\d+/\d+/\d+', text):
    print('yes')
else:
    print('no')

# 将模式字符串预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
# match() 总是从字符串开始去匹配
if datepat.match(text):
    print('yes')
else:
    print('no')

tmp = datepat.match(text)
print(tmp)
# findall() 查找字符串任意部分的模式出现位置
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
tmp = datepat.findall(text)
print(tmp)

# 定义正则式的时候，通常会利用括号去捕获分组。
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/22/2016')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

month, day, year = m.groups()

x = datepat.findall(text)
print(x)

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))


for m in datepat.finditer(text):
    print(m.groups())

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
x = datepat.match('11/22/2012 asd')
print(x)
x = datepat.match('11/22/2012')
print(x)
