# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline

from Douyu.settings import IMAGES_STORE


class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 图片url
        image_url = item['vertical_src']
        # 发送请求
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 老的path
        old_path = IMAGES_STORE + [x['path'] for ok, x in results if ok ][0]
        # 新的  path + 拼接昵称
        new_path = IMAGES_STORE + item['nickname'] + '.jpg'
        # 3.替换
        os.rename(old_path, new_path)
        return item


class DouyuPipeline(object):
    def open_spider(self, spider):
        self.file = open('douyu.json', 'w')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item)) + '\n'
        self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()