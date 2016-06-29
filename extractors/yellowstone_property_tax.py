import time
from pyetl_framework import Extractor as Extractor
from lib import UrlExtractor as UrlExtractor

class YellowstonePropertyTax(UrlExtractor):
    def __init__(self, url):
        super().__init__()
        self.url = url

        print("YellowstonePropertyTaxExtractor::init()")
        print("url should be: ",url," it is:", self.url)

    def execute(self):
        print("YellowstonePropertyTaxExtractor::execute() for url: ", self.url)
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'
        }
        proxy = {
            'http'  : 'mtna.porta.codes'#,
            # 'https' : 'username:mypassword@77.75.105.165'
        }
        data = {'url': self.url, 'data': self.GET(self.url, headers=headers, proxy=proxy)}
        print('Got data back for ', data['url'])
        return data

        # # for testing
        # # # some simple caching while we test so we don't annoy anyone at the tax site. =)
        # with open('./tmp', encoding='utf-8') as f:
        #     d = f.read()
        # print('Sleeping for 2 seconds before continuing...')
        # time.sleep(2)
        # return {'url': self.url, 'data': d}
