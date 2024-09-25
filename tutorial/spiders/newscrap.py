import scrapy
import json
import re
import math

class ProfileSpider(scrapy.Spider):
    name = "profile_spider"
    base_url = "https://www.bhhsamb.com/CMS/CmsRoster/RosterSearchResults?layoutID=963&pageSize=40&pageNumber={}&sortBy=random"
    current_page = 1
    profiles = 0
    

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
            #'Sec-Fetch-Dest': 'empty',
        #'Sec-Fetch-Mode': 'cors',
        #'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
            'X-Requested-With': 'XMLHttpRequest'
    }

    def start_requests(self):
        url = self.base_url.format(self.current_page)
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response): 
        #converting to pure json by removing the ///rn
        response_dict = json.loads(response.json()) #response in dictionary form have doubt response.json and response_dict are same
        html_content = response_dict.get('Html')
        total_count = response_dict.get('TotalCount')
        print(total_count)

        selector = scrapy.Selector(text=html_content)
        profile_links = selector.xpath('//a[contains(@class, "site-roster-card-image-link")]/@href').getall()   # Extract all profile links

        numoflinksineachpage = 0
        for link in profile_links:
            print(link)
            full_url = 'https://www.bhhsamb.com' + link  # Create the full URL 
            yield scrapy.Request(full_url, callback=self.parse_profile)
            numoflinksineachpage +=1

        if(numoflinksineachpage != 40 ):
            print("not 40")

        print("number of profile in this page = ",numoflinksineachpage)
        no_pages = math.ceil(total_count / 40)
        no_pages = 3
        
        if self.current_page <= no_pages:   
            self.current_page +=1
            next_url = self.base_url.format(self.current_page)
            print("current page is  "+ str(self.current_page))
            print(next_url) #url to next page
            yield scrapy.Request(url=next_url, callback=self.parse,headers=self.headers) 
                 
    def parse_profile(self, response):
        self.profiles +=1
        print("no of calls to parse",self.profiles)  #calling parsse_profile function
        profile_name = response.xpath('//p[@class="rng-agent-profile-contact-name"]/text()').get().strip()          #name
        job_title = response.xpath('//span[@class="rng-agent-profile-contact-title"]/text()').get()                 #title
        image_url = response.xpath('//img[@class="rng-agent-profile-photo"]/@src').get()                            #image url
        address = response.xpath('string(//li[@class="rng-agent-profile-contact-address"])').get().strip()
        Address = re.sub(r'\s+', ' ', address)                                                                      #Address
        tel = response.xpath('//li[@class="rng-agent-profile-contact-phone"]/a/text()').get()
        contact_dict = {                                                                                            #dictionary of contact details
            "office" : "null",
            "Cell" : tel,
            "Fax" : "null"
        }

        social_media_elements = response.xpath('//li[contains(@class, "social-")]')
        social_media_dict = {}
        for element in social_media_elements:
            key = element.xpath('a/@aria-label').get().strip()
            value = element.xpath('a/@href').get().strip()
            social_media_dict[key] = value                                                     # dictionary of social acounts

        offices = response.xpath('//div[@class="office"]/ul/li/text()').getall()
        offices_list = [office.strip() for office in offices]                                  #list of offices
        languages = response.xpath('//div[@class="languages"]/ul/li/text()').getall()
        languages_list = [lang.strip() for lang in languages]                                  #list of languages
        description = response.xpath('//div[contains(@id, "body-text-")]/text()').get()        #description

        print("no of calls to parse",self.profiles)               #calling parsse_profile function
        yield {
            'profile_name': profile_name,
            'job_title' : job_title,
            'image_url' : image_url,
            'address' : Address,   
            'Contact_details' : contact_dict,       
            'social_media' : social_media_dict,
            'offices' : offices_list,
            'languages' : languages_list,
            'description' : description,
            
        }
         
