"""
items.py

This module defines the item classes for the Scrapy project.

Items are custom Python objects used to store the scraped data. They provide a
structured way to define the data fields the spider will extract from the webpage.
"""

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PricePulseScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass