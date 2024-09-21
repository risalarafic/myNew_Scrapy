import scrapy


class QuotesSpider(scrapy.Spider):
    name = "agents"

    def start_requests(self):
        url = "https://www.bhhsamb.com/bio/AmandaFoster" # link to individal profile of amanda

        yield scrapy.Request(url=url, callback=self.parse)
        

    def parse(self, response):
        for agent in response.xpath("//section[@class='rng-agent-profile bio1']"):
            address = agent.xpath('.//li[@class="rng-agent-profile-contact-address"]/strong/text() | .//li[@class="rng-agent-profile-contact-address"]/text()').getall()
            cleaned_address = ' '.join([text.strip() for text in address if text.strip()])
            yield {
                "name": agent.xpath('.//p[@class="rng-agent-profile-contact-name"]/text()').get().strip(), #extract name
                "Title": agent.xpath('.//span[@class="rng-agent-profile-contact-title"]/text()').get().strip(), #extract title
                "image": agent.xpath('.//img[@class="rng-agent-profile-photo"]/@src').get(), #extract image link
                "address": cleaned_address #extract contact address
                
            }
        next_page = response.xpath(".//li[@class='next']/a/@href").get()   #following links to next page
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)      #response.follow directly follow the link without the urljoin