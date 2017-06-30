#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf

import time
from threading import Thread
# def countdown(n):
#     while n>0:
#         print('T-minus',n)
#         n-=1
#         time.sleep(2)

# t=Thread(target=countdown,args=(10,))
# t.start()
# #监听线程是否还在运行
# if t.is_alive():
#     print('still running')
# else:
#     print('completed')

#-------可以手动停止的-----
class CountdownTask:
    def __init__(self):
        self.running=True
    def terminate(self):#手动停止线程
        self._running=False
    def run(self,n):
        print('T-minus',n)
        n-=1
        time.sleep(2)
c=CountdownTask()
t=Thread(target=c.run,args=(10,))
t.start()

c.terminate()
t.join()

class IOTask:
    def terminate(self):
        self._running=False
    def run(self,sock):
        sock.settimeout(5)
        while self._running:
            try:
                data=sock.recv(8192)
                break
            except socket.timeout:
                continue
        return 
class Base(object):
    def __init__(self):
        print ("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

print(ChildA(),ChildB())
#python 三元运算
c=1
a=2
b=3
d=4
x= (c if (a>b) else d)
print(x)
