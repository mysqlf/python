#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 函数参数
#   **kwargs
# **kwargs 允许你将不定长度的键值对, 
# 作为参数传递给一个函数。 
# 如果你想要在一个函数里处理带名字的参数,
# 你应该使用**kwargs。

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0}=={1}".format(key,value))
greet_me(name='zl')
# *args
# 你将不定个数的参数传递给函数时,
# 使用*args能全部接收,
# 不会出现因此报错或者丢失参数
def test_var_args(f_arg,*argv):
    print('first normal arg:',f_arg)
    print(argv[0],argv[1],argv[2])
    for arg in argv:
        print("another arg through *argv",arg)

test_var_args('zl','zc','zp','zn')

#两种参数方法的使用
def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)
args=('two',3,5)
test_args_kwargs(*args)

kwargs={"arg3":3,"arg2":"two","arg1":5}
test_args_kwargs(**kwargs)


#迭代器

def generator_function():
    for i in range(10):
        yield i
for item in generator_function():
    print(item)

def generator_function2():
    for i in [1,2,3,4]:
        yield i
for item in generator_function2():
    print(item)
# 这个异常说那个str对象不是一个迭代器。
# 对，就是这样！它是一个可迭代对象，
# 而不是一个迭代器。这意味着它支持迭代，
# 但我们不能直接对其进行迭代操作。
# 那我们怎样才能对它实施迭代呢？
# 是时候学习下另一个内置函数，iter。
# 它将根据一个可迭代对象返回一个迭代器对象。
# 这里是我们如何使用它：
mystring="asdaszxc"
myiter=iter(mystring)
print(next(myiter))


#map--参数
item=[1,2,3,4,5,6]
squared=list(map(lambda x:x**2,item))
print(squared)
#map--函数参数
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
#普通版
func=[multiply,add]
for i in range(5):
    value=map(lambda x:x(i),func)
    print(list(value))
#迭代器版
def test():
    func=[multiply,add]
    for i in range(5):
        value=map(lambda x:x(i),func)
        yield value
for x in test():
    print(list(x))

#
number_list=range(-5,5)
less_than_zero=filter(lambda x:x<0,number_list)
print(list(less_than_zero))

from functools import reduce
product=reduce((lambda x ,y: x*y),[1,2,3,4])
print(product)

#set 

some_list=['a','b','c','b','d','a']
duplicates=set([x for x in some_list if some_list.count(x)>1])
print(duplicates)

#装饰器
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

print(a_function_requiring_decoration())

#装饰器写日志
def logit(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string=func.__name__+"was called"
            print(log_string)
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
            return func(*args,**kwargs)
        return wrapped_function
    return logging_decorator
@logit()
def addition_func(x):
    return x+x

@logit(logfile='func2.log')
def func2():
    pass
result=addition_func(2)
func2()
#在Python中当函数被定义时，
#默认参数只会运算一次，
#而不是每次被调用时都会重新运算。
#永远不要定义可变类型的默认参数，
def add_to(num,target=[]):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))
# output
# [1]
# [1, 2]
# [1, 2, 3]
#__slots__  减少内存占用
#方法是通过减少实例对象属性内存的分配
class testclass(object):
    def __init__(self,name,identi):
        self.name=name
        self.identi=identi
class testclass2(object):
    __slots__=['name','identi']
    def __init__(self,name,identi):
        self.name=name
        self.identi=identi
x=10
a=lambda y,x=x:x+y
x=20
b=lambda y,x=x:x+y
print(a(10))
print(b(10))
