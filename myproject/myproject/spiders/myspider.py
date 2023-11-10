import scrapy
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.loader import ItemLoader


class MySpider(scrapy.Spider):
    name = 'myspider'
    # start_urls = ['https://mortgagedeliveryguy.ca/join-us/']

    def start_requests(self):
        url = self.url
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        yield {
            "html_body": response.body.decode('utf-8')
        }
 
    
