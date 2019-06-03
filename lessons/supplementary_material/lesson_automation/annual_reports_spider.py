import scrapy

class AnnualReportsSpider(scrapy.Spider):
    name = "annual_reports"
    # create a list of all the pages with alphabetical company names
    start_urls = ['http://www.annualreports.com/Companies?a={}'.format(letter) for letter in ['A']]

    def parse(self, response):
    	# get the url of the company specific webpage
        for company in response.css('#wrapper > section > table > tbody > tr > td > a::attr(href)').extract():
            if company is not None:
            	# go to each company page to extract the names of all the annual reports
                yield response.follow(company, self.parse_reports)

    def parse_reports(self, response):
    	# extract the company name 
        company_name = str(response.css('#wrapper > div.company-header.portal-header > h1::text')[0].extract())
        # collect all available annual reports
        reports = [report for report in response.css('#wrapper > div.venders-block > article > div.content-holder.content-archive > ul > li > div.text-holder > ul > li:nth-child(1)::text').extract()]
        yield {company_name:str(reports)}