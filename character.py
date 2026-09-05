class Character():
    def __init__(self, name: str, level: int, race: str, role: str) -> None:
        # TO-DO: Add validation to ensure inputs are correct types
        self.name = name
        if 0 < level <= 20:
            self.level = level
        else:
            raise ValueError("Character level must be an integer, 1-20.")

        self.race = race
        self.role = role

        self.xp = 0
        self.hp = 0

    def level_up(self):
        pass
