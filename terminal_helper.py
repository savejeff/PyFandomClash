from data_structures import *
from param import *


# Function to print character status
def print_character_status(character: Character):
    print(f"===== Character Status Sheet: {character.name} =====")
    print(f"Player: {character.player}")
    print(f"Size: {character.size}")
    print(f"Role: {character.role if character.role else 'None'}")
    print(f"Fandom Trait: {character.fandom_trait if character.fandom_trait else 'None'}")
    print(f"Position: {character.position[0]} units, {character.position[1]} units")
    print("-" * 50)

    print("Base Stats:")
    print(f"  Power (P): {character.P}")
    print(f"  Agility (A): {character.A}")
    print(f"  Wisdom (W): {character.W}")
    print(f"  Movement Range (MR): {character.MR} units ({character.MR * GRID_SIZE} cm)")
    print()
    print(f"Current Health: {character.HP}/{character.max_HP}")
    print(f"Current Ability Points (AP): {character.AP}")
    print()

    # Calculate base damage for melee and ranged attacks
    melee_base_damage = character.P + character.temp_P
    ranged_base_damage = character.W + character.temp_W

    print("Attack Information:")
    print(f"  Melee Base Damage: {melee_base_damage}")
    print(f"  Ranged Base Damage: {ranged_base_damage}")
    print(f"  Note: Actual damage varies based on attack and defense rolls.")
    print()

    print("Abilities:")
    if character.abilities:
        for ability in character.abilities:
            print(f"  - {ability.name} (Cost: {ability.cost} AP)")
            print(f"    Description: {ability.description}")
        print()
    else:
        print("  None")
        print()

    print("Items:")
    if character.items:
        for item in character.items:
            print(f"  - {item.name} ({item.item_type})")
            print(f"    Description: {item.description}")
        print()
    else:
        print("  None")
        print()

    print("-" * 50)