from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quote"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):     
        for quote in response.xpath(".//div[@class='quote']"):
            yield {
                "text": quote.xpath(".//span[@class='text']/text()").get(),     #extracting quotes
                "author": quote.xpath(".//small[@class='author']/text()").get(),        #extracting authors
                "tags": quote.xpath(".//div[@class='tags']//a[@class='tag']/text()").getall(),        #extracting tags
            }
        next_page = response.xpath(".//li[@class='next']/a/@href").get()   #following links to next page
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)      #response.follow directly follow the link without the urljoin