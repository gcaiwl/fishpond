#!/usr/bin/python
# -*- encoding: utf-8 -*-

import requests as req

from pond.utils.fish_log import FishLog


class FishAgent(object):

    @staticmethod
    def get(url, header=None):
        try:
            res = req.get(url, headers=header)
            if res.status_code != 200:
                FishLog.error("status={}, resonse={}".format(res.status_code, res.text))
            return res
        except Exception as e:
            FishLog.error("{} get exception {}".format(url, e))
        return None

    @staticmethod
    def post(url, data=None, header=None):
        try:
            res = req.post(url, data, headers=header)
            if res.status_code != 200:
                FishLog.error("status={}, resonse={}".format(res.status_code, res.text))
            return res
        except Exception as e:
            FishLog.error("{} post exception {}".format(url, e))
        return None
