from pyetl_framework import Pipeline as Pipeline
from pyetl_framework import ETLJob as ETLJob

class YellowstoneOrion(Pipeline):
    def __init__(self, pipeline_manager, name, extractor_class, transformer_class, loader_class):
        print("YellowstoneOrionPipeline::init()")
        super().__init__(pipeline_manager, name, extractor_class, transformer_class, loader_class)

    def start(self, queue):
        print("YellowstoneOrionPipeline::start()",queue)
        super().start(queue)
        print("Init a new job")

        extractor = self.init_extractor(url='http://google.com')
        print("Made an extractor, son: ", extractor)

        transformer = self.init_transformer()
        print("Made an transformer, son: ", transformer)

        loader = self.init_loader()
        print("Made an loader, son: ", loader)

        job = ETLJob(extractor, transformer, loader)
        print("Made an etljob, son: ", job)

        queued_job = queue.enqueue_call(
            func=job.execute, result_ttl=5000
        )

        job_id = queued_job.get_id()
        print("Job was queued, bro", job_id)
