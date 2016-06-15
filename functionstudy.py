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
x=jiecheng(12)
print(hex(x))
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

