import scrapy
import json

class RealityScraper(scrapy.Spider):
    name = 'reality'
    allowed_domains = ["https://www.sreality.cz"]
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&locality_country_id=10001&per_page=500']

    def parse(self, response):
        jsonresponse = json.loads(response.body)
        items = {}
        all_flats = jsonresponse['_embedded']['estates']
        for flat in all_flats:
            key_name = flat['_links']['images'][0]['href']
            items[key_name] = flat['name']
        yield items

