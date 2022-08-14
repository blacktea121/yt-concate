from .step import Step
from yt_concate.model.yt_class import YT


class InitializeYT(Step):
    def process(self, data, inputs: dict, utils):
        return [YT(url) for url in data]
