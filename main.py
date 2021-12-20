import json

with open('steam.json') as json_file:
    data = json.load(json_file)

def eerste_spel_naam():
    spel = data[0]
    for i in spel:
        if 'name' in i:
            naam = spel[i]
    return naam