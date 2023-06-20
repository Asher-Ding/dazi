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
from .models import Chat, ChatRecord
from flask.views import MethodView


chat = Blueprint("chat", __name__, url_prefix="/chat")

# [ ] 定义一个获取records的API，并能通过postman获取到数据
# [ ] 定义一个添加records的API，并能通过postman添加数据

class RecordAPI(MethodView):
    def get(self, chat_id):
        """
        Get chat records from database

        This API returns the chat records from database.

        ---
        tags:
            - chat
        parameters:
            - name: chat_id
              in: path
              type: string
              required: true
              description: The chat id of the chat room, which is unique.

            - name: user_id
              in: path
              type: string
              required: true
              description: The user id of the user, which is unique.

        responses:
            200:
              description: The chat records of the chat room.
            404:
              description: The chat room does not exist.

        returns:
            - name: chat_records
              in: body
              type: json
        """
        # TODO 编写获取窗口聊天信息记录的内容
        pass

    def post(self, chat_id):
        """
        Add a chat record to database

        This API adds a chat record to database.

        ---
        tags:
            - chat
        parameters:
            - name: chat_id
              in: path
              type: string
              required: true
              description: The chat id of the chat room, which is unique.

            - name: user_id
              in: path
              type: string
              required: true
              description: The user id of the user, which is unique.

        responses:
            200:
              description: The chat record is added to database successfully.
            404:
              description: The chat room does not exist.

        returns:
            - name: chat_record
              in: body
              type: json
        """
        # TODO 编写添加聊天信息记录的内容
        chat_record = ChatRecord

        pass

    def put(self, chat_id):
        pass

    def delete(self, chat_id):
        pass


# @impl 是Python中的一个装饰器，用于标记某个方法实现了目标接口或抽象类的抽象方法
# tryfirst=True 表示优先使用该方法
# @impl(RecordAPI, tryfirst=True)
