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
def add(x,y):
	return x+y
def str2float(str):
	n = str.index('.')
	l=str.split('.')
	return l
	if n==0:
		
	elif n==len(str)-1:
		return int(l[0])
	elif len(l)==2:
		cd=len(l[1])
		tmp=list(map(int,l))
		tmp[1]=tmp[1]/(10**cd)
		return reduce(add,tmp)
	
x=str2float('1.')
print(x)