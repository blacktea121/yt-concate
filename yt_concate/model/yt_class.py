import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import CAPTIONS_DIR

"""
helper class:協助儲存資料的class
"""


class YT:
    def __init__(self, url):
        self.id = self.get_video_id_from_url(url)
        self.url = url
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_list_filepath()

    @ staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + ".txt")

    def get_video_list_filepath(self):
        return os.path.join(DOWNLOADS_DIR, self.id + '.txt')
