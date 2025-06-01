# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    'url':Scrapy.field()
    'title': scrapy.Field()
    'product_type': scrapy.Field()
    'price_excluding_tax': scrapy.Field()
    'price_including_tax': scrapy.Field()
    'tax': scrapy.Field()

        