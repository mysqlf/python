#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串令牌解析
import re
text = 'foo = 23 + 42 * 10'
# tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
#           ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


tokens = (tok for tok in generate_tokens(master_pat, text))

for tok in tokens:
    print(tok)


# 这段是自己手动一步步解析token 如果超过长度继续解析会报错
# 需要自己控制长度
# scanner = master_pat.scanner('foo=42+23')
# tmp = scanner.match()
# print(tmp)
# print(tmp.lastgroup, tmp.group())
# tmp = scanner.match()
# print(tmp)
# print(tmp.lastgroup, tmp.group())
# tmp = scanner.match()
# print(tmp)
# print(tmp.lastgroup, tmp.group())
# tmp = scanner.match()
# print(tmp)
# print(tmp.lastgroup, tmp.group())
# tmp = scanner.match()
# print(tmp)
# print(tmp.lastgroup, tmp.group())
