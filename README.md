# 🐶 DogMatch – Recommandez la race de chien idéale
## Développé de façon agile pour livrer un MVP en 3 jours

DogMatch est une application qui aide les utilisateurs à trouver la race de chien la plus adaptée à leur mode de vie.
Le projet est composé de trois parties principales :

* 🔙 **Backend** : API REST avec **FastAPI** et **MongoDB**
* ⚛️ **Frontend** : Interface utilisateur en **React + Vite**
* 🕷 **Scraper** : Extraction des données avec **Scrapy**

---
## 👨‍💻 Auteurs

* **Théo Personne** – Frontend - Backend - Scraping
* **Théo Kraichette** – Scraping / Backend / DevOps
---

## 📁 Structure du projet

```bash
dogmatch/
├── backend/             # API FastAPI
│   ├── main.py
│   ├── database.py
│   ├── utils.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── breeds.py
│   │   └── recommendation.py
│   └── __init__.py
│
├── frontend/            # Application React (Vite)
│   ├── src/
│   ├── public/
│   └── vite.config.js
│
├── scraper/             # Scraper Scrapy
│   ├── scrapy.cfg
│   └── scraper/
│       ├── spiders/
│       │   └── woopets.py
│       ├── items.py
│       ├── pipelines.py
│       └── settings.py
│
├── .env                 # Variables d'environnement
├── requirements.txt     # Dépendances backend/scraper
└── README.md
```

---

## 🚀 Lancement du projet

### 1. ⚙️ Prérequis

* Python 3.10+
* Node.js 21+
* MongoDB local ou distant
* Environnement virtuel Python (recommandé)

---

### 2. 🔍 Scraper les données

```bash
cd scraper
scrapy crawl woopets
```

---

### 3. 🔙 Lancer le backend FastAPI

```bash
cd backend
uvicorn main:app --reload
```


```env
MONGO_URI=YOUR_MONGO_URI
```

---

### 4. ⚛️ Lancer le frontend React

```bash
cd frontend
npm install
npm run dev
```

Cela démarre le serveur Vite sur [http://localhost:5173](http://localhost:5173).

---

## 🔗 API disponibles

* `GET /races?search=labra` — Rechercher une race
* `GET /race/Berger Allemand` — Obtenir les détails d'une race
* `POST /recommandation` — Obtenir les races recommandées selon des critères

---

## 🚛 requirements.txt

```txt
# Core FastAPI app
fastapi
uvicorn[standard]

# Data validation
pydantic

# CORS & fichiers
python-multipart
aiofiles
requests

# MongoDB
pymongo

# Environnement
python-dotenv

# Scraping
scrapy

# Dev / test
httpx
pytest
```


---

## 📅 To-do / Idées futures

* [ ] Amélioration des filtres
* [ ] Amélioration de l'interface
* [ ] Authentification utilisateur
* [ ] Historique des recommandations
* [ ] Dashboard admin
* [ ] Classement des races les plus populaires

---

