import warnings

from yt_concate.settings import CHANNEL_ID
from yt_concate.utils import Utils
from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.pipline import Pipline
from yt_concate.pipline.steps.preflight import Preflight
from yt_concate.pipline.steps.get_vedio_list import GetVideoList
from yt_concate.pipline.steps.download_captions import DownloadCaptions
from yt_concate.pipline.steps.read_caption import ReadCaption
from yt_concate.pipline.steps.postflight import Postflight


warnings.filterwarnings("ignore")

steps = [
    Preflight(),
    GetVideoList(),
    DownloadCaptions(),
    ReadCaption(),
    Postflight(),
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
