#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
from functionstudy import myabs
# a=100
# if a>=0:
# 	print(a)
# else:
# 	print(-a)
# print('I\'m ok')
# print('I\'m learning\n Python')
# print('\\\\n\\')
# print(True and False)
# print(True or False)
# print(not False)
# print(not 3>1)
# age=19
# if age>=18:
# 	print('adult')
# else:
#  	print("teenager")
# a=123
# print(a)
# a='ABC'
# print(a)
# int a=100
# #a="ABC" 如果声明为INT 则不能再改变其类型
# x=100
# x=x+2
# print(9/3)#除结果为浮点数
# print(9//3)#地板除结果为整数
# print(10/3)#除结果为浮点数
# print(10//3)#地板除结果为整数
# print(10%3)#%取余数
# print("文本包含teenager")
# python 字符编码转换
# print(ord('A'))
# print(ord('中'))
# print(chr(25991))
# print(chr(89))
# print('\u4e2d\u6587')
# 
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# python 字符长度计算
# print(len('ABC'))
# print(len('中文'))
# print(len(b'ABC'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('utf-8')))
# 格式化字符串
# print('Hello,%s' % 'world')
# print('Hi,%s,you have $%d' % ('Michael',100000))
# 实例计算成绩提升绩点
# s1=72
# s2=85
# r=(s2-s1)/s1
# print('%f' % r)
# 
# classmate=['Michael','Bob','Tracy']
# print(classmate)
# x=len(classmate)
# print(x)
# # print(classmate[0])
# # print(classmate[1])
# # print(classmate[2])
# classmate.append('ZL')#在末尾追加元素
# print(classmate)
# print(classmate[-1])
# classmate.insert(3,'ZC')#3是指下标(索引)为3而不是第三个元素
# print(classmate)
# classmate[3]='CZ'#重新赋值
# print(classmate)
# classmate.pop(3)//删除
# print(classmate)
# classmate[3]=['ZL','ZC']
# print(classmate)
# guding=('A','B','C')
# print(guding)
# s2=(3,)
# print(s2)
# s2=(1,2)
# #s2[1]=4 #报错 tuple 不可变是指它的值不可改变,但变量可以被重新赋值
# print(s2)
# s2=(1,23)
# print(s2)
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[1][1])
# 



# python 字典基本操作
# d={'A':1,'B':2,'C':3}#赋值
# print(d['A'])
# d['A']=4
# print(d['A'])
# print('A' in d)#判断key是否存在于字典中
# print(d.get('A'))
# print(d.get('D'))
# print(d.get('D',-1))#获取已经存在的值如果值不存在就给不存在的key直接赋值
# d.pop('A')#删除
# print(d)
# 

# #python set #用于做数学的交并运算
# s=set([1,2,3,4,5])
# e=set([2,3,4,5,6,7])
# t=set([5,6,8,8])
# print(s)
# s.add(7)
# print(s)
# se=s&e
# print(se)
# st=s|t
# print(st)
# 
 
#python 字符串变化行为
# s=['a','c','b']
# s.sort()
# print(s)
# a='abc'
# b=a.replace('a','B')
# print(a)
# print(b)
# 

#python字典与set的比较

# d={'s':1,'e':2,'t':3}
# i={'s':1,'e':[2,3]}#字典的值是可以改变的 
# i['e']=4
# t={'1':'s','[2,3]':'e'}#key永远都是字符串,字符串是不会变的

# print(d)
# print(i)
# print(t)

# s=set([1,2,3])
# #e=set([1,[2,3]])#无法放入,因为[2,3]是可变的,通过一些方法这个list对象会改变
# print(s)
# #print(e)
# 

# print(hex(120))
# print(bool(1))
# print(bool(2))
# print(bool(''))
# 

# x=myabs(6)
# print(x)


import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.hset()
# #清空数据库
# r.flushdb()
# r.set('foo','bar')
# x=r.get('foo')
# print(x)

# print(r['foo'])
# print(r.keys())


#管道操作
# p=r.pipeline()
# p.set('hello','redis').sadd('fax','bax').incr('num').execute()