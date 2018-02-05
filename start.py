from common import Global
from function import *
from save import *
import threading
import api
import time
import function

def thread_get_info(num):
    try:
        threadpool = []
        for i in range(num):
            th = threading.Thread(target=get_info, args=(i + 1, num,), name='thread-get-info' + str(i))
            threadpool.append(th)
            print('[INFO] Start thread-test-ip-' + str(i) + ' to test proxy')
            th.start()
        for th in threadpool:
            threading.Thread.join(th)
    except Exception as e:
        print(e)

def get_info(i,step):
    while(1):
        data = []
        print(i)
        res = function_get_info(i)
        if res == 0:
            #换ip
            pass
        elif res != None:
            data.append(res)
        if data.__len__()!=0:
            save_user_info(data)
        i = i+step
        time.sleep(1)

Global.__init__()
i = 22975
while(1):
    data = []
    res = function_get_info(i)
    if res == 0:
        print(time.ctime()+"sleeping。。。。。。。")
        time.sleep(10*60)       #ip被封睡眠10min
    elif res != None:
        data.append(res)
    if data.__len__() != 0:
        save_user_info(data)
    i = i + 1
    time.sleep(1.5)