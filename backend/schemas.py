from typing import List, Dict
from pydantic import BaseModel
from typing import Optional, List, Dict

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
