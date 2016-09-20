#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: fib.py
import itertools


def fib():
    first, second = 0, 1
    while 1:
        yield second
        first, second = second, first + second

print(list(itertools.islice(fib(), 10)))
