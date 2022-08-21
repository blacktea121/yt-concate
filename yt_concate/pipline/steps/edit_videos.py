import os.path

from moviepy.editor import VideoFileClip, concatenate_videoclips

from .step import Step
from yt_concate.settings import OUTPUTS_DIR


class EditVideos(Step):
    def process(self, data, inputs: dict, utils):
        lst_clip = []
        for found in data:
            print(found.time)
            video_path = found.yt.video_filepath
            time_start, end_time = self.parse_video_time(found.time)

            video = VideoFileClip(video_path).subclip(time_start, end_time)
            lst_clip.append(video)
            if len(lst_clip) == inputs['limit']:
                break

        final_clip = concatenate_videoclips(lst_clip)
        output_video_filepath = utils.get_outputs_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_video_filepath)

    def parse_video_time(self, srt_time):
        return  srt_time.split(" --> ")
