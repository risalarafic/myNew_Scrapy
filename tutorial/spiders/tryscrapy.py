# import scrapy
# import json
# import re
# import math

# class ProfileSpider(scrapy.Spider):
#     name = "profile"
#     current_page = 1

#     headers = {
#         #'Accept': 'application/json, text/javascript, /; q=0.01',
#         #'Accept-Encoding': 'gzip, deflate, br, zstd',
#         #'Accept-Language': 'en-US,en;q=0.9',
#         #'Connection': 'keep-alive',
#             'Cookie': 'subsiteID=318059; subsiteDirectory=; culture=en; ASP.NET_SessionId=g5ga33tjlzvuhaq3xjqugvtz; currencyAbbr=USD; currencyCulture=en-US; rnSessionID=176147961743124518; _gid=GA1.2.297314699.1726988153; _ga_Z938GKV5TZ=GS1.1.1726993164.2.1.1726993877.3.0.0; _ga=GA1.1.1863450144.1726988153; NSC_ESNS=99d9a815-d63a-16ef-9678-0050569dcf56_3437730026_4152340064_00000000011170205488',
#             'Host': 'www.bhhsamb.com',
#             'Referer': 'https://www.bhhsamb.com/roster/Agents',
#             'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#             'Sec-CH-UA-Mobile': '?0',
#             'Sec-CH-UA-Platform': '"macOS"',
#             'Sec-Fetch-Dest': 'empty',
#         #'Sec-Fetch-Mode': 'cors',
#         #'Sec-Fetch-Site': 'same-origin',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#             #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
#             'X-Requested-With': 'XMLHttpRequest'

#         }
#     #def start_requests(self):
#        # url = 'https://www.bhhsamb.com/CMS/CmsRoster/RosterSearchResults?layoutID=963&pageSize=10&pageNumber=1&sortBy=random'
#        # yield scrapy.Request(url, callback=self.parse)
#     def start_requests(self):
   
#         url = 'https://www.bhhsamb.com/CMS/CmsRoster/RosterSearchResults?layoutID=963&pageSize=10&pageNumber=1&sortBy=random'

#         yield scrapy.Request(url, headers= self.headers, callback=self.parse)
        
#     def parse(self, response):
#         #print(response.json()) 
#         print(type(response.json()))         #converting to pure json byb removing the ///rn
#         response_dict = json.loads(response.json()) #response in dictionary form have doubt response.json and response_dict are same
#         #print(response_dict)
#         print(type(response_dict))          #<class 'dict'>
#         html_content = response_dict.get('Html')
#         total_count = response_dict.get('TotalCount')
#         print(total_count)
#         #print(html_content)
        
        
#         selector = scrapy.Selector(text=html_content)
#         print(type(selector))
#         #print(selector)
#         #type of selector
#         # Extract all profile links
#         profile_links = selector.xpath('//a[contains(@class, "site-roster-card-image-link")]/@href').getall()
#         print("hiiiiiiii")
#         print(profile_links)
#         print(len(profile_links)) #number of links in each page (10)
#         page_size = len(profile_links)
#         # each profile page
#         for link in profile_links:
#             #print(link)
#             full_url = 'https://www.bhhsamb.com' + link  # Create the full URL 
#             yield scrapy.Request(full_url, callback=self.parse_profile)

#         no_pages = math.ceil(total_count / page_size)
#         print(page_size)
#         print(no_pages)
#         print("hiiiiii")
#         if current_page <= no_pages:   
#             current_page += 1           #need to increment the  current page
#             next_url = f'https://www.bhhsamb.com/CMS/CmsRoster/RosterSearchResults?layoutID=963&pageSize=10&pageNumber={current_page}&sortBy=random'
#             yield scrapy.Request(next_url, headers= self.headers, callback=self.parse)        
#             #current_page += 1
    
#     def parse_profile(self, response):
       
#         profile_name = response.xpath('//p[@class="rng-agent-profile-contact-name"]/text()').get().strip()
#         job_title = response.xpath('//span[@class="rng-agent-profile-contact-title"]/text()').get()
#         image_url = response.xpath('//img[@class="rng-agent-profile-photo"]/@src').get()
#         address = response.xpath('string(//li[@class="rng-agent-profile-contact-address"])').get().strip()
#         Address = re.sub(r'\s+', ' ', address)
#         #contact_details = response.xpath('//ul[@class="rng-agent-profile-contact"]/@href')
#         social_media_elements = response.xpath('//li[contains(@class, "social-")]')
#         social_media = {}
#         for element in social_media_elements:
#             key = element.xpath('a/@aria-label').get().strip()
#             value = element.xpath('a/@href').get().strip()
#             social_media[key] = value
#         offices = response.xpath('//div[@class="office"]/ul/li/text()').getall()
#         offices = [eoffice.strip() for office in offices]
#         phone_number = response.xpath('//a[contains(@href, "tel:")]/text()').getall()
#         languages = response.xpath('//div[@class="languages"]/ul/li/text()').getall()
#         languages = [lang.strip() for lang in languages]
#         description = response.xpath('//div[contains(@id, "body-text-")]/text()').get()


#         yield {
#             'profile_name': profile_name,
#             'job_title' : job_title,
#             'image_url' : image_url,
#             'address' : Address,
#             'social_media' : social_media,
#             'offices' : offices,
#             'languages' : languages,
#             'phone_number': phone_number,
#             'description' : description,
            
#         }
