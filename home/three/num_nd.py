#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
print(round(1.23, 1))
# 1.2
print(round(11.27, -1))

# 10.0
print(round(16.27, -1))

# 20.0
print(round(-1.27, -1))

#-0.0

tmpr = round(1.25361, 3)
print(tmpr)

# 1.254
tmp = 1.25361
tmpf = format(tmp, '0.3f')

print(tmpf)
print(tmp)

a = 1627731
# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下，
# 舍入运算会作用在十位、百位、千位等上面
print(round(a, -1))
# 1627730
print(round(a, -2))
# 1627700
print(round(a, -4))
# 1630000

a = 2.1
b = 4.2
c = a + b
print(c)
# 6.300000000000001
print(round(c, 2))
# 6.3

# 这个与输出一定宽度的
