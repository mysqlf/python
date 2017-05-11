#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import asyncio


# @asyncio.coroutine
# def hello():
#     print('hello world')
#     #使用异步将
#     r = yield from asyncio.sleep(1)
#     print('hello again')
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()
# import threading
# import asyncio


# @asyncio.coroutine
# def hello():
#     print('hello world (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('hello again(%s)' % threading.currentThread())
# loop = asyncio.get_event_loop()
# task = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(task))
# loop.close()
# hello world (<_MainThread(MainThread, started 5760)>)
# hello world (<_MainThread(MainThread, started 5760)>)
# hello again(<_MainThread(MainThread, started 5760)>)
# hello again(<_MainThread(MainThread, started 5760)>)
# [Finished in 1.2s]
#
# 3.5异步IO函数写法
import asyncio
async def hello():
    print('hello')
    r = await asyncio.sleep(1)
    print('hello again')
# 使用方面照旧
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
