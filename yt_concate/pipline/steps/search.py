from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs: dict, utils):
        search_word = inputs['search_word']
        print("搜尋字串: ", search_word)
        found = []

        for yt_obj in data:
            captions = yt_obj.captions
            if not captions:
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt_obj, time, caption)
                    found.append(f)
        # print(found)
        return found
