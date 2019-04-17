#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: statistic_view
# Date: 4/17/2019
"""
blueprint：代码上传统计视图
"""

from flask import Blueprint, request, session, render_template

from mysql_connection import get_connection

statistic_bp = Blueprint('statistic', __name__)


# 上传代码视图
@statistic_bp.route('/upload_code/', methods=['POST', 'GET'])
def upload_code():
    if request.method == 'GET':
        return render_template('statistic/upload.html')
    return 'upload success'


# 查看用户的上传记录
@statistic_bp.route('/code_record/<int:uid>/')
def code_record(uid):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "select `id`, `codelines`, `date` from code_statistics where `user_id`=%s"
            cursor.execute(sql, (uid,))
            result = cursor.fetchmany(size=50)
            print(result)
        with connection.cursor() as cursor:
            sql = "select * from account where id=%s"
            cursor.execute(sql, (uid,))
            user = cursor.fetchone()
    finally:
        connection.close()

    return render_template(template_name_or_list='statistic/code_records.html', **{'records': result,
                                                                                   'user': user})


if __name__ == '__main__':
    pass
