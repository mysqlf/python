#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import time
# import threading


# def loop():
#     print('thread %s is running' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
# print('thread %s is running ' % threading.current_thread().name)
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print('thread %s send' % threading.current_thread().name)
#
# 输出
# thread MainThread is running
# thread LoopThread is running
# thread LoopThread >>> 1
# thread LoopThread >>> 2
# thread LoopThread >>> 3
# thread LoopThread >>> 4
# thread LoopThread >>> 5
# thread LoopThread ended
# thread MainThread send
# [Finished in 5.1s]
# blance = 0

# def chang_it(n):
#     global blance
#     blance = blance + n
#     blance = blance - n


# def runthread(n):
#     for i in range(50000):
#         chang_it(n)
# t1 = threading.Thread(target=runthread, args=(5,))
# t2 = threading.Thread(target=runthread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(blance)

# blance = 0
# lock = threading.Lock()


# def run_thread(n):
#     for i in range(1000):
#         lock.acquire()
#         try:
#             chang_it(n)
#         finally:
#             lock.release()
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(blance)
# import threading
# local_school = threading.local()


# def process_student():
#     std = local_school.student
#     print('Hello %s (in %s)' % (std, threading.current_thread().name))


# def process_thread(name):
#     local_school.student = name
#     process_student()
# t1 = threading.Thread(target=process_thread, args=('A'), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('B'), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# 输出
# Hello A (in Thread-A)
# Hello B (in Thread-B)
# 线程内的面向对象实现吧,每个线程内有一个自己的变量绑定数组
# 就和对象的属性一样,对象之间互不干扰
