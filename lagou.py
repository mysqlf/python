#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import time
from lxml import html

import pymysql.cursors
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

class db:
        # 初始化数据库连接

    def __init__(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'db': 'test',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
        }

        # Connect to the database
        self.connection = pymysql.connect(**config)
        self.cursor = self.connection.cursor()

    def add(self, salar, exp, com, position, www, num):
        # try:
        sql = 'insert into job(salar, exp, com, position, www,position_num) values(%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (salar, exp, com, position, www, num))
        self.connection.commit()
        # finally:
        #    self.connection.close()


def get_one_page_data(url):
    result = []
    res = urllib.request.urlopen(url)
    tree = html.fromstring(res.read())
    # 工资
    salar = tree.xpath('//span[@class="money"]/text()')
    # 经验
    exps = tree.xpath('//div[@class="li_b_l"]/text()')
    # 公司
    com = tree.xpath('//div[@class="company_name"]/a/text()')
    # 职位名称
    position = tree.xpath('//a[@class="position_link"]/h2/text()')
    exp = removeEmptyInList(exps)

    for a, e, c, p in zip(salar, exp, com, position):
        tmp = []
        tmp.append(a)
        tmp.append(p)
        tmp.append(c)
        tmp.append(e.split()[0])
        result.append(tmp)
    return result


# 筛选


def fitler_exp(list, exp):
    result = []
    for x in list:
        if x[3] == exp:
            result.append(x)
    return result

# 去空


def removeEmptyInList(list):
    newList = []
    for i in range(len(list)):
        if len(list[i].split()) < 2:
            pass
        else:
            newList.append(list[i])

    return newList

# 获取总页数


def get_count_page(url):
    res = urllib.request.urlopen(url)
    tree = html.fromstring(res.read())
    # 工资
    count_page = tree.xpath('//span[@class="span totalNum"]/text()')
    return count_page

# 数据标签


def app_from(list, ww):
    for tmp in list:
        tmp.append(ww)
    return list

# 构建链接


def build_url(lang, page, Option):
    return 'https://www.lagou.com/zhaopin/' + lang + '/' + str(page) + '/?filterOption=' + str(Option)

# 抓取


def lunzi(lang, Option, num):
    url = build_url(lang, 2, Option)
    #result = []
    D = db()
    count = get_count_page(url)
    for i in range(2, int(count[0])):
        page_url = build_url(lang, i, Option)
        res = get_one_page_data(page_url)
        exp = '经验1-3年'
        filt_res = fitler_exp(res, exp)
        arr = app_from(filt_res, 'lagou')
        for one in arr:
            D.add(one[0], one[3], one[2], one[1], one[4], num)
            # result.append(one)
        time.sleep(1)
    # return result


def lunzi_zj(lang, Option, num):
    url = build_url(lang, 2, Option)
    #result = []
    D = db()
    count = get_count_page(url)
    for i in range(2, int(count[0])):
        page_url = build_url(lang, i, Option)
        res = get_one_page_data(page_url)
        #exp = '经验1-3年'
        #filt_res = fitler_exp(res, exp)
        arr = app_from(res, 'lagou')
        for one in arr:
            D.add(one[0], one[3], one[2], one[1], one[4], num)
            # result.append(one)
        time.sleep(1)

# print(phpresult)
# lunzi('PHP', 3, 1)
# lunzi('Java', 2, 2)
# lunzi('qianduankaifa', 2, 3)
# lunzi('UIshejishi', 2, 4)
# lunzi('chanpinjingli1', 2, 5)
# lunzi('ceshi', 2, 6)
lunzi_zj('jishujingli', 2, 7)
lunzi_zj('jishuzongjian', 2, 8)
