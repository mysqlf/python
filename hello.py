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
