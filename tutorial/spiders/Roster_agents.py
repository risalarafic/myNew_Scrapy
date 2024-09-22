import scrapy

class RealtorSpider(scrapy.Spider):
    name = "realtors"
    start_urls = [
        'https://www.bhhsamb.com/roster/Agents'  
    ]

    def parse(self, response):
        
        profile_links = response.xpath('//a[contains(@class, "site-roster-card-image-link")]/@href').extract()
        
        for link in profile_links:
            profile_url = response.urljoin(link)
            yield scrapy.Request(profile_url, callback=self.parse_profile)

    def parse_profile(self, response):
        name = response.xpath('//h2/text()').get()
        title = response.xpath('//div[contains(@class, "site-roster-card-content-title")]/span/text()').get()
        phone = response.xpath('//li/a[contains(@title, "(Call using Call-From-Browser)")]/text()').get()
        email = response.xpath('//li/a[contains(@href, "Contact")]/@href').get()
        website = response.xpath('//li/a[contains(@href, "bhhsamb.com")]/@href').get()
        location = response.xpath('//li[not(a)]/text()').get()

        yield {
            'name': name,
            'title': title,
            'phone': phone,
            'email': email,
            'website': website,
            'location': location,
        }
