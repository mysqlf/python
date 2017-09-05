#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串中处理html
s = 'Elements are written as "<tag>text</tag>".'


import html

print(s)
print(html.escape(s))
tmp = html.escape(s)
print(html.escape(s, quote=False))
# 处理的是ASCII文本，并且想将非ASCII文本对应的编码实体嵌入进去，
# 可以给某些I/O函数传递参数errors='xmlcharrefreplace' 来达到这个目的。
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors="xmlcharrefreplace"))
# 替换文本中的编码实体
# 这段在IDE和cmd下运行会报错,因为python默认编码的问题.需要修改一下系统编码
# cmd不能很好地兼容utf8，而IDE就可以
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # IDE运行编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')#cmd运行编码

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))
