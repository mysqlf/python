# -*- coding: utf-8 -*-
import scrapy
from one.items import WangyiItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/weapi/v1/resource/comments/R_SO_4_27483204?csrf_token=5ac9f77928358e613345eb182c52f9d8']

    def parse(self, response):
        print(response)
        exit(1)
        sing=response.xpath('//div[@class="tit"]/em/text()').extract()
        print(sing)
        # exit()
        # filename=sing+'.txt'
        # f=fopen(filename,'w')

        # for sel in response.xpath('//div[@class="cmmts j-flag"]'):
        #     name=sel.xpath('div[@class="itm"]/div[@class="cntwrap"]/div/div[@class="cnt f-brk"]/a/text()')
        #     content=sel.xpath('div[@class="itm"]/div[@class="cntwrap"]/div/div[@class="cnt f-brk"]/text()')
        #     f.write(name)
        #     f.write(conten)
            
        
