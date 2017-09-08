#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import numpy as np
import matplotlib.pyplot as plt
plt.Figure(figsize=(4,8))#创建图表1
plt.Figure(figsize=(4,8))#创建图表2
ax1=plt.subplot(211)#在图表2中创建子图1
ax2=plt.subplot(212)#在图表2中创建子图2
x=np.linspace(0,2,100)
for i in range(5):
    plt.Figure(figsize=(4,8))
    plt.plot(x,np.exp(i*x/3))
    plt.sca(ax1)
    plt.plot(x,np.sin(i*x))
    plt.sca(ax2)
    plt.plot(x,np.cos(i*x))
fig1 = plt.gcf()
#plt.show()
plt.draw()
fig1.savefig('pltsinco.png', dpi=100)
