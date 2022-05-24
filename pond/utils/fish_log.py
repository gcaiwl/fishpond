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
    _fishlogger = None

    @staticmethod
    def get_logger():
        if FishLog._fishlogger is None:
            FishLog._fishlogger = FishLog._get_logger()
        return FishLog._fishlogger

    @staticmethod
    def debug(msg):
        FishLog._debug(FishLog.get_logger(), msg)

    @staticmethod
    def info(msg):
        FishLog._info(FishLog.get_logger(), msg)

    @staticmethod
    def warning(msg):
        FishLog._warning(FishLog.get_logger(), msg)

    @staticmethod
    def error(msg):
        FishLog._error(FishLog.get_logger(), msg)

    @staticmethod
    def critical(msg):
        FishLog._critical(FishLog.get_logger(), msg)

    @staticmethod
    def _get_logger(name=''):
        return logging.getLogger(name)

    @staticmethod
    def _debug(logger, msg):
        logger.debug(msg)

    @staticmethod
    def _info(logger, msg):
        logger.info(msg)

    @staticmethod
    def _warning(logger, msg):
        logger.warning(msg)

    @staticmethod
    def _error(logger, msg):
        logger.error(msg)

    @staticmethod
    def _critical(logger, msg):
        logger.critical(msg)


if __name__ == '__main__':
    # logger = FishLog.get_logger()
    FishLog.info("asdf")
    FishLog.info("asdf")
