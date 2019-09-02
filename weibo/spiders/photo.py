# -*- coding: utf-8 -*-
import scrapy


class PhotoSpider(scrapy.Spider):
    name = 'photo'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']

    def parse(self, response):
        pass
