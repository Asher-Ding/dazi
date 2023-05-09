#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   view.py
@Time    :   2023/05/09 21:53:54
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
"""
from flask import Blueprint, request, redirect, url_for, flash

chat = Blueprint("chat", __name__, url_prefix="/chat")


@chat.route("/get_records", methods=["GET", "POST"])
def get_records():
    # TODO 编写获取窗口聊天信息记录的内容
    pass


@chat.route("/send_message", methods=["GET", "POST"])
def send_message(msg):
    # TODO 编写发送聊天信息的内容
    pass
