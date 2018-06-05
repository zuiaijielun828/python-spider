import scrapy
from bs4 import BeautifulSoup

class Httpbin(scrapy.Spider):
	allowed_domains = ['httpbin.org']
	name='httpbin'
	start_urls=['http://httpbin.org/get']
	#start_urls=['http://localhost:8080/mbj/test/12']
	def parse(self,response):
		soup = BeautifulSoup(response.text,'lxml')
		self.logger.info('处理结果是:'+str(response.status))
		self.logger.info('收到结果为~~~~:'+soup.prettify())