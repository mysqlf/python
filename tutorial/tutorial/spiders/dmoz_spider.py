from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
import re


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["12333sh.gov.cn"]
    start_urls = [
        "http://www.12333sh.gov.cn/201412333/wsbs/bszn/index.shtml",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="gfwjcontent"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['name'] = site.xpath('//a/text()').extract()
            item['url'] = site.xpath('//a/@href').extract()
            #item['title'] = site.xpath('//p[@class="title"]').extract()
            # item['name']= site.xpath('//p[@class="cn"]').extract()
            # item['url'] = site.xpath('//a/@href').extract()
            # item['description'] = site.xpath(
            #     '//ul/li/p[@class="first"]').extract()
            items.append(item)
        return items
