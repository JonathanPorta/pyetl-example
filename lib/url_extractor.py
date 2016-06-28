import requests
from pyetl_framework import Extractor

class UrlExtractor(Extractor):

    def GET(self, url, *args, **kwargs):
        r = requests.get(url, *args, **kwargs)
        print('=======================================================')
        print('response')
        print('=======================================================')
        print(r)
        return r.text
