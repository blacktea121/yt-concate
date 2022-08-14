import os
from pprint import pprint

from yt_concate.pipline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    """讀取字幕檔的時間跟字幕放入字典中
    從captions資料夾逐一讀取字幕檔，將時間跟字幕放入字典。
    再把小字典放入以id當作key的字典中
    """
    def process(self, data, inputs: dict, utils):
        caption_files = os.listdir(CAPTIONS_DIR)
        dict_key_by_filename = {}

        for caption_file in caption_files:
            dict_caption_taxi = {}
            caption_file_path = os.path.join(CAPTIONS_DIR, caption_file)

            with open(caption_file_path, "r", encoding='utf-8') as f:
                lines = f.readlines()
                tf_time = False

                for line in lines:
                    if "-->" in  line:
                        caption_time = line
                        tf_time = True
                        continue
                    if tf_time:
                        caption_line = line
                        dict_caption_taxi[caption_line] = caption_time
                        tf_time = False
            dict_key_by_filename[caption_file] = dict_caption_taxi
        pprint(dict_key_by_filename)
        print("字典title: ", dict_key_by_filename.keys())
        return dict_key_by_filename
