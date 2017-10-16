#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# import pythoncom
# import pyHook
# import time

# def onMouseEvent(event):
#     '''处理鼠标事件'''
#     fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
#     fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
#     fobj.writelines("MessageName:%s\n" % str(event.MessageName))
#     fobj.writelines("Message:%d\n" % event.Message)
#     fobj.writelines("Time_sec:%d\n" % event.Time)
#     fobj.writelines("Window:%s\n" % str(event.Window))
#     fobj.writelines("WindowName:%s\n" % str(event.WindowName))
#     fobj.writelines("Position:%s\n" % str(event.Position))
#     fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
#     return True
# def onKeyboardEvent(event): 
#     '''处理键盘事件'''   
#     fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
#     fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
#     fobj.writelines("MessageName:%s\n" % str(event.MessageName))
#     fobj.writelines("Message:%d\n" % event.Message)
#     fobj.writelines("Time:%d\n" % event.Time)
#     fobj.writelines("Window:%s\n" % str(event.Window))
#     fobj.writelines("WindowName:%s\n" % str(event.WindowName))
#     fobj.writelines("Ascii_code: %d\n" % event.Ascii)
#     fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))
#     fobj.writelines("Key:%s\n" % str(event.Key))
#     fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
#     return True

# if __name__ == '__main__':
#     file_name="hook_log.txt"
#     fobj=open(file_name,'a+')
#     hm=pyHook.HookManager()
#     hm.KeyDown=onKeyboardEvent
#     hm.HookKeyboard()
#     hm.MouseAll=onMouseEvent
#     hm.HookMouse()
#     pythoncom.PumpMessages(1000)
#     fobj.close()
#     
#     第二版
import os
import sys
import pythoncom
import pyHook
import time,os
import win32api
def onMouseEvent(event):
    # """监听鼠标事件"""
    global preWindowName, switch
    if not os.path.exists(mouseFilepath):
        os.makedirs(mouseFilepath)
    if switch:    
        localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        datafileName = localTime[:localTime.find(" ")] + ".txt"
        #time  WindowName
        if not os.path.exists(mouseFilepath + datafileName):
            f = open(mouseFilepath + datafileName, "w")
            f.write("localTime                windowname\n")
            f.close()
        if type(event.WindowName) ==  str:     
            if event.WindowName != preWindowName:
                datafileContent = localTime + ',    ' + event.WindowName + '\n'
                f = open(mouseFilepath + datafileName, "a")
                f.write(datafileContent)
                f.close()
                preWindowName = event.WindowName
    #返回True以便将事件传给其他处理程序
    return True

def onKeyboardEvent(event):
    """监听键盘事件"""
    global switch
    if not os.path.exists(keyboardFilepath):
        os.makedirs(keyboardFilepath)

    if switch:
        localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        datafileName = localTime[:localTime.find(" ")] + ".txt"
        #time keyvalue Key WindowName
        if not os.path.exists(keyboardFilepath + datafileName):
            f = open(keyboardFilepath + datafileName, "w")
            f.write("localTime        keyvalue        key        windowname\n")
            f.close()
        if type(event.WindowName) ==  str:
            datafileContent = localTime + ',    ' + chr(event.Ascii) + ',    ' \
                    + event.Key + ',    ' + event.WindowName + '\n'
            f = open(keyboardFilepath + datafileName, "a")
            f.write(datafileContent)
            f.close()

    if event.KeyID == 120:#Key=F9
        switch = True
    #按下F12才能真正结束
    elif event.KeyID == 123:#Key=F12
        win32api.PostQuitMessage()
        sys.exit()
    #把python当快捷键监听，如果是按下F10就打开我的桌面图标motv，类似的你可以多定义几个，这就是你的自定义快捷键功能
    elif event.KeyID == 121:
        import subprocess
        p = subprocess.Popen("cmd.exe /c" + "C:\\Users\\Administrator\\Desktop\\motv.lnk", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #print(event.KeyID)
    #同鼠标监听事件函数的返回值
    return True

def main():
    """创建一个'钩子'管理对象"""
    hm = pyHook.HookManager()
    #监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    #设置键盘'钩子'
    hm.HookKeyboard()
    #监听所有鼠标事件
    #hm.MouseAll = onMouseEvent
    #设置鼠标'钩子'
    #hm.HookMouse()
    #进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages(1000)
  
    # os.exit()

if __name__ == '__main__':
    keyboardFilepath = "./key/"
    mouseFilepath = "./mouse/"
    preWindowName = ''
    switch = True #控制是否开启日志功能
    main()

#第三版
# # -*- coding: utf-8 -*-
# import pythoncom  
# import pyHook  
# import time
# import win32api
# t=''
# asciistr=''
# keystr=''
# def onKeyboardEvent(event):   
#     global t,asciistr,keystr
#     filename='test.txt'
#     wrfile=open(filename,'ab')
#     #"处理键盘事件"
#     if t==str(event.WindowName):
#         asciistr=asciistr+chr(event.Ascii)
#         keystr=keystr+str(event.Key)
#     else:
#         t=str(event.WindowName)
#         if asciistr=='' and keystr=='':
#             wrfile.writelines("\nWindow:%s\n" % str(event.Window))
#             wrfile.writelines("WindowName:%s\n" % str(event.WindowName)) #写入当前窗体名
#             wrfile.writelines("MessageName:%s\n" % str(event.MessageName))
#             wrfile.writelines("Message:%d\n" % event.Message)
#             wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#         else:
#             wrfile.writelines("Ascii_char:%s\n" %asciistr)
#             wrfile.writelines("Key_char:%s\n" %keystr)
#             wrfile.writelines("\nWindow:%s\n" % str(event.Window))
#             wrfile.writelines("WindowName:%s\n" % str(event.WindowName)) #写入当前窗体名
#             wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        
#         asciistr=chr(event.Ascii)
#         keystr=str(event.Key)
#     if str(event.Key)=='F12':  #按下F12后终止
#         wrfile.writelines("Ascii_char:%s\n" %asciistr)
#         wrfile.writelines("Key_char:%s\n" %keystr)
#         wrfile.close()    
#         win32api.PostQuitMessage()
#     return True
# if __name__ == "__main__":
#     '''
# 小五义：http://www.cnblogs.com/xiaowuyi
# '''
#     #创建hook句柄  
#     hm = pyHook.HookManager()  
#     #监控键盘  
#     hm.KeyDown = onKeyboardEvent  
#     hm.HookKeyboard()  
#     #循环获取消息  
#     pythoncom.PumpMessages(100) 

