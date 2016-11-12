#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 解压可迭代对象赋值给多个变量

# 扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
record = ('Zl', '11545@qq.com', '773-555-1212',
          '773-555-1212', '773-555-1212' '773-555-1212', '874-555-1212', 'abc')
#*变量能够读取多个值
name, email, *phone_numbers, test = record
print(name)
print(email)
print(phone_numbers)
print(test)
sales_record = ('123', '123', 'abc')
*trailing_qtrs, current_qtr = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing_qtrs)
print(current_qtr)

# 根据第一个参数决定使用对应的方法
record = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print(x, y)


def do_bar(s):
    print('bar', s)
for tag, *args in record:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/flase'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(*tail)

# 递归求和


def sum(items):
    head, *tail = items
    return head+sum(tail) if tail else head
x = sum(items)
print(x)
