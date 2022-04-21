#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests as req

FISH_MIN_LEVEL = 1
FISH_MAX_LEVEL = 4

FISH_MIN_TYPE_ID = 0
FISH_MAX_TYPE_ID = 1000000

FISH_MAX_PIECE = 50


def build_url(page, level, id):
    return 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php' \
           '/Market_Center.getHQNodeData?page={}&num=100&sort=symbol&asc=1&node=sw{}_{}'.format(page, level, id)


def query_fish_type():
    for id in range(FISH_MIN_TYPE_ID, FISH_MAX_TYPE_ID):
        for level in range(FISH_MIN_LEVEL, FISH_MAX_LEVEL):
            for page in range(0, FISH_MAX_PIECE):
                try:
                    url = build_url(page, level, str(id).zfill(6))
                    res = req.get(url)
                    if res == "[]":
                        break
                    else:
                        print("useful id {}".format(id))
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    query_fish_type()
    1
