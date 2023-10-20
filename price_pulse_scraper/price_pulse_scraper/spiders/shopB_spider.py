import scrapy


class ShopbSpiderSpider(scrapy.Spider):
    name = "shopB_spider"
    allowed_domains = ["www.idealo.fr"]
    start_urls = ["https://www.idealo.fr/prix/202069623/apple-iphone-14-pro-max.html"]

    def parse(self, response):
        pass
