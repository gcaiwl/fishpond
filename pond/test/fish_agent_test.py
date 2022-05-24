#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests as req

from pond.agent.fish_agent import FishAgent
from pond.seed.fish_company import FishCompany


def get_cookie():
    res = req.get('https://xueqiu.com/snowman/account/login')

    cookies = res.cookies
    print(cookies)

    cookie = req.utils.dict_from_cookiejar(cookies)
    print(cookie)
    return cookie


# 'cookie': 'device_id=13c2e937e30f3da96470259ced7d6738; s=do1wt5nrhl; xq_a_token=e8119f7d7a050cdbfa822fa0da4de5bec1ee0dc7; xqat=e8119f7d7a050cdbfa822fa0da4de5bec1ee0dc7; xq_r_token=bab125594aab3ef313d5a620a0e9aa1dc69c42bb; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY1NDAzOTczMSwiY3RtIjoxNjUxNzYyMzc2NTE0LCJjaWQiOiJkOWQwbjRBWnVwIn0.Ai4-LkSJZbeMlrEiPamfac7056qPS4ZlB37HcRxYGzibaafgsUmJvbUVO_OqShljjxvqL2nFGkw--EE5jIwVmaWFaDfHijzwbpeGQbaVWYr2ZEjcft-frQlkFId6I6LMy-k9yJdZItYGxKPCfkX4z8bl1XI7sVg6fhEsyy3jvFyIecdovZI-KeHcTw6N9ndVHFKDgsyXcJtOiEaYgR9u7uhKMD7x4c5YZAkEXgOsFcJPArW9osuBZ_xNX2Xlg0Jw-hYz4Ri4kgLVUL0Iv9yaoLj4UELg5QF8-nuGIrY5WdoFuMzt_2_7JqDwDy5u_yv2K2weoDO8CmK6xThR0_2xPQ; u=451651762376926; Hm_lvt_1db88642e346389874251b5a1eded6e3=1650552423; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1652679191'

def build_header(code, cookie):
    return {
        'authority': 'stock.xueqiu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://xueqiu.com',
        'referer': 'https://xueqiu.com/snowman/S/{}/detail'.format(code),
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'cookie': cookie
    }


if __name__ == '__main__':
    company = FishCompany()

    cookie = get_cookie()
    val = ""
    for (k, v) in cookie.items():
        val += "{}:{};".format(k, v)



    # val = 'device_id=13c2e937e30f3da96470259ced7d6738; s=do1wt5nrhl; __utmz=1.1650067661.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=1; u=451651762376926; xq_a_token=93613ef2dc688245d6f2ef8b913d9525607d4717; xqat=93613ef2dc688245d6f2ef8b913d9525607d4717; xq_r_token=992a34d4f1f561614ca2b79c397c111777b854a7; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY1NTMzNTc0MCwiY3RtIjoxNjUyNzQ0Nzg4MDU4LCJjaWQiOiJkOWQwbjRBWnVwIn0.pjcFTkyKRYqJpThAnatXMTwLRWegGzxpAEE8pgGGy2sUE0fskrRc8ezvVOkZvCxSbaSccdwK7VsY9gbquWOPQpUpZ_FG8aFAvH-531_ZkwwjDEkG-EwnlQZRfvLCXOnrzeSSd1YFsogJCmfX9XUt9GgvP1CBGKTvWDpiDZzXFI6bLC7L3kXf3WmD9YDzO8bMfhDCUEa6J87AMqzYozmeysJaexSyYUOypslrhaIjUd-48OhB_Zsr1oGi7FGPb-JuFY3fU6-QNDq6cCOXVOYpJo0_cgc837uDalbdf2QgCLXacGpDXI1_9MmANMwLoXonLKikggGJBLufd98AW4rlaw; acw_tc=2760779216533193161312443ebbf44c913e55448b3f1fc128c80f2bb3481a; __utma=1.2114782632.1650067661.1652678842.1653319317.12; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1653319324; __utmb=1.3.10.1653319317; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1653319858'

    # val = 'device_id=13c2e937e30f3da96470259ced7d6738; ' \
    #     's=do1wt5nrhl; ' \
    #     '__utmz=1.1650067661.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ' \
    #     '__utmc=1; ' \
    #     'u=451651762376926; ' \
    #     'xq_a_token=93613ef2dc688245d6f2ef8b913d9525607d4717; ' \
    #     'xqat=93613ef2dc688245d6f2ef8b913d9525607d4717; ' \
    #     'xq_r_token=992a34d4f1f561614ca2b79c397c111777b854a7; ' \
    #     'xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY1NTMzNTc0MCwiY3RtIjoxNjUyNzQ0Nzg4MDU4LCJjaWQiOiJkOWQwbjRBWnVwIn0.pjcFTkyKRYqJpThAnatXMTwLRWegGzxpAEE8pgGGy2sUE0fskrRc8ezvVOkZvCxSbaSccdwK7VsY9gbquWOPQpUpZ_FG8aFAvH-531_ZkwwjDEkG-EwnlQZRfvLCXOnrzeSSd1YFsogJCmfX9XUt9GgvP1CBGKTvWDpiDZzXFI6bLC7L3kXf3WmD9YDzO8bMfhDCUEa6J87AMqzYozmeysJaexSyYUOypslrhaIjUd-48OhB_Zsr1oGi7FGPb-JuFY3fU6-QNDq6cCOXVOYpJo0_cgc837uDalbdf2QgCLXacGpDXI1_9MmANMwLoXonLKikggGJBLufd98AW4rlaw; ' \
    #     'acw_tc=2760779216533193161312443ebbf44c913e55448b3f1fc128c80f2bb3481a; ' \
    #     '__utma=1.2114782632.1650067661.1652678842.1653319317.12; ' \
    #     '__utmt=1; ' \
    #     'Hm_lvt_1db88642e346389874251b5a1eded6e3=1653319324; ' \
    #     '__utmb=1.3.10.1653319317; ' \
    #     'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1653319858'

    # todo
    # 'xqat=93613ef2dc688245d6f2ef8b913d9525607d4717;'

    val = 'xqat=93613ef2dc688245d6f2ef8b913d9525607d4717; '

    url = company.build_url('SH600613')
    header = build_header('SH600613', val)

    agent = FishAgent()
    res = agent.get(url, header)
    print(res)
