import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # charge le .env à la racine (ou le chemin que tu donnes)

class ScraperPipeline:
    def open_spider(self, spider):
        uri = os.getenv("MONGO_URI")
        self.client = MongoClient(uri)
        self.db = self.client["dogmatch"]
        self.collection = self.db["breeds"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.update_one(
            {"nom": item.get("nom")},
            {"$set": dict(item)},
            upsert=True
        )
        return item
