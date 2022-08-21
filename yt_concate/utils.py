import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import OUTPUTS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def creat_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def get_caption_filepath(self, channel_id):
        return os.path.join(CAPTIONS_DIR, channel_id + '.txt')

    def get_outputs_filepath(self, channel_id, search_word):
        filename = f"{channel_id}_{search_word}.mp4"
        return os.path.join(OUTPUTS_DIR, filename)

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exist(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exist(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

