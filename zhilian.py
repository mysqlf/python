#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import sys
import urllib.request
import time
from lxml import html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
import pymysql.cursors


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
        sql = 'insert into job_zhilian(salar, exp, com, position, www, position_num) values(%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (salar, exp, com, position, www, num))
        self.connection.commit()
        # finally:
        #    self.connection.close()

# 获取一页数据


def get_one_page_data(url):
    result = []
    res = urllib.request.urlopen(url)
    tree = html.fromstring(res.read())
    # 工资
    salar = tree.xpath('//td[@class="zwyx"]/text()')

    # 经验
    # exps = tree.xpath('//div[@class="li_b_l"]/text()')
    # 公司
    com = tree.xpath('//td[@class="gsmc"]/a/text()')

    # 职位名称
    position = tree.xpath('//td[@class="zwmc"]/div/a/text()')

   # exp = removeEmptyInList(exps)

    for a, c, p in zip(salar, com, position):
        tmp = []
        tmp.append(a)
        tmp.append(c)
        tmp.append(p)
        result.append(tmp)
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


def app_from(list, ww):
    for tmp in list:
        tmp.append(ww)
    return list


def build_php_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=php&sm=0&kt=3&we=0103&isfilter=1&fl=765&isadv=0&sg=0c28c697e2f94c5b957a543aafd9b3e7&p=' + str(page)
    return url


def build_java_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=java&kt=3&isadv=0&isfilter=1&we=0103&sg=9f229661d58c4bb5932141e4476a9bfc&p=' + str(page)
    return url


def build_ui_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=UI&sm=0&isfilter=1&we=0103&sg=15a84cad84664d408847a43e829c4621&p=' + str(page)
    return url


def build_js_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E5%89%8D%E7%AB%AF&sm=0&isadv=0&isfilter=1&we=0103&sg=aad7fee1a8144e8bbb7330b3fd5481d6&p=' + str(page)
    return url


def build_cs_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&isadv=0&isfilter=1&we=0103&sg=ade2b9cc68c8419580055da91f0cfacd&p=' + str(page)
    return url


def build_chanpin_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86%E4%BA%92%E8%81%94%E7%BD%91&sm=0&isadv=0&isfilter=1&we=0103&sg=a722439dcbb04966a685edc9db73ad52&p=' + str(page)
    return url


def build_jszj_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E6%8A%80%E6%9C%AF%E6%80%BB%E7%9B%91&sm=0&isadv=0&we=-1&isfilter=1&bj=160000&sg=64c9f6e2e7624fc79c04dd15cb9a2e29&p=' + str(page)
    return url


def build_jsjl_url(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E6%8A%80%E6%9C%AF%E7%BB%8F%E7%90%86&isadv=0&isfilter=1&we=0103&sg=ce08c1f1c241460699a44d9c2345ec79&p=' + str(page)
    return url


def lunzi(job, page, num):
    D = db()
    for i in range(1, page):
        if job == 'php':
            url = build_php_url(i)
        elif job == 'java':
            url = build_java_url(i)
        elif job == 'ui':
            url = build_ui_url(i)
        elif job == 'qianduan':
            url = build_js_url(i)
        elif job == 'cs':
            url = build_cs_url(i)
        elif job == 'chanpin':
            url = build_chanpin_url(i)
        elif job == 'jsjl':
            url = build_jsjl_url(i)
        elif job == 'jszj':
            url = build_jszj_url(i)
        res = get_one_page_data(url)
        result = app_from(res, 'zhilian')
        for tmp in result:
            D.add(tmp[0], '1-3年', tmp[1], tmp[2], tmp[3], num)
    time.sleep(1)

# php 1
# java 2
# qianduan 3
# UI 4
# chanpin 5
# cs 6
# jsjl 7
# jszj 8
#
# lunzi('php', 5, 1)
# lunzi('java', 9, 2)
# lunzi('qianduan', 15, 3)
# lunzi('ui', 12, 4)
# lunzi('chanpin', 7, 5)
# lunzi('cs', 4, 6)
# lunzi('jsjl', 6, 7)
# lunzi('jszj', 5, 8)
