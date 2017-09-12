# -*- coding: utf-8 -*-
import scrapy
from one.items import GovItem

class GovSpider(scrapy.Spider):
    name = 'gov'
    allowed_domains = ['www.gov.cn']
    start_urls = [
                    'http://www.gov.cn/ziliao/flfg/2005-06/14/content_6310_3.htm',
                ]

    def parse(self, response):
        for url in range(3,12):
            url = 'http://www.gov.cn/ziliao/flfg/2005-06/14/content_6310_'+str(url)+'.htm'
            yield scrapy.Request(url,callback=self.parse_content)

    def parse_content(self,response):
        for sel in response.xpath('//td[@class="p1"]'):
            item= GovItem()
            item['content']=sel.xpath('font/text()').extract()
            yield item

