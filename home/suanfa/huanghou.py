#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 皇后问题
# 
def col(m,col):
    #竖标记为1
    print(col)
    for x in range(0,len(m[col])):
        if m[x][col]==0:
            m[x][col]=1
    return m
def row(m,row):
    #横
    for x in range(0,len(m[row])):
        if m[row][x]==0:
            m[row][x]=1
    return m
    
def slash(m,row,col):
    #斜线标记
    #左下
    tmp=col
    for c in range(row+1,len(m[row])):
        tmp=tmp-1
        if tmp>=0 and m[c][tmp]==0:
            m[c][tmp]=1

    #右下
    j=col
    for c in range(row+1,len(m[row])):
        j=j+1
        if j<(len(m[row])) and m[c][j]==0:
            m[c][j]=1
    return m
# m=[[0 for i in range(6)]  for j in range(6)]
# shh=[] 
# for i in range(0,6):
#     for j in range(0,6):
#         if m[i][j]==0:
#             m[i][j]='*'
#             tmp=[i,j]
#             shh.append(tmp)
#             m=row(m,i)
#             m=col(m,j)
#             m=slash(m,i,j)

# print(shh)

        
import random
#随机模块

def conflict(state,col):
    #冲突函数，row为行，col为列
    row=len(state)
    for i in range(row):
        #对角线的行差不能等于列差
        if abs(state[i]-col) in (0,row-i):#重要语句
            return True
    return False
    
def queens(num=8,state=()):
    #生成器函数
    for pos in range(num):
        if not conflict(state, pos):
            if len(state)==num-1:
                yield(pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,)+result

def queenprint(solution):
    #打印函数
    def line(pos,length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print (line(pos))
        

for solution in list(queens(8)):
    print(solution) 
    
# print('  total number is '+str(len(list(queens())))) 
# print('  one of the range is:\n') 
queenprint(random.choice(list(queens())))
