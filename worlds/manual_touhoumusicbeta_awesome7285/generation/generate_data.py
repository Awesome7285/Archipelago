# This file is intended to be ran separately from the AP implementation.
# It will fill items.json and locations.json with a different dataset

import json

DIR = "worlds/manual_touhoumusicbeta_awesome7285/generation/"

class Archipelago:

    def __init__(self):
        self.items = []
        self.locations = []
        self.victory = {
            "name": "Victory",
            "requires": "{victory_rule()}",
            "victory": True
        }
        self.video_data = []


    def open_video_data(self, filename):
        self.video_data = json.load(filename)

    def add_location_basic(self, track, region = "Meme"):
        self.locations.append(
            {
                "name": f"{track['title']} ({track['url']})",
                "requires": f"|{track['user']}|",
                "region": region,
                "category": [f"Tracks by {track['user']}"]
            },
        )
    
    def add_item_composer(self, user):
        self.items.append(
            { 
                "name": user, 
                "count": 1, 
                "progression": True, 
                "category": ["Composer/Arranger"] 
            },
        )

    def check_name_for_characters(self):
        pass



if __name__ == "__main__":
    world = Archipelago
    world.open_video_data(DIR+"template_output.json")