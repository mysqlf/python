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
print(a)
# python 实现，因为循环是从1开始
# 而数组下标是从0开始的，
# 所以这个判断条件是>=0


def mer(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def sorts(lists):
    if len(lists) <= 1:
        return lists
    mid1 = len(lists)/2
    print(mid1)
    mid = len(lists)//2
    print(mid)
    # 坑爹之处./除以返回的是浮点数
    # 要地板除才会返回整数
    left = sorts(lists[:mid])
    right = sorts(lists[mid:])
    return mer(left, right)


a = [3, 2, 4, 5, 6, 7, 8, 1, 9, 0]
print(sorts(a))
#
