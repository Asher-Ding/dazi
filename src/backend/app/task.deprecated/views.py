#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   views.py
@Time    :   2023/05/09 22:18:57
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

task = Blueprint("task", __name__, url_prefix="/task")

# TODO 编写任务功能的内容
# 当用户访问包含任务的搭子时，首先会调用chat获取所有的聊天信息，～～若聊天信息包含任务，则会调用task获取任务信息～～
# Q：是否需要单独的数据库存储task的信息？task信息和普通的主题有什么不同？
# 获取任务信息（Deprecated）
# @task.route("/get_info", methods=["GET", "POST"])
# 任务信息直接在chat里面返回，任务详细也直接在msg里面返回
