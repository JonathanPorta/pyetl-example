import requests, tinys3, urllib
from pyscraper_framework import Loader
from io import BytesIO, StringIO

class S3Loader(Loader):
    def upload(self, key, value, bucket):
        key_encoded = urllib.parse.quote_plus(key)
        print('key_encoded', key_encoded)
        print('bucket', bucket)
        value = StringIO(value)
        value_encoded = BytesIO(value.getvalue().encode('utf-8'))

        connection = tinys3.Connection(os.environ['S3_ACCESS_ID'], os.environ['S3_SECRET_KEY'], tls=True)
        connection.upload(key_encoded, value_encoded, bucket, public=True)
