#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 打印输出到到文件内
# with open('./test.txt','wt') as f:
# 	print('15112630931',file=f)
#
#sep 输出分隔符
print('ZL',24,12,sep=':')
#end 结尾字符
print('ZL',24,12,sep=',',end='!!!')
#end 禁止换行
for x in range(4):
	print(x,end='')

with open('./x810.txt',"w") as f:
	f.write('test')