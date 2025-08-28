from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.

# Victory Rule
def victory_rule(world: World):
    """Calculates Victory"""
    comp = world.options.completion_percentage.value
    total = world.options.total_modules.value

    needed = round((comp / 100) * total)

    logic = f"|@Module:{needed}|"

    return logic
