from flask import Flask, jsonify, request
from myproject.myproject.spiders.myspider import MySpider
from scrapy.crawler import CrawlerRunner, CrawlerProcess
import subprocess
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def scrape_and_display():
    url = request.args.get("url")
    if url is None:
        return "There is no url, please enter a url to be parsed"

    # Get the current working directory because we will need to go back after the initial change
    curr_wd = os.getcwd()
    os.chdir("myproject/myproject")

    output_file = "output.xml"

    # Check to see if output file exists before
    # If it does we want to remove it before creating a new one, re-writing does not work
    if os.path.exists(output_file):
        os.remove(output_file)

    subprocess.check_output(['scrapy', 'crawl', "myspider", "-a", f"url={url}", "-o", output_file], text=True)
    # Extract the HTML data from the spider
    with open('output.xml', 'r', encoding='utf-8') as f:
        data = f.read()

    # Change back to original path so the initial change path doesnt cause an isse
    os.chdir(curr_wd)

    return data
   
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)