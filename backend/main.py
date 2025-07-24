from fastapi import FastAPI, HTTPException
from backend.database import connect_db, get_breeds, insert_breeds
from backend.schemas import RecoRequest, BreedOut
from backend.utils import recommend_breeds
import subprocess

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    connect_db()

@app.get("/breeds", response_model=list[BreedOut])
def get_all_breeds():
    return get_breeds()

@app.post("/scrape/woopets")
def run_scraper():
    result = subprocess.Popen(["scrapy", "crawl", "woopets"], cwd="./scraper")
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail="Scraping failed.")
    return {"message": "Scraping terminé."}

@app.post("/recommend", response_model=list[BreedOut])
def recommend(request: RecoRequest):
    breeds = get_breeds()
    return recommend_breeds(breeds, request)
