# -*- coding: utf-8 -*-
import scrapy
from one.items import GanjiItem
#赶集租房循环抓取
class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    #设置每个页面1s,防止被ban
    download_delay = 1  
    allowed_domains = ['sz.ganji.com']
    start_urls = ['http://sz.ganji.com/fang1/a1/']

    def parse(self,response):
        for sel in response.xpath('//div[@class="f-list js-tips-list"]/div'):
            item= GanjiItem()
            item['address']=sel.xpath('dl/dd[@class="dd-item address"]/span/a/text()').extract()
            item['price']=sel.xpath('dl/dd/div[@class="price"]/span/text()').extract()
            item['biaoqian']=sel.xpath('dl/dd[@class="dd-item size"]/span/text()').extract()
            yield item
        urls=response.xpath('//ul/li/a[@class="next"]/@href').extract()
        for url in urls:
            uri = 'http://sz.ganji.com'+url
            yield scrapy.Request(uri,callback=self.parse)

