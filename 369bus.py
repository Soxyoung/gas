# coding:utf-8
import base64
import requests
import json
from datetime import datetime
import time
from datetime import timedelta
from datetime import timezone
import sys
import random
import uuid

geo_dict = [
    'F%QDqpc',
    'F%L#VZj',
    'F%Pq-jD',
    "aL?Jp,q",
    "aL~M!6f",
    "aL:O:5-",
    "aL?,!D;",
    "aL;x^1J",
    "aL/j~j7",
    "aL;L4=%",
    "aL/j~j^",
    "aL(1)/s",
    "aL%*G5*",
    "aL)^Rd'",
    "aL;^eP3",
    "aL`BHoj",
    "aL~TP!%",
    "aL;u7u)",
    "F%A2-sv",
    "F%Or_qC",
    "F%K)2r`",
    "F%Ma4SQ"
]

def get_jwt_token():
    try:
        time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
        sign = str(uuid.uuid1()).replace("-", "")
        s_host = b'YXBpLjM2OWN4LmNu'
        host = base64.b64decode(s_host).decode()
        headers = {
            'Host': host,
            'accept': '*/*',
            'authorization': '',
            'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
            'date': time_369,
            'cityid': '2500',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7200 NetType/WIFI DarkMode/0 BlindMode/0',
            'geo': '',
            'sign': sign,
        }
        s_url = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvQXV0aC9Mb2dpbkJ5VGVtcA=='
        url = base64.b64decode(s_url).decode()
        response = requests.post(url, headers=headers)
        print(response.json()["result"]["token"])
        return str(response.json()["result"]["token"])
    except Exception as err:
        print(err)
        jwt_dict = [
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1ESXpNalE1TmpJdE5URmhaUzAwTURFM0xXSmpOREl0TTJaaU5HVTNNMkk1T0dabCIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTEyNjQ5OTIyNjciLCJqdGkiOiJiOTNiNmE2Zi04ZTEzLTRhZTQtOTMyYy1jZDhjNjdhNGU3ZDYiLCJuYmYiOjE2NDc3NTQyMTUsImV4cCI6MTgwNTUyMDYxNSwiaWF0IjoxNjQ3NzU0MjE1LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.GZ-1YIfaikow-ijfZeM7tbZcL-QYZ5c621lBlvevcE5n5VzgNtCJt93S_0iemH29tTNMH2Bjqvo5unByEdixCFlkFC_LRgPBfPXhEelGwoSu5jLrldoXGNFF8mp6tJPsPaqqglkcq1KOBu-RjMmuyDgMmFAlAoKyijbEEKhJ9Pj_9SjqRBbkKgDj8qUeSRc-TGtFaEMgGRWYZX2EHRglE_aXOrWPm-6tNffuuDn234LJysVtoTlBDMbfIz2G_cVs5usSEVD7CXyZ8ZZ9j5845nrp7Z8wdg8mCj2-Z3xasPnfvi5v5XZmOJK7ShAebfK5IgIRRS_EUk5Oxhq6COP_Xw",
            'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlpETXhZVEZpWW1ZdFlUazVOUzAwTmpjMUxUaG1NelV0TVRjNFl6aGtaamhqWWpNMyIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE4Nzk4NDY3MTkiLCJqdGkiOiIxMGFlMmFkYi0wNGFlLTQ3MmMtYjgwMC1jMjliMzQwMTc3YzMiLCJuYmYiOjE2NDcxODI4MTMsImV4cCI6MTgwNDk0OTIxMywiaWF0IjoxNjQ3MTgyODEzLCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.EULawyV_Zd1phVU1xMQXDTM9MsemJi8NBe_wQJPhZnX_Vxb80GtDl-l5LhZkULaq9YtTF6COTt7z_-qvdWYit2OUS627rjUWitXA34DPFvoTpaQDpiC9YuLF9gxI7qcwz3Uij_pM4wIRWaiTqy1CCqkoyl4gGAcV5BHKectVM1n01n30aQJt529aaSwo1AfhJDjNqUCrfbnbNo5FFq06Z_M4-xyvjK22oXh8EzGDwsc324PP1l8oZmZnpFhLnOdzbgqaE9P1uoqdENFJP7q_tDIihpRboB4XmXnvWpTqCbJAtgX8u081-dQfZm_TslsN391bYzWbdxFZBIF8LEgiQg',
            'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlptTmxNMll3WkRjdFpXWTJNaTAwT1RRNExUZ3dZbVl0T0dZMFlXWTBaVE0yTkRJeSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE2MTA5MzUyODIiLCJqdGkiOiJlNjhiNWRiZS00ZTJlLTRhM2EtOWVlNi03MDE2NzFhNDk1MGIiLCJuYmYiOjE2NDcxMzc1MDksImV4cCI6MTgwNDkwMzkwOSwiaWF0IjoxNjQ3MTM3NTA5LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.PiR8LEjkcySPEpv2nJzHY2lp-_t0SeKWOMOw-Ag_tQl_Mis03jlvV-2Y01WfU-nvMtfrzXreUDH8Da06exjSoMdZ9Amy5GsQ-VxgxZHflloB04hp-MZ1zDFZPC3PfwYZTGDk2RHBzwcq62l7RLVWfq1XR84LH6wqcNeUDvUe89VivbH3kJ0QO4CRaqjCThbDq7GF9CDsTg-ajMd6bCu3ZhE5VXfH2NcmtFE_okM8feH7bLkSIgKJMrBS2pdNSTPmTSYwi4oEDxAQiBge4IhqI9JE_KPfqB5cKaW5C_9O-9yVpj7w-ItrhhQsaMAylm7buTJeyj72nmGRk1niGGUeCA',
            'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik4yTXlPR1F4WW1JdE1tUXpOaTAwTmpZeUxXSXhNalF0TmpRM09XRXpOVFF3TmpVeSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTEyNTQ0NzQ0NjEiLCJqdGkiOiIwNjEzMjFhZC1hN2U5LTQ2OTYtODliOS03YTA3ZTg5M2IwZjUiLCJuYmYiOjE2NDc3MDAxMTcsImV4cCI6MTgwNTQ2NjUxNywiaWF0IjoxNjQ3NzAwMTE3LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.FmlJ_IsLb3CP5uJ1ycqnAlpylO8bigsS7FkV3pNqMoUvr-6886_JYjdRD-W5anaXaJpuZmoLL7Mnwg5bjk8imbO5NUzjOH9mDwDKLlqMBQxUiWK-2gkAih2S3v9LKckDl28v09j4N5tGZx9Fwiz2OuARr-6cq15VshUZRDtwFbo9FTIg9FgP4517bqnKxc7IJOneN0x4iuISgnl3KVwFYDP6za8eCHMZgcoufACpwAjr44Wnh7Oj7TC4HWhlRtdCpTN8lAv27wboCHC9KmEiU8tJHIf9oJiKEeAi18NITWgJaNIdfW9EO_G8F_sTxVZ5S-2xuaKfZjvIFd9XXmYa_Q',
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik5UbGtNbVZrTnpVdFpEVmlPUzAwWVRsa0xUazFNalV0WVdOalpHRm1aVE5qTm1aaSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE3NzU0NTQyNjMiLCJqdGkiOiI5MGEzYzRmZi0wMjliLTQ3MTctOThmMS1lZDYzNDJhY2NhNjYiLCJuYmYiOjE2NDY5ODMyMzMsImV4cCI6MTgwNDc0OTYzMywiaWF0IjoxNjQ2OTgzMjMzLCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.ngXiGrBc44VE9nWGT_2Kmm8METc-aNugaLRzf3lBtQL2mmxSVKN0eMjgmfWuISj6nphdj8dUN6oDkBss2t5fV3W0Z3lITpSr32_m0m2K5l2RlL-lrWVzTWvZci6rmIB1WcxCVzNcOeaw4oAUO8jSmXXK5rxYfml8sd-Nzc07pvOZOw8qLX0tZyedDCeVPcc7GRuJzzu4e4Bjaurtrs-lunYwrilW7ZF-lzC3RDUj5bW8x3Bk-Am2ClIw8UvrA3QQvozD8dOFD_IT_Sot0vCVCe_WB6QBbGxFdowg9AOCJ6lvzTriPhPTbZY2WnZG4Buh_2AoMo8ztz8zlflDhXBygg",
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik9HSm1NVFpqWldVdE5qTTVOeTAwWVROaUxUZzBOakl0TURObE5qWXhNVEl3TmpneSIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTE3MDAwNjEwMCIsImp0aSI6ImE3MmYxNTUyLWUwMzUtNDYwOC05NDcyLTZmNmIwZTYzNjA3YSIsIm5iZiI6MTY0Nzc1NjE4MiwiZXhwIjoxODA1NTIyNTgyLCJpYXQiOjE2NDc3NTYxODIsImlzcyI6IndlYi4zNjljeC5jbiIsImF1ZCI6ImFwaS53ZWIuMzY5Y3guY24ifQ.LI-b11u8AiuJldQZki1gqHqqDyp2oKIsX3KwgexatllQObNFaeO3TrLZR1Xx_AkytXayyH2RaiBUbgoPMj1uJeF3nRs4DFEH3WU2KXPYHDan466lvoodoEko7ogkukD025_LdPKmL5AVWcPa-7iEBWJNyvZW3LyFjUz3czMUFPDNr0NQDNT2IyokSiB_TefuV_9UozZbiIuKEaF8AS_rtmWPETE5AkVy84TvjSpkG3RzE0smvIotxNfFnfq_inwr_iJpUm0AsZJtfbqEoe4QgcavJJrdzZThtXqYZQr8x3k3sjkYAIrHJvPerTLPe2omVuth098180s0_FSCaAg6uA",
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IllqUmhNMlJtWVdZdE9UQTVNQzAwWkRCakxUaGpORFV0TmpobU1tTm1OVFpqWmpsayIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTc4OTg3NTEyOCIsImp0aSI6IjI2MzA1MmFjLTZhNzktNDQ0Ni1iMGNiLTgxOWRkNDI3YmNhYSIsIm5iZiI6MTY0Nzc1NjI4OSwiZXhwIjoxODA1NTIyNjg5LCJpYXQiOjE2NDc3NTYyODksImlzcyI6IndlYi4zNjljeC5jbiIsImF1ZCI6ImFwaS53ZWIuMzY5Y3guY24ifQ.Eo714MKjyq9zMja4tYlcrZ5Mye9Nv1OaVS62SnYtMWEAjsjNIRrx1d0ZqW43EZAW4WhGD-TUc4o6R88Jrj_Hk9QjQ0ryyhITuzQE3TDDOlU6Ja3en-jWQGwbUhmanrOWJxKzjVU5H2jXHg6FfOGll2ZLK85ohKiiS9JpCtQN7hNeY0XroewtmR_CuCMCJEmpapI1SbGjgUKrW0CF-Je2GK1IiG7L5RJ-o-1U2bvQ4cot5lWE2BHLxvJZbqbBVctL7aJnN-euzPQ_AtYK3Qe2YuHV8Yj0AYf4r0slW8JqwRGzZysM8W7pW5p6iCruIxEJT9mTHoXhafh_mUbmWfkghQ",
            "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik5EUTJNalEzWldRdFpEY3haaTAwWm1FeUxUZzFNV1V0WkRZellXRXlPVFU0WW1KbCIsInJvbGUiOiJWaXNpdG9yIiwibmFtZWlkIjoiLTk4NzYxNTUxMSIsImp0aSI6IjEwYThiNTZmLWUwOTgtNDUwNi05ZjI2LWJiODkwM2YyZjI5YSIsIm5iZiI6MTY0Nzc1NjU3NSwiZXhwIjoxODA1NTIyOTc1LCJpYXQiOjE2NDc3NTY1NzUsImlzcyI6IndlYi4zNjljeC5jbiIsImF1ZCI6ImFwaS53ZWIuMzY5Y3guY24ifQ.LCT4bENKbn_HqbivZxQoZ0_mrekZtsLcRwzj3gWvf_NvTgTYJQN4BvZItN0Peq1niQ6GgEwuVdBdZLb6rScXDqXNqs5uWwrOgBfeaZwuA01NKRs5R19vDVWCcrJ_clxUOUjPzKH8xV75x9_48GGll1UPXqvGL6tuw7aY2ahudgmnkui8dVNKDz199XaUMaXs0d1D8MZR6lNNd3QKV8A4C_Lm3AgGWld3kbfvc3q1NlRUEGuuUScJZhDm8NQXADhYHvW5eV0VgkWi9JseczbpmiMwGrRL4gadV6o1xkg-44wfw7PhHHjQC9p989dDIR3QmE52J_WQx8OwV-87E2_6OQ",
        ]
        return random.choice(jwt_dict)

