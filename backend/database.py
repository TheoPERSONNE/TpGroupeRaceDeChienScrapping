from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = None
db = None

def connect_db():
    global client, db
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db = client["dogmatch"]

def get_breeds():
    return list(db["breeds"].find({}, {"_id": 0}))

def insert_breeds(breeds: list[dict]):
    if not breeds:
        return 0
    db["breeds"].insert_many(breeds)
    return len(breeds)
