#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

import types
def checkint(x):
	if type(x) == type(1):
		return True
	else:
		return False
	
def jiecheng(x):
	ck=checktype(x,int)
	su=1
	if ck==True:
		if x<0:
			x=abs(x)
			for i in range(1,x+1):
				su=su*i
			y=x%2
			if y==0:
				return su
			else:
				return -su
		else:
			for i in range(1,x+1):
				su=su*i
			return su
	else:
		return "输入错误"
	


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