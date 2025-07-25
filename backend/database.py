from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = None
db = None

def connect_db():
    global client, db
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise ValueError("MONGO_URI is not set in the .env file.")
    client = MongoClient(uri)
    db = client["dogmatch"]
    print("✅ Connexion à MongoDB réussie.")
