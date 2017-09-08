#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 线加点
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
cases=[None,
    8,
    (30,8),
    [16,24,30],[0,-1],
    slice(100,200,3),
    0.1,0.3,1.5,
    (0.0,0.1),(0.45,0.1)]
figsize=(10,8)
cols=3
gs=gridspec.GridSpec(len(cases)//cols+1,cols)
delta=0.11
x=np.linspace(0,10-2*delta,200)+delta
y=np.sin(x)+1.0+delta
fig1=plt.figure(num=1,figsize=figsize)
ax=[]
for i,case in enumerate(cases):
    row=(i//cols)
    col=i%cols
    ax.append(fig1.add_subplot(gs[row,col]))
    ax[-1].set_title('makevery=%s'%str(case))
    ax[-1].plot(x,y,'o',ls='-',ms=4,markevery=case)

fig2=plt.figure(num=2,figsize=figsize)
axlog=[]
for i,case in enumerate(cases):
    row=(i//cols)
    col=i%cols
    axlog.append(fig2.add_subplot(gs[row,col]))
    axlog[-1].set_title('makevery=%s'%str(case))
    axlog[-1].set_xscale('log')
    axlog[-1].set_yscale('log')
    axlog[-1].plot(x,y,'o',ls='-',ms=4,markevery=case)
fig2.tight_layout()

fig3=plt.figure(num=3,figsize=figsize)
axzoom=[]
for i,case in enumerate(cases):
    row=(i//cols)
    col=i%cols
    axzoom.append(fig3.add_subplot(gs[row,col]))
    axzoom[-1].set_title('makevery=%s'%str(case))
    axzoom[-1].plot(x,y,'o',ls='-',ms=4,markevery=case)
    axzoom[-1].set_xlim((6,6.7))
    axzoom[-1].set_ylim((1.1,1.7))
fig3.tight_layout()
r=np.linspace(0,3.0,200)
theta=2*np.pi*r
fig4=plt.figure(num=4,figsize=figsize)
axpolar=[]
for i,case in enumerate(cases):
    row=(i//cols)
    col=i%cols
    #画子图add_subplot
    axpolar.append(fig4.add_subplot(gs[row,col],projection='polar'))
    axpolar[-1].set_title('makevery=%s'%str(case))
    axpolar[-1].plot(theta,r,'o',ls='-',ms=4,markevery=case)
fig4.tight_layout()
plt.draw()
fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
fig3.savefig('fig3.png')
fig4.savefig('fig4.png')
# plt.show()
