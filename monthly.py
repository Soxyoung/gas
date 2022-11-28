# coding:utf-8

import sys
import calendar
import requests
import base64
import json
import time
import uuid
import random
from datetime import datetime
from datetime import timedelta
from datetime import timezone

# 在容器里运行时时间为 UTC 时间，不是北京时间，需要进行调整
def beijing(sec, what):
    beijing_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    return beijing_time.timetuple()

SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)

def sendSeverJ(sendKey, title, content):
    api = "https://sctapi.ftqq.com/" + sendKey + ".send"
    data = {
       "text":title,
       "desp":content
    }
    req = requests.post(api, data = data)

def main(rst, sendKey):
    title = str(beijing_now.month) + u"月燃气费"
    content = rst
    sendSeverJ(sendKey, title, content)

def judge():
    # 协调世界时
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)
    currentdate = beijing_now.today()

    year= currentdate.year
    month = currentdate.month
    day = currentdate.day

    return beijing_now

if __name__ == '__main__':

    beijing_now = judge()
    print(beijing_now, beijing_now.tzname())
    print(beijing_now.strftime('%Y-%m-%d %H:%M:%S.%f'))

    key = sys.argv[0]
    rst = sys.argv[1]
    main(rst, key)
