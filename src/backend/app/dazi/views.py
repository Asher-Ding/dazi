#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   views.py
@Time    :   2023/05/09 22:04:58
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
"""
from flask import Blueprint, render_template, request, jsonify

dazi = Blueprint("dazi", __name__, url_prefix="/dazi")


# 获取搭子列表
@dazi.route("/get_list", methods=["GET", "POST"])
def get_list():
    # TODO 编写获取搭子列表的内容
    pass


# 选中搭子后，进入聊天窗口
@dazi.route("/chat", methods=["GET", "POST"])
def chat():
    # TODO 编写进入聊天窗口的内容
    pass


# 对搭子进行排序
@dazi.route("/sort", methods=["GET", "POST"])
def sort():
    # TODO 编写对搭子进行排序的内容
    pass


# 删除搭子
@dazi.route("/delete", methods=["GET", "POST"])
def delete():
    # TODO 编写删除搭子的内容
    pass
