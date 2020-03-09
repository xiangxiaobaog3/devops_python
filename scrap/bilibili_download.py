# -*- coding:utf-8 -*-
import os
import sys
import subprocess

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrap.paser.bilibili.paser_data import PaserData
from scrap.conf import setting

def VideoUrl(aid):
    data_json = PaserData().many_data(aid)
    video_url_list = []

    for page in data_json:
        video_header = 'https://www.bilibili.com/video/av'
        page = page['page']
        video_url = '{}{}{}{}'.format(video_header, aid, '?p=', page)
        video_url_list.append(video_url)

    return video_url_list

def VideoName(aid):
    class_name = PaserData().one_data(aid)

    return class_name

if __name__ == '__main__':
    aid = 84457418

    for video_url in VideoUrl(aid):
        subprocess.call([setting.YOU_GET_CMD, '-o', VideoName(aid), video_url])