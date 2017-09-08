# -*- coding: utf-8 -*-
import scrapy
from one.items import QuotesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        allowed_domains = ['quotes.toscrape.com']
        start_urls = ['http://quotes.toscrape.com/page/1/']
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    
    def parse(self, response):
        for sel in response.xpath('//div[@class="col-md-8"]/div'):
            item= QuotesItem()
            item['content']=sel.xpath('span/text()').extract()
            item['author']=sel.xpath('span/small/text()').extract()
            item['author_url']=sel.xpath('span/a/@href').extract()
            item['tags']=sel.xpath('div/a/text()').extract()
            yield item
