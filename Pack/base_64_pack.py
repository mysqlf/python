#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
x = base64.b64encode(b'binary\x00string')
# print(x)
# print(base64.b64decode(x))


def safe_baser64(s):
    if not isinstance(s, bytes):
        s = s.encode('utf-8')
    while len(s) % 4 != 0:
        s = s + b'='
    if len(s) % 4 == 0:
        print(base64.b64decode(s))
        return base64.b64decode(s)
    else:
        print('sorry')
x = safe_baser64(b'YWJjZA==')
x = safe_baser64(b'YWJjZA')
assert b'abcd' == safe_baser64(b'YWJjZA=='), safe_baser64('YWJjZA==')
assert b'abcd' == safe_baser64(b'YWJjZA'), safe_baser64('YWJjZA')
print('Pass')
