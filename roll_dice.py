import random

def roll_dice(num_dice: int, num_faces: int) -> list[int]:
    rolls = []


    for d in range(0,num_dice):
        r = random.randint(1, num_faces)
        rolls.append(r)

    return rolls

# Use the following to get the resultant rolls and sum
# print(f"{" + ".join(str(r) for r in result)} = {sum(result)}")
