#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   decorators.py
@Time    :   2023/05/13 15:09:35
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   装饰器
"""

from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user_id"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))

    return wrapper
