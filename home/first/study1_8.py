#!/usr/bin/env python
# -*- coding: utf-8 -*-
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# zip()函数可以将键值翻转,但是是只能访问一次的迭代器
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)


# 这样有错误
k = zip(prices.values(), prices.keys())
print(min(k))
# print(max(k)) 这句会报错


# 这样才不会报错
k = zip(prices.values(), prices.keys())
print(min(k))
k = zip(prices.values(), prices.keys())
print(max(k))


x = max(prices, key=lambda k: prices[k])
print(x)
x = min(prices, key=lambda k: prices[k])
print(x)


# 当多个实体拥有相同的值的时候，键会决定返回结果
# 会根据ASCII编码来决定
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(max(zip(prices.values(), prices.keys())))
print(min(zip(prices.values(), prices.keys())))
