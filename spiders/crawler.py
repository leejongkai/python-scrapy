import scrapy
from bs4 import BeautifulSoup
from apple.items import AppleItem
from scrapy.spiders import CrawlSpider ,Rule
from scrapy.linkextractors import LinkExtractor
#spider
class AppleCrawler(CrawlSpider):
	name = 'apple'
	start_urls = ['https://tw.news.appledaily.com/international/realtime']	
	rules = [
		Rule(LinkExtractor(allow=('/international/realtime/[1-2]$')), callback='parse_list', follow=True)
	]
	def parse_list(self, response):
		domain = 'https://tw.appledaily.com/'
		res = BeautifulSoup(response.body, 'lxml')
		for news in res.select('.rtddt'):
			#print domain + news.select('a')[0]['href']
			yield scrapy.Request(domain+news.select('a')[0]['href'], self.parse_detail)
	def parse_detail(self, response):
		res = BeautifulSoup(response.body, 'lxml')
		appleitem = AppleItem()
		appleitem['title'] = res.select('h1')[0].text
		appleitem['content'] = res.select('.ndArticle_margin p')[0].text
		appleitem['time'] = res.select('.ndArticle_creat')[0].text
		return appleitem
##scrapy crawl apple -o apple.json -t json

# class AppleCrawler(scrapy.Spider):
# 	name = 'apple'
# 	start_urls = ['http://www.appledaily.com.tw/realtimenews/section/new/']
# 	def parse(self,response):
# 		res = BeautifulSoup(response.body)
# 		for news in res.select('.rtddt'):
# 			print news.select('h1')[0].text
##scrapy crawl apple
