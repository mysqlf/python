#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import hashlib
# md5 = hashlib.md5()
# # # python加密方法
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))  # 单独加密
# x = md5.hexdigest()  # 获取加密结果
# print(x)
# # d26a53750bc40b38b65a520292f69306
# # # 如果数据量很大，可以分块多次调用update()
# # 如果要重新使用MD5而不是组合之前的数据加密的话,需要重新实例化一个MD5的对象
# md5 = hashlib.md5()
# md5.update('how to use md5 in python'.encode('utf-8'))
# md5.update(' hashlib?'.encode('utf-8'))
# x = md5.hexdigest()
# print(x)
# # 重新实例化一个MD5对象
# # d26a53750bc40b38b65a520292f69306
# #
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# x = md5.hexdigest()
# print(x)
# # 不重新实例化则会拼接上一个字符再MD5加密
# #
# # 8d7f266bcebe4d9b68611c1eb4b02ef8
# # sha1于MD5加密方法使用一样,只不过生成的加密字符更长,安全性略高,但是速度略慢
# sha1 = hashlib.sha1()
# sha1.update('how to use md5 in python'.encode('utf-8'))
# sha1.update(' hashlib?'.encode('utf-8'))
# x = sha1.hexdigest()
# print(x)
# # 加密账号密码一般可以将用户的账号与密码组合起来,再进行MD5加密
# #
# # 或者将密码加密再拼接账号再进行一次MD5加密
