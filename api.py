# -*- coding: utf-8 -*-
'''
    返回api得到的原始数据
'''
import requests

def get_info(mid,proxy=0):
    data = {'mid':mid,'csrf':'null'}
    header = {
        'Accept':'*/*',
        'Connection':'close',
        'Content-Length':'20',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'https://space.bilibili.com',
        'Origin':'https://space.bilibili.com'
    }
    try:
        if proxy == 0:
            response = requests.post('http://space.bilibili.com/ajax/member/GetInfo',headers=header,data=data,timeout=5)
        else:
            response = requests.post('http://space.bilibili.com/ajax/member/GetInfo', headers=header, data=data,proxies = proxy,timeout=10)
        response.close()
        return response.text
    except Exception as e:
        return "fail"