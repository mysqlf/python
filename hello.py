#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello,%s'%name)


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('error')

    def __setattr__(self, key, value):
        self[key] = value


def spam(a, b, c, d):
    print(a, b, c, d)
from functools import partial
s1 = partial(spam, 1)
s1(2, 3, 4)
s2 = partial(spam, 1, 2, d=4)
s2(3)

# 返回多个返回值,自动转为元组


def return_more_than(a, b, c, d):
    return a, b, c, d
print(return_more_than(1, 2, 3, 4))


# 把函数名当参数传入新的函数
# 在新的函数内运行函数
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


class ResultHandler:

    def __init__(self):
        self.sequece = 0

    def hander(self, result):
        self.sequece += 1
        print('[{}] Got :{}'.format(self.sequece, result))
r = ResultHandler()
apply_async(add, (2, 3), callback=r.hander)
