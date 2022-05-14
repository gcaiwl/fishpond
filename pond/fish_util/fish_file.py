#!/usr/bin/python
# -*- encoding: utf-8 -*-

from os import path


class FishFile(object):
    @staticmethod
    def read_file(filename, encoding='utf-8'):
        context = list()
        if filename:
            with open(filename, 'r', encoding=encoding) as r:
                for l in r.readlines():
                    context.append(l.strip())
        return context

    @staticmethod
    def read_config():
        config = dict()
        config_path = path.join(path.dirname(path.abspath(__file__)), '../../fish.cfg')
        context = FishFile.read_file(config_path)
        for ctx in context:
            kv = ctx.split("=")
            if len(kv) == 2:
                config[kv[0].strip()] = kv[1].strip()
        return config
