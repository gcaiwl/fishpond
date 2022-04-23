#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pymysql


class Pond(object):
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset)

    def __del__(self):
        if self.conn:
            self.conn.close()

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
    fish_pond_host = '127.0.0.1'
    fish_pond_user = 'fish'
    fish_pond_pass = 'fish1234'
    fish_pond_db = 'fishpond'

    pond = Pond(fish_pond_host, fish_pond_user, fish_pond_pass, fish_pond_db)
    num = pond.query('select * from fish_test')
    print(num)
