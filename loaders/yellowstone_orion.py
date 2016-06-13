from pyetl_framework import Loader as Loader

class YellowstoneOrion(Loader):
    def __init__(self):
        super().__init__()
        print("YellowstoneOrionLoader::init()")

    def execute(self, data):
        print("YellowstoneOrionLoader::execute()")
        # super().execute()
