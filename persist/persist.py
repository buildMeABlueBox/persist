from pymongo import MongoClient
import requests

#name_brief doesn't work without first and last name.
def names_exist(player):
    return not player['firstname'] or not player['lastname']

#return format for name brief for specific sport
def get_name_brief(sport, player):
    firstname = player['firstname']
    lastname = player['lastname']
    if(sport == 'baseball'):    return firstname[0] + '. ' + lastname[0] + '.'
    if(sport == 'basketball'):  return firstname +' ' + lastname[0] + '.'
    if(sport == 'football'):    return firstname[0] + '. ' + lastname

client = MongoClient() 
sports = ['baseball', 'basketball', 'football']

for sport in sports:
    r = requests.get(url = 'http://api.cbssports.com/fantasy/players/list', params = {'version':'3.0', 'SPORT': sport, 'response_format':'JSON'})
    players = r.json()['body']['players']

    for player in players:
        if not names_exist(player): continue 
        
        payload = {
            'id': player['id'],
            'name_brief':   get_name_brief(),
            'first_name':   player['firstname'],
            'last_name':    player['lastname'],
            'position':     player['position'],
            'age':          player['age']
        }

    