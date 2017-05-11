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
        sql = 'insert into job_qiancheng(salar, exp, com, position, www, position_num) values(%s,%s,%s,%s,%s,%s)'
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
    salar = tree.xpath('//div[@class="el"]/span[@class="t4"]/text()')

    # 公司
    com = tree.xpath('//span[@class="t2"]/a/text()')

    for a, c in zip(salar, com):
        tmp = []
        tmp.append(a)
        tmp.append(c)
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
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=php&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_java_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=java&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_ui_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=UI&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_js_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_cs_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_chanpin_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_jszj_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E6%8A%80%E6%9C%AF%E6%80%BB%E7%9B%91&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=03&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def build_jsjl_url(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E6%8A%80%E6%9C%AF%E7%BB%8F%E7%90%86&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    return url


def lunzi(job, page, num, position):
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
        result = app_from(res, 'qiancheng')
        for tmp in result:
            D.add(tmp[0], '1-3年', tmp[1], position, tmp[2], num)
    time.sleep(1)

# url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=php&keywordtype=2&curr_page=' + str(page) + '&lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
# get_one_page_data(url)


lunzi('php', 8, 1, 'php')
lunzi('java', 13, 2, 'java')
lunzi('qianduan', 15, 3, '前端')
lunzi('ui', 7, 4, 'UI')
lunzi('chanpin', 9, 5, '产品经理')
lunzi('cs', 18, 6, '测试')
lunzi('jsjl', 1, 7, '技术经理')
lunzi('jszj', 2, 8, '技术总监')
