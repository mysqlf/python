# -*- coding: utf-8 -*-
import scrapy
from one.items import OneItem

class ScrapychsSpider(scrapy.Spider):
    name = 'scrapychs'
    def start_requests(self):
        allowed_domains = ['scrapy-chs.readthedocs.io']
        start_urls = ['http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html']
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response):
        for sel in response.xpath('//div[@class="section"]'):
            item= OneItem()
            item['text']=sel.xpath('p/text()').extract()
            yield item

