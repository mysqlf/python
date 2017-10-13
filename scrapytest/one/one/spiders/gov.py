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
        for sel in response.xpath('//*[@id="Zoom"]'):
            item= GovItem()
            print(sel.tags())
            item['content']=sel.xpath('string(.)').extract()#获取多标签内的文字,适用于不规则页面内容获取
            yield item

