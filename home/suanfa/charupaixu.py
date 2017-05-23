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
    # mid1 = len(lists)/2
    # print(mid1)
    mid = len(lists)//2
    print(mid)
    # 坑爹之处./除以返回的是浮点数
    # 要地板除才会返回整数
    left = sorts(lists[:mid])
    right = sorts(lists[mid:])
    return mer(left, right)


a = [3, 2, 4, 5, 6, 7, 8, 1, 9, 0]
#print(sorts(a))

#将字符串作为矩阵形式
#求对角线上最长的序列
def find_lcsubstr(s1, s2):   
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)] 
    #生成0矩阵，
    #为方便后续计算，比字符串长度多了一列  
    mmax=0   #最长匹配的长度  
    p=0  #最长匹配对应在s1中的最后一位  
    for i in range(len(s1)):  
        for j in range(len(s2)):  
            if s1[i]==s2[j]:  
                #如果字符相同，则对应标识加一
                #用于记录相同字串长度
                m[i+1][j+1]=m[i][j]+1  
                if m[i+1][j+1]>mmax:  
                #如果新的字串长度大于之前长度，更新长度
                    mmax=m[i+1][j+1]  
                    p=i+1  #记录最长字串末尾位置
    for x in range(len(s2)):
        print(m[x])
        print("\n")
    return s1[p-mmax:p],mmax   #返回最长子串及其长度  

print(find_lcsubstr('abcdfegse','abdfgabc'))   
#
