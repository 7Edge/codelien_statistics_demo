#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: sql_helpers
# Date: 4/21/2019
from settings import DevConfig


def connection():
    conn = DevConfig.DB_POOL.connection()
    cursor = conn.cursor()
    return conn, cursor


def connection_close(conn, cursor):
    cursor.close()
    conn.close()  # 连接不是真的关闭，是放回连接池


# 获取一条数据
def fetch_one(sql, params):
    conn, cursor = connection()
    cursor.execute(sql, params)
    result = cursor.fetchone()
    connection_close(conn, cursor)
    return result


# 获取所有数据
def fetch_all(sql, params):
    conn, cursor = connection()
    cursor.execute(sql, params)
    result = cursor.fetchall()
    connection_close(conn, cursor)
    return result


# 获取指定行数据
def fetch_many(sql, params, size=5):
    conn, cursor = connection()
    cursor.execute(sql, params)
    result = cursor.fetchmany(size=size)
    connection_close(conn, cursor)
    return result


# 插入一条数据
def insert(sql, params):
    conn, cursor = connection()
    result = cursor.execute(sql, params)
    cursor.commit()
    connection_close(conn, cursor)
    return result


if __name__ == '__main__':
    pass
