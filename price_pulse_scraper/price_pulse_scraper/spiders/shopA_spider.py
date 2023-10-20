import scrapy


class ShopaSpiderSpider(scrapy.Spider):
    name = "shopA_spider"
    allowed_domains = ["www.pixmania.com"]
    start_urls = ["https://www.pixmania.com/fr/fr/smartphones-iphone-14-pro-max.html"]

    def parse(self, response):
        pass
