from schemas import RaceCriteria

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
