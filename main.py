#! /usr/bin/env python3
from character import Character
from roll_dice import roll_dice
from get_data import get_roles, get_races



def main():
    print("Hello world!")

    sam = Character("Samwise Gamgee", 1, "Halfling", "Fighter")
    print(f"{sam.name} is a level {sam.level} {sam.race} {sam.role}.")

if __name__ == "__main__":
    main()
