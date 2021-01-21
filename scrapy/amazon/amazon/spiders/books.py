import scrapy
from ..items import AmazonItem
from ..proxy_address import generate


class AmazonBooks(scrapy.Spider):
    generate('list.txt')

    name = 'amazon_books'
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1606643660&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0']
    page_number = 2

    def parse(self, response):
        items = AmazonItem()
        all_book_div = response.css('.s-result-item')
        for i in all_book_div:
            title = i.css('.a-color-base.a-text-normal::text').extract_first()
            author = ' '.join([i.strip() for i in i.css(
                '.sg-col-12-of-20 .sg-col-12-of-20 .a-size-base+ .a-size-base::text').extract()])
            field = [j.strip() for j in i.css(
                '.a-link-normal.a-text-bold::text').extract()]
            image = i.css('.s-image::attr(src)').extract_first()
            price = ['$'+j for j in ''.join(
                i.css('.a-price span span::text').extract()).split('$') if j.strip()]
            book_price = {}
            for m, n in zip(field, price):
                book_price[m] = n
            if title:
                items['title'] = title
                items['author'] = author
                items['image_link'] = image
                items['price'] = book_price
                yield items
        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page={}&fst=as%3Aoff&qid=1606651995&rnid=1250225011&ref=sr_pg_1'.format(
            AmazonBooks.page_number)
        if AmazonBooks.page_number < 76:
            AmazonBooks.page_number += 1
            yield response.follow(next_page, callback=self.parse, meta={'crawl_once': True})
