from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.steps.get_vedio_list import GetVideoList
from yt_concate.pipline.pipline import Pipline
from yt_concate.pipline.steps.download_captions import DownloadCaptions
from yt_concate.utils import Utils


CHANNEL_ID = 'UC4GZ1dNQKWWFDQ4IWl4DezA'

steps = [
    # GetVideoList(),
    DownloadCaptions(),
]


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    utils = Utils()
    p = Pipline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
