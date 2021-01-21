import scrapy


class AmazonItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    image_link = scrapy.Field()
    price = scrapy.Field()
