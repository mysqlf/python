#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 大文件切割
import sys,os
kilobytes=1024
megabytes=kilobytes*1000
chunksize=int(200*megabytes)
def split(fromfile,todir,chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    partnum=0
    inputfile=open(fromfile,'rb')
    while True:
        chunk=inputfile.read(chunksize)
        if not chunk:
            break
        partnum+=1
        filename=os.path.join(todir,('part%04d'%partnum))
        fileobj=open(filename,'wb')
        fileobj.write(chunk)
        fileobj.close()
    return partnum
if __name__ == '__main__':
    fromfile='php_error.log'
    todir='E:/phpstudy-master/filefunction/test'
    chunksizes = chunksize
    absfrom,absto = map(os.path.abspath,[fromfile,todir])
    print('Splitting',absfrom,'to',absto,'by',chunksizes)
    try:
        parts = split(fromfile,todir,chunksize)
    except:
        print('Error during split:')
        print(sys.exc_info()[0],sys.exc_info()[1])
    else:
        print('split finished:',parts,'parts are in',absto)
