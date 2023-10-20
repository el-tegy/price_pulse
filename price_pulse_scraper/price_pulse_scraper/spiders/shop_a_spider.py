"""
shop_a_spider.py

This module contains the spider definition for scraping data from Shop A.

The spider navigates through the product listings of Shop A, extracts details
like product name, price, description, and other relevant details, and stores
them for further processing or analysis.

Usage:
    scrapy crawl shop_a_spider

Attributes:
    name (str): Unique identifier for the spider.
    start_urls (list): List of URLs where the spider begins to crawl.

Methods:
    parse(response): Extracts and processes the data from the given webpage.
"""

import scrapy


class ShopaSpider(scrapy.Spider):
    """
    Spider to scrape product information from Shop A's website.

    This spider navigates through Shop A's product listings, extracts details
    like product name, price, and description, and stores them for further analysis.
    It also handles pagination and ensures that all relevant product pages are visited.

    Attributes:
        name (str): The name of the spider.
        allowed_domains (list): The domains this spider is allowed to crawl.
        start_urls (list): The list of URLs where the spider begins crawling.

    Methods:
        parse(self, response): Processes the response and extracts the required data.
    """

    name = "shopA_spider"
    allowed_domains = ["www.pixmania.com"]
    start_urls = ["https://www.pixmania.com/fr/fr/smartphones-iphone-14-pro-max.html"]
    custom_settings = {"FEED_URI": "../data/shopA.csv"}

    def parse(self, response):
        """
        This method is called to handle the response downloaded for each of the requests made.
        It parses the HTML response and extracts the links, series and prices of the products.
        It then transforms the extracted links to absolute links and the extracted prices to float.
        Finally, it yields a dictionary containing the link, series and price of each product.
        """
        links = response.css(".producttile::attr(href)").extract()
        # -max-256-go-argent-129973.html
        series = response.css(".reconditionne.order-2::text").extract()
        # 14 Pro Max 256 Go, Argent'
        prices = response.css(".producttile-price.price::text").extract()

        # transform extracted_links to absolute links in form of https://www.pixmania.com/fr/fr/
        # iphone-14-pro-max-256-go-argent-129973.html
        # and extracted_series to "iPhone 14 Pro Max 256 Go, Argent"
        # and extracted_prices to "1599,00" as float
        for i in len(links):
            links[i] = "https://www.pixmania.com" + links[i]
            series[i] = series[i].strip()
            prices[i] = float(prices[i].replace(",", ".").replace("€", ""))

        for item in zip(links, series, prices):
            scraped_info = {"link": item[0], "series": item[1], "price": item[2]}
            yield scraped_info
