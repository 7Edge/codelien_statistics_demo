#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: statistic_view
# Date: 4/17/2019
"""
blueprint：代码上传统计视图
"""

import os
import zipfile
import datetime
import filetype

from flask import Blueprint, request, session, render_template

from mysql_connection import get_connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE_PATH = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload_codes')

statistic_bp = Blueprint('statistic', __name__)


# 上传代码视图
@statistic_bp.route('/upload_code/', methods=['POST', 'GET'])
def upload_code():
    if request.method == 'GET':
        return render_template('statistic/upload.html')

    # 处理上传文件
    upload_file = request.files.get('codefile', None)
    if not upload_file:
        return '上传文件失败'

    file_name = upload_file.filename
    local_full_filename = os.path.join(STORE_PATH, file_name)

    # 1. 将文件保存到本地
    upload_file.save(dst=local_full_filename)

    # 2. 判断文件类型
    line_cnt = 0

    kind = filetype.guess(local_full_filename)
    if kind.extension == 'zip':
        # 2.1 如果时候压缩文件，先解压文件
        zipfile_obj = zipfile.ZipFile(local_full_filename)
        zipfile_obj.extractall(path=STORE_PATH)
        zipfile_obj.close()
        # 2.2 获取压缩文件中所有文件的行数

    else:
        # 2.3 对于普通文件直接读取
        with open(local_full_filename, 'r') as fp:
            for line in fp:
                line_cnt += 1
    # 3. 将提交代码写入到数据库中
    uid = session.get('user_id')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "insert into code_statistics (user_id, codelines, date) values(%s, %s, %s)"
            result = cursor.execute(sql, (uid, line_cnt, today))
            print(result)
        connection.commit()
    finally:
        connection.close()
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
