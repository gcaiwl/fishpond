#!/usr/bin/python
# -*- encoding:utf-8 -*-
from pond.fish_farm.fish_store import Farm

if __name__ == '__main__':
    farm = Farm()
    num = farm.query('select * from fish_test')
    print(num)
    #
    # farm2 = Farm()
    # num = farm2.query('desc fish_company')
    # print(num)
    #
    # schema = farm2.schema('fish_company')
    # print(schema)
