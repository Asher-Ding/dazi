#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2023/05/09 12:35:05
@Author  :   Asher Ding 
@Version :   0.1.0
@Contact :   asherding@icloud.com
@License :   (C)Copyright 2023-2023, Asher Ding
@Desc    :   None
"""
# 导入必要的模块和依赖项
from flask import Flask

# from flasgger import Swagger

# 创建应用程序实例
app = Flask("DAZIX")
# 初始化Swagger
# swagger = Swagger(app)
# flasgger have some bugs needed to be fixed

# 配置应用程序
app.config.from_object("app.configs.default.DefaultConfig")

# 注册蓝图

# 启动应用程序
if __name__ == "__main__":
    app.run()
