from scrapy.spiders import Spider

class TeslaSpider(Spider):
    name = "tesla"
    allowed_domains = ["www.tesla.com"]
    start_urls = [""]