from data_structures import *
from util import *


ATTACK_TYPE_MELEE = "melee"
ATTACK_TYPE_RANGED = "ranged"

DEFEND_REACTION_DODGE = "dodge"
DEFEND_REACTION_BLOCK = "block"

TypeDefendReaction = str


# Function to handle attacks
def attack(attacker: Character, defender: Character, attack_type=ATTACK_TYPE_MELEE, defender_reaction: Optional[TypeDefendReaction] = None):
	# Determine attack and defense stats
	if attack_type == ATTACK_TYPE_MELEE:
		attack_stat = attacker.P + attacker.temp_P
		base_damage = attacker.P + attacker.temp_P
	elif attack_type == ATTACK_TYPE_RANGED:
		attack_stat = attacker.W + attacker.temp_W
		base_damage = attacker.W + attacker.temp_W
	else:
		return "Invalid attack type."

	# Attacker's roll
	attack_roll = average_roll_2d6() + attack_stat

	# Defender's roll and reaction
	defense_stat = defender.A + defender.temp_A
	if defender_reaction == DEFEND_REACTION_DODGE and defender.AP >= 1:
		defender.AP -= 1
		defense_roll = roll_with_advantage() + defense_stat
	elif defender_reaction == DEFEND_REACTION_BLOCK and defender.AP >= 1:
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
			return ability.effect(user, target, [])
		else:
			return f"{user.name} uses {ability.name}."
	else:
		return f"{user.name} does not have enough AP to use {ability.name}."


# Example ability effect functions
def heal_ability(user: Character, target: Character, heal_amount : int):
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




if __name__ == '__main__':

	from character_creator import create_character

	res = []
	for i in range(1000):
		#print(f"Attempt #{i}")

		CharDev1 = create_character(CHARACTER_DEV1,
			PLAYER_DEV1,
			P=7, A=5, W=3,
			size= FIGURE_SIZE_LARGE,
			fandom_trait=FANDOM_ANIME,
			role=ROLE_WARRIOR
		)

		CharDev2 = create_character(CHARACTER_DEV2,
			PLAYER_DEV2,
			P=5, A=7, W=3,
			size= FIGURE_SIZE_SMALL,
			fandom_trait=FANDOM_ANIME,
			role=ROLE_SUPPORT
		)

		attack_count = 0
		while CharDev2.HP > 0:
			attack_count += 1
			CharDev2.AP = 10
			#print
			(
				attack(CharDev1, CharDev2, ATTACK_TYPE_MELEE, defender_reaction=DEFEND_REACTION_BLOCK)
			)
		res.append(attack_count)

	print(res)

	print(f"Avg: {sum(res) / len(res)}")
