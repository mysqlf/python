#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from itertools import *
count=0
for i in range(1,5):
    for j in range(1,5):
        if i==j:
            continue
        for k in range(1,5):
            if  (i!=k) and (j!=k):
                count=count+1
print(count)

count=0
for i in permutations('1234',3):
    count=count+1
print(count)

from itertools import count
for i in zip(count(1), ['a','b','c']):
    print(i)