s_host = b'YXBpLjM2OWN4LmNu'
host = base64.b64decode(s_host).decode()
headers = {
    'Host': host,
    'content-type': 'application/json',
    'authorization': get_jwt_token(),
    'CityId': '2500',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x18001231) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx358ad33429ed6508/32/page-frame.html',
}

SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)

def scan(LINE, stations, SRC, DEST, dict, LINE_NAME):
    try:
        s_url = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvQnVzL0dldEJ1c3Nlc0J5TGluZUlkLw=='
        url = base64.b64decode(s_url).decode()
        response = requests.get(str(url) + str(LINE), headers=headers)
        info = json.loads(response.text)
        result = info['result']
        for bus in result:
            no = bus['stationNo']
            src_station = stations[no]
            key = bus['name']
            val = bus['siteTime']
            if (src_station['name'] == SRC and dict.get(key) == None):
                dict[key] = val
                site_time = datetime.fromtimestamp(bus['siteTime'], SHA_TZ).strftime('%H:%M:%S')
                # print(site_time, bus['name'], src_station['name'], bus['velocity'], bus['quJian'])
            if (src_station['name'] == DEST and dict.get(key) != None):
                then = dict.pop(key)
                delta = (val - then)
                minute = int(delta / 60)
                end_time = datetime.fromtimestamp(bus['siteTime'], SHA_TZ).strftime('%H:%M:%S')
                begin_time = datetime.fromtimestamp(then, SHA_TZ).strftime('%H:%M:%S')
                # print(site_time, bus['name'], src_station['name'], bus['velocity'], bus['quJian'], minute , "m" , (delta % 60) , "s" )
                print(begin_time, end_time, bus['name'], minute, "m", (delta % 60), "s", LINE_NAME)
    except Exception as err:
        print(err)
        print("刷新", LINE_NAME, "线路信息出错")
    finally:
        return

