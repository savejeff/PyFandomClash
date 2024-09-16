from dataclasses import dataclass, field
from typing import List, Optional



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
	position: tuple = (0, 0)  # (x, y) coordinates in grid units
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
