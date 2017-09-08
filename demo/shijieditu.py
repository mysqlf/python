#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 中国地图
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # IDE运行编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')#cmd运行编码
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap

from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex

plt.figure(figsize=(16,8))
m = Basemap(
    llcrnrlon=77, 
    llcrnrlat=14, 
    urcrnrlon=140, 
    urcrnrlat=51, 
    projection='lcc', 
    lat_1=33, 
    lat_2=45, 
    lon_0=100
    )
m.drawcoastlines(linewidth=1.5)
m.readshapefile('adm/CHN_adm1', 'states', drawbounds=True)

df=pd.read_csv('men.csv')
df['省名']=df.地区.str[:2]

df.set_index('省名',inplace=True)

statenames=[]
colors={}
cmap=plt.cm.YlOrRd
vmax=50000000
vmin=500000
for shapedict in m.states_info:
    statename=shapedict['NL_NAME_1']
    p=statename.split('|')
    if len(p)>1:
        s=p[1]
    else:
        s=p[0]
    s=s[:2]
    if s=='黑龍':
        s='黑龙'
    statenames.append(s)
    pop=df['人口数'][s]
    colors[s]=cmap(np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
ax=plt.gca()   

for nshape,seg in enumerate(m.states):
    color=rgb2hex(colors[statenames[nshape]])
    poly=Polygon(seg,facecolor=color,edgecolor=color)
    ax.add_patch(poly)

m.readshapefile('adm/TWN_adm1', 'states', drawbounds=True)
for nshape,seg in enumerate(m.states):
    poly=Polygon(seg,facecolor='r')
    ax.add_patch(poly)
fig1 = plt.gcf()
#plt.show()
plt.draw()
fig1.savefig('tessstttyyy.png', dpi=100)
plt.show()
