#! /usr/bin/env python3
from character import Character


def main():
    sam = Character("Samwise Gamgee", 1, "Halfling", "Fighter")

    print(f"Character name: {sam.name}")
    print(f"Character level: {sam.level}")
    print(f"Character race: {sam.race}")
    print(f"Character class: {sam.role}")

    print(f"Character HP: {sam.hp}")

if __name__ == "__main__":
    main()
