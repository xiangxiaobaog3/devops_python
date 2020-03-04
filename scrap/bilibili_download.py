import requests
import subprocess

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

def get_json(aid):
    params = {
        'aid': aid
        # 'jsonp': 'jsonp'
    }
    # url = 'https://api.bilibili.com/x/player/pagelist?'
    url = 'https://api.bilibili.com/x/web-interface/view?'

    try:
        response = requests.get(url=url, params=params, headers=headers)
        data_json = response.json()['data']['pages']

        data_list = []
        for data in data_json:
            data_dict = {
                'cid': data['cid'],
                'page': data['page'],
                'part': data['part']
            }
            data_list.append(data_dict)
        return data_list
    except:
        return '请求失败'

def VideoUrl(aid):
    data_json = get_json(aid)
    video_url_list = []
    for page in data_json:
        video_header = 'https://www.bilibili.com/video/av'
        page = page['page']
        video_url = '{}{}{}{}'.format(video_header, aid, '?p=', page)
        video_url_list.append(video_url)
    return video_url_list

def you_get_video(aid):
    params = {
        'aid': aid
        # 'jsonp': 'jsonp'
    }
    # url = 'https://api.bilibili.com/x/player/pagelist?'
    url = 'https://api.bilibili.com/x/web-interface/view?'

    try:
        response = requests.get(url=url, params=params, headers=headers)
        class_name = response.json()['data']['title']
        for video_url in VideoUrl(aid):
            cmd = '/usr/local/bin/you-get'
            subprocess.call([cmd, '-o', class_name, video_url])
    except:
        print('请求失败')


            # print(down_print)



you_get_video(84457418)


# print(get_json(84457418))