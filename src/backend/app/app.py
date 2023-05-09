#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   app.py
@Time    :   2023/05/09 12:36:03
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
'''
import os
from flask import Flask

def creat_app(config=None, instance_path=None):
    app = Flask('DAZIX', instance_path=instance_path)
    
    configure_app(app, config)
    configure_context_processors(app)
    
    return app
    
def configure_app(app, config):
    # Use the default config and override it afterwards
    app.config.from_object('app.configs.default.DefaultConfig')
    

def configure_context_processors(app):
    pass

creat_app()