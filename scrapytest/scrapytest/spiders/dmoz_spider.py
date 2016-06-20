from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapytest.items import DmozItem 
class DmozSpider(Spider):
    name="dmoz"
    allowed_domains=['dmoz.org']
    start_url=["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/","http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]
        # def parse(self,response):
        #         filename=response.url.split("/")[-2]
        #         open(filename,'wb').write(response.body)
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print(title, link, desc)
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)
        return items