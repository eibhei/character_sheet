# Character Sheet
A python3 program to use for participating in Dungeons and Dragons games as a player.

## Intention
A fully functional, 1-20 character sheet application, with dice rolling and damage calculations

## Features
- Create a character at any level
- Track all information about their stats, abilities, spells, equipment, background, etc.
- Save/load, import/export characters
- Roll dice with all modifiers applied
- Track XP, level up

## Plan
1. Build the Python logic first
  - Character() class which contains the core stats such as HP, ability scores, inventory, level, etc.
  - Add methods to calculate derivative values such as ability modifiers, proficiency bonuses, armour class
  - Add a simple dice-rolling utility

2. Build the persistence layer
  - Saving and loading
    - With a selection screen on first run?
  - Export and import

3. Build interactivity
  - Basic text-prompt menu to test things such as taking damage, rolling checks, modifying inventory
  - Verify rules and mechanics work as expected

4. Build the true TUI
  - Decide on the library to use. `textual` seems like a good choice
  - Wrap Character data into a tabbed interface
