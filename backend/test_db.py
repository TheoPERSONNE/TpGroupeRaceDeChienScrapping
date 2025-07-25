# backend/test_db.py

from database import get_database

db = get_database()
breeds = list(db.races.find())  # Assure-toi que ta collection s'appelle "races"
print("Nombre de races:", len(breeds))

if breeds:
    print("Exemple :", breeds[0]["nom"])
else:
    print("⚠️ La base est vide")
