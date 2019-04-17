#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: statistic_view
# Date: 4/17/2019
"""
blueprint：代码上传统计视图
"""

from flask import Blueprint, request, session, render_template

statistic_bp = Blueprint('statistic', __name__)


# 上传代码视图
@statistic_bp.route('/upload_code/', methods=['POST', 'GET'])
def upload_code():
    if request.method == 'GET':
        return render_template('statistic/upload.html')
    return 'upload success'


if __name__ == '__main__':
    pass
