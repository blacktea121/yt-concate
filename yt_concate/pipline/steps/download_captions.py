from pytube import YouTube
from bs4 import BeautifulSoup
import os
import time

from .step import Step
from yt_concate.settings import CHANNEL_ID
from yt_concate.settings import DOWNLOADS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        # return data
        start = time.time()
        for yt_obj in data:
            url = yt_obj.url
            print(f"{url}, 數量: {data.index(yt_obj)+1}/{len(data)}")

            if utils.caption_file_exist(yt_obj.get_caption_filepath()):
                continue

            source = YouTube(url)
            yt_obj.language = str(source.captions).split('=')[-1][1:-3]
            print(yt_obj.language)
            self.write_language_to_txt(yt_obj)

            caption = self.get_support_lang_caption(source)
            if not caption:
                print("找不到支援字幕")
                continue

            xml = caption.xml_captions
            srt = self.xml2srt(xml)

            text_file = open(utils.get_caption_filepath(yt_obj.id), "w", encoding='utf-8')
            text_file.write(srt)
            text_file.close()
        end = time.time()
        print(end - start)
        return data

    def get_support_lang_caption(self, source):
        first_lang = 'zh-TW'
        second_lang = 'a.en'
        func_first = source.captions.get_by_language_code(first_lang)
        func_sec = source.captions.get_by_language_code(second_lang)
        first_try = self.try_download(func_first)

        if first_try is not None and first_try != "AttributeError":
            print(f"有{first_lang}")
            return self.try_download(func_first)
        elif first_try is None:
            return self.try_download(func_sec)

    def try_download(self, func):
        try:
            return func
        except AttributeError:
            print("AttributeError")
            return "AttributeError"

    def get_support_lang(self, language):
        return language.split('"')[-1]

    def write_language_to_txt(self, yt_obj):
        path = os.path.join(DOWNLOADS_DIR, CHANNEL_ID + "_support_lang.txt")
        with open(path, "a") as f:
            content = yt_obj.id + " : " + yt_obj.language + "\n"
            f.write(content)

    @staticmethod
    def xml2srt(text):
        soup = BeautifulSoup(text, "html.parser")  # 使用 BeautifulSoup 轉換 xml
        ps = soup.findAll('p')  # 取出所有 p tag 內容

        output = ''  # 輸出的內容
        num = 0  # 每段字幕編號
        for i, p in enumerate(ps):
            try:
                a = p['a']  # 如果是自動字幕，濾掉有 a 屬性的 p tag
            except:
                try:
                    num = num + 1  # 每段字幕編號加 1
                    text = p.text  # 取出每段文字
                    t = int(p['t'])  # 開始時間
                    d = int(p['d'])  # 持續時間

                    h, tm = divmod(t, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                    m, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                    s, ms = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                    t2 = t + d  # 根據持續時間，計算結束時間
                    if t2 > int(ps[i + 1]['t']): t2 = int(ps[i + 1]['t'])  # 如果時間算出來比下一段長，採用下一段的時間
                    h2, tm = divmod(t2, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                    m2, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                    s2, ms2 = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                    output = output + str(num) + '\n'  # 產生輸出的檔案，\n 表示換行
                    output = output + f'{h:02d}:{m:02d}:{s:02d},{ms:03d} --> {h2:02d}:{m2:02d}:{s2:02d},{ms2:03d}' + '\n'
                    output = output + text + '\n'
                    output = output + '\n'
                except:
                    pass

        return output
