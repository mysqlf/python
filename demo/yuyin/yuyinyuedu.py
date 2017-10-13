#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 语音阅读
# 
# python3 需要安装pyttsx3
# 文件地址
# 安装方法pip install pyttsx3
# https://github.com/nateshmbhat/pyttsx3
# pyttsx3 需要 pypiwin32
# pip install pypiwin32
import pyttsx3

def read_local_file(tts):
    file_name=input("file path:")
    try:
        fobj=open(file_name,'r')
    except IOError as e:
        print('file open error:{0}'.format(e))
        return 
    else:
        for eachline in fobj:
            print(eachline)
            tts.say(eachline)
            tts.runAndWait()
        fobj.close()

def init_tts():
    engine = pyttsx3.init()
    return engine
if __name__ == '__main__':
    tts=init_tts()
    read_local_file(tts)
    
