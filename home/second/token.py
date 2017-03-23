#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串令牌解析
import re
text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


scanner = master_pat.scanner('foo=42+23')
tmp = scanner.match()
print(tmp)
print(tmp.lastgroup, tmp.group())
tmp = scanner.match()
print(tmp)
print(tmp.lastgroup, tmp.group())
tmp = scanner.match()
print(tmp)
print(tmp.lastgroup, tmp.group())
tmp = scanner.match()
print(tmp)
print(tmp.lastgroup, tmp.group())
tmp = scanner.match()
print(tmp)
print(tmp.lastgroup, tmp.group())
# tmp = scanner.match()
# print(tmp)
# print(scanner.match().lastgroup, scanner.match().group())

from collections import namedtuple


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo=42'):
    print(tok)

tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
for tok in tokens:
    print(tok)
