#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 饼状图
import matplotlib.pyplot as plt
labels='Frogs','Hogs','Dogs','Logs'#名字根据抓取的来
size=[15,30,45,10]#比例大小,到时候可以使用计算得出
explode=(0,0,0,0)#间距这个可以设置为默认的
fig1,ax1=plt.subplots()
ax1.pie(size,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
