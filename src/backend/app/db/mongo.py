import os
from pymongo import MongoClient
from app import app

# 定义MongoDB的连接信息
# TODO 通过环境变量来获取
db_host = "mongodb://localhost:27017/"
db_name = "dazi_db"

db_username_path = "/run/secrets/db_username"
db_password_path = "/run/secrets/db_password"

if os.path.exists(db_username_path):
    # 只有在容器的情况下才会存在这个文件
    with open(db_username_path, "r") as f:
        db_username = f.read().strip()
    with open(db_password_path, "r") as f:
        db_password_path = f.read().strip()
else:
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(
        "The 'db_username_path' does not exists, your current path is: "
        + current_path
        + ". It seems like you are not in a container, so we will use the default username and password."
    )
    db_username = "root"
    db_password = "12345678"


class Mongo:
    def __init__(self):
        self.client = MongoClient(db_host)
        self.db = self.client[db_name]

