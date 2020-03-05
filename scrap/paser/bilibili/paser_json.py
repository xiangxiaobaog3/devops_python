# -*- coding:utf-8 -*-

import sys
import os
import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrap.conf import setting

def get_json(aid):
    params = {
        'aid': aid
    }
    url = setting.API_URL
    try:
        response = requests.get(url=url, params=params, headers=setting.HEADERS)
        return response
    except:
        return '请求失败'
