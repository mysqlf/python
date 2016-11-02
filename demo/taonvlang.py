#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Greedy-Wolf'

import urllib.request
import urllib
import os
import re
import sys


class Spide:

    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        #req = urllib.request.Request(url=url)
        resource = urllib.request.urlopen(url)
        content = resource.read().decode('gbk')
        return content
        # req = urllib.request.Request(url)
        # response = urllib.request.urlopen(req)
        # print(response.read())
        # page = response.read().encode('').decode("gbk")
        # return page

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4])

Spide = Spide()
Spide.getContents(1)


# import urllib.request
# f = urllib.request.urlopen('http://www.python.org/')
# print(f.read(300))
