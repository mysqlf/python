#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x = s.connect(('192.168.2.19', 6195))
print(x)
# print(s.recv(1024).decode('utf-8'))
# for data in [b'ZL', b'ZN', b'ZV']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()
