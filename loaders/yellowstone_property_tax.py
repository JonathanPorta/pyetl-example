from pyscraper_framework import Loader as Loader
from lib import S3Loader as S3Loader

class YellowstonePropertyTax(S3Loader):
    def __init__(self):
        super().__init__()
        print("YellowstonePropertyTaxLoader::init()")

    def execute(self, data, *args, **kwargs):
        print('='*94)
        print("YellowstonePropertyTaxLoader::execute()")
        print('='*94, 'args')
        print(*args)
        print('='*94, 'kwargs')
        print(**kwargs)
        print('='*94)
        print('FOR URL: ', data['url'])
        # TODO: Pass the bucket in as a config param
        self.upload(key=data['url'], value=data['data'], bucket='pyscraper-etl-test')
