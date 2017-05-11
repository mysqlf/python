#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 优先级排序
# 使用的是堆排序
import heapq


class Prior:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        print(self._queue)
        self._index += 1

    def pop(self):
        print(self._queue)
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
q = Prior()
q.push(Item('foo'), 1)
q.push(Item('bar'), 1)
q.push(Item('foo'), 1)
q.push(Item('fo'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 2)
x = q.pop()
x = q.pop()
x = q.pop()
x = q.pop()
x = q.pop()
