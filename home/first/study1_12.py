#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 取前3
top_three = word_counts.most_common(3)
print(top_three)
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# 直接update
word_counts.update(morewords)
print(word_counts)

# 手动增
for word in morewords:
    word_counts[word] += 1

top_three = word_counts.most_common(3)
print(top_three)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
c = a+b
print(c)
d = a-b
print(d)
# Counter 对象
# 在几乎所有需要制表或者计数数据的场合是非常有用的工具。
#  在解决这类问题的时候你应该优先选择它，
# 而不是手动的利用字典去实现。
