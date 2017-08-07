# !/usr/bin/python
# -*- coding: utf-8 -*-
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = True

    APP_ENV = os.environ.get("APP_ENV")

class TestConfig(BaseConfig):
    DEBUG = False
    WTF_CSRF_ENABLED = False

class LocalhostConfig(BaseConfig):
    DEBUG = True
    TESTING = False

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


config = {
    '_baseconfig': BaseConfig,
    'localhost': LocalhostConfig,
    'test': TestConfig,
    'production': ProductionConfig,
}

__all__ = ['config']
