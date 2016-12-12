#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 最短匹配模式
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
tmp = str_pat.findall(text1)
print(tmp)
text2 = 'Computer says "no." Phone says "yes."'
tmp = str_pat.findall(text2)
print(tmp)
# ['no.']
#['no." Phone says "yes.']
#
# 在模式中的*操作符后面加上?修饰符
str_pat = re.compile(r'\"(.*?)\"')
text1 = 'Computer says "no."'
tmp = str_pat.findall(text1)
print(tmp)
text2 = 'Computer says "no." Phone says "yes."'
tmp = str_pat.findall(text2)
print(tmp)
# ['no.']
# ['no.', 'yes.']


# 多行匹配模式

comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = ''' /* this is a
multiline comment */
'''
tmp = comment.findall(text1)
print(tmp)
tmp = comment.findall(text2)
print(tmp)
# 增加对换行的支持
comment = re.compile(r'/\*((?:.|\n)*?\*/)')
tmp = comment.findall(text2)
print(tmp)

# 第二个参数 re.DOTALL
# 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符。
comment = re.compile(r'(/\*(.*?)\*/)', re.DOTALL)
tmp = comment.findall(text2)
print(tmp)
