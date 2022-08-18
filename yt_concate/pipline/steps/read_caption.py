from pprint import pprint

from yt_concate.pipline.steps.step import Step


class ReadCaption(Step):
    """讀取字幕檔的時間跟字幕放入字典中
    從captions資料夾逐一讀取字幕檔，將時間跟字幕放入字典。
    再把小字典放入以id當作key的字典中
    """
    def process(self, data, inputs: dict, utils):
        for yt_obj in data:
            caption_file_path = yt_obj.get_caption_filepath()
            dict_caption_taxi = {}

            if not utils.caption_file_exist(caption_file_path):
                continue

            with open(caption_file_path, "r", encoding='utf-8') as f:
                lines = f.readlines()
                tf_time = False
                for line in lines:
                    if "-->" in line:
                        caption_time = line
                        tf_time = True
                        continue
                    if tf_time:
                        caption_line = line
                        dict_caption_taxi[caption_line] = caption_time
                        tf_time = False

            yt_obj.captions = dict_caption_taxi
            # pprint(yt_obj.caption)
        # print("title: ", [yt_obj.id for yt_obj in data])
        return data

