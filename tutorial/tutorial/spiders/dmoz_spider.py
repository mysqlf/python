from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem 


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://djangobook.py3k.cn/2.0/chapter01/",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="document"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['name'] = site.xpath('//p/text()').extract()
            item['title'] = site.xpath('//a/text()').extract()
            item['url']=site.xpath('//a/@href').extract()
            item['description'] = site.xpath('//ul/li/text()').extract()
            items.append(item)
        return items