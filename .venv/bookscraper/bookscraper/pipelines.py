# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name !='description':
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()

        lowercase_keys =['category','product_type']
        for key in lowercase_keys:
            value = adapter.get(key)
            adapter[key] = value.lower()

        price_keys = ['price_excluding_tax', 'price_including_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            adapter[price_key] = float(value)

        
        return item
