#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)
# 错误
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# 解决方法 #这个主要用于金融领域
import math
tmp = math.fsum(nums)
print(tmp)
