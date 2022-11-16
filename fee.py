# coding:utf-8
import requests
import random
import json
from datetime import datetime
import time
from datetime import timedelta
from datetime import timezone
from dateutil.parser import parse
from bs4 import BeautifulSoup
import sys

def generateNewID():
    characters = '0123456789ABCDEF'
    session_id = ''
    # E0FC7ADDD8796D1FC8D3DD9343BD5485
    for i in range(32):
        ch = random.choice(characters)
        session_id += ch
    return session_id

def query(host, meteraddr):
    try:
        utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
        beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
        beijing_cur = utc_now.astimezone(SHA_TZ)
        # print(beijing_cur.strftime("%Y-%m-%d %H:%M:%S.%f"))
        cookies = {
            'JSESSIONID': generateNewID(),
        }
        headers = {
            'Host': host,
            'Accept': 'text/plain, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-cn',
            'Origin': 'http://' + host,
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d34) NetType/4G Language/zh_CN',
            'Referer': 'http://' + host + '/WxPay/',
        }
        data = {
            'meteraddr': meteraddr,
        }
        response = requests.post('http://' + host + '/WxPay/pay/search', cookies=cookies, headers=headers, data=data)
        res = response.json()
        print(beijing_cur.strftime("%Y-%m-%d %H:%M:%S.%f"), res["data"]['remainmoney'])
        return res["data"]['remainmoney']
    except:
        pass

SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)

def qryHis(host, meteraddr):
    dict = {}
    try:
        utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
        beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
        beijing_cur = utc_now.astimezone(SHA_TZ)
        # print(beijing_cur.strftime("%Y-%m-%d %H:%M:%S.%f"))
        cookies = {
            'JSESSIONID': generateNewID(),
        }
        headers = {
            'Host': host,
            'Accept': 'text/plain, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-cn',
            'Origin': 'http://' + host,
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d34) NetType/4G Language/zh_CN',
            'Referer': 'http://' + host + '/WxPay/',
        }
        data = {
            'meteraddr': meteraddr,
        }
        response = requests.post('http://' + host + '/WxPay/record/torecord', cookies=cookies, headers=headers, params=data)

        resp = response.text
        soup = BeautifulSoup(resp, "lxml")
        tab = soup.find('table')
        print("----------------------------------")
        today = utc_now
        for tr in tab.findAll('tr')[1:]:
            tore_time = parse(tr.findAll('td')[0].getText().strip())
            tore_hour = tore_time.hour
            dead_line = datetime(today.year, today.month, today.day, 6, 0, 0)
            if (tore_time >= dead_line):
                continue
            print(tr.findAll('td')[0].getText().strip(), "-----", tr.findAll('td')[1].getText().strip())
            dict.update({tr.findAll('td')[0].getText().strip(): tr.findAll('td')[1].getText().strip()})
        print("----------------------------------")
        return dict
    except:
        pass

if __name__ == '__main__':

    var0 = sys.argv[1]
    var1 = sys.argv[2]

    start_time = sys.argv[3]
    end_time = sys.argv[4]
    _start_time = sys.argv[5]
    _end_time = sys.argv[6]
    period = (float)(sys.argv[7])
    
    delta_max = (int)(period*60*60)
    start = time.time()

    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
    beijing_cur = utc_now.astimezone(SHA_TZ)
    print(beijing_cur.strftime("%Y-%m-%d %H:%M"), "星期" + str(beijing_cur.weekday() + 1))
    begin = query(var0, var1)
    print("初始查询：", begin)
    while True:
        now = time.time()
        delta = (int)(now - start)
        if (delta >= delta_max):
            # print(utc_now.astimezone(SHA_TZ).strftime("%Y-%m-%d %H:%M:%S.%f"),"触发超时巡检退出条件，结束运行！")
            # print("触发超时巡检退出条件，结束运行！")
            exit(0)
        if (beijing_now >= end_time):
            # print(utc_now.astimezone(SHA_TZ).strftime("%Y-%m-%d %H:%M:%S.%f"),"我生君未生，君生我已老！")
            exit(0)
        if (start_time > beijing_now):
            # print(utc_now.astimezone(SHA_TZ).strftime("%Y-%m-%d %H:%M:%S.%f"),"不是不报，时候未到！")
            time.sleep(10)
            utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
            beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
            continue
        if (beijing_now > start_time and beijing_now < end_time):
            cur = query(var0, var1)
            print("循环查询查询：", cur)
            if (begin == cur):
                sleep_times = 595
                time.sleep(sleep_times)
                utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
                beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
            if (cur < begin):
                print("昨日未充值！昨日消费：" , (cur - begin))
                exit(0)
            if (cur > begin):
                print("昨日充值！")
                dict = qryHis(var0, var1)
                for k,v in dict.items():
                    if (begin + (float)(v) > cur):
                        print(k, "充值",   v, " |昨日消费：", (begin + (float)(v) - cur))
                        exit(0)
                    else:
                        begin = begin + (float)(v)
