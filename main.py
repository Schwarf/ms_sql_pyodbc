import argparse
import sys

import scrapy
from scrapy.crawler import CrawlerProcess

from database_access.access import get_database_connection
from scrapy_crawler.bookscraper.bookscraper.pipelines import BookscraperPipeline
from scrapy_crawler.bookscraper.bookscraper.spiders.bookscraper import BookScraper


def _create_engine(self):
    engine = scrapy.core.engine.ExecutionEngine(self, lambda _: self.stop())
    engine.scraper.itemproc._add_middleware(BookscraperPipeline())  # loads item pipeline
    # engine.donwloader.middleware._add_middleware(downloader_middleware_class)
    return engine


"""
ITEM_PIPELINES = {
    'mybot.pipelines.validate.ValidateMyItem': 300,
    'mybot.pipelines.validate.StoreMyItem': 800,
}
"""


def main2() -> None:
    spider = BookScraper()
    #    scrapy.crawler.Crawler._create_engine = _create_engine
    settings ={}
    settings['ITEM_PIPELINES'] = {'scrapy_crawler.bookscraper.bookscraper.pipelines.BookscraperPipeline': 300, }
    process = CrawlerProcess(settings)
    #    settings = get_project_settings()
    #    crawler = Crawler(settings)

    process.crawl(BookScraper)
    process.start()


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()

    connection = get_database_connection(arguments.password_file)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sys.database_principals ")
    for row in cursor.fetchall():
        print(row)

    string = "In stock (19 available)"
    splits = string.split('(')
    number_of_copies = int(''.join((filter(str.isdigit, string))))
    print(splits, " ", number_of_copies)


if __name__ == "__main__":
    main2()
