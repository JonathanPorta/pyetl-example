import time
from pyscraper_framework import Extractor as Extractor
from lib import UrlExtractor as UrlExtractor

class YellowstonePropertyTax(UrlExtractor):
    def __init__(self, url):
        super().__init__()
        self.url = url

        print("YellowstonePropertyTaxExtractor::init()")
        print("url should be: ",url," it is:", self.url)

    def execute(self):
        print("YellowstonePropertyTaxExtractor::execute() for url: ", self.url)
        return {'url': self.url, 'data': self.GET(self.url)}

        # # for testing
        # # # some simple caching while we test so we don't annoy anyone at the tax site. =)
        # with open('./tmp', encoding='utf-8') as f:
        #     d = f.read()
        # print('Sleeping for 2 seconds before continuing...')
        # time.sleep(2)
        # return {'url': self.url, 'data': d}