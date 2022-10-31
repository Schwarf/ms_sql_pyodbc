from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TeslaCrawler(CrawlSpider):
    name = 'tesla'
    allowed_domains = ['www.tesla.com']
    start_urls = ['https://www.tesla.com/']
    rules = (Rule(LinkExtractor()),)
