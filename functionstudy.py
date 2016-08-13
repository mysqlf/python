#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

import types
def checkint(x):
	if type(x) == type(1):
		return True
	else:
		return False
	
# def jiecheng(x):
# 	ck=checktype(x,int)
# 	su=1
# 	if ck==True:
# 		if x<0:
# 			x=abs(x)
# 			for i in range(1,x+1):
# 				su=su*i
# 			y=x%2
# 			if y==0:
# 				return su
# 			else:
# 				return -su
# 		else:
# 			for i in range(1,x+1):
# 				su=su*i
# 			return su
# 	else:
# 		return "输入错误"
	


def myabs(x):
	if x>0:
		return x
	else:
		return -x
#int str list dict tuple
def checktype(value,typ):	
	if isinstance(value,typ):
	    return True
	else:
	    return False
# x=jiecheng(12)
# print(hex(x))


# d={'a':1,'b':2,'c':3}
# for k,v in d.items():
# 	print(k,v)
# for k,v in enumerate(['A','B','C'],2):#最后一个参数,设置下标初始值
# 	print(k,v)
# k=[x*x for x in range(1,11)]
# print(k)
# l=[m+n for m in 'ABC' for n in 'XYX']
# print(l)

#函数斐波那契数列
# def fb(max):
# 	n,a,b=0,0,1
# 	sl=[]
# 	while n<max:
# 		sl.append(b)
# 		yield b
# 		a,b=b,a+b
# 		n=n+1
# 	return sl
# #输出
# g=fb(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

#杨辉三角
# def triangles(max):
#     a = [1]
#     k=0
#     n=[]
#     while k<max:
#         yield a
#         n.append(a)
#         a = [sum(i) for i in zip([0] + a, a + [0])]
#         k=k+1
#     return n
# test=triangles(10)
# 
#输出生成器内容需要使用捕捉异常的方式
# while True:
#     try:
#         x = next(test)
#         print('test:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break


			



# x=checktype('abc',str)
# print(x)
	# if isinstance(b,list):
	#     print "b is list"
	# else:
	#     print "b is not list"
	# if isinstance(c,tuple):
	#     print "c is tuple"
	# else:
	#     print "c is not tuple"
	# if isinstance(d,dict):
	#     print "d is dict"
	# else:
	#     print "d is not dict"
	# if isinstance(e,str):
	#     print "d is str"
	# else:
	#     print "d is not str"		
#map 的使用 map将列表运算,返回还是列表 
#reduce 将列表按函数来迭代进行运算,运算的函数需要且只要两个参数
# def f(x):
#     return x*x
# r=map(f,[1,2,3,4,5,6,7,8,9])
# while True:
#     try:
#         x = next(r)
#         print('r:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
#         
# reduce 使用
# from functools import reduce
# def su(x,y):
#     return x+y
# s=reduce(su,[1,2,3,4,5,6,7])
# print(s)
# def fn(x,y):
#     return x*10+y
# s=reduce(fn,[1,2,3,4,5,6,7])
# print(s)

def up(str):
	return str.capitalize()
#x=up('AAAA')
#print(x)
tmp=list(map(up,['zAx','XXX','CzA']))
# print(tmp)

def cj(x,y):
	return x*y
from functools import reduce
# s=reduce(cj,[1,4,5,6,7,8,9])
# print(s)

#字符转浮点数
# def str2float(str):
# 	def add(x,y):
# 		return x+y
# 	n = str.index('.')
# 	l=str.split('.')
# 	if n==0:
# 		l[0]=0
# 		cd=len(l[1])
# 		tmp=list(map(int,l))
# 		tmp[1]=tmp[1]/(10**cd)
# 		return reduce(add,tmp)
# 	elif n==len(str)-1:
# 		return int(l[0])
# 	elif len(l)==2:
# 		cd=len(l[1])
# 		tmp=list(map(int,l))
# 		tmp[1]=tmp[1]/(10**cd)
# 		return reduce(add,tmp)
# x=str2float('1.1')
# x=x*1.1
# print(x)
# 


#filter 筛选函数(删掉返回未false的数值)(需要两个参数,一个为判断函数,一个为一个list)
# # 
# def is_two(n):
# 	return n%2==1
# #删掉返回false的
# x=list(filter(is_two,[1,2,3,4,5,6,7,8,9,11,12]))
# print(x)

#筛选素数
# def make_list():
# 	n=1
# 	while True:
# 		n=n+2
# 		yield n
# def filter_ss(n):
# 	return lambda x:x%n>0
# def primes():
# 	yield 2
# 	it=make_list()
# 	while True:
# 		n=next(it)
# 		yield n
# 		it=filter(filter_ss(n),it)
# for n in primes():
# 	if n<1000:
# 		print(n)
# 	else:
# 		break

