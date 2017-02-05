#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串中插入变量
s = '{name} has {n} message'
tmp = s.format(name='ZL', n=37)
print(tmp)

name = 'ZC'
n = '23'
tmp = s.format_map(vars())
print(tmp)


class Info:

    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('ZZ', 32)
tmp = s.format_map(vars(a))
print(tmp)


class safesub(dict):

    def __missing__(self, key):
        return '{' + key + '}'

del n
tmp = s.format_map(safesub(vars()))
print(tmp)
import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = "zz"
n = 12
print(sub('Hello {name}'))
print(sub('You have {n} message'))
print(sub('You favorite color is {color}'))
