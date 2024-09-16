from data_structures import *

def create_character(
	name: str,
	player: str,
	P: int,
	A: int,
	W: int,
	abilities: list[Ability],
	items: list[Item],
	size: str = 'Medium',  # 'Small', 'Medium', 'Large'
	position: tuple = (0, 0),  # Starting position in grid units
	fandom_trait: Optional[str] = None,  # e.g., 'Anime', 'Superhero'
	role: Optional[str] = None  # e.g., 'Warrior', 'Ranger'
) -> Character:
	"""
	Creates and returns a Character instance with calculated derived stats.
	"""

	# Validate core stats
	if not P + A + W == 15:
		raise ValueError("Core stats P, A, and W must sum up to 15")
	if not (3 <= P <= 7) or not (3 <= A <= 7) or not (3 <= W <= 7):
		raise ValueError("Core stats P, A, and W must be between 3 and 7.")

	# Calculate derived stats
	max_HP = 10 + P
	AP = 5 + W
	MR = 1 + (A // 2)  # Movement Range in grid units

	# Apply size modifiers
	if size == 'Large':
		max_HP += 2
		MR -= 1
	elif size == 'Small':
		max_HP -= 1
		MR += 1
	# Medium size has no modifiers

	# Apply role bonuses
	temp_P = 0
	temp_A = 0
	temp_W = 0
	if role == 'Warrior':
		P += 1
	elif role == 'Ranger':
		W += 1
	elif role == 'Scout':
		A += 1
	elif role == 'Support':
		W += 1
	# Add other roles as needed

	# Initialize the Character instance
	character = Character(
		name=name,
		player=player,
		P=P, A=A, W=W,
		max_HP=max_HP,
		HP=max_HP, AP=AP, MR=MR,
		abilities=abilities,
		items=items,
		size=size,
		position=position,
		fandom_trait=fandom_trait,
		role=role,
		temp_HP=0,
		temp_A=temp_A,
		temp_P=temp_P,
		temp_W=temp_W
	)

	return character
