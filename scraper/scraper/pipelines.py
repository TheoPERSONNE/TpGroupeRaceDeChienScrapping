import os
import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class ScraperPipeline:
    def open_spider(self, spider):
        self.logger = logging.getLogger(__name__)
        uri = os.getenv("MONGO_URI")

        if not uri:
            self.logger.error("❌ MONGO_URI n'est pas défini dans le fichier .env")
            raise ValueError("MONGO_URI est requis")

        try:
            self.logger.info("🔌 Connexion à MongoDB...")
            self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Timeout de 5 secondes
            self.client.server_info()  # Déclenche une exception si la connexion échoue
            self.db = self.client["dogmatch"]
            self.collection = self.db["breeds"]
            self.logger.info("✅ Connexion MongoDB réussie")
        except ServerSelectionTimeoutError as e:
            self.logger.error(f"❌ Connexion MongoDB échouée : {e}")
            raise e

    def close_spider(self, spider):
        self.logger.info("🔒 Fermeture de la connexion MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            result = self.collection.update_one(
                {"nom": item.get("nom")},
                {"$set": dict(item)},
                upsert=True
            )
            self.logger.debug(f"📥 Donnée insérée/mise à jour : {item.get('nom')}")
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'enregistrement de l'item : {e}")
        return item
