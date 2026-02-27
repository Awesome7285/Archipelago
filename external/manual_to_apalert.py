import json

DIR = "./worlds/manual_thmusic_awesome7285/data/items.json"
OUTPUT = 'external/out.txt'

with open(DIR, encoding='utf-8') as f:
    data = json.load(f)

with open(OUTPUT, 'w+', encoding='utf-8') as f:

    for item in data:
        for typ in ['progression', 'trap', 'filler', 'useful']:
            if item.get(typ, None):
                f.write(f'{item['name']}: {typ}\n')
                break