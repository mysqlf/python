#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)  # 这个能保存以前的结果
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)
if __name__ == '__main__':
    with open(r'../otherfile/test.txt') as f:
        for line, prevlines in search(f, 'python', 3):
            for pline in prevlines:
                print(pline, end='')
                print('-'*20)
            print(line, end='2')
            print('-'*20)
        print('-'*20)
# 不设置大小则可以无限压入
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
x = q.pop()
print(x)
q.appendleft(4)
print(q)
# 压入时如果超过长度，相对于压入端的尾部元素会被移除
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
q.appendleft(5)
print(q)
x = q.pop()
print(x)
q.appendleft(6)
print(q)
