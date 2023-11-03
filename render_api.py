from flask import Flask, jsonify, request
from myproject.myproject.spiders.myspider import MySpider
from scrapy.crawler import CrawlerRunner, CrawlerProcess
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def scrape_and_display():
    url = request.args.get("url")
    os.chdir("myproject/myproject")
    subprocess.check_output(['scrapy', 'crawl', "myspider", "-a", f"url={url}", "-o", "output.xml"])
    # Extract the HTML data from the spider
    with open('output.xml', 'r', encoding='utf-8') as f:
        data = f.read()

    return data


if __name__ == '__main__':
    app.run()
