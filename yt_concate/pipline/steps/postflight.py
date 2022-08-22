import os

from yt_concate.pipline.steps.step import Step
from yt_concate.settings import DOWNLOADS_DIR


class Postflight(Step):
    def process(self, data, inputs, utils):
        print("In postflight")
        if inputs['cleanup']:
            for file in os.walk(DOWNLOADS_DIR):
                print(file)
                # os.remove(file)
        