#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import time
from functools import reduce
def test_factorial_reduce():
    time_begin=time.clock()
    print(reduce(lambda x,y:x*y,range(1,int(input('input a number (> 1)'))+1)))
    print("use time:%s"%(time.clock()-time_begin))
    return 
def test_factorial_math():
    import math
    time_begin=time.clock()
    print(math.factorial(int(input('input a number (> 1)'))))
    print("use time:%s"%(time.clock()-time_begin))
    return 
if __name__ == '__main__':
    print("*"*50+"use reduce"+"*"*50)
    test_factorial_reduce()
    print("*"*50+"use math"+"*"*50)
    test_factorial_math()   