#回数:把数字翻转再比对相等即可判断是否为回数
# def filter_hs(n):
# 	n1=list(str(n))
# 	n2=list(str(n))
# 	n1.reverse()
# 	if n2==n1:
# 		return True
# output = list(filter(filter_hs, range(1, 10000)))
# print(output)

#列表排序函数
#key数据经过该方法处理后再排序

#是先将整个数列全部经过该函数处理生成一个新的临时数列,再进行排序
#reverse倒序
# l=sorted([9,-3,-1,8,6,7],key=abs, reverse=True)
# print(l)

# def by_name(x):
# 	l=[]
# 	#将原有数列的数值一个个的传过去,而不是整个数列传过去,所以原有数列是二维的话,在内部处理就变成处理一维的
# 	l.append(x[0])
# 	return l

# def by_socre(x):
# 	l=[]
# 	l.append(x[1])
# 	return l
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# l=sorted(L,key=by_name)
# print(l)
# l=sorted(L,key=by_socre,reverse=True)
# print(l)

#将函数作为返回值
# def count():
# 	def f(j):
# 		def g():
# 			return j*j
# 		return g
# 	fs=[]
# 	for i in range(1,5):
# 		fs.append(f(i))
# 	return fs

# f1,f2,f3,f4=count()
# print(f1())
# print(f2())
# print(f3())
# print(f4())

#匿名函数
# k=lambda x:[s for s in range(1,x)]
# l=k(10)
# print(l)
# 
# 
# def now():
# 	print('2016-08-04')
# f=now
# f()
# print(f.__name__)


#装饰器
# def log(func):
# 	def wraper(*args,**kw):
# 		print('call %s():'% func.__name__)
# 		return func(*args,**kw)
# 	return wraper
# @log
# def now():
# 	print('20160804')
# now()
# now=log(now)
# now()

# def log(text):
# 	def decorator(func):
# 		def wrapper(*a,**k):
# 			print('%s %s():'%(text,func.__name__))
# 			return func(*a,**k)
# 		return wrapper
# 	return decorator
# @log('execute')
# def nows():
# 	print('123456789')
# nows()
# print(nows.__name__)

# import functools
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*a,**k):
# 		print('call %s():' %func.__name__)
# 		return func(*a,**k)
# 	return wrapper
# @log
# def now():
# 	print('123')
# now()
# print(now.__name__)
# 
#偏函数相当于给函数某一个参数绑定默认值
#只需要一行即可完成
# import functools
# int2=functools.partial(int,base=2)
# print(int2('100100'))
# def int3(x,base=2):
# 	return int(x,base)
# print(int3('1111'))
# 测试自己的想法
# def test(x,y,z):
# 	return x*y*z
# test1=functools.partial(test,y=3,z=4)
# print(test1(2))
# 
# 
# 导入模块学习
# 1,导入直接的函数,函数可直接调用
# from test import my_func
# my_func()
# from test import my_test
# x=my_test(10)
# print(x)

#2导入整个文件
#函数要在该文件后面使用点形式调用
# import test
# test.my_func()
# x=test.my_test(10)
# print(x)
# import test
# test.my_func()
# import sys
# print(sys.path)
# sys.path.append('D:\Git\python')
# print(sys.path)
# class Student(object):
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score
# 	def print_score(self):
# 		print('%s:%s' %(self.name,self.score))
# A=Student('As',100)
# B=Student('B',99)
# A.print_score()
# B.print_score()
# print(A.name)
# A.name='ASD';
# print(A.name)#可以改变属性的值
# print(A)#输出A在内存中的位置

#变量加上__代表变量私有,只能在本类中访问,对象不能访问,在类外不能通过直接赋值修改属性值
#修改属性可以通过在类中定义相关方法来进行修改
# class Student1(object):
# 	def __init__(self,name,score):
# 		self.__name=name
# 		self.__score=score
# 	def print_score(self):
# 		print('%s:%s' %(self.__name,self.__score))
# 	def getname(self):
# 		return self.__name
# 	def getscore(self):
# 		return self.__score
# 	def setname(self,name):
# 		self.__name=name
# A1=Student1('A','90')
# A1.__name="ZXCB"#无效
# print(A1.getname())
# A1._Student1__name="ZXC"#有效,但不建议这样修改
# print(A1.getname())
#print(A1.__name)#这句会报错

# A1.setname('QWE')
# print(A1.getname())
# A1.print_score()
# 
 
class Animal(object):
	def run(self):
		print('Animal running')

	def eat(self):
		print('Animal Eating')




