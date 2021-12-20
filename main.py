import json

with open('steam.json') as json_file:
    data = json.load(json_file)

def eerste_spel_naam():
    spel = data[0]
    for i in spel:
        if 'name' in i:
            naam = spel[i]
    return naam

def steam_sort():
    lijst = sorted(data,key=lambda i: i['price'])
    #,reverse=True om om te keren --- price veranderen in iets anders om daarop te sorteren
    return lijst



