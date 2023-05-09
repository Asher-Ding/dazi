#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   views.py
@Time    :   2023/05/09 22:13:30
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
"""
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    current_app,
)

msg = Blueprint("msg", __name__, url_prefix="/msg")


# 获取当前主题下的所有留言
@msg.route("/get_records", methods=["GET", "POST"])
def get_records():
    # TODO 编写获取当前主题下的所有留言的内容
    pass


# 发表留言
@msg.route("/send_message", methods=["GET", "POST"])
def send_message():
    # TODO 编写发表留言的内容
    pass
