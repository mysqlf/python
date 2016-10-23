from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
import re


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://djangobook.py3k.cn/2.0/chapter01/",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="section"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('//p[@class="title"]').extract()
            item['name'] = site.xpath('//p[@class="cn"]').extract()
            item['url'] = site.xpath('//a/@href').extract()
            item['description'] = site.xpath(
                '//ul/li/p[@class="first"]').extract()
            items.append(item)
        return items
