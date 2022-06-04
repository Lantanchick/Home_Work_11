import json


def load_candidates_from_json():
    """
    возвращает список всех кандидатов
    """
    with open("date/cands.json", "r", encoding="utf8") as file:
        date = json.load(file)
    return date


def get_candidate(candidate_id, date):
    """
    возвращает одного кандидата по его id
    """
    for cand in date:
        if cand["id"] == candidate_id:
            return cand


def get_candidates_by_name(candidate_name, date):
    """
    возвращает кандидатов по имени
    """
    lt = []
    for cand in date:
        if candidate_name.lower() in cand["name"].lower():
            lt.append(cand)
    return lt


def get_candidates_by_skill(skill_name, date):
    """
    возвращает кандидатов по навыку
    """
    lt = []
    for cand in date:
        if skill_name.lower() in cand["skills"].lower().split(", "):
            lt.append(cand)
    return lt
