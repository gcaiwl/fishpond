#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json as j
import time

import requests as req


def build_header(code):
    return {
        'authority': 'stock.xueqiu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://xueqiu.com',
        'referer': 'https://xueqiu.com/snowman/S/{}/detail'.format(code),
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'cookie': 'device_id=13c2e937e30f3da96470259ced7d6738; s=do1wt5nrhl; xq_a_token=7a84ec3929cd1e60abe21a2c26b9292767c1bd62; xqat=7a84ec3929cd1e60abe21a2c26b9292767c1bd62; xq_r_token=1b89b595a3ae0881d42538acf4948a94fd506777; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY1Mjc0MzcwMywiY3RtIjoxNjUwNTUyMzgyNDYxLCJjaWQiOiJkOWQwbjRBWnVwIn0.USX3T9A87gEOiqSOSj30sKgZQCV3A9U8ZqyVsS76r_sSp-Ff6m7LYcicSJQ7_S0BQCuCNpKEU6wqQZjyFyFbko9Wu1Csj-HlcBpmlK1wQB0CjIFRMAN51wJSdutmMGp5Ee9rTckhocPvdKRmo8IkVrbt_j8YaB0z6RdO7t9iVkUjoUjCooyUYlfvfN5_0nGX9H86b2zkpCEM3l1OchzoVRyyMZbpuio9oewJaYBtu0xOc3eYxbaxMXPBLK-sSxuVemwU8wXzzSX5JTHxcufHdZhsYDlYBg6OiHIEI2MXYHTUlnWkxuXS-C2zanVvJYcIlrS78JZzTbEuBqxPILQN4Q; u=511650552422008; Hm_lvt_1db88642e346389874251b5a1eded6e3=1650067654,1650552423; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1650552487'
    }


def query_fish_company(code):
    # build header
    header = build_header(code)

    # build url
    publish_time = None
    url = "https://stock.xueqiu.com/v5/stock/f10/cn/company.json?symbol={}".format(code)
    res = req.get(url, headers=header)
    if res.status_code == 200:
        apps = j.loads(res.content)
        publish_time = apps["data"]['company']["listed_date"]
    return publish_time


def query_fish_data(code, begin, count):
    # build header
    header = build_header(code)

    # build url
    url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json?' \
          'symbol={}&begin={}&period=day&type=before&count=-{}' \
          '&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'.format(code, begin, count)

    value = 0
    res = req.get(url, headers=header)
    if res.status_code == 200:
        try:
            apps = j.loads(res.content)
            # print(len(apps["data"]["item"]))

            items = apps["data"]["item"]
            if items is None:
                return

            for i in range(len(items)):
                if i < 1:
                    value = items[i][0]
                # print(items[i])
                time_loc = time.localtime(int(items[i][0]) / 1000)
                time_date = time.strftime("%Y-%m-%d %H:%M:%S", time_loc)
                print(time_date)
        except Exception as e:
            print(e)
    return value


def query_time():
    return int(round(time.time() * 1000))


def scan():
    # https://xueqiu.com/service/v5/stock/screener/quote/list?page=2&size=90&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1650259427950
    return 1


if __name__ == '__main__':
    # SH600508
    # 1650332328532
    # 284

    code = 'SZ002180'
    count = 200

    now = query_time()
    begin = query_fish_company(code)
    if begin is None:
        print("begin None error")

    while now > begin:
        print("show now value {}".format(now))
        now = query_fish_data(code, now, count)
        if now > 0:
            now -= 3600 * 24 * 1000
