from data_structures import *

"""
	• Warrior:
		○ Bonus: +1 P
		○ Ability: "Battle Aura" – Allies within 3 units gain +1 P (always active)
	• Ranger:
		○ Bonus: +1 W
		○ Ability: "Sharpshooter" – Ignore cover penalties for ranged attacks. (always active)
	• Scout:
		○ Bonus: +1 A
		○ Ability: "Quick Reflexes" – 3 times per Game, reroll one die during a movement or defense test.
	• Support:
		○ Bonus: +1 W
		○ Ability: "Healing Touch" – Spend 2 AP to restore 3 HP to an ally within 3 units.

"""


def ask(question, options, multi_answer: bool) -> int | list[int]:
	print(question)
	for i, opt in enumerate(options):
		print(f"{i}. {options}")

	answer_str = input()
	if multi_answer:
		return [int(ma.strip()) for ma in answer_str.split(",")]
	else:
		return int(answer_str.strip())


def ability_battle_aura(char_user: Character, char_target: Character, char_rest: list[Character]):
	"""
	Allies within 3 units gain +1 P (always active after usage)
	:param char_user:
	:param char_target:
	:param char_rest:
	:return:
	"""
	targets_i = ask("What Allies are within of 3 units", [char.name for char in char_rest], True)
	for char in [char_rest[i] for i in targets_i]:
		char.P += 1


def bonus_warrior(char: Character):
	char.P += 1


Role_Warrior = Role(
	"Warrior",
	Ability(
		name = "Battle Aura",
		cost = 2,
		description = "Allies within 3 units gain +1 P (always active after usage)",
		effect = ability_battle_aura
	),
	bonus = bonus_warrior
)

