# -*- coding: utf-8 -*-
import scrapy
from one.items import QuotesItem

class FollowSpider(scrapy.Spider):
    name = 'follow'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for sel in response.xpath('//div[@class="col-md-8"]/div'):
            item= QuotesItem()
            item['content']=sel.xpath('span[1]/text()').extract()
            item['author']=sel.xpath('span/small/text()').extract()
            item['author_url']='http://quotes.toscrape.com/author/'+sel.xpath('span/a/@href').extract()
            item['tags']=sel.xpath('div/a/text()').extract()
            yield item
        urls=response.xpath('//ul/li[@class="next"]/a/@href').extract()
        for url in urls:
            url = 'http://quotes.toscrape.com'+url
            yield scrapy.Request(url,callback=self.parse)
    #     for href in self.start_urls:
    #         yield scrapy.Request(href,callback=self.parse_dir_contents)
    #     self.start_urls.append(response.xpath('//ul/li[@class="next"]/a/@href').extract())
    # def parse_dir_contents(self,response):
    #     for sel in response.xpath('//div[@class="col-md-8"]/div'):
    #         item= QuotesItem()
    #         item['content']=sel.xpath('span/text()').extract()
    #         item['author']=sel.xpath('span/small/text()').extract()
    #         item['author_url']=sel.xpath('span/a/@href').extract()
    #         item['tags']=sel.xpath('div/a/text()').extract()
    #         yield item
