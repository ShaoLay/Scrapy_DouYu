# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):

    room_id = scrapy.Field()
    vertical_src = scrapy.Field()
    nickname = scrapy.Field()
    anchor_city = scrapy.Field()