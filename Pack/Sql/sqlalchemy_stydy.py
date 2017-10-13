#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql.cursors
from sqlalchemy.types import Integer
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    sex = Column(Integer)

engine = create_engine('mysql+pymysql://root:''@127.0.0.1:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
# 插入方法
new_test = Test(id=17, name='Bob', age=23, sex=1)
session.add(new_test)
session.commit()
# 查询方法
test = session.query(Test).filter(Test.id == '17').one()

print(test.name)
session.close()
