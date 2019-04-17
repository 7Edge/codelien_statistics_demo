#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: mysql_connection
# Date: 4/17/2019
import pymysql


def get_connection():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='123456',
                                 db='codeline_statistics_demo',
                                 charset='utf8mb4',
                                 port=3306,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


if __name__ == '__main__':
    pass
