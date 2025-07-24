def recommend_breeds(breeds, criteria):
    scores = []

    for breed in breeds:
        score = 0
        if criteria.taille and breed.get("taille", "").lower() == criteria.taille.lower():
            score += 1
        if criteria.activite and breed.get("activite", "").lower() == criteria.activite.lower():
            score += 1
        if criteria.habitation and criteria.habitation.lower() in breed.get("appartement", "").lower():
            score += 1
        if criteria.enfants and "oui" in breed.get("enfants", "").lower():
            score += 1
        scores.append((score, breed))
        
    scores.sort(key=lambda x: -x[0])
    return [b for s, b in scores if s > 0][:5]
