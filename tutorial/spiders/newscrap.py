import scrapy
import json

class ProfileSpider(scrapy.Spider):
    name = "profile_spider"
    current_page = 1

    
    #def start_requests(self):
        # Starting URL or API endpoint to make the AJAX request
       # url = 'https://www.bhhsamb.com/CMS/CmsRoster/RosterSearchResults?layoutID=963&pageSize=10&pageNumber=1&sortBy=random'
       # yield scrapy.Request(url, callback=self.parse)
    def start_requests(self):
   
        url = 'https://www.bhhsamb.com/CMS/CmsRoster/RosterSearchResults?layoutID=963&pageSize=10&pageNumber=1&sortBy=random'
    
    # headers
        headers = {
        #'Accept': 'application/json, text/javascript, /; q=0.01',
        #'Accept-Encoding': 'gzip, deflate, br, zstd',
        #'Accept-Language': 'en-US,en;q=0.9',
        #'Connection': 'keep-alive',
            'Cookie': 'subsiteID=318059; subsiteDirectory=; culture=en; ASP.NET_SessionId=g5ga33tjlzvuhaq3xjqugvtz; currencyAbbr=USD; currencyCulture=en-US; rnSessionID=176147961743124518; _gid=GA1.2.297314699.1726988153; _ga_Z938GKV5TZ=GS1.1.1726993164.2.1.1726993877.3.0.0; _ga=GA1.1.1863450144.1726988153; NSC_ESNS=99d9a815-d63a-16ef-9678-0050569dcf56_3437730026_4152340064_00000000011170205488',
            'Host': 'www.bhhsamb.com',
            'Referer': 'https://www.bhhsamb.com/roster/Agents',
            'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'Sec-CH-UA-Mobile': '?0',
            'Sec-CH-UA-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
        #'Sec-Fetch-Mode': 'cors',
        #'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        yield scrapy.Request(url, headers=headers, callback=self.parse)
        
    def parse(self, response):
        #print(response.json())
        print(type(response.json()))
        response_dict = json.loads(response.json())
        #print(response_dict)
        print(type(response.json()))
        html_content = response_dict.get('Html')
        total_count = response_dict.get('TotalCount')
        if cureentpage!= total_count:
            start_requests         #need to increment the  current page 
        print("hhhhhhhhhhh")
        print(total_count)
        #print(html_content)
        
        
        selector = scrapy.Selector(text=html_content)
        print("hiiiii")
        print(selector)
        
        # Extract all profile links
        profile_links = selector.xpath('//a[contains(@class, "site-roster-card-image-link")]/@href').getall()
        #print(profile_links)
        print(len(profile_links))

        # each profile page
        for link in profile_links:
            print(link)
            full_url = 'https://www.bhhsamb.com' + link  # Create the full URL 
            yield scrapy.Request(full_url, callback=self.parse_profile)
            
    
    def parse_profile(self, response):
       
        profile_name = response.xpath('//p[@class="rng-agent-profile-contact-name"]/text()').get()
        phone_number = response.xpath('//a[contains(@href, "tel:")]/text()').get()

        yield {
            'profile_name': profile_name,
            'phone_number': phone_number,
        }
