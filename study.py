#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# import types
# def my_love(self,girl):
#     print('%s love %s'%(self.name,girl))
# class Me(object):
#     def __init__(self,name):
#         self.name=name
# Me.my_love=my_love
# zl=Me('zl')
# zl.my_love('who')
# 
# class Me(object):
#     @property
#     def love(self):
#         print(self._love)
#     @love.setter
#     def love(self,name):
#         self._love=name
# m=Me()
# m.love='zc'
# m.love
    
class Student(object):
    def __init__(self,name):
        self._name=name
    def __str__(self):
        return 'Student object (name :%s)'%self._name
    __repr__=__str__
# print(Student('ZL'))
# s=Student('ZL')
# print(s)

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration();
        return self.a
# for n in Fib():
#     print(n)
#     
#     定制一个产生斐波那契数列的类
# class Fibs(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# # f=Fibs()
# # print(f[100])
# 定制一个产生斐波那契数列的类支持切片
# class Fib3(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# f=Fib3()
# print(f[98:100])
# 
# __getattr__
class Student(object):
    def __init__(self,path=''):#初始化类的属性
        self._path=path
    def __getattr__(self,path):#调用不存在的类方法时返回
        return Student('%s/%s' % (self._path, path))
    def __str__(self):#这用来返回字符串
        return self._path
    __repr__=__str__
    def __call__(self,path):#调用自己的方法或属性
        return Student('%s/%s' % (self._path, path))

print(Student().user('zl').up)
#流程Student()实例化一个类
#Student().user('')