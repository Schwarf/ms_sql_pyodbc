# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def open_spider(self, spider):
        self._json_file = open('book_items.json', 'w')

    def close_spider(self, spider):
        self._json_file.close()

    def process_item(self, item, spider):
        print("HALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOOOOOOOOOOO")
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self._json_file.write(line)
        return item
