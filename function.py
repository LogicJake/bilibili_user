# -*- coding: utf-8 -*-
'''
    将api数据转化成字典
'''
import json
from api import *

def function_get_info(mid):
    '''
        返回0代表ip被封
    :param mid:
    :return:
    '''
    data = {}
    res = get_info(mid)
    if res.find('status') == -1:
        return 0        #代表ip被封
    res = json.loads(res)
    if res['status']:
        json_data = res['data']
        data['mid'] = json_data['mid']
        data['name'] = json_data['name']
        if json_data['approve']:
            data['approve'] = 1
        else:
            data['approve'] = 0
        data['sex'] = json_data['sex']
        data['face'] = json_data['face']
        data['regtime'] = json_data.get('regtime',0)        #解决没有注册时间的问题
        data['place'] = json_data.get('place',0)
        data['birthday'] = json_data['birthday']
        data['sign'] = json_data['sign']
        data['current_level'] = json_data['level_info']['current_level']
        return data
    else:
        return None

