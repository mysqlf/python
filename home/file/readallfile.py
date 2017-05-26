#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 列出指定目录下所有文件
# 非文件夹
import os
def Test2(rootDir,dirs=[]):
    for lists in os.listdir(rootDir):     
        path = os.path.join(rootDir, lists)
        if os.path.isfile(path):
            dirs.append(path)
        if os.path.isdir(path):
            Test2(path,dirs)
    return dirs
dirs=Test2("..\\")
print(dirs)
