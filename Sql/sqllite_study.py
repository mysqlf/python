#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sqllite
import sqlite3
# 连接到sqlite
# 数据库文件test.db@不存在会自动创建

# try:
#     conn = sqlite3.connect('test.db')
#     cursor = conn.cursor()

#     #cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
#     #cursor.execute('insert into user(id,name) values(\'1\', \'ZL\')')
#     cursor.execute('select * from user where id=\'1\'')
#     values = cursor.fetchall()
#     print(values)
# except Exception:
#     print(Exception)
# finally:
#     cursor.close()
#     conn.commit()
#     conn.close()

#
# # print(x)
# cursor.close()
# conn.commit()
# conn.close()
# -*- coding: utf-8 -*-

import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute(
    'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(
            'select * from user where score between ? and ? order by score ', (low, high))
        values = cursor.fetchall()
        print([x[0] for x in values], ', get_score_in(%s, %s)' % (low, high))
    except Exception:
        print('查询失败')
    finally:
        cursor.close()
        conn.commit()
        conn.close()
# 测试:
# x = get_score_in(80, 100)
# print(x)
get_score_in(30, 100)
#assert get_score_in(96, 100) == ['Adam'], get_score_in(70, 95)
#assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
#assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
