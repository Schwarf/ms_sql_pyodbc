from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem


class BookScraper(CrawlSpider):
    name = "bookscraper"
    start_urls = ["http://books.toscrape.com"]

    rules = (Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
             Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse")
             )

    def parse(self, response):
        book_item = BookItem()
        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
        book_item["title"] = response.css(".col-sm-6.product_main > h1 ::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        availability_string = response.css(".table.table-striped > tr:nth-child(6) > td::text").get()
        splits = availability_string.split('(')
        stock_string = splits[0]
        in_stock = "In stock "
        number_of_copies = 0
        if stock_string==in_stock:
            number_of_copies = int(''.join((filter(str.isdigit, splits[1]))))
        book_item["availability"] = stock_string
        book_item['number_of_copies'] = number_of_copies
        book_item["url"] = response.url
        yield book_item
