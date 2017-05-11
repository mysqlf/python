#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 字节到大整数的打包

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
tmp = len(data)
print(tmp)

tmp = int.from_bytes(data, 'little')
print(tmp)
tmp = int.from_bytes(data, 'big')
print(tmp)

x = 94522842520747284487117727783387188
tmp_b = x.to_bytes(16, 'big')
print(tmp_b)
tmp_b = x.to_bytes(16, 'little')
print(tmp_b)

import struct
hi, lo = struct.unpack('>QQ', data)
print(hi)
print((hi << 64))
print(lo)
print((hi << 64) + lo)

x = 0x01020304
tmp = x.to_bytes(4, 'big')
print(tmp)
tmp = x.to_bytes(4, 'little')
print(tmp)

x = 523**23
print(x)

# x.to_bytes(16, 'little')  会报错,长度不够
# int.bit_length() 方法来决定需要多少字节位来存储这个值
tmp = x.bit_length()
print(tmp)

nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
tmp = x.to_bytes(nbytes, 'little')
print(tmp)
