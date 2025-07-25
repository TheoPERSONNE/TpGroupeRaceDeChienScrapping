from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query
from pydantic import BaseModel
from typing import Optional, List, Dict
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # adapte selon ton front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["dogmatch"]
breeds_collection = db["breeds"]

# MODELS

class StatBlock(BaseModel):
    resume: Optional[str]
    stats: Dict[str, int]

class RaceCriteria(BaseModel):
    activite: Optional[List[StatBlock]] = None
    caractere: Optional[List[StatBlock]] = None
    comportementautres: Optional[List[StatBlock]] = None
    conditionsvie: Optional[List[StatBlock]] = None
    education: Optional[List[StatBlock]] = None
    entretien: Optional[List[StatBlock]] = None
    sante: Optional[List[StatBlock]] = None

# ROUTES

@app.get("/race/{nom}")
def get_race(nom: str):
    race = breeds_collection.find_one(
        {"nom": {"$regex": f"^{nom}$", "$options": "i"}}, {"_id": 0}
    )
    if not race:
        all_races = list(breeds_collection.find({}, {"_id": 0, "nom": 1}))
        return {"error": "Race non trouvée", "available_races": all_races}
    return race
@app.get("/races")
def list_races(search: Optional[str] = Query(None), gabarit: Optional[str] = Query(None)):
    query = {}

    if search:
        # Recherche insensible à la casse sur le nom
        query["nom"] = {"$regex": search, "$options": "i"}

    if gabarit:
        query["gabarit"] = gabarit

    races = list(breeds_collection.find(query, {"_id": 0}))
    return {"races": races}
def score_similarity(race: dict, criteria: RaceCriteria) -> float:
    score = 0
    count = 0

    def compare_section(section_name):
        nonlocal score, count
        crit_blocks = getattr(criteria, section_name)
        race_blocks = race.get(section_name, [])
        if crit_blocks and race_blocks:
            for crit_block in crit_blocks:
                crit_stats = crit_block.stats
                for race_block in race_blocks:
                    race_stats = race_block.get("stats", {})
                    for key, val in crit_stats.items():
                        if key in race_stats:
                            score += abs(race_stats[key] - val)
                            count += 1

    for section in [
        "activite",
        "caractere",
        "comportementautres",
        "conditionsvie",
        "education",
        "entretien",
        "sante",
    ]:
        compare_section(section)

    return score / count if count > 0 else float('inf')

@app.post("/recommandation")
def recommandation(criteria: RaceCriteria):
    races = list(breeds_collection.find({}, {"_id": 0}))
    scored = [(score_similarity(race, criteria), race) for race in races]
    scored.sort(key=lambda x: x[0])
    result = [r[1] for r in scored if r[0] != float('inf')][:3]
    return {"recommendations": result}
