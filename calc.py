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
import math

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
#         print(beijing_cur.strftime("%Y-%m-%d %H:%M:%S.%f"), res["data"]['remainmoney'])
        return float(res["data"]['remainmoney'])
    except Exception as err:
        print(err)
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
        soup = BeautifulSoup(resp, "html.parser")
        tab = soup.find('table')
#         print("----------------------------------")
        today = utc_now.astimezone(SHA_TZ)
        for tr in tab.findAll('tr')[1:]:
            tore_time = parse(tr.findAll('td')[0].getText().strip())
            dead_line = datetime(today.year, today.month, today.day, 6, 15, 0)
            if (tore_time >= dead_line):
                continue
#             print(tr.findAll('td')[0].getText().strip(), "-----", tr.findAll('td')[1].getText().strip())
            dict.update({tr.findAll('td')[0].getText().strip(): tr.findAll('td')[1].getText().strip()})
#         print("----------------------------------")
        return dict
    except Exception as err:
        print(err)
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
    beijing_yesterday = utc_now.astimezone(SHA_TZ) + timedelta(days=-1)
    date_info = beijing_yesterday.strftime("%Y-%m-%d")
    begin = query(var0, var1)
    while True:
        now = time.time()
        delta = (int)(now - start)
        if (delta >= delta_max):
            utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
            exit(0)
        cur = query(var0, var1)
        if math.isclose(begin, cur):
            sleep_times = 541.95
            time.sleep(sleep_times)
        if (cur < begin):
            print(date_info, round((begin - cur),2))
            exit(0)
        if (cur > begin):
            dict = qryHis(var0, var1)
            for k,v in dict.items():
                if (begin + (float)(v) > cur or math.isclose(begin + (float)(v), cur)):
                    print(date_info, round((begin + (float)(v) - cur),2))
                    exit(0)
                else:
                    begin = begin + (float)(v)
