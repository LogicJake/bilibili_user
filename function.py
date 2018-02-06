# -*- coding: utf-8 -*-
import json
import requests
def get_proxy():
    response = requests.get('')
    res = json.loads(response.text)
    if res['code'] == 0:
        try:
            ip = res['data']['IP']
            port = res['data']['PORT']
            proxy = {}
            proxy['http'] = ip+":"+port
            return proxy
        except Exception as e:
            return None

