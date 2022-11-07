# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

#from database.database_access.access import get_database_connection


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
        sql_statement = f"SET NOCOUNT ON"\
                        f"INSERT INTO books (title, price, upc, availability, number_of_copies, url, image_url)" \
                        f"VALUES (?, ?, ?, ?, ?, ?, ?)"
        self._cursor.execute(sql_statement, (item['title'],
                                             item['price'],
                                             item['upc'],
                                             item['availability'],
                                             item['number_of_copies'],
                                             item['url'],
                                             item['image_url']))

    def close_spider(self, spider):
        self._cursor.commit()
        self._database_connection.close()
"""