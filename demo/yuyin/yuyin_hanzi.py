#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
#汉语阅读
#可以直接使用win的api实现
#所以这个脚本只适用于win平台
import win32com.client
import time
spk = win32com.client.Dispatch("SAPI.SpVoice")
for i in range(100):
    spk.Speak(u"%d你好"%i)
    time.sleep(1)
