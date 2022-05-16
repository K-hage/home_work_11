import json
from pprint import pp
DATA_PATH = "candidates.json"


def load_candidates_from_json(path=DATA_PATH):
    """
    Возвращает список всех кандидатов
    """

    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    """

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if int(candidate_id) == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """

    candidates = load_candidates_from_json()
    candidates_list = []
    for candidate in candidates:
        if candidate_name.title().strip() == candidate["name"].title().split()[0]:
            candidates_list.append(candidate)
    return candidates_list


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    """

    candidates = load_candidates_from_json()
    candidates_list = []

    for candidate in candidates:
        if skill_name.lower().strip() in candidate["skills"].lower().split(", "):
            candidates_list.append(candidate)
    return candidates_list


# pp(get_candidates_by_name("Adela"))
