#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests as req

from pond.fish_util.fish_log import FishLog

logger = FishLog.get_logger()


def get(url, header=None):
    try:
        res = req.get(url, headers=header)
        if res.status_code != 200:
            FishLog.error(logger, "status={}, resonse={}".format(res.status_code, res.text))
            return

        return res.text
    except Exception as e:
        FishLog.error(logger, "{} get exception {}".format(url, e))
    return None

# def post(url, data=None):
#     try:
#         res = req.post(url, data)
#     except Exception as e:
#         FishLog.error(logger, "{} post exception {}".format(url, e))
#     #     apps = j.loads(res.text)
#     #     publish_time = apps["data"]['company']["listed_date"]
#     # return publish_time
