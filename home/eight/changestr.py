#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
class Pair:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
         return 'Pair(%r, %r)' % (self.x, self.y)
    def __str__(self):
        return '(x:{0.x!s},y:{0.y!s})'.format(self)
p=Pair(3, 4)
print(p)
print('p is {0!r}'.format(p))
