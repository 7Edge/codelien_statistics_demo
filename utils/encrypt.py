#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: encrypt
# Date: 4/19/2019
import hashlib

from settings import BaseConfig

salt_bytes = bytes(BaseConfig.PWD_SALT)


# 加密用户密码
def encrypt_pwd(password):
    md5_obj = hashlib.md5()
    md5_obj.update(salt_bytes)
    md5_obj.update(bytes(password, encoding='utf8'))
    return md5_obj.hexdigest()


if __name__ == '__main__':
    print(encrypt_pwd('123456'))
    print(encrypt_pwd('123456'))
    print(hashlib.md5(b'123456').hexdigest())