def research(LINE, SRC, DEST, LINE1, SRC1, DEST1, start_time, end_time):

    try:
        s_url = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvTGluZS9HZXRSZWFsVGltZUxpbmVJbmZvLw=='
        url = base64.b64decode(s_url).decode()
        response = requests.get(str(url) + str(LINE), headers=headers)
        info = json.loads(response.text)
        stations = info['result']['stations']
        name = info['result']['name']
    except Exception as err:
        print(err)
        print("获取线路", LINE, "站点信息出错")
        exit(0)

    try:
        s_url = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvTGluZS9HZXRSZWFsVGltZUxpbmVJbmZvLw=='
        url = base64.b64decode(s_url).decode()
        response = requests.get(url + str(LINE1), headers=headers)
        info = json.loads(response.text)
        stations1 = info['result']['stations']
        name1 = info['result']['name']
    except Exception as err:
        print(err)
        print("获取线路", LINE1, "站点信息出错")
        exit(0)

    dict_k163 = {}
    dict_308 = {}

    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
    beijing_cur = utc_now.astimezone(SHA_TZ)
    print(beijing_cur.strftime("%Y-%m-%d %H:%M"))
    print(beijing_cur.weekday() + 1)

    delta_max = (int)(3.95*60*60)
    start = time.time()

    if (0 != info['status']['code']):
        exit(0)

    cnt = 0
    content = ""
    detail1_fmt = "东八区：当前时间 %s 期望开始时间 %s 期望结束时间 %s"
    detail2_fmt = "倒计时：已经运行 %s 期望结束时差 %s 当前时间 %s"
    while True:
        cnt += 1

        now = time.time()
        delta = (int)(now - start)
        # print(now, start, now - start)
        data1 = (beijing_now, start_time, end_time)
        data2 = (delta, delta_max, time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
        detail1 = (detail1_fmt %data1)
        detail2 = (detail2_fmt %data2)

        content += detail1 + "\r\n"
        content += detail2
        content += "\r\n"

        if (delta >= delta_max):
            print("触发超时巡检退出条件，结束运行！")
            exit(0)
        if (beijing_now > end_time):
            exit(0)
        if (start_time > beijing_now):
            time.sleep(10)
            utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
            beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
            continue
        else:
            try:
                begin = time.time()

                scan(LINE, stations, SRC, DEST, dict_k163, name)
                scan(LINE1, stations1, SRC1, DEST1, dict_308, name1)

                end = time.time()
                sleep_times = begin + 10.0 - end
                if (sleep_times <= 0.0):
                    sleep_times = 9.5
                time.sleep(sleep_times)
                utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
                beijing_now = utc_now.astimezone(SHA_TZ).strftime("%H:%M")
            except Exception as err:
                print(err)
                time.sleep(9.5)

if __name__ == '__main__':

    _LINE = sys.argv[1]
    _SRC = sys.argv[2]
    _DEST = sys.argv[3]

    _LINE1 = sys.argv[4]
    _SRC1 = sys.argv[5]
    _DEST1 = sys.argv[6]

    _start_time = sys.argv[7]
    _end_time = sys.argv[8]

    data = (_LINE, _SRC, _DEST, _LINE1, _SRC1, _DEST1, _start_time, _end_time)
    format_str=" %s %s %s %s %s %s %s %s"
    title = (format_str %data)

    research(_LINE, _SRC, _DEST, _LINE1, _SRC1, _DEST1, _start_time, _end_time)
