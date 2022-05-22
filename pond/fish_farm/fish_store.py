#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re

import pymysql

from pond.fish_util.fish_file import FishFile
from pond.fish_util.fish_log import FishLog

logger = FishLog.get_logger()


class Farm(object):
    connect_cached = dict()

    def __init__(self, is_auto_load=True):
        if is_auto_load:
            kv = FishFile.read_config()
            if len(kv.keys()) < 1:
                FishLog.error('read fish.cfg fail')
                return

            self.conn = self.connect(kv['fish_pond_host'], kv['fish_pond_user'], kv['fish_pond_pass'],
                                     kv['fish_pond_db'])

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

    def schema(self, table):
        if table is None:
            FishLog.error("table is None")
            return None

        result = self.query("desc {}".format(table))
        if result is None:
            FishLog.error("desc query failed")
            return None

        schema = dict()
        for col in result:
            col_type = re.sub('\(.*$|\s.*', '', col[1])
            col_type = re.sub('text|varchar', 'str', col_type)
            col_type = re.sub('bigint|decimal|int', 'number', col_type)
            schema[col[0]] = col_type
        return schema

    def execute(self, sql):
        num = 0
        if sql:
            try:
                with self.conn.cursor() as cursor:
                    num = cursor.execute(sql)
                    self.conn.commit()
            except Exception as e:
                FishLog.error("{} execute exception {}".format(sql, e))
        return num

    def insert(self, sql):
        return self.execute(sql)

    def update(self, sql):
        return self.execute(sql)

    def query(self, sql):
        result = None
        if sql:
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
            except Exception as e:
                FishLog.error("{} query exception {}".format(sql, e))
        return result
