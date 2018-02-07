# bilibili

![pyversions](https://img.shields.io/badge/python%20-3.6%2B-blue.svg)
![Travis](https://img.shields.io/travis/rust-lang/rust.svg)

## 介绍
从接口 http://space.bilibili.com/ajax/member/GetInfo 获取b站用户非隐私信息。post方法，post数据data = {'mid':mid,'csrf':'null'}，mid为用户id，从1开始递增。每隔1.5s访问请求不会被封IP。

## 返回数据格式

```
{
    "status": true,
    "data": {
        "mid": "1",
        "name": "bishi",
        "approve": false,
        "sex": "男",
        "rank": "10000",
        "face": "http://i0.hdslb.com/bfs/face/34c5b30a990c7ce4a809626d8153fa7895ec7b63.gif",
        "coins": 0,
        "DisplayRank": "1001",
        "regtime": 1245823614,
        "spacesta": 0,
        "place": "",
        "birthday": "0000-09-19",
        "sign": "",
        "description": "",
        "article": 0,
        "level_info": {
            "next_exp": 10800,
            "current_level": 4,
            "current_min": 4500,
            "current_exp": 6319
        },
        "pendant": {
            "pid": 0,
            "name": "",
            "image": "",
            "expire": 0
        },
        "nameplate": {
            "nid": 0,
            "name": "",
            "image": "",
            "image_small": "",
            "level": "",
            "condition": ""
        },
        "official_verify": {
            "type": -1,
            "desc": ""
        },
        "toutu": "bfs/space/768cc4fd97618cf589d23c2711a1d1a729f42235.png",
        "toutuId": 1,
        "theme": "default",
        "theme_preview": "",
        "im9_sign": "4f5abf0502acb53b58c344190153f40d",
        "playNum": 983549,
        "fans_badge": false
    }
}
```
