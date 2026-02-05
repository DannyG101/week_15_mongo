import pymongo
import json
import os
from dotenv import load_dotenv

load_dotenv()


class DBConnect:

    def __init__(self):
        self.client = None
        self.db = None
        self.coll = None

        self.host = os.getenv("MONGO_HOST", "localhost")
        self.user = os.getenv("MONGO_USER", "root")
        self.password = os.getenv("MONGO_PASS", "mypassword")
        self.port = os.getenv("MONGO_PORT", "27017")
        self.file_path = './employee_data_advanced.json'

    def connect(self):
        if self.client is None:
            uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}"
            self.client = pymongo.MongoClient(uri)
            self.db = self.client["test_db"]
            self.coll = self.db["restaurants"]

    def load_file(self):
        self.connect()
        if len(list(self.coll.find())) == 0:
            with open(self.file_path) as file:
                file_data = json.load(file)
                self.coll.insert_many(file_data)

    def get_all(self):
        self.connect()
        return list(self.coll.find())




