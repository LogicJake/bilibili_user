# -*- coding: utf-8 -*-
from common import Global
import pymysql
import time

def save_user_info(datas):
    try:
        conn = pymysql.connect(host=Global.get_value('host'), user=Global.get_value('user'),
                               passwd=Global.get_value('password'), db=Global.get_value('dbname'),
                               port=Global.get_value('port'), charset='utf8',autocommit = True)
        cursor = conn.cursor()
        sql = "INSERT INTO usr_info(mid, name, approve,sex,face,regtime,place,birthday,sign) VALUES "
        for data in datas:
            sql  = sql+"({},'{}',{},'{}','{}',{},'{}','{}','{}'),".format(data['mid'],data['name'].replace("'","''"),data['approve'],data['sex'],data['face'],data['regtime'],data['place'],data['birthday'],data['sign'].replace("'","''"))
        sql = sql[:-1]
        cursor.execute(sql)
        cursor.close()
        conn.close()
    except Exception as e:
        print(sql)
        print(time.ctime()+e)