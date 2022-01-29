import json

with open('steam.json') as json_file:
    data = json.load(json_file)

teller = -1
def eerste_spel_naam():
    spel = data[teller]
    for i in spel:
        if 'name' in i:
            naam = spel[i]
    return naam

def eerste_spel_info():
    global teller
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
    teller +=1
    return info

def steam_sort():
    lijst = sorted(data,key=lambda i: i['price'])
    #,reverse=True om om te keren --- price veranderen in iets anders om daarop te sorteren
    return lijst

# def search():
#     for i in data:


def rating():
    global teller
    spel = data[teller]
    for i in spel:
        if "positive_ratings" in i:
            positive = spel[i]
        if "negative_ratings" in i:
            negative = spel[i]
    totaal = positive + negative
    rating = positive/totaal
    if rating > 0 and rating <= 0.125:
        lampjes = 1
    elif rating > 0.125 and rating <= 0.25:
        lampjes = 2
    elif rating > 0.25 and rating <= 0.375:
        lampjes = 3
    elif rating > 0.375 and rating <= 0.5:
        lampjes = 4
    elif rating > 0.5 and rating <= 0.625:
        lampjes = 5
    elif rating > 0.625 and rating <= 0.75:
        lampjes = 6
    elif rating > 0.75 and rating <= 0.875:
        lampjes = 7
    elif rating > 0.875 and rating <= 1:
        lampjes = 8
    return lampjes
