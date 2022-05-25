#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json as J

from pond.agent.fish_agent import FishAgent
from pond.seed.fish_seed import FishSeed
from pond.utils.fish_log import FishLog


class FishCompany(FishSeed):
    FISH_SEED = 'fish_company'

    FISH_DICT = {
        'id': None,
        'gmt_create': None,
        'gmt_modified': None,
        'code': None,
        'short_name': '$.data.company.org_short_name_cn',
        'company_name': '$.data.company.org_name_cn',
        'country_region': '$.data.company.provincial_name',
        'business_mode': '$.data.company.classi_name',
        'main_business': '$.data.company.main_operation_business',
        'company_desc': '$.data.company.org_cn_introduction',
        'establish_date': '$.data.company.established_date',
        'employees': '$.data.company.staff_num',
        'listing_date': '$.data.company.listed_date',
        'shares_offered': '$.data.company.actual_issue_vol',
        'initial_price': '$.data.company.issue_price',
        'initial_pe': '$.data.company.pe_after_issuing'
    }

    @staticmethod
    def resolve(code):
        if code is None:
            FishLog.error("code is None")
            return None

        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }

        try:
            res = FishAgent.get('https://xueqiu.com/snowman/account/login', header)
            if res.cookies:
                header['cookie'] = '{}={};'.format('xqat', res.cookies.get('xqat'))
                header['accept'] = 'application/json, text/plain, */*'
                header['accept-language'] = 'zh-CN,zh;q=0.9'

            url = "https://stock.xueqiu.com/v5/stock/f10/cn/company.json?symbol={}".format(code)
            FishLog.info("seed={}, code={}, url={}".format(FishCompany.FISH_SEED, code, url))

            res = FishAgent.get(url, header)
            if res:
                return J.loads(res.text)
        except Exception as e:
            FishLog.error("{} resolve exception {}".format(code, e))
        return None
