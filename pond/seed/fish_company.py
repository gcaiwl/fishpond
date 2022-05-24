#!/usr/bin/python
# -*- encoding: utf-8 -*-
from pond.seed.fish_seed import FishSeed


class FishCompany(FishSeed):
    def build_url(self, code):
        return "https://stock.xueqiu.com/v5/stock/f10/cn/company.json?symbol={}".format(code)

    def build_header(self, code):
        return {
            'authority': 'stock.xueqiu.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'origin': 'https://xueqiu.com',
            'referer': 'https://xueqiu.com/snowman/S/{}/detail'.format(code),
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'cookie': 'device_id=13c2e937e30f3da96470259ced7d6738; s=do1wt5nrhl; xq_a_token=e8119f7d7a050cdbfa822fa0da4de5bec1ee0dc7; xqat=e8119f7d7a050cdbfa822fa0da4de5bec1ee0dc7; xq_r_token=bab125594aab3ef313d5a620a0e9aa1dc69c42bb; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY1NDAzOTczMSwiY3RtIjoxNjUxNzYyMzc2NTE0LCJjaWQiOiJkOWQwbjRBWnVwIn0.Ai4-LkSJZbeMlrEiPamfac7056qPS4ZlB37HcRxYGzibaafgsUmJvbUVO_OqShljjxvqL2nFGkw--EE5jIwVmaWFaDfHijzwbpeGQbaVWYr2ZEjcft-frQlkFId6I6LMy-k9yJdZItYGxKPCfkX4z8bl1XI7sVg6fhEsyy3jvFyIecdovZI-KeHcTw6N9ndVHFKDgsyXcJtOiEaYgR9u7uhKMD7x4c5YZAkEXgOsFcJPArW9osuBZ_xNX2Xlg0Jw-hYz4Ri4kgLVUL0Iv9yaoLj4UELg5QF8-nuGIrY5WdoFuMzt_2_7JqDwDy5u_yv2K2weoDO8CmK6xThR0_2xPQ; u=451651762376926; Hm_lvt_1db88642e346389874251b5a1eded6e3=1650552423; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1652679191'
        }

    def resolve(self):
        pass

# header = build_header(code)
#
# # build url
# publish_time = None
# url = "https://stock.xueqiu.com/v5/stock/f10/cn/company.json?symbol={}".format(code)
# res = req.get(url, headers=header)
# if res.status_code == 200:
#     apps = j.loads(res.text)
#     publish_time = apps["data"]['company']["listed_date"]
# return publish_time
