"""
shop_b.py

This module contains the spider definition for scraping data from Shop B.

The spider navigates through the product listings of Shop B, extracts details
like product name, price, description, and other relevant details, and stores
them for further processing or analysis.

Usage:
    scrapy crawl shop_b

Attributes:
    name (str): Unique identifier for the spider.
    start_urls (list): List of URLs where the spider begins to crawl.

Methods:
    parse(response): Extracts and processes the data from the given webpage.
"""

import scrapy


class ShopBSpider(scrapy.Spider):
    """
    Spider to scrape product information from Shop B's website.

    This spider navigates through Shop B's product listings, extracts details
    like product name, price, and description, and stores them for further analysis.
    It also handles pagination and ensures that all relevant product pages are visited.

    Attributes:
        name (str): The name of the spider.
        allowed_domains (list): The domains this spider is allowed to crawl.
        start_urls (list): The list of URLs where the spider begins crawling.

    Methods:
        parse(self, response): Processes the response and extracts the required data.
    """

    name = "shop_b"
    allowed_domains = ["www.idealo.fr"]
    start_urls = ["https://www.idealo.fr/prix/202069623/apple-iphone-14-pro-max.html"]
    custom_settings = {"FEED_URI": "./data/shopB.csv"}

    def parse(self, response):
        """
        This method is called to handle the response downloaded for each of the requests made.
        It parses the HTML response and extracts the links, series and prices of the products.
        It then transforms the extracted links to absolute links and the extracted prices to float.
        Finally, it yields a dictionary containing the link, series and price of each product.
        """
        links = response.css(".productVariants-listItemWrapper::attr(href)").extract()
        # '/prix/202093781/apple-iphone-14-pro-max-128-go-noir-sideral.html'
        series = response.css(
            ".productVariants-listItemWrapperImage::attr(alt)"
        ).extract()
        # Apple iPhone 14 Pro Max 128 Go noir sidéral
        prices_1 = response.css(".price > span:nth-child(2)::text").extract()
        # '1\u202f165,'
        prices_2 = response.css(".price .priceSup::text").extract()
        # '\xa050'
        full_price = []
        # transform links to absolute links in form of https://www.idealo.fr/prix/
        # 202093781/apple-iphone-14-pro-max-128-go-noir-sideral.html
        # and prices_1 and prices_2 into  full_price like "1165,50" as float
        for i, link in enumerate(links):
            links[i] = "https://www.idealo.fr" + link
            prices_1[i] = prices_1[i].replace("\u202f", "").replace(",", "")
            prices_2[i] = prices_2[i].replace("\xa0", ".").replace(",", ".")
            full_price.append(float(prices_1[i] + prices_2[i]))

        for item in zip(links, series, full_price):
            scraped_info = {"link": item[0], "series": item[1], "price": item[2]}
            yield scraped_info
