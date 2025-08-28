from BaseClasses import Item

BASE_ID = 2247200

class TomTom4Item(Item):
    game: str = "TomTom Adventures Flaming Special"

stage_items = [
    "Level Access: Dirty World",
    "Level Access: Desert World",
    "Level Access: School",
    "Level Access: Above the Clouds",
    "Level Access: Snow World",
    "Level Access: Space World",
    "Level Access: Condensed Milk World",
    "Level Access: Rumi's Palace",
    "Level Access: Fire Hydrent World",
    "Level Access: Maze World",
    "Level Access: Mars",
    "Level Access: Jungle World",
    "Level Access: Tetris World",
    "Level Access: Christmas World",
    "Level Access: The Jungle Inferno",
    "Level Access: Mexico",
    "Level Access: Pythag World",
    "Level Access: Lava World",
    "Level Access: Purple Abyss",
    "Level Access: The End",
    "Level Access: Bridge World"
]

other_items = [
    "Jump Power-Up",
    "Key",
    "Hose"
]

victory_items = [
    "Tyler Defeated",
    "House Cleaned"
]

filler_items = [
    "Life",
    "Declan Power-Up"
]

all_items = stage_items + other_items + victory_items + filler_items

item_table = {name: id for id, name in enumerate(all_items, BASE_ID)}

#Name classification:
#713 01 001
#713 Auth
#01 Game
#001 itemID

# modules_item_table = {
#     "Complicated Wires": 71301001,
#     "Maze": 71301002,
#     "Memory": 71301003,
#     "Morse Code": 71301004,
#     "Password": 71301005,
#     "Simon Says": 71301006,
#     "Who's on First": 71301007,
#     "Wire Sequence": 71301008,
#     "Capacitor": 71301009,
#     "Knob": 71301010,
#     "Vent Gas": 71301011
# }

# modules_item_nohl_table = {
#     "Complicated Wires": 71301001,
#     "Maze": 71301002,
#     "Memory": 71301003,
#     "Morse Code": 71301004,
#     "Password": 71301005,
#     "Simon Says": 71301006,
#     "Who's on First": 71301007,
#     "Wire Sequence": 71301008,
#     "Knob": 71301010
# }

# other_progression_items = {
#     "Bomb Fragment": 71301012,
#     "Time++": 71301013
# }

# useful_items = {
#     "Time+": 71301014
# }

# filler_item = {
#     "Strike+": 71301015
# }

# item_table = {
#     **modules_item_table, **other_progression_items, **useful_items, **filler_item
# }