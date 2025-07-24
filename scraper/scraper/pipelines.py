import os
import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv
from scraper.utils.cleaning import clean_label, clean_value, extract_poids_taille

load_dotenv()  # Charge .env

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
        # Nettoyage labels & valeurs
        cleaned_item = {}

        for key, value in item.items():
            clean_key = clean_label(key)
            if isinstance(value, str):
                # Pour poids/taille on traite différemment
                if clean_key.startswith("poids_") or clean_key.startswith("taille_"):
                    poids, taille = extract_poids_taille(value)
                    # Enregistre uniquement la bonne donnée (poids ou taille) selon la clé
                    if clean_key.startswith("poids_") and poids:
                        cleaned_item[clean_key] = poids
                    elif clean_key.startswith("taille_") and taille:
                        cleaned_item[clean_key] = taille
                    else:
                        cleaned_item[clean_key] = clean_value(value)
                else:
                    cleaned_item[clean_key] = clean_value(value)
            else:
                cleaned_item[clean_key] = value

        # Upsert dans MongoDB
        self.collection.update_one(
            {"nom": cleaned_item.get("nom")},
            {"$set": cleaned_item},
            upsert=True
        )
        return cleaned_item
