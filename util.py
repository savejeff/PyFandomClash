import random

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

