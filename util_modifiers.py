from data_structures import *
from util import *


# Function to handle character movement
def move_character(character: Character, new_position: tuple):
	from math import sqrt
	x1, y1 = character.position
	x2, y2 = new_position
	distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	units_moved = distance
	if units_moved <= character.MR:
		character.position = new_position
		return f"{character.name} moves to position {character.position}."
	else:
		return f"{character.name} cannot move that far. Maximum movement range is {character.MR} steps."


# Function to handle attacks
def attack(attacker: Character, defender: Character, attack_type='melee', defender_reaction: Optional[str]=None):
	# Determine attack and defense stats
	if attack_type == 'melee':
		attack_stat = attacker.P + attacker.temp_P
		base_damage = attacker.P + attacker.temp_P
	elif attack_type == 'ranged':
		attack_stat = attacker.W + attacker.temp_W
		base_damage = attacker.W + attacker.temp_W
	else:
		return "Invalid attack type."

	# Attacker's roll
	attack_roll = average_roll_2d6() + attack_stat

	# Defender's roll and reaction
	defense_stat = defender.A + defender.temp_A
	if defender_reaction == 'dodge' and defender.AP >= 1:
		defender.AP -= 1
		defense_roll = average_roll_with_advantage() + defense_stat
	elif defender_reaction == 'block' and defender.AP >= 1:
		defender.AP -= 1
		defense_roll = average_roll_2d6() + defender.P + defender.temp_P
	else:
		defense_roll = average_roll_2d6() + defense_stat

	# Determine if the attack hits
	if attack_roll > defense_roll:
		damage = base_damage + (attack_roll - defense_roll)
		defender.HP -= damage
		if defender.HP < 0:
			defender.HP = 0
		return f"{attacker.name} hits {defender.name} for {damage} damage. {defender.name} has {defender.HP} HP left."
	else:
		return f"{attacker.name}'s attack misses {defender.name}."


# Function to use an ability
def use_ability(user: Character, ability: Ability, target: Optional[Character]=None):
	if user.AP >= ability.cost:
		user.AP -= ability.cost
		# Apply the ability's effect
		if ability.effect:
			return ability.effect(user, target)
		else:
			return f"{user.name} uses {ability.name}."
	else:
		return f"{user.name} does not have enough AP to use {ability.name}."


# Example ability effect functions
def heal_ability(user: Character, target: Character):
	heal_amount = 3  # Example heal amount
	target.HP += heal_amount
	if target.HP > target.max_HP:
		target.HP = target.max_HP
	return f"{user.name} heals {target.name} for {heal_amount} HP."


def fireball_ability(user: Character, targets: List[Character]):
	damage = user.W + 2  # Damage as per the ability
	result = []
	for target in targets:
		target.HP -= damage
		if target.HP < 0:
			target.HP = 0
		result.append(f"{target.name} takes {damage} fire damage and has {target.HP} HP left.")
	return ' '.join(result)


# Function to pick up an item
def pick_up_item(character: Character, item: Item):
	character.items.append(item)
	return f"{character.name} picks up {item.name}."


# Function to use an item
def use_item(character: Character, item: Item):
	if item in character.items:
		if item.effect:
			result = item.effect(character)
			character.items.remove(item)  # Remove consumable items after use
			return result
		else:
			return f"{character.name} uses {item.name}."
	else:
		return f"{character.name} does not have {item.name}."


# Example item effect function
def healing_potion_effect(character: Character):
	heal_amount = 2
	character.HP += heal_amount
	if character.HP > character.max_HP:
		character.HP = character.max_HP
	return f"{character.name} consumes a Healing Potion and restores {heal_amount} HP."

