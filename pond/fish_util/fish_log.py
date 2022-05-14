#!/usr/bin/python
# -*- encoding: utf-8 -*-

import logging
from logging.config import fileConfig
from os import path

# load logger config
log_file_path = path.join(path.dirname(path.abspath(__file__)), '../../logging.cfg')
fileConfig(log_file_path)


class FishLog(object):
    # critical > error > warning > info > debug
    @staticmethod
    def get_logger(name=''):
        return logging.getLogger(name)

    @staticmethod
    def debug(logger, msg):
        logger.debug(msg)

    @staticmethod
    def info(logger, msg):
        logger.info(msg)

    @staticmethod
    def warning(logger, msg):
        logger.warning(msg)

    @staticmethod
    def error(logger, msg):
        logger.error(msg)

    @staticmethod
    def critical(logger, msg):
        logger.critical(msg)


if __name__ == '__main__':
    logger = FishLog.get_logger()
    FishLog.info(logger, "asdf")
