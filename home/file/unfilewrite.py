#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 文件不存在才能写入
# 不能覆盖文件
# wt则是覆盖式写入
with open('temp.txt','wt') as f:
    f.write('which is always equal to the length of the string')
#使用xt则是检验文件是否存在,存在则不能写入
#不覆盖文件的形式
with open('temp.txt','xt') as f:
    f.write('which is always equal to the length of the string')
