#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# win下没有fork方法,,,,这段代码在win下无法执行
# import os
# print('Process(%s) start'%os.getpid())
# pid=os.fork()
# if pid==0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# 多进程实例
#  from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s(%s)...'%(name,os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     p.start()
#     p.join()
#     print('Child process end')
#
# D:\Git\python>more.py
# Parent process 6752.
# Run child process test(7444)...
# Child process end

# 多进程实例
from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end-start)))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done')

# 多进程实例
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     #print('Run task %s (%s)...'%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('Task %s runs %0.2f seconds'%(name,(end-start)))

# if __name__=='__main__':
#     print('Parent process %s'%os.getpid())
#     p=Pool(8)
#     for i in range(9):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done')

# D:\Git\python>more.py
# Parent process 7324
# Waiting for all subprocesses done...
# Run task 0 (7552)...
# Run task 1 (7236)...
# Run task 2 (1836)...
# Run task 3 (7936)...
# Task 0 runs 0.49 seconds
# Run task 4 (7552)...
# Task 2 runs 0.58 seconds
# Task 4 runs 0.28 seconds
# Task 1 runs 1.58 seconds
# Task 3 runs 2.82 seconds
# All subprocesses done

#
# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])#nslookup 查询dns
# print('Exit code :',r)
# $ nslookup www.python.org
# 服务器:  cache-a.guangzhou.gd.cn
# Address:  202.96.128.86

# 非权威应答:
# 名称:    prod.python.map.fastlylb.net
# Addresses:  2a04:4e42:4::223
#           151.101.36.223
# Aliases:  www.python.org
#           python.map.fastly.net

# Exit code : 0

# import subprocess
# print('$ nslookup')
# p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')#这一段将作为输入参数传入函数内,实际使用可使用获取输入传递方式
# print(output.decode('latin-1').encode('utf-8'))
# print('Exit code:',p.returncode)
