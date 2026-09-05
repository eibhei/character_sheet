import json
from pathlib import Path

CLASSES_DATA = Path(__file__).parent / "data" / "classes"

def get_roles() -> list[str]:
    roles = []
    for role_file in sorted(CLASSES_DATA.glob("*.json")):
        data = json.loads(role_file.read_text())
        for cls in data["class"]:
            if cls.get("source") == "XPHB" or cls.get("basicRules2024"):
                roles.append(cls["name"])
                break

    return roles

def get_races() -> list[str]:
    races = []
    races_file = Path(__file__).parent / "data" / "races.json"
    data = json.loads(races_file.read_text())
    for race in data["race"]:
        if race.get("source") == "XPHB" or race.get("basicRules2024"):
            races.append(race["name"])

    return races
