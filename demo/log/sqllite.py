#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import logging
import logging.config
import sqlite3
#日志配置文件
LOG_FILENAME='logging.conf'
#日志语句提示信息
LOG_CONTENT_NAME='sqlite_log'
#定义SQLite 数据库名称
DB_SQLTE_PATH='.\\sqlite_pytest.db'

def log_init(log_config_filename,logname):
    logging.config.fileConfig(log_config_filename)
    logger=logging.getLogger(logname)
    return logger
def sqlite_close(sqlite_cursor,sqlite_conn):
    sqlite_cursor.close()
    sqlite_conn.close()

def operate_sqlite3_tbl_product():
    sqlite_logger.debug('operate_sqlite3_tbl_product enter..')
    #连接数据库
    try:
        sqlite_conn=sqlite3.connect(DB_SQLTE_PATH)
    except sqlite3.Error as e:
        print('connect sqlite database faild')
        sqlite_logger.error("connect sqlite3 database failed ,ret=%s"%e.args[0])
        return 
    sqlite_logger.info('connect sqlite database(%s) succ'% DB_SQLTE_PATH)
    sqlite_cursor=sqlite_conn.cursor()
    #删除表
    sql_desc2="DROP table if exists tbl_product3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    try:
        sqlite_cursor.execute(sql_desc2)
    except Exception as e:
        print('drop table failed')
        sqlite_logger.Error('drop table failed ,ret=%s'%e.args[0])
        sqlite_close(sqlite_cursor,sqlite_conn)
        return
    sqlite_conn.commit()
    sqlite_logger.info('drop table(tbl_product3) succ')
    #创建表
    sql_desc='''Create table tbl_product3(
    i_index integer primary key,
    sv_productname varchar(32)
    );'''
    try:
        sqlite_cursor.execute(sql_desc)
    except Exception as e:
        print('create table filed')
        sqlite_logger.Error('create table failed ,ret=%s'%e.args[0])
        sqlite_close(sqlite_cursor,sqlite_conn)
        return 
    sqlite_conn.commit()
    sqlite_logger.info('create table(tbl_product3) succ')
    
    #插入记录
    sql_desc="insert into tbl_product3(sv_productname) values('apple')"
    try:
        sqlite_cursor.execute(sql_desc)
    except Exception as e:
        print('insert filed')
        sqlite_logger.Error('insert  failed ,ret=%s'%e.args[0])
        sqlite_close(sqlite_cursor,sqlite_conn)
        return 
    sqlite_conn.commit()
    sqlite_logger.info('insert table(tbl_product3) succ')
    #查询
    sql_desc="select * from tbl_product3;"
    sqlite_cursor.execute(sql_desc)
    for row in sqlite_cursor:
        print(row)
        sqlite_logger.info("%s",row)
    sqlite_close(sqlite_cursor,sqlite_conn)
    sqlite_logger.debug('886')
if __name__ == '__main__':
    sqlite_logger=log_init(LOG_FILENAME, LOG_CONTENT_NAME)
    operate_sqlite3_tbl_product()
