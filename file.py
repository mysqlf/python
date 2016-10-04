#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
f = open('D:/Git/python/test.txt', 'r')
# print(f)
# x=f.read()
# print(x)
# f.close()
# f=open('D:/Git/python/test.txt1','r')
# print(f)
# f=open('D:/Git/python/test.txt','r')
# print(f)
# try:
#     f=open('D:/Git/python/test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# with open('D:/Git/python/test.txt','r',encoding='gbk',errors='ignore') as f:
#     print(f.read())
# f=open('D:/Git/python/test.txt','r',encoding='gbk',errors='ignore')
# for line in f.readlines():
#     print(line.strip())
# f=open('D:/Git/python/test.txt','w',encoding='gbk',errors='ignore')
# f.write('asdzxc')
# with open('D:/Git/python/test.txt', 'w') as f:#尽量使用with语句操作文件
#     f.write('Hello, world!')
#
# 内存读写
# from io import StringIO
# d=StringIO('Hello!\nHi\nGoodbye!')
# print(d.tell())#将指针指向起始位置 ,没有参数
# print(d.readline())#读一行
# print(d.readline())
# print(d.readline())
# #将指针指向任意位置
# d.seek(3)
# print(d.readline())#读取一行,换行符结束读取
# print(d.readline())
# print(d.readline())
# print(d.readline())
# print(d.readline())
# print(d.readline())

# # f=StringIO()
# # f.write('hello')
# # print(f.getvalue())
# f=StringIO('Hello!\nHi\nGoodbye!')
# while True:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.strip())
#
# 内存二进制读写
#
# from io import BytesIO
# f=BytesIO()
# x=f.write('asd'.encode('utf-8'))
# f.seek(9)
# print(f.readline())
# print(x)
# print(os.name)
# nt#代表是win系统
# #print(os.uname())#win下没有这个函数
# #print(os.environ)#查看所有的环境变量
# x=os.environ.get('PATH')#查看某一个的
# print(x)
# D:\python\Scripts;D:\wamp\wamp\bin\php\php5.4.3;D:\python;C:\Windows\system32; C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\TortoiseSVN\bin;d:\sqlserver (x86) (x86)\100\Tools\Binn\VSShell\Common7\IDE\;d:\sqlserver (x86) (x86)\100\Tools\Binn\;C:\Program Files\MicrosoftSQL Server\100\Tools\Binn\;d:\sqlserver (x86) (x86)\100\DTS\Binn\;D:\Git\cmd
# x=os.environ.get('x','default')
# print(x)
# default
# print(os.environ.get('Python'))
# D:\python
# print(os.path.abspath('.'))#查看当前目录绝对路径
# #D:\Git\python
# print(os.path.join('D:\Git\python','newdemo'))
# D:\Git\python#先返回
# D:\Git\python\newdemo#再拼接
# print(os.mkdir(os.path.join(os.path.abspath('.'),'demo')))#创建目录
# print(os.rmdir(os.path.join(os.path.abspath('.'),'demo')))#删除目录
# 从内到外
# 获取当前绝对路径
# 组装新路径
# 创建目录/删除目录
# None--最外层这个函数的返回值是None
# print(os.path.split(os.path.join(os.path.abspath('.'),'file.py')))
# print(os.path.splitext(os.path.join(os.path.abspath('.'),'file.py')))
# l=[x for x in os.listdir('.') if os.path.isdir(x)]
# print(l)

# def dir1(path='.'):
#     allfile=[x for x in os.listdir(path) ]
#     dirs=[]
#     for k in allfile:
#         v=os.path.join(path,k)
#         dirs.append(v)
#     return dirs
# x=dir1(os.path.abspath('.'))
# dirs=[]
# for k in x:
#     dirs.append(k)
#     if os.path.isdir(k):
#         dirs.append(dir1(k))
# print(dirs)
# allfile.append(dir1(v))
# print()
# import pickle
# d=dict(name='A',age=18,score=88)
# print(pickle.dumps(d))#序列化
# f=open('test.txt','wb')
# pickle.dump(d,f)
# f.close()
# f=open('test.txt','rb')
# d=pickle.load(f)#反序列化
# f.close()
# print(d)
# import json
# # d=dict(name='A',age=18,score=88)
# # x=json.dumps(d)
# # print(x)
# # print(json.loads(x))


# class Student(object):

#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score

#     def student2Dict(self):
#         return {
#             'name': self.name,
#             'age': self.age,
#             'score': self.score
#         }

#     def dict2Student(self, objdict):
#         return Student(objdict['name'], objdict['age'], objdict['score'])
# s = Student('K', 12, 99)
# k = s.__dict__
# # 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
# # print(json.dumps(s.__dict__))
# # 将json字符串转为对象
# # 第一个参数是该对象实例转化的json字符串,第二个参数是通过字典实例化对象的函数
# print(json.loads(json.dumps(s.student2Dict()), object_hook=s.dict2Student))
# # <__main__.Student object at 0x0000000001131710>
