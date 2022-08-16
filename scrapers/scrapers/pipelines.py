# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2


class ScrapersPipeline:
    def __init__(self):
        
        self.connection = psycopg2.connect(
            host="postgres",
            user="postgres",
            password="heslo123",
            dbname="postgres",
            port="5432",
        )
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        rows = zip(item.values(), item.keys())
        self.cur.execute("SELECT count(*) FROM public.flats")
        number_of_items_in_db = self.cur.fetchone()
        if 0 == number_of_items_in_db[0] < 500:
            for row in rows:
                self.cur.execute("SELECT * FROM public.flats WHERE links = %s", (row[1],))
                result = self.cur.fetchone()
                if result is None:
                    self.cur.execute(
                        """ INSERT into public.flats (title, links) values (%s,%s)""", (row)
                    )
            self.connection.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
