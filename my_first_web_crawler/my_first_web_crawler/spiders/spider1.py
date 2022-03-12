#imports
import scrapy

#Spider class
class QuotesSpider(scrapy.Spider):
    #name of your spider
    name = "blogs"

    def start_requests(self):
        #Website links to crawl
        urls = [
            'https://gourav-dhar.com',
            'https://gourav-dhar.com/profile',
        ]

        #loop through the urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, callback=self.downloadParsedFile)
        self.downloadParsedFile(response)

    def downloadParsedFile(self, response):
        page = response.url.split("/")[-2]
        filename = f'home-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)





