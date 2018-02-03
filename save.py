# -*- coding: utf-8 -*-
from common import Global
def save_user_info():
    try:
        conn = pymysql.connect(host=Global.get_value('host'), user=Global.get_value('user'),
                               passwd=Global.get_value('password'), db=Global.get_value('dbname'),
                               port=Global.get_value('port'), charset='utf8')
        cursor = conn.cursor()
        for ip in validIp:
            sql = "INSERT INTO origin(IP, PORT, UPDATE_TIME) VALUES ('{}',{},unix_timestamp())".format(ip['ip'],
                                                                                                       ip['port'])
            cursor.execute(sql)
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
        print("[ERROR] Failed to save proxy data")