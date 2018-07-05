from pymongo import MongoClient
import requests, utils

#uri = f'mongodb://akamat-mongo:{primary_password}@akamat-mongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
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
            'name_brief':   utils.get_name_brief(sport,player),
            'first_name':   player['firstname'],
            'last_name':    player['lastname'],
            'position':     player['position'],
            'age':          player['age'],
            'id':           player['id']
        }

        initial_position_info = {
            'position_info': {
                'position': player['position'],
                'players': 1,
                'age_total': player['age'],
                'avg_age' : player['age']
            }
        }

        utils.insert(collection, player_info, player_info) #insert player if they don't already exist

        pos_query = {'position_info.position': player['position']}
        pos_inserted = utils.insert(collection, initial_position_info, pos_query) #try inserting position info object

        if not pos_inserted: # position info object already exists in DB
            utils.update_position(collection, pos_query, player)