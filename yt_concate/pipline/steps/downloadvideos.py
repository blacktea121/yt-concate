from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs: dict, utils):
        lst_yt = [found.yt for found in data]
        set_yt = set(lst_yt)
        print(len(set_yt))

        for yt in set_yt:
            url = yt.url
            if utils.video_file_exist(yt.video_filepath):
                print(f'video file is existing for {url}, skipping')
                continue

            print(f'downloading video from {url}')
            # YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + ".mp4")
            YouTube(url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id + ".mp4")

        return data
