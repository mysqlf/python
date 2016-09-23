#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b3])
print(bs)
# b'\x00\x9c@@'
import struct
x = struct.pack('>I', 10240099)
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(x)
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
