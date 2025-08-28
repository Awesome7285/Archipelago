import os
import sys
import Utils
import asyncio
import multiprocessing
import configparser
import colorama

from CommonClient import CommonContext, server_loop, gui_enabled, get_base_parser
from .Items import item_table
from .Locations import location_table, stage_locations

INI_FILE = "tomtom4_ap.ini"

def clear_ini():
    if os.path.exists(INI_FILE):
        os.remove(INI_FILE)
    open(INI_FILE, "w").close()

def read_ini_section(section):
    config = configparser.ConfigParser()
    config.read(INI_FILE)
    return dict(config[section]) if section in config else {}

def write_ini(section, key, value):
    config = configparser.ConfigParser()
    if os.path.exists(INI_FILE):
        config.read(INI_FILE)
    if section not in config:
        config[section] = {}
    config[section][key] = str(value).lower()
    with open(INI_FILE, "w") as f:
        config.write(f)

class TomTom4Client(CommonContext):
    game = "TomTom Adventures Flaming Special"

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.checked_locations = set()

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = f"TomTom 4 Client"
        return ui

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd, args):
        super().on_package(cmd, args)

    def on_connected(self):
        self.send_connect()
        # Sync items you already have from the server into INI
        for item in self.items_received:
            self._apply_item_to_ini(item.item)
        # Optionally sync completed locations
        for loc_id in self.locations_checked:
            name = self.location_name(loc_id)
            self._apply_location_to_ini(name)

    def on_item(self, item):
        item_name = self.item_name(item.item)
        print(f"Received item: {item_name}")
        self._apply_item_to_ini(item_name)

    def on_tick(self):
        # Read completed locations from game
        complete_flags = read_ini_section("Complete")
        for lvl_str, value in complete_flags.items():
            if value.lower() == "true":
                loc_name = self._level_complete_name(int(lvl_str))
                if loc_name in location_table and loc_name not in self.checked_locations:
                    self.send_location_checks([location_table[loc_name]])
                    self.checked_locations.add(loc_name)

    def _apply_item_to_ini(self, item_name):
        if item_name.startswith("Level Access: "):
            lvl_id = self._stage_to_id(item_name.replace("Level Access: ", "") + " Complete")
            write_ini("Access", str(lvl_id), True)
        elif item_name == "Jump Power-Up":
            write_ini("Access", "jump", True)
        elif item_name == "Key":
            write_ini("Access", "key", True)
        elif item_name == "Hose":
            write_ini("Access", "hose", True)
        elif item_name in ("House Cleaned", "Tyler Defeated"):
            write_ini("Access", item_name.lower().replace(" ", "_"), True)

    def _apply_location_to_ini(self, location_name):
        lvl_id = self._stage_to_id(location_name)
        write_ini("Complete", str(lvl_id), True)

    def _stage_to_id(self, stage_name):
        # stage_name must match stage_locations entries
        return stage_locations.index(stage_name + " Complete") + 1

    def _level_complete_name(self, lvl_id):
        return stage_locations[lvl_id - 1]

    # def run_cli(self):
    #     import argparse
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument("server", help="Server address in the form host:port")
    #     parser.add_argument("name", help="Player name")
    #     parser.add_argument("--password", default="", help="Server password")
    #     args = parser.parse_args()

    #     clear_ini()
    #     self.server_address = args.server
    #     self.password = args.password
    #     self.auth = args.name
    #     self.connect()

    # def run_gui(self):
    #     from kvui import GameManager

    #     class BanjoTooieManager(GameManager):
    #         logging_pairs = [
    #             ("Client", "Archipelago")
    #         ]
    #         base_title = "Banjo-Tooie Client "+ version + " for AP"

    #     self.ui = BanjoTooieManager(self)
    #     self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

def main():
    Utils.init_logging("TomTom 4 Client")
    parser = get_base_parser()
    args = sys.argv[1:]
    if "TomTom 4 Client" in args:
        args.remove("TomTom 4 Client")
    args = parser.parse_args(args)

    async def _main():
        multiprocessing.freeze_support()
        ctx = TomTom4Client(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await ctx.exit_event.wait()
        ctx.server_address = None
        await ctx.shutdown()

    colorama.init()
    asyncio.run(_main())
    colorama.deinit()

if __name__ == "__main__":
    main()
