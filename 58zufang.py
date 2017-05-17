#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf


import requests
from bs4 import BeautifulSoup
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

#from pyRedis import connredis
#r=connredis()

url='http://sz.58.com/nanshan/zufang/b11/?PGTID=0d300008-0000-44db-e022-14328f1c452a&ClickID=4'

class zufang():
	"""docstring for zufang"""
	def __init__(self, url):
		super(zufang, self).__init__()
		self.url = url

	def html(self):
		html = self.request(self.url)  # 调用request函数把套图地址传进去会返回给我们一个response
		all_address = BeautifulSoup(html.text, 'lxml').find_all('div', class_='des')
		for address in all_address:
			a_address=address.find('p',class_='add').get_text()
			print(a_address)
			
	def save(key,value):
		pass
	def request(self, url):  # 这个函数获取网页的response 然后返回
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
		content = requests.get(url, headers=headers)
		return content


zufang= zufang(url)
zufang.html()
		