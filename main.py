from dataclasses import dataclass, field
from typing import List, Optional
import random


# Define the Ability class
@dataclass
class Ability:
	name: str
	cost: int  # AP cost
	description: str
	effect: Optional[callable] = None  # Function to apply the ability effect


# Define the Item class
@dataclass
class Item:
	name: str
	item_type: str  # e.g., 'weapon', 'shield', 'consumable'
	description: str
	effect: Optional[callable] = None  # Function to apply the item's effect


# Define the Character class
@dataclass
class Character:
	name: str
	player: str
	P: int  # Power
	A: int  # Agility
	W: int  # Wisdom
	max_HP: int
	HP: int
	AP: int
	MR: int  # Movement Range (in units of 5 cm)
	abilities: List[Ability] = field(default_factory=list)
	items: List[Item] = field(default_factory=list)
	size: str = 'Medium'  # 'Small', 'Medium', or 'Large'
	position: tuple = (0, 0)  # (x, y) coordinates in cm
	fandom_trait: Optional[str] = None  # e.g., 'Anime', 'Superhero'
	role: Optional[str] = None  # e.g., 'Warrior', 'Ranger'

	# Temporary modifiers (e.g., from abilities or items)
	temp_HP: int = 0
	temp_A: int = 0
	temp_P: int = 0
	temp_W: int = 0

	def is_alive(self):
		return self.HP > 0


# Define the GameState class
@dataclass
class GameState:
	characters: List[Character]
	current_turn: int = 0
	players: List[str] = field(default_factory=list)
	terrain: dict = field(default_factory=dict)  # For environmental interactions


# Dice rolling functions
def roll_d6():
	return random.randint(1, 6)


def roll_2d6():
	return roll_d6() + roll_d6()


def average_roll_2d6():
	return (roll_2d6()) // 2


def roll_with_advantage():
	roll1 = roll_d6()
	roll2 = roll_d6()
	return max(roll1, roll2)


def roll_with_disadvantage():
	roll1 = roll_d6()
	roll2 = roll_d6()
	return min(roll1, roll2)


def average_roll_with_advantage():
	return (roll_with_advantage()) // 2


def average_roll_with_disadvantage():
	return (roll_with_disadvantage()) // 2


# Function to handle character movement
def move_character(character: Character, new_position: tuple):
	from math import sqrt
	x1, y1 = character.position
	x2, y2 = new_position
	distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	units_moved = distance / 5  # Since 1 unit = 5 cm
	if units_moved <= character.MR:
		character.position = new_position
		return f"{character.name} moves to position {character.position}."
	else:
		return f"{character.name} cannot move that far. Maximum movement range is {character.MR * 5} cm."


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

# Additional functions can be added to handle other game mechanics


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

	# Create characters
	attacker = Character(
		name="Warrior",
		player="Player 1",
		P=7,
		A=4,
		W=4,
		max_HP=17,
		HP=17,
		AP=9,
		MR=6,
		abilities=[],
		position=(0, 0)
	)

	defender = Character(
		name="Mage",
		player="Player 2",
		P=3,
		A=5,
		W=7,
		max_HP=13,
		HP=13,
		AP=13,
		MR=6,
		abilities=[],
		position=(10, 0)
	)

	# Attacker moves towards the defender
	print(move_character(attacker, (5, 0)))

	# Attacker attacks the defender
	print(attack(attacker, defender, attack_type='melee', defender_reaction='dodge'))

	# Defender uses an ability to heal
	healing_ability = Ability(
		name="Healing Touch",
		cost=2,
		description="Restore 3 HP to an ally within range.",
		effect=heal_ability
	)
	defender.abilities.append(healing_ability)
	print(use_ability(defender, healing_ability, target=defender))
