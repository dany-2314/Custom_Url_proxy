import scrapy
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.loader import ItemLoader


class MySpider(scrapy.Spider):
    name = 'myspider'
    # start_urls = ['https://mortgagedeliveryguy.ca/join-us/']

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]

    def parse(self, response):
        yield {
            "html_body": response.body.decode('utf-8')
        }
 
    
# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })

# process.crawl(MySpider)
# process.start()