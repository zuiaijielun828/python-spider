# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
	collection ='products'
	image= scrapy.Field()
	price= scrapy.Field()
	title= scrapy.Field()
	shop= scrapy.Field()
