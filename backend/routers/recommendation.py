from fastapi import APIRouter
from database import breeds_collection
from schemas import RaceCriteria
from utils import score_similarity

router = APIRouter()

@router.post("/recommandation")
def recommandation(criteria: RaceCriteria):
    races = list(breeds_collection.find({}, {"_id": 0}))
    scored = [(score_similarity(race, criteria), race) for race in races]
    scored.sort(key=lambda x: x[0])
    result = [r[1] for r in scored if r[0] != float('inf')][:5]
    return {"recommendations": result}
