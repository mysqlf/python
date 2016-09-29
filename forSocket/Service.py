#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time


def tcplink(sock, addr):
    print('Accpet new connection from %s:%s..' % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection From %s:%s closed' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(3)
print('waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
