import json

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem


class BookScraper(CrawlSpider):
    name = "bookscraper"
    start_urls = ["http://books.toscrape.com"]

    rules = (Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
             Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
             )

    def parse_book(self, response):
        book_item = BookItem()
        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
        book_item["title"] = response.css(".col-sm-6.product_main > h1 ::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["availability"] = response.css(".table.table-striped > tr:nth-child(6) > td::text").get()
        book_item["url"] = response.url
        data = []
        data.append(book_item)
        filename = "test_result.json"
        with open(filename, 'w') as json_file:
            json.dump(data, json_file,
                      indent=4,
                      separators=(',', ': '))


        return book_item
