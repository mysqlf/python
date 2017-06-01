#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
#导入模块
import pymysql
import time
import datetime
import os
"""
  Purpose: 备份数据库
"""
def backup_database(backupDate=''):
    dbUser='test'
    #不能使用空密码的用户导出数据库
    dbPasswd='test'
    dbHost='127.0.0.1'
    dbCharset = 'utf8'
    backupDir = 'E:\\'
    if len(backupDate)==0:
        backupDate =  time.strftime("%Y%m%d\\%H-%M")
    print ('The database backup to start! %s'%time.strftime('%Y-%m-%d %H:%M:%S'))
    # 打开数据库连接
    db = pymysql.connect(dbHost,dbUser,dbPasswd,'')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    #查出MySQL中所有的数据库名称
    sqlStr1 = "show databases"
    #执行查询
    cursor.execute(sqlStr1)
    allDatabase = cursor.fetchall()
    #根据日期时间生成目录
    path=backupDir+backupDate
    if not os.path.exists(path):
        os.makedirs(path)
    #循环导出
    for db in allDatabase:
        dbName=db[0]
        fileName = '%s\\%s.sql' %(path,dbName)
        if os.path.exists(fileName):
            os.remove(fileName)
        os.system("mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s" %(dbHost,dbUser,dbPasswd,dbName,dbCharset,fileName))
    print ('The database backup success! %s'%time.strftime('%Y-%m-%d %H:%M:%S'))

backup_database()
