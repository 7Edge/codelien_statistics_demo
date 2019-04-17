#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: wrappers
# Date: 4/17/2019


# 视图认证检测装饰器
# def auth_wrapper(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         is_login = session.get('is_login', None)
#         if is_login:
#             ret = func(*args, **kwargs)
#         else:
#             ret = redirect(location=url_for(endpoint='login'))
#         return ret
#
#     return inner

if __name__ == '__main__':
    pass
