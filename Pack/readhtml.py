#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# print()函数的局限就是Python默认编码的局限，
# 因为系统是win7的，python的默认编码不是'utf-8',
# 改一下python的默认编码成'utf-8'就行了
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# IDE下输出则需要将IO修改为UTF-6
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# #命令行下输出需要将IO字符编码改为与系统一致
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_charref(self, name):
        print('&#%s' % name)

parser = MyHtmlParser()
x = parser.feed('''<html>
<head>汉字</head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML &nbsp; tutorial...<br>END</p>
</body></html>''')
print(x)
