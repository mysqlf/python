# -*- coding: utf-8 -*-
import scrapy
from one.items import QuotesItem

class FollowSpider(scrapy.Spider):
    name = 'follow'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/tag/books/page/1/']

    def parse(self, response):
        for href in response.xpath('//ul/li[@class="next"]/a/@href'):
            url=response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_dir_contents)
    
    def parse_dir_contents(self,response):
        for sel in response.xpath('//div[@class="col-md-8"]/div'):
            item= QuotesItem()
            item['content']=sel.xpath('span/text()').extract()
            item['author']=sel.xpath('span/small/text()').extract()
            item['author_url']=sel.xpath('span/a/@href').extract()
            item['tags']=sel.xpath('div/a/text()').extract()
            yield item
