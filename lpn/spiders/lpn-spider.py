import scrapy

class LogoAndPhoneNumbersSpider(scrapy.Spider):
	name = "logo-and-phone-numbers"
	
	with open('websites.txt', 'r') as websites:
		start_urls = []
		input_urls = [website.strip() for website in websites.readlines()]
		for input_url in input_urls:
			if not 'https://' in input_url:
				input_url = 'https://'+input_url
				start_urls.append(input_url)
			else:
				start_urls.append(input_url)
	
	def parse(self, response):
	
		logo = response.css('img::attr(src)').get()
		absolute_logo = response.urljoin(logo)
		
		phone_numbers = response.css('body').re(r'[(+]?\d[\s()/-]*\d[\s()/-]*\d[\s()/-]*\d[\s()/-]*\d[\s()/-]*\d[\s()/-]*'
												r'\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*'
												r'\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*\d*[\s()/-]*')
		cleaner_phone_numbers = list(dict.fromkeys([pn.replace("/", " ").replace("-", " ") for pn in phone_numbers]))
		
		yield {
			'logo': absolute_logo,
			'phones': cleaner_phone_numbers,
			'website': response.url
		}
