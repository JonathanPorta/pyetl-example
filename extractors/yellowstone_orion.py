from pyetl_framework import Extractor as Extractor
from lib import UrlExtractor as UrlExtractor

class YellowstoneOrion(UrlExtractor):
    def __init__(self, url):
        super().__init__()
        self.url = url

        print("YellowstoneOrionExtractor::init()")
        print("url should be: ",url," it is:",self.url)

    def execute(self):
        print("YellowstoneOrionExtractor::execute() for url: ", self.url)
        return self.GET(self.url)
