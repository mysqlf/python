#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf

#计算进程需要多少资源
#Max=最大,Allocation=现有
def cipher_need(Max,Allocation):
    need=[]
    for row in range(0,len(Max)):
        tmp_need=[]
        for col in range(0,len(Max[row])):
            tmp_need.append(Max[row][col]-Allocation[row][col])
        need.append(tmp_need)
    return need
#计算安排执行顺序
#need 需要,Available 系统空闲 Allocation 现有
def cipher_exce_order(need,Available,Allocation):
    is_exec=[]
    run=0
    while len(is_exec)<4:

        for row in range(0,len(need)):
            if row not in is_exec:
                more_flag=True
                #寻找需求小于系统现有资源的进程
                for col in range(0,len(need[row])):
                    if Available[col]<need[row][col]:
                        more_flag=False
                if  more_flag:
                    #如果系统现有资源大于进程所需资源，则分配资源，
                    for col in range(0,len(need[row])):
                        #回收资源
                        Available[col]=Available[col]+Allocation[row][col]
                    #记录执行记录    
                    is_exec.append(row)
        #每次循环必须寻找出至少一个可分配子程序
        #否则程序会进入死锁
        run=run+1
        if run > len(is_exec):
            return False
    return is_exec
#系统现有
Available=[1,5,2,0]
#进程现有
Allocation=[[0,0,1,4],[1,4,3,2],[1,3,5,4],[1,0,0,0]]
#最大需要
Max=[[0,6,5,6],[1,9,4,2],[1,3,5,6],[1,7,11,0]]

need=cipher_need(Max, Allocation)
print(need)
is_exec=cipher_exce_order(need, Available,Allocation)
print(is_exec)
