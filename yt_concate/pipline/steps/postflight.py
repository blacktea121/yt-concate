import shutil, os

from yt_concate.pipline.steps.step import Step
from yt_concate.settings import DOWNLOADS_DIR


class Postflight(Step):
    def process(self, data, inputs, utils):
        print("In postflight")
        if inputs['cleanup']:
            print("開始刪除" + DOWNLOADS_DIR)
            shutil.rmtree(DOWNLOADS_DIR)
            print("已刪除" + DOWNLOADS_DIR)


if __name__ == '__main__':
    print("開始刪除" + DOWNLOADS_DIR)
    path = os.path.join("C:", os.sep, r"Users\USER\Desktop\yt-concate\yt_concate", DOWNLOADS_DIR)
    shutil.rmtree(path)
    print("已刪除" + DOWNLOADS_DIR)
