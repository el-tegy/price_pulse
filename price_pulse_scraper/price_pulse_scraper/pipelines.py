"""
pipelines.py

This module defines the item pipelines for the Scrapy project.

Pipelines are classes that process and handle the data returned by the spider.
Each defined pipeline processes the scraped item and performs actions like cleaning,
validation, and data storage (e.g., saving to a database or writing to a file).
"""

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PricePulseScraperPipeline:
    def process_item(self, item, spider):
        return item
