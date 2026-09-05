from get_data import get_roles, get_races

class Character:
    def __init__(self, name: str, level: int, race: str, role: str) -> None:
        # TO-DO: Add validation to ensure inputs are correct types
        self.name = name

        if 0 < level <= 20:
            self.level = level
        else:
            raise ValueError("Character level must be an integer, 1-20.")

        allowed_races = get_races()
        if race in allowed_races:
            self.race = race
        else:
            raise ValueError(f"Race must be one of {allowed_races}.")

        # Class is a protected term, using role instead
        allowed_roles = get_roles()
        if role in allowed_roles:
            self.role = role
        else:
            raise ValueError(f"Role must be one of {allowed_roles}.")

        self.xp = 0
        self.hp = 0

        self.strength = 0
        self.dexterity = 0
        self.constituion = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    def level_up(self):
        pass
