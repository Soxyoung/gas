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
        today = utc_now.astimezone(SHA_TZ)
        for tr in tab.findAll('tr')[1:]:
            tore_time = parse(tr.findAll('td')[0].getText().strip())
            dead_line = datetime(today.year, today.month, today.day, 6, 15, 0)
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

    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
    beijing_cur = utc_now.astimezone(SHA_TZ)
    print(beijing_cur.strftime("%Y-%m-%d %H:%M"), "星期" + str(beijing_cur.weekday() + 1))
    begin = query(var0, var1)
    print("初始查询：", begin)
    qryHis(var0, var1)