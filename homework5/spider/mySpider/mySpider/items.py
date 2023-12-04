import scrapy


class MyspiderItem(scrapy.Item):
    name = scrapy.Field()   # 讲师的名字
    price = scrapy.Field()  # 讲师的职称
