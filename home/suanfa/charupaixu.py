#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = [6, 7, 3, 2, 5, 8]
leng = len(a)
for j in range(leng):
    key = a[j]
    i = j-1
    while((i >= 0) and (a[i] > key)):
        a[i+1] = a[i]
        i = i-1
    a[i+1] = key
#print(a)
#插入排序
def crpx(a):
    for j in range(leng):
        key = a[j]
        i = j-1
        while((i >= 0) and (a[i] > key)):
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a
# python 实现，因为循环是从1开始
# 而数组下标是从0开始的，
# 所以这个判断条件是>=0




