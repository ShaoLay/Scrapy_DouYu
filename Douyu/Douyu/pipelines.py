# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 图片url
        image_url = item['vertical_src']
        # 发送请求
        yield scrapy.Request(image_url)


class DouyuPipeline(object):
    def open_spider(self, spider):
        self.file = open('douyu.json', 'w')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item)) + '\n'
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()