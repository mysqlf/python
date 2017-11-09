# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OneItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    #title = scrapy.Field()
class QuotesItem(scrapy.Item):
    content=scrapy.Field()
    author=scrapy.Field()
    author_url=scrapy.Field()
    tags=scrapy.Field()
#genspider anjuke 'quotes.toscrape.com'
class WangyiItem(scrapy.Item):
    sing=scrapy.Field()
    content=scrapy.Field()
class GovItem(scrapy.Item):
    #num=scrapy.Field()
    content=scrapy.Field()
class GanjiItem(scrapy.Item):
    address=scrapy.Field()
    price=scrapy.Field()
    biaoqian=scrapy.Field()


