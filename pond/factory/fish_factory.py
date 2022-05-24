#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re
import time

import jsonpath as jp

from pond.store.fish_store import FishStore
from pond.utils.fish_log import FishLog

table_schema_cache = dict()


class FishFactory(object):

    def __init__(self):
        self.store = FishStore()

    def build(self, data, data_schema, table):
        num = 0
        try:
            table_schema = table_schema_cache.get(table)
            if table_schema is None:
                table_schema = self.store.schema(table)
                table_schema_cache[table] = table_schema

            obj = self._build_object(data, data_schema)
            sql = self._build_insert(table, table_schema, obj)
            FishLog.info("build sql={}".format(sql))

            num = self.store.execute(sql)
        except Exception as e:
            FishLog.error("table = {}; data_schema={}; data={} build exception {}".format(table, data_schema, data, e))
        return num

    def _build_object(self, data, schema) -> dict:
        obj = dict()
        for (key, path) in schema.items():
            obj[key] = None
            if path:
                res = jp.jsonpath(data, path)
                if res and len(res) > 0:
                    obj[key] = res[0]
        return obj

    def _build_insert(self, table, schema, obj):
        field = ""
        value = ""
        index = 1

        for (key, val) in obj.items():
            if "id" == key:
                continue
            field += key

            if val is None:
                val = 'null'

            if key in ('gmt_create', 'gmt_modified'):
                val = 'now()'
            elif re.match("^.*_date", key):
                deta = 1
                if len(str(val)) > 11:
                    deta = 1000
                val = time.strftime('%Y-%m-%d', time.localtime(val / deta))
                val = "'{}'".format(val)
            elif 'str' == schema[key]:
                val = "'{}'".format(val.strip())
            else:
                val = str(val)

            value += val
            if index != len(obj) - 1:
                field += ', '
                value += ', '
            index += 1
        return "insert into {} ({}) values ({});".format(table, field, value)
