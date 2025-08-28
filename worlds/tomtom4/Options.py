from dataclasses import dataclass
from Options import Option, Choice, DefaultOnToggle, Toggle, PerGameCommonOptions, DeathLink

class Goal(Choice):
	"""Determine what is needed to be done to complete your goal."""
	display_name = "Goal"
	option_hose = 0
	option_tyler = 1
	option_both = 2
	default = 0

class Roomsanity(Toggle):
    """Makes each individual level's rooms a check for completing them."""
    display_name = "Roomsanity"


@dataclass
class TomTom4Options(PerGameCommonOptions):
    goal: Goal
    roomsanity: Roomsanity
    death_link: DeathLink
