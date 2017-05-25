#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 最长共同子串
#将字符串作为矩阵形式
#求对角线上最长的序列
#思维局限了所以想不到这些方法,需要学习
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
    for x in range(len(s2)+1):
        print(m[x])
        print("\n")
    return s1[p-mmax:p],mmax   #返回最长子串及其长度  

print(find_lcsubstr('abcdfegse','abdfgabc'))   
#
#最长非减序列  ---为毛加个0 就死了？ 
def long_add(s):
    m=[[1 for i in range(len(s)+1)] for j in range(len(s)+1)] 
    #生成0矩阵，
    #为方便后续计算，比字符串长度多了一列  
    mmax=0   #最长匹配的长度  
    p=0  #最长匹配对应在s1中的最后一位  
    for i in range(len(s)):  
        for j in range(i):  
            if i==j:
                continue;
            if int(s[i])>=int(s[j]):
                #因为位置相同所以不需要比较超过对角位置的数据
                m[i+1][j+1]=m[i][j]+1  
                if m[i+1][j+1]>mmax:  
                #如果新的字串长度大于之前长度，更新长度
                    mmax=m[i+1][j+1]  
                    p=i+1  #记录最长字串末尾位置
    for x in range(len(s)+1):
        print(m[x])
        print("\n")
    return s[p-mmax:p],mmax   #返回最长子串及其长度  
print(long_add('501123345678899101010303000023456'))  


def lists(s):
    if len(s)==1:
        return s
    d=[0 for i in range(len(s)+1)]
    sums=0
    ret=1
    for i in range(0, len(s)-1):
        d[i]=0
        for j in range(0,i):
            
            if s[j]<s[i] and d[j]>sums:
                sums=d[j]
        d[i]=sums+1
        sums=0
        if d[i]>ret:
            ret=d[i]
    return ret
s=[3,2,4,5,6,9,7,3,3,10]
print(lists(s))
