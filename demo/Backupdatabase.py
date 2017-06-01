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
dbUser='test'
dbPasswd='test'
#不能使用空密码的用户导出数据库
dbHost='127.0.0.1'
dbCharset = 'utf8'
backupDir = 'E:\\'
backupDate =  time.strftime("%Y%m%d")

print ('The database backup to start! %s'   %time.strftime('%Y-%m-%d %H:%M:%S'))
# 打开数据库连接
db = pymysql.connect(dbHost,dbUser,dbPasswd,'')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#查出MySQL中所有的数据库名称
sqlStr1 = "show databases"
#执行查询
cursor.execute(sqlStr1)
allDatabase = cursor.fetchall()
#循环导出
for db in allDatabase:
    dbName=db[0]
    fileName = '%s\\%s_%s.sql' %(backupDir,backupDate,dbName)
    if os.path.exists(fileName):
        os.remove(fileName)
    os.system("mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s/%s_%s.sql" %(dbHost,dbUser,dbPasswd,dbName,dbCharset,backupDir,backupDate,dbName))
print ('The database backup success! %s'%time.strftime('%Y-%m-%d %H:%M:%S'))

