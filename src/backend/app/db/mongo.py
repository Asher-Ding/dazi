from pymongo import MongoClient
from app import app

# from configs.default import MONGO_URI, MONGO_DB_NAME

mongo_uri = app.config.get("MONGODB_URI")
mongo_db_name = app.config.get("MONGODB_DB_NAME")


class Mongo:
    def __init__(self):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db_name]


mongo_instance = Mongo()
print(mongo_db_name)
