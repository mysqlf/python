#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 读取字节数据
with open("byte.bin",'rb') as f:
    data=f.read()
print(data)

with open('byte.bin','wb') as f:
    f.write(b"which is always equal to the length of the string")


t='hello world'
print(t[0])
for c in t:
    print(c)
t=b'hello world'
print(t[0])
for c in t:
    print(c)

with open('byte.bin','rb') as f:
    data=f.read(16)
    text=data.decode('utf-8')
print(text)

with open('byte.bin','wb') as f:
    text='which is always equal to the length of the string'
    f.write(text.encode('utf-8'))



a=b'acada'
print(a[0])


import array
nums=array.array('i',[1111,1112,1113,1114])
with open('byte.bin','wb') as f:
    f.write(nums)
a=array.array('i',[0,0,0,0,0,0,0,0])
with open('byte.bin','rb') as f:
    #直接读取二进制数据到其底层的内存中去
    f.readinto(a)
print(a)
