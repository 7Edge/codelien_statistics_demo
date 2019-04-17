#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: account
# Date: 4/17/2019

from flask import Blueprint, session, redirect, render_template, request, url_for

from mysql_connection import get_connection

account_bp = Blueprint(name='account_bp', import_name=__name__)


@account_bp.route(rule='/login/', endpoint='login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template(template_name_or_list='account/login.html')
    # 获取用户名和密码
    loginname = request.form.get('loginname')
    password = request.form.get('password')

    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "select `id` from `account` where `username`=%s and `password`=%s"
            cursor.execute(sql, (loginname, password))
            result = cursor.fetchone()
            pass
    finally:
        connection.close()

    if not result:
        return '用户名或密码错误!'

    if 'username' in session:  # 这里对已经登陆再进行登陆的都进行清空会话，即使同一个用户旧的也不保留。
        session.clear()
    session['username'] = loginname
    session['user_id'] = result.get('id')

    return redirect(location=url_for(endpoint='.users'))


@account_bp.route('/users/', methods=['GET', ])
def users():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "select a.id, a.username, b.codelines from `account` a left join `code_statistics` b on a.id=b.user_id"
            cursor.execute(sql)
            result = cursor.fetchmany(size=50)
            print(result)
    finally:
        connection.close()
    return render_template('account/users.html', **{'users': result})


if __name__ == '__main__':
    pass