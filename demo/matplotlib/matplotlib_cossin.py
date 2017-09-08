#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from pylab import *
#创建一个8*6的图,设置分辨率为80

#基本版
def base():
    Figure(figsize=(8,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=1.0,linestyle='-')
    #绘制正弦曲线
    plot(X,S,color='green',linewidth=1.0,linestyle="-")
    #设置x的范围
    xlim(-4.0,4.0)
    #设置横轴记号
    #-4,4指范围,5指在轴上显示几个数字
    xticks(np.linspace(-4,4,5,endpoint=True))
    #设置y轴范围
    ylim(-1.0,1.0)
    yticks(np.linspace(-1,1,5,endpoint=True))
    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
#base()
#
#线条加粗版
#
def line_up():
    Figure(figsize=(10,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=2.5,linestyle='-')
    #绘制正弦曲线
    plot(X,S,color='green',linewidth=2.5,linestyle="-")
    #设置x的范围
    xlim(-4.0,4.0)
    #设置横轴记号
    #-4,4指范围,5指在轴上显示几个数字
    xticks(np.linspace(-4,4,5,endpoint=True))
    #设置y轴范围
    ylim(-1.0,1.0)
    yticks(np.linspace(-1,1,5,endpoint=True))
    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
# line_up()
# 边距修改
def margin():
    Figure(figsize=(8,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=1.0,linestyle='-')
    #绘制正弦曲线
    plot(X,S,color='green',linewidth=1.0,linestyle="-")
    #设置x的范围
    xmin,xmax=X.min()*1.1,X.max()*1.1
    xlim(xmin,xmax)
    #设置横轴记号
    #-4,4指范围,5指在轴上显示几个数字
    xticks(np.linspace(-4,4,5,endpoint=True))
    #设置y轴范围
    ymin,ymax=C.min()*1.1,C.max()*1.1
    ylim(ymin,ymax)
    yticks(np.linspace(-1,1,5,endpoint=True))
    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
#margin()
#设置记号
def tick():
    Figure(figsize=(8,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=1.0,linestyle='-')
    #绘制正弦曲线
    plot(X,S,color='green',linewidth=1.0,linestyle="-")
    #设置x的范围
    xmin,xmax=X.min()*1.1,X.max()*1.1
    xlim(xmin,xmax)
    #设置横轴记号
    xticks([np.pi,-np.pi/2,np.pi/2,np.pi])
    #设置y轴范围
    ymin,ymax=C.min()*1.1,C.max()*1.1
    ylim(ymin,ymax)
    yticks([-1,0,+1])
    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
#tick()
#设置坐标轴的标签
def tick_pai():
    Figure(figsize=(10,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=1.0,linestyle='-')
    #绘制正弦曲线
    plot(X,S,color='green',linewidth=1.0,linestyle="-")
    #设置x的范围
    xmin,xmax=X.min()*1.1,X.max()*1.1
    ymin,ymax=C.min()*1.1,C.max()*1.1
    dx=(xmax-xmin)*0.2
    dy=(ymax-ymin)*0.2
    #设置xy轴范围
    xlim(xmin-dx,xmax+dx)
    ylim(ymin-dy,ymax+dy)
    #设置横轴记号
    xticks([np.pi,-np.pi/2,np.pi/2,np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    
    yticks([-1,0,+1],[r'$-1$', r'$0$', r'$+1$'])
    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
#tick_pai()
#设置坐标轴位置
def xy_change():
    Figure(figsize=(10,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    ax=gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=1.0,linestyle='-')
    #绘制正弦曲线
    plot(X,S,color='green',linewidth=1.0,linestyle="-")
    #设置x的范围
    xmin,xmax=X.min()*1.1,X.max()*1.1
    ymin,ymax=C.min()*1.1,C.max()*1.1
    dx=(xmax-xmin)*0.2
    dy=(ymax-ymin)*0.2
    #设置xy轴范围
    xlim(xmin-dx,xmax+dx)
    ylim(ymin-dy,ymax+dy)
    #设置横轴记号
    xticks([np.pi,-np.pi/2,np.pi/2,np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks([-1,0,+1],[r'$-1$', r'$0$', r'$+1$'])
    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
#xy_change()
#设置图例
def example():
    Figure(figsize=(10,6),dpi=80)
    #创建一个1*1的子图,接下来的图样绘制在其中的第一块
    subplot(1,1,1)
    #设置坐标轴部分
    ax=gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    X=np.linspace(-np.pi,np.pi,256,endpoint=True)
    C,S=np.cos(X),np.sin(X)
    #绘制余弦曲线,使用连续宽度为1的线条
    plot(X,C,color='blue',linewidth=1.0,linestyle="-",label='cosine')
    #绘制正弦曲线
    plot(X,S,color='red',linewidth=1.0,linestyle="-",label='sine')
    legend(loc='upper left')
    #设置x的范围
    xmin,xmax=X.min()*1.1,X.max()*1.1
    ymin,ymax=C.min()*1.1,C.max()*1.1
    dx=(xmax-xmin)*0.2
    dy=(ymax-ymin)*0.2
    #设置xy轴范围
    xlim(xmin-dx,xmax+dx)
    ylim(ymin-dy,ymax+dy)
    #设置横轴记号
    xticks([np.pi,-np.pi/2,np.pi/2,np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks([-1,0,+1],[r'$-1$', r'$0$', r'$+1$'])

    #保存图片,分辨率为72
    savefig("cossin.png",dpi=72)
    #直接展示
    show()
example()
