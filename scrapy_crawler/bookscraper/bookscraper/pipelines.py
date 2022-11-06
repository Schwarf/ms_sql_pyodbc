# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

# from database.database_access.access import get_database_connection


class BookscraperPipeline:
    def open_spider(self, spider):
        self._json_file = open('book_items.jsonl', 'w')

    def close_spider(self, spider):
        self._json_file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self._json_file.write(line)
        return item

"""
class SQLServerPipeline:
    def open_spider(self, spider):
        self._database_connection = get_database_connection(
            password_file='/home/andreas/Documents/database_access/access.txt')
        self._cursor = self._database_connection.cursor()

    def process_item(self, item, spider):
        pass

    def close_spider(self, spider):
        self._cursor.commit()
        self._database_connection.close()
"""