from data_structures import *
from util import *
from util_modifiers import *
from terminal_helper import *
from character_creator import *



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

	if True:

		# Example abilities
		def fireball_effect(user: Character, targets: List[Character]):
			damage = user.W + 2
			result = []
			for target in targets:
				target.HP -= damage
				if target.HP < 0:
					target.HP = 0
				result.append(f"{target.name} takes {damage} fire damage and has {target.HP} HP left.")
			return ' '.join(result)


		fireball_ability = Ability(
			name="Fireball",
			cost=3,
			description="Deal W + 2 damage to all enemies within 2 units of target area.",
			effect=fireball_effect
		)


		def healing_touch_effect(user: Character, target: Character):
			heal_amount = 3
			target.HP += heal_amount
			if target.HP > target.max_HP:
				target.HP = target.max_HP
			return f"{user.name} heals {target.name} for {heal_amount} HP."


		healing_touch_ability = Ability(
			name="Healing Touch",
			cost=2,
			description="Restore 3 HP to yourself or an ally within range.",
			effect=healing_touch_effect
		)

		# Example items
		healing_potion = Item(
			name="Healing Potion",
			item_type="consumable",
			description="Restores 2 HP when used.",
			effect=healing_potion_effect
		)

		# Create the character
		mage_character = create_character(
			name="Elwyn the Mage",
			player="Alice",
			P=3,
			A=5,
			W=7,
			abilities=[fireball_ability, healing_touch_ability],
			items=[healing_potion],
			size='Medium',
			position=(2, 3),
			fandom_trait='Fantasy',
			role='Support'  # Grants +1 W
		)

		# Print the character's status sheet
		print_character_status(mage_character)

	if False:

		# Create characters
		unit0_attacker = Character(
			name="Warrior",
			player="Player 1",
			P=7, A=4, W=4,
			max_HP=17,
			HP=17, AP=9, MR=6,
			abilities=[],
			position=(0, 0)
		)

		unit1_defender = Character(
			name="Mage",
			player="Player 2",
			P=3, A=5, W=7,
			max_HP=13,
			HP=13, AP=13, MR=6,
			abilities=[],
			position=(10, 0)
		)

		print_character_status(unit0_attacker)
		print_character_status(unit1_defender)

		# Attacker moves towards the defender
		print(move_character(unit0_attacker, (5, 0)))

		# Attacker attacks the defender
		print(attack(unit0_attacker, unit1_defender, attack_type='melee', defender_reaction='dodge'))

		# Defender uses an ability to heal
		healing_ability = Ability(
			name="Healing Touch",
			cost=2,
			description="Restore 3 HP to an ally within range.",
			effect=heal_ability
		)
		unit1_defender.abilities.append(healing_ability)
		print(use_ability(unit1_defender, healing_ability, target=unit1_defender))
