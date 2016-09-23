#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# def my_func():
#     print('1234567')
# def my_test(x):
#     return x**2
# if __name__=='__main__':
#     my_func()

# 异常处理
# try:
#     print('try...')
#     r=10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('end')

# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar(0)
#     except Exception as e:
#         print('Error:',e)
#     finally:
#         print('1234567')
# main()
# def test(s):
#     try:
#         r=10/int(s)
#     except ValueError as e:
#         print('ValueError',e)
#     except ZeroDivisionError as e:
#         print('ZeroDivisionError:',e)
#     else:
#         print('no error')
#         return r
#     finally:
#         print('finally')
# r=test(1)
# print(r)
# test(0)
# test('q')
# 调试方式
import logging  # logging方式 主要方法还是使用log
logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d'%n)
# print(10/n)
#
# def foo(s):#assert 方式
#     n=int(s)
#     assert n!=0, 'n is zero'
#     return 10/n
# def main():
#     foo(0)
# main()
#
# s='0'
# n=int(s)
# print(10/n)
# import pdb
# s='0'
# n=int(s)
# pdb.set_trace()
# print(10/n)

# 单元测试
#
# 被测试的类
# class Dict(dict):
#     def __init__(self,**kw):
#         super().__init__(**kw)
#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError('error')
#     def __setattr__(self,key,value):
#         self[key]=value

import unittest


class TestDict(unittest.TestCase):

    def setUp(self):  # 可以在单元测试中编写两个特殊的setUp()和 tearDown() 方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
        print('setUp')

    def tearDown(self):
        print('tetsDown...')

    def test_unit(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言输出是否是我们所期望的,覆盖所有的情况
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# #d=Dict(a=1,b=2)
# # print(d['a'])
# if __name__=='__main__':#运行单元测试的方法
#     unittest.main()
#
# 文档测试
import re
# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
# m=re.search('(?<=abc)def','abcdef')
# print(m.group(0))


class Dict(dict):

    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest  # 只有在引入了dotest才会运行文档中的测试代码,其他时间不会执行
    doctest.testmod()
