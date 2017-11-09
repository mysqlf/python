#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 设置输出编码
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
import pandas as pd
# 读取excel 返回list
def read_xlsx(file):
    df = pd.read_excel(file)
    return df.as_matrix()
#组合list为想要的格式
def filter_arr(arr):
    provice={}
    for item in arr:
        city={}
        val=[]
        #最开始写入的店铺应该是一个二维的,因为后续加入的是append加入一维数组.
        val.append([item[0],item[2],item[3]])
        #如果省份里面已经有这个省
        if provice.__contains__(item[1]):
            #取出省份下的城市
            citys=provice[item[1]]
            #判断城市里面是否有这个市
            if citys.__contains__(item[4]):
                #如果已经有这个市,则在后面追加这个店铺,这个只能是一维数组
                citys[item[4]].append(val[0])
            else:
                #否则添加这个市以及这个店铺
                citys[item[4]]=val
            #将省份的值更新
            provice[item[1]]=citys
        else:
            #没有和这个省
            #添加市区和这个店铺
            city[item[4]]=val
            #添加这个省份下的这个城市
            provice[item[1]]=city
    return provice
# 组装xmlstr
def build_xml(resdict):
    xml="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml+="<list>\n"
    for items in resdict:
        xml+='<Province name="'+items+"\">\n"
        for item in resdict[items]:
            xml+="<City name=\""+item+"\">\n"
            provice=resdict[items]
            city=provice[item]
            for shop in city:
                xml+="<Shop>\n"
                xml+="<WS_CODE>"+shop[0]+"</WS_CODE>\n"
                xml+="<WS_NAME>"+shop[1]+"</WS_NAME>\n"
                xml+="<WS_SHORTNAME>"+shop[2]+"</WS_SHORTNAME>\n"
                xml+="</Shop>\n"
            xml+="</City>\n"
        xml+="</Province>\n"
    xml+='</list>'
    return xml
def write_xml(xmlstrs,filename):
    with open(filename,'w') as f:
        f.write(xmlstrs)
res=read_xlsx('excel.xlsx')
resdict=filter_arr(res)
xmlstrs=build_xml(resdict)
write_xml(xmlstrs,'excel.xml')
print(xmlstrs)


