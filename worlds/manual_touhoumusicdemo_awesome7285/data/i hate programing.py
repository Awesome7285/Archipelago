import json
with open('data/locations.json') as f:
    data= json.load(f)

def change():
    c = ""
    j = -1
    g=[1,2,3,4,5,6,7,7.5,8,9,9.5,10,10.5,11,12,12.3,12.5,12.8,13,13.5,14,14.3,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,101,102,103,104,105,105.5,106,107,108,109,109.5,110,201,202,203,204,205,206,207,208,209,210,211,212,213,214]

    for i in data:
        if i["category"][0] != c:
            j+=1
            c = i["category"][0]
        p = str(g[j]+100)
        if float(p) > 300:
            p = "PW" + p
            p = p[:2]+p[3:]
        elif float(p) > 200:
            p = "MC" + p
            p = p[:2]+p[3:]
        else:
            p = p[1:]
        i["category"] = [p + " - " + i["category"][0]]

    with open('data/locations.json', 'w+') as f:
        json.dump(data, f)

def save_to_text():
    l = [i["requires"] for i in data]
    with open('data/out.txt', 'w+') as f:
        f.write('\n'.join(l))

def load_from_text():
    with open('data/requirements.txt') as f:
        for i, line in enumerate(f):
            if line.strip() != "":
                data[i]["requires"] += " AND |" + line.strip() + "|"
    with open('data/locations.json', 'w') as f:
        json.dump(data, f, indent=4)

load_from_text()