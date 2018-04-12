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

        player_info = {
            'id': player.id,
            'name_brief':   utils.get_name_brief(sport,player),
            'first_name':   player.firstname,
            'last_name':    player.lastname,
            'position':     player.position,
            'age':          player.age
        }

        initial_position_info = {
            'position_info': {
                'position': player.position,
                'players': 1,
                'age_total': player.age,
                'age_avg' : player.age
            }
        }

        utils.insert(collection, player_info)
        utils.insert(collection, initial_position_info)