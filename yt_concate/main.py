from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.steps.get_vedio_list import GetVideoList
from yt_concate.pipline.pipline import Pipline

CHANNEL_ID = 'UC4GZ1dNQKWWFDQ4IWl4DezA'

steps = [
    GetVideoList(),
]
def main():
    inputs = {
        'channel_id': CHANNEL_ID,

    }

    p = Pipline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
