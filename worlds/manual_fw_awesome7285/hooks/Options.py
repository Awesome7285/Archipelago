# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class NumberLifeMid(Range):
    """Number of lives the randomizer expects you to have before facing Nareko and Yuiman"""
    display_name = "Number of lives expected in order to face Nareko and Yuiman"
    range_start = 0
    range_end = 8
    default = 3

class NumberBombsMid(Range):
    """Number of bombs the randomizer expects you to have before facing Nareko and Yuiman"""
    display_name = "Number of bombs expected in order to face Nareko and Yuiman"
    range_start = 0
    range_end = 8
    default = 2

class DifficultyMid(Choice):
    """The difficulty expected in order to face Nareko and Yuiman (Starting from Lunatic and goes to Easy)"""
    display_name = "Difficulty in order to face Nareko and Yuiman"
    option_lunatic = 0
    option_hard = 1
    option_normal = 2
    option_easy = 3
    default = 1

class NumberLifeEnd(Range):
    """Number of lives the randomizer expects you to have before facing Toyohime and Ariya"""
    display_name = "Number of lives expected in order to face Toyohime and Ariya"
    range_start = 0
    range_end = 8
    default = 3

class NumberBombsEnd(Range):
    """Number of bombs the randomizer expects you to have before facing Toyohime and Ariya"""
    display_name = "Number of bombs expected in order to face Toyohime and Ariya"
    range_start = 0
    range_end = 8
    default = 2

class DifficultyEnd(Choice):
    """The difficulty expected in order to face Toyohime and Ariya (Starting from Lunatic and goes to Easy)"""
    display_name = "Difficulty in order to face Toyohime and Ariya"
    option_lunatic = 0
    option_hard = 1
    option_normal = 2
    option_easy = 3
    default = 1

class EndingRequired(Range):
    """How many endings are required to finish the game"""
    display_name = "How many endings are required to finish the game"
    range_start = 1
    range_end = 2
    default = 2


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["number_life_mid"] = NumberLifeMid
    options["number_bomb_mid"] = NumberBombsMid
    options["difficulty_mid"] = DifficultyMid
    options["number_life_end"] = NumberLifeEnd
    options["number_bomb_end"] = NumberBombsEnd
    options["difficulty_end"] = DifficultyEnd
    options["ending_required"] = EndingRequired
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
