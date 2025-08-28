from BaseClasses import MultiWorld, Region, Entrance
from .Locations import TomTom4Location, stage_locations, extra_locations, location_table

def create_regions(world: MultiWorld, player: int):
    # Menu region
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    # Store all entrances from Menu for use in Rules.py
    world.menu_entrances = {}

    # Create each world region and connect it from Menu
    for stage_name in stage_locations:
        base_name = stage_name.replace(" Complete", "")
        region = Region(base_name, player, world)

        # Add the "Complete" location
        region.locations.append(
            TomTom4Location(player, stage_name, location_table[stage_name], region)
        )

        # Add any extra locations for this world
        if base_name in extra_locations:
            for loc_name in extra_locations[base_name]:
                region.locations.append(
                    TomTom4Location(player, loc_name, location_table[loc_name], region)
                )

        # Add region to the world
        world.regions.append(region)

        # Create an entrance from Menu to this stage
        entrance = Entrance(player, f"To {base_name}", menu)
        menu.exits.append(entrance)
        entrance.connect(region)

        # Save the entrance for Rules.py
        world.menu_entrances[base_name] = entrance


# def create_regions(world: MultiWorld, player: int):
#     world.regions.append(Region("Menu", player, world))

#     # Worlds
#     region_world_1: Region = Region("Underground World", player, world)
#     region_world_1.locations += [TomTom4Location(player, "Underground World Complete",
#                                                  section1_table["Section 1 Completed"], region_section_1)]
#     world.regions.append(region_section_1)

#     # Bomb sections
#     region_section_1: Region = Region("Section 1", player, world)
#     region_section_1.locations += [KTANELocation(player, "Section 1 Completed",
#                                                  section1_table["Section 1 Completed"], region_section_1)]
#     world.regions.append(region_section_1)

#     region_section_2: Region = Region("Section 2", player, world)
#     region_section_2.locations += [KTANELocation(player, "Section 2 Completed",
#                                                  section2_table["Section 2 Completed"], region_section_2)]
#     world.regions.append(region_section_2)

#     region_section_3: Region = Region("Section 3", player, world)
#     region_section_3.locations += [KTANELocation(player, "Section 3 Completed",
#                                                  section3_table["Section 3 Completed"], region_section_3)]
#     world.regions.append(region_section_3)

#     region_section_4: Region = Region("Section 4", player, world)
#     region_section_4.locations += [KTANELocation(player, "Section 4 Completed",
#                                                  section4_table["Section 4 Completed"], region_section_4)]
#     world.regions.append(region_section_4)

#     region_section_5: Region = Region("Section 5", player, world)
#     region_section_5.locations += [KTANELocation(player, "Section 5 Completed",
#                                                  section5_table["Section 5 Completed"], region_section_5)]
#     world.regions.append(region_section_5)

#     region_section_6: Region = Region("Section 6", player, world)
#     world.regions.append(region_section_6)

#     # Bombs
#     region_bomb_11: Region = Region("Bomb 1.1", player, world)
#     for locationKey in [x for x in section1_table if x[0:3] == "1.1"]:
#         location = KTANELocation(player, locationKey, section1_table[locationKey], region_bomb_11)
#         region_bomb_11.locations += [location]
#     world.regions.append(region_bomb_11)

#     region_bomb_21: Region = Region("Bomb 2.1", player, world)
#     for locationKey in [x for x in section2_table if x[0:3] == "2.1"]:
#         location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_21)
#         region_bomb_21.locations += [location]
#     world.regions.append(region_bomb_21)

#     region_bomb_22: Region = Region("Bomb 2.2", player, world)
#     for locationKey in [x for x in section2_table if x[0:3] == "2.2"]:
#         location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_22)
#         region_bomb_22.locations += [location]
#     world.regions.append(region_bomb_22)

#     region_bomb_23: Region = Region("Bomb 2.3", player, world)
#     for locationKey in [x for x in section2_table if x[0:3] == "2.3"]:
#         location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_23)
#         region_bomb_23.locations += [location]
#     world.regions.append(region_bomb_23)

#     region_bomb_24: Region = Region("Bomb 2.4", player, world)
#     for locationKey in [x for x in section2_table if x[0:3] == "2.4"]:
#         location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_24)
#         region_bomb_24.locations += [location]
#     world.regions.append(region_bomb_24)

#     region_bomb_25: Region = Region("Bomb 2.5", player, world)
#     for locationKey in [x for x in section2_table if x[0:3] == "2.5"]:
#         location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_25)
#         region_bomb_25.locations += [location]
#     world.regions.append(region_bomb_25)

