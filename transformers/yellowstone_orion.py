from pyetl_framework import Transformer as Transformer

class YellowstoneOrion(Transformer):
    def __init__(self):
        super().__init__()
        print("YellowstoneOrionTransformer::init()")

    def execute(self, data):
        print("YellowstoneOrionTransformer::execute()")
        # super().execute()
