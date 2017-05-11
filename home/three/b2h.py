#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 进制转换
x = 1234
print(bin(x))
print(format(x, 'b'))
print(oct(x))
print(format(x, 'o'))
print(hex(x))
print(format(x, 'x'))
x = -1234
print(bin(x))
print(format(x, 'b'))
print(oct(x))
print(format(x, 'o'))
print(hex(x))
print(format(x, 'x'))

x = -1234
print(format(2**32 + x, 'b'))

print(format(2**32 + x, 'x'))

print(int('4d2', 16))
