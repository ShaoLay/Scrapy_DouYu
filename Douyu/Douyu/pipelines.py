# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DouyuPipeline(object):
    def open_spider(self, spider):
        self.file = open('douyu.json', 'w')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item)) + '\n'
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()