import tmdbsimple as tmdb
import json
import requests

data_fetch = True
pages = ['&page=1', '&page=2', '&page=3']
count = 0
todays_shows = []
our_shows = []
favourites = ['Superman & Lois', 'Emmerdale', 'WWE Raw']

for items in pages:

    if count >= 3:
        break
    
    page_number = pages[0]

    tmdb.api_key = "74d5287b6bd749f76603010fdcf24585"   
    url = "https://api.themoviedb.org/3/tv/airing_today?api_key=74d5287b6bd749f76603010fdcf24585&language=en-US"+str(items)
    count += 1


    request = requests.get(url)
    json = request.json()
       
    for i in json.get('results'):
        y = i["name"]
        if y in favourites:
            todays_shows.append(y)

  
print(todays_shows)


