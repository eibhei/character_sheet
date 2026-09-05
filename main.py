#! /usr/bin/env python3
from character import Character
from roll_dice import roll_dice

def main():
    # sam = Character("Samwise Gamgee", 1, "Halfling", "Fighter")

    # print(f"Character name: {sam.name}")
    # print(f"Character level: {sam.level}")
    # print(f"Character race: {sam.race}")
    # print(f"Character class: {sam.role}")

    # print(f"Character HP: {sam.hp}")

    result = roll_dice(3, 6)
    print(f"{" + ".join(str(r) for r in result)} = {sum(result)}")

if __name__ == "__main__":
    main()
