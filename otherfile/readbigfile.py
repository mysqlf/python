#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 文件读取和输出的解码格式指定方法
# 用于指定读取文件的解码方式
import codecs

#   用于指定输出的解码方式
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def read_in_chunks(filePath,chunk_size=1024*1024):
    file_object=open(filePath,'r',encoding="utf8")
    while True:
        chunk_data=file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data
if __name__ == '__main__':
    filePath="php_error.log"
    for chunk in read_in_chunks(filePath):
        print(chunk)
