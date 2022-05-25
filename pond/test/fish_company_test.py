#!/usr/bin/python
# -*- encoding: utf-8 -*-

from pond.factory.fish_factory import FishFactory
from pond.seed.fish_company import FishCompany
from pond.utils.fish_log import FishLog

if __name__ == '__main__':
    code = 'SH600613'
    data = FishCompany.resolve(code)
    if data is None:
        FishLog.error('code={}, return None', code)
    else:
        fatctory = FishFactory()
        num = fatctory.build(data, FishCompany.FISH_DICT, FishCompany.FISH_SEED)
        print("num={}".format(num))
