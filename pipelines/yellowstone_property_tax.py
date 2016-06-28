from pyetl_framework import Pipeline as Pipeline
from bs4 import BeautifulSoup
import requests, re

class YellowstonePropertyTax(Pipeline):

    def url(self, page=1, page_size=10):
        # URL is longer by default, but it appears unnecessary to add all of these empty valued query params.
        # http://www.co.yellowstone.mt.gov/gis/csacond.asp?whichpage=1&pagesize=1000&Tax_ID=&OwnerName=&Post_dir=&Str_Num=&Pre_dir=&Street_Addr=&Blk=&St_type=&Cert=&Subd=&Lot=&Geo_code=&B1=Submit
        return "http://google.com"
        return "http://www.co.yellowstone.mt.gov/gis/csacond.asp?whichpage={}&pagesize={}".format(page, page_size)

    def __init__(self, *args, limit=1, **kwargs):
        super().__init__(*args, **kwargs)
        print("YellowstonePropertyTax::init()")

        # We ignore the page limit if it's less than 1.
        self.limit = limit

        # Set some defaults
        self.record_count = 0
        self.page_count = 0

    def start(self, queue):
        super().start(queue)
        print("YellowstonePropertyTax::start()", queue)

        e = self.init_extractor(self.url(page=1))
        queued_job = queue.enqueue_call(
            func=e.execute, result_ttl=5000
        )
        print('==========STARTER JOB QUEUED===========')

        # self.results = self.GET(self.url(page=1))
        # self.generate_counts()
        #
        # if self.limit > 0:
        #     self.limit = min(self.page_count, self.limit)
        # else:
        #     self.limit = self.page_count
        #
        #
        # for page in range(1, self.limit+1):
        #     url = self.url(page=page)
        #     print("URL for page #{}: {}".format(page, url))
        #     extractor = self.init_extractor(url)
        #     job = self.init_etl_job(extractor=extractor)
        #     print("JOB: ", job)
        #     queued_job = queue.enqueue_call(
        #         func=job.execute, result_ttl=5000
        #     )
        #
        #     job_id = queued_job.get_id()
        #     print("Job was queued, bro", job_id)

    def generate_counts(self):
        regex = re.compile("Page 1 of ([0-9]+) from ([0-9]+) total records")
        soup = BeautifulSoup(self.results, 'html.parser')
        matches = soup.find_all(string=regex, limit=1)[0].strip()
        self.record_count = int(regex.match(matches).group(2).strip())
        self.page_count = int(regex.match(matches).group(1).strip())
        print("Total: {}, Pages: {}".format(self.record_count, self.page_count))

    def GET(self, url, *args, **kwargs):
        # We already have an extractor for URLs, why not use it here as well?
        e = self.init_extractor(url)
        r = e.execute()
        return r['data']
