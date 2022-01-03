import json

with open('steam.json') as json_file:
    data = json.load(json_file)

teller = 0
def eerste_spel_naam():
    spel = data[teller]
    for i in spel:
        if 'name' in i:
            naam = spel[i]
    return naam

def eerste_spel_info():
    spel = data[teller]
    for i in spel:
        if 'appid' in i:
            app_id = 'AppID:' + str(spel[i])
        if 'release_date' in i:
            release_date = 'Release_date:' + str(spel[i])
        if 'genres' in i:
            genre = 'Genre:' + str(spel[i])
        if 'price' in i:
            price = 'Price:' + str(spel[i])
    info = app_id + '\n' + release_date + '\n' + genre + '\n' + price
    return info

def steam_sort():
    lijst = sorted(data,key=lambda i: i['price'])
    #,reverse=True om om te keren --- price veranderen in iets anders om daarop te sorteren
    return lijst