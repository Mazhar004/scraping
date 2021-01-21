# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import sys

root = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(root)
try:
    from dataset import Database as db
except:
    from dataset import Database as db


class AmazonPipeline:
    def __init__(self):
        self.db_obj = db('amazon_books.db')
        self.db_obj.create_table('books_data',
                                 {'Title': 'text',
                                  'Author': 'text',
                                  'Image': 'text',
                                  'Price': 'text'},
                                 exist_ok=False)

    def process_item(self, item, spider):
        self.db_obj.connection()
        string = 'insert into books_data values ("{}","{}","{}","{}")'.format(
            *item.values())
        self.db_obj.execute(string)
        self.db_obj.connection(status='commit')

        return item
