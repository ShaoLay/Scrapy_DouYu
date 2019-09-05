# -*- coding: utf-8 -*-
import json

import scrapy

from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=60&offset='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        print('我是第一步')
        data_list = json.loads(response.body.decode())['data']
        if not data_list:
            print('没有数据呀！')
            return
        for room_dict in data_list:
            item = DouyuItem()
            item['room_id'] = room_dict['room_id']
            item['vertical_src'] = room_dict['vertical_src']
            item['nickname'] = room_dict['nickname']
            item['anchor_city'] = room_dict['anchor_city']

            yield item
        self.offset += 60
        url = self.base_url + str(self.offset)
        yield scrapy.Request(url, callback=self.parse)

