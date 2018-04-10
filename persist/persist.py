from pymongo import MongoClient
import requests, utils

client = MongoClient() 
sports = ['baseball', 'basketball', 'football']

for sport in sports:
    r = requests.get(url = 'http://api.cbssports.com/fantasy/players/list', params = {'version':'3.0', 'SPORT': sport, 'response_format':'JSON'})
    players = r.json()['body']['players']
    print(sport.upper()+'\n')
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

        print(payload)
    