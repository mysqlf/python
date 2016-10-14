#!/usr/bin/env python
# -*- coding: utf-8 -*-

# l = [1, 2]
# if type(l) == type([]):
#     print('L is list')
# # dir(l)  # 函数列表
# # print(dir(l))#打印出函数列表
# # help(l)  # 根据对象的类型，列出该类的方法
# # print(type(l))  # <class 'list'>

# # if type(l) == list:
# #     print('L is list')
# x = 9
# # 201
# y = 2
# print(x >> y)  # 位运算
# print(y << x)  # 位运算

from socket import *


def portScanner(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, post))
        print('[+]%d open ' % port)
        s.close()
    except:
        print('[-]%d close' % port)


def main():
    setdefaulttimeout(1)
    for p in range(1, 1024):
        portScanner('127.0.0.1', p)
if __name__ == '__main__':
    main()
