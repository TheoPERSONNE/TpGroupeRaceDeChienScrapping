from typing import List, Dict
from pydantic import BaseModel

class StatSection(BaseModel):
    resume: str
    stats: Dict[str, int]

class RaceModel(BaseModel):
    nom: str
    activite: List[StatSection]
    caractere: List[StatSection]
    comportementautres: List[StatSection]
    conditionsvie: List[StatSection]
    description: str
    education: List[StatSection]
    entretien: List[StatSection]
    gabarit: str
    origine: str
    poids_femelle: str
    poids_male: str
    poil: str
    sante: List[StatSection]
    taille_femelle: str
    taille_male: str
    tete: str
    url: str
