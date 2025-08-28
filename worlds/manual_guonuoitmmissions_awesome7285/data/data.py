import json

def regions_to_json(data):
    level = "1.1"
    if "Level" in data[0]:
        level = data[0][5:].strip()

    modules = []
    for line in data[2:]:
        if not ("Pooled" in line or "Chapter" in line):
            modules.append(line.strip())

    output = '"' + level + '": {\n        "connects_to": [],\n        "requires": "|Bomb Fragment:23|'
    for module in modules:
        output += f" AND |{module}|"
    output += '"\n    },'

    return output

def locations_to_json(data):
    # level = "1.1"
    # if "Level" in data[0]:
    #     level = data[0][5:].strip()

    # name = data[1] #hope
    main = "3."
    out = '    '
    for i, name in enumerate(data):
        out += '{ ' + f'"name": "{main}{i+1} {name}:  Solved", "region": "{main}{i+1}", "category": ["{main}{i+1} {name}"] ' + '},\n    '
        out += '{ ' + f'"name": "{main}{i+1} {name}: Bomb Defused", "region": "{main}{i+1}", "category": ["{main}{i+1} {name}"] ' + '},\n\n    '

    print(out)



if __name__ == "__main__":
    data = """
Counting Solves	The Crucible	Intersection of Circles	My Lil' Possibly Impossible	Housemaiden	A Way to Go	Lost in Limbo	Point of View	Finding Clues	Answering Machine	Pick Up the Math	My Lil' Easy Challenge	Fight Under the Broken Sky
"""

    data = data.strip()
    data = data.split('\t')

    print(locations_to_json(data))