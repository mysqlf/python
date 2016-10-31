#!/usr/bin/env python
__author__ = 'GreedyWolf'
# -*- coding:utf-8 -*-
import time
import sys
import urllib
f_handler = open('out.log', 'w')
sys.stdout = f_handler


class ask():

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    def getCurrentDate(self):
        return time.strftime('[%Y-%m-%d]', time.localtime(time.time()))

    def main(self):
        f_handler = open('out.log', 'w')
        sys.stdout = f_handler
        page = open('page.txt', 'r')
        content = page.readline()
        start_page = int(content.strip())-1
        page.close()
        print(self.getCurrentTime(), '开始页码', start_page)
        print(self.getCurrentTime(), '开始启动')
        self.total_num = self.getTotalPageNum()
        print(self.getCurrentTime(), '获取到的页面个数', self.total_num, '个')
        if not start_page:
            start_page = self.total_num
        for x in range(1, start_page):
            print(self.getCurrentTime(), '正在抓取', start_page-x+1, '个页面')
            try:
                self.getQuestions(start_page-x+1)
                Exception
