#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import random
# 整数
tmp = random.randint(1, 100)
print(tmp)
# 浮点数
tmp = random.random()
print(tmp)
# N位随机
tmp = random.getrandbits(200)
print(tmp)
t = bin(tmp)
print(t)


tmp = random.uniform(1, 3)
print(tmp)
