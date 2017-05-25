#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 读取二进制数据到缓冲区
# 直接读取二进制数据到一个可变缓冲区中，
# 而不需要做任何的中间复制操作。 
# 或者你想原地修改数据并将它写回到一个文件中去。
import os.path

def read_into_buffer(filename):
    #开辟缓冲区大小为文件大小
    buf=bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf

with open('file.bin','wb') as f:
    f.write(b'which is always equal to the length of the string')
buf=read_into_buffer('file.bin')
print(buf)
with open('files.bin','wb') as f:
    f.write(buf)


#可以零复制的方式对缓冲区执行切片操作,修改缓冲区内容
m1=memoryview(buf)
m2=m1[-5:]
print(m2)
m2[:]=b'WORLD'
print(buf)
