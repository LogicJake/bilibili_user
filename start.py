from common import Global
from function import *
from save import *
import threading
import api
import time
import function
import json

start_mid = [70847, 70848, 70849, 70850]       #多线程起始mid值
proxy_fail_num = 5
data_len = 1                    #多少个data开始存储
single_num = 40*10               #本地爬取运行几个周期 ，每个周期1.5s左右
thread_num = 4                  #线程数

def function_get_info(mid,proxy=0):             #根据传进来来的代理进行api访问
    '''
    :param mid:
    :return:返回0代表ip被封，None查无此人
    '''
    data = {}
    if proxy == 0:      #不采用代理
        res = api.get_info(mid)
    else:
        res = api.get_info(mid,proxy)
    if res.find('status') == -1:
        return 0        #代表ip被封或代理失效
    res = json.loads(res)
    if res['status']:
        json_data = res['data']
        data['mid'] = json_data.get('mid',0)
        data['name'] = json_data['name']
        if json_data['approve']:
            data['approve'] = 1
        else:
            data['approve'] = 0
        data['sex'] = json_data['sex']
        data['face'] = json_data['face']
        data['regtime'] = json_data.get('regtime',0)        #解决没有注册时间的问题
        data['place'] = json_data.get('place','null')
        data['birthday'] = json_data.get('birthday','null')
        data['sign'] = json_data.get('sign','null')
        data['current_level'] = json_data['level_info']['current_level']
        data['tid'] = threading.current_thread().getName()
        return data
    else:
        return None

def get_info(i,step):
    data = []
    while(1):
        fail_num = -1  # 代理访问失败次数
        res = 0
        while res == 0:
            fail_num = fail_num+1
            if fail_num == proxy_fail_num:      #失败proxy_fail_num次就认为无有效代理退出此线程
                if data.__len__() != 0:     #退出前要写入数据
                    save_user_info(data)

                thread = threading.current_thread()
                print('[INFO] ' + thread.getName() + ' has finished his work due to having no invalid proxy. The current mid is {}'.format(i))
                start_mid[int(threading.current_thread().getName())] = i          #更新current_mid
                return
            proxy = function.get_proxy()
            if proxy != None:  # 代理获取正确
                res = function_get_info(i, proxy)
            else:
                fail_num = fail_num + 1
        if res != None:
            data.append(res)
        if data.__len__() == data_len:
            save_user_info(data)
            data.clear()
        i = i+step

def thread_get_info(start_mid,num):           #多线程获取
    '''
    :param start_mid: 起始为止，一个长度为num的列表
    :param num: 线程总数
    :return:
    '''
    try:
        threadpool = []
        for i in range(num):
            th = threading.Thread(target=get_info, args=(start_mid[i], num,), name= str(i))
            threadpool.append(th)
            print('[INFO] Start thread-get-info-' + str(i) + ' to get info')
            th.start()
        for th in threadpool:
            th.join()

    except Exception as e:
        print(e)

def single_get_info(start_mid,num):              #单线程本地ip获取
    data = []
    end_mid = start_mid+single_num*num
    while (start_mid < end_mid):
        res = function_get_info(start_mid)
        if res == 0:
            print(time.ctime() + "sleeping。。。。。。。")
            time.sleep(10 * 60)  # ip被封睡眠10min
        elif res != None:
            data.append(res)
        if data.__len__() == data_len:
            save_user_info(data)
            data.clear()
        start_mid = start_mid + num
        time.sleep(1.5)             #休眠防止被封


if __name__ =="__main__":
    Global.__init__()

    while True:
        thread_get_info(start_mid,thread_num)
        print('[INFO] Threading has finished!')
        print(start_mid)
        min_start_mid = min(start_mid)
        min_index = start_mid.index(min_start_mid)

        single_get_info(min_start_mid,thread_num)      #从最小值开始

        start_mid[min_index] = min_start_mid+single_num*thread_num

        print('[INFO] Start threading')
        print(start_mid)

