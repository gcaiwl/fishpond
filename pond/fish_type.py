#!/usr/bin/python
# -*- encoding: utf-8 -*-

import datetime as dt
import requests as req
import json as j


def build_header():
    return {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Cookie': 'language=zh_CN; ctx=""',
        'Pragma': 'no-cache',
        'Referer': 'http://www.cnindex.com.cn/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }


# curl 'http://www.cnindex.com.cn/queryStockSylDetail' \
#   -H 'Accept: application/json, text/javascript, */*; q=0.01' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
#   -H 'Cookie: language=zh_CN; ctx=""' \
#   -H 'Origin: http://www.cnindex.com.cn' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: http://www.cnindex.com.cn/module/analysis-csrc-detail.html?act_menu=3' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36' \
#   -H 'X-Requested-With: XMLHttpRequest' \
#   --data-raw 'plateCode=4&category=008001&industry=B&dateStr=2022-04-25&pageNo=1&pageSize=10' \
#   --compressed \
#   --insecure

def build_url(date):
    return 'http://www.cnindex.com.cn/syl/{}/crsc.json'.format(date)


def query_fish_type(date):
    try:
        header = build_header()
        url = build_url(time_date)

        res = req.get(url, headers=header)
        if res.status_code != 200:
            print("code:{},response:{}".format(res.status_code, res.text))
            return

        # print(res.status_code)
        # print(res.text)

        result_json = j.loads(res.text)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    d = dt.datetime.now()
    print(d)
    d = d + dt.timedelta(days=-1)
    print(d)
    time_date = d.strftime("%Y-%m-%d")
    print(time_date)

    query_fish_type(time_date)
    1
