#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
#a_unicode=a.decode('utf-8')
strs = "菜鸟教程";
str_utf8 = strs.encode("UTF-8")
str_gbk = strs.encode("GBK")
str_un = strs.encode("unicode-escape")
print(strs)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("unicode 编码：", str_un)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
print("unicode 解码：", str_un.decode('unicode-escape','strict'))
#python 3 str 不能decode了,可以直接encode为目标编码
#如果是从网页抓取回来的数据
#则先使用decode处理
#再encode 为utf-8编码

def vardump(x):
    print(x)
for x in [1,10]:
    # yield x
    vardump(x)

def test_yield(x):
    i=0
    while i<x:
        yield i
        i=i+1

for x in test_yield(9):
    print(x)
