# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FbsproItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    addr = scrapy.Field()  # 地点

    price = scrapy.Field()  # 价格
    room = scrapy.Field()  # 厅室
    direc = scrapy.Field()  # 方向
    area = scrapy.Field()  # 面积
    agent = scrapy.Field()  # 经纪人

