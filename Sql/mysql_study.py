#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# py连接数据库
# 使用库PyMySql
import pymysql.cursors
# 使用dict 连接数据库
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': '',
#     'db': 'test',
#           'charset': 'utf8mb4',
#           'cursorclass': pymysql.cursors.DictCursor,
# }

# # Connect to the database
# connection = pymysql.connect(**config)
# cursor = connection.cursor()
# try:
#     sql = 'insert into test(name,age,sex) values(\'zl\',23,1)'
#     cursor.execute(sql)
#     connection.commit()
# finally:
#     connection.close()

# 面向对象实现


class db:
        # 初始化数据库连接

    def __init__(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'db': 'test',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
        }

        # Connect to the database
        self.connection = pymysql.connect(**config)
        self.cursor = self.connection.cursor()

    def add(self, name, age, sex):
        try:
            sql = 'insert into test(name,age,sex) values(%s,%s,%s)'
            self.cursor.execute(sql, (name, age, sex))
            self.connection.commit()
        finally:
            self.connection.close()

    def select(self, id):
        try:
            sql = 'select * from test where id=%s'
            self.cursor.execute(sql, id)
            result = self.cursor.fetchone()
            # self.connection.commit()
            return result
        finally:
            self.connection.close()
test = db()
#test.add('wj', 22, 2)
k = test.select(14)
print(k)
