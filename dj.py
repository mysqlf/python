# -*- coding: utf-8 -*-

# import django
# print(django.VERSION)

import django
print(django.VERSION)
# print('asd')
import socket


def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None
name, alias, addresslist = lookup('4.2.2.2')
# print(name)
