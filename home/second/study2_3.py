#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用Shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
tmp = fnmatch('foo.txt', '*.txt')
print(tmp)
tmp = fnmatch('foo.txt', '?oo.txt')
print(tmp)
tmp = fnmatch('Dat1.csv', 'Dat[0-9].csv')
print(tmp)
tmp = fnmatch('Dat11.csv', 'Dat[0-9]*')
print(tmp)

names = ['Dat1.csv', 'Dat2.csv', 'donfig.ini', 'foo.py']
tmp = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(tmp)
# fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式
# 就是跟系统一致
tmp = fnmatch('foo.txt', '*.Txt')
print(tmp)
# True  我的系统大小写不区分
#
# 这种写法则严格区分大小写
tmp = fnmatchcase('foo.txt', '*.TXT')
print(tmp)

# 在处理非文件名的字符串时候它们也是很有用的。
# 比如，假设你有一个街道地址的列表数据：
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
tmp = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(tmp)

tmp = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(tmp)
# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。
#  如果在数据处理操作中只需要简单的通配符就能完成的时候，
#  这通常是一个比较合理的方案。
