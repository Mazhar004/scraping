import scrapy
from scrapy.http import FormRequest
#from scrapy.utils.response import open_in_browser

from ..items import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        csrf = response.xpath(
            '//input[@name="csrf_token"]').css('input::attr(value)').extract_first()
        username = 'abc@gmail.com'
        password = '1234'
        return FormRequest.from_response(response, formdata={
            'csrf_token': csrf,
            'username': username,
            'password': password
        }, callback=self.parse_item)

    def parse_item(self, response):
        # open_in_browser(response)
        all_quote = response.css('div.quote')
        item = QuotetutorialItem()
        for i in all_quote:
            quote = i.css('.text::text').extract_first()
            author = i.css('.author::text').extract_first()
            tags = i.css('.tag::text').extract()

            item['quote'] = quote.strip()
            item['author'] = author.strip()
            item['tags'] = tags

            yield item

        next_page = response.css('.next a::attr(href)').get()
        # next_page = response.xpath(
        #    '//li[@class="next"]//a[@href]').extract()

        if next_page:
            yield response.follow(next_page, callback=self.parse_item)
