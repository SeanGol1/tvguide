import tmdbsimple as tmdb
import json
import requests


pages = ['&page=1','&page=2', '&page=3', '&page=4', '&page=5']
upcoming = []
thisweek = ''
favourites = ['Superman & Lois', 'Greys Anatomy', 'Legacies', 'Loki', "DC's legends of tomorrow", 'The Flash', 'Clarksons Farm', "America's Got Talent", 'The voice']


for items in pages:

    url2 = "https://api.themoviedb.org/3/tv/on_the_air?api_key=74d5287b6bd749f76603010fdcf24585&language=en-US"+str(items)
 
    request2 = requests.get(url2)
    dict = request2.json()
    
    for i in dict.get('results'):
        y = i["name"]
        if y in favourites:
            upcoming.append(y)
            thisweek += y +'\n'

print ('Shows airing this week:\n' + thisweek)  # On computer
#print (upcoming)  # On Raspberry Pi 






