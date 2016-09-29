#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# udp 服务端
# 好像只要数据不超过就不会关闭连接
# UDP的使用与TCP类似，但是不需要建立连接。
# 此外，服务器绑定UDP端口和TCP端口互不冲突，
# 也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9998))
print('bind UDP on 9998...')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello %s' % data, addr)
