#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pymysql

from pond.fish_util.fish_file import FishFile


class Farm(object):
    def __init__(self):
        kv = FishFile.read_config()
        if len(kv.keys()) < 1:
            print('read fish.cfg fail')
            return
        self.conn = self.connect(kv['fish_pond_host'], kv['fish_pond_user'], kv['fish_pond_pass'], kv['fish_pond_db'])

    def __del__(self):
        if self.conn:
            self.conn.close()

    def connect(self, host, user, password, db, port=3306, charset='utf8'):
        return pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset)

    def execute(self, sql):
        num = 0
        if sql:
            try:
                with self.conn.cursor() as cursor:
                    num = cursor.execute(sql)
            except Exception as e:
                print(e)
        return num

    def query(self, sql):
        result = None
        if sql:
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
            except Exception as e:
                print(e)
        return result


if __name__ == '__main__':
    farm = Farm()
    num = farm.query('select * from fish_test')
    print(num)
