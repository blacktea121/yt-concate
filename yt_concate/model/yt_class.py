import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR

"""
helper class:協助儲存資料的class
"""


class YT:
    def __init__(self, url):
        self.id = self.get_video_id_from_url(url)
        self.url = url
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_list_filepath()
        self.captions = None

    @ staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + ".txt")

    def get_video_list_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return '<YT_obj>'

    def __repr__(self):
        content = "|".join([
            'id=' + str(self.id),
            'url' + str(self.url),
        ])
        return f'<Found ( {content} ) >'
