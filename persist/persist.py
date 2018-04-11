from pymongo import MongoClient
import requests, utils

client = MongoClient() 
db = client['sports']

sports = ['baseball', 'basketball', 'football']

for sport in sports:
    collection = db[sport]

    r = requests.get(url = 'http://api.cbssports.com/fantasy/players/list', params = {'version':'3.0', 'SPORT': sport, 'response_format':'JSON'})
    players = r.json()['body']['players']
    
    for player in players:
        if not utils.vars_exist(player): continue 

        payload = {
            'id': player['id'],
            'name_brief':   utils.get_name_brief(sport,player),
            'first_name':   player['firstname'],
            'last_name':    player['lastname'],
            'position':     player['position'],
            'age':          player['age']
        }
        
        #check for duplicate data
        player_info = collection.find(payload)

        if player_info.count() == 0: 
            collection.insert(payload)        
    