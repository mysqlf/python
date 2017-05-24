#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
#读写压缩文件
import gzip
data='dsflihbsKJdvcnbSKJFOW;EFOFQWQPWDJSDI'
with gzip.open('filename.gz','wt') as f:
    f.write(data)
f=open('filename.gz','rt')
with gzip.open('filename.gz','rt') as f:
    text=f.read()
    print(text)

    
import bz2
with bz2.open('filename.bz2','wt') as f:
    f.write(data)
f=open('filename.bz2','rt')
with bz2.open('filename.bz2','rt') as f:
    text=f.read()
    print(text)
# gzip.open() 和 bz2.open() 还有一个特性， 
# 它们可以作用在一个已存在并以二进制模式打开的文件上。
# 也就是文件锁对其没有影响
# 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，
# 比如套接字，管道和内存中文件等。
