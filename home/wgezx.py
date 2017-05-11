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

# from socket import *


# def portScanner(host, port):
#     try:
#         s = socket(AF_INET, SOCK_STREAM)
#         s.connect((host, post))
#         print('[+]%d open ' % port)
#         s.close()
#     except:
#         pass
#         #print('[-]%d close' % port)


# def main():
#     setdefaulttimeout(1)
#     for p in range(1, 1024):
#         portScanner('192.168.10.101', p)
# if __name__ == '__main__':
#     main()
#
# 解压序列赋值给多个变量
p = (4, 5)
x, y = p
print(x)
print(y)
data = ['AM', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)
name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)

s = 'hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)
data = ['AM', 50, 91.1, (2012, 12, 21)]

_, shares, price, _ = data
print(_)
print(shares)
print(price)
