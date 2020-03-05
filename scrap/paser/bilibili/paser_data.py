# -*- coding:utf-8 -*-

from scrap.paser.bilibili.paser_json import get_json

class PaserData():

    def many_data(self, aid):
        data_json = get_json(aid).json()['data']['pages']

        data_list = []
        for data in data_json:
            data_dict = {
                'cid': data['cid'],
                'page': data['page'],
                'part': data['part']
            }
            data_list.append(data_dict)

        return data_list

    def one_data(self, aid):
        class_name = get_json(aid).json()['data']['title']

        return class_name