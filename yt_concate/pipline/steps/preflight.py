from yt_concate.pipline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        utils.creat_dirs()
