#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   default.py
@Time    :   2023/05/09 12:42:31
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   This is the default configuration file.
"""
import os
import sys


class DefaultConfig(object):
    # Get the app root path
    # 获取当前文件所在目录的上三级目录即backend目录
    basedir = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    )

    # Python version
    py_version = "{0.major}.{0.minor}.{0.micro}".format(sys.version_info)

    # Flask Settings
    DEBUG = True
    TESTING = False

    # Flask-Bcrypt Settings
    MONGODB_URI = "mongodb://localhost:27017"
    MONGODB_DB_NAME = "dazi_db"
