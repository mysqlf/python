#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 文件查找的方法
#
filename = 'test.txt'
# 匹配字符尾 参数必须为元组
tmp = filename.endswith('.txt')
print(tmp)
# 匹配字符头
tmp = filename.startswith('file')
print(tmp)

import os
filename = os.listdir('.')
print(filename)
tmp = [name for name in filename if name.endswith(('.py', '.h'))]
print(tmp)
filename = ['123.jpg', '234.png', '345.zip', 'asd.exe']
tmp = [name for name in filename if name.endswith(('.png', '.jpg'))]
print(tmp)
tmp = any(name.endswith('.png') for name in filename)
print(tmp)
star = ['http:', 'https:', 'ftp:']
srars = ('http:', 'https:', 'ftp:')
file = 'test.txt'

tmp = file.startswith(tuple(star))
print(tmp)
# 检测某个目录下是否有该文件
tmp = any(name.endswith(('.py', '.h')) for name in os.listdir('.'))
print(tmp)
