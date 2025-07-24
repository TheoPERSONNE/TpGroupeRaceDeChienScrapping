import unicodedata
import re

def clean_label(text):
    text = text.strip().lower()
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    return text.replace(" ", "_")

def clean_value(text):
    text = text.replace('\xa0', ' ')
    text = re.sub(r'(\d)(à)(\d)', r'\1 à \3', text)
    text = re.sub(r'(\d)(kg|cm)', r'\1 \2', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_poids_taille(text):
    poids = None
    taille = None
    poids_match = re.search(r'De\s*[\d\s]+kg\s*à\s*[\d\s]+kg', text, re.IGNORECASE)
    taille_match = re.search(r'De\s*[\d\s]+cm\s*à\s*[\d\s]+cm', text, re.IGNORECASE)
    if poids_match:
        poids = clean_value(poids_match.group(0))
    if taille_match:
        taille = clean_value(taille_match.group(0))
    return poids, taille
