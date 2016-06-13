from pyetl_framework import Transformer as Transformer

class YellowstonePropertyTax(Transformer):
    def __init__(self):
        super().__init__()
        print("YellowstonePropertyTaxTransformer::init()")

    def execute(self, data):
        print("YellowstonePropertyTaxTransformer::execute()")
        print('Data for', data['url'])
        return data
