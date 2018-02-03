# -*- coding: utf-8 -*-
'''
    将api数据转化成字典
'''
import json
from api import *

def function_get_info(mid):
    data = {}
    json_data = json.loads(get_info(mid))['data']
    data['mid'] = json_data['mid']
    data['name'] = json_data['name']
    if json_data['approve']:
        data['approve'] = 1
    else:
        data['approve'] = 0
    data['sex'] = json_data['sex']
    data['face'] = json_data['face']
    data['regtime'] = json_data['regtime']
    data['place'] = json_data['place']
    data['birthday'] = json_data['birthday']
    data['sign'] = json_data['sign']
    data['current_level'] = json_data['level_info']['current_level']
    return data