from fastapi import APIRouter, Query
from typing import Optional
from database import breeds_collection

router = APIRouter()

@router.get("/race/{nom}")
def get_race(nom: str):
    race = breeds_collection.find_one(
        {"nom": {"$regex": f"^{nom}$", "$options": "i"}}, {"_id": 0}
    )
    if not race:
        all_races = list(breeds_collection.find({}, {"_id": 0, "nom": 1}))
        return {"error": "Race non trouvée", "available_races": all_races}
    return race

@router.get("/races")
def list_races(search: Optional[str] = Query(None), gabarit: Optional[str] = Query(None)):
    query = {}
    if search:
        query["nom"] = {"$regex": search, "$options": "i"}
    if gabarit:
        query["gabarit"] = gabarit
    races = list(breeds_collection.find(query, {"_id": 0}))
    return {"races": races}
