# -*- coding: utf-8 -*-
'''
    返回api的原始数据
'''
import requests

def get_info(mid):
    data = {'mid':mid,'csrf':'null'}
    header = {
        'Accept':'*/*',
        'Connection':'keep-alive',
        'Content-Length':'20',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'https://space.bilibili.com',
        'Origin':'https://space.bilibili.com'
    }
    response = requests.post('https://space.bilibili.com/ajax/member/GetInfo',headers=header,data=data)
    return response.content.decode('unicode-escape')