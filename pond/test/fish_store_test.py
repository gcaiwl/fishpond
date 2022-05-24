#!/usr/bin/python
# -*- encoding:utf-8 -*-
from pond.store.fish_store import FishStore

if __name__ == '__main__':
    store = FishStore()
    num = store.query('select * from test')
    print(num)
    #
    # store = FishStore()
    # num = store.query('desc fish_company')
    # print(num)
    #
    # schema = store.schema('fish_company')
    # print(schema)
