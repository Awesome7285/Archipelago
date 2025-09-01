from bs4 import BeautifulSoup as bs
import json

def modlist_html_to_json():
    with open('worlds/manual_ktanemodules_awesome7285/ignore/modlist.html', encoding='utf-8') as f:
        text = f.read()

    soup = bs(text, features='html.parser')

    mod_list = {}

    for mod in soup.find_all('div', {'class': 'mod-info'}):
        module_name, module_id = mod.find_all('div')
        mod_list[module_name.text] = module_id.text

    with open('worlds/manual_ktanemodules_awesome7285/ignore/modlist.json', 'w+', encoding='utf-8') as f:
        json.dump(mod_list, f, indent=4, ensure_ascii=False)
    # with open('worlds/manual_ktanemodules_awesome7285/data/modlist.json', 'w+', encoding='utf-8') as f:
    #     json.dump(list(mod_list.keys()), f, indent=4, ensure_ascii=False)
    
    return mod_list

def modlist_json_to_manual_json(mod_list:dict = None):
    if mod_list == None:
        with open('worlds/manual_ktanemodules_awesome7285/ignore/modlist.json', encoding='utf-8') as f:
            mod_list = json.load(f)
    
    itemsjson = {
        "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.items.schema.json",
        "data": []
    }
    locationsjson = {
	    "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.locations.schema.json",
        "data": [
            { "name": "Victory", "victory": True, "category": ["Victory"], "requires": "{victory_rule()}"}
        ]
    }
    regionsjson = {
        "Office": {
            "starting": True, "requires": [], "connects_to": []
        }
    }

    for i, mod in enumerate(mod_list.keys()):
        # Items
        mod_item = {
            "name": mod,
            "count": 0,
            "progression": True,
            "category": ["Module"]
        }

        itemsjson["data"].append(mod_item)

        # Locations
        mod_location = {
            "name": f"{mod} Solved",
            "requires": f"|{mod}|",
            #"region": mod,
            "category": ["Module"],
            "id": i+2
        }

        locationsjson["data"].append(mod_location)

        # Regions
        regionsjson[mod] = {
            "connects_to": [],
            "requires": f"|{mod}|"
        }

        regionsjson["Office"]["connects_to"].append(mod)


    with open('worlds/manual_ktanemodules_awesome7285/data/items.json', 'w', encoding='utf-8') as f:
        json.dump(itemsjson, f, indent=4, ensure_ascii=False)
    
    with open('worlds/manual_ktanemodules_awesome7285/data/locations.json', 'w', encoding='utf-8') as f:
        json.dump(locationsjson, f, indent=4, ensure_ascii=False)
    
    # with open('worlds/manual_ktanemodules_awesome7285/data/regions.json', 'w', encoding='utf-8') as f:
    #     json.dump(regionsjson, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    # Get modlist from modlist.html
    mod_list = modlist_html_to_json()

    # Turn mod list dict into manual's items.json and locations.json
    modlist_json_to_manual_json(mod_list)