#     region_bomb_26: Region = Region("Bomb 2.6", player, world)
#     for locationKey in [x for x in section2_table if x[0:3] == "2.6"]:
#         location = KTANELocation(player, locationKey, section2_table[locationKey], region_bomb_26)
#         region_bomb_26.locations += [location]
#     world.regions.append(region_bomb_26)

#     region_bomb_31: Region = Region("Bomb 3.1", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.1"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_31)
#         region_bomb_31.locations += [location]
#     world.regions.append(region_bomb_31)

#     region_bomb_32: Region = Region("Bomb 3.2", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.2"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_32)
#         region_bomb_32.locations += [location]
#     world.regions.append(region_bomb_32)

#     region_bomb_33: Region = Region("Bomb 3.3", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.3"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_33)
#         region_bomb_33.locations += [location]
#     world.regions.append(region_bomb_33)

#     region_bomb_34: Region = Region("Bomb 3.4", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.4"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_34)
#         region_bomb_34.locations += [location]
#     world.regions.append(region_bomb_34)

#     region_bomb_35: Region = Region("Bomb 3.5", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.5"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_35)
#         region_bomb_35.locations += [location]
#     world.regions.append(region_bomb_35)

#     region_bomb_36: Region = Region("Bomb 3.6", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.6"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_36)
#         region_bomb_36.locations += [location]
#     world.regions.append(region_bomb_36)

#     region_bomb_37: Region = Region("Bomb 3.7", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.7"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_37)
#         region_bomb_37.locations += [location]
#     world.regions.append(region_bomb_37)

#     region_bomb_38: Region = Region("Bomb 3.8", player, world)
#     for locationKey in [x for x in section3_table if x[0:3] == "3.8"]:
#         location = KTANELocation(player, locationKey, section3_table[locationKey], region_bomb_38)
#         region_bomb_38.locations += [location]
#     world.regions.append(region_bomb_38)

#     region_bomb_41: Region = Region("Bomb 4.1", player, world)
#     for locationKey in [x for x in section4_table if x[0:3] == "4.1"]:
#         location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_41)
#         region_bomb_41.locations += [location]
#     world.regions.append(region_bomb_41)

#     region_bomb_42: Region = Region("Bomb 4.2", player, world)
#     for locationKey in [x for x in section4_table if x[0:3] == "4.2"]:
#         location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_42)
#         region_bomb_42.locations += [location]
#     world.regions.append(region_bomb_42)

#     region_bomb_43: Region = Region("Bomb 4.3", player, world)
#     for locationKey in [x for x in section4_table if x[0:3] == "4.3"]:
#         location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_43)
#         region_bomb_43.locations += [location]
#     world.regions.append(region_bomb_43)

#     region_bomb_44: Region = Region("Bomb 4.4", player, world)
#     for locationKey in [x for x in section4_table if x[0:3] == "4.4"]:
#         location = KTANELocation(player, locationKey, section4_table[locationKey], region_bomb_44)
#         region_bomb_44.locations += [location]
#     world.regions.append(region_bomb_44)

#     region_bomb_51: Region = Region("Bomb 5.1", player, world)
#     for locationKey in [x for x in section5_table if x[0:3] == "5.1"]:
#         location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_51)
#         region_bomb_51.locations += [location]
#     world.regions.append(region_bomb_51)

#     region_bomb_52: Region = Region("Bomb 5.2", player, world)
#     for locationKey in [x for x in section5_table if x[0:3] == "5.2"]:
#         location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_52)
#         region_bomb_52.locations += [location]
#     world.regions.append(region_bomb_52)

#     region_bomb_53: Region = Region("Bomb 5.3", player, world)
#     for locationKey in [x for x in section5_table if x[0:3] == "5.3"]:
#         location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_53)
#         region_bomb_53.locations += [location]
#     world.regions.append(region_bomb_53)

#     region_bomb_54: Region = Region("Bomb 5.4", player, world)
#     for locationKey in [x for x in section5_table if x[0:3] == "5.4"]:
#         location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_54)
#         region_bomb_54.locations += [location]
#     world.regions.append(region_bomb_54)

#     region_bomb_55: Region = Region("Bomb 5.5", player, world)
#     for locationKey in [x for x in section5_table if x[0:3] == "5.5"]:
#         location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_55)
#         region_bomb_55.locations += [location]
#     world.regions.append(region_bomb_55)

#     region_bomb_56: Region = Region("Bomb 5.6", player, world)
#     for locationKey in [x for x in section5_table if x[0:3] == "5.6"]:
#         location = KTANELocation(player, locationKey, section5_table[locationKey], region_bomb_56)
#         region_bomb_56.locations += [location]
#     world.regions.append(region_bomb_56)

#     world.regions.append(Region("Bomb 6.1", player, world))
