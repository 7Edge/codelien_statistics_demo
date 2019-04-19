#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: settings
# Date: 4/17/2019


#
class BaseConfig(object):
    PWD_SALT = b'sas3_e2&we%$^l234j'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    pass


# dev
class DevConfig(BaseConfig):
    SECRET_KEY = 'dev'
    DEBUG = True


# product
class ProductConfig(BaseConfig):
    SECRET_KEY = 'a82_e98j2_34kd_kd'
    DEBUG = False


# test
class TestConfig(BaseConfig):
    SECRET_KEY = 'test'
    DEBUG = True


if __name__ == '__main__':
    pass
