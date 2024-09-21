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
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),     #extracting quotes
                "author": quote.css("small.author::text").get(),        #extracting authors
                "tags": quote.css("div.tags a.tag::text").getall(),        #extracting tags
            }
        next_page = response.css("li.next a::attr(href)").get()   #following links to next page
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)      #response.follow directly follow the link without the urljoin