# 情形1
class Dog(Animal):
	pass
	#print('Dog running')
class Cat(Animal):
	pass
	#print('Cat running')
D=Dog()
# D.run()
# D.eat()
C=Cat()
# C.run()
# C.eat()
# def run_t(tmp):
# 	tmp.run()
# run_t(Animal())
# run_t(Dog())
# run_t(Cat())
# D:\Git\python>functionstudy.py  #运行结果
# Dog running
# Cat running
# Animal running
# Animal running
# Animal running	
# 
# 情形2
# class Dog(Animal):
# 	def run(self):
# 		print('Dog running')
# class Cat(Animal):
# 	def run(self):
# 		print('Cat running')
# 		
def run_t(tmp):
	tmp.run()
# run_t(Animal())
# run_t(Dog())
# run_t(Cat())
# 
# D:\Git\python>functionstudy.py
# Animal running
# Dog running
# Cat running


# print(isinstance(D,Dog)) #判断对象类型
# print(isinstance(C,Cat))
# print(isinstance(C,Animal))
# 
# type函数 获取对象信息
# print(type(123))
# <class 'int'>
# print(type(D))
# <class '__main__.Dog'>
# print(type(abs))
# <class 'builtin_function_or_method'>
# print(type(run_t)==types.FunctionType)
# #True
# print(type(run_t))
# #<class 'function'>
# print(type(lambda x:x)==types.LambdaType)
# dir可以获取所有的方法
# print(dir(D))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__','__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eat', 'run']
# print('ABC'.__len__())
#
#
# class Student(object):
# 	name="Student"
# 	def __init__(self,name):
# 		self.name=name
# s=Student('bob')

# print(s.name)
# #bob
# print(Student.name)
# #Student

# class Word(object):
# 	def __init__(self,text):
# 		self.text=text
# 	def equal(self,word1):
# 		return self.text.lower()==word1.text.lower()
# 	def equal1(self,word2):
# 		return self.text.lower()==word2.lower()
# w=Word('qwert')
# x=w.equal(Word('Qwert'))
# print(x)
# True
# x=w.equal1('QWERT')
# print(x)
# True
#  
#  #类的方法绑定,可以在使用时实时添加类所缺少的方法,这个类的所有的对象都能使用
# class Student(object):
# 	pass
# s=Student()
# #给对象绑定属性,这个属性
# s.name="zl"
# #print(s.name)


# def set_age(self,age):
# 	self.age=age
# from types import MethodType
# #给对象绑定方法,这个方法只能这个对象使用,不是这个类的方法
# s.set_age=MethodType(set_age,s)
# s.set_age(23)
# #print(s.age)
# #给类绑定属性,类与对象都可以使用,包括后面绑定的方法
# def set_score(self,score):
# 	self.score=score
# Student.set_score=set_score
# s.set_score(1000)
# #print(s.score)

# def get_score(self):
# 	print(self.score)
# Student.get_score=get_score
# s.get_score()

# class Student(object):
# 	__slots__=('name','age')

# # s.name="zl"
# # print(s.name)
# # s.age=23
# # print(s.age)
# # s.score=100
# # print(s.score)
# class Student(object):	
# 	def get_score(self):
# 		print(self._score)

# 	def set_score(self,score):
# 		if not isinstance(score,int):
# 			raise ValueError('not int')
# 		if score<0 or score>100:
# 			raise ValueError('not 1~100')
# 		self._score=score
# s=Student()
# # s.set_score('qwe')
# # #ValueError: not int
# # s.set_score(1000)
# # #ValueError: not 1~100
# s.set_score(99)
# s.get_score()
# #99
# 
# #将类方法当做属性来调用
# class Student(object):
# 	@property	
# 	def score(self):
# 		print(self._score)
# 	@score.setter
# 	def score(self,score):
# 		if not isinstance(score,int):
# 			raise ValueError('not int')
# 		if score<0 or score>100:
# 			raise ValueError('not 1~100')
# 		self._score=score
# 	@property
# 	def values(self):
# 		print('%s:%s'%(self.name,self.age))
# 	@values.setter
# 	def values(self,va):
# 		self.name=va[0]
# 		self.age=va[1]
# s=Student()
# # s.score=99#等于调用了 set_score(self,score):
# # s.score#等于get_score(self):

# s.values=['zl',23]
# s.values
# #切片
# k=[1,2,3,4]
# print(k[0:1])
# print(k[0:2])#从下标0取到下标2,取的其实是下标为0,1的值
# print(k[1:2])#从下标1取到下标2,取的其实是下标为1的值
# print(k[2:3])#从下标2取到下标3,取的其实是下标为2的值
# print(k[2])