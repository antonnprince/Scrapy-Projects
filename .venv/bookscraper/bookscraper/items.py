# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# add money symbol to price
def serialize_price(value):
    return f'$ {str(value)}'

class BookItem(scrapy.Item):
    url = scrapy.Field()
    title =  scrapy.Field()
    product_type= scrapy.Field()
    # 'price_excluding_tax': scrapy.Field(serializer =serialize_price)
    price_excluding_tax =  scrapy.Field()
    price_including_tax =  scrapy.Field()
    tax =  scrapy.Field()

        