from pydantic import BaseModel
from typing import Optional

class RecoRequest(BaseModel):
    taille: Optional[str]
    activite: Optional[str]
    habitation: Optional[str]
    experience: Optional[str]
    enfants: Optional[bool]
    allergies: Optional[bool]

class BreedOut(BaseModel):
    nom: str
    description: str
    origine: Optional[str]
    groupe: Optional[str]
    taille: Optional[str]
    poids: Optional[str]
    activite: Optional[str]
    entretien: Optional[str]
    appartement: Optional[str]
    enfants: Optional[str]
    url: str
