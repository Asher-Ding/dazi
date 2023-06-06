#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   models.py
@Time    :   2023/05/10 11:39:49
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   chat的models
"""
# ==== 思考 ====
# 1. 一个用户可以有多个聊天室
# 2. 一个聊天室可以有多个用户
# 3. 一个聊天室可以有多条聊天记录
# 4. 一条聊天记录可以属于一个聊天室
# 5. 一条聊天记录可以属于一个用户
# 6. 一个用户可以有多条聊天记录
# 7. 聊天记录分成多成类型，如：文字、图片、视频、文件、任务等
# 8. 聊天记录可以有多个附件
# 9. 以后聊天记录的类型还会增加，如：语音、视频等，所以聊天记录的类型应该是一个表
# 10. 聊天记录如何设计表？根据类型设计？还是根据聊天室设计？还是根据用户设计？
# 11. 因此只能使用非关系型数据库，如：MongoDB，因为聊天记录的类型是不固定的，而且聊天记录的类型还会增加
# 12. 聊天记录的类型表，应该是一个字典，如：{"text": "文字", "image": "图片", "video": "视频", "file": "文件", "task": "任务"}
# 13. 直接存储在聊天记录表中，不需要单独设计一个聊天记录类型表

from app.db import mongo


class ChatRoom(mongo.Document):
    """聊天室"""

    name = mongo.StringField(max_length=64, required=True, unique=True)
    members = mongo.ListField(mongo.StringField(max_length=64), required=True)
    messages = mongo.ListField(mongo.StringField(max_length=64), required=True)

    meta = {"collection": "chat_rooms"}


class ChatRecord(mongo.Document):
    """聊天记录"""

    user_id = mongo.StringField(max_length=64, required=True)
    user_name = mongo.StringField(max_length=64, required=True)
    user_avatar = mongo.StringField(max_length=64, required=True)
    content = mongo.StringField(max_length=64, required=True)
    type = mongo.StringField(max_length=64, required=True)
    attachments = mongo.ListField(mongo.StringField(max_length=64), required=True)

    meta = {"collection": "records"}

    def __str__(self):
        return f"<Records {self.user_name}>"

    {
        "chat_id": "1234567890",
        "user_id": "1234567890",
        "chat_name": "随机森林",
        "records": [
            {
                "record_id": "1234567890",
                "user_id": "1234567890",
                "user_name": "Asher Ding",
                "user_avatar": "https://avatars.githubusercontent.com/u/38181430?v=4",
                "content": "Hello World!",
                "type": "text",
                "attachments": [
                    {
                        "type": "image",
                        "url": "https://avatars.githubusercontent.com/u/38181430?v=4",
                    }
                ],
            },
            {
                "record_id": "1234567890",
                "user_id": "1234567890",
                "user_name": "Asher Ding",
                "user_avatar": "https://avatars.githubusercontent.com/u/38181430?v=4",
                "content": "Hello World!",
                "type": "text",
                "attachments": [
                    {
                        "type": "image",
                        "url": "https://avatars.githubusercontent.com/u/38181430?v=4",
                    }
                ],
            },
        ],
    }
