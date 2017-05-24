#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 
# 归并排序
# 合并数组
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

#拆分数组
def sorts(lists):
    if len(lists) <= 1:
        return lists
    mid = len(lists)//2
    print(mid)
    # 坑爹之处./除以返回的是浮点数
    # 要地板除才会返回整数
    left = sorts(lists[:mid])
    right = sorts(lists[mid:])
    return mer(left, right)


a = [3, 2, 4, 5, 6, 7, 8, 1, 9, 0]
#print(sorts(a))
